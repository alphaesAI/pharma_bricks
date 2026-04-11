# Databricks notebook source
# DBTITLE 1,Setup Path
dbutils.widgets.text("ClientContainer","","")
clientCode = dbutils.widgets.get("ClientContainer")

mountPoint = "/mnt/"
destPath = mountPoint + clientCode + "/Gold/MA/Q360/Q360Visit"

returnStr = "["
# print(destPath)
destDf = spark.read.format('delta').option("header", "true").load(destPath) 
destDf.createOrReplaceTempView("Q360Visit")


# COMMAND ----------

# DBTITLE 1,Method to Check if Source Table Exists 
def checkSourceTbl(tblName):
  res = spark._jsparkSession.catalog().tableExists(clientCode, tblName)
  return res

# COMMAND ----------

# DBTITLE 1,Source Tables
hedisTbl = "gold_ma_hediseligiblemember"
memberPersonBridgeTbl = "gold_ma_memberpersonbridge"
providerTbl = "consolidated_ma_provider"

medClaimHeaderTbl = "consolidated_ma_medicalclaimheader"
medClaimLineTbl = "consolidated_ma_medicalclaimline"
goldenClaimTbl = "gold_ma_goldenclaim"

visionClaimHeaderTbl = "consolidated_ma_visionclaimheader"
visionClaimLineTbl = "consolidated_ma_visionclaimline"

hedisChk = checkSourceTbl(hedisTbl)

memberPersonBridgeChk = checkSourceTbl(memberPersonBridgeTbl)
providerChk = checkSourceTbl(providerTbl)

medClaimHeaderChk = checkSourceTbl(medClaimHeaderTbl)
medClaimLineChk = checkSourceTbl(medClaimLineTbl)
goldenClaimChk = checkSourceTbl(goldenClaimTbl)

visionClaimHeaderChk = checkSourceTbl(visionClaimHeaderTbl)
visionClaimLineChk = checkSourceTbl(visionClaimLineTbl)


# COMMAND ----------

# DBTITLE 1,Create an Empty DF
from pyspark.sql.types import StructType,StructField, StringType, IntegerType, TimestampType
emptyDf= spark.createDataFrame([], StructType([]))

# COMMAND ----------

# DBTITLE 1,FCF Client Specific Logic for PlanMemberId
# For Premera and BCBSKS, FCF data needs to add '00' at the end of planMemberId if it only has 9 digits
medClaimHeaderCust = f"""
select distinct GeneratedMedicalClaimsUniqueKey
--checked prod fcf data in MedicalClaimHeader that we only have 9 digits or 11 digits for planMemberId
    ,COALESCE(UniquePersonKey
        ,CASE WHEN LENGTH(PlanMemberID) = 9
            THEN CONCAT(PlanMemberID, '00')
            ELSE PlanMemberID 
        END) AS MemberID
    ,AdmissionDate
    ,ClaimFormType
    ,DischargeDate
    ,StatementToDate
    ,StatementFromDate
    ,DischargeStatusCode
    ,PrimaryDiagCode
    ,DiagCode2,DiagCode3, DiagCode4, DiagCode5,DiagCode6, DiagCode7, DiagCode8, DiagCode9, DiagCode10, DiagCode11, DiagCode12,DiagCode13, DiagCode14, DiagCode15, DiagCode16, DiagCode17, DiagCode18, DiagCode19,DiagCode20,DiagCode21,DiagCode22,DiagCode23,DiagCode24,DiagCode25,
    DiagCode26,DiagCode27,DiagCode28,DiagCode29,DiagCode30,DiagCode31,DiagCode32,DiagCode33,DiagCode34,DiagCode35,DiagCode36,DiagCode37,DiagCode38
    ,PrimaryProcCode
    ,ProcCode2, ProcCode3, ProcCode4, ProcCode5, ProcCode6 ,ProcCode7 ,ProcCode8 ,ProcCode9 ,ProcCode10 ,ProcCode11 ,ProcCode12 ,ProcCode13 ,ProcCode14 ,ProcCode15 ,ProcCode16 ,ProcCode17 ,ProcCode18 ,ProcCode19 ,ProcCode20 ,ProcCode21 ,ProcCode22 ,ProcCode23 ,ProcCode24 ,ProcCode25 ,ProcCode26 ,ProcCode27 ,ProcCode28 ,ProcCode29 ,ProcCode30 ,ProcCode31 ,ProcCode32 ,ProcCode33 ,ProcCode34 ,ProcCode35 ,ProcCode36 ,ProcCode37 ,ProcCode38
    ,ICDVersion
    ,DischargeStatusCode
    ,BillTypeCode
    ,PlaceOfService
    ,ClaimStatus
    ,RenderingProviderID
    ,RenderingProviderNPI
    ,BillingProviderID
    ,ClaimNumber
    ,ServiceFacilityNPI
from {clientCode}.{medClaimHeaderTbl}
where filelayoutid in (1000)
"""

medClaimHeaderRaw = f"""
select distinct GeneratedMedicalClaimsUniqueKey
    ,COALESCE(UniquePersonKey,PlanMemberID) AS MemberID     
    ,AdmissionDate
    ,ClaimFormType
    ,DischargeDate
    ,StatementToDate
    ,StatementFromDate
    ,DischargeStatusCode
    ,PrimaryDiagCode
    ,DiagCode2,DiagCode3, DiagCode4, DiagCode5,DiagCode6, DiagCode7, DiagCode8, DiagCode9, DiagCode10, DiagCode11, DiagCode12,DiagCode13, DiagCode14, DiagCode15, DiagCode16, DiagCode17, DiagCode18, DiagCode19,DiagCode20,DiagCode21,DiagCode22,DiagCode23,DiagCode24,DiagCode25,
    DiagCode26,DiagCode27,DiagCode28,DiagCode29,DiagCode30,DiagCode31,DiagCode32,DiagCode33,DiagCode34,DiagCode35,DiagCode36,DiagCode37,DiagCode38
    ,PrimaryProcCode
    ,ProcCode2, ProcCode3, ProcCode4, ProcCode5, ProcCode6 ,ProcCode7 ,ProcCode8 ,ProcCode9 ,ProcCode10 ,ProcCode11 ,ProcCode12 ,ProcCode13 ,ProcCode14 ,ProcCode15 ,ProcCode16 ,ProcCode17 ,ProcCode18 ,ProcCode19 ,ProcCode20 ,ProcCode21 ,ProcCode22 ,ProcCode23 ,ProcCode24 ,ProcCode25 ,ProcCode26 ,ProcCode27 ,ProcCode28 ,ProcCode29 ,ProcCode30 ,ProcCode31 ,ProcCode32 ,ProcCode33 ,ProcCode34 ,ProcCode35 ,ProcCode36 ,ProcCode37 ,ProcCode38
    ,ICDVersion
    ,DischargeStatusCode
    ,BillTypeCode
    ,PlaceOfService
    ,ClaimStatus
    ,RenderingProviderID
    ,RenderingProviderNPI
    ,BillingProviderID
    ,ClaimNumber
    ,ServiceFacilityNPI
from {clientCode}.{medClaimHeaderTbl}
where filelayoutid in (1000)
"""

if medClaimHeaderChk == True:
  if clientCode == 'premera' \
    or clientCode == 'bcbsks' \
    or clientCode == 'qaidap2':     
    dfMCHRaw = spark.sql(medClaimHeaderCust)
#     print("planmemberid will add 00")
  else:
    dfMCHRaw = spark.sql(medClaimHeaderRaw)
  dfMCHRaw.createOrReplaceTempView("MedicalClaimHeader")  

# COMMAND ----------

# DBTITLE 1,BCBSNE without Golden Claims
# Note: BCBSNE we did not enable Golden Claims, need to relax the join
rawFCFSqlBcbsne = f"""
With MedicalClaimLine AS (
select distinct GeneratedMedicalClaimsUniqueKey
    ,ServiceFromDate
    ,ServiceToDate
    ,ProcCode
    ,ProcCodeType
    ,ProcMod1
    ,ProcMod2
    ,RevenueCode
    ,LineNumber
from {clientCode}.{medClaimLineTbl}
)
,EligibleMemberData AS(
SELECT distinct
  COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
FROM {clientCode}.{memberPersonBridgeTbl} mpb
INNER JOIN {clientCode}.{hedisTbl} hem
ON mpb.BISInternalPersonId = hem.BISInternalPersonId
LEFT JOIN {clientCode}.{memberPersonBridgeTbl} ompb
ON ompb.BISInternalPersonId = hem.BISInternalPersonId
AND ompb.IsOriginalMemberId = 1
)
-- first joins get the Claims in ClaimLine, HedisEligibleMember and MemberPersonBridge
SELECT DISTINCT
  ch.*
  ,em.OriginalMemberID
  ,cl.ServiceFromDate
  ,cl.ServiceToDate
  ,cl.ProcCode
  ,cl.ProcCodeType
  ,cl.ProcMod1
  ,cl.ProcMod2
  ,cl.RevenueCode
  ,cl.LineNumber
FROM MedicalClaimHeader ch
JOIN MedicalClaimLine cl
ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey
join EligibleMemberData em
on ch.MemberID = em.MemberID
"""

