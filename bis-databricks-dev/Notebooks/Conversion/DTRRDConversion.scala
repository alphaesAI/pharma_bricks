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
val dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
val expRecordType = dfJSon.select(explode($"RecordTypes")).select($"col.Type",$"col.ColumnNames") 

// COMMAND ----------

// DBTITLE 1,Create Dataframes Based on Record Types
//Load full file into rdd
val dfData = spark.sparkContext.textFile(dataFilePath) 

case class ColumnNames( 
        FieldName: String 
       ,OrdinalPosition: String
       ,StartPos: String
       ,EndPos: String
       ,Length: String
       ,DestPos: String 
)

case class RecordType( 
         Type: String 
        ,ColumnNames: Array[ColumnNames]
)

var df = spark.emptyDataFrame

expRecordType.as[RecordType].take(expRecordType.count.toInt).foreach(t =>
          {
            val dfColumnNames = expRecordType.where($"col.Type" === t.Type).select(explode($"ColumnNames")).select(
                                               $"col.FieldName"
                                              ,$"col.OrdinalPosition"
                                              ,$"col.StartPos"
                                              ,$"col.EndPos"
                                              ,$"col.Length"
                                              ,$"col.DestPos"   
            )
            
            
            val expColumnSort = expRecordType.select(explode($"ColumnNames")).select($"col.FieldName",$"col.DestPos".cast(IntegerType).alias("DestPos")).where($"col.Type" === t.Type)
            
            val cols = getSortedSelect(expColumnSort,"FieldName","DestPos")
            
            val dfDetail1 = createFixedWidthDF(dfData, dfColumnNames, t.Type)
            
            if(df.count() == 0)
                  {df = dfDetail1.select(cols:_*)}
            else
                  {df = df.union(dfDetail1.select(cols:_*))}  
          }
    )

//df.createOrReplaceTempView("DeltaTable")

// COMMAND ----------

// DBTITLE 1,Convert Source File to DataFrame
writeDfCSV(df, fullconvertedFilePath, fileName, delimiter)

// COMMAND ----------

// DBTITLE 1,Return - Data File Record Count
val recordCount = df.count()

returnJSON = """{
       "RecordCount":" """ + recordCount + """ "
       }"""

dbutils.notebook.exit(returnJSON)
