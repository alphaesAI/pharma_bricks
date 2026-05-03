// Local Spark version of GenericConversion.scala
// Non-Databricks dependent Scala

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.hadoop.fs._
import scala.util.{Try, Success, Failure}
import io.delta.tables._
import spark.implicits._
import scala.io.Source
import org.json4s._
import org.json4s.jackson.JsonMethods._

// Case class for configuration
case class ConversionConfig(
  fileId: String,
  fileLayoutDescription: String,
  currentContainer: String,
  currentFolderPath: String,
  fileName: String,
  delimiter: String,
  conversionType: String,
  conversionJsonContainer: String,
  conversionJsonFolderPath: String,
  conversionJsonFileName: String,
  hasControlFile: String
)

object GenericConversion {
  def main(args: Array[String]): Unit = {
    // Initialize Spark session
    val spark = SparkSession.builder()
      .appName("GenericConversion")
      .master("local[*]")
      .getOrCreate()

    try {
      // Load configuration from JSON file instead of dbutils.widgets
      val config = loadConfig()
      
      // Extract parameters from config
      val fileId = config.fileId
      val fileLayoutDescription = config.fileLayoutDescription
      val currentContainer = config.currentContainer
      val currentFolderPath = config.currentFolderPath
      val fileName = config.fileName
      val delimiter = config.delimiter
      val conversionType = config.conversionType
      val conversionJsonContainer = config.conversionJsonContainer
      val conversionJsonFolderPath = config.conversionJsonFolderPath
      val conversionJsonFileName = config.conversionJsonFileName
      val hasControlFile = config.hasControlFile

      // Create folder and file variables
      val mountPoint = "/mnt/"  // This will need to be adjusted for local environment
      val blobPath = mountPoint + currentContainer + "blob"
      val toProcessPath = blobPath + currentFolderPath
      val dataFilePath = toProcessPath + "/" + fileName
      val conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" + conversionJsonFileName

      val convertedFilePath = blobPath + "/ConvertedFiles/" + fileLayoutDescription
      val fullconvertedFilePath = convertedFilePath + "/" + fileName

      val controlFileName = fileName + ".ctl"
      val controlFilePath = convertedFilePath + "/" + controlFileName
      val fullcontrolFilePath = controlFilePath + "/" + controlFileName
      val ctlProcessPath = toProcessPath + "/" + controlFileName

      var returnJSON: String = ""

      // Import shared methods (local version)
      // Instead of %run, we'll import the methods directly
      import ConversionMain._

      // Create Schema Dataframe
      // Create json dataframe and explode columns
      val dfJSon = spark.read.format("json").option("multiline", "true").load(conversionJsonPath)
      val expColumnNames = dfJSon.select(explode($"ColumnNames")).select($"col.FieldName", $"col.Length").filter($"col.FieldName" =!= "TEMPLATE")

      // Convert Source File to DataFrame
      val dfData = spark.sparkContext.textFile(dataFilePath)

      val dfDetail = createFixedWidthDF(dfData, expColumnNames)

      // Create Consolidated Detail Data File Dataframe and Data File
      writeDfCSV(dfDetail, fullconvertedFilePath, fileName, delimiter)

      // Return - Data File Record Count
      val recordCount = dfDetail.count()

      returnJSON = s"""{
         "RecordCount":" $recordCount "
         }"""

      println(returnJSON)
      println(s"Conversion completed successfully. Record count: $recordCount")
      
    } catch {
      case e: Exception =>
        println(s"Error in GenericConversion: ${e.getMessage}")
        e.printStackTrace()
        val returnJSON = s"""{"error": "${e.getMessage}"}"""
        println(returnJSON)
    } finally {
      spark.stop()
    }
  }

  // Load configuration from JSON file
  def loadConfig(): ConversionConfig = {
    implicit val formats = DefaultFormats
    
    val configPath = "config/credentials.json"  // Adjust path as needed
    try {
      val jsonSource = Source.fromFile(configPath)
      val jsonString = jsonSource.mkString
      jsonSource.close()
      
      parse(jsonString).extract[ConversionConfig]
    } catch {
      case _: Exception =>
        println(s"Config file not found at $configPath, using default values")
        // Return default config
        ConversionConfig(
          fileId = "",
          fileLayoutDescription = "",
          currentContainer = "",
          currentFolderPath = "",
          fileName = "",
          delimiter = "|",
          conversionType = "",
          conversionJsonContainer = "",
          conversionJsonFolderPath = "",
          conversionJsonFileName = "",
          hasControlFile = ""
        )
    }
  }
}