rawFCFSql = f"""
With MedicalClaimLine AS (
select distinct GeneratedMedicalClaimsUniqueKey
    ,ServiceFromDate
    ,ServiceToDate
    ,ProcCode
    ,ProcCodeType
    ,ProcMod1
    ,ProcMod2
    ,RevenueCode
    ,LineNumber
from {clientCode}.{medClaimLineTbl}
)
,GoldenClaims AS (
select distinct GeneratedMedicalClaimsUniqueKey 
from {clientCode}.{goldenClaimTbl}
)
,EligibleMemberData AS(
SELECT distinct
  COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
FROM {clientCode}.{memberPersonBridgeTbl} mpb
INNER JOIN {clientCode}.{hedisTbl} hem
ON mpb.BISInternalPersonId = hem.BISInternalPersonId
LEFT JOIN {clientCode}.{memberPersonBridgeTbl} ompb
ON ompb.BISInternalPersonId = hem.BISInternalPersonId
AND ompb.IsOriginalMemberId = 1
)
-- first joins get the Claims in ClaimLine and GoldenClaims, HedisEligibleMember and MemberPersonBridge
SELECT DISTINCT
  ch.*
  ,em.OriginalMemberID
  ,cl.ServiceFromDate
  ,cl.ServiceToDate
  ,cl.ProcCode
  ,cl.ProcCodeType
  ,cl.ProcMod1
  ,cl.ProcMod2
  ,cl.RevenueCode
  ,cl.LineNumber
FROM MedicalClaimHeader ch
JOIN MedicalClaimLine cl
ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey
JOIN GoldenClaims gc
on ch.GeneratedMedicalClaimsUniqueKey = gc.GeneratedMedicalClaimsUniqueKey
join EligibleMemberData em
on ch.MemberID = em.MemberID
"""
# Need check MedicalClaimHeader, MedicalClaimLine, GoldenClaim, HedisEligibleMember and MemberBridgeTable
if hedisChk == True \
  and memberPersonBridgeChk == True \
  and medClaimHeaderChk == True \
  and medClaimLineChk == True:
  if clientCode == 'bcbsne':  
    dfRawFCFClaims = spark.sql(rawFCFSqlBcbsne)
#     print("Not joined GC")
  elif goldenClaimChk == True:
    dfRawFCFClaims = spark.sql(rawFCFSql)
#     print("Joined GC")
  else:
    dfRawFCFClaims = emptyDf
  dfRawFCFClaims.createOrReplaceTempView("RawFCFClaims")   

# COMMAND ----------

