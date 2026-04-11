# Databricks notebook source
# DBTITLE 1,Setup variables and mount point
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

clientCode = dbutils.widgets.get("ClientContainer")

mntPnt = '/mnt/'

# COMMAND ----------

# DBTITLE 1,Setup table configs
tableConfig = """
{
  "DestinationTableName": "Q360MembershipStars",
  "DestinationTablePath": "#clientCode/Gold/MA/Quality/Q360MembershipStars",
  "SourceTables": [
    {
      "TableName": "MemberPersonBridge",
      "TablePath": "#clientCode/Gold/MA/Client/MemberPersonBridge",
      "TableFormat": "delta"
    },
    {
      "TableName": "SpanOther",
      "TablePath": "#clientCode/consolidated/MA/Data/SpanOther",
      "TableFormat": "delta"
    },
    {
      "TableName": "Member",
      "TablePath": "#clientCode/consolidated/MA/Data/Member",
      "TableFormat": "delta"
    },
    {
      "TableName": "MemberEnrollment",
      "TablePath": "#clientCode/consolidated/MA/Data/MemberEnrollment",
      "TableFormat": "delta"
    },
    {
      "TableName": "Provider",
      "TablePath": "#clientCode/consolidated/MA/Data/Provider",
      "TableFormat": "delta"
    },
    {
      "TableName": "ProviderHierarchy",
      "TablePath": "#clientCode/consolidated/MA/Data/ProviderHierarchy",
      "TableFormat": "delta"
    },
    {
      "TableName": "Product",
      "TablePath": "#clientCode/consolidated/MA/Data/Product",
      "TableFormat": "delta"
    },
    {
      "TableName": "MMR",
      "TablePath": "#clientCode/consolidated/MA/Data/MMR",
      "TableFormat": "delta"
    },
    {
      "TableName": "LISHIST",
      "TablePath": "#clientCode/consolidated/MA/Data/LISHIST",
      "TableFormat": "delta"
    },
    {
      "TableName": "PCPAttribution",
      "TablePath": "#clientCode/consolidated/MA/Data/PCPAttribution",
      "TableFormat": "delta"
    },   
    {
      "TableName": "MemberRoster",
      "TablePath": "#clientCode/consolidated/MA/Data/MemberRoster",
      "TableFormat": "delta"
    }, 
    {
      "TableName": "ConsolidatedMMR",
      "TablePath": "#clientCode/consolidated/MA/Data/ConsolidatedMMR",
      "TableFormat": "delta"
    },
    {
      "TableName": "CarePreciseTaxo",
      "TablePath": "global/processed/Mult/Data/CarePreciseTaxo/custom/CarePreciseTaxo",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ProviderSpecialtyDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ProviderSpecialtyDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ProviderRollup",
      "TablePath": "#clientCode/consolidated/MA/Data/ProviderRollup",
      "TableFormat": "delta"
    }
  ]
}
"""

# COMMAND ----------

# DBTITLE 1,Basic rules provided from Confluence
# MAGIC
# MAGIC %md
# MAGIC - Process sets year_mth_key as yyyymm of the run date --see Final
# MAGIC - Process selects member details from most recent consol Member --see LatestMember
# MAGIC - Process selects member enrollment details file from most recent consol MemberEnrollment --see LatestMemberEnrollment 
# MAGIC - Process selects member risk score from most recent consol ConsolidatedMMR based on FileID and CMMRFileCreateDate --see  LatestConsolidatedMMR
# MAGIC - Process selects latest member hospice, esrd, lti flag from most recent consol MMR --see LatestMMRIndicators
# MAGIC   -Requires latest MRR file to be populated in the final output
# MAGIC - Process selects latest member lis from most recent consol CMSLISHIST --see Get LISHIST -- latest file
# MAGIC   - NOTE: LowIncomePeriodStartDate could be null since we did not validate null/blank in L2 for it
# MAGIC - Process finds the member in the most recent consol MemberRoster and pulls attributed provider and provider organization details --see LatestMemberRoster 
# MAGIC   - also note if the member is not in the member roster then attribution / provider / taxonomy data will not be populated in the final output
# MAGIC - Process selects altproviderreporting3 provider network from most recent consol Provider per logic --see LatestProvider
# MAGIC - Process finds the provider taxonomy and specialty in CarePreciseTaxo / ProviderSpecialtyDataset per logic --see Get Provider Taxonomies and Get Provider Specialities
# MAGIC - Process selects latest product name and product type for the member group code from most recent consol Product --see LatestProduct (based on FileName)
# MAGIC - Member Person Bridge section
# MAGIC   - Process applies the earliest known member id from gold member person bridge --see MemberInformation
# MAGIC   - Process also preserves latest known member id from gold member person bridge --see MemberInformation --not going into the output
# MAGIC - Process sets member address type as mailing or permanent per logic --see Final
# MAGIC   - Process sets curr_cvg_ind, death_ind, attribution_class flags per logic --see Final
# MAGIC   - Process blanks out attributed provider fields and provider organization fields for terminated and deceased members per logic --see Final
# MAGIC - Process the PCPAttribution for bcbsne -- see BcbsnePCPAttributionFinal
# MAGIC - Process select latest ProviderRollup to support bcbsne -- see LatestProviderRollup
# MAGIC - Create the final Dataframe based on clientcode -- see the final
# MAGIC

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Create TempView if exists
def LoadAndCreateTempView(path, format, tablename, clientCode, mntPnt):
  UpdatedPath = mntPnt + path.replace("#clientCode",clientCode)
   
  if(pathExists(UpdatedPath)):
    dfFile = spark.read.format(format).option("header","true").load(UpdatedPath)
    dfFile.createOrReplaceTempView(tablename)
    print("TempViewCreated: " + tablename)
  else:
    print("TempViewNotCreated because path does not exist: "  + tablename)

# COMMAND ----------

# DBTITLE 1,Loop tables and create views
from pyspark.sql.functions import explode, col

jsonList = []
jsonList.append(tableConfig)
df = spark.read.json(sc.parallelize(jsonList))
df.createOrReplaceTempView("tables")

for destTable in df.collect():
  DestinationTableName = destTable["DestinationTableName"]
  DestinationTablePath = destTable["DestinationTablePath"]
  LoadAndCreateTempView(DestinationTablePath, 'delta', DestinationTableName, clientCode, mntPnt)

dfSourceTables = df.select(explode("SourceTables").alias("SourceTables")) \
                   .select("SourceTables.TableFormat", "SourceTables.TableName", "SourceTables.TablePath")

for sourceTable in dfSourceTables.collect():
  TableFormat = sourceTable["TableFormat"]
  TableName = sourceTable["TableName"]
  TablePath = sourceTable["TablePath"]
  LoadAndCreateTempView(TablePath, TableFormat, TableName, clientCode, mntPnt)

dfSourceTables.createOrReplaceTempView("sourcetables")

# COMMAND ----------

