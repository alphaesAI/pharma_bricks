# Databricks notebook source
# DBTITLE 1,Setup Parameters
#Data File Parameters
dbutils.widgets.text("FileId","","") #0 
dbutils.widgets.text("CurrentContainer","","") #validate
dbutils.widgets.text("CurrentFolderPath","","") #/MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("FileName","","") #PBC_VIS_FCF_prod_20200227070003. TXT
dbutils.widgets.text("HasHeader","","") #"|"
dbutils.widgets.text("ColumnDelimiter","","") #"|"
dbutils.widgets.text("IgnoreHeader","","") #"|"
dbutils.widgets.text("TextQualifier","","") #"""

#Control File Parameters
dbutils.widgets.text("ControlContainer","","") #validate
dbutils.widgets.text("ControlFolderPath","","") #/MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("ControlFileName","","") #PBC_VIS_FCF_prod_20200227070003.TXT
dbutils.widgets.text("ControlHasHeader","","") #"|"
dbutils.widgets.text("ControlColumnDelimiter","","") #"|"

#Validated Zone Parameters
dbutils.widgets.text("ValidatedFolderPath","","")   #validate

#Schema File Parameters
dbutils.widgets.text("ValidationFileContainer","","")   #validate
dbutils.widgets.text("ValidationFileFolderPath","","") #ValidationRules
dbutils.widgets.text("ValidationFileName","","") #fcf_schema.json 

#Error
dbutils.widgets.text("FullError","","")   


# COMMAND ----------

# DBTITLE 1,Set Variables
mountPoint = "/mnt/"
fileId = dbutils.widgets.get("FileId")  
currentContainer = dbutils.widgets.get("CurrentContainer") 
currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
fileName = dbutils.widgets.get("FileName") 
hasHeader = dbutils.widgets.get("HasHeader")
columnDelimiter = dbutils.widgets.get("ColumnDelimiter")
if(columnDelimiter == ""):
  columnDelimiter ="|"
ignoreHeader = dbutils.widgets.get("IgnoreHeader")
textQualifier = dbutils.widgets.get("TextQualifier")

#Validated Zone
validatedFolderPath = dbutils.widgets.get("ValidatedFolderPath") 

#Configuration File
validationFileContainer = dbutils.widgets.get("ValidationFileContainer") 
validationFileFolderPath = dbutils.widgets.get("ValidationFileFolderPath") 
validationFileName = dbutils.widgets.get("ValidationFileName")

controlContainer = dbutils.widgets.get("ControlContainer") 
controlFolderPath = dbutils.widgets.get("ControlFolderPath") 
controlFileName = dbutils.widgets.get("ControlFileName")
controlHasHeader = dbutils.widgets.get("ControlHasHeader")
cotnrolColumnDelimiter = dbutils.widgets.get("ControlColumnDelimiter")
if(cotnrolColumnDelimiter == ""):
  cotnrolColumnDelimiter ="|"

# get FileName without extension '.txt'
errorFolderName = fileName
if(fileName.lower()[-4] == ".txt" or fileName.lower()[-4] == ".csv"):
  errorFolderName = fileName.slice(0, fileName.lastIndexOf("."))

fullFile = mountPoint + currentContainer + currentFolderPath + "/"+ fileName
fullControl = mountPoint + controlContainer + controlFolderPath + "/"+ controlFileName
fullValidation = mountPoint + validationFileContainer + validationFileFolderPath + "/" +validationFileName
fullError = dbutils.widgets.get("FullError") 

#User For JSON Returned
recordCountMismatch = 0
sumColumnValueMismatch = 0
systemException = "false"
returnJSON  = ""

# COMMAND ----------

# DBTITLE 1,Call L3 Validators Notebook
# MAGIC %run "../CommonMethods/ABC/ValidationsL3"

# COMMAND ----------

# DBTITLE 1,Method hasColumn
def hasColumn (df, col):
  return (col in df.columns)

# COMMAND ----------

# DBTITLE 1, Create Json Dataframes
from pyspark.sql.functions import explode,monotonically_increasing_id,lit,row_number, sequence
from pyspark.sql.window import Window
from pyspark.sql.types import StructType,StructField, StringType

explodedRules = spark.createDataFrame([], StructType([]))
explodedRowCheck = spark.createDataFrame([], StructType([]))
explodedColumns = spark.createDataFrame([], StructType([]))

# creating json dataframe
dfSchema = spark.read.format("json").option("multiline", "true").load(fullValidation)

