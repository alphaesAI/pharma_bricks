# Databricks notebook source
dbutils.widgets.text("OutboundJSON","","")

OutboundJSON = dbutils.widgets.get("OutboundJSON")
DatalakeMountPoint = "/mnt/"
print(OutboundJSON)

# COMMAND ----------

# DBTITLE 1,WRITE CSV (pipe/comma/tab) .<anything>
import os

def CreateCSV(dfFile, destTempTarget, destFinalTarget, delimiter, hasHeader):
  dbfs = "/dbfs"
  
  if(delimiter =="|"):    
    (
      dfFile.coalesce(1) #Creates one part- file
           .write
           .format("com.databricks.spark.csv") 
           .mode("Overwrite")
           .option("header", hasHeader)
           .option("delimiter", delimiter)
           .option("emptyValue", None)
           .option("nullValue", None)
           .option("quote", "\u0000")
           .save(destTempTarget)
    )
  else:   
    (
      dfFile.coalesce(1) #Creates one part- file
           .write
           .format("com.databricks.spark.csv") 
           .mode("Overwrite")
           .option("header", hasHeader)
           .option("delimiter", delimiter)
#            .option("emptyValue", '""')
#            .option("nullValue", '""')
           .option("quote", "\u0000")
           .save(destTempTarget)
    )
    
  
  Files = os.listdir(dbfs + destTempTarget)
  PartFileName = next(entry for entry in  Files if entry.startswith('part-'))
  
  #Combine all part file paths together -- same as .coalesce(1) in above write
  TempJson = os.path.join(destTempTarget, PartFileName)
  #copyFile TempJSON to destFinalTarget
  dbutils.fs.cp(TempJson, destFinalTarget)
  #remove files in destTempTarget
  dbutils.fs.rm(destTempTarget, recurse=True)
  #remove temp target also
  dbutils.fs.rm(destTempTarget)

# COMMAND ----------

# DBTITLE 1,Create NDJSON from DataFrame
import os

def CreateNDJsonExtract(dfFile, destTempTarget, destFinalTarget):
  dbfs = "/dbfs"

  (
    dfFile.coalesce(1) #Creates one part- file
         .write
         .format('json')  
         .mode("Overwrite")
         .option("multiLine","true")
         .save(destTempTarget)
  )

  Files = os.listdir(dbfs + destTempTarget)
  PartFileName = next(entry for entry in  Files if entry.startswith('part-'))
  
  #Combine all part file paths together -- same as .coalesce(1) in above write
  TempJson = os.path.join(destTempTarget, PartFileName)
  #copyFile TempJSON to destFinalTarget
  dbutils.fs.cp(TempJson, destFinalTarget)
  #remove files in destTempTarget
  dbutils.fs.rm(destTempTarget, recurse=True)
  #remove temp target also
  dbutils.fs.rm(destTempTarget)

# COMMAND ----------

# DBTITLE 1,SQL Config DB connection
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
fileLetter = "" #used for the env tag in the file name
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  fileLetter = envLetter
  envUser = "DEV"+envUser
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  fileLetter = envLetter
  envUser = "QA"+envUser
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  fileLetter = "t"  #changed for actual client use
  envUser = "STG"+envUser
else:
  envLetter = "p"
  fileLetter = envLetter
  envUser = "PRD"+envUser

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"

# COMMAND ----------

# DBTITLE 1,Replace FileNameTags
from datetime import datetime

def UpdateFileName(FileNamingConvention,ExportFileNamingExtension,ClientCode, SubClientCode,LOB,envLetter):
  FileName = FileNamingConvention

  FileNamingConventionList = FileName.split('_') 

  currentDate = datetime.today().strftime('%Y%m%d%H%M')
  currentDateAsYYYY = datetime.today().strftime('%Y')
  currentDateAsYYYYMM = datetime.today().strftime('%Y%m')
  currentDateAsYYYYMMDD = datetime.today().strftime('%Y%m%d')
  currentDateASYYYYMMDDhhmmss = datetime.today().strftime('%Y%m%d%H%M%S')
  
  FileName = FileName.replace("<ClientCode>", ClientCode)\
                    .replace("<SubClientCode>", SubClientCode)\
                    .replace("<YYYY>", str(currentDateAsYYYY))\
                    .replace("<YYYYMM>", str(currentDateAsYYYYMM))\
                    .replace("<YYYYMMDD>", str(currentDateAsYYYYMMDD))\
                    .replace("<YYYYMMDDhhmm>", currentDate)\
                    .replace("<YYYYMMDDhhmmss>", str(currentDateASYYYYMMDDhhmmss))\
                    .replace("<Env>", fileLetter)

  FileName += ExportFileNamingExtension
              
  return FileName

