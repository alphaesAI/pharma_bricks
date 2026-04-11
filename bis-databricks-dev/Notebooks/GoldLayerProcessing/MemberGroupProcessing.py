# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")

container = dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,Defined File Paths
mePath =  "/mnt/"+ container + "/consolidated/MA/Data/MemberEnrollment"
soPath =  "/mnt/"+ container + "/consolidated/MA/Data/SpanOther"
goldPath = "/mnt/"+ container + "/Gold/MA/Client/MemberGroup"
returnStr = "["

# COMMAND ----------

# DBTITLE 1,Method: check file path
#will be used to check distributed file system paths. sc exposes the java api to python and scala
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

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

# DBTITLE 1,SQL to Pull from MemOut and Populate Open EndDate
memOutSql = """
WITH MemberEnrollmentRaw AS (
SELECT DISTINCT
   mo.SubscriberID
	,mo.BeneficiaryID
  ,to_date(StartDate,"yyyy-MM-dd") AS StartDate  
  ,to_date(IfNull(mo.EndDate,to_date(concat_ws("-",CAST(YEAR(mo.StartDate) AS STRING),'12','31'), "yyyy-MM-dd")), "yyyy-MM-dd")  AS EndDate  
  ,mo.CMSContractNumber
	,mo.MemberGroupCode AS GroupNumber
  ,mo.FileID
  ,DENSE_RANK() OVER(PARTITION BY mo.BeneficiaryId, to_date(StartDate,"yyyy-MM-dd") , to_date(IfNull(mo.EndDate,to_date(concat_ws("-",CAST(YEAR(mo.StartDate) AS STRING),'12','31'), "yyyy-MM-dd")), "yyyy-MM-dd")ORDER BY mo.FileID DESC) AS RowNumber
FROM MemOutRaw mo
WHERE upper(mo.filelayoutdescription) like '%MEMOUT%'
  AND IFNULL(mo.startdate,'') <> ''
),
BaseMemberEnrollment AS (
SELECT
   SubscriberID
	,BeneficiaryID
	,StartDate
	,EndDate
	,CMSContractNumber
	,GroupNumber
	,FileID
FROM MemberEnrollmentRaw
WHERE 
RowNumber = 1
)
SELECT
   SubscriberID
	,BeneficiaryID
	,StartDate
	,EndDate
	,CMSContractNumber
	,GroupNumber
	,FileID
FROM BaseMemberEnrollment
"""

# COMMAND ----------

# DBTITLE 1,SQL to Pull from Span Other and Populate Open EndDate
spanOtherSql = """
WITH SpanOther AS(
SELECT DISTINCT
   so.BeneficiaryID
  ,so.SubscriberID
  ,to_date(StartDate,"yyyy-MM-dd") AS StartDate
  ,to_date(IfNull(so.EndDate,to_date(concat_ws("-",CAST(YEAR(so.StartDate) AS STRING),'12','31'), "yyyy-MM-dd")), "yyyy-MM-dd")  AS EndDate
  ,so.Subgroup
  ,so.FileID
  ,DENSE_RANK() OVER(PARTITION BY BeneficiaryId, to_date(StartDate,"yyyy-MM-dd"), to_date(IfNull(so.EndDate,to_date(concat_ws("-",CAST(YEAR(so.StartDate) AS STRING),'12','31'), "yyyy-MM-dd")), "yyyy-MM-dd") ORDER BY so.FileId DESC) AS RowNumber
FROM SpanOtherRaw so
WHERE upper(so.filedescription) like '%MEMOUT%'
    AND so.SpanType='GRP'
    AND IFNULL(so.startdate,'') <> ''
),
BaseSpanOther AS (
SELECT
   BeneficiaryID
  ,SubscriberID
  ,StartDate
  ,EndDate
  ,Subgroup
  ,FileID
FROM SpanOther
where RowNumber = 1
)
SELECT
   BeneficiaryID
  ,SubscriberID
  ,StartDate
  ,EndDate
  ,Subgroup
  ,FileID
FROM BaseSpanOther
"""