# DBTITLE 1,Get Provider Taxonomies
ProviderTaxonomyQuery = """
WITH Taxonomy AS(
SELECT  
   Taxo AS TaxonomyCode
  ,NPI
  ,ROW_NUMBER() OVER(PARTITION BY NPI,Taxo ORDER BY FILE_ID DESC) RowNumber
FROM CarePreciseTaxo 
WHERE 
TaxoSwitch = 'Y'
),
ProviderSpec AS(
SELECT DISTINCT
   TaxonomyCode
  ,RIGHT(CONCAT('00',CAST(CMSSpecialtyCode AS VARCHAR(2))),2) AS CMSSpecialtyCode 
FROM ProviderSpecialtyDataset
WHERE
CMSSpecialtyCode IS NOT NULL
AND 
TaxonomyCode IS NOT NULL
),
FinalTaxo AS(
SELECT 
   t.TaxonomyCode
  ,t.NPI
  ,ps.CMSSpecialtyCode 
  ,ROW_NUMBER() OVER(PARTITION BY t.NPI,t.TaxonomyCode ORDER BY CMSSpecialtyCode DESC) RowNumber 
FROM Taxonomy t
  INNER JOIN ProviderSpec ps
    ON t.TaxonomyCode = ps.TaxonomyCode
WHERE
RowNumber = 1
)
SELECT
   TaxonomyCode
  ,NPI
  ,CMSSpecialtyCode
FROM FinalTaxo
WHERE
RowNumber = 1
"""
  
ProviderTaxonomyDF = spark.sql(ProviderTaxonomyQuery)
ProviderTaxonomyDF.createOrReplaceTempView("ProviderTaxoFinal")

# COMMAND ----------

# DBTITLE 1,Get Provider Specialities
ProviderSpecialityQuery = """
WITH ProviderSpec AS(
 SELECT 
	 TaxonomyCode 
	,RIGHT(CONCAT('00',CAST(CMSSpecialtyCode AS VARCHAR(2))),2) AS CMSSpecialtyCode
	,ROW_NUMBER() OVER(PARTITION BY TaxonomyCode ORDER BY RIGHT(CONCAT('00',CAST(CMSSpecialtyCode AS VARCHAR(2))),2) DESC) RowNumber
FROM ProviderSpecialtyDataset
WHERE 
COALESCE(TaxonomyCode,'') <> ''
AND 
COALESCE(cmsspecialtycode,'') <> ''
)
SELECT 
	 TaxonomyCode
	,CMSSpecialtyCode
FROM ProviderSpec
WHERE 
RowNUmber = 1
"""
  
ProviderSpecialityDF = spark.sql(ProviderSpecialityQuery)
ProviderSpecialityDF.createOrReplaceTempView("ProviderSpecialityFinal")

# COMMAND ----------

# DBTITLE 1,Method : Split to Monthly
from dateutil.relativedelta import relativedelta
import pyspark.sql.functions as psf
from pyspark.sql.types import *

def month_range(startDate, endDate):
  return [startDate + relativedelta(months=+x) for x in range((endDate.year - startDate.year)*12 + endDate.month - startDate.month + 1)]

month_range_udf = psf.udf(month_range, ArrayType(DateType()))
spark.udf.register("month_range", month_range_udf) #registers as a spark sql function

# COMMAND ----------

# DBTITLE 1,Method: PaternIndex
# import re

# def paternindex(string,s):
#     if s:
#         match = re.search(string, s)
#         if match:
#             return match.start()+1
#         else:
#             return 0
#     else:
#         return 0

# spark.udf.register("PATERNINDEX", paternindex)

# COMMAND ----------

# DBTITLE 1,Get LISHIST -- latest file
# LowIncomePeriodStartDate could be NULL/Blank, we did not handle it in code for now
# LowIncomePeriodEnd will the last day of the current year if LowIncomePeriodEnd is null or blank
LISQuery = """
WITH LIS AS(
SELECT DISTINCT --added distinct as LISHIST files can have multiple of the same record
   BeneficiaryID
  ,LowIncomePeriodStartDate AS OriginalLowIncomePeriodStartDate
  ,LowIncomePeriodEndDate AS OriginalLowIncomePeriodEndDate
  ,to_date(LowIncomePeriodStartDate,'yyyyMMdd') AS LowIncomePeriodStartDate -- leave it as same as BI team, but we did NOT check isRequried in L2 for LISHIST
  --,to_date(coalesce(LowIncomePeriodStartDate,'19000101'),'yyyyMMdd') AS LowIncomePeriodStartDate --set it to default 1/1/1900 << comment it out for now
	,CASE --If LowIncomePeriodEndDate is populated use that, else use the last day of the current year
      WHEN coalesce(nullif(nullif(LowIncomePeriodEndDate,''),'NULL'),'99991231') = '99991231' THEN date_add(add_months(date_trunc('yyyy',current_date()),12),-1)
      ELSE to_date(LowIncomePeriodEndDate,'yyyyMMdd')
   END AS LowIncomePeriodEndDate
  ,1 LISFlag
FROM LISHIST
WHERE
FileID IN(SELECT MAX(FileID) FROM LISHIST)
),
SplitLIS AS (
SELECT 
	 BeneficiaryID
  ,OriginalLowIncomePeriodStartDate
  ,OriginalLowIncomePeriodEndDate
  ,LowIncomePeriodStartDate
	,LowIncomePeriodEndDate
	,LISFlag
  ,explode(month_range(LowIncomePeriodStartDate, LowIncomePeriodEndDate)) AS LISStartDate
FROM LIS
),
FinalLIS AS (
SELECT 
	 BeneficiaryID
  ,OriginalLowIncomePeriodStartDate
  ,OriginalLowIncomePeriodEndDate
  ,LowIncomePeriodStartDate
	,LowIncomePeriodEndDate
	,LISFlag
  ,LISStartDate
  ,Last_day(LISStartDate) AS LISEndDate
FROM SplitLIS
)
SELECT DISTINCT
	 BeneficiaryID
	,LISFlag
  ,LISStartDate
  ,LISEndDate
FROM FinalLIS
WHERE
LISStartDate <= to_date(concat(year(current_date()), '-12', '-01'), 'yyyy-MM-dd')
-- current year /12/01
--month(current_date()) = month(LISStartDate)
--AND
--year(current_date()) = year(LISStartDate)
"""

LISDF = spark.sql(LISQuery)
LISDF.createOrReplaceTempView("LISFinal")

# COMMAND ----------

# DBTITLE 1,Get PCPAttribution
PCPAttributionQuery = """
WITH PCPAttributionRank AS(
 SELECT 
     COALESCE(PlanMemberID, UniquePersonKey) AS MemberID
	 ,ProviderTIN
	 ,BillingProviderTIN
	 ,Source
   ,ProviderID
	 ,ProviderNPI
	 ,ProviderTaxonomy
	 ,ProviderLastName
	 ,ProviderFirstName
	 ,ProviderAddress1
	 ,ProviderAddress2
	 ,ProviderCity
	 ,ProviderState
	 ,ProviderZip
	 ,ProviderPhone
   ,ROW_NUMBER() OVER (PARTITION BY COALESCE(PlanMemberID, UniquePersonKey) ORDER BY Source ASC) RowNumber 
FROM PCPAttribution
WHERE FileLayoutId = 34000
  AND
    IFNULL(Source,'') <> ''
)
SELECT MemberID
		,BillingProviderTIN
		,ProviderTIN
		,Source
    ,ProviderID
		,ProviderNPI
		,ProviderTaxonomy
		,ProviderLastName
		,ProviderFirstName
		,ProviderAddress1
		,ProviderAddress2
		,ProviderCity
		,ProviderState
		,ProviderZip
		,ProviderPhone
FROM PCPAttributionRank
WHERE RowNumber = 1
"""

PcpAttributionDf = spark.sql(PCPAttributionQuery)
PcpAttributionDf.createOrReplaceTempView("PCPAttributionFinal")

# COMMAND ----------

# DBTITLE 1,Create ConfigDB connection
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
  blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
  blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
  blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="
else:
  envLetter = "p"
  envUser = "PRD"+envUser
  blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
