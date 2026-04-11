# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigFile","","")
dbutils.widgets.text("ConfigMountPoint","","")
dbutils.widgets.text("ExportAuditTable","","")
dbutils.widgets.text("ExportAuditTableMountPoint","","")
dbutils.widgets.text("ExportAuditTrackingTable","","")
dbutils.widgets.text("ExportAuditTrackingTableMountPoint","","")
dbutils.widgets.text("Entity","","")

ConfigFile = dbutils.widgets.get("ConfigFile")
ConfigMountPoint = dbutils.widgets.get("ConfigMountPoint")
ExportAuditTable = dbutils.widgets.get("ExportAuditTable")
ExportAuditTableMountPoint = dbutils.widgets.get("ExportAuditTableMountPoint")
ExportAuditTrackingTable = dbutils.widgets.get("ExportAuditTrackingTable")
ExportAuditTrackingTableMountPoint = dbutils.widgets.get("ExportAuditTrackingTableMountPoint")
ClientContainer =  dbutils.widgets.get("ClientContainer")
Entity =  dbutils.widgets.get("Entity")

# COMMAND ----------

# DBTITLE 1,Get Mount Point by Name
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

# DBTITLE 1,Create NDJSON from DataFrame
def CreateFileExtract(dfFile, destTempTarget, destFinalTarget):
  numberOfTries = 1

  ## will force this to continue until the file is written
  while numberOfTries < 5:
    try:
      #Create File in path
      (
      dfFile.coalesce(1) #Creates one part- file with .json as the output -- this also moves all data to a single node so will only work on smaller files
           .write
           .format('json')
           .mode("Overwrite")
           .option("multiLine","true")
           .save(destTempTarget)
      )

      #Get the only file in the path with .json --- this folder location should remain small
      FilePath = [x.path for x in dbutils.fs.ls(destTempTarget) if ".json".lower() in x.name][0]
      #copy file to destination this actually renames the file
      dbutils.fs.cp(FilePath,destFinalTarget)
      #remove all other crap that was there
      dbutils.fs.rm(destTempTarget,recurse=True)
      FileWritten = True
      numberOfTries += 1
      print("Wrote file processed.....")
      break
    except:
      numberOfTries += 1
      print("Failed to write File try again")

# COMMAND ----------

from datetime import datetime

def UpdateFileName(FileNamingConvention,ExportFileNamingExtension,batchId,LOB):
  FileName = FileNamingConvention

  FileNamingConventionList = FileName.split('_')

  for val in FileNamingConventionList:
    if (val == "<LOB>"):
      FileName = FileName.replace("<LOB>", LOB)
    if (val == "<BatchId>"):
      FileName = FileName.replace("<BatchId>", str(batchId))
    if (val == "<DateTime>"):
      currentDate = datetime.today().strftime('%Y%m%d')
      FileName = FileName.replace("<DateTime>", currentDate)

  FileName += ExportFileNamingExtension
      
  return FileName

# COMMAND ----------

def InsertExportAuditTracking(Batch, FileId, ExportFileName, Date, currentEntity, FileRecordCount, ExportAuditTrackingId):

  InsertExportAuditTrackingBatch = f"""
    INSERT INTO ExportAuditTrackingTable
    VALUES (
         '{ExportAuditTrackingId}'
        ,'{currentEntity}'
        ,'{FileId}'
        ,'{Batch}'
        ,'{ExportFileName}'
        ,'{Date}'
        ,False
        ,'{FileRecordCount}'
        ,current_timestamp()
    )
  """

  #Execute query 
  spark.sql(InsertExportAuditTrackingBatch)

  return "Success"

# COMMAND ----------