# COMMAND ----------

# DBTITLE 1,Get Member Group Info with FileId From two tables
sqlStmt = """
SELECT DISTINCT
   mo.SubscriberID
  ,mo.BeneficiaryID
  ,mo.StartDate
  ,mo.EndDate
  ,mo.CMSContractNumber
  ,mo.GroupNumber
  ,so.Subgroup as GroupSuffix
  ,CAST(mo.FileID AS BIGINT) AS SourceFileID
  ,current_timestamp() AS LoadDateTime
FROM MemOutSplit mo
   INNER JOIN SpanOtherSplit so
   ON mo.BeneficiaryID = so.BeneficiaryID 
      AND mo.SubscriberID = so.SubscriberID 
      AND mo.StartDate = so.StartDate
      AND mo.EndDate = so.EndDate
      AND mo.FileID = so.FileID
"""

# COMMAND ----------

# DBTITLE 1,Filter MemberEnrollment -- split by month
filteredMemberEnrollment = """
WITH ExplodeDates AS(
SELECT 
   SubscriberID
  ,BeneficiaryID
  ,StartDate AS OriginalStartDate
  ,EndDate AS OriginalEndDate
  ,CMSContractNumber
  ,GroupNumber
  ,FileID
  ,explode(month_range(StartDate, EndDate)) AS StartDate
FROM MemOut
),
ExplodedMemoutDates AS(
SELECT  
   SubscriberID
  ,BeneficiaryID
  ,OriginalStartDate
  ,OriginalEndDate
  ,CMSContractNumber
  ,GroupNumber
  ,FileID
  ,StartDate
  ,CASE WHEN OriginalStartDate = OriginalEndDate THEN OriginalEndDate ELSE last_day(StartDate) END AS EndDate
FROM ExplodeDates
),
FinalMemout AS(
SELECT 
     SubscriberID
    ,BeneficiaryID
    ,OriginalStartDate
    ,OriginalEndDate
    ,CMSContractNumber
    ,FileId
    ,GroupNumber
    ,StartDate
    ,EndDate
    ,CASE WHEN OriginalStartDate = OriginalEndDate THEN 1 ELSE 0 END AS IsVoid
FROM ExplodedMemoutDates
WHERE
StartDate <= OriginalEndDate 
),
Voids AS (
  SELECT 
     BeneficiaryID
    ,StartDate
    ,EndDate
    ,SUM(CASE WHEN IsVoid = 1 THEN 1 ELSE 0 END) AS IsVoid
  FROM FinalMemout
  GROUP BY
     BeneficiaryID
    ,StartDate
    ,EndDate
),
FinalFinalMemout AS (
SELECT 
    fm.SubscriberID
    ,fm.BeneficiaryID
    ,fm.OriginalStartDate
    ,fm.OriginalEndDate
    ,fm.CMSContractNumber
    ,fm.FileId
    ,fm.GroupNumber
    ,fm.StartDate
    ,fm.EndDate
    ,v.IsVoid AS IsActuallyVoid
   ,DENSE_RANK() OVER(PARTITION BY fm.BeneficiaryID,fm.StartDate ORDER BY fm.FileId DESC) rnk
FROM FinalMemout fm
  LEFT JOIN Voids v
    ON fm.BeneficiaryID = v.BeneficiaryID
    AND fm.EndDate = v.EndDate
    AND fm.StartDate = v.StartDate
WHERE
COALESCE(v.IsVoid,1) = 0
)
SELECT DISTINCT 
   SubscriberID
  ,BeneficiaryID
  ,StartDate
  ,EndDate
  ,CMSContractNumber
  ,GroupNumber
  ,FileId
FROM FinalFinalMemout
WHERE 
OriginalStartDate <> OriginalEndDate
AND
EndDate <= OriginalEndDate
AND 
StartDate < EndDate
AND
rnk = 1
  """


# COMMAND ----------

