# Databricks notebook source
# MAGIC %md
# MAGIC This notebook will run pre deployment to back out data and update Databases
# MAGIC 1. Update file status as ProcessingError for the FileLayoutId = 51000
# MAGIC 2. Back out data in consolidated zone as requried
# MAGIC 3. Removes the files from processed and consolidation folders
# MAGIC 4. Should run this notebook before DB creation Job.

# COMMAND ----------

# DBTITLE 1,Method: getEnvLetter
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

# DBTITLE 1,Get all Clients
from pyspark.sql.functions import explode, col

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))


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

# DBTITLE 1,Setup SQL Database connection URLs
def ConfigurationDBConnection(clientContainer):
  jdbcDatabase = "Configuration_DB_" + clientContainer.upper()
  jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase
  return jdbcUrl

# COMMAND ----------

# DBTITLE 1,Get FileIDs
def getFileList(jdbcUrl):
  getFileList = f"""
      SELECT 
        CAST(FileID AS VARCHAR(20)) AS FileID
      FROM LatestFileWorkflowState
      WHERE 
      FileLayoutID = 51000
      AND
	    WorkflowStateDescription = 'ConsolidationCompleted'
  """
  pushdown_query = "(" + getFileList + ") a"
  
  fileDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  fileList = fileDF.rdd.flatMap(lambda x: x).collect()
  return fileList

# COMMAND ----------

# DBTITLE 1,backout consolidated data
def backOutConsolidatedData(clientContainer, fileList):
  sqlBackoutQuery = f"""
    DELETE FROM {clientContainer.lower()}.consolidated_ma_rollupparameters
    WHERE
    FileId IN({fileList})
  """
  
  spark.sql(sqlBackoutQuery)

# COMMAND ----------

# DBTITLE 1,remove entries from filetracking with consolidation status
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

# DBTITLE 1,set final status for files - processing error
def UpdateFileTracking(fileList, jdbcUrl):
  driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
  con = driver_manager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
  
  updateSQLFileTracking = f"""
	  UPDATE FileTracking
    SET WorkflowStateID = 19,RecordsProcessed=0
    WHERE
    FileId IN({fileList})
    AND
    WorkflowStateID = 18
  """

  exec_statement = con.prepareCall(updateSQLFileTracking)
  exec_statement.execute()
  exec_statement.close()
  con.close()

# COMMAND ----------

# DBTITLE 1,remove files from datagrouptracking
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

# DBTITLE 1,Method: Check File Path
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Method: Delete Files in current Folder
def deleteFiles(folderPath):
  files = dbutils.fs.ls(folderPath)
  
  for f in files:
    if f.isDir():
      deleteFiles(f.path)
    else:
      dbutils.fs.rm(f.path, recurse=True)

  #Remove root level folder path
  dbutils.fs.rm(folderPath, recurse=True)

# COMMAND ----------

# DBTITLE 1,Final Step
EntityDelCollect = dfClientsForEnvironment.collect()

for ent in EntityDelCollect:
  clientCode = ent["Clients"]
  processedPath = f"/mnt/{clientCode}/processed/MA/Data/RollUpParameters/V1.0/ClientRollUpParameters"
  consolidatedPath = f"/mnt/{clientCode}/consolidated/MA/Data/RollUpParameters"
  if(clientCode != "global"):
    print(f"INFO: Begin deleting for Client: {clientCode}")

    try:
      url = ConfigurationDBConnection(clientCode)
      fileList = getFileList(url)

      if(len(fileList) > 0):
        delimiter = "," #string delimiter
        #combine into a list
        fileListModified = delimiter.join(fileList)
        #print("\tRemoving these fileids from consolidation:" +  fileListModified)
        #backOutConsolidatedData(clientCode, fileListModified) #removing files from consolidation
        #reseting status to processing complete
        print("\tRemoving these fileids from FileTracking:" +  fileListModified)
        DeleteFromFileTracking(fileListModified, url)
        print("\tUpdating fileids in FileTracking:" +  fileListModified)
        UpdateFileTracking(fileListModified, url)
        print("\tRemoving these fileids from DataGroupTracking:" +  fileListModified)
        DeleteFromDataGroupTracking(fileListModified, url)

        if(path_exists(processedPath)):deleteFiles(processedPath)
        print(f"INFO: Delete processed files and folder in {clientCode} for RollUpParameters ...")
        if(path_exists(consolidatedPath)):deleteFiles(consolidatedPath)
        print(f"INFO: Delete consolidated files and folder in {clientCode} for RollUpParameters ...")

    except Exception as e:
      print(str(e))
