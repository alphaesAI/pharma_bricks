# Databricks notebook source
# DBTITLE 1,Get File List JSON For Processing
dbutils.widgets.text("ProcessedJSON","","")
ProcessedJSON = dbutils.widgets.get("ProcessedJSON")

print("!!! DEBUG CHECK: MY PATHS ARE ABSOLUTE !!!")

# COMMAND ----------

# DBTITLE 1,Notebook Variable Assignment
fcfNotebook = "/Users/logi@openhealthagents.org/.bundle/pharma_bricks/dev/files/src/etl/databricks-dev/Notebooks/DatalakeProcessing/FCFClaimsProcessing"
procNotebook = "/Users/logi@openhealthagents.org/.bundle/pharma_bricks/dev/files/src/etl/databricks-dev/Notebooks/DatalakeProcessing/MoveFileToProcess"

# COMMAND ----------

# DBTITLE 1,Import Libraries
from pyspark.sql.functions import explode, col

# COMMAND ----------

# DBTITLE 1,Call SynJSONCreatorClass
# MAGIC %run "/Users/logi@openhealthagents.org/.bundle/pharma_bricks/dev/files/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/SynJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Call FileHandling Notebook For Helper Methods
# MAGIC %run "/Users/logi@openhealthagents.org/.bundle/pharma_bricks/dev/files/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/FileHandling"
# COMMAND ----------

# DBTITLE 1,Explode List Into Dataframe with Multiple Columns
filesDF = spark.read.json(spark.sparkContext.parallelize([ProcessedJSON]))

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

# COMMAND ----------

# DBTITLE 1,Get JobID
ErrorMessage = ""
doubleQuote = '"'

# Replaces Scala context maps with the official Databricks Java-Python Gateway interface
ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")

# COMMAND ----------

# DBTITLE 1,Loop Through FileIDs to Process
rJSON = synJSONCreator()

rJSON.addBracketStart()

iterator = 0

for t in explodedFileIDs.collect():
    print(f"Begin {t['FileID']}-{t['FileName']}")
    notebook = ""
    mnt = "/mnt/"
    CurrPath = f"{t['ClientContainer']}{t['CurrentFolderPath']}"
    ProcessedPath = f"{mnt}{t['ClientContainer']}{t['ProcessedFolderPath']}"
    SchemaFile = f"{mnt}{t['SchemaFilePath']}/{t['SchemaFileName']}"
    FullFileName = f"{mnt}{t['ClientContainer']}{t['CurrentFolderPath']}/{t['FileName']}"

    f = path_exists(FullFileName)
    s = path_exists(SchemaFile)

    if f == True and s == True:
        if iterator != 0:
            rJSON.addComma()
            
        if t['FileLayoutDescription'] == "FCF":
            notebook = fcfNotebook
        else:
            notebook = procNotebook

        rJSON.addBraceStart()
        rJSON.addNewEntry("FileID", t['FileID'])
        rJSON.addNewEntry("FileName", t['FileName'])
        
        try: 
            results = dbutils.notebook.run(notebook, 0, {
                 "ClientID": t['ClientID']
                ,"FileID": t['FileID']
                ,"FileLayoutID": t['FileLayoutID']
                ,"FileLayoutDescription": t['FileLayoutDescription']
                ,"ColumnDelimiter": t['ColumnDelimiter']
                ,"HasHeader": t['HasHeader']
                ,"IgnoreHeader": t['IgnoreHeader']
                ,"FullFileName": FullFileName
                ,"SchemaFile": SchemaFile
                ,"ProcessedPath": ProcessedPath
                ,"TextQualifier": t['TextQualifier']
            })
          
            returnedJson = spark.read.json(spark.sparkContext.parallelize([str(results)]))

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