jdbcDatabase = "Configuration_DB_"+ clientCode.upper()
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Connect to ConfigDB and get FileNames (for specific layouts)
SQLConfigQuery = f"""
SELECT 
	 FileId
	--,FileName
FROM LatestFileWorkflowState
WHERE
FileLayoutId IN(
	4000,4001,4008, --Member
	3000,3001,3004, --Enrollment
	6005,6003,6008, --Provider
	10000,10001,10002,10007, --Product
	15000,15001--CMMR 
)
"""

pushdown_query = "(" + SQLConfigQuery + ") a" 
#Gets the outbound file layout description
FileRegistrationDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
FileRegistrationDF.createOrReplaceTempView("FileRegistration")

# COMMAND ----------

# DBTITLE 1,LatestMemberEnrollment (based on FileID)
MemberEnrollmentSQLQuery = """
WITH LatestMemberEnrollment AS(
SELECT
     me.UniquePersonKey
    ,me.BeneficiaryID
    ,me.PlanMemberID
    ,me.StartDate
    ,me.EndDate
    ,me.CMSContractNumber
    ,me.ProductID
    ,me.PBP
    ,coalesce(LEFT(me.MemberGroupCode,5),'') AS MemberGroupCode
    ,me.Pharmacy
    ,fr.FileId
    ,RANK() OVER(ORDER BY fr.FileID DESC) AS LatestFile
FROM MemberEnrollment me
    INNER JOIN FileRegistration fr
      ON me.FileID = fr.FileID
WHERE
coalesce(EndDate,'9999-12-31') >= add_months(current_date(), -24) --go 2 years back? -- also note this filters prior to the RANKING 
AND
StartDate <= last_day(current_date())
),
FinalMemberEnrollment AS(
SELECT 
     UniquePersonKey
    ,BeneficiaryID
    ,PlanMemberID
    ,StartDate
    ,EndDate
    ,CMSContractNumber
    ,ProductID
    ,PBP
    ,MemberGroupCode
    ,Pharmacy
    ,FileId
    ,ROW_NUMBER() OVER(PARTITION BY coalesce(UniquePersonKey,PlanMemberID) ORDER BY StartDate DESC) RowNumber 
FROM LatestMemberEnrollment 
WHERE 
LatestFile = 1
)
SELECT
     COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None')) AS MemberID
    ,BeneficiaryID
    ,UniquePersonKey
    ,PlanMemberID
    ,StartDate
    ,EndDate
    ,CMSContractNumber
    ,ProductID
    ,PBP
    ,MemberGroupCode
    ,Pharmacy
    ,FileId
FROM FinalMemberEnrollment
WHERE
RowNumber = 1
"""

MemberEnrollmentDF = spark.sql(MemberEnrollmentSQLQuery)
MemberEnrollmentDF.createOrReplaceTempView("LatestMemberEnrollment")

# COMMAND ----------

# DBTITLE 1,LatestOriginalMemberEnrollment (based on FileID)
OriginalEnrollmentSQLQuery = """
WITH OriginalEnrollment AS (
SELECT 
     me.UniquePersonKey
    ,me.PlanMemberID
    ,me.StartDate
    ,fr.FileId
    ,RANK() OVER (PARTITION BY coalesce(me.UniquePersonKey,me.PlanMemberID) ORDER BY fr.FileID DESC,me.StartDate) AS RankNumber
FROM MemberEnrollment me
    JOIN FileRegistration fr 
      ON ME.FileID = FR.FileID
)
SELECT
   COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None')) AS MemberID
  ,FileId
  ,MIN(StartDate) AS ENRL_MIN_BEGIN_DATE 
FROM OriginalEnrollment  
WHERE
RankNumber = 1
GROUP BY 
   COALESCE(nullif(UniquePersonKey,'None'),nullif(PlanMemberID,'None'))
  ,FileId
"""

OriginalEnrollmentDF = spark.sql(OriginalEnrollmentSQLQuery)
OriginalEnrollmentDF.createOrReplaceTempView("LatestOriginalMemberEnrollment")

# COMMAND ----------

# DBTITLE 1,LatestProduct (based on FileID) --not filtered yet
#7.9 MemberGroupCode will not be populated -- will only work for 7.12
LatestProductSQLQuery = """
WITH FinalProduct AS(
SELECT DISTINCT 
   p.PlanGroupID
  ,p.PlanGroupName
  ,p.PlanSubGroup
  ,p.PlanSubType
  ,p.ProductType
  ,p.StartDate
  ,p.EndDate
  ,RANK() OVER(PARTITION BY p.PlanGroupID ORDER BY fr.FileID DESC,p.StartDate DESC) AS RankNumber
FROM Product p
  INNER JOIN FileRegistration fr 
    ON p.FileID = fr.FileID
)
SELECT 
   PlanGroupID
  ,PlanGroupName
  ,PlanSubGroup
  ,PlanSubType
  ,ProductType
  ,StartDate
  ,EndDate
FROM FinalProduct
WHERE
RankNumber = 1
AND
StartDate < EndDate
"""

LatestProductDF = spark.sql(LatestProductSQLQuery)
LatestProductDF.createOrReplaceTempView("LatestProduct")

# COMMAND ----------

# DBTITLE 1,Expiry Date (by FileID)
ExpiryDateSQLQuery = """
WITH ExpiryDate AS(
SELECT DISTINCT
   s.PlanMemberID
  ,s.StartDate
  ,s.FileLayoutID
  ,ROW_NUMBER() OVER(PARTITION BY s.PlanMemberID ORDER BY fr.FileID DESC) AS RowNumber 
FROM SpanOther s
  INNER JOIN FileRegistration fr
    ON s.FileID = fr.FileID
WHERE 
--s.FileLayoutID IN(3004) --PremeraMemberEnrollment --filterin this out and allowing all spans in
--AND 
s.SpanType='EXP'
)
SELECT 
   PlanMemberID
  ,StartDate
  ,FileLayoutID
FROM ExpiryDate
WHERE
RowNumber = 1
"""

ExpiryDateDF = spark.sql(ExpiryDateSQLQuery)
ExpiryDateDF.createOrReplaceTempView("LatestExpiryDate")

# COMMAND ----------

# DBTITLE 1,LatestMMRIndicators -- Filters MMR for only the current month?
MMRIndicatorsSQLQuery = """
WITH TypeIndicator AS (
SELECT BeneficiaryID,HOSPICE_IND,ESRD_IND,INSTL_IND,PaymentAdjustmentStartDate,PaymentAdjustmentEndDate
FROM (
SELECT DISTINCT 
   BeneficiaryID
  ,CASE WHEN coalesce(AdjustmentReasonCode,'') IN('','07') AND HOSPICE = 'Y' THEN 1 ELSE 0 END AS HOSPICE_IND
  ,CASE WHEN coalesce(AdjustmentReasonCode,'') IN('','08') AND ESRD = 'Y' THEN 1 ELSE 0 END ESRD_IND
  ,CASE WHEN coalesce(AdjustmentReasonCode,'') = '' AND LTIFlag = 'Y' THEN 1 ELSE 0 END INSTL_IND
  ,to_date(PaymentAdjustmentStartDate,'yyyyMMdd') AS PaymentAdjustmentStartDate
  ,to_date(PaymentAdjustmentEndDate,'yyyyMMdd') AS PaymentAdjustmentEndDate
  ,Row_Number()Over(Partition By BeneficiaryID order by FileID desc,PaymentAdjustmentStartDate desc) as RowNum
FROM MMR
WHERE
current_date() BETWEEN to_date(PaymentAdjustmentStartDate,'yyyyMMdd') AND to_date(PaymentAdjustmentEndDate,'yyyyMMdd')
)mmr WHERE mmr.RowNum=1
)
SELECT 
   BeneficiaryID
  ,HOSPICE_IND
  ,ESRD_IND
  ,INSTL_IND
  ,PaymentAdjustmentStartDate
  ,PaymentAdjustmentEndDate
FROM TypeIndicator
"""

