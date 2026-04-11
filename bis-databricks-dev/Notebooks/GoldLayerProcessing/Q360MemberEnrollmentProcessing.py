# Databricks notebook source
# DBTITLE 1,setup config
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigPath","","")

ClientCode = dbutils.widgets.get("ClientContainer")
SourceConfigPath = dbutils.widgets.get("ConfigPath")

MountPoint = "/mnt/"
FullConfigPath = MountPoint + SourceConfigPath

ClientCodeLower = ClientCode.lower()
ClientCodeUpper = ClientCode.upper()

print(ClientCode)
print(ClientCodeLower)
print(ClientCodeUpper)
print(SourceConfigPath)
print(FullConfigPath)

# COMMAND ----------

# DBTITLE 1,def source data
def mountSource():
  SourcePath = MountPoint + f"{ClientCodeLower}/consolidated/MA/Data/MemberEnrollment"
  Sourcedf = spark.read.format("delta").option("header","true").load(SourcePath)
  Sourcedf.createOrReplaceTempView("MemberEnrollment")
  print(SourcePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def destination data
def mountDestination():
  DestinationPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Q360/Q360MemberEnrollment"
  Destinationdf = spark.read.format("delta").option("header","true").load(DestinationPath)
  Destinationdf.createOrReplaceTempView("Q360MemberEnrollment")
  print(DestinationPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def HEDISEligibleMembers data
def mountHedisEligibleMember():
  HedisEligibleMemberPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Q360/HedisEligibleMember"
  HedisEligibleMemberPathdf = spark.read.format("delta").option("header","true").load(HedisEligibleMemberPath)
  HedisEligibleMemberPathdf.createOrReplaceTempView("HedisEligibleMember")
  print(HedisEligibleMemberPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def MemberPersonBridge data
def mountMemberPersonBridge():
  MemberPersonBridgePath = MountPoint + f"{ClientCodeLower}/Gold/MA/Client/MemberPersonBridge"
  MemberPersonBridgePathdf = spark.read.format("delta").option("header","true").load(MemberPersonBridgePath)
  MemberPersonBridgePathdf.createOrReplaceTempView("MemberPersonBridge")
  print(MemberPersonBridgePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def Q360PlanBenefitReference data
def mountQ360PlanBenefitReference():
  Q360PlanBenefitReferencePath = MountPoint + f"{ClientCodeLower}/consolidated/MA/Data/Q360PlanBenefitReference"
  Q360PlanBenefitReferencePathdf = spark.read.format("delta").option("header","true").load(Q360PlanBenefitReferencePath)
  Q360PlanBenefitReferencePathdf.createOrReplaceTempView("Q360PlanBenefitReference")
  print(Q360PlanBenefitReferencePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Run Source Query
def RunTempSQLScript():
  tempSQLScript=f"""
WITH LatestFileID AS (
  SELECT
     FileLayoutID
    ,CASE 
        WHEN FileLayoutDescription LIKE '%Mem%Enroll%' THEN 'MA'
        WHEN FileLayoutDescription LIKE '%Agein%' THEN 'COMM'
    END AS LineOfBusiness
    ,MAX(FileID) AS MaxFileID
  FROM MemberEnrollment
  WHERE 
  CASE 
    WHEN FileLayoutDescription LIKE '%Mem%Enroll%' THEN 1
    WHEN FileLayoutDescription LIKE '%Agein%' THEN 1
    ELSE 0 
  END = 1
  GROUP BY 
     FileLayoutID
    ,CASE 
        WHEN FileLayoutDescription LIKE '%Mem%Enroll%' THEN 'MA'
        WHEN FileLayoutDescription LIKE '%Agein%' THEN 'COMM'
    END
),
EligibleMemberData AS(
SELECT DISTINCT   
    COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID  
FROM MemberPersonBridge mpb
  INNER JOIN HedisEligibleMember hem
    ON mpb.BISInternalPersonId = hem.BISInternalPersonId
  LEFT JOIN MemberPersonBridge ompb
    ON ompb.BISInternalPersonId = hem.BISInternalPersonId
    AND ompb.IsOriginalMemberId = 1
),
LatestQ360PlanBenefitReference as (
  select max(fileid) as maxfileid from Q360PlanBenefitReference
),
Q360PlanBenefitReferenceData as (
  select distinct lower(pbf.Client) as Client,pbf.PlanGroupID,pbf.Dental,pbf.Pharmacy,pbf.MHIP,pbf.MHDN,pbf.MHAMB,pbf.CDIP,pbf.CDDN,pbf.CDAMB,pbf.Medical,pbf.FileID
  from Q360PlanBenefitReference pbf
  INNER JOIN LatestQ360PlanBenefitReference lpbf on pbf.FileID=lpbf.maxfileid
),
BaseData AS(
  SELECT 
     em.OriginalMemberID AS MemberId
    ,me.BeneficiaryID
    ,CAST(me.StartDate AS DATE) AS StartDate
    ,CAST(COALESCE(me.EndDate,'9999-12-31') AS DATE) AS EndDate
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.Dental
      else pbfa.Dental
      end,'Y') as Dental
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.Pharmacy
      else pbfa.Pharmacy
      end,'Y') as Pharmacy
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.MHIP
      else pbfa.MHIP
      end,'Y') as MHIP
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.MHDN
      else pbfa.MHDN
      end,'Y') as MHDN
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.MHAMB
      else pbfa.MHAMB
      end,'Y') as MHAMB
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.CDIP
      else pbfa.CDIP
      end,'Y') as CDIP
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.CDDN
      else pbfa.CDDN
      end,'Y') as CDDN
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='MA' then 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and lfid.LineOfBusiness='COMM' then me.CDAMB
      else pbfa.CDAMB
      end,'Y') as CDAMB
    ,coalesce(CASE
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and me.MHIP = 'Y' THEN 'Y'
      WHEN '{ClientCodeLower}' IN ('bcbsks','qaidap2','devidap2') and me.MHIP = 'N' THEN 'N'
      else pbfa.Medical
      end,'Y') as Medical
    ,me.ProductID
    ,me.PlanEmployee
    ,me.PBP
    ,me.MemberGroupCode
    ,me.ProductLine
    ,me.FileLayoutID
    ,me.FileID
    ,me.filelayoutdescription
    ,lfid.LineOfBusiness
  FROM MemberEnrollment me
      INNER JOIN LatestFileID lfid
        ON me.FileId = lfid.MaxFileID
        AND me.FileLayoutID = lfid.FileLayoutID
      INNER JOIN EligibleMemberData em
        ON COALESCE(me.PlanMemberID, me.UniquePersonkey) = em.MemberID
      LEFT JOIN Q360PlanBenefitReferenceData pbfa
        ON LEFT(me.MemberGroupCode,5)=pbfa.PlanGroupID
  WHERE
	CASE 
    WHEN to_date(me.StartDate) > IfNULL(to_date(me.EndDate),'9999-12-31') THEN 0 --to remove void spans or spans with a startdate greater than an enddate
    WHEN to_date(me.StartDate) = IfNULL(to_date(me.EndDate),'9999-12-31') THEN 0 --to remove void spans or spans with a startdate equal to an enddate
    ELSE 1
  END = 1
),
ExplodedMonths AS(
  SELECT 
     MemberId
    ,BeneficiaryID
    ,StartDate
    ,EndDate
    ,Dental
    ,Pharmacy
    ,MHIP
    ,MHDN
    ,MHAMB
    ,CDIP
    ,CDDN
    ,CDAMB
    ,Medical
    ,ProductID
    ,PlanEmployee
    ,PBP
    ,MemberGroupCode
    ,ProductLine
    ,FileLayoutID
    ,FileID
    ,filelayoutdescription
    ,LineOfBusiness
    ,explode(sequence(StartDate, EndDate, interval 1 month)) AS EnrollmentStartDate
  FROM BaseData
),
OriginalMemberIds AS (
	SELECT 
     em.MemberId
    ,em.BeneficiaryID 
    ,CAST(date_add(last_day(add_months(EnrollmentStartDate,-1)),1) AS DATE) AS StartDate
    ,CAST(last_day(EnrollmentStartDate) AS DATE) AS EndDate
    ,em.Dental
    ,em.Pharmacy
    ,em.MHIP
    ,em.MHDN
    ,em.MHAMB
    ,em.CDIP
    ,em.CDDN
    ,em.CDAMB
    ,em.Medical
    ,em.ProductID
    ,em.PlanEmployee
    ,em.PBP
    ,em.MemberGroupCode
    ,em.ProductLine
    ,em.FileLayoutID
    ,em.FileID
    ,em.filelayoutdescription
    ,em.LineOfBusiness
	  ,ROW_NUMBER() OVER(PARTITION BY em.MemberID, CAST(last_day(EnrollmentStartDate) AS DATE), CAST(date_add(last_day(add_months(EnrollmentStartDate,-1)),1) AS DATE) ORDER BY CASE WHEN em.LineOfBusiness = 'MA' THEN 0 ELSE 1 END) AS RowNumber
	FROM ExplodedMonths em
  WHERE
  em.EnrollmentStartDate <= last_day(current_timestamp())
),
LatestMemberEnrollmentData (
	SELECT 
		   MemberID			
			,StartDate
      ,EndDate
			,CASE WHEN to_date(IfNULL(EndDate,'9999-12-31')) >= to_date(CURRENT_TIMESTAMP()) AND year(StartDate) = year(current_timestamp()) THEN 1 ELSE 0 END AS OpenDate
			,Dental AS DentalBenefit
			,Pharmacy AS DrugBenefit
			,MHIP AS MentalHealthBenefitInpatient
			,MHDN AS MentalHealthBenefitIntensiveOutpatient
			,MHAMB AS MentalHealthBenefitOutpatient
			,CDIP AS ChemDepBenefitInpatient
			,CDDN AS ChemDepBenefitIntensiveOutpatient
			,CDAMB AS ChemDepBenefitOutpatientED
			,Medical AS MedicalBenefit
			,CASE 
					WHEN FileLayoutID = 19000 AND UPPER(ProductLine) = 'COMMERCIAL' THEN 'PPO'   
					WHEN FileLayoutID <> 19000 AND ProductID = 'PPO' THEN 'MP'
					WHEN FileLayoutID <> 19000 AND ProductID = 'HMO' THEN 'MCR'       
					ELSE ''
			 END AS Payer
			,PlanEmployee AS HealthPlanEmployeeDependantFlag
			,PBP AS ProductID
			,MemberGroupCode AS MemberGroupCode
			,CASE 
    		WHEN FileLayoutID = 19000 AND UPPER(ProductLine) = 'COMMERCIAL' THEN 'Y'   
    		WHEN FileLayoutID <> 19000 THEN 'Y'   		      
    		ELSE ''
			END AS PrimaryEnrollmentFlag
			,FileLayoutDescription
			,LineOfBusiness
	FROM OriginalMemberIds
  WHERE
  RowNumber = 1
)
,Final as (
SELECT 
     MemberID 
		,date_format(mes.StartDate,'yyyyMMdd') AS EnrollmentStartDate
		,CASE WHEN  mes.EndDate = last_day(current_timestamp()) THEN '99991231' ELSE date_format(mes.EndDate,'yyyyMMdd') END AS DisEnrollmentDate
		,mes.DentalBenefit
		,mes.DrugBenefit
		,mes.MentalHealthBenefitInpatient
		,mes.MentalHealthBenefitIntensiveOutpatient
		,mes.MentalHealthBenefitOutpatient
		,mes.ChemDepBenefitInpatient
		,mes.ChemDepBenefitIntensiveOutpatient
		,mes.ChemDepBenefitOutpatientED
		,mes.MedicalBenefit
		,'' AS InstitutionalLTSSBenefit
		,'' AS HomeandCommunityLTSSBenefit
		,mes.Payer
		,mes.HealthPlanEmployeeDependantFlag
		,'A' AS Indicator
		,mes.PrimaryEnrollmentFlag
		,mes.ProductID
		,'' AS ReportingID
		,mes.MemberGroupCode
		,'' AS AdditionalColumn1
		,'' AS AdditionalColumn2
		,'' AS AdditionalColumn3
		,'' AS AdditionalColumn4
		,'' AS AdditionalColumn5
		,'' AS Filler
		,mes.FileLayoutDescription
		,current_timestamp() AS LoadDateTime
FROM LatestMemberEnrollmentData mes
)
SELECT
     MemberID 
		,EnrollmentStartDate
		,DisEnrollmentDate
		,DentalBenefit
		,DrugBenefit
		,MentalHealthBenefitInpatient
		,MentalHealthBenefitIntensiveOutpatient
		,MentalHealthBenefitOutpatient
		,ChemDepBenefitInpatient
		,ChemDepBenefitIntensiveOutpatient
		,ChemDepBenefitOutpatientED
		,MedicalBenefit
		,InstitutionalLTSSBenefit
		,HomeandCommunityLTSSBenefit
		,Payer
		,HealthPlanEmployeeDependantFlag
		,Indicator
		,PrimaryEnrollmentFlag
		,ProductID
		,ReportingID
		,MemberGroupCode
		,AdditionalColumn1
		,AdditionalColumn2
		,AdditionalColumn3
		,AdditionalColumn4
		,AdditionalColumn5
		,Filler
		,FileLayoutDescription
		,LoadDateTime
FROM Final
"""
  print("Running main sql query")
  dfData = spark.sql(tempSQLScript)
  dfData.createOrReplaceTempView("tempSQLScript")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Delete Statement
def RunDeleteSQLQuery():
  DeleteSQLQuery="""
DELETE FROM Q360MemberEnrollment
"""
  print("Running delete sql query")
  dfData = spark.sql(DeleteSQLQuery)
  dfData.createOrReplaceTempView("DeleteSQLQuery")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Merge Statement
def Merge(): 
  print("Running merge script")
  mergeSQL = """
MERGE INTO Q360MemberEnrollment t 
USING (
	SELECT
	 MemberID
	,EnrollmentStartDate
	,DisEnrollmentDate
	,DentalBenefit
	,DrugBenefit
	,MentalHealthBenefitInpatient
	,MentalHealthBenefitIntensiveOutpatient
	,MentalHealthBenefitOutpatient
	,ChemDepBenefitInpatient
	,ChemDepBenefitIntensiveOutpatient
	,ChemDepBenefitOutpatientED
	,MedicalBenefit
	,InstitutionalLTSSBenefit
	,HomeandCommunityLTSSBenefit
	,Payer
	,HealthPlanEmployeedependantFlag
	,Indicator
	,PrimaryEnrollmentFlag
	,ProductID
	,ReportingID
	,MemberGroupCode
	,AdditionalColumn1
	,AdditionalColumn2
	,AdditionalColumn3
	,AdditionalColumn4
	,AdditionalColumn5
	,Filler
	,FileLayoutDescription
	,LoadDateTime
 FROM tempSQLScript
) s
on t.MemberID=s.MemberID
WHEN NOT MATCHED THEN 
INSERT (
	 MemberID
	,EnrollmentStartDate
	,DisEnrollmentDate
	,DentalBenefit
	,DrugBenefit
	,MentalHealthBenefitInpatient
	,MentalHealthBenefitIntensiveOutpatient
	,MentalHealthBenefitOutpatient
	,ChemDepBenefitInpatient
	,ChemDepBenefitIntensiveOutpatient
	,ChemDepBenefitOutpatientED
	,MedicalBenefit
	,InstitutionalLTSSBenefit
	,HomeandCommunityLTSSBenefit
	,Payer
	,HealthPlanEmployeedependantFlag
	,Indicator
	,PrimaryEnrollmentFlag
	,ProductID
	,ReportingID
	,MemberGroupCode
	,AdditionalColumn1
	,AdditionalColumn2
	,AdditionalColumn3
	,AdditionalColumn4
	,AdditionalColumn5
	,Filler
	,FileLayoutDescription
	,LoadDateTime
) 
VALUES (
	 s.MemberID
	,s.EnrollmentStartDate
	,s.DisEnrollmentDate
	,s.DentalBenefit
	,s.DrugBenefit
	,s.MentalHealthBenefitInpatient
	,s.MentalHealthBenefitIntensiveOutpatient
	,s.MentalHealthBenefitOutpatient
	,s.ChemDepBenefitInpatient
	,s.ChemDepBenefitIntensiveOutpatient
	,s.ChemDepBenefitOutpatientED
	,s.MedicalBenefit
	,s.InstitutionalLTSSBenefit
	,s.HomeandCommunityLTSSBenefit
	,s.Payer
	,s.HealthPlanEmployeedependantFlag
	,s.Indicator
	,s.PrimaryEnrollmentFlag
	,s.ProductID
	,s.ReportingID
	,s.MemberGroupCode
	,s.AdditionalColumn1
	,s.AdditionalColumn2
	,s.AdditionalColumn3
	,s.AdditionalColumn4
	,s.AdditionalColumn5
	,s.Filler
	,s.FileLayoutDescription
	,s.LoadDateTime
)
"""

  spark.sql(mergeSQL)
  return "SUCCESS"

# COMMAND ----------

def RunQ360MemberEnrollment(ClientCode):
  #mount destination
  mountDestination()
  #mount source
  mountSource()
  #mount HedisEligibleMember
  mountHedisEligibleMember()
  #mount MemberPersonBridge
  mountMemberPersonBridge()
  #mount Q360PlanBenefitReference
  mountQ360PlanBenefitReference()
  #Execute tempSQLScript -- creates a tempView called tempSQLScript
  RunTempSQLScript()
  #run delete script -- deletes the existing yearmonth based on condition
  RunDeleteSQLQuery()
  #run merge
  Merge()
  return "SUCCESS"

# COMMAND ----------

returnStr = ""
try:
  RunQ360MemberEnrollment(ClientCode) 
  returnStr = "SUCCESS"
except Exception as e:
  returnStr += repr(e)
  returnStr = "FAILURE"
finally:
  dbutils.notebook.exit(returnStr)
