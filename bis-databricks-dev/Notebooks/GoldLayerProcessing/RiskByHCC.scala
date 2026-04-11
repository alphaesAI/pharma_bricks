// Databricks notebook source
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

import  org.apache.hadoop.fs.{FileSystem,Path}

def path_exists(pathToCheck: String): Boolean =
{ 
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val IsExists = fs.exists(new org.apache.hadoop.fs.Path(pathToCheck)) 
  return IsExists 
}

// COMMAND ----------

// get client container
dbutils.widgets.text("ClientContainer","","")
val clientContainer = dbutils.widgets.get("ClientContainer")
val mountPoint = "/mnt/"
val fileLocations = mountPoint + clientContainer + "/"

// COMMAND ----------

// load all file dependencies
class FileDependency (val location: String, val viewName: String, val format: String) {}


val dependencies: Array[FileDependency] = Array(
    new FileDependency("Gold/MA/PEC/providerGroupReference", "ProviderGroupReference", "delta"),
    new FileDependency("Gold/MA/Client/Member", "Member", "delta"),
    new FileDependency("Gold/MA/Client/Provider", "Provider", "delta"),
    new FileDependency("Gold/MA/Risk/CacheSuspectAnalysis", "CacheSuspectAnalysis", "delta"),
    new FileDependency("Gold/MA/Risk/CacheSuspectAnalysisHistory", "CacheSuspectAnalysisHistory", "delta"),
    new FileDependency("Gold/MA/Risk/ChaseProviderList", "ChaseProviderList", "delta"),
    new FileDependency("Gold/MA/Risk/MAO004Diagnosis", "MAO004Diagnosis", "delta"),
    new FileDependency("Gold/MA/Risk/MedicalGoldenClaimDiagnosis", "MedicalGoldenClaimDiagnosis", "delta"),
    new FileDependency("Gold/MA/Risk/Membership", "Membership", "delta"),
    new FileDependency("Gold/MA/Risk/SupplementalDiagnosis", "SupplementalDiagnosis", "delta"),
    new FileDependency("Gold/MA/Risk/Membership", "Membership", "delta"),
    new FileDependency("global/Gold/icd", "icd", "delta"),
    new FileDependency("global/Gold/hcc", "hcc", "delta"),
    new FileDependency("global/Gold/icdHCCXref", "icdHCCXref", "delta"),
    new FileDependency("global/Gold/TrumpingHCC", "TrumpingHCC", "delta"),
    new FileDependency("OperationalData/RAQ/MerlinRA7/dbo/tblSuspectCriteria", "tblSuspectCriteria", "parquet"),
    new FileDependency("OperationalData/RAQ/MerlinRA7/dbo/tblSuspectMembers", "tblSuspectMembers", "parquet"),
    new FileDependency("OperationalData/RAQ/MerlinRA7/dbo/tblCapturedDataNotes", "tblCapturedDataNotes", "parquet"),
    new FileDependency("OperationalData/RAQ/MerlinRA7/dbo/tblNotesText", "tblNotesText", "parquet"),
    new FileDependency("global/OperationalData/RAQ/TepReference/dbo/HCCRate", "HCCRate", "parquet"),
    new FileDependency("global/OperationalData/RAQ/TepReference/dbo/HCCEffectiveYear", "HCCEffectiveYear", "parquet"),
    new FileDependency("Gold/MA/Risk/Segment", "Segment", "delta") 
)

def getDependencyPath(fileLocation: String): String = if (fileLocation.contains("global")) mountPoint + fileLocation else fileLocations + fileLocation
  


dependencies.foreach( (x: FileDependency) => spark.read.format(x.format).option("header","true").load(getDependencyPath(x.location)).createOrReplaceTempView(x.viewName))

// COMMAND ----------

// MAGIC %md
// MAGIC ### Set the SPARK SQL Parser RegExColumn Names to True

// COMMAND ----------

// MAGIC %sql
// MAGIC -- set the regex column selector to true
// MAGIC SET spark.sql.parser.quotedRegexColumnNames=True

// COMMAND ----------

// MAGIC %md
// MAGIC ### Set the DATE Values

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW IncurredDate AS select max(StatementToDate) from MedicalGoldenClaimDiagnosis;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create DIAGS Temp View

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW DIAGS AS SELECT DISTINCT
// MAGIC     XR.icd AS ICDCODE,
// MAGIC 	IC.icdCodeType AS ICDCODEFORMATTED,
// MAGIC 	IC.icdDisplayDescripton AS ICDDESCRIPTION,
// MAGIC 	coalesce(IC.isChronic,null) AS ISCHRONIC,
// MAGIC 	IC.ISComplete AS ISCOMPLETE,
// MAGIC 	XR.icdCodeType,
// MAGIC     	CASE 
// MAGIC     		WHEN XR.icdCodeType = 10 THEN 1 ELSE 0 --CHANGED FROM CODETYPE 9 TO 10
// MAGIC     	END ISICD10, --icdHCCXref.ICDcodetype
// MAGIC 	XR.effectiveStartDate AS EFFECTIVEDATESTART,
// MAGIC 	XR.effectiveEndDate AS EFFECTIVEDATEEND,
// MAGIC 	XR.HCCVersion AS HCCVERSION, 
// MAGIC 	HC.HCCNumber AS  HCC,
// MAGIC 	HC.HCCDescription AS HCCDESCRIPTION
// MAGIC from icd IC
// MAGIC 	JOIN icdhccxref XR
// MAGIC 		ON IC.icd = XR.icd AND IC.icdCodeType = XR.icdCodeType AND IC.icdEffectiveYear = XR.icdEffectiveYear
// MAGIC 	JOIN  hcc HC 
// MAGIC 		ON XR.hccType = HC.HCCType AND XR.icdEffectiveYear = HC.EffectiveYEar AND HC.HCCTYPE IN ('COMM', 'ESRD', 'Comm')
// MAGIC ORDER BY ICDCODE,
// MAGIC EFFECTIVEDATESTART,
// MAGIC EFFECTIVEDATEEND,
// MAGIC HCC,
// MAGIC HCCDESCRIPTION;
// MAGIC 
// MAGIC SELECT * FROM DIAGS;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create TRUMPING Temp View

// COMMAND ----------