MMRIndicatorsDF = spark.sql(MMRIndicatorsSQLQuery)
MMRIndicatorsDF.createOrReplaceTempView("LatestMMRIndicators")

# COMMAND ----------

# DBTITLE 1,LatestConsolidatedMMR --by FileId and CMMRFileCreateDate
ConsolidatedMMRSQLQuery = """
WITH RawCMMR AS (
  SELECT DISTINCT FILEID
  	,CMMRFileCreateDate
  	,ROW_NUMBER()OVER(ORDER BY CMMRFileCreateDate desc, FileID DESC) RANK
  FROM ConsolidatedMMR 
  WHERE FILELAYOUTID in (15000,15001)
  GROUP BY FILEID,CMMRFileCreateDate
)
,LatestCMMR AS (
	SELECT FILEID
		,CMMRFileCreateDate
	FROM RawCMMR
  	WHERE RANK=1
)
,RiskScore AS (
	SELECT DISTINCT cmmr.BeneficiaryID
        ,cmmr.RiskAdjusterFactorA AS RISK_SCORE_cMMR
		,cmmr.EnrollmentYear
        ,to_date(concat_ws("-",CAST(cmmr.EnrollmentYear AS STRING)
			,CAST(MONTH(ifnull(to_timestamp(left(cmmr.EnrollmentMonth,3), "MMM")
				,to_timestamp(right(cmmr.EnrollmentMonth,3), "MMM"))) AS STRING),'01'), "yyyy-MM-dd") AS DATE_ENROLLMENTMONTH
    FROM ConsolidatedMMR cmmr
    INNER JOIN LatestCMMR fr
    ON cmmr.FILEID = fr.FILEID
)
,RiskScoreRnk AS (
	SELECT BeneficiaryID
		,RISK_SCORE_cMMR
		,EnrollmentYear
		,DATE_ENROLLMENTMONTH
    	,RANK() OVER (PARTITION BY BeneficiaryID ORDER BY DATE_ENROLLMENTMONTH DESC) RNK
    FROM RiskScore
)
SELECT BeneficiaryID
	,RISK_SCORE_cMMR
FROM RiskScoreRnk
WHERE RNK = 1
"""

ConsolidatedMMRDF = spark.sql(ConsolidatedMMRSQLQuery)
ConsolidatedMMRDF.createOrReplaceTempView("LatestConsolidatedMMR")

# COMMAND ----------

# DBTITLE 1,LatestMemberRoster -- by RosterMonth
MemberRosterSQLQuery = """
SELECT 
   PlanMemberId AS ClientMemberID
  ,POCode
  ,POName
  ,PracticeCode
  ,PracticeName
  ,ProviderID as ClientProviderID
  ,ProviderNPI
  ,ProviderLastName
  ,ProviderFirstName
  ,ProviderAddress1
  ,ProviderAddress2
  ,ProviderCity
  ,ProviderState
  ,ProviderZipCode
  ,ProviderPhoneNumber
FROM MemberRoster
WHERE
CAST(RosterMonth AS int) = (SELECT MAX(CAST(RosterMonth AS int)) FROM MemberRoster)
"""

MemberRosterDF = spark.sql(MemberRosterSQLQuery)
MemberRosterDF.createOrReplaceTempView("LatestMemberRoster")

# COMMAND ----------

# DBTITLE 1,LatestProvider-- by FileID
ProviderSQLQuery = """
WITH FinalProvider AS(
SELECT DISTINCT 
   p.ProviderID
  ,p.TaxonomyCode1
  ,p.AltProvReporting3
  ,RANK() OVER(ORDER BY fr.FileID DESC) AS RankNumber
FROM Provider p
    INNER JOIN FileRegistration fr 
      ON p.FileId = fr.FileId
)
SELECT 
   ProviderID
  ,TaxonomyCode1
  ,AltProvReporting3
FROM FinalProvider
WHERE
RankNumber = 1
"""

ProviderDF = spark.sql(ProviderSQLQuery)
ProviderDF.createOrReplaceTempView("LatestProvider")

# COMMAND ----------

# DBTITLE 1,MemberInformation --note is using the actual LatestMemberId
MemberPersonSQLQuery = """
WITH Members AS(
SELECT DISTINCT
   COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID --B
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID --A --Q360File output
  ,COALESCE(nullif(lmpb.UniquePersonKey,'None'),nullif(lmpb.PlanMemberID,'None')) AS LatestMemberID --not being output anywhere --C
FROM MemberPersonBridge mpb --current member
  LEFT JOIN MemberPersonBridge ompb --Original Member
      ON ompb.BISInternalPersonId = mpb.BISInternalPersonId
      AND ompb.IsOriginalMemberId = 1
  LEFT JOIN MemberPersonBridge lmpb --latest member
      ON lmpb.BISInternalPersonId = mpb.BISInternalPersonId
      AND lmpb.IsCurrent = 1
)
SELECT 
   MemberID
  ,OriginalMemberID
  ,LatestMemberID
FROM Members
"""

MemberPersonDF = spark.sql(MemberPersonSQLQuery)
MemberPersonDF.createOrReplaceTempView("MemberInformation")

# COMMAND ----------

# DBTITLE 1,LatestMember -- by FileID
MemberSQLQuery = """
WITH Members AS(
SELECT 
       COALESCE(nullif(m.UniquePersonKey,'None'),nullif(m.PlanMemberID,'None')) AS MemberID
      ,m.PlanMemberId
      ,m.UniquePersonKey
      ,m.BeneficiaryID
      ,m.FirstName
      ,m.LastName
      ,m.Gender
      ,m.DateOfBirth
      ,m.DeceasedDate
      ,m.MailingAddressLine1
      ,m.MailingAddressLine2
      ,m.PermanentAddressLine1
      ,m.PermanentAddressLine2
      ,m.MailingCity
      ,m.PermanentCity
      ,m.MailingState
      ,m.PermanentState
      ,MailingZipCode
      ,m.PermanentZipCode
      ,m.MailingCounty
      ,m.PermanentCounty
      ,m.PhoneNumber
      ,m.Email
      ,RANK() OVER (ORDER BY fr.FileID DESC) AS RankNumber 
FROM Member m
    INNER JOIN FileRegistration fr 
      ON m.FileId = fr.FileId
)
SELECT
       MemberID
      ,PlanMemberId
      ,UniquePersonKey
      ,BeneficiaryID
      ,FirstName
      ,LastName
      ,Gender
      ,DateOfBirth
      ,DeceasedDate
      ,MailingAddressLine1
      ,MailingAddressLine2
      ,PermanentAddressLine1
      ,PermanentAddressLine2
      ,MailingCity
      ,PermanentCity
      ,MailingState
      ,PermanentState
      ,MailingZipCode
      ,PermanentZipCode
      ,MailingCounty
      ,PermanentCounty
      ,PhoneNumber
      ,Email
FROM Members 
WHERE
RankNumber = 1
"""

MemberDF = spark.sql(MemberSQLQuery)
MemberDF.createOrReplaceTempView("LatestMember")

# COMMAND ----------

