# Databricks notebook source
# DBTITLE 1,Get Client Container
dbutils.widgets.text("ClientContainer","","")
container = dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,Execute Notebook SpanProcessingRules
# MAGIC %run "./SpanProcessingRules"

# COMMAND ----------

# DBTITLE 1,Execute Notebook getJDBCUrl
# MAGIC %run "../CommonMethods/Helpers/getJDBCUrl"

# COMMAND ----------

# DBTITLE 1,Create view to get FileLayoutID for GoldPCPAttribution
#call getJDBCUrl
jdbcUrlResults = getJDBCUrl('config', container)
jdbcUrl = jdbcUrlResults[0]
jdbcProperties= jdbcUrlResults[1]
jdbcUser = jdbcProperties['user']
jdbcPassword = jdbcProperties['password']
jdbcDriver = jdbcProperties['driver']

getGoldPCPAttFileLayoutsSql = """SELECT DISTINCT FileLayoutID FROM dbo.refFileLayout WHERE FilterEntity = 'GoldPCPAttribution'"""

getGoldPCPAttFileLayouts = (spark.read.format("jdbc") 
        .options(url=jdbcUrl,            
                query=getGoldPCPAttFileLayoutsSql,
                driver=jdbcDriver,
                user=jdbcUser,
                password=jdbcPassword).load())

getGoldPCPAttFileLayouts.createOrReplaceTempView("GoldPCPAttFileLayouts")

# COMMAND ----------

# DBTITLE 1,Source Tables
sourcePCP = f"/mnt/{container}/consolidated/MA/Data/PCPAttribution"
sourceMPB = f"/mnt/{container}/Gold/MA/Client/MemberPersonBridge" 
destPCP = f"/mnt/{container}/Gold/MA/Client/PCPAttribution"

# COMMAND ----------

# DBTITLE 1,Method: pathExists() - check file path
#will be used to check distributed file system paths. sc exposes the java api to python and scala
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Method: createDateRange() - creates monthly view
from pyspark.sql.functions import explode, sequence, to_date
def createDateRange(df, start, end):
    beginDate, endDate = dfSourcePCP.select(min(start),max(end)).first()

    dfDates = spark.sql(f"SELECT explode(sequence(to_date('{beginDate}'), to_date('{endDate}'), interval 1 month)) AS CalendarDate")
    
    return dfDates

# COMMAND ----------

# DBTITLE 1,SQL: MemberPersonBridge and PCPAttribution Joined
joinedSQL = """
WITH MemberPersonBridge(
SELECT DISTINCT 
   BISInternalPersonID
  ,PlanMemberId
FROM MPBRaw
WHERE 
IsCurrentPlanMemberId = 1
)
SELECT DISTINCT 
       m.BISInternalPersonID
      ,st.*
FROM PCPRaw st
  INNER JOIN GoldPCPAttFileLayouts fls 
    ON st.FileLayoutID = fls.FileLayoutID
  INNER JOIN MemberPersonBridge m 
    ON st.PlanMemberId = m.PlanMemberId
"""

# COMMAND ----------