// MAGIC %sql 
// MAGIC CREATE OR REPLACE TEMP VIEW TRUMPING AS
// MAGIC SELECT XR.icd AS ICDCODE,
// MAGIC 	IC.icdCodeType AS ICDCODEFORMATTED,
// MAGIC 	IC.icdDisplayDescripton AS ICDDESCRIPTION,
// MAGIC 	coalesce(IC.isChronic,null) AS ISCHRONIC,
// MAGIC 	IC.ISComplete AS ISCOMPLETE,
// MAGIC 	XR.icdCodeType,
// MAGIC 	XR.effectiveStartDate AS EFFECTIVEDATESTART,
// MAGIC 	XR.effectiveEndDate AS EFFECTIVEDATEEND,
// MAGIC 	XR.HCCVersion, 
// MAGIC 	HC.HCCNumber AS  HCC,
// MAGIC 	HC.HCCDescription
// MAGIC from icd IC
// MAGIC 	JOIN icdhccxref XR
// MAGIC 		ON IC.icd = XR.icd AND IC.icdCodeType = XR.icdCodeType AND IC.icdEffectiveYear = XR.icdEffectiveYear
// MAGIC 	JOIN  hcc HC 
// MAGIC 		ON XR.hccType = HC.HCCType AND XR.icdEffectiveYear = HC.EffectiveYEar AND HC.HCCTYPE IN ('COMM', 'ESRD', 'Comm');
// MAGIC         
// MAGIC SELECT * FROM TRUMPING;     

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create  Cache Suspect Analysis All  Temp View - CacheSuspectAnalysis UNION CacheSuspectAnalysisHistory

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW CacheSupsectAnalysisAll AS SELECT DISTINCT *,
// MAGIC   RecordType = CASE WHEN RecordType IN ('C', '21') THEN 'V21' 
// MAGIC              WHEN DOSYear IN ('2019','2020','2021','2022') AND RecordType='23' THEN 'V24' 
// MAGIC              WHEN DOSYear<'2019' AND RecordType='23' THEN 'V23'
// MAGIC              WHEN RecordType='24' THEN 'V24' 
// MAGIC         ELSE 'ERROR' 
// MAGIC         END,
// MAGIC 'CURRENT' AS ISHISTORICAL
// MAGIC FROM CacheSuspectAnalysis
// MAGIC where DOSYear = year(current_date())
// MAGIC UNION
// MAGIC SELECT DISTINCT *,
// MAGIC     RecordType = CASE WHEN RecordType IN ('B','22') THEN 'V22' 
// MAGIC                WHEN RecordType IN ('C', '21') THEN 'V21' 
// MAGIC                WHEN DOSYear IN ('2019','2020','2021','2022') AND RecordType='23' THEN 'V24' 
// MAGIC                WHEN DOSYear<'2019' AND RECORDTYPE='23' THEN 'V23'
// MAGIC                WHEN RecordType='24' THEN 'V24' 
// MAGIC         ELSE 'ERROR'  
// MAGIC         END ,
// MAGIC 'HISTORICAL' AS ISHISTORICAL
// MAGIC   FROM CacheSuspectAnalysisHistory
// MAGIC       where DOSYear = year(current_date());
// MAGIC       
// MAGIC SELECT * FROM CacheSupsectAnalysisAll;

// COMMAND ----------