# DBTITLE 1,Latest ProviderRollup for BCBSNE
LatestProviderRollupQuerry = """
 WITH LatestFileId AS (
	SELECT MAX(FILEID) AS FileId
	FROM ProviderRollUp
	WHERE FILELAYOUTID = 21001 ---21001 NE
)
SELECT Tier1BillingProviderTIN
  	,Tier3ID as POCode
		,Tier3Description as POName
		,AltProvReporting2
  FROM ProviderRollup pr
  INNER JOIN LatestFileId lf 
  ON pr.Fileid = lf.Fileid
 """

ProviderRollupDF = spark.sql(LatestProviderRollupQuerry)
ProviderRollupDF.createOrReplaceTempView("LatestProviderRollup")

# COMMAND ----------

# DBTITLE 1,Final query
from pyspark.sql.functions import regexp_replace

FinalSQLQuery = """
WITH AlmostFinalQuery AS(
SELECT DISTINCT
     date_format(current_date(), 'yyyyMM') AS YEAR_MTH_KEY
    ,mi.OriginalMemberId AS MEMBER_ID
    ,mi.OriginalMemberId AS ALT_MEMBER_ID9
    ,mi.MemberId AS ALT_MEMBER_ID_CURR
    ,m.BeneficiaryID AS MBI
    ,UPPER(m.FirstName) AS MEMBER_FIRST_NAME
    ,UPPER(m.LastName) AS MEMBER_LAST_NAME
    ,UPPER(m.Gender) AS MEMBER_GENDER
    ,m.DateOfBirth AS MEMBER_DOB 
		,COALESCE(m.DeceasedDate,s.StartDate) AS MEMBER_DOD  
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingAddressLine1) ELSE UPPER(m.PermanentAddressLine1) END AS MEMBER_ADDRESS1
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingAddressLine2) ELSE UPPER(m.PermanentAddressLine2) END AS MEMBER_ADDRESS2
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingCity) ELSE UPPER(m.PermanentCity) END AS MEMBER_CITY
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingState) ELSE UPPER(m.PermanentState) END AS MEMBER_STATE
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingZipCode) ELSE UPPER(m.PermanentZipCode) END AS MEMBER_ZIP
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingCounty) ELSE UPPER(m.PermanentCounty) END AS MEMBER_COUNTY
    ,CASE 
        WHEN COALESCE(m.MailingAddressLine1,'')<>'' THEN 'MAILING' WHEN COALESCE(m.PermanentAddressLine1,'')<>'' THEN 'PERMANENT'
        WHEN COALESCE(m.PermanentAddressLine1,'')='' AND COALESCE(m.MailingAddressLine1,'')='' THEN '' 
     END AS MEMBER_ADDRESS_TYPE
    ,regexp_replace(m.PhoneNumber, '[^0-9]+', '') AS MEMBER_PHONE
    ,m.Email AS MEMBER_EMAIL
    ,em.ENRL_MIN_BEGIN_DATE AS ENRL_MIN_BEGIN_DATE
		,me.StartDate AS ENRL_BEGIN_DT
		,me.EndDate AS ENRL_END_DT	    
    ,me.CMSContractNumber AS PLAN_ID
    ,me.ProductID AS PRODUCT_NAME
    ,me.PBP
    ,me.MemberGroupCode AS MEMBER_GROUP_NUMBER
    ,p.PlanGroupName AS MEMBER_GROUP_NAME
    ,p.ProductType AS MEMBER_GROUP_CATEGORY
    ,CASE WHEN me.Pharmacy = 'Y' THEN 1 ELSE 0 END RX_FLAG
    ,mi.Hospice_IND
    ,mi.ESRD_IND
    ,mi.INSTL_IND
    ,COALESCE(lis.LISFlag,0) AS LIS_IND
    ,cmmr.RISK_SCORE_cMMR
    ,mr.POName AS PO_Name
    ,mr.POCode AS PO_ID
    ,mr.PracticeCode AS PU_ID
    ,mr.PracticeName AS PU_NAME
    ,mr.ClientProviderID AS Provider_ID
    ,mr.ProviderNPI AS NPI
    ,UPPER(mr.ProviderLastName) AS Provider_Last_Name
    ,UPPER(mr.ProviderFirstName) AS Provider_First_Name
    ,UPPER(mr.ProviderAddress1) AS Provider_Address1
    ,UPPER(mr.ProviderAddress2) AS Provider_Address2
    ,UPPER(mr.ProviderCity) AS Provider_City
    ,UPPER(mr.ProviderState) AS Provider_State 
    ,mr.ProviderZipCode AS Provider_Zip
    ,regexp_replace(mr.ProviderPhoneNumber, '[^0-9]+', '')AS PROVIDER_PHONE
    ,COALESCE(pf.TaxonomyCode1,ptax.TaxonomyCode) AS PROVIDER_TAXONOMY
    ,COALESCE(ps.CMSSPECIALTYCODE,ptax.CMSSpecialtyCode) AS PROVIDER_SPECIALTY
    ,current_timestamp() AS LOAD_DATE
    ,pf.AltProvReporting3 AS ALT_PROVIDER_REPORTING_01
    ,cbtt.BillingProviderTIN AS BILLING_PROVIDER_TIN
    ,cbtt.Source AS ATTRIBUTION_SOURCE
FROM LatestMember m
    INNER JOIN LatestMemberEnrollment me  
        ON m.MemberID = me.MemberID
    LEFT JOIN LatestOriginalMemberEnrollment em
        ON m.MemberID = em.MemberID
    LEFT JOIN LatestProduct p --May get dups
        ON p.PlanGroupID = me.MemberGroupCode
    LEFT JOIN LatestExpiryDate s
        ON m.MemberID = s.PlanMemberID
    LEFT JOIN LatestMMRIndicators mi
        ON m.BeneficiaryID = mi.BeneficiaryID
    LEFT JOIN LatestConsolidatedMMR cmmr 
            ON m.BeneficiaryID = cmmr.BeneficiaryID
    LEFT JOIN LISFinal lis
        ON me.BeneficiaryID = lis.BeneficiaryID
        AND me.EndDate  BETWEEN lis.LISStartDate AND lis.LISEndDate
    LEFT JOIN LatestMemberRoster mr
        ON m.MemberID = mr.ClientMemberID
    LEFT JOIN LatestProvider pf
        ON pf.ProviderID = mr.ClientProviderID
    LEFT JOIN ProviderTaxoFinal ptax  
        ON mr.ProviderNPI = ptax.NPI
    LEFT JOIN ProviderSpecialityFinal ps
        ON COALESCE(pf.TaxonomyCode1,ptax.TaxonomyCode) = ps.TAXONOMYCODE
    LEFT JOIN PCPAttributionFinal cbtt 
        ON cbtt.MemberID = m.MemberID
    INNER JOIN MemberInformation mi
        ON m.MemberID = mi.MemberId
),
FinalQuery AS(
SELECT 
	 YEAR_MTH_KEY
	,MEMBER_ID
	,ALT_MEMBER_ID9
	,ALT_MEMBER_ID_CURR
	,MBI
	,MEMBER_FIRST_NAME
	,MEMBER_LAST_NAME
	,MEMBER_GENDER
	,MEMBER_DOB
	,MEMBER_DOD
	,MEMBER_ADDRESS1
	,MEMBER_ADDRESS2
	,MEMBER_CITY
	,MEMBER_STATE
	,MEMBER_ZIP
	,MEMBER_COUNTY
	,MEMBER_ADDRESS_TYPE
	,MEMBER_PHONE
	,MEMBER_EMAIL
	,ENRL_MIN_BEGIN_DATE
	,ENRL_BEGIN_DT
	,ENRL_END_DT
	,PLAN_ID
	,PRODUCT_NAME
	,PBP
	,MEMBER_GROUP_NUMBER
	,MEMBER_GROUP_NAME
	,MEMBER_GROUP_CATEGORY
	,RX_FLAG
	,Hospice_IND
	,ESRD_IND
	,INSTL_IND
	,LIS_IND
	,RISK_SCORE_cMMR
	,PO_Name
	,PO_ID
	,PU_ID
	,PU_NAME
	,Provider_ID
	,NPI
	,Provider_Last_Name
	,Provider_First_Name
	,Provider_Address1
	,Provider_Address2
	,Provider_City
	,Provider_State
	,Provider_Zip
	,PROVIDER_PHONE
	,PROVIDER_TAXONOMY
	,PROVIDER_SPECIALTY
	,LOAD_DATE
	,ALT_PROVIDER_REPORTING_01
	,BILLING_PROVIDER_TIN
	,ATTRIBUTION_SOURCE
	,CASE WHEN MEMBER_DOD IS NOT NULL THEN 1 ELSE 0 END AS MEMBER_DEATH_IND
	,CASE 
		WHEN MEMBER_DOD IS NOT NULL THEN 0 
		WHEN ENRL_END_DT >= current_date() THEN 1 
		ELSE 0 
	 END AS CURR_CVG_IND
	,CASE 
		WHEN MEMBER_DOD IS NOT NULL THEN 'Not Attributed'
		WHEN ENRL_END_DT >= current_date() AND coalesce(Provider_ID,'') <> '' THEN 'Attributed' 
		ELSE 'Not Attributed' 
	 END AS ATTRIBUTION_CLASS
FROM AlmostFinalQuery
)
SELECT 
	 YEAR_MTH_KEY
	,MEMBER_ID
	,ALT_MEMBER_ID9
	,ALT_MEMBER_ID_CURR
	,MBI
	,MEMBER_FIRST_NAME
	,MEMBER_LAST_NAME
	,MEMBER_GENDER
	,date_format(MEMBER_DOB, 'yyyyMMdd') AS MEMBER_DOB
	,date_format(MEMBER_DOD, 'yyyyMMdd') AS MEMBER_DOD
	,MEMBER_ADDRESS1
	,MEMBER_ADDRESS2
	,MEMBER_CITY
	,MEMBER_STATE
	,MEMBER_ZIP
	,MEMBER_COUNTY
	,MEMBER_ADDRESS_TYPE
	,MEMBER_PHONE
	,MEMBER_EMAIL
	,date_format(ENRL_MIN_BEGIN_DATE, 'yyyyMMdd') AS ENRL_MIN_BEGIN_DATE
	,date_format(ENRL_BEGIN_DT, 'yyyyMMdd') AS ENRL_BEGIN_DT
	,date_format(ENRL_END_DT, 'yyyyMMdd') AS ENRL_END_DT
	,PLAN_ID
	,PRODUCT_NAME
	,PBP
	,MEMBER_GROUP_NUMBER
	,MEMBER_GROUP_NAME
	,MEMBER_GROUP_CATEGORY
	,RX_FLAG
	,Hospice_IND
	,ESRD_IND
	,INSTL_IND
	,LIS_IND
	,RISK_SCORE_cMMR
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PO_Name END AS PO_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PO_ID END AS PO_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PU_ID END AS PU_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PU_NAME END AS PU_NAME
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_ID END AS Provider_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE NPI END AS NPI
  ,'' AS TIN
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Last_Name END AS Provider_Last_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_First_Name END AS Provider_First_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Address1 END AS Provider_Address1
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Address2 END AS Provider_Address2
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_City END AS Provider_City
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_State END AS Provider_State
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Zip END AS Provider_Zip
  ,'' AS PROVIDER_COUNTY
  ,'' AS PROVIDER_EMAIL
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_PHONE END AS PROVIDER_PHONE
  ,'' AS PROVIDER_FAX
  ,'' AS PROVIDER_TYPE
  ,'' AS PCMH
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_TAXONOMY END AS PROVIDER_TAXONOMY
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_SPECIALTY END AS PROVIDER_SPECIALTY
  ,'' AS MEMBER_DO_NOT_CONTACT
	,LOAD_DATE
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE ALT_PROVIDER_REPORTING_01 END AS ALT_PROVIDER_REPORTING_01
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE BILLING_PROVIDER_TIN END AS BILLING_PROVIDER_TIN
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE ATTRIBUTION_SOURCE END AS ATTRIBUTION_SOURCE
	,MEMBER_DEATH_IND
	,CURR_CVG_IND
	,ATTRIBUTION_CLASS
FROM FinalQuery
"""

