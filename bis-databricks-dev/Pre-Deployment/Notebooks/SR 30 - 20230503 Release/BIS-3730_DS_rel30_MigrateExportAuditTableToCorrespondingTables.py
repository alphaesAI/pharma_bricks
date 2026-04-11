# Databricks notebook source
### Must be run after databricks rebuild database job
### Reason -- tables will not exist if you do not. This does not actually move the path so it can be run multiple times. 
### The path will need to be deleted "manually after execution". This ensures the data gets migrated and nothing is changed from the source. This also does inserts only. There are no deletes or updates.

FullConfigPath = "/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json"

# COMMAND ----------

def getEnvLetter():
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
  envLetter = ""  

  if(dbEnv == "934226345849410"):
    envLetter = "d" 
  elif(dbEnv == "5826678703751685"):
    envLetter = "q" 
  elif(dbEnv == "7093677384385470"):
    envLetter = "s" 
  else:
    envLetter = "p" 
    
  return envLetter

# COMMAND ----------

envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

from pyspark.sql.functions import explode, col, sha2, concat_ws, coalesce, lit

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

#dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

from pyspark.sql.functions import substring

def MigrateData(AuditTablePath,ExportAuditTablePath,ExportAuditTrackingTablePath):
  dfTempAuditTable = spark.read.format("delta").option("header","true").load(AuditTablePath)
  dfExportAuditTable = spark.read.format("delta").option("header","true").load(ExportAuditTablePath)
  dfExportAuditTrackingTable = spark.read.format("delta").option("header","true").load(ExportAuditTrackingTablePath)

  dfAuditTable = dfTempAuditTable.withColumn("ExportAuditTrackingId", sha2(concat_ws("|", coalesce("Entity",lit("")), coalesce("SourceFileId",lit("")), coalesce("BatchId",lit(""))), 256))
  
  dfAuditTable.createOrReplaceTempView("AuditTable")
  dfExportAuditTable.createOrReplaceTempView("ExportAuditTable")
  dfExportAuditTrackingTable.createOrReplaceTempView("ExportAuditTrackingTable")
  
  #insert into Exportaudit
  ExportAuditMergesql = """
      MERGE INTO ExportAuditTable d
      USING (SELECT * FROM AuditTable) s
          ON s.SourceFileId = d.SourceFileId
          AND s.BatchId = d.BatchId
          AND s.Entity = d.Entity
      WHEN NOT MATCHED THEN  
      INSERT(
           ExportAuditTrackingId --Need to add this hash of the Entity / SourceFileId and BatchId
          ,Entity
          ,Layer 
          ,LOB
          ,ClientCode
          ,SubClientCode
          ,SourceFileId
          ,SourceFileName
          ,BatchId
          ,TotalNumberOfBatches 
          ,LoadDateTime --not actually loaddatetime but best we got
      ) 
      VALUES (
           s.ExportAuditTrackingId
          ,s.Entity
          ,s.Layer
          ,s.LOB
          ,s.ClientCode
          ,s.SubClientCode
          ,s.SourceFileId
          ,s.SourceFileName
          ,s.BatchID
          ,s.TotalNumberOfBatches
          ,s.ExtractionDate
      )
  """
  
  spark.sql(ExportAuditMergesql)
  
  InsertExportAuditTrackingBatch = f"""
      MERGE INTO ExportAuditTrackingTable d
      USING (SELECT * FROM AuditTable) s
          ON s.SourceFileId = d.SourceFileId
          AND s.BatchId = d.BatchId
          AND s.Entity = d.Entity
      WHEN NOT MATCHED THEN  
      INSERT(
           ExportAuditTrackingId --Need to add this hash of the Entity / SourceFileId and BatchId
          ,Entity
          ,SourceFileId
          ,BatchId
          ,JSONFileName
          ,ExtractionDate
          ,SentToTopic
          ,NDJSONCount          
          ,LoadDateTime
      ) 
      VALUES (
           s.ExportAuditTrackingId
          ,s.Entity
          ,s.SourceFileId
          ,s.BatchId
          ,s.JSONFileName
          ,s.ExtractionDate
          ,s.SentToTopic
          ,s.NDJSONCount
          ,s.ExtractionDate --also not loaddatetime but best we can do
      )
  """

  #Execute query 
  spark.sql(InsertExportAuditTrackingBatch)

  return "Success"

# COMMAND ----------

clients = dfClientsForEnvironment.collect()

for c in clients: 
  print(c["Clients"])
  try:
    clientCode = c["Clients"]

    AuditTablePath = fr"dbfs:/mnt/export{clientCode}/BatchAudit/Audit"
    ExportAuditTablePath = fr"dbfs:/mnt/export{clientCode}/BatchAudit/export_audit"
    ExportAuditTrackingTablePath = fr"dbfs:/mnt/export{clientCode}/BatchAudit/export_audit_tracking"
    
    if(path_exists(AuditTablePath)):
      MigrateData(AuditTablePath,ExportAuditTablePath,ExportAuditTrackingTablePath)
  except Exception as e:
    print(str(e))