# DBTITLE 1,SQL: Pull From Processed and Create a Record for Each Month Within Span
spanSql = """SELECT DISTINCT 
		 pcp.FileLayoutID AS FileLayoutID
        ,pcp.BisInternalPersonID AS BISInternalPersonID
        ,pcp.UniquePersonKey AS UniquePersonKey
        ,pcp.PlanMemberID  AS PlanMemberID 
        ,pcp.BeneficiaryID AS BeneficiaryID
        ,pcp.MedicaidID AS MedicaidID
        ,coalesce(mon.CalendarDate, pcp.StartDate) AS StartDate
        ,CASE WHEN pcp.EndDateEOY < coalesce(last_day(mon.CalendarDate)) 
              THEN pcp.EndDateEOY 
              ELSE coalesce(last_day(mon.CalendarDate), pcp.EndDateEOY) END AS EndDate
        ,pcp.AdditionalSpanValue AS AdditionalSpanValue
        ,pcp.ProviderID AS ProviderID
        ,pcp.AltPCPReporting1 AS AltPCPReporting1
        ,pcp.AltPCPReporting2 AS AltPCPReporting2
        ,pcp.AltPCPReporting3 AS AltPCPReporting3
        ,pcp.AltPCPReporting4 AS AltPCPReporting4
        ,pcp.AltPCPReporting5 AS AltPCPReporting5
        ,pcp.AltPCPReporting6 AS AltPCPReporting6
        ,pcp.AltPCPReporting7 AS AltPCPReporting7
        ,pcp.AltPCPReporting8 AS AltPCPReporting8
        ,pcp.AltPCPReporting9 AS AltPCPReporting9
        ,pcp.AltPCPReporting10 AS AltPCPReporting10
        ,pcp.SubscriberID AS SubscriberID
        ,pcp.ProviderAddressSuffix AS ProviderAddressSuffix
        ,pcp.ProviderEffDate AS ProviderEffDate
        ,pcp.ProviderFirstName AS ProviderFirstName
        ,pcp.ProviderLastName AS ProviderLastName
        ,pcp.ProviderMiddleInitial AS ProviderMiddleIntial
        ,pcp.MemberFirstName AS MemberFirstName
        ,pcp.MemberLastName AS MemberLastName
        ,pcp.MemberMiddleInitial AS MemberMiddleIntial
        ,pcp.MemberDOB AS MemberDOB
        ,pcp.CMSContractNumber AS ContractNumber
        ,pcp.ProviderNPI AS ProviderNPI
        ,pcp.ProviderTaxonomy AS ProviderTaxonomy
        ,pcp.ProviderTIN AS ProviderTIN
        ,pcp.ProviderAddress1 AS ProviderAddress1
        ,pcp.ProviderAddress2 AS ProviderAddress2
        ,pcp.ProviderCity AS ProviderCity
        ,pcp.ProviderState AS ProviderState
        ,pcp.ProviderZip AS ProviderZip
        ,pcp.ProviderCounty AS ProviderCounty
        ,pcp.ProviderPhone AS ProviderPhone
        ,pcp.ProviderFax AS ProviderFax
        ,pcp.ProviderEmail AS ProviderEmail
        ,pcp.BillingProviderID AS BillingProviderID
        ,pcp.BillingProviderLastName AS BillingProviderLastName
        ,pcp.BillingProviderMiddleInitial AS BillingProviderMiddleInitial
        ,pcp.BillingProviderFirstName AS BillingProviderFirstName
        ,pcp.BillingProviderNPI AS BillingProviderNPI
        ,pcp.BillingProviderTIN AS BillingProviderTIN
        ,pcp.BillingProviderAddressLine1 AS BillingProviderAddressLine1
        ,pcp.BillingProviderAddressLine2 AS BillingProviderAddressLine2
        ,pcp.BillingProviderCity AS BillingProviderCity
        ,pcp.BillingProviderState AS BillingProviderState
        ,pcp.BillingProviderZip AS BillingProviderZipCode
        ,pcp.BillingProviderCountyCode AS BillingProviderCountyCode
        ,pcp.BillingProviderPhoneNumber AS BillingProviderPhoneNumber
        ,pcp.BillingProviderFaxNumber AS BillingProviderFaxNumber
        ,pcp.BillingProviderEmail AS BillingProviderEmail
        ,pcp.Source AS Source
        ,CASE WHEN pcp.Inactive_Flag = 'inactive' OR coalesce(pcp.Void_Flag,pcp.Error_Flag) IS NOT NULL THEN 0 ELSE 1 END AS IsActive
        ,coalesce(pcp.Void_Flag,pcp.Error_Flag) AS ErrorVoidStatus
        ,pcp.FileGenerationDateTime AS FileGenerationDateTime
FROM SpanProcessed pcp 
    LEFT JOIN Months mon ON pcp.StartDate <= mon.CalendarDate 
        AND pcp.EndDateEOY >= mon.CalendarDate
  """

# COMMAND ----------

# DBTITLE 1,Process and Write Data into Gold PCP Attribution Table
from delta.tables import *
from pyspark.sql.functions import *

# check if source file path exists
if pathExists(sourcePCP) and pathExists(sourceMPB):
  #Create source dataframes
  #pcp
  dfSourcePCP = spark.read.format("delta").load(sourcePCP)\
                .withColumn("MemberID",coalesce("UniquePersonKey","BeneficiaryId", "PlanMemberId"))\
                .withColumn("EndDate",coalesce("EndDate",lit("9999-12-31")))\
                .withColumn("EndDateEOY", when(col("EndDate")=="9999-12-31",concat(year("StartDate").cast("string"),lit("-12-31"))).otherwise(coalesce("EndDate",concat(year("StartDate").cast("string"),lit("-12-31")))).cast("date"))\
                .withColumn("SourceGrouping",coalesce("Source",lit("PCP-Span")))
  dfSourcePCP.createOrReplaceTempView("PCPRaw")

  #memberpersonbridge
  dfSourceMPB = spark.read.format("delta").load(sourceMPB)
  dfSourceMPB.createOrReplaceTempView("MPBRaw")
  
  #join dfSourcePCP to MPB to get BISInternalPersonKey
  dfJoined = spark.sql(joinedSQL)
  dfJoined.createOrReplaceTempView("Joined")
  
  #Create view for dates which will be used to create spans
  dfMonths = createDateRange(dfSourcePCP,'StartDate','EndDateEOY')
  dfMonths.createOrReplaceTempView("Months")
  
  #Unique sources dataframe creation.  This puts new dataframes by source into a list which will be iterated over for processing.
  dfSources = dfJoined.groupBy("SourceGrouping").count().select("SourceGrouping") 
  sources = [list(x.asDict().values())[0] for x in dfSources.select("SourceGrouping").collect()]
  sourceList = [dfJoined.where(dfJoined.Source == x) for x in sources]
  
  #Check if destination path exists and if so delete the data.  This avoids potential dupes.
  destExists = pathExists(destPCP)
  if (destExists is True):
      print("Deleting data in table at: " + destPCP)
      dfGoldDF = DeltaTable.forPath(spark, destPCP)
      dfGoldDF.delete()
      print("Deleted data in table at: " + destPCP)
      
#   Loop through each source base dataframe
  for i in sourceList:
    #Call SpanProcessingRules() to apply span processing rules to the current source set
    dfSpanProcessing = SpanProcessingRules(i)

    #Create temp views to be used in queries
    dfSpanProcessing.createOrReplaceTempView("SpanProcessed")
    
    #Create monthly spans from processed dataframe
    dfSpans = spark.sql(spanSql)
    
    #Write to final gold layer
    print("Loading table at: " + destPCP)
    dfSpans.write.format("delta").mode("append").save(destPCP)
    print("Loaded "+str(dfSpans.count()) + " records at "+ destPCP)
