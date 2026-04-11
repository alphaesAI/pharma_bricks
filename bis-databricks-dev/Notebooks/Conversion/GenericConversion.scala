// Databricks notebook source
// DBTITLE 1,Set Parameters
//File Parameters
dbutils.widgets.text("FileId","","") //0 
dbutils.widgets.text("FileLayoutDescription","","") //0 
dbutils.widgets.text("CurrentContainer","","") //validate
dbutils.widgets.text("CurrentFolderPath","","") ///MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("ConversionType","","")
dbutils.widgets.text("FileName","","") //PBC_VIS_FCF_prod_20200227070003.TXT
dbutils.widgets.text("Delimiter","","") //"|"
dbutils.widgets.text("ConversionJsonContainer","","")   //fileconfig
dbutils.widgets.text("ConversionJsonFolderPath","","") // /JSON/Conversion
dbutils.widgets.text("ConversionJsonFileName","","") //lishist_conversion.json
dbutils.widgets.text("HasControlFile","","") //lishist_conversion.json

//capture values passed into from ADF
val fileId = dbutils.widgets.get("FileId") 
val FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
val currentContainer = dbutils.widgets.get("CurrentContainer") 
val currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
val fileName = dbutils.widgets.get("FileName") 
val delimiter = dbutils.widgets.get("Delimiter")
val conversionType = dbutils.widgets.get("ConversionType")
val conversionJsonContainer = dbutils.widgets.get("ConversionJsonContainer") 
val conversionJsonFolderPath = dbutils.widgets.get("ConversionJsonFolderPath") 
val conversionJsonFileName = dbutils.widgets.get("ConversionJsonFileName")
val hasControlFile = dbutils.widgets.get("HasControlFile")

//create folder and file variables
val mountPoint = "/mnt/"
val blobPath = mountPoint + currentContainer + "blob" //blob storage reference
val toProcessPath = blobPath + currentFolderPath 
val dataFilePath = toProcessPath + "/" + fileName //datafile reference
val conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" +  conversionJsonFileName //conversion json reference

val convertedFilePath = blobPath + "/ConvertedFiles/" + FileLayoutDescription 
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
val dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
val expColumnNames = dfJSon.select( explode($"ColumnNames")).select($"col.FieldName",$"col.Length").filter($"col.FieldName" =!= "TEMPLATE")

// COMMAND ----------

// DBTITLE 1,Convert Source File to DataFrame
val dfData = spark.sparkContext.textFile(dataFilePath)

val dfDetail = createFixedWidthDF(dfData, expColumnNames)

// COMMAND ----------

// DBTITLE 1,Create Consolidated Detail Data File Dataframe and Data File
writeDfCSV(dfDetail, fullconvertedFilePath, fileName, delimiter)

// COMMAND ----------

// DBTITLE 1,Return - Data File Record Count
val recordCount = dfDetail.count()

returnJSON = """{
       "RecordCount":" """ + recordCount + """ "
       }"""

println(returnJSON)
//return JSON
dbutils.notebook.exit(returnJSON)