# DBTITLE 1,FCF Claims Source Sql
fcfSourceSql = f"""
With Provider AS (
Select * from(
SELECT DISTINCT ProviderID,npi,fileid, ROW_NUMBER()OVER(PARTITION BY npi ORDER BY fileID DESC,providerid DESC) as RNK
FROM {clientCode}.{providerTbl} --bcbsne.consolidated_ma_provider
WHERE filelayoutid in(6005, 6003)
) A
where A.rnk=1
)
--join Provider to populate ProviderID
,FcfClaims AS(
select distinct
   ch.OriginalMemberID AS MemberID
  ,ServiceFromDate
  ,ServiceToDate
  ,StatementToDate
  ,ClaimFormType
  ,StatementFromDate
  ,from_unixtime(unix_timestamp(ch.ServiceFromDate,'yyyy-MM-dd'), 'yyyyMMdd') as DateOfService
  ,AdmissionDate
  ,DischargeDate
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcCode
        ELSE NULL
   END AS CPT
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTModifier1
   ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod2
        ELSE NULL
   END AS CPTModifier2
  ,CASE WHEN ch.ProcCodeType = 'HCPCSCode' THEN ch.ProcCode
        ELSE NULL
   END AS HCPCSCDT
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcCode
        ELSE NULL
   END AS CPTII 
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTIIModifier
  ,ch.PrimaryDiagCode AS PrincipalICDDiagnosis
  ,ch.DiagCode2 AS ICDDiagnosis2
  ,ch.DiagCode3 AS ICDDiagnosis3
  ,ch.DiagCode4 AS ICDDiagnosis4
  ,ch.DiagCode5 AS ICDDiagnosis5
  ,ch.DiagCode6 AS ICDDiagnosis6
  ,ch.DiagCode7 AS ICDDiagnosis7
  ,ch.DiagCode8 AS ICDDiagnosis8
  ,ch.DiagCode9 AS ICDDiagnosis9
  ,ch.DiagCode10 AS ICDDiagnosis10
  ,ch.DiagCode11 AS ICDDiagnosis11
  ,ch.DiagCode12 AS ICDDiagnosis12
  ,ch.DiagCode13 AS ICDDiagnosis13
  ,ch.DiagCode14 AS ICDDiagnosis14
  ,ch.DiagCode15 AS ICDDiagnosis15
  ,ch.DiagCode16 AS ICDDiagnosis16
  ,ch.DiagCode17 AS ICDDiagnosis17
  ,ch.DiagCode18 AS ICDDiagnosis18
  ,ch.DiagCode19 AS ICDDiagnosis19
  ,ch.DiagCode20 AS ICDDiagnosis20
  ,ch.DiagCode21 AS ICDDiagnosis21
  ,ch.DiagCode22 AS ICDDiagnosis22
  ,ch.DiagCode23 AS ICDDiagnosis23
  ,ch.DiagCode24 AS ICDDiagnosis24
  ,ch.DiagCode25 AS ICDDiagnosis25
  ,ch.DiagCode26 AS ICDDiagnosis26
  ,ch.DiagCode27 AS ICDDiagnosis27
  ,ch.DiagCode28 AS ICDDiagnosis28
  ,ch.DiagCode29 AS ICDDiagnosis29
  ,ch.DiagCode30 AS ICDDiagnosis30
  ,ch.DiagCode31 AS ICDDiagnosis31
  ,ch.DiagCode32 AS ICDDiagnosis32
  ,ch.DiagCode33 AS ICDDiagnosis33
  ,ch.DiagCode34 AS ICDDiagnosis34
  ,ch.DiagCode35 AS ICDDiagnosis35
  ,ch.DiagCode36 AS ICDDiagnosis36
  ,ch.DiagCode37 AS ICDDiagnosis37
  ,ch.DiagCode38 AS ICDDiagnosis38
  ,ch.PrimaryProcCode AS PrincipalICDProcedure
  ,ch.ProcCode2 AS ICDProcedure2
  ,ch.ProcCode3 AS ICDProcedure3
  ,ch.ProcCode4 AS ICDProcedure4
  ,ch.ProcCode5 AS ICDProcedure5
  ,ch.ProcCode6 AS ICDProcedure6 
  ,ch.ProcCode7 AS ICDProcedure7
  ,ch.ProcCode8 AS ICDProcedure8
  ,ch.ProcCode9 AS ICDProcedure9
  ,ch.ProcCode10 AS ICDProcedure10
  ,ch.ProcCode11 AS ICDProcedure11
  ,ch.ProcCode12 AS ICDProcedure12
  ,ch.ProcCode13 AS ICDProcedure13
  ,ch.ProcCode14 AS ICDProcedure14
  ,ch.ProcCode15 AS ICDProcedure15
  ,ch.ProcCode16 AS ICDProcedure16
  ,ch.ProcCode17 AS ICDProcedure17
  ,ch.ProcCode18 AS ICDProcedure18
  ,ch.ProcCode19 AS ICDProcedure19
  ,ch.ProcCode20 AS ICDProcedure20
  ,ch.ProcCode21 AS ICDProcedure21
  ,ch.ProcCode22 AS ICDProcedure22
  ,ch.ProcCode23 AS ICDProcedure23
  ,ch.ProcCode24 AS ICDProcedure24
  ,ch.ProcCode25 AS ICDProcedure25
  ,ch.ProcCode26 AS ICDProcedure26
  ,ch.ProcCode27 AS ICDProcedure27
  ,ch.ProcCode28 AS ICDProcedure28
  ,ch.ProcCode29 AS ICDProcedure29
  ,ch.ProcCode30 AS ICDProcedure30
  ,ch.ProcCode31 AS ICDProcedure31
  ,ch.ProcCode32 AS ICDProcedure32
  ,ch.ProcCode33 AS ICDProcedure33
  ,ch.ProcCode34 AS ICDProcedure34
  ,ch.ProcCode35 AS ICDProcedure35
  ,ch.ProcCode36 AS ICDProcedure36
  ,ch.ProcCode37 AS ICDProcedure37
  ,ch.ProcCode38 AS ICDProcedure38
  ,CASE WHEN ch.ICDVersion IN(1, 0) THEN 'X'
        ELSE '9'
   END AS ICDIdentifier
  ,ch.DischargeStatusCode AS DischargeStatus
  ,ch.RevenueCode AS UBRevenue
  ,ch.BillTypeCode AS UBTypeOfBill
  ,ch.PlaceOfService AS CMSPlaceOfService
  ,CASE WHEN ch.ClaimStatus = '6' THEN 1
        WHEN ch.ClaimStatus = '8' THEN 2
        WHEN ch.ClaimStatus = 'O' THEN 4
        WHEN ch.ClaimStatus = 'C' THEN 4
        ELSE NULL
   END AS ClaimStatus
  ,CASE WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')='' and IFNULL(ch.BillingProviderID,'')='' then '00000000'
       WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')='' and IFNULL(ch.BillingProviderID,'')<>'' then ch.BillingProviderID
       WHEN IFNULL(ch.RenderingProviderID,'')<>'' then ch.RenderingProviderID
       WHEN IFNULL(ch.RenderingProviderID,'')<>'' and IFNULL(pr.ProviderID,'')<>'' then pr.ProviderID
       WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')<>'' and IFNULL(pr1.ProviderID,'')='' then ch.RenderingProviderNPI
       WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')<>'' and IFNULL(pr1.ProviderID,'')<>'' then pr1.ProviderID
   End AS ProviderID
 ,'N' AS SupplementalDataFlag
 ,ch.ClaimNumber AS ClaimID
 ,cast(ch.LineNumber as int) AS ClaimLineID
 ,'FCF' AS DataSourceName
 ,'' AS AdditionalColumn1
 ,'' AS AdditionalColumn2
 ,'' AS AdditionalColumn3
 ,'' AS AdditionalColumn4
 ,'' AS AdditionalColumn5
 ,'' AS Filler
 ,case
	when IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')='' then '00000000'
	when IFNULL(ch.RenderingProviderID,'')<>'' then ch.RenderingProviderID
	when IFNULL(ch.RenderingProviderID,'')<>'' and IFNULL(Pr.ProviderID,'')<>'' then Pr.ProviderID
	when IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')<>'' and IFNULL(PR1.ProviderID,'')='' then ch.RenderingProviderNPI
	when IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.RenderingProviderNPI,'')<>'' and IFNULL(PR1.ProviderID,'')<>'' then PR1.ProviderID
end as RenderingProviderID
,Case
	When ifnull(ch.ServiceFacilityNPI,'')<>'' then ch.ServiceFacilityNPI
	ELSE '00000000'
end as ServicingProviderID
,Case
	When ifnull(ch.BillingProviderID,'')<>'' then ch.BillingProviderID
	ELSE '00000000'
end as BillingProviderID
,ClaimFormType
from RawFCFClaims ch
left join Provider pr
on ch.RenderingProviderID = pr.NPI
left join Provider pr1
on ch.RenderingProviderNPI=pr1.NPI
),
MinMaxServiceFromToDate AS(
SELECT 
   ClaimID
  ,MIN(ServiceFromDate) AS MinServiceFromDate
  ,MAX(ServiceToDate) AS MaxServiceToDate
FROM FcfClaims
GROUP BY 
   ClaimID
)
select DISTINCT
 fcf.MemberID
,fcf.DateOfService
,date_format(
CASE
  WHEN COALESCE(fcf.AdmissionDate,'') <> '' then fcf.AdmissionDate 
  WHEN COALESCE(fcf.AdmissionDate,'') = '' AND COALESCE(fcf.DischargeStatus,'') <> '' AND fcf.ClaimFormType IN('1','2') THEN fcf.StatementFromDate 
  WHEN COALESCE(fcf.AdmissionDate,'') = '' AND COALESCE(fcf.DischargeDate,'') <> '' AND COALESCE(fcf.DischargeStatus,'') = '' AND fcf.ClaimFormType IN('1','2') THEN msd.MinServiceFromDate 
  WHEN COALESCE(fcf.AdmissionDate,'') = '' AND COALESCE(fcf.DischargeDate,'') = '' AND COALESCE(fcf.DischargeStatus,'') = '' AND fcf.ClaimFormType IN('1','2') AND COALESCE(fcf.UBRevenue,'') <> '' THEN COALESCE(msd.MinServiceFromDate,StatementFromDate)
 END, 'yyyyMMdd') AS AdmissionDate
,date_format(
CASE
  WHEN COALESCE(fcf.DischargeDate,'') <> '' then fcf.DischargeDate 
  WHEN COALESCE(fcf.DischargeDate,'') = '' AND COALESCE(fcf.AdmissionDate,'') <> '' AND fcf.ClaimFormType = '1' THEN msd.MaxServiceToDate 
  WHEN COALESCE(fcf.DischargeDate,'') = '' AND COALESCE(fcf.AdmissionDate,'') <> '' AND fcf.ClaimFormType = '2' THEN fcf.StatementToDate 
  WHEN COALESCE(fcf.DischargeDate,'') = '' AND COALESCE(fcf.AdmissionDate,'') = '' AND COALESCE(fcf.DischargeStatus,'') <> '' AND fcf.ClaimFormType IN('1','2') THEN fcf.StatementToDate 
  WHEN COALESCE(fcf.DischargeDate,'') = '' AND COALESCE(fcf.AdmissionDate,'') = '' AND COALESCE(fcf.DischargeStatus,'') = '' AND fcf.ClaimFormType IN('1','2') AND COALESCE(UBRevenue,'') <> '' THEN COALESCE(msd.MaxServiceToDate,StatementToDate)
 END, 'yyyyMMdd')  AS DischargeDate
,fcf.CPT
,fcf.CPTModifier1
,fcf.CPTModifier2
,fcf.HCPCSCDT
,fcf.CPTII
,fcf.CPTIIModifier
,fcf.PrincipalICDDiagnosis
,fcf.ICDDiagnosis2
,fcf.ICDDiagnosis3
,fcf.ICDDiagnosis4
,fcf.ICDDiagnosis5
,fcf.ICDDiagnosis6
,fcf.ICDDiagnosis7
,fcf.ICDDiagnosis8
,fcf.ICDDiagnosis9
,fcf.ICDDiagnosis10
,fcf.ICDDiagnosis11
,fcf.ICDDiagnosis12
,fcf.ICDDiagnosis13
,fcf.ICDDiagnosis14
,fcf.ICDDiagnosis15
,fcf.ICDDiagnosis16
,fcf.ICDDiagnosis17
,fcf.ICDDiagnosis18
,fcf.ICDDiagnosis19
,fcf.ICDDiagnosis20
,fcf.ICDDiagnosis21
,fcf.ICDDiagnosis22
,fcf.ICDDiagnosis23
,fcf.ICDDiagnosis24
,fcf.ICDDiagnosis25
,fcf.ICDDiagnosis26
,fcf.ICDDiagnosis27
,fcf.ICDDiagnosis28
,fcf.ICDDiagnosis29
,fcf.ICDDiagnosis30
,fcf.ICDDiagnosis31
,fcf.ICDDiagnosis32
,fcf.ICDDiagnosis33
,fcf.ICDDiagnosis34
,fcf.ICDDiagnosis35
,fcf.ICDDiagnosis36
,fcf.ICDDiagnosis37
,fcf.ICDDiagnosis38
,fcf.PrincipalICDProcedure
,fcf.ICDProcedure2
,fcf.ICDProcedure3
,fcf.ICDProcedure4
,fcf.ICDProcedure5
,fcf.ICDProcedure6
,fcf.ICDProcedure7
,fcf.ICDProcedure8
,fcf.ICDProcedure9
,fcf.ICDProcedure10
,fcf.ICDProcedure11
,fcf.ICDProcedure12
,fcf.ICDProcedure13
,fcf.ICDProcedure14
,fcf.ICDProcedure15
,fcf.ICDProcedure16
,fcf.ICDProcedure17
,fcf.ICDProcedure18
,fcf.ICDProcedure19
,fcf.ICDProcedure20
,fcf.ICDProcedure21
,fcf.ICDProcedure22
,fcf.ICDProcedure23
,fcf.ICDProcedure24
,fcf.ICDProcedure25
,fcf.ICDProcedure26
,fcf.ICDProcedure27
,fcf.ICDProcedure28
,fcf.ICDProcedure29
,fcf.ICDProcedure30
,fcf.ICDProcedure31
,fcf.ICDProcedure32
,fcf.ICDProcedure33
,fcf.ICDProcedure34
,fcf.ICDProcedure35
,fcf.ICDProcedure36
,fcf.ICDProcedure37
,fcf.ICDProcedure38
,fcf.ICDIdentifier
,DischargeStatus
,fcf.UBRevenue
,fcf.UBTypeOfBill
,fcf.CMSPlaceOfService
,fcf.ClaimStatus
,fcf.ProviderID
,fcf.SupplementalDataFlag
,fcf.ClaimID
,fcf.ClaimLineID
,fcf.DataSourceName
,fcf.AdditionalColumn1
,fcf.AdditionalColumn2
,fcf.AdditionalColumn3
,fcf.AdditionalColumn4
,fcf.AdditionalColumn5
,fcf.Filler
,fcf.RenderingProviderID
,fcf.ServicingProviderID
,fcf.BillingProviderID
,fcf.ClaimFormType
FROM FcfClaims fcf
  LEFT JOIN MinMaxServiceFromToDate msd
    ON fcf.ClaimId = msd.ClaimId
"""

