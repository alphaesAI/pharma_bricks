# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("WizardOrchestratorJSON","","")

WizardOrchestrator = dbutils.widgets.get("WizardOrchestratorJSON")
WizardOrchestratorpath = "/mnt/fileconfig/" + WizardOrchestrator
clientContainer =  dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,import
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType, LongType, TimestampType, BooleanType
from pyspark.sql.functions import explode
from pyspark.sql.functions import lit
from pyspark.sql.functions import sha2
from pyspark.sql.functions import concat_ws

# COMMAND ----------

# DBTITLE 1,function to validate path
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Flatten configuration
Entity_schema = StructType(fields=[
    StructField('ExportAuditTable', StringType(), False),
    StructField('ExportAuditTableMountPoint', StringType(), True),
    StructField('ExportAuditTrackingTable', StringType(), False),
    StructField('ExportAuditTrackingTableMountPoint', StringType(), True),
    StructField(
        'Entities', ArrayType(
            StructType([
                StructField('Entity', StringType(), True),
                StructField('ConfigFile', StringType(), True),
                StructField('ConfigMountPoint', StringType(), True), 
                StructField('LOB', StringType(), True),
                StructField('SourceLayer', StringType(), True),
                StructField('BatchSize', IntegerType(), True)
            ])
        )
    )
])

df = spark.read.format("json").option("multiline", "true").json(WizardOrchestratorpath, schema=Entity_schema)

entity_df = df.select("ExportAuditTable","ExportAuditTableMountPoint","ExportAuditTrackingTable","ExportAuditTrackingTableMountPoint",
    explode("Entities").alias("EntitiesExplode")
).select("ExportAuditTable","ExportAuditTableMountPoint","ExportAuditTrackingTable","ExportAuditTrackingTableMountPoint", "EntitiesExplode.*")

entity_df.createOrReplaceTempView("TempEntity")  

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM TempEntity

# COMMAND ----------


def ConnectToConfigDBAndGetFileIds(clientContainer):
  ################# CONNECT TO DATABASE ###################################
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
  jdbcDatabase = "Configuration_DB_" + clientContainer.upper() ###Replace with Configdb
  jdbcPort = "1433"

  jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

  jdbcProperties = {
                "user" : jdbcUsername,
                "password" : jdbcPassword,
                "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
              }

  ################# RUN SQL QUERY AGAINST CONFIGDB###################################
  ConfigSQLQuery = """
        SELECT DISTINCT --need this for files with multiple datagroups
             FileID
            ,SubClientDescription
            ,ClientDescription
            ,FileName
            ,WorkflowStateDescription
        FROM LatestFileWorkflowState
        WHERE
        WorkflowStateDescription = 'ConsolidationCompleted'
        AND
        FileReferenceID IS NOT NULL
  """
  
  pushdown_query = "(" + ConfigSQLQuery + ") a"
  
  ##Loads a dataframe with the results of the sqlQuery
  configResults = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  
  return configResults

# COMMAND ----------

# DBTITLE 1,Function to insert ExportAudit table
from pyspark.sql.functions import coalesce, lit

def InsertExportAudit(Entity, LOB, Layer, BatchingPath, ExportAuditPath,clientContainer):

  ExportAuditdf = spark.read.format("delta").option("header", "true").load(ExportAuditPath) 
  ExportAuditdf.createOrReplaceTempView("ExportAudit")
  
  #connect to configDB and get FileIds with SubClient and Client
  configResult = ConnectToConfigDBAndGetFileIds(clientContainer).cache()
  configResult.createOrReplaceTempView("ConfigQuery")
  
  sourceBatchingdf = spark.read.format("delta").option("header", "true").load(BatchingPath) 
  sourceBatchingdf.createOrReplaceTempView("Sourcebatch")
  
  sourceSql = f"""
  WITH Source AS(
    SELECT DISTINCT 
       FileId
      ,BatchId
      ,'{Entity}' AS Entity
      ,TotalNumberOfBatches
    FROM Sourcebatch
  ),
  ExportAudit AS(
    SELECT 
       SourceFileId AS FileId
      ,BatchId
      ,Entity
    FROM ExportAudit
  ),
  NewRecords AS(
    SELECT
       s.FileId
      ,s.BatchId
      ,s.TotalNumberOfBatches
    FROM Source s
      LEFT JOIN ExportAudit ea
        ON s.FileId = ea.FileId
        AND s.BatchId = ea.BatchId
        AND s.Entity = ea.Entity
    WHERE
    ea.BatchId IS NULL
  )
  SELECT 
     s.FileId
    ,s.BatchId
    ,s.TotalNumberOfBatches
    ,cq.FileName AS SourceFileName
    ,cq.SubClientDescription AS SubClientCode 
    ,cq.ClientDescription  AS ClientCode
    ,current_timestamp() AS LoadDateTime
  FROM NewRecords s
    LEFT JOIN ConfigQuery cq
      ON s.FileId = cq.FileId
ORDER BY 
BatchId
  """
  
  sdf = spark.sql(sourceSql)
  adf = sdf.withColumn("Entity", lit(Entity)).withColumn("Layer", lit(Layer)).withColumn("LOB", lit(LOB)).withColumn("ExportAuditTrackingId", sha2(concat_ws("|", coalesce("Entity",lit("")), coalesce("FileId",lit("")), coalesce("BatchId",lit(""))), 256))
  
  adf.createOrReplaceTempView("s_df")
  
  AuditInsertsql = """
      INSERT INTO ExportAudit
      SELECT 
           s.ExportAuditTrackingId
          ,s.Entity
          ,s.FileID
          ,s.SourceFileName
          ,s.BatchID
          ,s.Layer
          ,s.LOB
          ,s.ClientCode
          ,s.SubClientCode
          ,s.TotalNumberOfBatches
          ,s.LoadDateTime
      FROM s_df s
  """

  spark.sql(AuditInsertsql)
  
  return True

