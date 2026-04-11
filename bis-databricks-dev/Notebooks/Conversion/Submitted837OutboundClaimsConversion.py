# Databricks notebook source
import os

dbutils.widgets.text("FileId","","")
dbutils.widgets.text("FileLayoutDescription","","")
dbutils.widgets.text("CurrentContainer","","")
dbutils.widgets.text("CurrentFolderPath","","")
dbutils.widgets.text("ConversionType","","")
dbutils.widgets.text("FileName","","")
dbutils.widgets.text("Delimiter","","")
dbutils.widgets.text("ConversionJsonContainer","","")
dbutils.widgets.text("ConversionJsonFolderPath","","")
dbutils.widgets.text("ConversionJsonFileName","","")

fileID = dbutils.widgets.get("FileId") 
FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
currentContainer = dbutils.widgets.get("CurrentContainer") 
currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
fileName = dbutils.widgets.get("FileName") 
delimiter = dbutils.widgets.get("Delimiter")
conversionType = dbutils.widgets.get("ConversionType")
conversionJsonContainer = dbutils.widgets.get("ConversionJsonContainer") 
conversionJsonFolderPath = dbutils.widgets.get("ConversionJsonFolderPath") 
conversionJsonFileName = dbutils.widgets.get("ConversionJsonFileName")

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

# jdbc url for connection to config db
jdbcDatabase = "Configuration_DB_"+ currentContainer.upper()
jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase

# COMMAND ----------

# DBTITLE 1,Get ClientID based on current container name
stmnt = f"""SELECT ClientID FROM refClient WHERE ClientDescription = '{currentContainer}'"""
clientID = (spark.read.format("jdbc") 
        .options(url=jdbcUrl,
                driver='com.microsoft.sqlserver.jdbc.SQLServerDriver',            
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

# DBTITLE 1,Method: CreateCSV
def CreateCSV(dfFile, destFinalTarget, delimiter, hasHeader):
  dbfs = "/dbfs"
  
  pathList = os.path.splitext(destFinalTarget)
  destTempTarget = pathList[0] + '/'
  extension = pathList[1]

  (
      dfFile.repartition(1) #Creates one part- file
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

# DBTITLE 1,Method: MoveFile
def MoveFile(SourceFile,TargetFile, blobPath):
  dfFrame = dbutils.fs.ls(blobPath)
  #ensures there is no empty file in the root directory to stop us from copying to ToProcess
  for item in dfFrame:
    if(item.size > 0):
      dbutils.fs.rm(item.path)

  dbutils.fs.mv(SourceFile,TargetFile)

  return "SUCCESS" 

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
#return JSON
dbutils.notebook.exit(returnJSON)