// MAGIC %md
// MAGIC ###Create Cache Suspected Analysis Final Temp View

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW CacheSuspectAnalysisFinal as 
// MAGIC SELECT DISTINCT
// MAGIC AAA.PlanMemberId,
// MAGIC AAA.DosYear,
// MAGIC AAA.Hcc,
// MAGIC AAA.RecordType,
// MAGIC AAA.SuspectType,
// MAGIC AAA.EvidenceDescription,
// MAGIC AAA.EvidenceType,
// MAGIC AAA.EvidenceResult,
// MAGIC '' as SuspectDescription,
// MAGIC ROW_NUMBER() OVER (
// MAGIC   PARTITION BY AAA.PlanMemberId, AAA.DosYear,AAA.Hcc 
// MAGIC   ORDER BY 
// MAGIC     CASE AAA.SuspectType 
// MAGIC       WHEN 3 THEN 1 
// MAGIC       WHEN AAA.SuspectType <> 4 THEN 2 
// MAGIC       ELSE 3 
// MAGIC     END, 
// MAGIC     AAA.SuspectType ASC, 
// MAGIC     AAA.EvidenceDescription DESC, 
// MAGIC     AAA.EvidenceType DESC, 
// MAGIC     AAA.EvidenceResult DESC
// MAGIC ) AS R2
// MAGIC 
// MAGIC FROM (
// MAGIC   SELECT
// MAGIC   AA.PlanMemberId,
// MAGIC   AA.DosYear,
// MAGIC   AA.Hcc,
// MAGIC   AA.RecordType,
// MAGIC   AA.SuspectType,
// MAGIC   
// MAGIC   (
// MAGIC     CASE AA.SuspectType
// MAGIC       WHEN AA.SuspectType = 3 AND NOT IsNull(AA.SuspectFor) THEN "MOR/RAPSRETURN/MAO-004"
// MAGIC       WHEN AA.SuspectType = 3 AND IsNull(AA.SuspectFor) THEN "MOR"
// MAGIC       WHEN 4 THEN AA.Weight
// MAGIC       WHEN NOT IsNull(CC.SuspectedHCC) THEN CC.CriteriaDescription
// MAGIC       WHEN AA.SuspectType NOT IN (3,4) AND IsNull(CC.SuspectedHCC) THEN "EVIDENCE NOT APPROVED FOR CDIALERTS"
// MAGIC       ELSE ""
// MAGIC     END
// MAGIC   ) AS EvidenceDescription,
// MAGIC   (
// MAGIC   CASE AA.SuspectType
// MAGIC     WHEN AA.SuspectType = 3 AND ISNull(AA.SUSPECTFOR) THEN "ICD10" 
// MAGIC     WHEN AA.SuspectType = 4 AND AA.EvidenceType = "LOINC" THEN AA.SuspectFor
// MAGIC     ELSE AA.EvidenceType 
// MAGIC   END
// MAGIC   ) AS EvidenceType,
// MAGIC   
// MAGIC   (CASE AA.SuspectType WHEN AA.SuspectType NOT IN (3,4) AND AA.EvidenceType = "LOINC" THEN AA.SuspectFor ELSE Null END) AS EvidenceResult
// MAGIC    
// MAGIC   FROM CacheSupsectAnalysisAll AA
// MAGIC   JOIN tblSuspectCriteria CC 
// MAGIC     ON AA.Hcc = CC.SuspectedHCC
// MAGIC     AND AA.SuspectType = CC.SuspectType
// MAGIC     AND AA.EvidenceType = CC.CodeType
// MAGIC     AND AA.EvidenceValue = CC.CodeValue 
// MAGIC     AND NOT CC.IsExcluded
// MAGIC    -- AND CC.CDIAlertLanguage
// MAGIC ) AAA;
// MAGIC 
// MAGIC 
// MAGIC SELECT * FROM CacheSuspectAnalysisFinal;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create EVIDENCES_ALL Temp View - union query - MedicalGoldenClaimDiagnosis, MAO004Diagnosis and SupplementalDiagnosis

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW EVIDENCE_ALL as 
// MAGIC SELECT 
// MAGIC   AA.PlanMemberID AS PlanMemberID,
// MAGIC   YEAR(AA.StatementFromDate) AS DOSYear, 
// MAGIC   CC.hccNumber AS HCCNumber,
// MAGIC   CC.hccVersion AS HCCVersion,
// MAGIC   'CLAIMS' AS EVIDENCESOURCE, 
// MAGIC   AA.ICD AS ICD, 
// MAGIC   AA.StatementFromDate AS FromDate,
// MAGIC   AA.StatementToDate AS ToDate,
// MAGIC   IC.isChronic AS IsChronic, 
// MAGIC   AA.BillingProviderID AS BillingProviderID
// MAGIC FROM 
// MAGIC   MedicalGoldenClaimDiagnosis AA 
// MAGIC   JOIN ChaseProviderList BB 
// MAGIC 	ON LTRIM(RTRIM(AA.BillingProviderID)) = LTRIM(RTRIM(BB.ProviderID)) AND BB.CMSApproved = 1
// MAGIC   JOIN icdHCCXref CC  
// MAGIC     ON AA.ICD = CC.icd -- AND CAST(AA.THRUDATE AS DATE) BETWEEN CC.effectiveStartDate AND CC.effectiveEndDate
// MAGIC   JOIN icd IC
// MAGIC     ON AA.ICD = IC.icd   
// MAGIC UNION
// MAGIC   SELECT
// MAGIC     MM.PlanMemberID AS PlanMemberID, 
// MAGIC     YEAR(AA.ServiceFromdate) AS DOSYear, 
// MAGIC     CC.hccNumber AS HCCNumber, 
// MAGIC     CC.hccVersion AS HCCVersion, 
// MAGIC     'MAO-004' AS EVIDENCESOURCE, 
// MAGIC     AA.ICD AS ICD, 
// MAGIC     AA.ServiceFromdate AS FromDate, 
// MAGIC     AA.ServiceTodate AS ThruDate, 
// MAGIC     IC.isChronic AS IsChronic, 
// MAGIC     ''
// MAGIC FROM 
// MAGIC   MAO004Diagnosis AA  
// MAGIC 	Inner JOIN icdHCCXref CC 
// MAGIC       ON AA.ICD = CC.icd -- AND CAST(AA.THRUDATE AS DATE) BETWEEN CC.EFFECTIVEDATESTART AND CC.EFFECTIVEDATEEND
// MAGIC 	Inner join Member MM 
// MAGIC       ON LTRIM(RTRIM(AA.BeneficiaryID)) = LTRIM(RTRIM(MM.BeneficiaryID)) 
// MAGIC     JOIN icd IC
// MAGIC       ON AA.ICD = IC.icd 
// MAGIC UNION
// MAGIC   SELECT
// MAGIC 	AA.planMemberID AS PlanMemberID, 
// MAGIC 	AA.dosYear AS DOSYear,  
// MAGIC     AA.hccNumber AS HCCNumber, 
// MAGIC     AA.hccVersion AS HCCVersion, 
// MAGIC 	'CAPTURED' AS EVIDENCESOURCE, 
// MAGIC 	AA.ICD AS ICD,  
// MAGIC 	AA.serviceFromDate AS FromDate, 
// MAGIC 	AA.serviceToDate AS ThruDate, 
// MAGIC 	IC.isChronic AS IsChronic, 
// MAGIC     ''
// MAGIC FROM 
// MAGIC   SupplementalDiagnosis AA 
// MAGIC     JOIN icdhccxref CC 
// MAGIC       ON AA.ICD = CC.icd -- AND CAST(AA.PRIMARYSERVICETHRU AS DATE) BETWEEN CC.EFFECTIVEDATESTART AND CC.EFFECTIVEDATEEND
// MAGIC     JOIN icd IC
// MAGIC       ON AA.ICD = IC.icd;
// MAGIC 
// MAGIC SELECT * FROM EVIDENCE_ALL;

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW EVIDENCE_CurrentDosYear as 
// MAGIC SELECT *
// MAGIC from  EVIDENCE_ALL
// MAGIC where DOSYear = year(current_date())
// MAGIC and HCCVersion in ('V21','V24');
// MAGIC 
// MAGIC SELECT * FROM EVIDENCE_CurrentDosYear;

// COMMAND ----------



// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW TBLCACHESUSPECTANALYSIS_CODED AS 
// MAGIC SELECT distinct  A.*
// MAGIC 	,B.hccNumber as CODED_HCC,  
// MAGIC 	'Yes' as CODED_FLAG
// MAGIC FROM CacheSuspectAnalysisFinal A
// MAGIC 	JOIN EVIDENCE_CurrentDosYear B
// MAGIC 		ON A.PlanMemberID =B.PlanMemberID 
// MAGIC 		--AND A.RecordType = B.hccVersion
// MAGIC 		--AND A.Hcc = B.hccNumber;
// MAGIC         
// MAGIC SELECT * FROM TBLCACHESUSPECTANALYSIS_CODED;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create EVIDENCE_CurrentDosYearTrumpingHCC Temp View - Filter out Further the EVIDENCE_CurrentDosYear for Trumping HCC

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW EVIDENCE_CurrentDosYearTrumpingHCC as 
// MAGIC SELECT * FROM EVIDENCE_CurrentDosYear A
// MAGIC 	JOIN TrumpingHCC B 
// MAGIC 		ON A.HCCVersion = B.hccVersion
// MAGIC 		AND A.HCCNumber= B.trumpingHcc
// MAGIC         AND B.trumpingHcc IS NOT NULL;
// MAGIC 
// MAGIC SELECT * FROM EVIDENCE_CurrentDosYearTrumpingHCC;

// COMMAND ----------

// MAGIC %md
// MAGIC ## Create Coded GAPS Temp View

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW CodedGaps AS
// MAGIC SELECT DISTINCT 
// MAGIC 			PlanMemberId,
// MAGIC 			DosYear,
// MAGIC 			HCC,
// MAGIC 			concat("V",RecordType) as RecordType,
// MAGIC 			SuspectType,
// MAGIC 			CASE WHEN SuspectType =  3 THEN 'PGI - historic' 
// MAGIC 				 WHEN SuspectType NOT IN (3,4) THEN 'PGI - suspect' END AS PGIGAPTYPE,
// MAGIC 			CASE WHEN SuspectType = 4 THEN  'Opportunity' END   AS CDIGAPTYPE,
// MAGIC 			CODED_FLAG, 
// MAGIC 			EvidenceDescription, 
// MAGIC 			EvidenceType ,
// MAGIC 			CASE  WHEN  SuspectType <> '4' THEN CODED_FLAG END  AS PGI_CODED_FLAG,
// MAGIC 			CASE SuspectType WHEN  SuspectType = '4' THEN  'No' END AS CDI_CODED_FLAG 
// MAGIC 			,Coded_HCC
// MAGIC 		FROM TBLCACHESUSPECTANALYSIS_CODED;
// MAGIC 
// MAGIC SELECT * FROM CodedGaps;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create Most Recent Evidence Temp View