# COMMAND ----------

# DBTITLE 1,Vision Claims Source Sql
visionSourceSql = f"""
WITH VisionClaimHeader AS (
select distinct GeneratedVisionClaimsUniqueKey
  ,CASE 
    WHEN LEN(COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None'))) = 9 THEN CONCAT(COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None')),'00')
    ELSE COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None'))
   END AS MemberID
  ,PrimaryProcCode
  ,ProcCode2, ProcCode3, ProcCode4, ProcCode5, ProcCode6 ,ProcCode7 ,ProcCode8 ,ProcCode9 ,ProcCode10 ,ProcCode11 ,ProcCode12 ,ProcCode13 ,ProcCode14 ,ProcCode15 ,ProcCode16 ,ProcCode17 ,ProcCode18 ,ProcCode19 ,ProcCode20 ,ProcCode21 ,ProcCode22 ,ProcCode23 ,ProcCode24 ,ProcCode25 ,ProcCode26 ,ProcCode27 ,ProcCode28 ,ProcCode29 ,ProcCode30 ,ProcCode31 ,ProcCode32 ,ProcCode33 ,ProcCode34 ,ProcCode35 ,ProcCode36 ,ProcCode37 ,ProcCode38
  ,ClaimICDVersionInd
  ,DischargeStatusCode
  ,BillTypeCode
  ,PlaceOfService
  ,ClaimStatus
  ,BillTypeCode
  ,ClaimNumber
  ,RenderingProviderID
  ,BillingProviderID
  ,null AS ClaimFormType
from {clientCode}.{visionClaimHeaderTbl}
where filelayoutid in (5001, 5000)
)
,VisionClaimLine AS (
select distinct GeneratedVisionClaimsUniqueKey
  ,LineServiceFrom
  ,ProcCode
  ,ProcCodeType
  ,ProcMod1, ProcMod2, ProcMod3
  ,DiagCode1,DiagCode2, DiagCode3, DiagCode4, DiagCode5,DiagCode6, DiagCode7, DiagCode8, DiagCode9, DiagCode10, DiagCode11, DiagCode12, DiagCode13, DiagCode14, DiagCode15, DiagCode16, DiagCode17, DiagCode18, DiagCode19,DiagCode20,DiagCode21,DiagCode22,DiagCode23,DiagCode24,DiagCode25, DiagCode26,DiagCode27,DiagCode28,DiagCode29,DiagCode30,DiagCode31,DiagCode32,DiagCode33,DiagCode34,DiagCode35,DiagCode36,DiagCode37,DiagCode38
  ,RevenueCode
  ,ClaimLineNumber
from {clientCode}.{visionClaimLineTbl}
)
,EligibleMemberData AS(
SELECT distinct
   COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
  ,CASE 
    WHEN LEN(COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None'))) = 9 THEN CONCAT(COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')),'00')
    ELSE COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None'))
   END AS MemberID
FROM {clientCode}.{memberPersonBridgeTbl} mpb
INNER JOIN {clientCode}.{hedisTbl} hem
ON mpb.BISInternalPersonId = hem.BISInternalPersonId
LEFT JOIN {clientCode}.{memberPersonBridgeTbl} ompb
ON ompb.BISInternalPersonId = hem.BISInternalPersonId
AND ompb.IsOriginalMemberId = 1
)
,Provider AS (
Select * from(
SELECT DISTINCT ProviderID,npi,fileid, ROW_NUMBER()OVER(PARTITION BY npi ORDER BY fileID DESC,providerid DESC) as RNK
FROM {clientCode}.{providerTbl}
WHERE filelayoutid in(6005, 6003)
) A
where A.rnk=1
)
-- first joins get the Claims in ClaimLine,HedisEligibleMember and MemberPersonBridge
,RawVisionClaims AS (
SELECT DISTINCT
  ch.*
  ,em.OriginalMemberID
  ,cl.LineServiceFrom
  ,cl.ProcCode
  ,cl.ProcCodeType
  ,cl.ProcMod1
  ,cl.ProcMod2
  ,cl.ProcMod3
  ,cl.DiagCode1
  ,cl.DiagCode2
  ,cl.DiagCode3
  ,cl.DiagCode4
  ,cl.DiagCode5
  ,cl.DiagCode6
  ,cl.DiagCode7
  ,cl.DiagCode8
  ,cl.DiagCode9
  ,cl.DiagCode10
  ,cl.DiagCode11
  ,cl.DiagCode12
  ,cl.DiagCode13
  ,cl.DiagCode14
  ,cl.DiagCode15
  ,cl.DiagCode16
  ,cl.DiagCode17
  ,cl.DiagCode18
  ,cl.DiagCode19
  ,cl.DiagCode20
  ,cl.DiagCode21
  ,cl.DiagCode22
  ,cl.DiagCode23
  ,cl.DiagCode24
  ,cl.DiagCode25
  ,cl.DiagCode26
  ,cl.DiagCode27
  ,cl.DiagCode28
  ,cl.DiagCode29
  ,cl.DiagCode30
  ,cl.DiagCode31
  ,cl.DiagCode32
  ,cl.DiagCode33
  ,cl.DiagCode34
  ,cl.DiagCode35
  ,cl.DiagCode36
  ,cl.DiagCode37
  ,cl.DiagCode38
  ,cl.RevenueCode
  ,cl.ClaimLineNumber
FROM VisionClaimHeader ch
  INNER JOIN VisionClaimLine cl
    ON ch.GeneratedVisionClaimsUniqueKey = cl.GeneratedVisionClaimsUniqueKey
  INNER JOIN EligibleMemberData em
    ON ch.MemberID = em.MemberID
)
--join ProviderKeys to populate ProviderKey
,VisionClaims AS(
select distinct
  ch.OriginalMemberID AS MemberID
  ,from_unixtime(unix_timestamp(ch.LineServiceFrom,'yyyy-MM-dd'), 'yyyyMMdd') AS DateOfService 
  ,'' AS AdmissionDate
  ,'' AS DischargeDate
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcCode
        ELSE NULL
   END AS CPT
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTModifier1
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod2
        ELSE NULL
   END AS CPTModifier2
  ,CASE WHEN ch.ProcCodeType = 'HCPCSCode' THEN ch.ProcCode
        ELSE NULL
   END AS HCPCSCDT
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcCode
        ELSE NULL
   END AS CPTII 
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTIIModifier
  ,ch.DiagCode1 AS PrincipalICDDiagnosis
  ,ch.DiagCode2 AS ICDDiagnosis2
  ,ch.DiagCode3 AS ICDDiagnosis3
  ,ch.DiagCode4 AS ICDDiagnosis4
  ,ch.DiagCode5 AS ICDDiagnosis5
  ,ch.DiagCode6 AS ICDDiagnosis6
  ,ch.DiagCode7 AS ICDDiagnosis7
  ,ch.DiagCode8 AS ICDDiagnosis8
  ,ch.DiagCode9 AS ICDDiagnosis9
  ,ch.DiagCode10 AS ICDDiagnosis10
  ,ch.DiagCode11 AS ICDDiagnosis11
  ,ch.DiagCode12 AS ICDDiagnosis12
  ,ch.DiagCode13 AS ICDDiagnosis13
  ,ch.DiagCode14 AS ICDDiagnosis14
  ,ch.DiagCode15 AS ICDDiagnosis15
  ,ch.DiagCode16 AS ICDDiagnosis16
  ,ch.DiagCode17 AS ICDDiagnosis17
  ,ch.DiagCode18 AS ICDDiagnosis18
  ,ch.DiagCode19 AS ICDDiagnosis19
  ,ch.DiagCode20 AS ICDDiagnosis20
  ,ch.DiagCode21 AS ICDDiagnosis21
  ,ch.DiagCode22 AS ICDDiagnosis22
  ,ch.DiagCode23 AS ICDDiagnosis23
  ,ch.DiagCode24 AS ICDDiagnosis24
  ,ch.DiagCode25 AS ICDDiagnosis25
  ,ch.DiagCode26 AS ICDDiagnosis26
  ,ch.DiagCode27 AS ICDDiagnosis27
  ,ch.DiagCode28 AS ICDDiagnosis28
  ,ch.DiagCode29 AS ICDDiagnosis29
  ,ch.DiagCode30 AS ICDDiagnosis30
  ,ch.DiagCode31 AS ICDDiagnosis31
  ,ch.DiagCode32 AS ICDDiagnosis32
  ,ch.DiagCode33 AS ICDDiagnosis33
  ,ch.DiagCode34 AS ICDDiagnosis34
  ,ch.DiagCode35 AS ICDDiagnosis35
  ,ch.DiagCode36 AS ICDDiagnosis36
  ,ch.DiagCode37 AS ICDDiagnosis37
  ,ch.DiagCode38 AS ICDDiagnosis38
  ,ch.PrimaryProcCode AS PrincipalICDProcedure
  ,ch.ProcCode2 AS ICDProcedure2
  ,ch.ProcCode3 AS ICDProcedure3
  ,ch.ProcCode4 AS ICDProcedure4
  ,ch.ProcCode5 AS ICDProcedure5
  ,ch.ProcCode6 AS ICDProcedure6 
  ,ch.ProcCode7 AS ICDProcedure7
  ,ch.ProcCode8 AS ICDProcedure8
  ,ch.ProcCode9 AS ICDProcedure9
  ,ch.ProcCode10 AS ICDProcedure10
  ,ch.ProcCode11 AS ICDProcedure11
  ,ch.ProcCode12 AS ICDProcedure12
  ,ch.ProcCode13 AS ICDProcedure13
  ,ch.ProcCode14 AS ICDProcedure14
  ,ch.ProcCode15 AS ICDProcedure15
  ,ch.ProcCode16 AS ICDProcedure16
  ,ch.ProcCode17 AS ICDProcedure17
  ,ch.ProcCode18 AS ICDProcedure18
  ,ch.ProcCode19 AS ICDProcedure19
  ,ch.ProcCode20 AS ICDProcedure20
  ,ch.ProcCode21 AS ICDProcedure21
  ,ch.ProcCode22 AS ICDProcedure22
  ,ch.ProcCode23 AS ICDProcedure23
  ,ch.ProcCode24 AS ICDProcedure24
  ,ch.ProcCode25 AS ICDProcedure25
  ,ch.ProcCode26 AS ICDProcedure26
  ,ch.ProcCode27 AS ICDProcedure27
  ,ch.ProcCode28 AS ICDProcedure28
  ,ch.ProcCode29 AS ICDProcedure29
  ,ch.ProcCode30 AS ICDProcedure30
  ,ch.ProcCode31 AS ICDProcedure31
  ,ch.ProcCode32 AS ICDProcedure32
  ,ch.ProcCode33 AS ICDProcedure33
  ,ch.ProcCode34 AS ICDProcedure34
  ,ch.ProcCode35 AS ICDProcedure35
  ,ch.ProcCode36 AS ICDProcedure36
  ,ch.ProcCode37 AS ICDProcedure37
  ,ch.ProcCode38 AS ICDProcedure38
  ,CASE WHEN ch.ClaimICDVersionInd IN(1, 0) THEN 'X'
        ELSE '9'
   END AS ICDIdentifier
  ,ch.DischargeStatusCode AS DischargeStatus
  ,ch.RevenueCode AS UBRevenue
  ,ch.BillTypeCode AS UBTypeOfBill
  ,ch.PlaceOfService AS CMSPlaceOfService
  ,CASE WHEN ch.ClaimStatus = 'I' THEN 1
        WHEN ch.ClaimStatus = 'D' THEN 2
        WHEN ch.ClaimStatus = 'R' THEN 4
        WHEN ch.ClaimStatus IN ('A', 'P') THEN 3
        ELSE NULL
   END AS ClaimStatus
  ,CASE WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.BillingProviderID,'')='' then '00000000'
       WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.BillingProviderID,'')<>'' then ch.BillingProviderID
       WHEN IFNULL(ch.RenderingProviderID,'')<>'' and upper(ch.RenderingProviderID) not like 'NPI-%' then ch.RenderingProviderID
       WHEN upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(pr.ProviderID,'')='' then ch.RenderingProviderID
       WHEN upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(pr.ProviderID,'')<>'' then pr.ProviderID
   END AS ProviderID
 ,'N' AS SupplementalDataFlag
 ,ch.ClaimNumber AS ClaimID
 ,cast(ch.ClaimLineNumber as int) AS ClaimLineID
 ,'Vision' AS DataSourceName
 ,'' AS AdditionalColumn1
 ,'' AS AdditionalColumn2
 ,'' AS AdditionalColumn3
 ,'' AS AdditionalColumn4
 ,'' AS AdditionalColumn5
 ,'' AS Filler
 ,case
	when IFNULL(ch.RenderingProviderID,'')='' then '00000000'
	when IFNULL(ch.RenderingProviderID,'')<>'' and upper(ch.RenderingProviderID) not like 'NPI-%' then ch.RenderingProviderID
	when upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(Pr.ProviderID,'')='' then ch.RenderingProviderID
	when upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(Pr.ProviderID,'')<>'' then Pr.ProviderID
end as RenderingProviderID
,'00000000' as ServicingProviderID
,case
	when IFNULL(ch.BillingProviderID,'')='' then '00000000'
	when IFNULL(ch.BillingProviderID,'')<>'' and upper(ch.BillingProviderID) not like 'NPI-%' then ch.BillingProviderID
	when upper(ch.BillingProviderID) like 'NPI-%' and IFNULL(PRB.ProviderID,'')='' then ch.BillingProviderID
	when upper(ch.BillingProviderID) like 'NPI-%' and IFNULL(PRB.ProviderID,'')<>'' then PRB.ProviderID
end as BillingProviderID
,ClaimFormType
from RawVisionClaims ch
left join Provider pr
on REPLACE(upper(ch.RenderingProviderID), 'NPI-', '') = pr.NPI
left join Provider prb
on REPLACE(upper(ch.BillingProviderID), 'NPI-', '') = prb.NPI
)
-- VisionClaims
select DISTINCT 
 MemberID
,DateOfService
,AdmissionDate
,DischargeDate
,CPT
,CPTModifier1
,CPTModifier2
,HCPCSCDT
,CPTII
,CPTIIModifier
,PrincipalICDDiagnosis
,ICDDiagnosis2
,ICDDiagnosis3
,ICDDiagnosis4
,ICDDiagnosis5
,ICDDiagnosis6
,ICDDiagnosis7
,ICDDiagnosis8
,ICDDiagnosis9
,ICDDiagnosis10
,ICDDiagnosis11
,ICDDiagnosis12
,ICDDiagnosis13
,ICDDiagnosis14
,ICDDiagnosis15
,ICDDiagnosis16
,ICDDiagnosis17
,ICDDiagnosis18
,ICDDiagnosis19
,ICDDiagnosis20
,ICDDiagnosis21
,ICDDiagnosis22
,ICDDiagnosis23
,ICDDiagnosis24
,ICDDiagnosis25
,ICDDiagnosis26
,ICDDiagnosis27
,ICDDiagnosis28
,ICDDiagnosis29
,ICDDiagnosis30
,ICDDiagnosis31
,ICDDiagnosis32
,ICDDiagnosis33
,ICDDiagnosis34
,ICDDiagnosis35
,ICDDiagnosis36
,ICDDiagnosis37
,ICDDiagnosis38
,PrincipalICDProcedure
,ICDProcedure2
,ICDProcedure3
,ICDProcedure4
,ICDProcedure5
,ICDProcedure6
,ICDProcedure7
,ICDProcedure8
,ICDProcedure9
,ICDProcedure10
,ICDProcedure11
,ICDProcedure12
,ICDProcedure13
,ICDProcedure14
,ICDProcedure15
,ICDProcedure16
,ICDProcedure17
,ICDProcedure18
,ICDProcedure19
,ICDProcedure20
,ICDProcedure21
,ICDProcedure22
,ICDProcedure23
,ICDProcedure24
,ICDProcedure25
,ICDProcedure26
,ICDProcedure27
,ICDProcedure28
,ICDProcedure29
,ICDProcedure30
,ICDProcedure31
,ICDProcedure32
,ICDProcedure33
,ICDProcedure34
,ICDProcedure35
,ICDProcedure36
,ICDProcedure37
,ICDProcedure38
,ICDIdentifier
,DischargeStatus
,UBRevenue
,UBTypeOfBill
,CMSPlaceOfService
,ClaimStatus
,ProviderID
,SupplementalDataFlag
,ClaimID
,ClaimLineID
,DataSourceName
,AdditionalColumn1
,AdditionalColumn2
,AdditionalColumn3
,AdditionalColumn4
,AdditionalColumn5
,Filler
,RenderingProviderID
,ServicingProviderID
,BillingProviderID
,ClaimFormType
from VisionClaims
"""