# COMMAND ----------

# DBTITLE 1,Final query  -Bcbsne
BcbsneFinalSQLQuery = """
WITH AlmostFinalQuery AS(
SELECT DISTINCT
     date_format(current_date(), 'yyyyMM') AS YEAR_MTH_KEY
    ,mi.OriginalMemberId AS MEMBER_ID
    ,mi.OriginalMemberId AS ALT_MEMBER_ID9
    ,mi.MemberId AS ALT_MEMBER_ID_CURR
    ,m.BeneficiaryID AS MBI
    ,UPPER(m.FirstName) AS MEMBER_FIRST_NAME
    ,UPPER(m.LastName) AS MEMBER_LAST_NAME
    ,UPPER(m.Gender) AS MEMBER_GENDER
    ,m.DateOfBirth AS MEMBER_DOB 
	,COALESCE(m.DeceasedDate,s.StartDate) AS MEMBER_DOD  
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingAddressLine1) ELSE UPPER(m.PermanentAddressLine1) END AS MEMBER_ADDRESS1
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingAddressLine2) ELSE UPPER(m.PermanentAddressLine2) END AS MEMBER_ADDRESS2
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingCity) ELSE UPPER(m.PermanentCity) END AS MEMBER_CITY
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingState) ELSE UPPER(m.PermanentState) END AS MEMBER_STATE
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingZipCode) ELSE UPPER(m.PermanentZipCode) END AS MEMBER_ZIP
    ,CASE WHEN COALESCE(m.MailingAddressLine1,'') <> '' THEN UPPER(m.MailingCounty) ELSE UPPER(m.PermanentCounty) END AS MEMBER_COUNTY
    ,CASE 
        WHEN COALESCE(m.MailingAddressLine1,'')<>'' THEN 'MAILING' WHEN COALESCE(m.PermanentAddressLine1,'')<>'' THEN 'PERMANENT'
        WHEN COALESCE(m.PermanentAddressLine1,'')='' AND COALESCE(m.MailingAddressLine1,'')='' THEN '' 
     END AS MEMBER_ADDRESS_TYPE
    ,regexp_replace(m.PhoneNumber, '[^0-9]+', '') AS MEMBER_PHONE
    ,m.Email AS MEMBER_EMAIL
    ,em.ENRL_MIN_BEGIN_DATE AS ENRL_MIN_BEGIN_DATE
		,me.StartDate AS ENRL_BEGIN_DT
		,me.EndDate AS ENRL_END_DT	    
    ,me.CMSContractNumber AS PLAN_ID
    ,me.ProductID AS PRODUCT_NAME
    ,me.PBP
    ,me.MemberGroupCode AS MEMBER_GROUP_NUMBER
    ,p.PlanGroupName AS MEMBER_GROUP_NAME
    ,p.ProductType AS MEMBER_GROUP_CATEGORY
    ,CASE WHEN me.Pharmacy = 'Y' THEN 1 ELSE 0 END RX_FLAG
    ,mi.Hospice_IND
    ,mi.ESRD_IND
    ,mi.INSTL_IND
    ,COALESCE(lis.LISFlag,0) AS LIS_IND
    ,cmmr.RISK_SCORE_cMMR
    ,mr.POName AS PO_Name --ProviderRollup
    ,mr.POCode AS PO_ID   --ProviderRollup
    ,'' AS PU_ID
    ,'' AS PU_NAME
    ,pcpatt.ProviderID AS Provider_ID --bcbsne
    ,pcpatt.ProviderNPI AS NPI --bcbsne
    ,pcpatt.ProviderTIN AS TNI --bcbsne
    ,UPPER(pcpatt.ProviderLastName) AS Provider_Last_Name --bcbsne
    ,UPPER(pcpatt.ProviderFirstName) AS Provider_First_Name --bcbsne
    ,UPPER(pcpatt.ProviderAddress1) AS Provider_Address1 --bcbsne
    ,UPPER(pcpatt.ProviderAddress2) AS Provider_Address2 --bcbsne
    ,UPPER(pcpatt.ProviderCity) AS Provider_City --bcbsne
    ,UPPER(pcpatt.ProviderState) AS Provider_State --bcbsne
    ,pcpatt.ProviderZip AS Provider_Zip --bcbsne
    ,regexp_replace(pcpatt.ProviderPhone, '[^0-9]+', '')AS PROVIDER_PHONE -- bcbsne
    ,pcpatt.ProviderTIN AS TIN -- bcbsne
    ,COALESCE(pf.TaxonomyCode1,ptax.TaxonomyCode) AS PROVIDER_TAXONOMY
    ,COALESCE(ps.CMSSPECIALTYCODE,ptax.CMSSpecialtyCode) AS PROVIDER_SPECIALTY
    ,current_timestamp() AS LOAD_DATE
    ,mr.AltProvReporting2 AS ALT_PROVIDER_REPORTING_01 -- bcbsne
    ,pcpatt.BillingProviderTIN AS BILLING_PROVIDER_TIN -- bcbsne
    ,pcpatt.Source AS ATTRIBUTION_SOURCE -- bcbsne
FROM LatestMember m
    INNER JOIN LatestMemberEnrollment me  
        ON m.MemberID = me.MemberID
    LEFT JOIN LatestOriginalMemberEnrollment em
        ON m.MemberID = em.MemberID
    LEFT JOIN LatestProduct p --May get dups
        ON p.PlanGroupID = me.MemberGroupCode
    LEFT JOIN LatestExpiryDate s
        ON m.MemberID = s.PlanMemberID
    LEFT JOIN LatestMMRIndicators mi
        ON m.BeneficiaryID = mi.BeneficiaryID
    LEFT JOIN LatestConsolidatedMMR cmmr 
            ON m.BeneficiaryID = cmmr.BeneficiaryID
    LEFT JOIN LISFinal lis
        ON me.BeneficiaryID = lis.BeneficiaryID
        AND me.EndDate  BETWEEN lis.LISStartDate AND lis.LISEndDate
    LEFT JOIN PCPAttributionFinal pcpatt -- bcbsne AND OTHER
        ON pcpatt.MemberID = m.MemberID
    LEFT JOIN LatestProviderRollup mr -- bcbsne only
        ON pcpatt.BillingProviderTIN = mr.Tier1BillingProviderTIN
    LEFT JOIN LatestProvider pf
        ON pf.ProviderID = pcpatt.ProviderID
    LEFT JOIN ProviderTaxoFinal ptax  
        ON pcpatt.ProviderNPI = ptax.NPI
    LEFT JOIN ProviderSpecialityFinal ps
        ON COALESCE(pf.TaxonomyCode1,ptax.TaxonomyCode) = ps.TAXONOMYCODE
    INNER JOIN MemberInformation mi
        ON m.MemberID = mi.MemberId
),
FinalQuery AS(
SELECT 
	 YEAR_MTH_KEY
	,MEMBER_ID
	,ALT_MEMBER_ID9
	,ALT_MEMBER_ID_CURR
	,MBI
	,MEMBER_FIRST_NAME
	,MEMBER_LAST_NAME
	,MEMBER_GENDER
	,MEMBER_DOB
	,MEMBER_DOD
	,MEMBER_ADDRESS1
	,MEMBER_ADDRESS2
	,MEMBER_CITY
	,MEMBER_STATE
	,MEMBER_ZIP
	,MEMBER_COUNTY
	,MEMBER_ADDRESS_TYPE
	,MEMBER_PHONE
	,MEMBER_EMAIL
	,ENRL_MIN_BEGIN_DATE
	,ENRL_BEGIN_DT
	,ENRL_END_DT
	,PLAN_ID
	,PRODUCT_NAME
	,PBP
	,MEMBER_GROUP_NUMBER
	,MEMBER_GROUP_NAME
	,MEMBER_GROUP_CATEGORY
	,RX_FLAG
	,Hospice_IND
	,ESRD_IND
	,INSTL_IND
	,LIS_IND
	,RISK_SCORE_cMMR
	,PO_Name
	,PO_ID
	,PU_ID
	,PU_NAME
	,Provider_ID
	,NPI
	,Provider_Last_Name
	,Provider_First_Name
	,Provider_Address1
	,Provider_Address2
	,Provider_City
	,Provider_State
	,Provider_Zip
	,PROVIDER_PHONE
    ,TIN
	,PROVIDER_TAXONOMY
	,PROVIDER_SPECIALTY
	,LOAD_DATE
	,ALT_PROVIDER_REPORTING_01
	,BILLING_PROVIDER_TIN
	,ATTRIBUTION_SOURCE
	,CASE WHEN MEMBER_DOD IS NOT NULL THEN 1 ELSE 0 END AS MEMBER_DEATH_IND
	,CASE 
		WHEN MEMBER_DOD IS NOT NULL THEN 0 
		WHEN ENRL_END_DT >= current_date() THEN 1 
		ELSE 0 
	 END AS CURR_CVG_IND
	,CASE 
		WHEN MEMBER_DOD IS NOT NULL THEN 'Not Attributed'
		WHEN ENRL_END_DT >= current_date() AND coalesce(Provider_ID,'') <> '' THEN 'Attributed' 
		ELSE 'Not Attributed' 
	 END AS ATTRIBUTION_CLASS
FROM AlmostFinalQuery
)
SELECT 
	 YEAR_MTH_KEY
	,MEMBER_ID
	,ALT_MEMBER_ID9
	,ALT_MEMBER_ID_CURR
	,MBI
	,MEMBER_FIRST_NAME
	,MEMBER_LAST_NAME
	,MEMBER_GENDER
	,date_format(MEMBER_DOB, 'yyyyMMdd') AS MEMBER_DOB
	,date_format(MEMBER_DOD, 'yyyyMMdd') AS MEMBER_DOD
	,MEMBER_ADDRESS1
	,MEMBER_ADDRESS2
	,MEMBER_CITY
	,MEMBER_STATE
	,MEMBER_ZIP
	,MEMBER_COUNTY
	,MEMBER_ADDRESS_TYPE
	,MEMBER_PHONE
	,MEMBER_EMAIL
	,date_format(ENRL_MIN_BEGIN_DATE, 'yyyyMMdd') AS ENRL_MIN_BEGIN_DATE
	,date_format(ENRL_BEGIN_DT, 'yyyyMMdd') AS ENRL_BEGIN_DT
	,date_format(ENRL_END_DT, 'yyyyMMdd') AS ENRL_END_DT
	,PLAN_ID
	,PRODUCT_NAME
	,PBP
	,MEMBER_GROUP_NUMBER
	,MEMBER_GROUP_NAME
	,MEMBER_GROUP_CATEGORY
	,RX_FLAG
	,Hospice_IND
	,ESRD_IND
	,INSTL_IND
	,LIS_IND
	,RISK_SCORE_cMMR
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PO_Name END AS PO_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PO_ID END AS PO_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PU_ID END AS PU_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PU_NAME END AS PU_NAME
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_ID END AS Provider_ID
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE NPI END AS NPI
    ,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE TIN END AS TIN -- bcbsne 
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Last_Name END AS Provider_Last_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_First_Name END AS Provider_First_Name
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Address1 END AS Provider_Address1
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Address2 END AS Provider_Address2
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_City END AS Provider_City
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_State END AS Provider_State
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE Provider_Zip END AS Provider_Zip
  ,'' AS PROVIDER_COUNTY
  ,'' AS PROVIDER_EMAIL
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_PHONE END AS PROVIDER_PHONE
  ,'' AS PROVIDER_FAX
  ,'' AS PROVIDER_TYPE
  ,'' AS PCMH
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_TAXONOMY END AS PROVIDER_TAXONOMY
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE PROVIDER_SPECIALTY END AS PROVIDER_SPECIALTY
  ,'' AS MEMBER_DO_NOT_CONTACT
	,LOAD_DATE
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE ALT_PROVIDER_REPORTING_01 END AS ALT_PROVIDER_REPORTING_01
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE BILLING_PROVIDER_TIN END AS BILLING_PROVIDER_TIN
	,CASE WHEN CURR_CVG_IND=0 OR MEMBER_DEATH_IND=1 OR ATTRIBUTION_CLASS = 'Not Attributed'
    THEN '' ELSE ATTRIBUTION_SOURCE END AS ATTRIBUTION_SOURCE
	,MEMBER_DEATH_IND
	,CURR_CVG_IND
	,ATTRIBUTION_CLASS
FROM FinalQuery
"""