# COMMAND ----------

# DBTITLE 1,Function to create Entity Batching
def CreateEntityBatch (sourcePath, destinationPath, batchSize,clientContainer): 
  batchCount = batchSize 
  
  if  batchSize > 0:
    #load source and target into a dataframe
    dfDestinationPath = spark.read.format("delta").option("header","true").load(destinationPath)     
    dfSourcePath = spark.read.format("delta").option("header","true").load(sourcePath)  
    newDFFile = dfSourcePath.withColumn("HashOfRow", sha2(concat_ws("|", *dfSourcePath.columns), 256))  

    #need to create local tables before anything else
    dfDestinationPath.createOrReplaceTempView("Destination") 
    newDFFile.createOrReplaceTempView("Source")

    #connect to configDB and get FileIds with SubClient and Client that are consolidation complete
    configResult = ConnectToConfigDBAndGetFileIds(clientContainer)
    configResult.createOrReplaceTempView("ConfigQuery")

    # create/insert entity batching
    sqlBatchQuery = """ 
       WITH ConsolidatedFiles AS(
       SELECT
           FileID
       FROM ConfigQuery
       ),
       DestinationTable AS( 
        SELECT  
           HashOfRow
          ,BatchId
          ,FileID
          ,FileLayoutID
          ,RowNumber
        FROM Destination
        ), 
        MaxBID AS (
          SELECT  
              MAX(CAST (BatchId AS INT)) AS MaxBatchID
          FROM Destination
        ),
        UniqueSource AS(
        SELECT DISTINCT 
             FileId
            ,FileLayoutId
            ,HashOfRow
        FROM Source
        WHERE
        FileId IN(SELECT FileID FROM ConsolidatedFiles)
        ),
        SourceWithRowNumber AS( 
        SELECT
           FileId
          ,FileLayoutId
          ,HashOfRow
          ,ROW_NUMBER() OVER(PARTITION BY FileId ORDER BY FileId, HashOfRow) AS RowNumber 
        FROM UniqueSource
        ),
        Combined AS(
        SELECT 
              s.HashOfRow AS HashOfRow
             ,0 AS BatchId
             ,s.FileID AS FileID
             ,s.FileLayoutID AS FileLayoutID
             ,s.RowNumber AS RowNumber
        FROM SourceWithRowNumber S
          LEFT JOIN DestinationTable dt
            ON dt.FileId = s.FileId
            AND dt.HashOfRow = s.HashOfRow 
        WHERE
        dt.BatchId IS NULL
      ), 
      Batched AS(
      SELECT 
         FileId
        ,FileLayoutId
        ,HashOfRow
        ,RowNumber
        ,CEIL(RowNumber / {batch}) AS BatchOfFileId 
      FROM Combined
      ), 
      Batches AS(
      SELECT BatchOfFileId 
        ,FileId 
        ,(ROW_NUMBER() OVER(ORDER BY FileId, BatchOfFileId) + IfNull(MaxBatchID,0)) AS BatchId
      FROM Batched
        CROSS JOIN MaxBID
      GROUP BY BatchOfFileId 
        ,FileId
        ,IfNull(MaxBatchID,0)
      ),
      TotalBatches AS(
      SELECT 
         FileId
        ,COUNT(BatchId) AS TotalNumberOfBatches
      FROM Batches
      GROUP BY 
         FileId
      )
      SELECT DISTINCT
             b.HashOfRow
            ,bs.BatchId
            ,tb.TotalNumberOfBatches
            ,b.FileID
            ,b.FileLayoutID
            ,b.RowNumber
      FROM Batched b
        LEFT JOIN Batches bs
          ON b.BatchOfFileId = bs.BatchOfFileId
          AND b.FileId = bs.FileId
        LEFT JOIN TotalBatches tb
          ON b.FileId = tb.FileId
      ORDER BY
       BatchId
      ,RowNumber
     """

    dfFinal = spark.sql(sqlBatchQuery.format(batch = batchCount))
    dfFinal.createOrReplaceTempView("s")

    sqlInsert = """
        INSERT INTO Destination
        SELECT 
             HashOfRow
            ,BatchId
            ,FileID
            ,FileLayoutID
            ,RowNumber 
            ,TotalNumberOfBatches
        FROM s
        """

    spark.sql(sqlInsert)
  
  return True