# COMMAND ----------

# DBTITLE 1,Agein Claims Source Sql
ageinSourceSql = f"""
WITH MedicalClaimHeader AS (
select distinct GeneratedMedicalClaimsUniqueKey
    ,FileID    
    ,COALESCE(UniquePersonKey,PlanMemberID) AS MemberID
    ,PrimaryDiagCode
    ,DiagCode2, DiagCode3, DiagCode4, DiagCode5,DiagCode6, DiagCode7, DiagCode8, DiagCode9, DiagCode10, DiagCode11, DiagCode12, DiagCode13, DiagCode14, DiagCode15, DiagCode16, DiagCode17, DiagCode18, DiagCode19,DiagCode20,DiagCode21,DiagCode22,DiagCode23,DiagCode24,DiagCode25,
    DiagCode26,DiagCode27,DiagCode28,DiagCode29,DiagCode30,DiagCode31,DiagCode32,DiagCode33,DiagCode34,DiagCode35,DiagCode36,DiagCode37,DiagCode38
    ,PrimaryProcCode
    ,ProcCode2, ProcCode3, ProcCode4, ProcCode5, ProcCode6 ,ProcCode7 ,ProcCode8 ,ProcCode9 ,ProcCode10 ,ProcCode11 ,ProcCode12 ,ProcCode13 ,ProcCode14 ,ProcCode15 ,ProcCode16 ,ProcCode17 ,ProcCode18 ,ProcCode19 ,ProcCode20 ,ProcCode21 ,ProcCode22 ,ProcCode23 ,ProcCode24 ,ProcCode25 ,ProcCode26 ,ProcCode27 ,ProcCode28 ,ProcCode29 ,ProcCode30 ,ProcCode31 ,ProcCode32 ,ProcCode33 ,ProcCode34 ,ProcCode35 ,ProcCode36 ,ProcCode37 ,ProcCode38
    ,ICDVersion
    ,DischargeStatusCode
    ,BillTypeCode
    ,PlaceOfService
    ,ClaimStatus
    ,RenderingProviderID
    ,BillingProviderID
    ,ClaimNumber
    ,ServiceFacilityNPI
    ,ClaimFormType
from {clientCode}.{medClaimHeaderTbl}
where filelayoutid in (12000, 37000)
)
,MedicalClaimLine AS (
select distinct GeneratedMedicalClaimsUniqueKey
    ,ServiceFromDate
    ,ProcCode
    ,ProcCodeType
    ,ProcMod1
    ,ProcMod2
    ,RevenueCode
    ,LineNumber
from {clientCode}.{medClaimLineTbl}
)
,EligibleMemberData AS(
SELECT distinct
  COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
FROM {clientCode}.{memberPersonBridgeTbl} mpb
INNER JOIN {clientCode}.{hedisTbl} hem
ON mpb.BISInternalPersonId = hem.BISInternalPersonId
LEFT JOIN {clientCode}.{memberPersonBridgeTbl} ompb
ON ompb.BISInternalPersonId = hem.BISInternalPersonId
AND ompb.IsOriginalMemberId = 1
)
,Provider AS (
Select * from(
SELECT DISTINCT ProviderID,npi,fileid, ROW_NUMBER()OVER(PARTITION BY npi ORDER BY fileID DESC,providerid DESC) as RNK
FROM {clientCode}.{providerTbl}
WHERE filelayoutid in(6005, 6003)
) A
where A.rnk=1
)
-- first joins get the Claims in ClaimLine, HedisEligibleMember and MemberPersonBridge
,RawAgeInClaims AS (
SELECT DISTINCT
  ch.*
  ,em.OriginalMemberID
  ,cl.ServiceFromDate
  ,cl.ProcCode
  ,cl.ProcCodeType
  ,cl.ProcMod1
  ,cl.ProcMod2
  ,cl.RevenueCode
  ,cl.LineNumber
FROM MedicalClaimHeader ch
JOIN MedicalClaimLine cl
ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey
JOIN EligibleMemberData em
ON ch.MemberID = em.MemberID
)
,DedupAgeInClaims AS(
select * from
(select *, ROW_NUMBER()OVER(PARTITION BY ClaimNumber,LineNumber,ServiceFromDate,MemberID,ProcCode,ClaimStatus  ORDER BY fileID DESC) as Rank
from RawAgeInClaims ) AS r
where r.Rank = 1
)
--join Provider to populate ProviderKey
,AgeInClaims AS(
select DISTINCT
  ch.OriginalMemberID AS MemberID
  ,from_unixtime(unix_timestamp(ch.ServiceFromDate,'yyyy-MM-dd'), 'yyyyMMdd') AS DateOfService  
  ,'' AS AdmissionDate
  ,'' AS DischargeDate
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcCode
        ELSE NULL
   END AS CPT
  ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTModifier1
   ,CASE WHEN ch.ProcCodeType = 'CPTCode' THEN ch.ProcMod2
        ELSE NULL
   END AS CPTModifier2
  ,CASE WHEN ch.ProcCodeType = 'HCPCSCode' THEN ch.ProcCode
        ELSE NULL
   END AS HCPCSCDT
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcCode
        ELSE NULL
   END AS CPTII 
  ,CASE WHEN ch.ProcCodeType = 'Unknown' AND RIGHT(ch.ProcCode, 1) = 'F' THEN ch.ProcMod1
        ELSE NULL
   END AS CPTIIModifier
  ,ch.PrimaryDiagCode AS PrincipalICDDiagnosis
  ,ch.DiagCode2 AS ICDDiagnosis2
  ,ch.DiagCode3 AS ICDDiagnosis3
  ,ch.DiagCode4 AS ICDDiagnosis4
  ,ch.DiagCode5 AS ICDDiagnosis5
  ,ch.DiagCode6 AS ICDDiagnosis6
  ,ch.DiagCode7 AS ICDDiagnosis7
  ,ch.DiagCode8 AS ICDDiagnosis8
  ,ch.DiagCode9 AS ICDDiagnosis9
  ,ch.DiagCode10 AS ICDDiagnosis10
  ,ch.DiagCode11 AS ICDDiagnosis11
  ,ch.DiagCode12 AS ICDDiagnosis12
  ,ch.DiagCode13 AS ICDDiagnosis13
  ,ch.DiagCode14 AS ICDDiagnosis14
  ,ch.DiagCode15 AS ICDDiagnosis15
  ,ch.DiagCode16 AS ICDDiagnosis16
  ,ch.DiagCode17 AS ICDDiagnosis17
  ,ch.DiagCode18 AS ICDDiagnosis18
  ,ch.DiagCode19 AS ICDDiagnosis19
  ,ch.DiagCode20 AS ICDDiagnosis20
  ,ch.DiagCode21 AS ICDDiagnosis21
  ,ch.DiagCode22 AS ICDDiagnosis22
  ,ch.DiagCode23 AS ICDDiagnosis23
  ,ch.DiagCode24 AS ICDDiagnosis24
  ,ch.DiagCode25 AS ICDDiagnosis25
  ,ch.DiagCode26 AS ICDDiagnosis26
  ,ch.DiagCode27 AS ICDDiagnosis27
  ,ch.DiagCode28 AS ICDDiagnosis28
  ,ch.DiagCode29 AS ICDDiagnosis29
  ,ch.DiagCode30 AS ICDDiagnosis30
  ,ch.DiagCode31 AS ICDDiagnosis31
  ,ch.DiagCode32 AS ICDDiagnosis32
  ,ch.DiagCode33 AS ICDDiagnosis33
  ,ch.DiagCode34 AS ICDDiagnosis34
  ,ch.DiagCode35 AS ICDDiagnosis35
  ,ch.DiagCode36 AS ICDDiagnosis36
  ,ch.DiagCode37 AS ICDDiagnosis37
  ,ch.DiagCode38 AS ICDDiagnosis38
  ,ch.PrimaryProcCode AS PrincipalICDProcedure
  ,ch.ProcCode2 AS ICDProcedure2
  ,ch.ProcCode3 AS ICDProcedure3
  ,ch.ProcCode4 AS ICDProcedure4
  ,ch.ProcCode5 AS ICDProcedure5
  ,ch.ProcCode6 AS ICDProcedure6 
  ,ch.ProcCode7 AS ICDProcedure7
  ,ch.ProcCode8 AS ICDProcedure8
  ,ch.ProcCode9 AS ICDProcedure9
  ,ch.ProcCode10 AS ICDProcedure10
  ,ch.ProcCode11 AS ICDProcedure11
  ,ch.ProcCode12 AS ICDProcedure12
  ,ch.ProcCode13 AS ICDProcedure13
  ,ch.ProcCode14 AS ICDProcedure14
  ,ch.ProcCode15 AS ICDProcedure15
  ,ch.ProcCode16 AS ICDProcedure16
  ,ch.ProcCode17 AS ICDProcedure17
  ,ch.ProcCode18 AS ICDProcedure18
  ,ch.ProcCode19 AS ICDProcedure19
  ,ch.ProcCode20 AS ICDProcedure20
  ,ch.ProcCode21 AS ICDProcedure21
  ,ch.ProcCode22 AS ICDProcedure22
  ,ch.ProcCode23 AS ICDProcedure23
  ,ch.ProcCode24 AS ICDProcedure24
  ,ch.ProcCode25 AS ICDProcedure25
  ,ch.ProcCode26 AS ICDProcedure26
  ,ch.ProcCode27 AS ICDProcedure27
  ,ch.ProcCode28 AS ICDProcedure28
  ,ch.ProcCode29 AS ICDProcedure29
  ,ch.ProcCode30 AS ICDProcedure30
  ,ch.ProcCode31 AS ICDProcedure31
  ,ch.ProcCode32 AS ICDProcedure32
  ,ch.ProcCode33 AS ICDProcedure33
  ,ch.ProcCode34 AS ICDProcedure34
  ,ch.ProcCode35 AS ICDProcedure35
  ,ch.ProcCode36 AS ICDProcedure36
  ,ch.ProcCode37 AS ICDProcedure37
  ,ch.ProcCode38 AS ICDProcedure38
  ,CASE WHEN ch.ICDVersion IN(1, 0) THEN 'X'
        ELSE '9'
   END AS ICDIdentifier
  ,ch.DischargeStatusCode AS DischargeStatus
  ,ch.RevenueCode AS UBRevenue
  ,ch.BillTypeCode AS UBTypeOfBill
  ,ch.PlaceOfService AS CMSPlaceOfService
  ,CASE WHEN ch.ClaimStatus = 'I' THEN 1
        WHEN ch.ClaimStatus = 'D' THEN 2
        WHEN ch.ClaimStatus = 'R' THEN 4
        WHEN ch.ClaimStatus IN('A', 'P') THEN 3
        ELSE NULL
   END AS ClaimStatus
 ,CASE WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.BillingProviderID,'')='' then '00000000'
       WHEN IFNULL(ch.RenderingProviderID,'')='' and IFNULL(ch.BillingProviderID,'')<>'' then ch.BillingProviderID
       WHEN IFNULL(ch.RenderingProviderID,'')<>'' and upper(ch.RenderingProviderID) not like 'NPI-%' then ch.RenderingProviderID
       WHEN upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(pr.ProviderID,'')='' then ch.RenderingProviderID
       WHEN upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(pr.ProviderID,'')<>'' then pr.ProviderID
   END AS ProviderID
 ,'N' AS SupplementalDataFlag
 ,ch.ClaimNumber AS ClaimID
 ,cast(ch.LineNumber as int) AS ClaimLineID
 ,'Agein' AS DataSourceName
 ,'' AS AdditionalColumn1
 ,'' AS AdditionalColumn2
 ,'' AS AdditionalColumn3
 ,'' AS AdditionalColumn4
 ,'' AS AdditionalColumn5
 ,'' AS Filler
 ,case
	when IFNULL(ch.RenderingProviderID,'')='' then '00000000'
	when IFNULL(ch.RenderingProviderID,'')<>'' and upper(ch.RenderingProviderID) not like 'NPI-%' then ch.RenderingProviderID
	when upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(Pr.ProviderID,'')='' then ch.RenderingProviderID
	when upper(ch.RenderingProviderID) like 'NPI-%' and IFNULL(Pr.ProviderID,'')<>'' then Pr.ProviderID
end as RenderingProviderID
,Case
	When ifnull(ch.ServiceFacilityNPI,'')<>'' then ch.ServiceFacilityNPI
	ELSE '00000000'
end as ServicingProviderID
,case
	when IFNULL(ch.BillingProviderID,'')='' then '00000000'
	when IFNULL(ch.BillingProviderID,'')<>'' and upper(ch.BillingProviderID) not like 'NPI-%' then ch.BillingProviderID
	when upper(ch.BillingProviderID) like 'NPI-%' and IFNULL(PRB.ProviderID,'')='' then ch.BillingProviderID
	when upper(ch.BillingProviderID) like 'NPI-%' and IFNULL(PRB.ProviderID,'')<>'' then PRB.ProviderID
end as BillingProviderID
,ClaimFormType
from DedupAgeInClaims ch
left join Provider pr
on REPLACE(upper(ch.RenderingProviderID), 'NPI-', '') = pr.NPI
left join Provider prb
on REPLACE(upper(ch.BillingProviderID), 'NPI-', '') = prb.NPI
)
select DISTINCT 
 MemberID
,DateOfService
,AdmissionDate
,DischargeDate
,CPT
,CPTModifier1
,CPTModifier2
,HCPCSCDT
,CPTII
,CPTIIModifier
,PrincipalICDDiagnosis
,ICDDiagnosis2
,ICDDiagnosis3
,ICDDiagnosis4
,ICDDiagnosis5
,ICDDiagnosis6
,ICDDiagnosis7
,ICDDiagnosis8
,ICDDiagnosis9
,ICDDiagnosis10
,ICDDiagnosis11
,ICDDiagnosis12
,ICDDiagnosis13
,ICDDiagnosis14
,ICDDiagnosis15
,ICDDiagnosis16
,ICDDiagnosis17
,ICDDiagnosis18
,ICDDiagnosis19
,ICDDiagnosis20
,ICDDiagnosis21
,ICDDiagnosis22
,ICDDiagnosis23
,ICDDiagnosis24
,ICDDiagnosis25
,ICDDiagnosis26
,ICDDiagnosis27
,ICDDiagnosis28
,ICDDiagnosis29
,ICDDiagnosis30
,ICDDiagnosis31
,ICDDiagnosis32
,ICDDiagnosis33
,ICDDiagnosis34
,ICDDiagnosis35
,ICDDiagnosis36
,ICDDiagnosis37
,ICDDiagnosis38
,PrincipalICDProcedure
,ICDProcedure2
,ICDProcedure3
,ICDProcedure4
,ICDProcedure5
,ICDProcedure6
,ICDProcedure7
,ICDProcedure8
,ICDProcedure9
,ICDProcedure10
,ICDProcedure11
,ICDProcedure12
,ICDProcedure13
,ICDProcedure14
,ICDProcedure15
,ICDProcedure16
,ICDProcedure17
,ICDProcedure18
,ICDProcedure19
,ICDProcedure20
,ICDProcedure21
,ICDProcedure22
,ICDProcedure23
,ICDProcedure24
,ICDProcedure25
,ICDProcedure26
,ICDProcedure27
,ICDProcedure28
,ICDProcedure29
,ICDProcedure30
,ICDProcedure31
,ICDProcedure32
,ICDProcedure33
,ICDProcedure34
,ICDProcedure35
,ICDProcedure36
,ICDProcedure37
,ICDProcedure38
,ICDIdentifier
,DischargeStatus
,UBRevenue
,UBTypeOfBill
,CMSPlaceOfService
,ClaimStatus
,ProviderID
,SupplementalDataFlag
,ClaimID
,ClaimLineID
,DataSourceName
,AdditionalColumn1
,AdditionalColumn2
,AdditionalColumn3
,AdditionalColumn4
,AdditionalColumn5
,Filler
,RenderingProviderID
,ServicingProviderID
,BillingProviderID
,ClaimFormType
FROM AgeInClaims
"""