# COMMAND ----------

# DBTITLE 1,Method: path_exists
def path_exists(pathToCheck):
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

def getSource(Source):
  MountPoint = ""

  if(Source == "DataLake"):
    MountPoint = "/mnt/"
  elif(Source == "ExportDataLake"):
    MountPoint = "/mnt/export"

  return MountPoint

# COMMAND ----------

def createSourceTableEntity(path, entity, format):
  checkPathExists = path_exists(path)

  if(checkPathExists):
    if(format == "parquet"):
      dfFile = spark.read.format("parquet").option("header", "true").load(path)
    if(format == "delta"):
      dfFile = spark.read.format("delta").option("header", "true").load(path)
    
    dfFile.createOrReplaceTempView(entity)
    print(entity + " temp view created")
  else:
    message = "Path does not exist for entity: " + entity
    print(message)
    raise Exception(message)

# COMMAND ----------

def copyFile(SourcePath, DestinationPath):
  dbutils.fs.cp(SourcePath, DestinationPath,False)

# COMMAND ----------

def GenerateExtract(SQLQuery, DestinationFileName, DestinationExtension, ClientCode, LOB, DataLakeMountPoint, DestinationDelimiter, \
                    DestinationType, DestinationArchiveTablePath, DestinationTablePath, jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, envLetter, DestinationFirstRowAsHeader):
  #execute sql statement and store in dataframe
  dfFile = spark.sql(SQLQuery)

  recordCount = 0
  fileSize = 0
 
  #update filename
  DestinationFileName = UpdateFileName(DestinationFileName, DestinationExtension, ClientCode,SubClientCode, LOB, envLetter)
  #Create initial file in the archive destination
  FinalArchiveDestination = DataLakeMountPoint + ClientCode + DestinationArchiveTablePath
  FullDestination = FinalArchiveDestination + "/" + DestinationFileName
  FullDestinationTemp = FinalArchiveDestination + "/temp/" + DestinationFileName
  FinalDestination = DataLakeMountPoint + ClientCode + DestinationTablePath + "/" + DestinationFileName

  if(dfFile.count() > 0):  
    if(DestinationType.lower() =="csv"):
      CreateCSV(dfFile, FullDestinationTemp, FullDestination, DestinationDelimiter, DestinationFirstRowAsHeader)
    if(DestinationType.lower() =="ndjson"):
      CreateNDJsonExtract(dfFile, FullDestinationTemp, FullDestination)
    
    recordCount = dfFile.count()
    fileSize = getFileSizeInBytes(FullDestination)
    
    # file tracking -- archived
    track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'FileArchived', FullDestination, fileSize, recordCount)
    
    #copy file to final output location. Leave it in the archive location
    copyFile(FullDestination, FinalDestination)

  # check fileSize before update file tracking table
  if(fileSize == 0):
    # file tracking -- NoFileExtractCreated
    track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'NoFileExtractCreated', FinalDestination, fileSize, recordCount)
  else:
    # file tracking -- completed
    track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'FileExtractCompleted', FinalDestination, fileSize, recordCount) 

# COMMAND ----------

def register_file(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileReferenceId):
  # Fetch the driver manager from your spark context, create connection object, execute sql statement
  driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
  con = driver_manager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
  
  if OutboundFileReferenceId is None:
    OutboundFileReferenceId=-1
  elif not OutboundFileReferenceId.isnumeric():
    OutboundFileReferenceId=-1
  else:
    OutboundFileReferenceId=int(OutboundFileReferenceId)

  stmnt = f""" EXEC out.InsertOutboundFileRegistration {OutboundFileReferenceId}, ? """
  exec_statement = con.prepareCall(stmnt)
  exec_statement.registerOutParameter(1, spark._sc._gateway.jvm.java.sql.Types.BIGINT)
  exec_statement.execute()
  OutboundFileId = exec_statement.getLong(1)
    # Close connection
  exec_statement.close() 
  con.close()
  return OutboundFileId