// COMMAND ----------

// MAGIC %sql
// MAGIC 
// MAGIC CREATE OR REPLACE TEMP VIEW MostRecentEvidence as 
// MAGIC WITH RemoveChronic as 
// MAGIC (
// MAGIC     WITH RecentEvidence as 
// MAGIC     (
// MAGIC             SELECT *
// MAGIC             FROM 
// MAGIC             (
// MAGIC               SELECT
// MAGIC                 *, 
// MAGIC                 RANK() OVER (PARTITION BY PlanMemberId, HCCNumber, hccVersion ORDER BY DosYear DESC) AS Rank
// MAGIC               FROM Evidence_All
// MAGIC             )
// MAGIC             WHERE Rank = 1
// MAGIC     )
// MAGIC 
// MAGIC     SELECT `^[^Rr].+$` -- Quick way of selecting every column expect rank
// MAGIC     FROM
// MAGIC     (
// MAGIC         SELECT DISTINCT 
// MAGIC             *,
// MAGIC             DENSE_RANK() OVER (PARTITION BY PlanMemberId, HCCNumber, HCCVersion ORDER BY ToDate) + DENSE_RANK() OVER (PARTITION BY PlanMemberId, HCCNumber, HCCVersion ORDER BY ToDate DESC) - 1 AS TIMES_CODED,
// MAGIC             RANK() OVER (PARTITION BY PlanMemberId, HCCNumber, HCCVersion ORDER BY IsChronic DESC) AS CHRONIC_CODE_FLAG,
// MAGIC             (CASE PlanMemberId WHEN PlanMemberId = NULL THEN 0 ELSE 1 END) AS ProvExistFlag
// MAGIC         FROM RecentEvidence
// MAGIC     )
// MAGIC     WHERE CHRONIC_CODE_FLAG = 1
// MAGIC )
// MAGIC 
// MAGIC SELECT *
// MAGIC FROM 
// MAGIC (
// MAGIC   SELECT DISTINCT *,
// MAGIC   Rank() OVER (PARTITION BY PlanMemberId, HCCNumber, HCCVersion ORDER BY ToDate DESC) AS Rank
// MAGIC   FROM RemoveChronic
// MAGIC )
// MAGIC WHERE Rank = 1;
// MAGIC 
// MAGIC SELECT * FROM MostRecentEvidence;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create HCC DESC Temp View

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW HccDesc AS WITH
// MAGIC   q1 AS (select RateYear,'V24' as HCCVersion,HCC,'CFA' as SEGMENT,DualFullRate as HCCRate,(DualFullRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'A' and IsESRD=0 and IsGraft=0),
// MAGIC   q2 as (select RateYear,'V24' as HCCVersion,HCC,'CFD' as SEGMENT,DualFullRate as HCCRate,(DualFullRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'D' and IsESRD=0 and IsGraft=0 ),
// MAGIC   q3 as (select RateYear,'V24' as HCCVersion,HCC,'CNA' as SEGMENT,NonDualRate  as HCCRate,(NonDualRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'A' and IsESRD=0 and IsGraft=0),
// MAGIC   q4 as (select RateYear,'V24' as HCCVersion,HCC,'CND' as SEGMENT,NonDualRate  as HCCRate,(NonDualRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'D' and IsESRD=0 and IsGraft=0),
// MAGIC   q5 as (select RateYear,'V24' as HCCVersion,HCC,'CPA' as SEGMENT,DualPartialRate as HCCRate,(DualPartialRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'A' and IsESRD=0 and IsGraft=0),
// MAGIC   q6 as (select RateYear,'V24' as HCCVersion,HCC,'CPD' as SEGMENT,DualPartialRate as HCCRate,(DualPartialRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = 'D' and IsESRD=0 and IsGraft=0),
// MAGIC   q7 as (select RateYear,'V24' as HCCVersion,HCC,'I'   as SEGMENT,InstitutionalRate as HCCRate,(InstitutionalRate/1.118)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason ='A' and IsESRD=0 and IsGraft=0),
// MAGIC   q8 as (select RateYear,'V21' as HCCVersion,HCC,'DI'  as SEGMENT,NonDualRate as HCCRate,(NonDualRate)/1.077 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = '' and IsESRD=1 and IsGraft=0),
// MAGIC   q9 as ( select RateYear,'V21' as HCCVersion,HCC,'GC'  as SEGMENT,NonDualRate as HCCRate,(NonDualRate/1.126)*0.941 as RAF from  HCCRate where RateYear=2021 and EligibilityReason = ''  and IsESRD=0 and IsGraft=1),
// MAGIC   
// MAGIC   A as (SELECT * FROM q1 UNION FROM 
// MAGIC                       q2 UNION FROM 
// MAGIC                       q3 UNION FROM 
// MAGIC                       q4 UNION FROM 
// MAGIC                       q5 UNION FROM 
// MAGIC                       q6 UNION FROM 
// MAGIC                       q7 UNION FROM 
// MAGIC                       q8 UNION FROM 
// MAGIC                       q9)
// MAGIC   
// MAGIC SELECT  a.*,b.HCCDescription as CATEGORY_DESCRIPTION
// MAGIC 
// MAGIC FROM  A
// MAGIC      
// MAGIC Join (
// MAGIC Select 
// MAGIC        a.EffectiveYear,HCCNumber,HCCDescription,HCCVersion,HCCType
// MAGIC        from HCCEffectiveYear a
// MAGIC        Inner join hcc b on a.EffectiveYear=b.EffectiveYear
// MAGIC        where a.EffectiveYear=2021
// MAGIC 
// MAGIC )b on b.EffectiveYear=a.Rateyear and a.HCC=b.HCCNumber and a.HCCVersion=b.HCCVersion;
// MAGIC 
// MAGIC SELECT * FROM HccDesc;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create #ADD_RAF_VALUE Temp View (line 665 on SP)

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW AddRafValue AS
// MAGIC SELECT  DISTINCT 
// MAGIC 	 CG.PlanMemberID
// MAGIC 	,SG.planMemberID AS MEMBERID
// MAGIC 	,CG.HCC
// MAGIC     ,CG.RecordType
// MAGIC 	,CG.PGI_CODED_FLAG
// MAGIC 	,CG.CDI_CODED_FLAG
// MAGIC 	,CG.PGIGAPTYPE	
// MAGIC 	,CG.CDIGAPTYPE	
// MAGIC 	,CG.SUSPECTTYPE	
// MAGIC 	,CG.EVIDENCEDESCRIPTION	
// MAGIC 	,CG.EVIDENCETYPE	
// MAGIC 	,SG1.SEGMENT AS SEGMENT
// MAGIC 	,HD.RAF AS CATEGORY_VALUE
// MAGIC 	,HD.CATEGORY_DESCRIPTION
// MAGIC 	,MRE.EVIDENCESOURCE
// MAGIC 	,MRE.ICD
// MAGIC 	,MRE.FROMDATE
// MAGIC 	,MRE.ToDATE
// MAGIC 	,MRE.ISCHRONIC
// MAGIC 	,MRE.PlanMemberID AS MREPlanMemberId
// MAGIC 	,MRE.TIMES_CODED
// MAGIC 	,MRE.CHRONIC_CODE_FLAG
// MAGIC 	,MRE.ProvExistFlag
// MAGIC 	,COALESCE(PM.NPI,GR.providerNPI) AS NPI_PROVMAST 
// MAGIC 	--,COALESCE(PM.TIN,GR.TIN) AS TIN_PROVMAST
// MAGIC     ,SG.providerNPI AS NPI
// MAGIC     ,SG.providerTIN AS TIN
// MAGIC 	,GR.providerNPI AS GRNPI
// MAGIC 	,GR.providerTIN AS GRTIN
// MAGIC FROM CodedGaps CG
// MAGIC 	LEFT JOIN Membership SG
// MAGIC 		ON CG.PlanMemberID=SG.planMemberID
// MAGIC 			LEFT JOIN HccDesc HD
// MAGIC 				ON CG.HCC = HD.HCC
// MAGIC 				AND CG.RecordType = HD.HCCVERSION
// MAGIC                   LEFT JOIN Segment SG1
// MAGIC                     ON SG1.Segment = HD.SEGMENT                
// MAGIC 					LEFT JOIN MostRecentEvidence MRE
// MAGIC 						ON CG.PlanMemberID = MRE.PlanMemberID
// MAGIC 						AND CG.Coded_HCC = MRE.HCCNumber 
// MAGIC 							LEFT JOIN 
// MAGIC 									 (
// MAGIC 										SELECT DISTINCT   
// MAGIC 											ProviderID, 
// MAGIC 											NPI 
// MAGIC 											--TIN
// MAGIC 										FROM Provider 
// MAGIC 										) AS PM
// MAGIC 											ON MRE.BillingProviderID = PM.ProviderID
// MAGIC 													LEFT JOIN ProviderGroupReference  GR
// MAGIC 														ON PM.ProviderID=GR.providerID;
// MAGIC                                                       
// MAGIC 
// MAGIC SELECT * FROM AddRafValue;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Create Risk By HCC Temp View