# COMMAND ----------

# DBTITLE 1,Create a DataFrame with Schema
schema = StructType([  
  StructField('MemberID', StringType(), True),
  StructField('DateOfService', StringType(), True),
  StructField('AdmissionDate', StringType(), True),
  StructField('DischargeDate', StringType(), True),
  StructField('CPT', StringType(), True),
  StructField('CPTModifier1', StringType(), True),
  StructField('CPTModifier2', StringType(), True),
  StructField('HCPCSCDT', StringType(), True),
  StructField('CPTII', StringType(), True),
  StructField('CPTIIModifier', StringType(), True),
  StructField('PrincipalICDDiagnosis', StringType(), True),
  StructField('ICDDiagnosis2', StringType(), True),
  StructField('ICDDiagnosis3', StringType(), True),
  StructField('ICDDiagnosis4', StringType(), True),  
  StructField('ICDDiagnosis5', StringType(), True),
  StructField('ICDDiagnosis6', StringType(), True),
  StructField('ICDDiagnosis7', StringType(), True),
  StructField('ICDDiagnosis8', StringType(), True),
  StructField('ICDDiagnosis9', StringType(), True),
  StructField('ICDDiagnosis10', StringType(), True),
  StructField('ICDDiagnosis11', StringType(), True),
  StructField('ICDDiagnosis12', StringType(), True),
  StructField('ICDDiagnosis13', StringType(), True),  
  StructField('ICDDiagnosis14', StringType(), True),
  StructField('ICDDiagnosis15', StringType(), True),
  StructField('ICDDiagnosis16', StringType(), True),
  StructField('ICDDiagnosis17', StringType(), True),
  StructField('ICDDiagnosis18', StringType(), True),
  StructField('ICDDiagnosis19', StringType(), True),
  StructField('ICDDiagnosis20', StringType(), True),
  StructField('ICDDiagnosis21', StringType(), True),
  StructField('ICDDiagnosis22', StringType(), True),
  StructField('ICDDiagnosis23', StringType(), True),
  StructField('ICDDiagnosis24', StringType(), True),
  StructField('ICDDiagnosis25', StringType(), True),
  StructField('ICDDiagnosis26', StringType(), True),
  StructField('ICDDiagnosis27', StringType(), True),
  StructField('ICDDiagnosis28', StringType(), True),
  StructField('ICDDiagnosis29', StringType(), True),
  StructField('ICDDiagnosis30', StringType(), True),
  StructField('ICDDiagnosis31', StringType(), True),
  StructField('ICDDiagnosis32', StringType(), True),
  StructField('ICDDiagnosis33', StringType(), True),
  StructField('ICDDiagnosis34', StringType(), True),
  StructField('ICDDiagnosis35', StringType(), True),
  StructField('ICDDiagnosis36', StringType(), True),
  StructField('ICDDiagnosis37', StringType(), True),
  StructField('ICDDiagnosis38', StringType(), True),
  StructField('PrincipalICDProcedure', StringType(), True),
  StructField('ICDProcedure2', StringType(), True),
  StructField('ICDProcedure3', StringType(), True),
  StructField('ICDProcedure4', StringType(), True),
  StructField('ICDProcedure5', StringType(), True),
  StructField('ICDProcedure6', StringType(), True),  
  StructField('ICDIdentifier', StringType(), True),
  StructField('ICDProcedure7', StringType(), True),
  StructField('ICDProcedure8', StringType(), True),
  StructField('ICDProcedure9', StringType(), True),
  StructField('ICDProcedure10', StringType(), True),
  StructField('ICDProcedure11', StringType(), True),
  StructField('ICDProcedure12', StringType(), True),
  StructField('ICDProcedure13', StringType(), True),
  StructField('ICDProcedure14', StringType(), True),
  StructField('ICDProcedure15', StringType(), True),
  StructField('ICDProcedure16', StringType(), True),
  StructField('ICDProcedure17', StringType(), True),
  StructField('ICDProcedure18', StringType(), True),
  StructField('ICDProcedure19', StringType(), True),
  StructField('ICDProcedure20', StringType(), True),
  StructField('ICDProcedure21', StringType(), True),
  StructField('ICDProcedure22', StringType(), True),
  StructField('ICDProcedure23', StringType(), True),
  StructField('ICDProcedure24', StringType(), True),
  StructField('ICDProcedure25', StringType(), True),
  StructField('ICDProcedure26', StringType(), True),
  StructField('ICDProcedure27', StringType(), True),
  StructField('ICDProcedure28', StringType(), True),
  StructField('ICDProcedure29', StringType(), True),
  StructField('ICDProcedure30', StringType(), True),
  StructField('ICDProcedure31', StringType(), True),
  StructField('ICDProcedure32', StringType(), True),
  StructField('ICDProcedure33', StringType(), True),
  StructField('ICDProcedure34', StringType(), True),
  StructField('ICDProcedure35', StringType(), True),
  StructField('ICDProcedure36', StringType(), True),
  StructField('ICDProcedure37', StringType(), True),
  StructField('ICDProcedure38', StringType(), True),
  StructField('DischargeStatus', StringType(), True),
  StructField('UBRevenue', StringType(), True),
  StructField('UBTypeOfBill', StringType(), True),
  StructField('CMSPlaceOfService', StringType(), True),
  StructField('ClaimStatus', IntegerType(), True),
  StructField('ProviderID', StringType(), True),
  StructField('SupplementalDataFlag', StringType(), True),
  StructField('ClaimID', StringType(), True),
  StructField('ClaimLineID', IntegerType(), True),  
  StructField('DataSourceName', StringType(), True),
  StructField('AdditionalColumn1', StringType(), True),
  StructField('AdditionalColumn2', StringType(), True),
  StructField('AdditionalColumn3', StringType(), True),
  StructField('AdditionalColumn4', StringType(), True),
  StructField('AdditionalColumn5', StringType(), True),
  StructField('Filler', StringType(), True),
  StructField('RenderingProviderID', StringType(), True),
  StructField('ServicingProviderID', StringType(), True),
  StructField('BillingProviderID', StringType(), True),
  StructField('ClaimFormType', StringType(), True)
  ])