#explode rules
try:
  explodedRules = dfSchema.select(explode("Rules")).select("col.Name", "col.data_file_query", "col.control_file_query")
except:
  print("INFO: No Rules Defined")

#explode row checks
try:
  explodedRowCheck = dfSchema.select(explode("RowCheck")).select("col.Name", "col.DataFileQuery", "col.Operator", "col.Value")
except:
  print("INFO: No RowChecks Defined")

explodedColumns = dfSchema.select(explode("ColumnNames")).select("col.FieldName").where("FieldName != 'TEMPLATE'")

# display(explodedRules)

# COMMAND ----------

# DBTITLE 1,Create Datafile Dataframe 
dfFile = spark.read \
  .format("csv") \
  .option("header", hasHeader) \
  .option("delimiter", columnDelimiter) \
  .option("quote", textQualifier) \
  .option("inferSchema", "true")\
  .load(fullFile) 

dfData1 = dfFile.withColumn("FILE_ID",lit(fileId)) \
                .withColumn("ROW_ID1",(monotonically_increasing_id()+1))
windowSpec = Window.partitionBy("FILE_ID").orderBy("ROW_ID1")
dfData2 = dfData1.withColumn("ROW_ID", row_number().over(windowSpec))
dfData = dfData2.drop("ROW_ID1")

#Drop unused dataframes
dfFile.unpersist(True)
dfData1.unpersist(True)
dfData2.unpersist(True)

dfData.createOrReplaceTempView("dataDF")

# COMMAND ----------

# DBTITLE 1,Create Controlfile Dataframe 
dfControl = spark.read\
  .format("csv") \
  .option("header", controlHasHeader)\
  .option("delimiter", cotnrolColumnDelimiter) \
  .option("inferSchema", "true")\
  .load(fullControl)

# COMMAND ----------

# DBTITLE 1,Notebook and Job context assignments
import json
notebook_info = json.loads(dbutils.notebook.entry_point.getDbutils().notebook().getContext().toJson())
currentJobId = ""
try: 
    #The tag jobId does not exists when the notebook is not triggered by dbutils.notebook.run(...) 
    currentJobId = notebook_info["tags"]["jobId"] 
except: 
    currentJobId = "-1"

# COMMAND ----------

# DBTITLE 1,Run Level 3 Validations
results = "true"
resultRules = ""
resultRows = 0
errorMessage = "";

rJSON = ""
rJSON += f""""CurrentJobId":"{str(currentJobId)}" """

#Execute level 3 validations
if (hasColumn(dfSchema,"Rules")):
  print("INFO: Processing Rules")
  resultRules = fileRulesValidator(dfData, explodedRules, dfControl, fullError)

if (hasColumn(dfSchema,"RowCheck")):
  print("INFO: Processing RowChecks")
  resultRows = rowCheckValidator(dfData, explodedRowCheck, fullError)


if(resultRules == "false"):
  results = resultRules


# COMMAND ----------

# DBTITLE 1,Error Handling  --Need to update to include the Both types of checks
#If error is returned
if(results == "false"):
  errFile = fullError +"/*.csv"

  dfError = spark.read.format("csv").option("header", "true").load(errFile)
  dfError.createOrReplaceTempView("dfError")

  #query error file to log errors in DB
  # if query is count() then 15 = RecordCountMismatch, then query is sum should be 16 = SumColumnValueMismatch
  ErrorView = sqlContext.sql(
                  """
                  SELECT 
                      monotonically_increasing_id() + 1 as RecordNumber 
                    ,CASE WHEN data_file_query LIKE '%count(%' THEN 15
                      ELSE 16 END AS ErrCnts
                    ,*
                  FROM dfError
                  WHERE validationOutput LIKE '%FAIL%'
                  """
    )

  #Get counts for each type of error
  recordCountMismatch = ErrorView.filter("Errcnts == 15").count()
  sumColumnValueMismatch = ErrorView.filter("Errcnts == 16").count()

  # if catched any error, results = false but won't have any data written into error
  if (ErrorView.count() == 0):
    systemException = "true" 

# COMMAND ----------

# DBTITLE 1,Return JSON --Need to Update to include Rowchecks
#Return JSON for error tracking
rJSON += f"""
      ,"RecordCountMismatch": "{recordCountMismatch}"
      ,"SumColumnValueMismatch": "{sumColumnValueMismatch}"
      ,"RowValueMismatch": "{resultRows}"
      ,"SystemException": "{systemException}"
      ,"ErrorPathSchema": "{fullError.replace("//","/")}" """

# print(rJSON)

#return JSON
dbutils.notebook.exit(rJSON)
