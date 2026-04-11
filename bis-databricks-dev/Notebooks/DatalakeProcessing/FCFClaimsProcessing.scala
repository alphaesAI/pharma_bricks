// Databricks notebook source
// DBTITLE 1,Create and setup parameters
//File Parameters
dbutils.widgets.text("ClientID","","") //"|"
dbutils.widgets.text("FileID","","") //0 
dbutils.widgets.text("FileLayoutID","","") //"|"
dbutils.widgets.text("FileLayoutDescription","","") //"|"
dbutils.widgets.text("ColumnDelimiter","","") //"|"
dbutils.widgets.text("HasHeader","","") //"|"
dbutils.widgets.text("IgnoreHeader","","") //"true"
dbutils.widgets.text("TextQualifier","","") //"true"

//File to be Processed
dbutils.widgets.text("FullFileName","","")  

//Schema File
dbutils.widgets.text("SchemaFile","","")  

//Processed File 
dbutils.widgets.text("ProcessedPath","","") 

val ClientId = dbutils.widgets.get("ClientID")
val FileId = dbutils.widgets.get("FileID")  
val FileLayoutId = dbutils.widgets.get("FileLayoutID")
val FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
val ColumnDelimiter = dbutils.widgets.get("ColumnDelimiter")
val HasHeader = dbutils.widgets.get("HasHeader").toString.capitalize
val IgnoreHeader = dbutils.widgets.get("IgnoreHeader").toString.capitalize
val textQualifier = dbutils.widgets.get("TextQualifier") //will not be used

val FullFileName = dbutils.widgets.get("FullFileName") 
val SchemaFile = dbutils.widgets.get("SchemaFile")
val ProcessedPath = dbutils.widgets.get("ProcessedPath")

// COMMAND ----------

// DBTITLE 1,Call libraries
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame

// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Method: createDF - Dataframe Creation
def createDF(file: String, validation: String, delimiter: String): DataFrame = {
  
  val fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  val parsedSchema = fullSchema.select( explode($"columnNames")).select($"col.FieldName",$"col.DataType").filter($"col.FieldName" =!= "TEMPLATE")
  val header = parsedSchema.select("FieldName").map(x=>x.getString(0).trim()).collect()
  val fields = header.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
  val schema = StructType(fields)
  
  var dfNew = spark.read.format("csv")
      .schema(schema)
      .option("header", HasHeader)
      .option("delimiter", delimiter)
      .load(file)
  
  //TRIM WHITE SPACES
  dfNew = dfNew.columns.foldLeft(dfNew){(DF, colName) => DF.withColumn(colName, trim(col(colName)))} 
  
  //ADD NEW COLUMS
   dfNew = dfNew.withColumn("FILE_ID",lit(FileId))
      .withColumn("FILE_LAYOUT_ID",lit(FileLayoutId))
      .withColumn("FILE_LAYOUT_DESCRIPTION",lit(FileLayoutDescription))
      .withColumn("CLIENT_ID",lit(ClientId))
      .withColumn("IS_SPLIT_CLAIM", when(col("MA_SPLIT_CLAIM_ID").isNull or trim(col("MA_SPLIT_CLAIM_ID")) === "" ,0).otherwise(1))
      .withColumn("CLAIM_WEIGHT", (when(col("MA_CLAIM_STATUS") === "6", 7).when(upper(col("MA_CLAIM_STATUS")) === "C", 7).when(col("MA_CLAIM_STATUS") === "8", 5).when(col("MA_CLAIM_STATUS") === "O" or col("MA_CLAIM_STATUS") === "o", 1) + ((unix_timestamp(col("MA_CLAIM_UPDATED_DT"), "MM/dd/yyyy HH:mm:ss")-unix_timestamp(lit("01/01/2016 00:00:00"),"MM/dd/yyyy HH:mm:ss"))*10)))
      .withColumn("MA_CLAIM_ID_ORIG", when(col("IS_SPLIT_CLAIM") === 1,col("MA_CLAIM_NUM")).otherwise(col("MA_CLAIM_ID_ORIG")))  //unlink for split claim
      .withColumn("MA_PATIENT_DOB", to_date($"MA_PATIENT_DOB", "MM/dd/yyyy"))
      .withColumn("MA_BEGINNING_DOS", to_date($"MA_BEGINNING_DOS", "MM/dd/yyyy"))
      .withColumn("MA_CHECK_DATE", to_date($"MA_CHECK_DATE", "MM/dd/yyyy"))
      .withColumn("MA_FINALIZED_FILE_CREATE_DATE", to_date($"MA_FINALIZED_FILE_CREATE_DATE", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_RECEIVE_DATE", to_date($"MA_CLAIM_RECEIVE_DATE", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_FINALIZED_DT", to_date($"MA_CLAIM_FINALIZED_DT", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_ENTRY_DT", to_timestamp($"MA_CLAIM_ENTRY_DT", "MM/dd/yyyy HH:mm:ss"))   
      .withColumn("MA_CLAIM_UPDATED_DT",to_timestamp($"MA_CLAIM_UPDATED_DT", "MM/dd/yyyy HH:mm:ss"))
      .withColumn("MA_SUBCRIBER_BIRTH_DATE", to_date($"MA_SUBCRIBER_BIRTH_DATE", "MM/dd/yyyy"))  
      .withColumn("MA_BENEFIT_PERIOD_BEGIN_DT", to_date($"MA_BENEFIT_PERIOD_BEGIN_DT", "MM/dd/yyyy"))  
      .withColumn("MA_BENEFIT_PERIOD_END_DT", to_date($"MA_BENEFIT_PERIOD_END_DT", "MM/dd/yyyy"))  
      .withColumn("MA_PATIENT_CURRENT_ILLNESS_DT", to_date($"MA_PATIENT_CURRENT_ILLNESS_DT", "MM/dd/yyyy"))  
      .withColumn("MA_PATIENT_SIMILAR_ILLNESS_DT", to_date($"MA_PATIENT_SIMILAR_ILLNESS_DT", "MM/dd/yyyy"))  
      .withColumn("MA_PATIENT_LAST_WORKED_DT", to_date($"MA_PATIENT_LAST_WORKED_DT", "MM/dd/yyyy"))   
      .withColumn("MA_PATIENT_RETURN_WORK_DT", to_date($"MA_PATIENT_RETURN_WORK_DT", "MM/dd/yyyy"))   
      .withColumn("MA_CLAIM_HOSP_ADMIT_DT", to_date($"MA_CLAIM_HOSP_ADMIT_DT", "MM/dd/yyyy"))   
      .withColumn("MA_CLAIM_HOSP_DISCHARGE_DT", to_date($"MA_CLAIM_HOSP_DISCHARGE_DT", "MM/dd/yyyy"))  
      .withColumn("MA_STATEMENT_FROM_DT", to_date($"MA_STATEMENT_FROM_DT", "MM/dd/yyyy"))   
      .withColumn("MA_STATEMENT_TO_DT", to_date($"MA_STATEMENT_TO_DT", "MM/dd/yyyy")) 
      .withColumn("MA_CLAIM_OCCUR_DT1", to_date($"MA_CLAIM_OCCUR_DT1", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT2", to_date($"MA_CLAIM_OCCUR_DT2", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT3", to_date($"MA_CLAIM_OCCUR_DT3", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT4", to_date($"MA_CLAIM_OCCUR_DT4", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT5", to_date($"MA_CLAIM_OCCUR_DT5", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT6", to_date($"MA_CLAIM_OCCUR_DT6", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT7", to_date($"MA_CLAIM_OCCUR_DT7", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT8", to_date($"MA_CLAIM_OCCUR_DT8", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT9", to_date($"MA_CLAIM_OCCUR_DT9", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT10", to_date($"MA_CLAIM_OCCUR_DT10", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT11", to_date($"MA_CLAIM_OCCUR_DT11", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT12", to_date($"MA_CLAIM_OCCUR_DT12", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT13", to_date($"MA_CLAIM_OCCUR_DT13", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT14", to_date($"MA_CLAIM_OCCUR_DT14", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT15", to_date($"MA_CLAIM_OCCUR_DT15", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT16", to_date($"MA_CLAIM_OCCUR_DT16", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT17", to_date($"MA_CLAIM_OCCUR_DT17", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT18", to_date($"MA_CLAIM_OCCUR_DT18", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT19", to_date($"MA_CLAIM_OCCUR_DT19", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT20", to_date($"MA_CLAIM_OCCUR_DT20", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT21", to_date($"MA_CLAIM_OCCUR_DT21", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT22", to_date($"MA_CLAIM_OCCUR_DT22", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT23", to_date($"MA_CLAIM_OCCUR_DT23", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_DT24", to_date($"MA_CLAIM_OCCUR_DT24", "MM/dd/yyyy"))  
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT1", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT1", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT1", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT1", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT2", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT2", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT2", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT2", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT3", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT3", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT3", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT3", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT4", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT4", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT4", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT4", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT5", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT5", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT5", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT5", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT6", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT6", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT6", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT6", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT7", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT7", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT7", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT7", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT8", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT8", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT8", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT8", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT9", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT9", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT9", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT9", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT10", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT10", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT10", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT10", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT11", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT12", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT11", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT11", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT12", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT12", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT12", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT12", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT13", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT13", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT13", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT13", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT14", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT14", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT14", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT14", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT15", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT15", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT15", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT15", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT16", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT16", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT16", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT16", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT17", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT17", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT17", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT17", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT18", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT18", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT18", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT18", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT19", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT19", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT19", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT19", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT20", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT20", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT20", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT20", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT21", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT21", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT21", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT21", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT22", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT22", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT22", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT22", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT23", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT23", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT23", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT23", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_FROM_DT24", to_date($"MA_CLAIM_OCCUR_SPAN_FROM_DT24", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OCCUR_SPAN_TO_DT24", to_date($"MA_CLAIM_OCCUR_SPAN_TO_DT24", "MM/dd/yyyy"))      
      .withColumn("MA_CLAIM_PRIM_PROC_DT", to_date($"MA_CLAIM_PRIM_PROC_DT", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_2", to_date($"MA_CLAIM_OTHER_PROC_DT_2", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_3", to_date($"MA_CLAIM_OTHER_PROC_DT_3", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_4", to_date($"MA_CLAIM_OTHER_PROC_DT_4", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_5", to_date($"MA_CLAIM_OTHER_PROC_DT_5", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_6", to_date($"MA_CLAIM_OTHER_PROC_DT_6", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_7", to_date($"MA_CLAIM_OTHER_PROC_DT_7", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_8", to_date($"MA_CLAIM_OTHER_PROC_DT_8", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_9", to_date($"MA_CLAIM_OTHER_PROC_DT_9", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_10", to_date($"MA_CLAIM_OTHER_PROC_DT_10", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_11", to_date($"MA_CLAIM_OTHER_PROC_DT_11", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_12", to_date($"MA_CLAIM_OTHER_PROC_DT_12", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_13", to_date($"MA_CLAIM_OTHER_PROC_DT_13", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_14", to_date($"MA_CLAIM_OTHER_PROC_DT_14", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_15", to_date($"MA_CLAIM_OTHER_PROC_DT_15", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_16", to_date($"MA_CLAIM_OTHER_PROC_DT_16", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_17", to_date($"MA_CLAIM_OTHER_PROC_DT_17", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_18", to_date($"MA_CLAIM_OTHER_PROC_DT_18", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_19", to_date($"MA_CLAIM_OTHER_PROC_DT_19", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_20", to_date($"MA_CLAIM_OTHER_PROC_DT_20", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_21", to_date($"MA_CLAIM_OTHER_PROC_DT_21", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_22", to_date($"MA_CLAIM_OTHER_PROC_DT_22", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_23", to_date($"MA_CLAIM_OTHER_PROC_DT_23", "MM/dd/yyyy"))
      .withColumn("MA_CLAIM_OTHER_PROC_DT_24", to_date($"MA_CLAIM_OTHER_PROC_DT_24", "MM/dd/yyyy"))  
      .withColumn("MA_ITS_CLM_RF_POST_DT", to_date($"MA_ITS_CLM_RF_POST_DT", "MM/dd/yyyy"))  
      .withColumn("MA_CLM_BACKOUT_DT", to_date($"MA_CLM_BACKOUT_DT", "MM/dd/yyyy"))
      .withColumn("MA_LINE_SERVICE_FROM_DT", to_date($"MA_LINE_SERVICE_FROM_DT", "MM/dd/yyyy"))
      .withColumn("MA_LINE_SERVICE_TO_DT", to_date($"MA_LINE_SERVICE_TO_DT", "MM/dd/yyyy"))
      .withColumn("MA_LINE_GL_DT", to_date($"MA_LINE_GL_DT", "MM/dd/yyyy"))
  dfNew
}

// COMMAND ----------

// DBTITLE 1,Method: deLinkClaims Mark DupDeniedClaims
def deLinkClaims(df: DataFrame): DataFrame = {
    var dfDeLink = df.as("df1")
           .withColumn("IS_DENIED_DUPLICATE", when((($"MA_CLAIM_STATUS" === "8" or ($"MA_CLAIM_STATUS" === "O" and $"MA_CLAIM_STATUS_PREV" === "8")) and ($"MA_LINE_EVENT_CD1" === "502" or $"MA_LINE_EVENT_CD1" === "505" or $"MA_LINE_EVENT_CD1" ===  "611" or $"MA_LINE_EVENT_CD2" === "502" or $"MA_LINE_EVENT_CD2" ===  "505" or $"MA_LINE_EVENT_CD2" === "611" or $"MA_LINE_EVENT_CD3" === "502" or $"MA_LINE_EVENT_CD3" === "505" or $"MA_LINE_EVENT_CD3" === "611" or $"MA_LINE_EVENT_CD4" === "502" or $"MA_LINE_EVENT_CD4" === "505" or $"MA_LINE_EVENT_CD4" === "611" or $"MA_LINE_EVENT_CD5" === "502"  or $"MA_LINE_EVENT_CD5" === "505"  or $"MA_LINE_EVENT_CD5" === "611" or $"MA_LINE_EVENT_CD6" === "502" or $"MA_LINE_EVENT_CD6" ===  "505" or $"MA_LINE_EVENT_CD6" ===  "611" or $"MA_LINE_EVENT_CD7" === "502" or $"MA_LINE_EVENT_CD7" === "505" or $"MA_LINE_EVENT_CD7" === "611" or $"MA_LINE_EVENT_CD8" === "502" or $"MA_LINE_EVENT_CD8" === "505"or $"MA_LINE_EVENT_CD8" === "611" or $"MA_LINE_EVENT_CD9" === "502" or $"MA_LINE_EVENT_CD9" ===  "505" or $"MA_LINE_EVENT_CD9" === "611" or $"MA_LINE_EVENT_CD10" === "502" or $"MA_LINE_EVENT_CD10" === "505" or $"MA_LINE_EVENT_CD10" === "611" or $"MA_LINE_EVENT_CD11" === "502" or $"MA_LINE_EVENT_CD11" === "505" or $"MA_LINE_EVENT_CD11" === "611"  or $"MA_LINE_EVENT_CD12" === "502" or $"MA_LINE_EVENT_CD12" === "505" or $"MA_LINE_EVENT_CD12" === "611" or $"MA_LINE_EVENT_CD13" === "502" or $"MA_LINE_EVENT_CD13" === "505" or $"MA_LINE_EVENT_CD13" === "611" or $"MA_LINE_EVENT_CD14" === "502" or $"MA_LINE_EVENT_CD14" === "505" or $"MA_LINE_EVENT_CD14" === "611" )) and $"IS_SPLIT_CLAIM" =!= 1,1).otherwise(0)) 
              .select("df1.*","IS_DENIED_DUPLICATE")

    //Unlink
    dfDeLink = dfDeLink.withColumn("MA_CLAIM_ID_ORIG", when($"IS_DENIED_DUPLICATE" === 1,$"MA_CLAIM_NUM").otherwise($"MA_CLAIM_ID_ORIG"))
    
    //Return
    dfDeLink
}

// COMMAND ----------

// DBTITLE 1,Get JobID
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //"1234" //

// COMMAND ----------

// DBTITLE 1,File Structure Check, Create DataFrame, Write to Processed
var rJSON = new synJSONCreator

var ErrorMessage = "";

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

var dfFile: DataFrame = sqlContext.emptyDataFrame

try{
  dfFile = createDF(FullFileName, SchemaFile, ColumnDelimiter)
  
  if (dfFile.rdd.isEmpty == false)
      { 
        dfFile = deLinkClaims(dfFile)
        dfFile = dfFile
            .withColumn("GENERATED_CLAIMS_UNIQUE_KEY",concat(col("MA_LINE_CLAIM_NUM"),lit("-"),col("FILE_ID"),lit("-"),col("CLIENT_ID")))
            .withColumn("GENERATED_GOLDEN_CLAIMS_UNIQUE_KEY",concat(col("MA_CLAIM_ID_ORIG"),lit("-"),col("FILE_LAYOUT_ID"),lit("-"),col("CLIENT_ID")))
            .withColumn("LOAD_DATETIME",to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))
            .withColumn("PARTITION_KEY", year(to_date($"MA_LINE_SERVICE_FROM_DT","MM/dd/yyyy")))

        dfFile.write
            .format("parquet")
            .mode("append")
            .partitionBy("PARTITION_KEY")
            .save(ProcessedPath)
        
      rJSON.addNewEntry("Status", "SUCCESS")
      rJSON.addNewEntry("ProcessedCount", dfFile.count().toString)
      rJSON.addNewEntry("ErrorMessage", "", newLine=false) 
      }
}  
catch{
   case e: Throwable =>  {
       rJSON.addNewEntry("Status", "FAILED")
       rJSON.addNewEntry("ProcessedCount", "0")
       rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), newLine=false) 
    }
}
rJSON.addBraceEnd()

// COMMAND ----------

// DBTITLE 1,Add Processed Records Return
// val recordsProcessed: String = dfFile.count().toString
val returnVal = rJSON.getJSON()
dbutils.notebook.exit(returnVal)