def CreateSingleBatch(batchId, FileID, currentEntity, ExportAuditTrackingId):
    #Filter Audit table to a single batch
    CurrentBatch = f"""
        SELECT DISTINCT
             a.BatchId
            ,a.Entity
            ,a.SourceFileId AS FileId
        FROM ExportAuditTable a
        WHERE
        a.SourceFileId = {FileID}
        AND
        a.Entity = '{currentEntity}'
        AND
        a.BatchId = {batchId}
    """

    #Execute query
    dfCurrentBatchAudit = spark.sql(CurrentBatch).cache()
    dfCurrentBatchAudit.createOrReplaceTempView("SkinnyAudit")
    
    newBatch = """
      SELECT DISTINCT 
           a.BatchId
          ,a.Entity
          ,st.*
      FROM SkinnyAudit a
      INNER JOIN BatchTable bt
          ON a.BatchId = bt.BatchId
          AND a.FileId = bt.FileID
      INNER JOIN SourceTable st
          ON bt.HashOfRow = st.HashOfRow
          AND bt.FileId = st.FileId
    """
    
    dfBatchFile = spark.sql(newBatch).cache()
    #recreates the QueryResult table after each attempt
    dfBatchFile.createOrReplaceTempView("QueryResult" + str(batchId))
    
    ExportFileName = "" # to reset the file name after each loop
    #create extract Filename info
    ExportFileName = UpdateFileName(ExportFileNamingConvention,ExportFileNamingExtension,str(batchId),LOB)
    
    destTempTarget = ExportFileLocation + "/temp/" + ExportFileName
    destFinalPath = ExportFileLocation + "/" + ExportFileName

    NewExportQuery = ExportQuery.replace("QueryResult", "QueryResult" + str(batchId))
  
    #Execute query 
    dfCurrentBatchWrite = spark.sql(NewExportQuery).distinct().cache()

    #Get unique records
    ExtractedFileCount = dfCurrentBatchWrite.count()
    
    #create single json file
    CreateFileExtract(dfCurrentBatchWrite, destTempTarget, destFinalPath)
    
    #update export_audit_tracking table
    Today = datetime.today()
    InsertExportAuditTracking(batchId, FileID, ExportFileName, Today, currentEntity, ExtractedFileCount, ExportAuditTrackingId)
    
    #release the pointer in memory in an attempt to help java garbage collector
    ########################################################################################################################
    ############################DO NOT RECALL THE DATAFRAME FOR ANY PURPOSE AFTER THIS######################################
    ########################################################################################################################
    dfBatchFile.unpersist()
    dfCurrentBatchAudit.unpersist()
    dfCurrentBatchWrite.unpersist()

# COMMAND ----------

import threading
import queue

class BatchClass:
  def __init__(self, batchId, FileID, currentEntity, ExportAuditTrackingId):
    self.BatchNumber = batchId
    self.FileId = FileID
    self.Entity = currentEntity
    self.ExportAuditTrackingId = ExportAuditTrackingId

def RunWorker(BatchQueue):
    while not BatchQueue.empty():
        CurrentBatch = BatchQueue.get()
        batchId = CurrentBatch.BatchNumber
        FileID = CurrentBatch.FileId
        currentEntity = CurrentBatch.Entity
        ExportAuditTrackingId = CurrentBatch.ExportAuditTrackingId
        CreateSingleBatch(batchId, FileID, currentEntity, ExportAuditTrackingId)
        BatchQueue.task_done()

def RunMultipleExtracts(dfBatchesToIterate):
  BatchQueue = queue.Queue()
  ThreadCount = 20 #fine line
  
  #Create Array of Dataframes to export
  for batchRecord in dfBatchesToIterate.collect():
    batchId = batchRecord["BatchId"]
    FileID = batchRecord["FileId"]
    currentEntity = batchRecord["Entity"]
    ExportAuditTrackingId = batchRecord["ExportAuditTrackingId"]
    BatchQueue.put(BatchClass(batchId, FileID, currentEntity, ExportAuditTrackingId))
  
  #get the size of the queue
  print("Queue Size: " + str(BatchQueue.qsize()))

  for i in range(ThreadCount):
      t = threading.Thread(target=RunWorker, args=(BatchQueue,)) #DOES NOT WAIT
      t.daemon = True #forces it to run on a single worker node
      t.start()
  
  # Block until all tasks are done.
  BatchQueue.join()

# COMMAND ----------

