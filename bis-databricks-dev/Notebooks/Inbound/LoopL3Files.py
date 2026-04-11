# Databricks notebook source
# DBTITLE 1,Create and setup parameter
dbutils.widgets.text("validationJSON","","")

validationJSON = dbutils.widgets.get("validationJSON")

# COMMAND ----------

# DBTITLE 1,Load File JSON into DataFrame and Explode
from pyspark.sql.functions import explode, col, sha2, concat_ws, coalesce, lit

jsonList = []
jsonList.append(validationJSON)
files_df = spark.read.json(sc.parallelize(jsonList)) 

# files_df = spark.read.format("json").option("multiline", "true").load(validationJSON)
explodedFiles = files_df.select(explode("FileIds")).select(
        "col.FileID"
        ,"col.CurrentContainer"
        ,"col.CurrentFolderPath"
        ,"col.FileName"
        ,"col.HasHeader"
        ,"col.ColumnDelimiter"
        ,"col.IgnoreHeader"
        ,"col.TextQualifier"
        ,"col.HasControlFile"
        ,"col.ControlContainer"
        ,"col.ControlFolderPath"
        ,"col.ControlFileName"
        ,"col.ControlHasHeader"
        ,"col.ControlColumnDelimiter"
        ,"col.ValidationFileContainer"
        ,"col.ValidationFileFolderPath"
        ,"col.ValidationFileName"
        ,"col.ValidatedContainer"
        ,"col.ValidatedFolderPath"
        ,"col.RegistrationDate"
        ,"col.FullCurrentPath"
        ,"col.FullValidatedPath"
        ,"col.ConversionType"
        ,"col.FileExtension"
        )

display(explodedFiles)

# COMMAND ----------

doubleQuote = """ " """.strip()
rJSON ="["
iterator = 0;
mountPoint = "/mnt/"

filesCollect = explodedFiles.collect()
for f in filesCollect:
  fileID = f["FileID"]
  currentContainer = f["CurrentContainer"]
  currentFolderPath = f["CurrentFolderPath"]
  fileName = f["FileName"]
  hasHeader = f["HasHeader"]
  columnDelimiter = f["ColumnDelimiter"]
  ignoreHeader = f["IgnoreHeader"]
  textQualifier = f["TextQualifier"]
  controlContainer = f["ControlContainer"]
  controlFolderPath = f["ControlFolderPath"]
  controlFileName = f["ControlFileName"]
  controlHasHeader = f["ControlHasHeader"]
  controlColumnDelimiter = f["ControlColumnDelimiter"]
  validationFileContainer = f["ValidationFileContainer"]
  validationFileFolderPath = f["ValidationFileFolderPath"]
  validationFileName = f["ValidationFileName"]
  validatedContainer = f["ValidatedContainer"]
  validatedFolderPath = f["ValidatedFolderPath"]
  registrationDate = f["RegistrationDate"]
  fullCurrentPath = f["FullCurrentPath"]
  fullValidatedPath = f["FullValidatedPath"]
  conversionType = f["ConversionType"]
  fileExtension = f["FileExtension"]
  
  if(conversionType == "837"):
    fileName = fileName.substring(0, fileName.lastIndexOf('.')).concat(".csv") 
  
  errorMessage  = ""
  errorFolderName = fileName
  if(fileName.lower()[-4] == ".txt" or fileName.lower()[-4] == ".csv"):
    errorFolderName = fileName.slice(0, fileName.lastIndexOf("."))
    
  fullError = mountPoint +fullValidatedPath + "/Error/" + errorFolderName + ".err"

  results = ""

  print(f"INFO: Starting L3 Validation for: FID:{fileID}, FName:{fileName}")

  try:
    notebookRunParameters = {"FileID":fileID
                          ,"CurrentContainer":currentContainer
                          ,"CurrentFolderPath":currentFolderPath
                          ,"FileName":fileName
                          ,"HasHeader":hasHeader
                          ,"ColumnDelimiter":columnDelimiter
                          ,"IgnoreHeader":ignoreHeader
                          ,"TextQualifier":textQualifier
                          ,"ControlContainer":controlContainer
                          ,"ControlFolderPath":controlFolderPath
                          ,"ControlFileName":controlFileName
                          ,"ControlHasHeader":controlHasHeader
                          ,"ControlColumnDelimiter":controlColumnDelimiter
                          ,"ValidatedFolderPath":validatedFolderPath
                          ,"ValidationFileContainer":validationFileContainer
                          ,"ValidationFileFolderPath":validationFileFolderPath
                          ,"ValidationFileName":validationFileName
                          ,"FullError":fullError
    }
    
    returnResults = dbutils.notebook.run("./Level3Validations", 0, notebookRunParameters)
    
    results = f""""Status": "SUCCESS"
      ,{returnResults}
      ,"ErrorMessage": "" """
  except Exception as e:
    results = f""""Status": "FAILED"
      ,"RecordCountMismatch": "0"
      ,"SumColumnValueMismatch": "0"
      ,"RowValueMismatch": "0"
      ,"SystemException": "true"
      ,"ErrorPathSchema": "{fullError.replace("//","/")}"
      ,"ErrorMessage":"{bytes(str(e), "utf-8").decode("unicode_escape")}" """

  if(iterator > 0):
    rJSON += "," 
    
  rJSON += f"""
      {{
      "FileID": "{str(fileID)}"
      ,"FullCurrentPath": "{fullCurrentPath}"
      ,"FileName": "{fileName}"
      ,"CurrentContainer": "{currentContainer}"
      ,"CurrentFolderPath": "{currentFolderPath}"
      ,"ValidatedContainer": "{validatedContainer}"
      ,"ValidatedFolderPath": "{validatedFolderPath}"
      ,"FullValidatedPath": "{fullValidatedPath}"
      ,"ConversionType": "{conversionType}"
      ,"RegistrationDate": "{registrationDate}"
      ,"FileExtension": "{fileExtension}"
      ,{results}
      }}
  """            
  iterator+=1

rJSON+="]"


# COMMAND ----------

# DBTITLE 1,Exit Notebook
dbutils.notebook.exit(rJSON)
