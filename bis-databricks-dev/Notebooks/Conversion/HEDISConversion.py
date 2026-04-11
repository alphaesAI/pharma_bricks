# Databricks notebook source
# DBTITLE 1,Set Parameters
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
dbutils.widgets.text("HasControlFile","","")

fileId = dbutils.widgets.get("FileId") 
FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
currentContainer = dbutils.widgets.get("CurrentContainer") 
currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
fileName = dbutils.widgets.get("FileName") 
delimiter = dbutils.widgets.get("Delimiter")
conversionType = dbutils.widgets.get("ConversionType")
conversionJsonContainer = dbutils.widgets.get("ConversionJsonContainer") 
conversionJsonFolderPath = dbutils.widgets.get("ConversionJsonFolderPath") 
conversionJsonFileName = dbutils.widgets.get("ConversionJsonFileName")
hasControlFile = dbutils.widgets.get("HasControlFile")

mountPoint = "/mnt/"
blobPath = mountPoint + currentContainer + "blob" 
toProcessPath = blobPath + currentFolderPath 
dataFilePath = toProcessPath + "/" + fileName
conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" +  conversionJsonFileName

convertedFilePath = blobPath + "/ConvertedFiles/" + conversionType #PremeraPharmacyOMIGPAL
fullconvertedFilePath = convertedFilePath + "/" + fileName + "/" + fileName

##need this to cleanup the name for the control file
pathList = os.path.splitext(fileName)
fileFolderName = pathList[0]

controlFileName = fileFolderName + ".ctl"
fullcontrolFilePath = convertedFilePath + "/" + controlFileName
ctlProcessPath = toProcessPath + "/" + controlFileName

finalControlFilePath = toProcessPath + controlFileName

returnJSON  = ""

print(blobPath)
print(toProcessPath)
print(fileName)
print(dataFilePath)
print(fullconvertedFilePath)
print(fullcontrolFilePath)
print(finalControlFilePath)

# COMMAND ----------

# DBTITLE 1,Create Schema Dataframe
#create json dataframe and explode columns
from pyspark.sql.functions import col, explode

dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
expColumnNames = dfJSon.select(explode("RecordTypes").alias("RecordTypes")).select("RecordTypes.Type",explode("RecordTypes.ColumnNames").alias("ColumnNames")).select("Type","ColumnNames.FieldName","ColumnNames.OrdinalPosition")

expQuerries = dfJSon.select(explode("Querries").alias("Querries")).select("Querries.HeaderDataFrame","Querries.DetailDataFrame","Querries.ControlDataFrame")

expColumnNames.createOrReplaceTempView("Columns")
expQuerries.createOrReplaceTempView("Querries")

# COMMAND ----------

# DBTITLE 1,Loads entire file into an rdd and converts it to Rows (single row per record)
def AnyFileToDataFrame(FileLocation):
  dfFile = spark.read.format("csv").option("delimiter","\n").load(FileLocation).withColumnRenamed("_c0", "Row")
  dfFile.createOrReplaceTempView("CurrentFile")
  return dfFile

# COMMAND ----------

# DBTITLE 1,Output CSV
import os

def CreateCSV(dfFile, destFinalTarget, delimiter, hasHeader):
  dbfs = "/dbfs"
  
  pathList = os.path.splitext(destFinalTarget)
  destTempTarget = pathList[0] + '/'
  extension = pathList[1]

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

def MoveFile(SourceFile,TargetFile, blobPath):
  dfFrame = dbutils.fs.ls(blobPath)
  #ensures there is no empty file in the root directory to stop us from copying to ToProcess
  for item in dfFrame:
    if(item.size > 0):
      dbutils.fs.rm(item.path)

  dbutils.fs.mv(SourceFile,TargetFile)

  return "SUCCESS" 

# COMMAND ----------

# DBTITLE 1,Convert Source File to DataFrame
from pyspark.sql.functions import substring,col
import pyspark.sql.functions as F

#Load entire file into a dataframe with one column named Row
dfData = AnyFileToDataFrame(dataFilePath)
dfData.createOrReplaceTempView("OriginalRawData")

sqlSplitQuery = f"""
WITH RawData AS(
  SELECT 
     substring(Row, 1, charindex('{delimiter}', Row) - 1) AS RecordType
    ,substring(Row, charindex('{delimiter}', Row) + 1, length(Row)) AS RestOfRecord
  FROM OriginalRawData
)
SELECT 
   RecordType
  ,RestOfRecord
  ,split(RestOfRecord, '[{delimiter}]', -1) AS RecordsSplitIntoArray
FROM RawData sd
"""

newDFData = spark.sql(sqlSplitQuery)
newDFData.createOrReplaceTempView("SourceData") #this needs to be here

configQuery = """
SELECT 
   HeaderDataFrame
  ,DetailDataFrame
  ,ControlDataFrame
FROM Querries"""

#get querries for Control/Header and Detail
sqlHeaderListQuery = spark.sql(configQuery).first()[0]
sqlDetailQuery = spark.sql(configQuery).first()[1]
sqlControlQuery = spark.sql(configQuery).first()[2]

#####Create Header
headerDF = spark.sql(sqlHeaderListQuery)
headerList = []

for column in headerDF.collect():
  newColumn = column["Header"]
  headerList.append(newColumn)

numDetailRecords = len(headerList)

#####Create Detail
detailDF = spark.sql(sqlDetailQuery)
# detailDF.createOrReplaceTempView("DetailDF")

## will create a dataframe with the record Details[0], Details[1] etc.. until the end of the number of records that exist in the header
dfTempDetail = detailDF.select([F.col("Details")[i] for i in range(numDetailRecords)])
# dfTempDetail.createOrReplaceTempView("TempDetailData")

#get detail data (will map the detail dataframe to the headerList via Ordinal positioning)
dfDetail = spark.createDataFrame(dfTempDetail.collect(),headerList)
# dfDetail.createOrReplaceTempView("DetailData")

#####Create Control
dfControlFile = spark.sql(sqlControlQuery)

########################Begin creation of files
#write detail file out
CreateCSV(dfDetail, fullconvertedFilePath, delimiter, "True")
#write control file out
CreateCSV(dfControlFile, fullcontrolFilePath, delimiter, "True")
# move the control file to ToProces
MoveFile(fullcontrolFilePath,finalControlFilePath, blobPath)

# COMMAND ----------

# DBTITLE 1,Return - Data File Record Count
recordCount = dfDetail.count()

returnJSON = """{
       "RecordCount":" """ + str(recordCount) + """ "
       }"""

print(returnJSON)
#return JSON
dbutils.notebook.exit(returnJSON)
