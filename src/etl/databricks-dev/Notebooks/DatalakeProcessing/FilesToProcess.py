# Databricks notebook source
# DBTITLE 1,Get File List JSON For Processing
dbutils.widgets.text("ProcessedJSON","","")
ProcessedJSON = dbutils.widgets.get("ProcessedJSON")

print("!!! DEBUG CHECK: MY PATHS ARE ABSOLUTE !!!")

# COMMAND ----------

# DBTITLE 1,Import Libraries
from pyspark.sql.functions import explode, col

# COMMAND ----------

# DBTITLE 1,Call SynJSONCreatorClass
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/SyncJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Call FileHandling Notebook For Helper Methods
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/FileHandling"

# COMMAND ----------

# DBTITLE 1,Load FCFClaimsProcessing Functions
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/FCFClaimsProcessing"

# COMMAND ----------

# DBTITLE 1,Load MoveFileToProcess Functions
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/DatalakeProcessing/MoveFileToProcess"

# COMMAND ----------

# DBTITLE 1,Explode List Into Dataframe with Multiple Columns
import json

if not ProcessedJSON or ProcessedJSON.strip() == "":
    raise ValueError("ProcessedJSON parameter is empty. This notebook requires JSON data to be passed via the ProcessedJSON widget parameter.")

filesDF = spark.createDataFrame([json.loads(ProcessedJSON)])

explodedFileIDs = filesDF.select(explode(col("FileIds"))).select(
     col("col.ClientID")
    ,col("col.FileID")
    ,col("col.FileName")
    ,col("col.ClientContainer")
    ,col("col.CurrentFolderPath")
    ,col("col.ProcessedFolderPath")
    ,col("col.ColumnDelimiter")
    ,col("col.HasHeader")
    ,col("col.IgnoreHeader")
    ,col("col.FileLayoutID")
    ,col("col.FileLayoutDescription")
    ,col("col.SchemaFileName")
    ,col("col.SchemaFilePath")
    ,col("col.TextQualifier")
)

ErrorMessage = ""
doubleQuote = '"'

ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()

try:
    currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")
except Exception:
    currentJobId = "Undefined"

rJSON = synJSONCreator()

rJSON.addBracketStart()

iterator = 0
exploded_pd = explodedFileIDs.toPandas()

if exploded_pd.empty:
    raise ValueError("No files found in explodedFileIDs. Please check the input JSON or upstream processing.")

