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
val textQualifier = dbutils.widgets.get("TextQualifier")

val FullFileName = dbutils.widgets.get("FullFileName") 
val SchemaFile = dbutils.widgets.get("SchemaFile")
val ProcessedPath = dbutils.widgets.get("ProcessedPath")


// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass -  FIX BEFORE CHECK IN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Call FileHandling Notebook
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Get JobID
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //"1234" //

// COMMAND ----------

// DBTITLE 1,Copy Dataframe to Parquet Format and add FileID
var rJSON = new synJSONCreator

var ErrorMessage = "";

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

var dfFile: DataFrame = sqlContext.emptyDataFrame

try{
    if (IgnoreHeader=="False")
      {
        dfFile = delimitedFile(FullFileName, SchemaFile, HasHeader, ColumnDelimiter, textQualifier)
      }
    else if (IgnoreHeader=="True" && HasHeader=="True")
      {
        dfFile = isIgnoreHeader(FullFileName, SchemaFile, ColumnDelimiter, textQualifier)
      }

    if (dfFile.rdd.isEmpty == false) {
      dfFile = dfFile.select(dfFile.columns.filter(x => (!x.startsWith("Filler_"))).map(dfFile(_)) : _*)
      //Add file based columns to df
      dfFile = dfFile.withColumn("FILE_ID",lit(FileId))
            .withColumn("FILE_LAYOUT_ID",lit(FileLayoutId))
            .withColumn("FILE_LAYOUT_DESCRIPTION",lit(FileLayoutDescription))
            .withColumn("CLIENT_ID",lit(ClientId))
            .withColumn("LOAD_DATETIME",to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))

    //write dataframe to processed path
      dfFile.write.format("parquet").mode("append").save(ProcessedPath)

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