// COMMAND ----------

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.udf

val spark = SparkSession.builder().getOrCreate()

val defaultNullStringTo = udf((x: String, default: String) => if (x == null) default else x)
val defaultNullIntTo = udf((x: Int, default: Int) => if (x == null) default else x)



spark.udf.register("defaultNullStringTo", defaultNullStringTo)
spark.udf.register("defaultNullIntTo", defaultNullIntTo)

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW RiskByHcc AS
// MAGIC SELECT 
// MAGIC     LTRIM(RTRIM(A.BeneficiaryID)) AS HICN,
// MAGIC 	LTRIM(RTRIM(A.PlanMemberId)) AS MBR_ID,
// MAGIC 	'' as MEME_CK, 
// MAGIC 	B.HCC AS HCC_CATEGORY,
// MAGIC 	B.CATEGORY_DESCRIPTION, 
// MAGIC 	B.CATEGORY_VALUE,
// MAGIC 	B.SEGMENT, 
// MAGIC 	defaultNullStringTo(B.ICD, '') AS MED_TRIGGER_CODE,
// MAGIC     TIN AS LAST_CODED_TIN,
// MAGIC     NPI AS LAST_CODED_PROV_ID,
// MAGIC 	defaultNullStringTo(B.ToDATE, '') AS LAST_CODED_DATE,
// MAGIC 	defaultNullIntTo(B.TIMES_CODED, 0 ) AS TIMES_CODED
// MAGIC 	,'NA' AS RX_TRIGGER_CODE
// MAGIC 	,'NA' AS RX_TRIGGER_CLINIC
// MAGIC 	,'NA' AS LAST_RX_DATE
// MAGIC 	,'NA' AS CONFIDENCE
// MAGIC 	,CASE WHEN UPPER(B.PGI_CODED_FLAG) LIKE 'YES%' OR UPPER(B.CDI_CODED_FLAG) LIKE 'YES%' THEN 'Y' 
// MAGIC 		 ELSE 'N' 
// MAGIC 	END AS CODED_FLAG,
// MAGIC     (SELECT * FROM IncurredDate) AS INCURRED_END,
// MAGIC     (SELECT * FROM IncurredDate) AS PAID_THROUGH,
// MAGIC 	B.RecordType AS RISK_MODEL,  
// MAGIC 	current_date() AS RUN_DATE,
// MAGIC 	CASE WHEN (SUSPECTTYPE = ''  OR B.PGI_CODED_FLAG LIKE '%INCR%' )AND ISCHRONIC = '1' THEN 'Chronic'
// MAGIC 		 WHEN  SUSPECTTYPE = ''  OR B.PGI_CODED_FLAG LIKE '%INCR%'  THEN 'Acute'
// MAGIC 		 ELSE  '' END AS NEW_CONDITION_INDICATOR, 
// MAGIC 	CASE WHEN (B.EVIDENCESOURCE IS NULL OR YEAR(B.ToDATE) != 2021) AND CDI_CODED_FLAG LIKE '%Yes (CDI%' then 'CDI Alert Response' /* RS why thru date is 2020*/
// MAGIC 		 WHEN B.EVIDENCESOURCE = 'Captured' THEN 'Captured - MRR'
// MAGIC 		 WHEN B.EVIDENCESOURCE IN ('RAPS', 'DPG-Claims', 'Claims','MAO004') then 'Medical Claims' 
// MAGIC 		 ELSE '' 
// MAGIC 	END AS CODE_SOURCE,
// MAGIC COALESCE(B.PGI_CODED_FLAG,'') AS PGI_CODED_FLAG
// MAGIC ,COALESCE(B.CDI_CODED_FLAG,'') AS  CDI_CODED_FLAG
// MAGIC ,COALESCE(B.PGIGAPTYPE,'') AS PGIGAPTYPE
// MAGIC ,COALESCE(B.CDIGAPTYPE,'')  AS CDIGAPTYPE,
// MAGIC 	B.SUSPECTTYPE,  
// MAGIC 	EVIDENCEDESCRIPTION, 
// MAGIC 	EVIDENCETYPE
// MAGIC FROM Membership as A
// MAGIC JOIN AddRafValue B
// MAGIC ON A.planMemberId = B.PlanMemberID
// MAGIC --AND B.HCC IS NOT NULL 
// MAGIC ORDER BY MBR_ID, HCC_CATEGORY;
// MAGIC 
// MAGIC SELECT * FROM RiskByHcc;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Vendor Gap Report A

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW VendorGapReportA AS
// MAGIC 
// MAGIC SELECT DISTINCT
// MAGIC 	A.MBR_ID, 
// MAGIC 	A.MBR_ID, 
// MAGIC 	A.HICN,
// MAGIC 	A.MEME_CK, 
// MAGIC 	A.HCC_CATEGORY,
// MAGIC 	A.CATEGORY_DESCRIPTION, 
// MAGIC 	A.SEGMENT,
// MAGIC     A.CATEGORY_VALUE AS CATEGORY_VALUE,
// MAGIC     CASE WHEN B.ICDCODE IS NOT NULL THEN  A.MED_TRIGGER_CODE 
// MAGIC     ELSE  ' ' END AS MED_TRIGGER_CODE, 	
// MAGIC     A.LAST_CODED_TIN,
// MAGIC 	CASE WHEN B.ICDCODE IS NOT NULL THEN A.LAST_CODED_PROV_ID
// MAGIC 	ELSE  ' ' END AS LAST_CODED_PROV_ID, 
// MAGIC 	CASE 
// MAGIC       WHEN B.ICDCODE IS NOT NULL THEN A.LAST_CODED_DATE
// MAGIC       WHEN A.LAST_CODED_DATE ='01/01/1900' THEN ' '	   
// MAGIC       ELSE ' '
// MAGIC     END AS LAST_CODED_DATE, 
// MAGIC 	A.TIMES_CODED, 
// MAGIC 	A.RX_TRIGGER_CODE, 
// MAGIC 	A.RX_TRIGGER_CLINIC, 
// MAGIC 	A.LAST_RX_DATE,
// MAGIC 	A.CONFIDENCE, 
// MAGIC 	A.CODED_FLAG, 
// MAGIC     A.INCURRED_END AS INCURRED_END, 
// MAGIC     A.PAID_THROUGH AS PAID_THROUGH,
// MAGIC     A.RISK_MODEL, 
// MAGIC 	A.RUN_DATE, 
// MAGIC 	A.NEW_CONDITION_INDICATOR, 
// MAGIC 	CASE WHEN A.CODED_FLAG = 'N' THEN '' ELSE A.CODE_SOURCE END AS CODE_SOURCE, 
// MAGIC 	A.PGI_CODED_FLAG, 
// MAGIC 	A.CDI_CODED_FLAG, 
// MAGIC 	A.PGIGAPTYPE, 
// MAGIC 	A.CDIGAPTYPE,
// MAGIC 	CASE WHEN A.PGIGAPTYPE = '' AND CDIGAPTYPE LIKE 'Opp%' then 'Opportunity'
// MAGIC 		 WHEN  A.PGIGapType like '%hist%' or CDIGapType like 'Drop%' then 'Historical'
// MAGIC 		 WHEN (A.PGIGapType = 'New' or CDIGapType = 'New') and A.NEW_CONDITION_INDICATOR like 'Chr%' then 'New - Chronic'
// MAGIC 		 WHEN (A.PGIGapType = 'New' or CDIGapType = 'New') and A.NEW_CONDITION_INDICATOR like 'Acu%' then 'New - Acute'
// MAGIC 		 WHEN A.PGIGapType like '%susp%' and (CDIGapType like 'Opp%' or CDIGapType = '') then 'Suspect'
// MAGIC 	END AS NORTHSTARGAPTYPE,
// MAGIC 	A.SUSPECTTYPE, 
// MAGIC 	A.EVIDENCEDESCRIPTION, 
// MAGIC 	A.EVIDENCETYPE
// MAGIC FROM RiskByHcc AS A  -- cannot do IN condition outside of where clause
// MAGIC LEFT JOIN (SELECT distinct ICDCODE FROM DIAGS) AS B ON A.MED_TRIGGER_CODE = B.ICDCODE; 
// MAGIC 
// MAGIC SELECT * FROM VendorGapReportA;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Vendor Gap Report + Suspect Type