for index, t in exploded_pd.iterrows():
    print(f"Begin {t['FileID']}-{t['FileName']}")
    CurrPath = f"{t['ClientContainer']}{t['CurrentFolderPath']}"
    # FIX: Use ProcessedFolderPath as absolute, do not prepend ClientContainer
    ProcessedPath = t['ProcessedFolderPath']
    SchemaFile = f"{t['SchemaFilePath']}/{t['SchemaFileName']}"
    FullFileName = f"{t['ClientContainer']}{t['CurrentFolderPath']}/{t['FileName']}"

    print(f"--> Target Data Path: file:{FullFileName}")
    print(f"--> Target Schema Path: file:{SchemaFile}")
    print(f"--> Target Output Path: {ProcessedPath}")

    try:
        dbutils.fs.ls(f"file:{FullFileName}")
        f = True
    except Exception as e:
        print(f"Data file check failed with error: {str(e)}")
        f = False

    try:
        dbutils.fs.ls(f"file:{SchemaFile}")
        s = True
    except Exception as e:
        print(f"Schema file check failed with error: {str(e)}")
        s = False

    if f == True and s == True:
        if iterator != 0:
            rJSON.addComma()

        rJSON.addBraceStart()
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['FileName'])
        try:
            if t['FileLayoutDescription'] == "FCF":
                results = process_fcf_claims(
                    ClientId=t['ClientID'],
                    FileId=t['FileID'],
                    FileLayoutId=t['FileLayoutID'],
                    FileLayoutDescription=t['FileLayoutDescription'],
                    ColumnDelimiter=t['ColumnDelimiter'],
                    HasHeader=t['HasHeader'],
                    IgnoreHeader=t['IgnoreHeader'],
                    textQualifier=t['TextQualifier'],
                    FullFileName=FullFileName,
                    SchemaFile=SchemaFile,
                    ProcessedPath=ProcessedPath
                )
            else:
                results = process_move_file(
                    ClientId=t['ClientID'],
                    FileId=t['FileID'],
                    FileLayoutId=t['FileLayoutID'],
                    FileLayoutDescription=t['FileLayoutDescription'],
                    ColumnDelimiter=t['ColumnDelimiter'],
                    HasHeader=t['HasHeader'],
                    IgnoreHeader=t['IgnoreHeader'],
                    textQualifier=t['TextQualifier'],
                    FullFileName=FullFileName,
                    SchemaFile=SchemaFile,
                    ProcessedPath=ProcessedPath
                )
          
            returnedJson = spark.createDataFrame([json.loads(str(results))])

            for x in returnedJson.collect():
                rJSON.addNewEntry("FullFilePath", ProcessedPath)
                rJSON.addNewEntry("CurrentJobId", x['CurrentJobId'])
                rJSON.addNewEntry("Status", x['Status']) 
                rJSON.addNewEntry("RecordCount", x['ProcessedCount'])     
                rJSON.addNewEntry("ErrorMessage", x['ErrorMessage'], False)                                    
                
        except Exception as e:
            clean_err = str(e).strip().replace(doubleQuote, "")
            rJSON.addNewEntry("CurrentJobId", "Undefined")
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("RecordCount", "")   
            rJSON.addNewEntry("ErrorMessage", clean_err, False)   
  
        rJSON.addBraceEnd()
  
    elif f == False:
        if iterator != 0: rJSON.addComma()
        rJSON.addBraceStart()
        rJSON.addNewEntry("CurrentJobId", "Undefined")
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['FileName'])
        rJSON.addNewEntry("FullFilePath", CurrPath)
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("RecordCount", "")   
        rJSON.addNewEntry("ErrorMessage", "Data File Not Found", False)
        rJSON.addBraceEnd()
        
    elif s == False:
        if iterator != 0: rJSON.addComma()
        rJSON.addBraceStart()
        rJSON.addNewEntry("CurrentJobId", "Undefined")
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['SchemaFileName'])
        rJSON.addNewEntry("FullFilePath", CurrPath)
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("RecordCount", "")   
        rJSON.addNewEntry("ErrorMessage", "Schema File Not Found", False)
        rJSON.addBraceEnd()
        
    iterator += 1

rJSON.addBracketEnd()

returnVal = rJSON.getJSON()
print(returnVal)
dbutils.notebook.exit(returnVal)

# COMMAND ----------

# DBTITLE 1,Get JobID
ErrorMessage = ""
doubleQuote = '"'

ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()

try:
    # This works on standard clusters, but will fail gracefully on Serverless
    currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")
except Exception:
    # Serverless fallback during testing
    currentJobId = "Undefined"

# COMMAND ----------

# DBTITLE 1,Loop Through FileIDs to Process
rJSON = synJSONCreator()

rJSON.addBracketStart()

iterator = 0

# Convert to Pandas rows to completely bypass the JVM layer
exploded_pd = explodedFileIDs.toPandas()

if exploded_pd.empty:
    raise ValueError("No files found in explodedFileIDs. Please check the input JSON or upstream processing.")

