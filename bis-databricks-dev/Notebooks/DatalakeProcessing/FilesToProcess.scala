// Databricks notebook source
// DBTITLE 1,Get File List JSON For Processing
dbutils.widgets.text("ProcessedJSON","","")
val ProcessedJSON = dbutils.widgets.get("ProcessedJSON")

// COMMAND ----------

// DBTITLE 1,Notebook Variable Assignment
val fcfNotebook = "../DatalakeProcessing/FCFClaimsProcessing"
val procNotebook = "../DatalakeProcessing/MoveFileToProcess"

// COMMAND ----------

// DBTITLE 1,Import Libraries
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Call FileHandling Notebook For Helper Methods
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Explode List Into Dataframe with Multiple Columns
val filesDF = spark.read.json(Seq(ProcessedJSON).toDS)

val explodedFileIDs = filesDF.select(explode($"FileIds")).select(
              $"col.ClientID"
             ,$"col.FileID"
             ,$"col.FileName"
             ,$"col.ClientContainer"
             ,$"col.CurrentFolderPath"
             ,$"col.ProcessedFolderPath"
             ,$"col.ColumnDelimiter"
             ,$"col.HasHeader"
             ,$"col.IgnoreHeader"
             ,$"col.FileLayoutID"
             ,$"col.FileLayoutDescription"
             ,$"col.SchemaFileName"
             ,$"col.SchemaFilePath"
             ,$"col.TextQualifier"
              )


// COMMAND ----------

// DBTITLE 1,Define Case Classes Used For Processing and Return
case class FileReferences(
         ClientID: String 
        ,FileID: String 
        ,FileName: String
        ,ClientContainer: String 
        ,CurrentFolderPath: String 
        ,ProcessedFolderPath: String 
        ,ColumnDelimiter: String 
        ,HasHeader: String 
        ,IgnoreHeader: String 
        ,FileLayoutID: String 
        ,FileLayoutDescription: String 
        ,SchemaFileName: String 
        ,SchemaFilePath: String 
        ,TextQualifier: String 
)

case class ReturnedData(
         CurrentJobId: String  
        ,Status: String 
        ,ProcessedCount: String
        ,ErrorMessage: String 
)

// COMMAND ----------

// DBTITLE 1,Get JobID
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //"1234" //

// COMMAND ----------

// DBTITLE 1,Loop Through FileIDs to Process
var rJSON = new synJSONCreator

rJSON.addBracketStart()

var iterator = 0;

explodedFileIDs.as[FileReferences].take(explodedFileIDs.count.toInt).foreach(t =>  {
println(s"Begin ${t.FileID}-${t.FileName}")
            var notebook = ""
            val mnt = "/mnt/"
            val CurrPath = s"${t.ClientContainer}${t.CurrentFolderPath}"
            val ProcessedPath = s"${mnt}${t.ClientContainer}${t.ProcessedFolderPath}"
            val SchemaFile = s"${mnt}${t.SchemaFilePath}/${t.SchemaFileName}"
            val FullFileName = s"${mnt}${t.ClientContainer}${t.CurrentFolderPath}/${t.FileName}"

            val f = path_exists(FullFileName)
            val s = path_exists(SchemaFile)

            if(f == true && s == true) 
            {
              if (iterator != 0) {rJSON.addComma()}  //Add comma if not the first record
              
              if (t.FileLayoutDescription == "FCF")
                {notebook = fcfNotebook}
              else
                {notebook = procNotebook}

              rJSON.addBraceStart()
              rJSON.addNewEntry("FileID", t.FileID)
              rJSON.addNewEntry("FileName", t.FileName)
            
              try { 
                  val results = dbutils.notebook.run(notebook,0,Map("ClientID"->t.ClientID
                                                      ,"FileID"->t.FileID
                                                      ,"FileLayoutID"->t.FileLayoutID
                                                      ,"FileLayoutDescription"->t.FileLayoutDescription
                                                      ,"ColumnDelimiter"->t.ColumnDelimiter
                                                      ,"HasHeader"->t.HasHeader
                                                      ,"IgnoreHeader"->t.IgnoreHeader
                                                      ,"FullFileName"->FullFileName
                                                      ,"SchemaFile"->SchemaFile
                                                      ,"ProcessedPath"->ProcessedPath
                                                      ,"TextQualifier"->t.TextQualifier)
                                                      )
          
                 //read output into a json table
                 val returnedJson = spark.read.json(Seq(results.toString).toDS)

                 returnedJson.as[ReturnedData].take(returnedJson.count.toInt).foreach(x =>
                          {
                                 rJSON.addNewEntry("FullFilePath", s"${t.ClientContainer}${t.ProcessedFolderPath}")
                                 rJSON.addNewEntry("CurrentJobId", x.CurrentJobId)
                                 rJSON.addNewEntry("Status", x.Status) 
                                 rJSON.addNewEntry("RecordCount", x.ProcessedCount)     
                                 rJSON.addNewEntry("ErrorMessage",x.ErrorMessage, false)                                    
                          }
                 )
               }
               catch{ case e: Exception =>  {
                               rJSON.addNewEntry("CurrentJobId", "Undefined")
                               rJSON.addNewEntry("Status", "FAILURE")
                               rJSON.addNewEntry("RecordCount", "")   
                               rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false) 
                   }  
               }
  
          rJSON.addBraceEnd()
            }
  
          else if(f == false)
          {
            if (iterator != 0) {rJSON.addComma()}
            rJSON.addBraceStart()
            rJSON.addNewEntry("CurrentJobId", "Undefined")
            rJSON.addNewEntry("FileID", t.FileID)
            rJSON.addNewEntry("FileName", t.FileName)
            rJSON.addNewEntry("FullFilePath", CurrPath)
            rJSON.addNewEntry("Status", "FAILED")
            rJSON.addNewEntry("RecordCount", "")   
            rJSON.addNewEntry("ErrorMessage", "Data File Not Found", false)
            rJSON.addBraceEnd()
          }
          else if(s == false)
          {
            if (iterator != 0) {rJSON.addComma()}
            rJSON.addBraceStart()
            rJSON.addNewEntry("CurrentJobId", "Undefined")
            rJSON.addNewEntry("FileID", t.FileID)
            rJSON.addNewEntry("FileName", t.SchemaFileName)
            rJSON.addNewEntry("FullFilePath", CurrPath)
            rJSON.addNewEntry("Status", "FAILED")
            rJSON.addNewEntry("RecordCount", "")   
            rJSON.addNewEntry("ErrorMessage", "Schema File Not Found", false)
            rJSON.addBraceEnd()
          }
          iterator+=1
    }
)

rJSON.addBracketEnd()

val returnVal = rJSON.getJSON()
println(returnVal)
dbutils.notebook.exit(returnVal)