// COMMAND ----------

// MAGIC %sql
// MAGIC DROP TABLE IF EXISTS SuspectType;
// MAGIC CREATE TABLE IF NOT EXISTS SuspectType (type int, typeDesc string);
// MAGIC INSERT INTO SuspectType 
// MAGIC VALUES
// MAGIC (1,'Pharmacy'),
// MAGIC (2,'Diagnosis Rule'),
// MAGIC (3,'Historical'),
// MAGIC (4,'Opportunity'),
// MAGIC (5,'Lab'),
// MAGIC (6,'RadV'),
// MAGIC (7,'Procedure Code'),
// MAGIC (8,'Provider Specialty'),
// MAGIC (9,'DME'),
// MAGIC (10,'Co-Morbidity'),
// MAGIC (11,'Machine Learning');

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW VendorGapReport AS
// MAGIC 
// MAGIC SELECT DISTINCT
// MAGIC   A.*,
// MAGIC   '' as LastMonthGapType,
// MAGIC   NorthStarGapType as FinalGapType,
// MAGIC   C.typeDesc as SuspectTypeDesc
// MAGIC FROM VendorGapReportA AS A
// MAGIC LEFT JOIN SuspectType C
// MAGIC   ON A.SuspectType = C.Type;
// MAGIC   
// MAGIC SELECT * FROM VendorGapReport;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Final Vendor Gap Report

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW FinalVendorGapReport AS
// MAGIC WITH RankedVendorGap AS
// MAGIC (
// MAGIC   SELECT DISTINCT
// MAGIC     A.*,
// MAGIC     Rank() OVER (PARTITION BY A.MBR_ID, A.HCC_CATEGORY, A.Risk_Model 
// MAGIC                   ORDER BY A.Last_Coded_Prov_Id DESC,
// MAGIC                    --        A.LastCodedTIN DESC,
// MAGIC                            A.Med_Trigger_Code DESC,
// MAGIC                           A.Code_Source DESC) as R
// MAGIC   FROM VendorGapReport A
// MAGIC )
// MAGIC 
// MAGIC SELECT * FROM RankedVendorGap WHERE R = 1;
// MAGIC 
// MAGIC SELECT * FROM FinalVendorGapReport;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Test Final 3A

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW TestFinal3A AS
// MAGIC SELECT DISTINCT
// MAGIC   A.*,
// MAGIC   CASE CODED_FLAG
// MAGIC     WHEN CODED_FLAG <> "Y" AND SUSPECTTYPE IN ('10', '2', '8', '7') THEN 1
// MAGIC     ELSE 0  
// MAGIC   END AS SUSPECTTYPE_DELETE,
// MAGIC   CASE CODED_FLAG
// MAGIC      WHEN CODED_FLAG <> "Y" AND HCC_CATEGORY IN (2,6,83,86,99,100,114,135,162,166,167,169,170,173,176) THEN 1 
// MAGIC      ELSE 0
// MAGIC   END AS ACUTEHCC_DELETE,
// MAGIC   CASE WHEN CODED_FLAG<>'Y' AND SUSPECTTYPE IN ('1') AND HCC_CATEGORY NOT IN (111,17,18,19,35,40,48,54,55,29,85) THEN 1 
// MAGIC 		 ELSE 0 
// MAGIC 	END PHARMACY_DELETE
// MAGIC FROM FinalVendorGapReport A;
// MAGIC 
// MAGIC SELECT * FROM TestFinal3A

