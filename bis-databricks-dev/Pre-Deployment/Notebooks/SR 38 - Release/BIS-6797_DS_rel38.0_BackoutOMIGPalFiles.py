# Databricks notebook source
# MAGIC %md
# MAGIC ## This notebook will run pre deployment to back out data and update Databases
# MAGIC - Update file status as ProcessingCompleted for the FileLayoutId = 11030
# MAGIC - Back out data in consolidated zone as requried
# MAGIC - Should run this notebook before DB creation Job. 

# COMMAND ----------

# DBTITLE 1,Setup Variables
FullConfigPath = "/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json"
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envUser = ""
envUser="_ETLUSER_SQL"

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
else:
  envLetter = "p"
  envUser = "PRD"+envUser

# COMMAND ----------

# DBTITLE 1,Gather Clients
from pyspark.sql.functions import explode, col

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Setup SQL Connection Parameters
jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"

jdbcPort = "1433"

jdbcProperties = {
                "user" : jdbcUsername,
                "password" : jdbcPassword,
                "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
              }

# COMMAND ----------

# DBTITLE 1,Setup SQL Database connection urls
def ConfigurationDBConnection(clientContainer):
  jdbcDatabase = "Configuration_DB_" + clientContainer.upper()
  jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase
  return jdbcUrl

# COMMAND ----------

def getFileList(jdbcUrl):
  getFileList = f"""
      SELECT 
        CAST(FileID AS VARCHAR(20)) AS FileID
      FROM LatestFileWorkflowState
      WHERE 
      FileLayoutID = 11030
      AND
	    WorkflowStateDescription = 'ConsolidationCompleted'
  """
  pushdown_query = "(" + getFileList + ") a"
  
  fileDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  fileList = fileDF.rdd.flatMap(lambda x: x).collect()
  return fileList

# COMMAND ----------

# DBTITLE 1,Method -- Back out data
def backOutConsolidatedData(clientContainer, fileList):
  sqlBackoutQuery = f"""
    DELETE FROM {clientContainer.lower()}.consolidated_ma_pharmacy
    WHERE
    FileId IN({fileList})
  """
  
  spark.sql(sqlBackoutQuery)

# COMMAND ----------

# DBTITLE 1,Connect to ConfigDB and update the file statuses in FileTracking table
def DeleteFromFileTracking(fileList, jdbcUrl):
  driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
  con = driver_manager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
  
  deletSQLFileTracking = f"""
	  DELETE
    FROM FileTracking
    WHERE
    FileId IN({fileList})
    AND
    WorkflowStateID IN(33,34)
  """

  exec_statement = con.prepareCall(deletSQLFileTracking)
  exec_statement.execute()
  exec_statement.close()
  con.close()

# COMMAND ----------

def DeleteFromDataGroupTracking(fileList, jdbcUrl):
  driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
  con = driver_manager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)

  deletSQLDataGroupTracking = f"""
    DELETE
    FROM DataGroupTracking
    WHERE
    FileId IN({fileList})
  """
  
  exec_statement = con.prepareCall(deletSQLDataGroupTracking)
  exec_statement.execute()
  exec_statement.close() 
  con.close()

# COMMAND ----------

# DBTITLE 1,Final one
EntityDelCollect = dfClientsForEnvironment.collect()

for ent in EntityDelCollect:
  clientCode = ent["Clients"]
  if(clientCode != "global"):
    print(f"INFO: Begin deleting for Client: {clientCode}")

    try:
      url = ConfigurationDBConnection(clientCode)
      fileList = getFileList(url)

      if(len(fileList) > 0):
        delimiter = "," #string delimiter
        #combine into a list
        fileListModified = delimiter.join(fileList)
        print("\tRemoving these fileids from consolidation:" +  fileListModified)
        backOutConsolidatedData(clientCode, fileListModified) #removing files from consolidation
        #reseting status to processing complete
        print("\tRemoving these fileids from FileTracking:" +  fileListModified)
        DeleteFromFileTracking(fileListModified, url)
        print("\tRemoving these fileids from DataGroupTracking:" +  fileListModified)
        DeleteFromDataGroupTracking(fileListModified, url)

    except Exception as e:
      print(str(e))