# COMMAND ----------

# DBTITLE 1,Final Dataframe Output --based on client

if clientCode.lower() == 'bcbsne' or clientCode.lower() == 'qaidap1' or clientCode.lower() == 'devidap1':
  print(f"Creating Final DF for client: {clientCode}")
  FinalDF = spark.sql(BcbsneFinalSQLQuery)
else :
  print(f"Creating Final DF for client: {clientCode}")
  FinalDF = spark.sql(FinalSQLQuery)

FinalDF.createOrReplaceTempView("FinalResult")

# COMMAND ----------

# DBTITLE 1,Delete existing YearMonthKey -- based on current date
DeleteSQLQuerry = """
DELETE FROM Q360MembershipStars
WHERE
YEAR_MTH_KEY = date_format(current_date(), 'yyyyMM')
"""

spark.sql(DeleteSQLQuerry) 

# COMMAND ----------

InsertSQLQuerry = """
INSERT INTO Q360MembershipStars (
   YEAR_MTH_KEY
  ,MEMBER_ID
  ,MBI
  ,MEMBER_LAST_NAME
  ,MEMBER_FIRST_NAME
  ,MEMBER_GENDER
  ,MEMBER_DOB
  ,MEMBER_DOD
  ,MEMBER_DEATH_IND
  ,MEMBER_ADDRESS1
  ,MEMBER_ADDRESS2
  ,MEMBER_CITY
  ,MEMBER_STATE
  ,MEMBER_ZIP
  ,MEMBER_COUNTY
  ,MEMBER_PHONE
  ,MEMBER_EMAIL
  ,PLAN_ID
  ,PRODUCT_NAME
  ,PBP
  ,MEMBER_GROUP_NUMBER
  ,MEMBER_GROUP_NAME
  ,MEMBER_GROUP_CATEGORY
  ,ATTRIBUTION_CLASS
  ,ENRL_MIN_BEGIN_DATE
  ,ENRL_BEGIN_DT
  ,ENRL_END_DT
  ,HOSPICE_IND
  ,ESRD_IND
  ,INSTL_IND
  ,RISK_SCORE_cMMR
  ,LIS_IND
  ,RX_FLAG
  ,PO_ID
  ,PO_NAME
  ,PU_ID
  ,PU_NAME
  ,PROVIDER_ID
  ,NPI
  ,TIN
  ,PROVIDER_LAST_NAME
  ,PROVIDER_FIRST_NAME
  ,PROVIDER_ADDRESS1
  ,PROVIDER_ADDRESS2
  ,PROVIDER_CITY
  ,PROVIDER_STATE
  ,PROVIDER_ZIP
  ,PROVIDER_COUNTY
  ,PROVIDER_EMAIL
  ,PROVIDER_PHONE
  ,PROVIDER_FAX
  ,PROVIDER_TYPE
  ,PCMH
  ,CURR_CVG_IND
  ,PROVIDER_TAXONOMY
  ,PROVIDER_SPECIALTY
  ,MEMBER_DO_NOT_CONTACT
  ,ALT_MEMBER_ID9
  ,ALT_MEMBER_ID_CURR
  ,MEMBER_ADDRESS_TYPE
  ,ALT_PROVIDER_REPORTING_01
  ,BILLING_PROVIDER_TIN
  ,ATTRIBUTION_SOURCE
  ,LOAD_DATE
)
SELECT 
   YEAR_MTH_KEY
  ,MEMBER_ID
  ,MBI
  ,MEMBER_LAST_NAME
  ,MEMBER_FIRST_NAME
  ,MEMBER_GENDER
  ,MEMBER_DOB
  ,MEMBER_DOD
  ,MEMBER_DEATH_IND
  ,MEMBER_ADDRESS1
  ,MEMBER_ADDRESS2
  ,MEMBER_CITY
  ,MEMBER_STATE
  ,MEMBER_ZIP
  ,MEMBER_COUNTY
  ,MEMBER_PHONE
  ,MEMBER_EMAIL
  ,PLAN_ID
  ,PRODUCT_NAME
  ,PBP
  ,MEMBER_GROUP_NUMBER
  ,MEMBER_GROUP_NAME
  ,MEMBER_GROUP_CATEGORY
  ,ATTRIBUTION_CLASS
  ,ENRL_MIN_BEGIN_DATE
  ,ENRL_BEGIN_DT
  ,ENRL_END_DT
  ,HOSPICE_IND
  ,ESRD_IND
  ,INSTL_IND
  ,RISK_SCORE_cMMR
  ,LIS_IND
  ,RX_FLAG
  ,PO_ID
  ,PO_NAME
  ,PU_ID
  ,PU_NAME
  ,PROVIDER_ID
  ,NPI
  ,TIN
  ,PROVIDER_LAST_NAME
  ,PROVIDER_FIRST_NAME
  ,PROVIDER_ADDRESS1
  ,PROVIDER_ADDRESS2
  ,PROVIDER_CITY
  ,PROVIDER_STATE
  ,PROVIDER_ZIP
  ,PROVIDER_COUNTY
  ,PROVIDER_EMAIL
  ,PROVIDER_PHONE
  ,PROVIDER_FAX
  ,PROVIDER_TYPE
  ,PCMH
  ,CURR_CVG_IND
  ,PROVIDER_TAXONOMY
  ,PROVIDER_SPECIALTY
  ,MEMBER_DO_NOT_CONTACT
  ,ALT_MEMBER_ID9
  ,ALT_MEMBER_ID_CURR
  ,MEMBER_ADDRESS_TYPE
  ,ALT_PROVIDER_REPORTING_01
  ,BILLING_PROVIDER_TIN
  ,ATTRIBUTION_SOURCE
  ,LOAD_DATE
FROM FinalResult
"""

spark.sql(InsertSQLQuerry) 