emptyRDD = spark.sparkContext.emptyRDD()
dfEmpty = spark.createDataFrame(emptyRDD,schema)

# COMMAND ----------

# DBTITLE 1,FCF Claims Source Data
# clients other than bcbsne Need all of MedicalClaimHeader, MedicalClaimLine, GoldenClaim, HedisEligibleMember, MemberBridgeTable and Provider tables
if hedisChk == True \
  and memberPersonBridgeChk == True \
  and medClaimHeaderChk == True \
  and medClaimLineChk == True:
  if clientCode == 'bcbsne':  
    dfFCFClaims = spark.sql(fcfSourceSql)
    returnStr += "(FCF Claims created!)"
  elif goldenClaimChk == True:
    dfFCFClaims = spark.sql(fcfSourceSql)
    returnStr += "(FCF Claims created!)"
  else:
#     assigned an empty datafrome to FCF Claims
    dfFCFClaims = dfEmpty    
    returnStr += f"(FCF Claims did not create because missing some source tables! \
      goldenClaimChk: {goldenClaimChk} !\
      hedisChk: {hedisChk} !\
      memberPersonBridgeChk: {memberPersonBridgeChk} !\
      providerChk: {providerChk} !\
      medClaimHeaderChk: {medClaimHeaderChk} !\
      medClaimLineChk: {medClaimLineChk} !)" 