for index, t in exploded_pd.iterrows():
    print(f"Begin {t['FileID']}-{t['FileName']}")
    CurrPath = f"{t['ClientContainer']}{t['CurrentFolderPath']}"
    ProcessedPath = f"{t['ClientContainer']}{t['ProcessedFolderPath']}"
    SchemaFile = f"{t['SchemaFilePath']}/{t['SchemaFileName']}"
    FullFileName = f"{t['ClientContainer']}{t['CurrentFolderPath']}/{t['FileName']}"

    # DEBUG PRINT STATEMENTS
    print(f"--> Target Data Path: file:{FullFileName}")
    print(f"--> Target Schema Path: file:{SchemaFile}")

    # Check if files exist
    try:
        dbutils.fs.ls(f"file:{FullFileName}")
        f = True
    except Exception as e:
        print(f"Data file check failed with error: {str(e)}")
        f = False

    try:
        dbutils.fs.ls(f"file:{SchemaFile}")
        s = True
    except Exception as e:
        print(f"Schema file check failed with error: {str(e)}")
        s = False

    if f == True and s == True:
        if iterator != 0:
            rJSON.addComma()

        rJSON.addBraceStart()
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['FileName'])
        
        try:
            # ✅ FIXED: Call functions directly instead of dbutils.notebook.run()
            if t['FileLayoutDescription'] == "FCF":
                results = process_fcf_claims(
                    ClientId=t['ClientID'],
                    FileId=t['FileID'],
                    FileLayoutId=t['FileLayoutID'],
                    FileLayoutDescription=t['FileLayoutDescription'],
                    ColumnDelimiter=t['ColumnDelimiter'],
                    HasHeader=t['HasHeader'],
                    IgnoreHeader=t['IgnoreHeader'],
                    textQualifier=t['TextQualifier'],
                    FullFileName=FullFileName,
                    SchemaFile=SchemaFile,
                    ProcessedPath=ProcessedPath
                )
            else:
                results = process_move_file(
                    ClientId=t['ClientID'],
                    FileId=t['FileID'],
                    FileLayoutId=t['FileLayoutID'],
                    FileLayoutDescription=t['FileLayoutDescription'],
                    ColumnDelimiter=t['ColumnDelimiter'],
                    HasHeader=t['HasHeader'],
                    IgnoreHeader=t['IgnoreHeader'],
                    textQualifier=t['TextQualifier'],
                    FullFileName=FullFileName,
                    SchemaFile=SchemaFile,
                    ProcessedPath=ProcessedPath
                )
          
            returnedJson = spark.createDataFrame([json.loads(str(results))])

            for x in returnedJson.collect():
                rJSON.addNewEntry("FullFilePath", f"{t['ClientContainer']}{t['ProcessedFolderPath']}")
                rJSON.addNewEntry("CurrentJobId", x['CurrentJobId'])
                rJSON.addNewEntry("Status", x['Status']) 
                rJSON.addNewEntry("RecordCount", x['ProcessedCount'])     
                rJSON.addNewEntry("ErrorMessage", x['ErrorMessage'], False)                                    
                
        except Exception as e:
            clean_err = str(e).strip().replace(doubleQuote, "")
            rJSON.addNewEntry("CurrentJobId", "Undefined")
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("RecordCount", "")   
            rJSON.addNewEntry("ErrorMessage", clean_err, False)   
  
        rJSON.addBraceEnd()
  
    elif f == False:
        if iterator != 0: rJSON.addComma()
        rJSON.addBraceStart()
        rJSON.addNewEntry("CurrentJobId", "Undefined")
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['FileName'])
        rJSON.addNewEntry("FullFilePath", CurrPath)
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("RecordCount", "")   
        rJSON.addNewEntry("ErrorMessage", "Data File Not Found", False)
        rJSON.addBraceEnd()
        
    elif s == False:
        if iterator != 0: rJSON.addComma()
        rJSON.addBraceStart()
        rJSON.addNewEntry("CurrentJobId", "Undefined")
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['SchemaFileName'])
        rJSON.addNewEntry("FullFilePath", CurrPath)
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("RecordCount", "")   
        rJSON.addNewEntry("ErrorMessage", "Schema File Not Found", False)
        rJSON.addBraceEnd()
        
    iterator += 1

rJSON.addBracketEnd()

returnVal = rJSON.getJSON()
print(returnVal)
dbutils.notebook.exit(returnVal)
