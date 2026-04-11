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

print(toProcessPath)
print(fileName)
print(dataFilePath)
print(fullconvertedFilePath)
print(fullcontrolFilePath)
print(finalControlFilePath)

# COMMAND ----------

# DBTITLE 1,Inject common methods
# MAGIC %run "../CommonMethods/ABC/CreateUserDefinedFunctions"

# COMMAND ----------

# DBTITLE 1,Create Schema Dataframe
#create json dataframe and explode columns
from pyspark.sql.functions import col, explode

dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
expColumnNames = dfJSon.select(explode("RecordTypes").alias("RecordTypes")).select("RecordTypes.Type",explode("RecordTypes.ColumnNames").alias("ColumnNames")).select("Type","ColumnNames.FieldName","ColumnNames.OrdinalPosition","ColumnNames.StartPos","ColumnNames.Length")#.filter("ColumnNames.FieldName" != "TEMPLATE")

expQuerries = dfJSon.select(explode("Querries").alias("Querries")).select("Querries.DetailFile","Querries.ControlFile")
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

def getSelectExpr(availableCols: list, requiredCols: list):
	SQLCommand = ""
	iterator = 0

	#Loop through required columns
	for column in requiredCols:
		if(iterator != 0):
			SQLCommand = SQLCommand + "," #split command for SQL select expr
			# SQLCommand = SQLCommand + "!" #split command for SQL select expr
			
		matchingColumn = ""
		#For each column in required columns loop through to find a match in columns available
		for columnsToMatch in availableCols:
			if column.lower() == columnsToMatch.lower():
				matchingColumn = columnsToMatch
				break

		if matchingColumn == "":
			SQLCommand = SQLCommand + "null " + " AS " + column
			# SQLCommand = SQLCommand + "CAST(null AS STRING) " + " AS " + column
		else:
			SQLCommand = SQLCommand + columnsToMatch + " AS " + column
		iterator = iterator + 1
	
	return SQLCommand #.split("!")

# COMMAND ----------

def DynamicUnionOfDataframes(dfList: list, dfLrequiredColsist: list):
  sqlQuery = ""
  iterator = 0
  
  for view in dfList:
    iterator = iterator + 1
    queryToGetAvailableColumns = """DESCRIBE """ + view
    currentSchemaColumns = spark.sql(queryToGetAvailableColumns)
    availableColumns = []
 
    for column in currentSchemaColumns.collect():
      availableColumns.append(column.col_name)

    columnSQLCommand = getSelectExpr(availableColumns, requiredCols)

    #generate sql script
    if(iterator == len(dfList)):
      sqlQuery += "SELECT " + columnSQLCommand + " FROM " + view
    else:
      sqlQuery += "SELECT " + columnSQLCommand + " FROM " + view + " UNION ALL "

  
  # print(sqlQuery)
  combinedDF = spark.sql(sqlQuery)
  combinedDF.createOrReplaceTempView("UnionDetail")

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
from pyspark.sql.functions import substring, col, lit

#Load entire file into a dataframe with one column named Row
dfData = AnyFileToDataFrame(dataFilePath)

#create a list for later use :)
dfList = []
# get a unique list of fields for union
requiredCols = []

##filter by RecordType column
for valueType in expColumnNames.filter(col("FieldName") == "RecordType").collect():
  RecordType = valueType["Type"]
  RecordFieldName = valueType["FieldName"]
  RecordStartPos = valueType["StartPos"]
  RecordLength = valueType["Length"]
  print("Processing RecordType: " + RecordType)

  #create a new dataframe for each one filtering by the RecordType
  dfTempDataFrame = dfData.withColumn("RecordTypeFilter", substring(dfData.Row, RecordStartPos, RecordLength))
  dfFinalTempDataFrame = dfTempDataFrame.where(dfTempDataFrame.RecordTypeFilter == RecordType)

  SQLQuery = ""
  iterator = 0

  #Loop through and split the row into columns
  for row in expColumnNames.filter(expColumnNames.Type == RecordType).collect():
    Type = row["Type"] 
    FieldName = row["FieldName"]
    StartPos = row["StartPos"]
    Length = row["Length"]

    if(iterator == 0):
      SQLQuery += "substring(Row, " +  str(StartPos) + ", " + str(Length) + ") AS " + FieldName
    else:
      SQLQuery += "|substring(Row, " +  str(StartPos) + ", " + str(Length) + ") AS " + FieldName
    iterator += 1
    
    if(FieldName not in requiredCols):
      requiredCols.append(FieldName)

  # print(SQLQuery)
  dfFinal = dfFinalTempDataFrame.selectExpr(SQLQuery.split("|"))
  dfFinal.createOrReplaceTempView(RecordType)
  dfList.append(RecordType)

#union all the record types together into a set list
DynamicUnionOfDataframes(dfList, requiredCols)

finalDetailQuery = ""
finalControlQuery = ""

#run querries
for row in expQuerries.collect():
  finalDetailQuery = row["DetailFile"]
  finalControlQuery = row["ControlFile"]

#load it into a datamodel
dfDetail = spark.sql(finalDetailQuery)
#write conversion file to csv
CreateCSV(dfDetail, fullconvertedFilePath, delimiter, "True")

# if(hasControlFile == True): just going to assume it will always have a ccontrol for now :)
dfControlFile = spark.sql(finalControlQuery)
CreateCSV(dfControlFile, fullcontrolFilePath, delimiter, "True")
#move the control file to ToProcess
MoveFile(fullcontrolFilePath,finalControlFilePath,blobPath)

# COMMAND ----------

# DBTITLE 1,Return - Data File Record Count
recordCount = dfDetail.count()

returnJSON = """{
       "RecordCount":" """ + str(recordCount) + """ "
       }"""

print(returnJSON)
#return JSON
dbutils.notebook.exit(returnJSON)
