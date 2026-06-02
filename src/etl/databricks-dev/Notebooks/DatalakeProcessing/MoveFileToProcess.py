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

# DBTITLE 1,Call SynJSONCreatorClass -  FIX BEFORE CHECK IN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Call FileHandling Notebook
# MAGIC %run "../CommonMethods/ABC/FileHandling"

# COMMAND ----------

# DBTITLE 1,Get JobID
from pyspark.sql.types import StructType
from pyspark.sql.functions import lit, to_timestamp, current_timestamp

ErrorMessage = ""
doubleQuote = '"'

# Replaces Scala context logic with official Databricks Java-Python Gateway interface
ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")

# COMMAND ----------

# DBTITLE 1,Copy Dataframe to Parquet Format and add FileID
rJSON = synJSONCreator()

ErrorMessage = ""

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

# Empty DataFrame initialisation matching sqlContext.emptyDataFrame
dfFile = spark.createDataFrame([], StructType([]))

try:
    # Routes parameters using your helper methods derived from FileHandling
    if IgnoreHeader == "False":
        dfFile = delimitedFile(FullFileName, SchemaFile, HasHeader, ColumnDelimiter, textQualifier)
    elif IgnoreHeader == "True" and HasHeader == "True":
        dfFile = isIgnoreHeader(FullFileName, SchemaFile, ColumnDelimiter, textQualifier)

    if not dfFile.rdd.isEmpty():
        # Cleanly filters out columns that start with "Filler_" mimicking Scala's dynamic map filter sequence
        filtered_cols = [col_name for col_name in dfFile.columns if not col_name.startswith("Filler_")]
        dfFile = dfFile.select(filtered_cols)
        
        # Add file based columns to df
        dfFile = dfFile.withColumn("FILE_ID", lit(FileId)) \
            .withColumn("FILE_LAYOUT_ID", lit(FileLayoutId)) \
            .withColumn("FILE_LAYOUT_DESCRIPTION", lit(FileLayoutDescription)) \
            .withColumn("CLIENT_ID", lit(ClientId)) \
            .withColumn("LOAD_DATETIME", to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))

        # write dataframe to processed path
        dfFile.write.format("parquet").mode("append").save(ProcessedPath)

        rJSON.addNewEntry("Status", "SUCCESS")
        rJSON.addNewEntry("ProcessedCount", str(dfFile.count()))
        rJSON.addNewEntry("ErrorMessage", "", newLine=False) 
        
except Exception as e:
    clean_err = str(e).strip().replace(doubleQuote, "")
    rJSON.addNewEntry("Status", "FAILED")
    rJSON.addNewEntry("ProcessedCount", "0")
    rJSON.addNewEntry("ErrorMessage", clean_err, newLine=False) 

rJSON.addBraceEnd()

# COMMAND ----------

# DBTITLE 1,Add Processed Records Return
returnVal = rJSON.getJSON()
dbutils.notebook.exit(returnVal)