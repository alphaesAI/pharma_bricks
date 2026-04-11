// Databricks notebook source
dbutils.widgets.text("ConsolidationJSON","","")

val ConsolidationJSON = dbutils.widgets.get("ConsolidationJSON")

// COMMAND ----------

import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

val FileID = spark.read.json(Seq(ConsolidationJSON).toDS)
val explodedFileIDs = FileID.select(explode($"FileIds")).select(
              $"col.DataGroupTrackingID"
             ,$"col.DataGroupMappingId"
             ,$"col.FileId"
             ,$"col.FileLayoutID"
             ,$"col.FileLayoutDescription"
             ,$"col.CurrentContainer"
             ,$"col.CurrentFolderPath"
             ,$"col.ConsolidatedMappingFilePath"
             ,$"col.ConsolidatedMappingFileName"
             ,$"col.ConsolidatedLayerDataModelFilePath"
             ,$"col.ConsolidatedLayerDataModel"
             ,$"col.ConsolidatedFolderPath"
              )

// COMMAND ----------

case class FileReferences(
         DataGroupTrackingID: String 
        ,DataGroupMappingId: String 
        ,FileId: String
        ,FileLayoutID: String 
        ,FileLayoutDescription: String 
        ,CurrentContainer: String 
        ,CurrentFolderPath: String 
        ,ConsolidatedMappingFilePath: String 
        ,ConsolidatedMappingFileName: String 
        ,ConsolidatedLayerDataModelFilePath: String 
        ,ConsolidatedLayerDataModel: String 
        ,ConsolidatedFolderPath: String 
)

case class returnedData(
         CurrentJobId: String 
        ,ConsolidatedCount: String 
        ,Status: String 
        ,ErrorMessage: String 
)

val doubleQuote = """ " """.trim()
var rJSON ="["

var iterator = 0;

explodedFileIDs.as[FileReferences].take(explodedFileIDs.count.toInt).foreach(t =>
          {          
            var results = ""
            
            try {   
               results = 
                  dbutils.notebook.run(
                                                  "MoveFileToConsolidation"
                                                 , 0
                                                 ,Map(
                                                      "FileId" -> t.FileId
                                                     ,"CurrentContainer" -> t.CurrentContainer
                                                     ,"CurrentFolderPath" -> t.CurrentFolderPath
                                                     ,"ConsolidatedLayerDataModel" -> t.ConsolidatedLayerDataModel
                                                     ,"ConsolidatedLayerDataModelFilePath" -> t.ConsolidatedLayerDataModelFilePath
                                                     ,"ConsolidatedMappingFileName" -> t.ConsolidatedMappingFileName
                                                     ,"ConsolidatedMappingFilePath" -> t.ConsolidatedMappingFilePath
                                                     ,"ConsolidatedFolderPath" -> t.ConsolidatedFolderPath 
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

             rJSON += doubleQuote + "FileID" + doubleQuote  + ":"  + doubleQuote + t.FileId + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "DataGroupTrackingID" + doubleQuote  + ":"  + doubleQuote + t.DataGroupTrackingID  + doubleQuote
             rJSON += "," 
             rJSON += doubleQuote + "DataGroupMappingId" + doubleQuote  + ":"  + doubleQuote + t.DataGroupMappingId  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "CurrentContainer" + doubleQuote  + ":"  + doubleQuote + t.CurrentContainer  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "CurrentFolderPath" + doubleQuote  + ":"  + doubleQuote + t.CurrentFolderPath  + doubleQuote
             rJSON += ","
             rJSON += doubleQuote + "ConsolidatedFolderPath" + doubleQuote  + ":"  + doubleQuote + t.ConsolidatedFolderPath  + doubleQuote
             rJSON += ","

             //read output into a json table
             val returnedData = spark.read.json(Seq(results.toString).toDS) 
                  //returnedData.createOrReplaceTempView("DeltaTable")
                  //returnedData.printSchema
             
             returnedData.as[returnedData].take(returnedData.count.toInt).foreach(x =>
                      {
                             rJSON += doubleQuote + "CurrentJobId" + doubleQuote  + ":"  + doubleQuote  + x.CurrentJobId + doubleQuote
                             rJSON += ","
                             rJSON += doubleQuote + "ConsolidatedCount" + doubleQuote  + ":"  + doubleQuote  + x.ConsolidatedCount + doubleQuote
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