def createBatchFiles(ExportAuditPath,ExportAuditTrackingPath,BatchFilePath,SourceFilePath, ExportFilePath,LOB, ExportFileNamingConvention,ExportFileNamingExtension, ExportQuery):
  dfExportAuditTable = spark.read.format("delta").option("header","true").load(ExportAuditPath)
  dfExportAuditTrackingTable = spark.read.format("delta").option("header","true").load(ExportAuditTrackingPath)
  dfBatchTable = spark.read.format("delta").option("header","true").load(BatchFilePath)
  dfSourceTable = spark.read.format("delta").option("header","true").load(SourceFilePath)
  dfNewSourceFile = dfSourceTable.withColumn("HashOfRow", sha2(concat_ws("|", *dfSourceTable.columns), 256)) 

  dfExportAuditTable.createOrReplaceTempView("ExportAuditTable")
  dfExportAuditTrackingTable.createOrReplaceTempView("ExportAuditTrackingTable")
  dfBatchTable.createOrReplaceTempView("BatchTable")
  dfNewSourceFile.createOrReplaceTempView("SourceTable")
  
  uniqueNewBatches = f"""
      WITH CurrentExportTracking AS( 
      SELECT 
         ExportAuditTrackingId
        ,JSONFileName 
        ,SentToTopic 
        ,ROW_NUMBER() OVER(PARTITION BY ExportAuditTrackingId ORDER BY LoadDateTime DESC) AS RowNumber
      FROM ExportAuditTrackingTable 
      )
      SELECT DISTINCT 
           a.BatchId
          ,a.Entity
          ,a.SourceFileId AS FileId
          ,a.ExportAuditTrackingId
      FROM ExportAuditTable a
        LEFT JOIN CurrentExportTracking cet
          ON a.ExportAuditTrackingId = cet.ExportAuditTrackingId
          AND cet.RowNumber = 1
      WHERE
      a.Entity = '{Entity}'
      AND
      COALESCE(cet.SentToTopic,False) = 0
      AND
      cet.JSONFileName IS NULL
  """
   
  #Execute query 
  dfBatchesToIterate = spark.sql(uniqueNewBatches).cache()
  
  # things above here are not threaded
  RunMultipleExtracts(dfBatchesToIterate)
  
  #release the pointer in memory in an attempt to help java garbage collector
  ########################################################################################################################
  ############################DO NOT RECALL THE DATAFRAME FOR ANY PURPOSE AFTER THIS######################################
  ########################################################################################################################
  dfBatchesToIterate.unpersist()

# COMMAND ----------

from pyspark.sql.functions import concat_ws, sha2, col

FullConfigPath = getMountPoint(ConfigFile.replace("#clientCode", ClientContainer),ConfigMountPoint)
configDF = spark.read.format("json").option("multiLine","true").load(FullConfigPath)

dataCollect = configDF.collect()

for subRow in dataCollect:
  SourceTable = subRow["SourceTable"]
  SourceTableMountPoint = subRow["SourceTableMountPoint"]
  LOB = subRow["LOB"]
  BatchTable = subRow["BatchTable"]
  BatchTableMountPoint = subRow["BatchTableMountPoint"]
  ExportFilePath = subRow["ExportFilePath"]
  ExportFileMountPoint = subRow["ExportFileMountPoint"]
  ExportFileNamingConvention = subRow["ExportFileNamingConvention"]
  ExportFileNamingExtension = subRow["ExportFileNamingExtension"]
  ExportQuery = subRow["ExportQuery"]
  FilterTables = subRow["FilterTables"]

  for entityRow in FilterTables:
    FilterEntity = entityRow["Entity"]
    FilterSourceFormat = entityRow["SourceFormat"]
    FilterSourcePath = entityRow["SourcePath"]
    FilterSourceTableMountPoint = entityRow["SourceTableMountPoint"]
    FilterSourceFileLocation = getMountPoint(FilterSourcePath.replace("#clientCode", ClientContainer),FilterSourceTableMountPoint) 
    #Create a tempview
    dfFile = spark.read.format(FilterSourceFormat).option("header", "true").load(FilterSourceFileLocation) 
    dfFile.createOrReplaceTempView(FilterEntity)
    print(FilterEntity + " temp view created")


ExportAuditFileLocation = getMountPoint(ExportAuditTable.replace("#clientCode", ClientContainer), ExportAuditTableMountPoint)
ExportAuditTrackingFileLocation = getMountPoint(ExportAuditTrackingTable.replace("#clientCode", ClientContainer), ExportAuditTrackingTableMountPoint)
BatchTableFileLocation = getMountPoint(BatchTable.replace("#clientCode", ClientContainer), BatchTableMountPoint)
SourceTableFileLocation = getMountPoint(SourceTable.replace("#clientCode", ClientContainer), SourceTableMountPoint)
ExportFileLocation = getMountPoint(ExportFilePath.replace("#clientCode", ClientContainer), ExportFileMountPoint)

createBatchFiles(
   ExportAuditFileLocation
  ,ExportAuditTrackingFileLocation
  ,BatchTableFileLocation
  ,SourceTableFileLocation
  ,ExportFileLocation
  ,LOB
  ,ExportFileNamingConvention
  ,ExportFileNamingExtension
  ,ExportQuery
)