# COMMAND ----------

# DBTITLE 1,Determine Mount Point
def getMountPoint(Path, MountName):
  mountPath = ""
  DataLakeMountPoint = "/mnt/"
  ExportMountPoint = "/mnt/export"
  FileConfigMountPoint = "/mnt/fileconfig/"

  if (MountName == "DataLake"):
    mountPath = DataLakeMountPoint + Path
  elif(MountName == "Export"):
    mountPath = ExportMountPoint + Path
  elif(MountName == "FileConfig"):
    mountPath = FileConfigMountPoint + Path
  
  return mountPath

# COMMAND ----------

#create MasterAudit schama
exportAuditSchema = StructType([
  StructField('ExportAuditTrackingId', StringType(), True),
  StructField('Entity', StringType(), True),
  StructField('Layer', StringType(), True),
  StructField('LOB', StringType(), True),
  StructField('ClientCode', StringType(), True),
  StructField('SubClientCode', StringType(), True),
  StructField('SourceFileId', StringType(), True),
  StructField('SourceFileName', StringType(), True),
  StructField('BatchId', IntegerType(), True),
  StructField('TotalNumberOfBatches', IntegerType(), True),
  StructField('LoadDateTime', TimestampType(), True)
  ])

#create MasterAudit schama
exportAuditTrackingSchema = StructType([
  StructField('ExportAuditTrackingId', StringType(), True),
  StructField('Entity', StringType(), True),
  StructField('SourceFileId', StringType(), True),
  StructField('BatchId', IntegerType(), True),
  StructField('JSONFileName', StringType(), True),
  StructField('ExtractionDate', TimestampType(), True),
  StructField('SentToTopic', BooleanType(), True),
  StructField('NDJSONCount', IntegerType(), True),
  StructField('LoadDateTime', TimestampType(), True)
  ])

def CreateExportAuditTables(ExportAuditPath,ExportAuditTableMountPoint,ExportAuditTrackingPath,ExportAuditTrackingTableMountPoint, clientContainer):
  emptyAuditRDD = spark.sparkContext.emptyRDD()
  
  ########ExportAudit
  ExportAuditTablePath = getMountPoint(row['ExportAuditTable'].replace("#clientCode", clientContainer),ExportAuditTableMountPoint)
  
  ExportAuditPathExists = path_exists(ExportAuditTablePath)
  ExportAuditDataModel = spark.createDataFrame(emptyAuditRDD, exportAuditSchema)
  
  #create masterAudit table if does not exist
  if ExportAuditPathExists:
    #should write 0 records
    ExportAuditDataModel.write \
		  .format("delta") \
		  .option("mergeSchema", "true")\
		  .mode("append") \
		  .save(ExportAuditTablePath)
  else:
    ExportAuditDataModel.write.format("delta").option("mergeSchema", "true").mode("append").save(ExportAuditTablePath)

  ########ExportAuditTracking
  ExportAuditTrackingTablePath = getMountPoint(row['ExportAuditTrackingTable'].replace("#clientCode", clientContainer),ExportAuditTableMountPoint)
  
  ExportAuditTrackingPathExists = path_exists(ExportAuditTrackingTablePath)
  ExportAuditTrackingDataModel = spark.createDataFrame(emptyAuditRDD, exportAuditTrackingSchema)
  
  #create masterAudit table if does not exist
  if ExportAuditTrackingPathExists:
    #should write 0 records
    ExportAuditTrackingDataModel.write \
		  .format("delta") \
		  .option("mergeSchema", "true")\
		  .mode("append") \
		  .save(ExportAuditTrackingTablePath)
  else:
    ExportAuditTrackingDataModel.write.format("delta").option("mergeSchema", "true").mode("append").save(ExportAuditTrackingTablePath)

