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
textQualifier = dbutils.widgets.get("TextQualifier") # will not be used

FullFileName = dbutils.widgets.get("FullFileName") 
SchemaFile = dbutils.widgets.get("SchemaFile")
ProcessedPath = dbutils.widgets.get("ProcessedPath")

# COMMAND ----------

# DBTITLE 1,Call libraries
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import explode, col, trim, lit, when, upper, unix_timestamp, to_date, to_timestamp, concat, current_timestamp, year
from functools import reduce

# COMMAND ----------

# DBTITLE 1,Call SynJSONCreatorClass
# MAGIC %run "/Workspace/Users/logi@openhealthagents.org/pharma_bricks/src/etl/databricks-dev/Notebooks/CommonMethods/ABC/SyncJSONCreatorClass"

# COMMAND ----------

# DBTITLE 1,Method: createDF - Dataframe Creation
def createDF(file: str, validation: str, delimiter: str):
    
    fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
    parsedSchema = fullSchema.select(explode(col("columnNames"))).select(col("col.FieldName"), col("col.DataType")).filter(col("col.FieldName") != "TEMPLATE")
    
    # Extract string values out from the row array collected locally
    header = [row[0].strip() for row in parsedSchema.select("FieldName").collect()]
    fields = [StructField(fieldName, StringType(), nullable=True) for fieldName in header] 
    schema = StructType(fields)
    
    dfNew = spark.read.format("csv") \
        .schema(schema) \
        .option("header", HasHeader) \
        .option("delimiter", delimiter) \
        .load(file)
    
    # TRIM WHITE SPACES: Replaced Scala's foldLeft with Python's native functools.reduce operation
    dfNew = reduce(lambda DF, colName: DF.withColumn(colName, trim(col(colName))), dfNew.columns, dfNew)
    
    # ADD NEW COLUMNS
    dfNew = dfNew.withColumn("FILE_ID", lit(FileId)) \
        .withColumn("FILE_LAYOUT_ID", lit(FileLayoutId)) \
        .withColumn("FILE_LAYOUT_DESCRIPTION", lit(FileLayoutDescription)) \
        .withColumn("CLIENT_ID", lit(ClientId)) \
        .withColumn("IS_SPLIT_CLAIM", when(col("MA_SPLIT_CLAIM_ID").isNull() | (trim(col("MA_SPLIT_CLAIM_ID")) == ""), 0).otherwise(1)) \
        .withColumn("CLAIM_WEIGHT", (when(col("MA_CLAIM_STATUS") == "6", 7).when(upper(col("MA_CLAIM_STATUS")) == "C", 7).when(col("MA_CLAIM_STATUS") == "8", 5).when((col("MA_CLAIM_STATUS") == "O") | (col("MA_CLAIM_STATUS") == "o"), 1) + ((unix_timestamp(col("MA_CLAIM_UPDATED_DT"), "MM/dd/yyyy HH:mm:ss") - unix_timestamp(lit("01/01/2016 00:00:00"), "MM/dd/yyyy HH:mm:ss")) * 10))) \
        .withColumn("MA_CLAIM_ID_ORIG", when(col("IS_SPLIT_CLAIM") == 1, col("MA_CLAIM_NUM")).otherwise(col("MA_CLAIM_ID_ORIG"))) \
        .withColumn("MA_PATIENT_DOB", to_date(col("MA_PATIENT_DOB"), "MM/dd/yyyy")) \
        .withColumn("MA_BEGINNING_DOS", to_date(col("MA_BEGINNING_DOS"), "MM/dd/yyyy")) \
        .withColumn("MA_CHECK_DATE", to_date(col("MA_CHECK_DATE"), "MM/dd/yyyy")) \
        .withColumn("MA_FINALIZED_FILE_CREATE_DATE", to_date(col("MA_FINALIZED_FILE_CREATE_DATE"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_RECEIVE_DATE", to_date(col("MA_CLAIM_RECEIVE_DATE"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_FINALIZED_DT", to_date(col("MA_CLAIM_FINALIZED_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_ENTRY_DT", to_timestamp(col("MA_CLAIM_ENTRY_DT"), "MM/dd/yyyy HH:mm:ss")) \
        .withColumn("MA_CLAIM_UPDATED_DT", to_timestamp(col("MA_CLAIM_UPDATED_DT"), "MM/dd/yyyy HH:mm:ss")) \
        .withColumn("MA_SUBCRIBER_BIRTH_DATE", to_date(col("MA_SUBCRIBER_BIRTH_DATE"), "MM/dd/yyyy")) \
        .withColumn("MA_BENEFIT_PERIOD_BEGIN_DT", to_date(col("MA_BENEFIT_PERIOD_BEGIN_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_BENEFIT_PERIOD_END_DT", to_date(col("MA_BENEFIT_PERIOD_END_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_PATIENT_CURRENT_ILLNESS_DT", to_date(col("MA_PATIENT_CURRENT_ILLNESS_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_PATIENT_SIMILAR_ILLNESS_DT", to_date(col("MA_PATIENT_SIMILAR_ILLNESS_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_PATIENT_LAST_WORKED_DT", to_date(col("MA_PATIENT_LAST_WORKED_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_PATIENT_RETURN_WORK_DT", to_date(col("MA_PATIENT_RETURN_WORK_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_HOSP_ADMIT_DT", to_date(col("MA_CLAIM_HOSP_ADMIT_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_HOSP_DISCHARGE_DT", to_date(col("MA_CLAIM_HOSP_DISCHARGE_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_STATEMENT_FROM_DT", to_date(col("MA_STATEMENT_FROM_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_STATEMENT_TO_DT", to_date(col("MA_STATEMENT_TO_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT1", to_date(col("MA_CLAIM_OCCUR_DT1"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT2", to_date(col("MA_CLAIM_OCCUR_DT2"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT3", to_date(col("MA_CLAIM_OCCUR_DT3"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT4", to_date(col("MA_CLAIM_OCCUR_DT4"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT5", to_date(col("MA_CLAIM_OCCUR_DT5"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT6", to_date(col("MA_CLAIM_OCCUR_DT6"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT7", to_date(col("MA_CLAIM_OCCUR_DT7"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT8", to_date(col("MA_CLAIM_OCCUR_DT8"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT9", to_date(col("MA_CLAIM_OCCUR_DT9"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT10", to_date(col("MA_CLAIM_OCCUR_DT10"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT11", to_date(col("MA_CLAIM_OCCUR_DT11"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT12", to_date(col("MA_CLAIM_OCCUR_DT12"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT13", to_date(col("MA_CLAIM_OCCUR_DT13"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT14", to_date(col("MA_CLAIM_OCCUR_DT14"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT15", to_date(col("MA_CLAIM_OCCUR_DT15"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT16", to_date(col("MA_CLAIM_OCCUR_DT16"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT17", to_date(col("MA_CLAIM_OCCUR_DT17"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT18", to_date(col("MA_CLAIM_OCCUR_DT18"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT19", to_date(col("MA_CLAIM_OCCUR_DT19"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT20", to_date(col("MA_CLAIM_OCCUR_DT20"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT21", to_date(col("MA_CLAIM_OCCUR_DT21"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT22", to_date(col("MA_CLAIM_OCCUR_DT22"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT23", to_date(col("MA_CLAIM_OCCUR_DT23"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_DT24", to_date(col("MA_CLAIM_OCCUR_DT24"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT1", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT1"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT1", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT1"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT2", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT2"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT2", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT2"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT3", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT3"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT3", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT3"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT4", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT4"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT4", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT4"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT5", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT5"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT5", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT5"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT6", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT6"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT6", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT6"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT7", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT7"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT7", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT7"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT8", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT8"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT8", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT8"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT9", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT9"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT9", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT9"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT10", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT10"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT10", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT10"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT11", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT12"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT11", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT11"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT12", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT12"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT12", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT12"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT13", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT13"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT13", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT13"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT14", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT14"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT14", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT14"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT15", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT15"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT15", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT15"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT16", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT16"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT16", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT16"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT17", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT17"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT17", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT17"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT18", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT18"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT18", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT18"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT19", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT19"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT19", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT19"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT20", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT20"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT20", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT20"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT21", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT21"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT21", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT21"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT22", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT22"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT22", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT22"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT23", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT23"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT23", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT23"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT24", to_date(col("MA_CLAIM_OCCUR_SPAN_FROM_DT24"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT24", to_date(col("MA_CLAIM_OCCUR_SPAN_TO_DT24"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_PRIM_PROC_DT", to_date(col("MA_CLAIM_PRIM_PROC_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_2", to_date(col("MA_CLAIM_OTHER_PROC_DT_2"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_3", to_date(col("MA_CLAIM_OTHER_PROC_DT_3"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_4", to_date(col("MA_CLAIM_OTHER_PROC_DT_4"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_5", to_date(col("MA_CLAIM_OTHER_PROC_DT_5"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_6", to_date(col("MA_CLAIM_OTHER_PROC_DT_6"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_7", to_date(col("MA_CLAIM_OTHER_PROC_DT_7"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_8", to_date(col("MA_CLAIM_OTHER_PROC_DT_8"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_9", to_date(col("MA_CLAIM_OTHER_PROC_DT_9"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_10", to_date(col("MA_CLAIM_OTHER_PROC_DT_10"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_11", to_date(col("MA_CLAIM_OTHER_PROC_DT_11"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_12", to_date(col("MA_CLAIM_OTHER_PROC_DT_12"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_13", to_date(col("MA_CLAIM_OTHER_PROC_DT_13"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_14", to_date(col("MA_CLAIM_OTHER_PROC_DT_14"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_15", to_date(col("MA_CLAIM_OTHER_PROC_DT_15"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_16", to_date(col("MA_CLAIM_OTHER_PROC_DT_16"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_17", to_date(col("MA_CLAIM_OTHER_PROC_DT_17"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_18", to_date(col("MA_CLAIM_OTHER_PROC_DT_18"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_19", to_date(col("MA_CLAIM_OTHER_PROC_DT_19"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_20", to_date(col("MA_CLAIM_OTHER_PROC_DT_20"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_21", to_date(col("MA_CLAIM_OTHER_PROC_DT_21"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_22", to_date(col("MA_CLAIM_OTHER_PROC_DT_22"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_23", to_date(col("MA_CLAIM_OTHER_PROC_DT_23"), "MM/dd/yyyy")) \
        .withColumn("MA_CLAIM_OTHER_PROC_DT_24", to_date(col("MA_CLAIM_OTHER_PROC_DT_24"), "MM/dd/yyyy")) \
        .withColumn("MA_ITS_CLM_RF_POST_DT", to_date(col("MA_ITS_CLM_RF_POST_DT"), "MM/dd/yyyy"))  \
        .withColumn("MA_CLM_BACKOUT_DT", to_date(col("MA_CLM_BACKOUT_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_LINE_SERVICE_FROM_DT", to_date(col("MA_LINE_SERVICE_FROM_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_LINE_SERVICE_TO_DT", to_date(col("MA_LINE_SERVICE_TO_DT"), "MM/dd/yyyy")) \
        .withColumn("MA_LINE_GL_DT", to_date(col("MA_LINE_GL_DT"), "MM/dd/yyyy"))
    
    return dfNew

# COMMAND ----------

# DBTITLE 1,Method: deLinkClaims Mark DupDeniedClaims
def deLinkClaims(df):
    dfDeLink = df.alias("df1") \
        .withColumn("IS_DENIED_DUPLICATE", when(
            ((col("MA_CLAIM_STATUS") == "8") | ((col("MA_CLAIM_STATUS") == "O") & (col("MA_CLAIM_STATUS_PREV") == "8"))) & 
            ((col("MA_LINE_EVENT_CD1") == "502") | (col("MA_LINE_EVENT_CD1") == "505") | (col("MA_LINE_EVENT_CD1") == "611") | 
             (col("MA_LINE_EVENT_CD2") == "502") | (col("MA_LINE_EVENT_CD2") == "505") | (col("MA_LINE_EVENT_CD2") == "611") | 
             (col("MA_LINE_EVENT_CD3") == "502") | (col("MA_LINE_EVENT_CD3") == "505") | (col("MA_LINE_EVENT_CD3") == "611") | 
             (col("MA_LINE_EVENT_CD4") == "502") | (col("MA_LINE_EVENT_CD4") == "505") | (col("MA_LINE_EVENT_CD4") == "611") | 
             (col("MA_LINE_EVENT_CD5") == "502") | (col("MA_LINE_EVENT_CD5") == "505") | (col("MA_LINE_EVENT_CD5") == "611") | 
             (col("MA_LINE_EVENT_CD6") == "502") | (col("MA_LINE_EVENT_CD6") == "505") | (col("MA_LINE_EVENT_CD6") == "611") | 
             (col("MA_LINE_EVENT_CD7") == "502") | (col("MA_LINE_EVENT_CD7") == "505") | (col("MA_LINE_EVENT_CD7") == "611") | 
             (col("MA_LINE_EVENT_CD8") == "502") | (col("MA_LINE_EVENT_CD8") == "505") | (col("MA_LINE_EVENT_CD8") == "611") | 
             (col("MA_LINE_EVENT_CD9") == "502") | (col("MA_LINE_EVENT_CD9") == "505") | (col("MA_LINE_EVENT_CD9") == "611") | 
             (col("MA_LINE_EVENT_CD10") == "502") | (col("MA_LINE_EVENT_CD10") == "505") | (col("MA_LINE_EVENT_CD10") == "611") | 
             (col("MA_LINE_EVENT_CD11") == "502") | (col("MA_LINE_EVENT_CD11") == "505") | (col("MA_LINE_EVENT_CD11") == "611") | 
             (col("MA_LINE_EVENT_CD12") == "502") | (col("MA_LINE_EVENT_CD12") == "505") | (col("MA_LINE_EVENT_CD12") == "611") | 
             (col("MA_LINE_EVENT_CD13") == "502") | (col("MA_LINE_EVENT_CD13") == "505") | (col("MA_LINE_EVENT_CD13") == "611") | 
             (col("MA_LINE_EVENT_CD14") == "502") | (col("MA_LINE_EVENT_CD14") == "505") | (col("MA_LINE_EVENT_CD14") == "611")) & 
            (col("IS_SPLIT_CLAIM") != 1), 1).otherwise(0)) \
        .select("df1.*", "IS_DENIED_DUPLICATE")

    # Unlink
    dfDeLink = dfDeLink.withColumn("MA_CLAIM_ID_ORIG", when(col("IS_DENIED_DUPLICATE") == 1, col("MA_CLAIM_NUM")).otherwise(col("MA_CLAIM_ID_ORIG")))
    
    return dfDeLink

# COMMAND ----------

# DBTITLE 1,Get JobID
# Get Job ID - Serverless compatible version
ErrorMessage = ""
doubleQuote = '"'

try:
    # Try to get job ID - works on classic clusters
    ctx = dbutils.notebook.entry_point.getDbutils().notebook().getContext()
    currentJobId = ctx.tags().get("jobId").getOrElse(lambda: "Undefined")
except Exception:
    # Serverless fallback - ctx.tags() is not whitelisted on Serverless
    currentJobId = "Undefined"

# COMMAND ----------

# DBTITLE 1,File Structure Check, Create DataFrame, Write to Processed
def process_fcf_claims(ClientId, FileId, FileLayoutId, FileLayoutDescription, 
                       ColumnDelimiter, HasHeader, IgnoreHeader, textQualifier,
                       FullFileName, SchemaFile, ProcessedPath):
    """
    Main FCF claims processing function that can be called directly.
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
        dfFile = createDF(FullFileName, SchemaFile, ColumnDelimiter)
        
        if len(dfFile.take(1)) > 0:
            dfFile = deLinkClaims(dfFile)
            dfFile = dfFile \
                .withColumn("GENERATED_CLAIMS_UNIQUE_KEY", concat(col("MA_LINE_CLAIM_NUM"), lit("-"), col("FILE_ID"), lit("-"), col("CLIENT_ID"))) \
                .withColumn("GENERATED_GOLDEN_CLAIMS_UNIQUE_KEY", concat(col("MA_CLAIM_ID_ORIG"), lit("-"), col("FILE_LAYOUT_ID"), lit("-"), col("CLIENT_ID"))) \
                .withColumn("LOAD_DATETIME", to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss")) \
                .withColumn("PARTITION_KEY", year(to_date(col("MA_LINE_SERVICE_FROM_DT"), "MM/dd/yyyy")))

            dfFile.write \
                .format("parquet") \
                .mode("append") \
                .partitionBy("PARTITION_KEY") \
                .save(ProcessedPath)
            
            rJSON.addNewEntry("Status", "SUCCESS")
            rJSON.addNewEntry("ProcessedCount", str(dfFile.count()))
            rJSON.addNewEntry("ErrorMessage", "", newLine=False) 

    except Exception as e:
        # Clean error message: remove quotes, newlines, and control characters that break JSON
        clean_err = str(e).strip().replace(doubleQuote, "").replace("\n", " ").replace("\r", " ").replace("\t", " ")
        rJSON.addNewEntry("Status", "FAILED")
        rJSON.addNewEntry("ProcessedCount", "0")
        rJSON.addNewEntry("ErrorMessage", clean_err, newLine=False) 

    rJSON.addBraceEnd()
    return rJSON.getJSON()

# COMMAND ----------

# DBTITLE 0,Main Processing Function
# When run as a standalone notebook, call the function with widget parameters
# When loaded via %run, this cell is skipped (function is already in scope)
if __name__ == '__main__':
    returnVal = process_fcf_claims(
        ClientId=ClientId,
        FileId=FileId,
        FileLayoutId=FileLayoutId,
        FileLayoutDescription=FileLayoutDescription,
        ColumnDelimiter=ColumnDelimiter,
        HasHeader=HasHeader,
        IgnoreHeader=IgnoreHeader,
        textQualifier=textQualifier,
        FullFileName=FullFileName,
        SchemaFile=SchemaFile,
        ProcessedPath=ProcessedPath
    )
    print(returnVal)
