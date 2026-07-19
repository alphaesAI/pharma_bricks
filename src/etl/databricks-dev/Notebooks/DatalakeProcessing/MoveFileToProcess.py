# Databricks notebook source
# DBTITLE 1,Create and setup parameters
# File Parameters
dbutils.widgets.text("ClientID","","") 
dbutils.widgets.text("FileID","","") 
dbutils.widgets.text("FileLayoutID","","") 
dbutils.widgets.text("FileLayoutDescription","","") 
dbutils.widgets.text("ColumnDelimiter","","") 
dbutils.widgets.text("HasHeader","","") 
dbutils.widgets.text("IgnoreHeader","","") 
dbutils.widgets.text("TextQualifier","","") 

# File to be Processed
dbutils.widgets.text("FullFileName","","")  

# Schema File
dbutils.widgets.text("SchemaFile","","")  

# Processed File 
dbutils.widgets.text("ProcessedPath","","") 

ClientId = dbutils.widgets.get("ClientID")
FileId = dbutils.widgets.get("FileID")  
FileLayoutId = dbutils.widgets.get("FileLayoutID")
FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
ColumnDelimiter = dbutils.widgets.get("ColumnDelimiter")
HasHeader = str(dbutils.widgets.get("HasHeader")).capitalize()
IgnoreHeader = str(dbutils.widgets.get("IgnoreHeader")).capitalize()
textQualifier = dbutils.widgets.get("TextQualifier")

FullFileName = dbutils.widgets.get("FullFileName") 
SchemaFile = dbutils.widgets.get("SchemaFile")
ProcessedPath = dbutils.widgets.get("ProcessedPath")

# COMMAND ----------

# DBTITLE 1,Call SynJSONCreatorClass
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/SyncJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Call FileHandling Notebook
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/FileHandling"

# COMMAND ----------

# DBTITLE 1,Get JobID
from pyspark.sql.types import StructType
from pyspark.sql.functions import lit, to_timestamp, current_timestamp

ErrorMessage = ""
doubleQuote = '"'

# Get job ID - Serverless compatible version
try:
    ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")
except Exception:
    # Serverless fallback - ctx.tags() is not whitelisted on Serverless
    currentJobId = "Undefined"

# COMMAND ----------

# DBTITLE 1,Copy Dataframe to Parquet Format and add FileID
def process_move_file(ClientId, FileId, FileLayoutId, FileLayoutDescription,
                      ColumnDelimiter, HasHeader, IgnoreHeader, textQualifier,
                      FullFileName, SchemaFile, ProcessedPath):
    """
    Main file move processing function that can be called directly.
    Returns JSON string with processing results.
    """
    rJSON = synJSONCreator()
    ErrorMessage = ""
    doubleQuote = '"'
    
    # Get job ID - Serverless compatible
    try:
        ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
        currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")
    except Exception:
        currentJobId = "Undefined"
    
    rJSON.addBraceStart()
    rJSON.addNewEntry("CurrentJobId", currentJobId)
    
    dfFile = spark.createDataFrame([], StructType([]))
    
    try:
        if IgnoreHeader == "False":
            dfFile = delimitedFile(FullFileName, SchemaFile, HasHeader, ColumnDelimiter, textQualifier)
        elif IgnoreHeader == "True" and HasHeader == "True":
            dfFile = isIgnoreHeader(FullFileName, SchemaFile, ColumnDelimiter, textQualifier)

        # Serverless-compatible empty check: use len(df.take(1)) instead of df.rdd.isEmpty()
        if len(dfFile.take(1)) > 0:
            filtered_cols = [col_name for col_name in dfFile.columns if not col_name.startswith("Filler_")]
            dfFile = dfFile.select(filtered_cols)
            
            dfFile = dfFile.withColumn("FILE_ID", lit(FileId)) \
                .withColumn("FILE_LAYOUT_ID", lit(FileLayoutId)) \
                .withColumn("FILE_LAYOUT_DESCRIPTION", lit(FileLayoutDescription)) \
                .withColumn("CLIENT_ID", lit(ClientId)) \
                .withColumn("LOAD_DATETIME", to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))

            dfFile.write.format("parquet").mode("append").save(ProcessedPath)

            rJSON.addNewEntry("Status", "SUCCESS")
            rJSON.addNewEntry("ProcessedCount", str(dfFile.count()))
            rJSON.addNewEntry("ErrorMessage", "", newLine=False)
        else:
            # Empty DataFrame after filtering - not an error, just no data
            rJSON.addNewEntry("Status", "SUCCESS")
            rJSON.addNewEntry("ProcessedCount", "0")
            rJSON.addNewEntry("ErrorMessage", "No records after filtering", newLine=False)
            
    except Exception as e:
        # Clean error message: remove quotes, newlines, and control characters that break JSON
        clean_err = str(e).strip().replace(doubleQuote, "").replace("\n", " ").replace("\r", " ").replace("\t", " ")
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("ProcessedCount", "0")
        rJSON.addNewEntry("ErrorMessage", clean_err, newLine=False) 

    rJSON.addBraceEnd()
    return rJSON.getJSON()
