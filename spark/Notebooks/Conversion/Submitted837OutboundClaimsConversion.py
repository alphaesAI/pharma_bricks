# Local Spark version of Submitted837OutboundClaimsConversion.py
# Non-Databricks dependent Python

import os
import json
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Submitted837OutboundClaimsConversion") \
    .getOrCreate()

# Load configuration from JSON file instead of dbutils.widgets
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "../../config/credentials.json")
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
        return {}

# Load configuration
config = load_config()

# Get parameters from config (replaces dbutils.widgets.get)
fileID = config.get("FileId", "")
FileLayoutDescription = config.get("FileLayoutDescription", "")
currentContainer = config.get("CurrentContainer", "")
currentFolderPath = config.get("CurrentFolderPath", "")
fileName = config.get("FileName", "")
delimiter = config.get("Delimiter", "|")
conversionType = config.get("ConversionType", "")
conversionJsonContainer = config.get("ConversionJsonContainer", "")
conversionJsonFolderPath = config.get("ConversionJsonFolderPath", "")
conversionJsonFileName = config.get("ConversionJsonFileName", "")

mountPoint = "/mnt/"
blobPath = mountPoint + currentContainer + "blob" 
toProcessPath = blobPath + currentFolderPath 
dataFilePath = toProcessPath + "/" + fileName
conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" +  conversionJsonFileName

convertedFilePath = blobPath + "/ConvertedFiles/" + conversionType #PremeraPharmacyOMIGPAL
fullConvertedFilePath = convertedFilePath + "/" + fileName + "/" + fileName

##need this to cleanup the name for the control file
pathList = os.path.splitext(fileName)
fileFolderName = pathList[0]


returnJSON  = ""

print(f"blobPath: {blobPath}")
print(f"toProcessPath: {toProcessPath}")
print(f"fileName: {fileName}")
print(f"dataFilePath: {dataFilePath}")
print(f"fullConvertedFilePath: {fullConvertedFilePath}")
print(f"conversionJsonPath: {conversionJsonPath}")

# COMMAND ----------

# Local PostgreSQL Config DB connection
envLetter = config.get("environment", "d")  # Default to dev
fileLetter = envLetter
envUser = config.get("sql", {}).get("username", "DEV_ETLUSER_SQL")

# PostgreSQL connection parameters
jdbcPort = config.get("sql", {}).get("port", "5432")
jdbcUsername = envUser
jdbcPassword = config.get("sql", {}).get("password", "")
jdbcHostname = config.get("sql", {}).get("hostname", "localhost")

# jdbc url for connection to config db (PostgreSQL)
jdbcDatabase = config.get("sql", {}).get("database", "configuration_db")
jdbcUrl = f"jdbc:postgresql://{jdbcHostname}:{jdbcPort}/{jdbcDatabase}"

# COMMAND ----------

# DBTITLE 1,Get ClientID based on current container name
stmnt = f"""SELECT ClientID FROM refClient WHERE ClientDescription = '{currentContainer}'"""
clientID = (spark.read.format("jdbc") 
        .options(url=jdbcUrl,
                driver='org.postgresql.Driver',            
                query=stmnt,
                user=jdbcUsername,
                password=jdbcPassword).load())
clientID = str(clientID.collect()[0][0])

# COMMAND ----------

# DBTITLE 1,Create Schema Dataframe
#create json dataframe and explode columns
from pyspark.sql.functions import col, explode

dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)

#get recordTypes and tempViewsNames
expRecordTypes = dfJSon.select(explode("RecordTypes").alias("RecordType")).select("RecordType.Type","RecordType.TempViewName")

#get columns by recordType
expColumnNames = dfJSon.select(explode("RecordTypes").alias("RecordType")).select("RecordType.Type",explode("RecordType.ColumnNames").alias("ColumnNames")).select("Type","ColumnNames.FieldName","ColumnNames.OrdinalPosition")

#get queries
expQueries = dfJSon.select(explode("Queries").alias("Queries")).select("Queries.FinalQuery")
finalSQLQuery = expQueries.select("FinalQuery").collect()[0][0]

# display(expQueries)

# COMMAND ----------

# DBTITLE 1,Loads entire file into an rdd and converts it to Rows (single row per record)
def AnyFileToDataFrame(FileLocation):
  dfFile = spark.read.format("csv").option("delimiter","\n").load(FileLocation).withColumnRenamed("_c0", "Row")
  dfFile.createOrReplaceTempView("CurrentFile")
  return dfFile

# COMMAND ----------