# COMMAND ----------

def track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, status, path, size, count):
  # Fetch the driver manager from your spark context, create connection object, execute sql statement
  driver_manager = spark._sc._gateway.jvm.java.sql.DriverManager
  con = driver_manager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
  stmnt = f""" EXEC out.InsertOutboundFileTracking {OutboundFileId}, '{status}', '{path}', '{size}', '{count}' """
  exec_statement = con.prepareCall(stmnt)
  exec_statement.execute()
  exec_statement.close()
  con.close()

# COMMAND ----------

def getFileSizeInBytes(filePath):
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  File = sc._jvm.org.apache.hadoop.fs.Path(filePath)
  Size =  fs.getLength(File)
  
  return Size

# COMMAND ----------

from pyspark.sql.functions import explode

#Root level information
jsonList = []
jsonList.append(OutboundJSON)
OutboundJsonExtracted = spark.read.json(sc.parallelize(jsonList)) 

# display(OutboundJsonExtracted.collect())
#ClientCode and OutboundFileReferenceId
for row in OutboundJsonExtracted.collect():
  ClientCode = row["ClientCode"]
  SubClientCode = row["SubClientCode"]
  OutboundFileReferenceId = row["OutboundFileReferenceId"]
  LOB = row["LOB"]

#Destination Information including extract query
OutboundJSON = OutboundJsonExtracted.select("ClientCode","SubClientCode","OutboundFileReferenceId", explode("OutboundFileExtract").alias("OutboundExtract")).select("OutboundExtract.*")

for subrow in OutboundJSON.collect():
  DestinationType = subrow["DestinationType"]
  DestinationArchiveTablePath = subrow["DestinationArchiveTablePath"]
  DestinationDelimiter = subrow["DestinationDelimiter"]
  DestinationExtension = subrow["DestinationExtension"]
  DestinationFileName = subrow["DestinationFileName"]
  DestinationFirstRowAsHeader = subrow["DestinationFirstRowAsHeader"]
  DestinationTablePath = subrow["DestinationTablePath"]
  IsInlineQuery = subrow["IsInlineQuery"]
  SQLScript = subrow["SQLScript"]
  SQLScriptPath = subrow["SQLScriptPath"]

#Create all source table views to run query against
SourceJSON = OutboundJSON.select(explode("SourceTables").alias("SourceTables")).select("SourceTables.*")

# jdbc url for connection to config db
jdbcDatabase = "Configuration_DB_"+ ClientCode.upper()
jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase

# register file and file tracking register status
OutboundFileId = register_file(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileReferenceId)
print("OutboundFileId is :", OutboundFileId)
track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'Registered', DestinationTablePath,0,0)

# file tracking in progress
track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'FileExtractInProcessing', DestinationTablePath,0,0)

try:
  for sourceTable in SourceJSON.collect():
    Entity = sourceTable["Entity"]
    SourceFormat = sourceTable["SourceFormat"]
    Source = sourceTable["Source"]
    SourcePath = sourceTable["SourcePath"]
    
    FullSourcePath = getSource(Source) + ClientCode + SourcePath
    #will throw an error if one of the tables does not exist
    createSourceTableEntity(FullSourcePath, Entity, SourceFormat)

  SQLQuery = ""

  if(IsInlineQuery.lower() == "yes"):
    SQLQuery = SQLScript
  else:
    FullSQLScriptPath = DatalakeMountPoint + SQLScriptPath
    #load entire file into a dataframe
    rdd = spark.sparkContext.wholeTextFiles(FullSQLScriptPath)
    SQLQuery = rdd.collect()[0][1]

  FinalSQLQuery = SQLQuery.replace("#clientCode", ClientCode.upper()).replace("#subClientCode", SubClientCode.upper())
  #generate the actual file. Currently can do NDJSON and CSV (any delimiter)
  GenerateExtract(FinalSQLQuery, DestinationFileName, DestinationExtension, ClientCode, LOB, DatalakeMountPoint, DestinationDelimiter, DestinationType, \
                  DestinationArchiveTablePath, DestinationTablePath, jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, envLetter, DestinationFirstRowAsHeader)
except Exception as e:
  # file tracking in progress
  track_file_status(jdbcUrl, jdbcUsername, jdbcPassword, OutboundFileId, 'FileExtractError', DestinationTablePath,0,0)
  print(str(e))