// COMMAND ----------

// MAGIC %md
// MAGIC ### Trumped HCC

// COMMAND ----------

// MAGIC %sql
// MAGIC --SELECT * FROM
// MAGIC --(
// MAGIC --  SELECT * from TestFinal3A a JOIN trumpingHcc b
// MAGIC --  ON A.HCC_CATEGORY = B.TRUMPEDHCC
// MAGIC --  AND A.CODED_FLAG = "Y"
// MAGIC --);
// MAGIC 
// MAGIC select * from trumpingHcc where hccVersion is not null

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW TrumpedHCC AS
// MAGIC WITH TrumpedJoined AS
// MAGIC (
// MAGIC   SELECT * FROM TestFinal3A A1 JOIN trumpingHcc B1
// MAGIC   ON A1.HCC_CATEGORY = B1.TRUMPEDHCC
// MAGIC   -- AND A1.RISK_MODEL = B1.HCCVERSION -- all hcc are 1 and don't have a version in the trumping table
// MAGIC   AND A1.CODED_FLAG = "Y"
// MAGIC )
// MAGIC 
// MAGIC SELECT 
// MAGIC MBR_ID, HCC_CATEGORY, RISK_MODEL FROM TestFinal3A A
// MAGIC WHERE EXISTS (SELECT * FROM TrumpedJoined A1 WHERE A.RISK_MODEL = A1.RISK_MODEL AND A.MBR_ID = A1.MBR_ID AND A.HCC_CATEGORY = A1.TrumpingHCC)

// COMMAND ----------

// MAGIC %md
// MAGIC ### Trumping HCC

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW TrumpingHccView AS
// MAGIC SELECT DISTINCT 
// MAGIC   A.*,
// MAGIC   CASE B.HCC_CATEGORY 
// MAGIC     WHEN B.HCC_CATEGORY IS NOT NULL THEN 1
// MAGIC     ELSE 0
// MAGIC   END AS TrumpingDeleted
// MAGIC FROM TestFinal3A A
// MAGIC LEFT JOIN TrumpedHCC B
// MAGIC ON A.HCC_CATEGORY = B.HCC_CATEGORY
// MAGIC AND A.RISK_MODEL = B.RISK_MODEL
// MAGIC AND A.MBR_ID = B.MBR_ID;
// MAGIC 
// MAGIC 
// MAGIC SELECT * FROM TrumpingHccView;

// COMMAND ----------

// MAGIC %md
// MAGIC ### Final Vendor Gap Report 2

// COMMAND ----------

// MAGIC %sql
// MAGIC 
// MAGIC 
// MAGIC CREATE OR REPLACE TEMP VIEW FinalVendorGapReport2 AS
// MAGIC 
// MAGIC 
// MAGIC SELECT DISTINCT
// MAGIC 	A.HICN, 
// MAGIC 	A.MBR_ID, 
// MAGIC 	A.MEME_CK, 
// MAGIC 	A.SEGMENT,
// MAGIC 	A.HCC_CATEGORY,
// MAGIC     CASE A.CATEGORY_DESCRIPTION
// MAGIC     WHEN A.CATEGORY_DESCRIPTION IS NULL THEN B.HCCDescription
// MAGIC     WHEN A.Category_Description != 'Intracranial Hemorrhage'  and Risk_model='V24' and HCC_Category=99 THEN 'Intracranial Hemorrhage'
// MAGIC     WHEN A.Category_Description != 'Substance Use Disorder, Moderate/Severe, or Substance Use with Complications'  and Risk_model='V24' and HCC_Category=55 THEN 'Substance Use Disorder, Moderate/Severe, or Substance Use with Complications'
// MAGIC     WHEN A.Category_Description!='Substance Use with Psychotic Complications'  and Risk_model='V24' and HCC_Category=54 THEN 'Substance Use with Psychotic Complications'
// MAGIC     ELSE A.CATEGORY_DESCRIPTION
// MAGIC     END AS CATEGORY_DESCRIPTION,
// MAGIC 	 
// MAGIC 	defaultNullIntTo(A.CATEGORY_VALUE, 0) AS Category_Value,
// MAGIC     A.MED_TRIGGER_CODE,
// MAGIC 	A.LAST_CODED_TIN,
// MAGIC 	A.LAST_CODED_PROV_ID, 
// MAGIC 	A.LAST_CODED_DATE,
// MAGIC 	A.TIMES_CODED, 
// MAGIC 	A.RX_TRIGGER_CODE,
// MAGIC 	A.RX_TRIGGER_CLINIC,
// MAGIC 	A.LAST_RX_DATE,
// MAGIC 	A.CONFIDENCE,
// MAGIC 	A.CODED_FLAG,
// MAGIC 	A.INCURRED_END, 
// MAGIC 	A.PAID_THROUGH, 
// MAGIC 	A.RISK_MODEL,
// MAGIC 	A.RUN_DATE, 
// MAGIC 	A.NEW_CONDITION_INDICATOR, 
// MAGIC 	A.CODE_SOURCE,
// MAGIC 	A.PGI_CODED_FLAG, 
// MAGIC 	A.CDI_CODED_FLAG, 
// MAGIC 	A.PGIGAPTYPE, 
// MAGIC 	A.CDIGAPTYPE,
// MAGIC 	A.NORTHSTARGAPTYPE, 
// MAGIC 	A.LASTMONTHGAPTYPE,
// MAGIC 	A.FINALGAPTYPE, 
// MAGIC     A.SUSPECTTYPEDESC, 
// MAGIC 	A.SUSPECTTYPE_DELETE,
// MAGIC 	A.ACUTEHCC_DELETE,
// MAGIC     A.PHARMACY_DELETE,
// MAGIC     A.TrumpingDeleted,
// MAGIC     CASE 
// MAGIC       WHEN A.SUSPECTTYPE_DELETE=1 
// MAGIC             OR A.ACUTEHCC_DELETE=1 
// MAGIC             OR A.PHARMACY_DELETE=1 
// MAGIC             OR A.TrumpingDeleted=1  AND A.CODED_FLAG != "Y" THEN 1 
// MAGIC       ELSE 0 
// MAGIC     END AS Dropped,
// MAGIC     A.EVIDENCEDESCRIPTION, 
// MAGIC 	A.EVIDENCETYPE
// MAGIC 
// MAGIC FROM TrumpingHccView A JOIN Hcc B ON A.HCC_CATEGORY = B.HCCNumber AND A.RISK_MODEL = B.HCCVERSION 
// MAGIC WHERE A.RISK_MODEL != "V21" AND HCC_CATEGORY  NOT IN (56, 59);
// MAGIC 
// MAGIC select * from FinalVendorGapReport2

