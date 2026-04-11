# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("GroupConfigPath","","") #empty config to work with the dataprocessing framework

clientCode = dbutils.widgets.get("ClientContainer")
clientContainer = clientCode.lower()

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, StringType, IntegerType

schema = StructType([ \
    StructField("name",StringType(),True), \
    StructField("catalog",StringType(),True), \
    StructField("namespace",StringType(),True), \
    StructField("description", StringType(), True), \
    StructField("tableType", StringType(), True), \
    StructField("isTemporary", StringType(), True) \
  ])

emptyRDD = spark.sparkContext.emptyRDD()
dfDataBase = spark.createDataFrame(emptyRDD,schema)

# COMMAND ----------

print(clientContainer)
databaseTables = spark.catalog.listTables(clientContainer) 
dfDatabaseTables = spark.createDataFrame(databaseTables, schema)
newDFDatabaseTables = dfDatabaseTables.filter(dfDatabaseTables.tableType == "EXTERNAL")
newDFDatabaseTables.createOrReplaceTempView(clientContainer)

# COMMAND ----------

sqlQuery = """SELECT 
   name
  ,catalog
  ,replace(replace(namespace,'[',''),']','') AS database
  ,description
  ,tableType
  ,isTemporary    
FROM """ + clientContainer + """ WHERE 
CASE 
  WHEN name LIKE 'gold_%' THEN 1 
  WHEN name LIKE 'platinum_%' THEN 1 
  ELSE 0 
END = 1"""

print(sqlQuery)
dfDataBase = spark.sql(sqlQuery)
dfDataBase.createOrReplaceTempView("DatabaseContents")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM DatabaseContents

# COMMAND ----------

# DBTITLE 1,Run SQL ConnectionNotebook
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
jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Setup Polybase connections
sparkPath = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"
spark.conf.set(sparkPath, blobKey)
tempDir = "wasbs://"+clientContainer+"@svtss"+envLetter+"idap01s.blob.core.windows.net/stream-temp"

# COMMAND ----------

# DBTITLE 1,Get existing Synapse Tables
synapseQuery = f"""
  SELECT 
      TableName = LOWER(TABLE_SCHEMA + '.' + TABLE_NAME)
  FROM INFORMATION_SCHEMA.TABLES
  WHERE
  TABLE_SCHEMA = '{clientContainer}'
"""

print(synapseQuery)
SynapseTablesQuery = "(" + synapseQuery + ") a"
dfSynapseTables = spark.read.jdbc(url=jdbcUrl, table=SynapseTablesQuery, properties=jdbcProperties)
dfSynapseTables.createOrReplaceTempView("SynapseDatabaseContents")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM SynapseDatabaseContents

# COMMAND ----------

tablesToSyncQuery = f"""
  SELECT 
     database
    ,name 
  FROM DatabaseContents
  WHERE 
  concat_ws('.', database, name) IN(SELECT TableName FROM SynapseDatabaseContents)
"""

print(tablesToSyncQuery)
dfTablesToSync = spark.sql(tablesToSyncQuery)
dfTablesToSync.createOrReplaceTempView("TablesToSync")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM TablesToSync

# COMMAND ----------

# DBTITLE 1,getSelectExpr
def getSelectExpr(availableCols, requiredCols):
	SQLCommand = ""
	iterator = 0
	#Loop through required columns
	for column in requiredCols:
		if(iterator != 0):
			SQLCommand = SQLCommand + "!" #split command for SQL select expr
			
		matchingColumn = ""
		#For each column in required columns loop through to find a match in columns available
		for columnsToMatch in availableCols:
			if column.lower() == columnsToMatch.lower():
				matchingColumn = columnsToMatch
				break
			
		if matchingColumn == "":
			SQLCommand = SQLCommand + "CAST(null AS STRING) " + " AS " + column
		else:
			SQLCommand = SQLCommand + columnsToMatch + " AS " + column
		iterator = iterator + 1
			
	#print(SQLCommand)
	return SQLCommand.split("!") 

# COMMAND ----------

def startTruncateAndLoad(destTable):
  trunSQL = """TRUNCATE TABLE """ + destTable
  
  #Read the table as a stream source 
  df = spark.read.table(destTable)
  
  pushdown_query = "(SELECT TOP 1 * FROM " + destTable + ") a" 
  #gets the table in ordinal position from source - just the first row
  synapse = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  
  (df.selectExpr(  
         getSelectExpr(                            
               df.columns, #Available columns
               synapse.columns #Required Columns 
             )
        )
      .write
      .format("com.databricks.spark.sqldw")
      .option("url", jdbcUrl)
      .option("user",jdbcUsername)
      .option("password",jdbcPassword) 
      .option("tempDir", tempDir)
      .option("forwardSparkAzureStorageCredentials", "true")
      .option("dbTable", destTable)
      .option("preActions", trunSQL)
      .option("maxStrLength",4000) #allows you to pass through strings of a max nvarchar(4000), buffers will be slower in polybase with this size
      .mode("append")
      .save()
  )
  
  return "SUCCESS"

# COMMAND ----------

#Configure the write semantics for Azure Synapse connector in the notebook session conf.
spark.conf.set("spark.databricks.sqldw.writeSemantics", "polybase")

# COMMAND ----------

# DBTITLE 1,loop through tables to dump into synapse
from pyspark.sql.functions import explode, col

tableCollect = dfTablesToSync.collect() #dfDataBase.collect()

returnStr = ""

for table in tableCollect:
  try:
    databaseName = table["database"]
    tableName = table["name"]
    #print(tempDir)
    fullTableName = databaseName + "." + tableName
    print(fullTableName + " is being truncated and loaded in synapse")
    startTruncateAndLoad(fullTableName)
    returnStr += fullTableName + " success!"
  except Exception as e:
    stringValue = fullTableName + " Failed to load because: " + str(e)
    returnStr += stringValue

dbutils.notebook.exit(returnStr)