# Local file system version of CreateCSV
def CreateCSV(dfFile, destFinalTarget, delimiter, hasHeader):
  import tempfile
  import shutil
  
  pathList = os.path.splitext(destFinalTarget)
  destTempTarget = pathList[0] + '/'
  extension = pathList[1]

  # Create temporary directory
  temp_dir = tempfile.mkdtemp()
  
  try:
    (
        dfFile.repartition(1) #Creates one part- file
             .write
             .format("csv") 
             .mode("overwrite")
             .option("header", hasHeader)
             .option("delimiter", delimiter)
             .option("emptyValue", "")
             .option("nullValue", "")
             .option("quote", "\u0000")
             .save(temp_dir)
    )
    
    # Find the part file
    Files = os.listdir(temp_dir)
    PartFileName = next(entry for entry in Files if entry.startswith('part-'))
    
    # Copy part file to final destination
    TempJson = os.path.join(temp_dir, PartFileName)
    
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(destFinalTarget), exist_ok=True)
    
    # Copy file
    shutil.copy2(TempJson, destFinalTarget)
    
  finally:
    # Clean up temporary directory
    shutil.rmtree(temp_dir, ignore_errors=True)

# COMMAND ----------

# Local file system version of MoveFile
def MoveFile(SourceFile,TargetFile, blobPath):
  import os
  import shutil
  
  # Ensure source file exists
  if os.path.exists(SourceFile):
    # Ensure destination directory exists
    os.makedirs(os.path.dirname(TargetFile), exist_ok=True)
    
    # Move file
    shutil.move(SourceFile, TargetFile)
    return "SUCCESS"
  else:
    print(f"Source file not found: {SourceFile}")
    return "FAILED" 

# COMMAND ----------

# DBTITLE 1,Method createTempViews
def createTempViews(rtList):
  for recordType in rtList:
    rt = recordType[0]
    viewName = recordType[1]

    sqlQuery = f"SELECT RecordsSplitIntoArray AS Details FROM SourceData WHERE RecordType = '{rt}'"
    headerList = []

    #create list for column names
    colList = expColumnNames.filter(expColumnNames.Type == rt).collect()
    for column in colList:
      newColumn = column["FieldName"]
      headerList.append(newColumn)

    numDetailRecords = len(headerList)

    #create detail dataframe for current rt
    detailDF = spark.sql(sqlQuery)

    ## will create a dataframe with the record Details[0], Details[1] etc.. until the end of the number of records that exist in the header
    dfTempDetail = detailDF.select([F.col("Details")[i] for i in range(numDetailRecords)])

    #get detail data (will map the detail dataframe to the headerList via Ordinal positioning)
    dfDetail = spark.createDataFrame(dfTempDetail.collect(),headerList)
    dfDetail.createOrReplaceTempView(viewName)
    print(f"  INFO: Created temp view for {viewName}")


# COMMAND ----------

# DBTITLE 1,SQL to split the records into separate columns
sqlSplitQuery = f"""
WITH RawData AS(
  SELECT 
     substring(Row, 1, charindex('{delimiter}', Row) - 1) AS RecordType
    ,Row AS FullfRecord
  FROM OriginalRawData
)
SELECT 
   RecordType
  ,FullfRecord
  ,split(FullfRecord, '[{delimiter}]', -1) AS RecordsSplitIntoArray
FROM RawData sd
"""

# COMMAND ----------

# DBTITLE 1,Main conversion
from pyspark.sql.functions import substring,col
import pyspark.sql.functions as F

#Load entire file into a dataframe with one column named Row
dfData = AnyFileToDataFrame(dataFilePath)
dfData.createOrReplaceTempView("OriginalRawData") #used in sqlSplitQuery
newDFData = spark.sql(sqlSplitQuery)
newDFData.createOrReplaceTempView("SourceData") #used in createTempViews() method

# #Get the record types for looping through
rtList = expRecordTypes.collect()

createTempViews(rtList)

finalDF = spark.sql(finalSQLQuery.replace("#FileID",fileID).replace('#ClientID', clientID))

########################Begin creation of files
#write detail file out
CreateCSV(finalDF, fullConvertedFilePath, delimiter, "True")


# COMMAND ----------

# DBTITLE 1,Return - Data File Record Count
recordCount = finalDF.count()

returnJSON = """{
       "RecordCount":" """ + str(recordCount) + """ "
       }"""

print(returnJSON)
# Return the result (replaces dbutils.notebook.exit)
print(returnJSON)
spark.stop()
