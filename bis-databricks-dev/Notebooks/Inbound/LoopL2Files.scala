// Databricks notebook source
// DBTITLE 1,Create and setup parameter
dbutils.widgets.text("SchemaValidationJSON","","")

val schemaValidationJSON = dbutils.widgets.get("SchemaValidationJSON")

// COMMAND ----------

// DBTITLE 1,Call libraries
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

val fileID = spark.read.json(Seq(schemaValidationJSON).toDS)
val explodedFileIDs = fileID.select(explode($"FileIds")).select(
              $"col.FileID"
             ,$"col.FileName"
             ,$"col.RegistrationDatetime"
             ,$"col.FullCurrentPath"
             ,$"col.CurrentContainer"
             ,$"col.CurrentFolderPath"
             ,$"col.ValidatedContainer"
             ,$"col.ValidatedFolderPath"
             ,$"col.FullValidatedPath"
             ,$"col.ValidationFileContainer"
             ,$"col.ValidationFileFolderPath"
             ,$"col.ValidationFileName"
             ,$"col.ColumnDelimiter"
             ,$"col.ConversionType"
             ,$"col.HasHeaders"
             ,$"col.IgnoreHeader"
             ,$"col.TextQualifier"
              )

// COMMAND ----------

case class FileReferences(
         FileID: String 
        ,FileName: String 
        ,RegistrationDatetime: String
        ,FullCurrentPath: String 
        ,CurrentContainer: String 
        ,CurrentFolderPath: String 
        ,ValidatedContainer: String 
        ,ValidatedFolderPath: String 
        ,FullValidatedPath: String
        ,ValidationFileContainer: String
        ,ValidationFileFolderPath: String 
        ,ValidationFileName: String
        ,ColumnDelimiter: String 
        ,ConversionType: String 
        ,HasHeaders: String 
        ,IgnoreHeader: String 
        ,TextQualifier: String
)

case class ReturnedData(
         CurrentJobId: String 
        ,RecordCount: String       
        ,ErrorCount: String 
        ,ErrorPathSchema: String
        ,Status: String 
        ,ErrorMessage: String 
)

val doubleQuote = """ " """.trim()
var rJSON ="["

var iterator = 0;

explodedFileIDs.as[FileReferences].take(explodedFileIDs.count.toInt).foreach(t =>
          {          
            var results = ""
            var fileName = t.FileName
            if(t.ConversionType == "837"){
             fileName = t.FileName.substring(0, t.FileName.lastIndexOf('.')).concat(".csv") 
            }
            try {
                 results = 
                  dbutils.notebook.run(
                                                  "Level2Validations"
                                                 , 0
                                                 ,Map(
                                                      "FileID" -> t.FileID
                                                     ,"FileName" -> fileName
                                                     ,"CurrentContainer" -> t.CurrentContainer
                                                     ,"CurrentFolderPath" -> t.CurrentFolderPath
                                                     ,"ValidationContainer" -> t.ValidationFileContainer
                                                     ,"ValidationFileFolderPath" -> t.ValidationFileFolderPath
                                                     ,"ValidationFileName" -> t.ValidationFileName
                                                     ,"ValidatedFolderPath" -> t.FullValidatedPath
                                                     ,"HasHeaders" -> t.HasHeaders
                                                     ,"IgnoreHeader" -> t.IgnoreHeader
                                                     ,"Delimiter" -> t.ColumnDelimiter
                                                     ,"TextQualifier" -> t.TextQualifier
                                                 )         
                                         )
              
              }
              catch {
                case e: com.databricks.WorkflowException =>  
                    results = e.getMessage.toString
              }
             
             if(iterator == 0){
               rJSON += "{" 
             }else{
               rJSON += ",{" 
             }

             rJSON += doubleQuote + "FileID" + doubleQuote  + ":"  + doubleQuote + t.FileID + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "FullCurrentPath" + doubleQuote  + ":"  + doubleQuote + t.FullCurrentPath  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "FileName" + doubleQuote  + ":"  + doubleQuote + t.FileName  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "CurrentContainer" + doubleQuote  + ":"  + doubleQuote + t.CurrentContainer  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "CurrentFolderPath" + doubleQuote  + ":"  + doubleQuote + t.CurrentFolderPath  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "ValidatedContainer" + doubleQuote  + ":"  + doubleQuote + t.ValidatedContainer  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "ValidatedFolderPath" + doubleQuote  + ":"  + doubleQuote + t.ValidatedFolderPath  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "FullValidatedPath" + doubleQuote  + ":"  + doubleQuote + t.FullValidatedPath  + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "ConversionType" + doubleQuote  + ":"  + doubleQuote + t.ConversionType  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "RegistrationDatetime" + doubleQuote  + ":"  + doubleQuote + t.RegistrationDatetime  + doubleQuote
             rJSON += ","        

             //read output into a json table
             val returnedData = spark.read.json(Seq(results.toString).toDS)             
             
             returnedData.as[ReturnedData].take(returnedData.count.toInt).foreach(x =>
                      {
                             rJSON += doubleQuote + "CurrentJobId" + doubleQuote  + ":"  + doubleQuote  + x.CurrentJobId + doubleQuote
                             rJSON += ","
                             rJSON += doubleQuote + "RecordCount" + doubleQuote  + ":"  + doubleQuote  + x.RecordCount + doubleQuote
                             rJSON += ","
                             rJSON += doubleQuote + "ErrorCount" + doubleQuote  + ":"  + doubleQuote  + x.ErrorCount + doubleQuote
                             rJSON += ","
                             rJSON += doubleQuote + "ErrorPathSchema" + doubleQuote  + ":"  + doubleQuote  + x.ErrorPathSchema + doubleQuote
                             rJSON += ","
                             rJSON += doubleQuote + "Status" + doubleQuote  + ":"  +  doubleQuote  + x.Status + doubleQuote
                             rJSON += ","        
                             rJSON += doubleQuote + "ErrorMessage" + doubleQuote  + ":"  + doubleQuote  + x.ErrorMessage + doubleQuote                                     
                      }
                            )
             
             rJSON += "}"
            
             iterator+=1
          }
 )

rJSON+="]"

dbutils.notebook.exit(rJSON)
