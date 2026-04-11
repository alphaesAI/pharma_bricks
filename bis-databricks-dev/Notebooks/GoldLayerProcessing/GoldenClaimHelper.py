# Databricks notebook source
# DBTITLE 1,Setup ConfigDB Connection
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
jdbcDatabase = "Configuration_DB_" + clientCode.upper()

jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Connect to ConfigDB to check if new file within 1 day (24 hrs) then insert GC
#query to get new medical claim file count loaded within 24 hrs, if exists run GC process, otherwise stop here
sqlclmQuery = """
SELECT 
	COUNT(1) as claimFileCnt
FROM LatestFileWorkflowState lfw
	INNER JOIN reffilelayout fl 
		ON lfw.filelayoutid = fl.filelayoutid
where 
lfw.DataGroupDescription IN ('MedicalClaimHeader', 'MedicalClaimLine')
AND 
lfw.WorkflowStateDescription IN('ConsolidationCompleted')
AND 
DATEDIFF(HOUR, lfw.ProcessedDateTime, GETDATE()) < 24
AND 
fl.FilterEntity = 'GoldenClaims'
"""

sqlclmQueryPushdown = "(" + sqlclmQuery + ") a" 
clmDF = spark.read.jdbc(url=jdbcUrl, table=sqlclmQueryPushdown, properties=jdbcProperties)
clmDF.createOrReplaceTempView("NumberClaims")

#query to get clm error fileIDs
sqlStatment = """
SELECT DISTINCT fr.FileId
FROM FileRegistration fr
    INNER JOIN LatestFileWorkflowState lws
        ON fr.FileID = lws.FileID
    INNER JOIN refFileReference rfr
        ON fr.FileReferenceId = rfr.FileReferenceId
    INNER JOIN refFileLayout fl
        ON rfr.FileLayoutId = fl.FileLayoutId
    INNER JOIN refDataGroupMapping dgm
        ON fl.FileLayoutID = dgm.FileLayoutId
    INNER JOIN refDataGroup dg
        ON dgm.DataGroupID = dg.DataGroupID
WHERE
dg.DataGroupDescription IN ('MedicalClaimHeader', 'MedicalClaimLine')
AND
fl.filterentity='GoldenClaims'
AND
lws.WorkflowStateDescription IN('ConsolidationError')
"""

sqlStatmentQueryPushdown = "(" + sqlStatment + ") a" 
errorFIDs = spark.read.jdbc(url=jdbcUrl, table=sqlStatmentQueryPushdown, properties=jdbcProperties)
errorFIDs.createOrReplaceTempView("ErrorFileIds")

#query to get fileLayoutId which needs to apply GC logic
gcFileLayoutIDStmt = """
SELECT DISTINCT 
	 fl.FileLayoutId
	,CASE WHEN fl.FileLayoutDescription LIKE '%FCF%' THEN 'FCF' END AS DataSourceName
FROM refFileLayout fl       		 
	INNER JOIN refFileReference rfr               
		ON rfr.FileLayoutId = fl.FileLayoutId        
WHERE 
fl.filterentity='GoldenClaims'
"""

gcFileLayoutIDStmtQueryPushdown = "(" + gcFileLayoutIDStmt + ") a" 
gcFileLayoutIDs = spark.read.jdbc(url=jdbcUrl, table=gcFileLayoutIDStmtQueryPushdown, properties=jdbcProperties)
gcFileLayoutIDs.createOrReplaceTempView("GoldenClaimFileLayouts")

# COMMAND ----------

def DeleteGC():
  #delete all data from the golden claim table -- this will ultimately avoid duplicates
  deleteGCSqlQuery = "DELETE FROM GoldenClaim"
  sqlContext.sql(deleteGCSqlQuery)

# COMMAND ----------

# DBTITLE 1,Insert data into Golden Claims
def InsertGC():
  #Insert new records from the local table into the external table
  #This is ordinal based -- so ensure you have every column
  insertGCSQLQuery = f"""
  INSERT INTO GoldenClaim
    SELECT 
         GeneratedGoldenClaimsUniqueKey
        ,GeneratedMedicalClaimsUniqueKey
        ,ClientID
        ,FileLayoutID
        ,FileLayoutDescription
        ,SourceName
        ,ClaimNumber
        ,OriginalClaimNumber
        ,BeneficiaryID
        ,PlanMemberID
        ,UniquePersonKey
        ,CMSContractNumber
        ,BillTypeCode
        ,ClaimTypeInd
        ,ClaimStatus
        ,ClaimProcessDate
        ,IsRiskAdjustable
        ,IsRiskAdjustableSource
        ,IsTeleHealth
        ,LoadTimestamp
    FROM FinalGoldenClaim
    WHERE 
    GeneratedGoldenClaimsUniqueKey IS NOT NULL
    AND 
    GeneratedMedicalClaimsUniqueKey IS NOT NULL
    AND
    ClientID IS NOT NULL
    AND
    FileLayoutID IS NOT NULL
    AND
    FileLayoutDescription IS NOT NULL
    AND
    ClaimNumber IS NOT NULL
  """
  sqlContext.sql(insertGCSQLQuery)

# COMMAND ----------

# DBTITLE 1,Insert data into Golden Claims History
def InsertGCHistory(): 
  insertGCHistorySQLQuery = f"""
    INSERT INTO GoldenClaimHistory
    SELECT 
        GeneratedGoldenClaimsUniqueKey
        ,GeneratedMedicalClaimsUniqueKey
        ,ClientID
        ,FileLayoutID
        ,FileLayoutDescription
        ,SourceName
        ,ClaimNumber
        ,OriginalClaimNumber
        ,BeneficiaryID
        ,PlanMemberID
        ,UniquePersonKey
        ,CMSContractNumber
        ,BillTypeCode
        ,ClaimTypeInd
        ,ClaimStatus
        ,ClaimProcessDate
        ,IsRiskAdjustable
        ,IsRiskAdjustableSource
        ,IsTeleHealth
        ,LoadTimestamp
    FROM GoldenClaim
  """

  sqlContext.sql(insertGCHistorySQLQuery)

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Create TempView if exists
failedTablesList = []

def LoadAndCreateTempView(path, format, tablename, clientCode, mntPnt):
  UpdatedPath = mntPnt + path.replace("#clientCode",clientCode)

  if(pathExists(UpdatedPath)):
    dfFile = spark.read.format(format).option("header","true").load(UpdatedPath)
    dfFile.createOrReplaceTempView(tablename)
    print("TempViewCreated: " + tablename)
  else:
    failedTablesList.append(tablename)
    
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

dfSourceTables.createOrReplaceTempView("SourceTables")

# COMMAND ----------

# DBTITLE 1,Method: PATERNINDEX
import re

def paternindex(string,s):
    if s:
        match = re.search(string, s)
        if match:
            return match.start()+1
        else:
            return 0
    else:
        return 0

spark.udf.register("PATERNINDEX", paternindex)