# COMMAND ----------

# DBTITLE 1,Main Execution
#create Entity batching schema
batchingSchema = StructType([
  StructField('HashOfRow', StringType(), True),
  StructField('BatchId', LongType(), True),
  StructField('FileID', LongType(), True),
  StructField('FileLayoutID', IntegerType(), True),
  StructField('RowNumber', IntegerType(), True),
  StructField('TotalNumberOfBatches', IntegerType(), True)
  ])

returnStr = ""
entity_psdf = entity_df.select("*").collect()

Entity = ""
SourceTable = ""
SourceTableMountPoint = ""
BatchTable = ""
BatchTableMountPoint = ""
LOB = ""
Layer = ""
BatchSize = -1

try:
  exportAuditDF = entity_df.select("ExportAuditTable","ExportAuditTableMountPoint","ExportAuditTrackingTable","ExportAuditTrackingTableMountPoint").distinct().collect()

  #should only be one row
  for row in exportAuditDF:
    ExportAuditTable = row['ExportAuditTable']
    ExportAuditTableMountPoint = row['ExportAuditTableMountPoint'] 
    ExportAuditTrackingTable = row['ExportAuditTrackingTable']
    ExportAuditTrackingTableMountPoint = row['ExportAuditTrackingTableMountPoint']
    CreateExportAuditTables(ExportAuditTable,ExportAuditTableMountPoint,ExportAuditTrackingTable,ExportAuditTrackingTableMountPoint, clientContainer)
  
  ExportAuditTablePath = getMountPoint(ExportAuditTable.replace("#clientCode", clientContainer),ExportAuditTableMountPoint)
  
  #iterate through each entity records 
  for row in entity_psdf:
      Entity = row['Entity']
      ConfigFile = row['ConfigFile']
      ConfigMountPoint = row['ConfigMountPoint']
      
      FullConfigPath = getMountPoint(ConfigFile.replace("#clientCode", clientContainer),ConfigMountPoint) 

      configDF = spark.read.format("json").option("multiLine","true").load(FullConfigPath)
      newConfigDF = configDF.select("SourceTable","SourceTableMountPoint","BatchTable","BatchTableMountPoint")
      
      dataCollect = newConfigDF.collect()
      for subRow in dataCollect:
        SourceTable = subRow["SourceTable"]
        SourceTableMountPoint = subRow["SourceTableMountPoint"]
        BatchTable = subRow["BatchTable"]
        BatchTableMountPoint = subRow["BatchTableMountPoint"]

      SourceTablePath = getMountPoint(SourceTable.replace("#clientCode", clientContainer),SourceTableMountPoint)
      BatchTablePath = getMountPoint(BatchTable.replace("#clientCode", clientContainer),BatchTableMountPoint) 
            
      LOB = row["LOB"]
      Layer = row["SourceLayer"]
      BatchSize = row["BatchSize"]
      
      #create entity batching table if does not exist
      if path_exists(SourceTablePath): 
        if not path_exists(BatchTablePath):  
          emptyRDD = spark.sparkContext.emptyRDD()
          destinationDataModel = spark.createDataFrame(emptyRDD, batchingSchema)
          destinationDataModel.write.format("delta").option("mergeSchema", "true").mode("append").save(BatchTablePath)    
        
        CreateEntityBatch(SourceTablePath, BatchTablePath,BatchSize,clientContainer)

        InsertExportAudit(Entity, LOB, Layer, BatchTablePath, ExportAuditTablePath,clientContainer)
        
        returnStr += " Source table " + SourceTablePath + " completed \r\n"
      else:
        returnStr += " Source table " + SourceTablePath + " doesn't exist! "
      #run export portion via another notebook
      try:
        dbutils.notebook.run("SubOrchestrator", 0, {
                                      "ClientContainer": clientContainer
                                     ,"ConfigFile": ConfigFile
                                     ,"ConfigMountPoint": ConfigMountPoint
                                     ,"ExportAuditTable": ExportAuditTable
                                     ,"ExportAuditTableMountPoint":ExportAuditTableMountPoint
                                     ,"ExportAuditTrackingTable": ExportAuditTrackingTable
                                     ,"ExportAuditTrackingTableMountPoint":ExportAuditTrackingTableMountPoint
                                     ,"Entity": Entity
                                   })
        
        returnStr += "SUCCESS"
      except Exception as e:
        returnStr += "FAILURE: " + str(e)

  returnStr += ""

except Exception as e:
      returnStr += str(e)
finally:
      dbutils.notebook.exit(returnStr)
