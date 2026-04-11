// Databricks notebook source
dbutils.widgets.text("lookupFilesJson","","")

val lookupFilesJson = dbutils.widgets.get("lookupFilesJson")

// COMMAND ----------

import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

val FileID = spark.read.json(Seq(lookupFilesJson).toDS)

val explodedFileIDs = FileID.select(explode($"FileIds")).select(
              $"col.FileID"
             ,$"col.FileLayoutDescription"
             ,$"col.CurrentContainer"
             ,$"col.CurrentFolderPath"
             ,$"col.FileName"
             ,$"col.ConversionType"
             ,$"col.ColumnDelimiter"
             ,$"col.ConversionFileContainer"
             ,$"col.ConversionFileFolderPath"
             ,$"col.ConversionFileName"
             ,$"col.HasControlFile" 
             ,$"col.RegistrationDatetime" 
             ,$"col.FullValidatedPath" 
              )


// COMMAND ----------

case class FileConversionType(
         fileId: String 
        ,FileLayoutDescription: String 
        ,currentContainer: String 
        ,currentFolderPath: String
        ,fileName: String 
        ,conversionType: String 
        ,columnDelimiter: String        
        ,conversionFileContainer: String 
        ,conversionFileFolderPath: String 
        ,conversionFileName: String 
        ,hasControlFile: String  
        ,registrationDatetime: String 
        ,fullValidatedPath: String 
)

case class returnedData(
         RecordCount: String         
)

val doubleQuote = """ " """.trim()
var rJSON ="["

var iterator = 0;

explodedFileIDs.as[FileConversionType].take(explodedFileIDs.count.toInt).foreach(t =>
          {          
            var results = ""
            var isSuccess = true  
            if(iterator == 0){
               rJSON += "{" 
             }else{
               rJSON += ",{" 
             }   
            
             rJSON += doubleQuote + "FileID" + doubleQuote  + ":"  + doubleQuote + t.fileId + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "FileLayoutDescription" + doubleQuote  + ":"  + doubleQuote + t.FileLayoutDescription + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "CurrentContainer" + doubleQuote  + ":"  + doubleQuote + t.currentContainer  + doubleQuote
             rJSON += ","             
             rJSON += doubleQuote + "CurrentFolderPath" + doubleQuote  + ":"  + doubleQuote + t.currentFolderPath  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "FileName" + doubleQuote  + ":"  + doubleQuote + t.fileName  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "ConversionType" + doubleQuote  + ":"  + doubleQuote + t.conversionType  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "RegistrationDatetime" + doubleQuote  + ":"  + doubleQuote + t.registrationDatetime  + doubleQuote
             rJSON += ","  
             rJSON += doubleQuote + "FullValidatedPath" + doubleQuote  + ":"  + doubleQuote + t.fullValidatedPath  + doubleQuote
             rJSON += ","            

            try {               
                  results = dbutils.notebook.run("CSVConversion", 0,Map("FileId"->t.fileId
                                        ,"FileLayoutDescription"->t.FileLayoutDescription
                                        ,"CurrentContainer"->t.currentContainer
                                        ,"CurrentFolderPath"->t.currentFolderPath
                                        ,"ConversionType"->t.conversionType
                                        ,"FileName"->t.fileName 
                                        ,"Delimiter"->t.columnDelimiter                                        
                                        ,"ConversionJsonContainer"->t.conversionFileContainer
                                        ,"ConversionJsonFolderPath"->t.conversionFileFolderPath
                                        ,"ConversionJsonFileName"->t.conversionFileName
                                        ,"HasControlFile"->t.hasControlFile)) 
              
                 //read output into a json table
                 val returnedData = spark.read.json(Seq(results.toString).toDS) 
               
                 returnedData.as[returnedData].take(returnedData.count.toInt).foreach(x =>
                            {                             
                                if(x.RecordCount.trim() == "0"){ //throwing exception for files where the dataframe was not written
                                  throw new Exception("Record count of the dataframe is 0. File was not written") 
                                }
                                else{
                                rJSON += doubleQuote + "ConvertedCount" + doubleQuote  + ":"  + doubleQuote  + x.RecordCount + doubleQuote
                                rJSON += "," 
                                }
                            }
                          )                        
                }
              catch {
                  case e: com.databricks.WorkflowException =>  
                    isSuccess = false
                    rJSON += doubleQuote + "ConvertedCount" + doubleQuote  + ":"  + doubleQuote  + 0 + doubleQuote  
                    rJSON += "," 
                 case _: Throwable =>
                    isSuccess = false
                    rJSON += doubleQuote + "ConvertedCount" + doubleQuote  + ":"  + doubleQuote  + 0 + doubleQuote  
                    rJSON += "," 
              }
            
             
             rJSON += doubleQuote + "IsConversionSucceed" + doubleQuote  + ":"  + doubleQuote + isSuccess  + doubleQuote
            
             
             rJSON += "}"
            
             iterator+=1
          }
 )

rJSON+="]"

dbutils.notebook.exit(rJSON)