dfFCFClaims.createOrReplaceTempView("dfFCFClaims")


# COMMAND ----------

# DBTITLE 1,Vision Claims Source Data
# Need all of VisionClaimHeader, VisionClaimLine, HedisEligibleMember, MemberBridgeTable and Provider tables
if hedisChk == True \
  and memberPersonBridgeChk == True \
  and providerChk == True \
  and visionClaimHeaderChk == True \
  and visionClaimLineChk == True:  
#   print("Vision is running")
  
  dfVisionClaims = spark.sql(visionSourceSql)  
  returnStr += "(Vision Claims created!)"
#   print("Vision Claims created!")   
else:
  #   assigned an empty datafrome to Vision Claims
  dfVisionClaims = dfEmpty
  returnStr += f"(Vision Claims did not create because missing some source tables! \
    hedisChk: {hedisChk} !\
    memberPersonBridgeChk: {memberPersonBridgeChk} !\
    providerChk: {providerChk} !\
    visionClaimHeaderChk: {visionClaimHeaderChk} !\
    visionClaimLineChk: {visionClaimLineChk} !)"    
  
dfVisionClaims.createOrReplaceTempView("dfVisionClaims")

# COMMAND ----------

# DBTITLE 1,Agein Claims Source Data
# Need all of MedicalClaimHeader, MedicalClaimLine, HedisEligibleMember, MemberBridgeTable and Provider tables
if hedisChk == True \
  and memberPersonBridgeChk == True \
  and providerChk == True \
  and medClaimHeaderChk == True \
  and medClaimLineChk == True :  
#   print("Agein is running")
  
  dfAgeinClaims = spark.sql(ageinSourceSql)  
  returnStr += "(Agein Claims created!)"
#   print("Agein Claims created!")     
else:
  #   assigned an empty datafrome to Agein Claims
  dfAgeinClaims = dfEmpty
  returnStr += f"(Agein Claims did not created because missing some source tables! \
    hedisChk: {hedisChk} !\
    memberPersonBridgeChk: {memberPersonBridgeChk} !\
    providerChk: {providerChk} !\
    medClaimHeaderChk: {medClaimHeaderChk} !\
    medClaimLineChk: {medClaimLineChk} !)"    

dfAgeinClaims.createOrReplaceTempView("dfAgeinClaims")

# COMMAND ----------

# DBTITLE 1,Combine All the Claims As Source
unionSql = """
select *, current_timestamp() AS LoadDateTime from dfFCFClaims
union
select *, current_timestamp() AS LoadDateTime from dfVisionClaims
union
select *, current_timestamp() AS LoadDateTime from dfAgeinClaims
"""

#Run main query and save into dataframe
sourceDf = spark.sql(unionSql).cache()
sourceDf.createOrReplaceTempView("sourceDf")
# print("Union SQL Query was executed")

#truncate destination table
spark.sql("""
    DELETE FROM Q360Visit
    """)

# print("Truncate SQL was executed")
#insert into destination table
sourceDf.write.format("delta").option("mergeSchema", "true").mode("append").save(destPath)
# print("Data was written to destination")


# COMMAND ----------

returnStr += "]"
dbutils.notebook.exit(returnStr)
