// Databricks notebook source
// DBTITLE 1,Set Parameters
//Actual File Parameters using widgets
dbutils.widgets.text("FileId","","") //0 
dbutils.widgets.text("CurrentContainer","","") //validate
dbutils.widgets.text("CurrentFolderPath","","") ///MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("FileName","","") //PBC_VIS_FCF_prod_20200227070003.TXT
dbutils.widgets.text("Delimiter","","") //"|"
dbutils.widgets.text("ConversionType","","")
dbutils.widgets.text("ConversionJsonContainer","","")   //fileconfig
dbutils.widgets.text("ConversionJsonFolderPath","","") // /JSON/Conversion
dbutils.widgets.text("ConversionJsonFileName","","") //lishist_conversion.json
dbutils.widgets.text("HasControlFile","","") //lishist_conversion.json

val fileId = dbutils.widgets.get("FileId")    
val currentContainer = dbutils.widgets.get("CurrentContainer") 
val currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
val fileName = dbutils.widgets.get("FileName") 
val Delimiter = dbutils.widgets.get("Delimiter")
val conversionType = dbutils.widgets.get("ConversionType")
val conversionJsonContainer = dbutils.widgets.get("ConversionJsonContainer") 
val conversionJsonFolderPath = dbutils.widgets.get("ConversionJsonFolderPath") 
val conversionJsonFileName = dbutils.widgets.get("ConversionJsonFileName")
val hasControlFile = dbutils.widgets.get("HasControlFile")

//create folder and file variables
val mountPoint = "/mnt/"
val sourceDelimiter = "*"
val blobPath = mountPoint + currentContainer + "blob" //blob storage reference
val toProcessPath = blobPath + currentFolderPath 
val dataFilePath = toProcessPath + "/" + fileName //datafile reference
val conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" +  conversionJsonFileName //conversion json reference

val convertedFilePath = blobPath + "/ConvertedFiles/" + conversionType 
val fullconvertedFilePath = convertedFilePath + "/" + fileName

val controlFileName = fileName+".ctl"
val controlFilePath = convertedFilePath + "/" + controlFileName
val fullcontrolFilePath = controlFilePath + "/" + controlFileName
val ctlProcessPath = toProcessPath + "/" + controlFileName

var returnJSON: String  = ""

// COMMAND ----------

// DBTITLE 1,Call Libraries
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.hadoop.fs._
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

// DBTITLE 1,Call Shared Methods Notebook
// MAGIC %run "../CommonMethods/ABC/ConversionMain"

// COMMAND ----------

// DBTITLE 1,Create Schema Dataframe
//create json dataframe and explode columns
val dfJSonFile = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
val expRecordType = dfJSonFile.select(explode($"RecordTypes")).select($"col.Type",$"col.ColumnNames")
val expColumnNames = expRecordType.select($"Type",explode($"ColumnNames")).select($"Type",$"col.FieldName",$"col.StartPos",$"col.Length",$"col.ControlFile")

// COMMAND ----------

// DBTITLE 1,Create Dataframes Based on Record Types
////Header - Pass in header array and data dataframe
val dfHheader = createDelimitedDF(expColumnNames, "0", sourceDelimiter, true, dataFilePath)
dfHheader.createOrReplaceTempView("dataHheader") 

////Data - Pass in detail array and data dataframe
val dfDdetail = createDelimitedDF(expColumnNames, "1", sourceDelimiter, false, dataFilePath)
dfDdetail.createOrReplaceTempView("dataDetail") 

////Trailer - Pass in trailer array and data dataframe
val dfTtrailer = createDelimitedDF(expColumnNames, "9", sourceDelimiter, true, dataFilePath)
dfTtrailer.createOrReplaceTempView("dataTtrailer") 

// COMMAND ----------

// DBTITLE 1,Create Consolidated Detail Data File
val dfDetail: DataFrame = dfDdetail.crossJoin(dfHheader)
writeDfCSV(dfDetail, fullconvertedFilePath, fileName, Delimiter)

// COMMAND ----------

// DBTITLE 1,Create Consolidated Control File Dataframe and Control File
if (hasControlFile == "True") {
val dfControlFile: DataFrame = dfHheader.crossJoin(dfTtrailer)
                                      .withColumn("FILE_ID",lit(fileId))


writeDfCSV(dfControlFile, controlFilePath, controlFileName, Delimiter)

Try(moveFile(fullcontrolFilePath, ctlProcessPath))
Try(removeFile(controlFilePath))
}

// COMMAND ----------

// DBTITLE 1,Record Counts
val recordCount = dfDetail.count()

returnJSON = """{
       "RecordCount":" """ + recordCount + """ "
       }"""

//println(returnJSON)
//return JSON
dbutils.notebook.exit(returnJSON)