// COMMAND ----------

// MAGIC %md
// MAGIC ## VendorRiskByHcc

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW VendorRiskByHccTempView AS -- HERE!
// MAGIC WITH VendorRiskByHcc AS 
// MAGIC (
// MAGIC   WITH GapReportRanked AS (
// MAGIC     SELECT 
// MAGIC       A.*, 
// MAGIC       ROW_NUMBER() OVER (PARTITION BY MBR_ID, RISK_MODEL, HCC_CATEGORY ORDER BY EVIDENCEDESCRIPTION ) AS Rank 
// MAGIC     FROM FinalVendorGapReport2 A
// MAGIC   )
// MAGIC 
// MAGIC   SELECT `^(?![Rr][Aa]).+$` FROM GapReportRanked WHERE Rank=1
// MAGIC )
// MAGIC 
// MAGIC select 
// MAGIC     current_date() as Refreshdate,
// MAGIC     year(current_date()) as ServiceYear,
// MAGIC     month(current_date()) as reportMonth ,
// MAGIC 	HICN as MEM_MEDICARE	,
// MAGIC 	MBR_ID	,
// MAGIC 	MEME_CK	,
// MAGIC 	SEGMENT	,
// MAGIC 	HCC_CATEGORY	,
// MAGIC 	CATEGORY_DESCRIPTION	,
// MAGIC 	round(CATEGORY_VALUE,3) as CATEGORY_VALUE 	,
// MAGIC 	MED_TRIGGER_CODE	,
// MAGIC 	LAST_CODED_TIN	,
// MAGIC 	LAST_CODED_PROV_ID	,
// MAGIC 	LAST_CODED_DATE	,
// MAGIC 	TIMES_CODED	,
// MAGIC 	RX_TRIGGER_CODE	,
// MAGIC 	RX_TRIGGER_CLINIC	,
// MAGIC 	LAST_RX_DATE	,
// MAGIC 	CONFIDENCE	,
// MAGIC 	CODED_FLAG	,
// MAGIC 	INCURRED_END	,
// MAGIC     PAID_THROUGH	,
// MAGIC 	RISK_MODEL	,
// MAGIC 	RUN_DATE	,
// MAGIC 	NEW_CONDITION_INDICATOR	,
// MAGIC 	CODE_SOURCE	,
// MAGIC 	PGI_CODED_FLAG	,
// MAGIC 	CDI_CODED_FLAG	,
// MAGIC 	PGIGAPTYPE	,
// MAGIC 	CDIGAPTYPE	,
// MAGIC 	NORTHSTARGAPTYPE	,
// MAGIC 	LASTMONTHGAPTYPE	,
// MAGIC 	FINALGAPTYPE	,
// MAGIC     SUSPECTTYPEDESC	,
// MAGIC 	SUSPECTTYPE_DELETE	,
// MAGIC 	ACUTEHCC_DELETE	,
// MAGIC     PHARMACY_DELETE	,
// MAGIC 	'' as ACUTEDX_DELETE	,
// MAGIC 	TrumpingDeleted	,
// MAGIC 	'' as NEGATIVE_GAP_CLOSED	,
// MAGIC 	DROPPED	,
// MAGIC 	EVIDENCEDESCRIPTION	,
// MAGIC 	EVIDENCETYPE	,
// MAGIC 	CATEGORY_VALUE as RAF
// MAGIC from VendorRiskByHcc;

// COMMAND ----------

// MAGIC %sql
// MAGIC SELECT * FROM VendorRiskByHccTempView

// COMMAND ----------

// MAGIC %md
// MAGIC ### Saving Report To Gold Layer

// COMMAND ----------

val query = s"""
SELECT 
'$clientContainer' as clientCode,
Refreshdate as snapshotDate,
reportMonth as reportMonth,
ServiceYear as serviceYear,
MEM_MEDICARE as	beneficiaryID,
MBR_ID as planMemberID,
'' as memberClientkey,
HCC_CATEGORY as	hccNumber,
CATEGORY_DESCRIPTION as	hccDescription,
CATEGORY_VALUE as riskScore,
MED_TRIGGER_CODE as medTriggerCode,
LAST_CODED_TIN as providerTIN,
LAST_CODED_PROV_ID as providerNPI,
LAST_CODED_DATE as dateCoded,
TIMES_CODED as timesCoded,
'' as rxTriggerCode,
'' as rxTriggerClinc,
'' as latestPrecriptionFilledDate,
'' as confidenceLevel,
CODED_FLAG as isCoded,
INCURRED_END as incurredEnddate,
PAID_THROUGH as paidThroughDate,
RISK_MODEL as cmsRiskModel,
RUN_DATE as runDate,
CODE_SOURCE as evidenceSource,
FINALGAPTYPE as gapType,
SUSPECTTYPEDESC as suspectTypedescription,
DROPPED as isDroppedHCC,
EVIDENCEDESCRIPTION as evidenceDescription,
EVIDENCETYPE as evidenceType 
FROM VendorRiskByHccTempView
"""


// COMMAND ----------

// MAGIC %md 
// MAGIC #### GOLD LAYER Risk By HCC - Create or Replace the Risk By Hcc Gold Layer Table

// COMMAND ----------

val GoldPath = "/mnt/"+ clientContainer + "/Gold/MA/Risk/RiskByHCC"
val PathToDelete = "/mnt/" + clientContainer + "/Gold/MA/Risk/ToDelete"

val df_RiskByHcc = spark.sql(query)

if(path_exists(GoldPath) == true)
{
dbutils.fs.mv(GoldPath, PathToDelete,true)
}

df_RiskByHcc.write.format("delta").save(GoldPath)

// COMMAND ----------

// MAGIC %md 
// MAGIC #### Just for Dev Read RiskByHcc Gold Table

// COMMAND ----------

val output = spark.read.format("delta").load(GoldPath).createOrReplaceTempView("Output")

// COMMAND ----------

// MAGIC %sql
// MAGIC SELECT * FROM Output
