// Databricks notebook source
// DBTITLE 1,Set Parameters
//File Parameters
dbutils.widgets.text("FileId","","") //0 
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

// DBTITLE 1,Method: getSortedSelect - Retrieves a Dynamic Select List in a Specific Order
def getSortedSelect (json: DataFrame, selectTag: String, orderTag: String): Array[org.apache.spark.sql.Column] = {
  val colNames = json.select(s"$selectTag")
                     .sort(s"$orderTag")
                     .collect()
                     .map(x=>col(x(0).toString))
  return colNames
}

// COMMAND ----------

// DBTITLE 1,Create Schema Dataframes
//create json dataframe and explode sections
val dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)

val expSections = dfJSon.select(explode($"RecordTypes")).select($"col.Headers",$"col.Trailers",$"col.Details")
val expHeaders = expSections.select(explode($"Headers")).select($"col.Type",$"col.ColumnNames")
val expTrailers = expSections.select(explode($"Trailers")).select($"col.Type",$"col.ColumnNames")
val expDetails = expSections.select(explode($"Details")).select($"col.Type",$"col.ColumnNames")


// COMMAND ----------

// DBTITLE 1,Loop Through Headers to Get Converted Delimited Dataframe
//Load full file into rdd
val dfData = spark.sparkContext.textFile(dataFilePath)

var dfHeader = spark.emptyDataFrame
val rTypes = expHeaders.select($"Type").collect.map(x=>x(0)).toList

rTypes.foreach(t=>
               {
                 val rt = t.toString
                 //create dataframe for record type
                 val expHeaderColNames = expHeaders.select(explode($"ColumnNames")).select($"col.FieldName",$"col.Length").filter($"Type".contains(s"$rt"))
                 val dfOutput = createFixedWidthDF(dfData, expHeaderColNames, rt)
                 
                if(dfHeader.count()== 0)
                  {dfHeader = dfOutput}
                else
                  {dfHeader = dfHeader.union(dfOutput)} 
               }
              )

// COMMAND ----------

// DBTITLE 1,Loop Through Trailers to Get Converted Delimited Dataframe
//Load full file into rdd
val dfData = spark.sparkContext.textFile(dataFilePath)

var dfTrailer = spark.emptyDataFrame
val rTypes = expTrailers.select($"Type").collect.map(x=>x(0)).toList

rTypes.foreach(t=>
               {
                 val rt = t.toString
                 //create dataframe for record type
                 val expTrailerColNames = expTrailers.select(explode($"ColumnNames")).select($"col.FieldName",$"col.Length").filter($"Type".contains(s"$rt"))
                 val dfOutput = createFixedWidthDF(dfData, expTrailerColNames, rt)
                 
                if(dfTrailer.count()== 0)
                  {dfTrailer = dfOutput}
                else
                  {dfTrailer = dfTrailer.union(dfOutput)} 
               }
              )

// COMMAND ----------

// DBTITLE 1,Create Consolidated Control File Dataframe and Control File
val dfControlFile: DataFrame = dfHeader.alias("h")
                                        .crossJoin(dfTrailer.alias("t"))
                                        .withColumn("FILE_ID",lit(fileId))
                                        .select("h.ContractNumber", "h.RunDate", "h.PaymentYearAndMonth", "t.TotalRecordCount", "FILE_ID")
writeDfCSV(dfControlFile, controlFilePath, controlFileName, delimiter)

Try(moveFile(fullcontrolFilePath, ctlProcessPath))
Try(removeFile(controlFilePath))

// COMMAND ----------

// DBTITLE 1,Loop Through Details to Get Converted Delimited Dataframe
//Load full file into rdd
val dfData = spark.sparkContext.textFile(dataFilePath)

var dfDetail = spark.emptyDataFrame
val rTypes = expDetails.select($"Type").collect.map(x=>x(0)).toList

rTypes.foreach(t=>
               { 
                 val rt = t.toString
                 //create dataframe for record type
                 val expDetailColNames = expDetails.select(explode($"ColumnNames")).select($"col.FieldName",$"col.Length").filter($"Type".contains(s"$rt"))
                 val dfOutput = createFixedWidthDF(dfData, expDetailColNames, rt)
                 
                 //get sort order for record type.  this will be used to get all of the dataframes using the same order
                 val expColumnSort = expDetails.select(explode($"ColumnNames"))
                               .select($"col.FieldName",$"col.DestPos".cast(IntegerType).alias("DestPos"))
                               .filter($"Type".contains(s"$rt") && !$"FieldName".contains("Filler")) 
                 val cols = getSortedSelect(expColumnSort,"FieldName","DestPos")
                 
                if(dfDetail.count()== 0)
                  {dfDetail = dfOutput.select(cols:_*)}
                else
                  {dfDetail = dfDetail.union(dfOutput.select(cols:_*))} 
               }
              )


// COMMAND ----------

// DBTITLE 1,Create Consolidated Detail and Write Out to Conversion Folder
val dfDetailFile: DataFrame = dfDetail.alias("d")
                                        .crossJoin(dfControlFile.alias("c"))
                                        .withColumn("FILE_ID",lit(fileId))
                                        .select("c.ContractNumber", "c.RunDate", "c.PaymentYearAndMonth","d.*")

writeDfCSV(dfDetailFile, fullconvertedFilePath, fileName, delimiter)

// COMMAND ----------

// DBTITLE 1,Return - Data File Record Count
val recordCount = dfDetail.count()

returnJSON = """{
       "RecordCount":" """ + recordCount + """ "
       }"""

dbutils.notebook.exit(returnJSON)