# DBTITLE 1,Filter SpanOther -- split by month
filteredSpanOther = """
WITH ExplodedDates AS(
SELECT 
   SubscriberID
  ,BeneficiaryID
  ,StartDate AS OriginalStartDate
  ,EndDate AS OriginalEndDate
  ,SubGroup
  ,FileID
  ,explode(month_range(StartDate, EndDate)) AS StartDate
FROM SpanOther
),
ExplodedSpanOtherDates AS(
SELECT  
   SubscriberID
  ,BeneficiaryID
  ,OriginalStartDate
  ,OriginalEndDate
  ,SubGroup
  ,FileID
  ,StartDate
  ,CASE WHEN OriginalStartDate = OriginalEndDate THEN OriginalEndDate ELSE last_day(StartDate) END AS EndDate
FROM ExplodedDates
),
FinalSpanOther AS(
SELECT 
     SubscriberID
    ,BeneficiaryID
    ,OriginalStartDate
    ,OriginalEndDate
    ,SubGroup
    ,FileId
    ,StartDate
    ,EndDate
FROM ExplodedSpanOtherDates
WHERE
StartDate <= OriginalEndDate 
),
FinalFinalSpanOther AS (
SELECT 
     fm.SubscriberID
    ,fm.BeneficiaryID
    ,fm.OriginalStartDate
    ,fm.OriginalEndDate
    ,fm.SubGroup
    ,fm.FileId
    ,fm.StartDate
    ,fm.EndDate
    ,DENSE_RANK() OVER(PARTITION BY fm.BeneficiaryID,fm.StartDate ORDER BY fm.FileId DESC) rnk
FROM FinalSpanOther fm
)
SELECT DISTINCT 
   SubscriberID
  ,BeneficiaryID
  ,StartDate
  ,EndDate
  ,SubGroup
  ,FileId
FROM FinalFinalSpanOther
WHERE 
OriginalStartDate <> OriginalEndDate
AND
EndDate <= OriginalEndDate
AND 
StartDate < EndDate
AND
rnk = 1
"""

# COMMAND ----------

# DBTITLE 1,Call the Method and Write Data into Gold MemberGroup Table
from delta.tables import *
from pyspark.sql.functions import *

# check if source file path exists
if path_exists(mePath) and path_exists(soPath):
  #read source data
  dfMemEnrolRaw = spark.read.format("delta").load(mePath)
  dfSpanOtherRaw = spark.read.format("delta").load(soPath) 
  dfMemEnrolRaw.createOrReplaceTempView("MemOutRaw")
  dfSpanOtherRaw.createOrReplaceTempView("SpanOtherRaw")

  #filter data based on FileLayoutID and SpanType
  dfMemEnrol = spark.sql(memOutSql)
  dfSpanOther = spark.sql(spanOtherSql)
  dfMemEnrol.createOrReplaceTempView("MemOut")
  dfSpanOther.createOrReplaceTempView("SpanOther")

  #create views for join
  dfMemOutSplit = spark.sql(filteredMemberEnrollment)
  dfSpanOtherSplit = spark.sql(filteredSpanOther)
  dfMemOutSplit.createOrReplaceTempView("MemOutSplit")
  dfSpanOtherSplit.createOrReplaceTempView("SpanOtherSplit")  
  
  #get the source joined data without voided records
  dfMemberGroup = spark.sql(sqlStmt)
  # dfMemberGroup.createOrReplaceTempView("dfMemberGroup") #if needed for analysis
  
  if path_exists(goldPath):
    # wipe the delta data and then write the final df into gold table
    destDf = spark.read.format('delta').option("header", "true").load(goldPath) 
    destDf.createOrReplaceTempView("MemberGroup")
    spark.sql("""DELETE FROM MemberGroup""")
    returnStr += "Gold Member Group Table refresh!"

  #write data to destination gold table
  dfMemberGroup.write.format("delta").option("mergeSchema", "true").mode("append").save(goldPath)

# COMMAND ----------

returnStr += "]"
dbutils.notebook.exit(returnStr)
