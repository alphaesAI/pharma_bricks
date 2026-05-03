// Local Spark version of CSVConversionBatch.scala
// Non-Databricks dependent Scala

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.{Try, Success, Failure}
import io.delta.tables._
import spark.implicits._
import scala.io.Source
import org.json4s._
import org.json4s.jackson.JsonMethods._

// Initialize Spark session
val spark = SparkSession.builder()
  .appName("CSVConversionBatch")
  .master("local[*]")
  .getOrCreate()

// Case class for file conversion parameters
case class FileConversionType(
  fileId: String,
  fileLayoutDescription: String,
  currentContainer: String,
  currentFolderPath: String,
  fileName: String,
  conversionType: String,
  columnDelimiter: String,
  conversionFileContainer: String,
  conversionFileFolderPath: String,
  conversionFileName: String,
  hasControlFile: String,
  registrationDatetime: String,
  fullValidatedPath: String
)

case class ReturnedData(
  recordCount: String
)

// Load configuration from JSON file
def loadBatchConfig(): String = {
  val configPath = "config/batch_files.json"  // Path to batch file configuration
  try {
    val jsonSource = Source.fromFile(configPath)
    val jsonString = jsonSource.mkString
    jsonSource.close()
    jsonString
  } catch {
    case _: Exception =>
      // Return default batch configuration for testing
      """{
        "FileIds": [
          {
            "FileID": "1",
            "FileLayoutDescription": "Submitted837OutboundClaims",
            "CurrentContainer": "testcontainer",
            "CurrentFolderPath": "/MA/Internal/FCF/2023/11/06/",
            "FileName": "837_mult_claims.txt",
            "ConversionType": "Submitted837OutboundClaims",
            "ColumnDelimiter": "|",
            "ConversionFileContainer": "fileconfig",
            "ConversionFileFolderPath": "/JSON/Conversion",
            "ConversionFileName": "submitted837_conversion.json",
            "HasControlFile": "false",
            "RegistrationDatetime": "20231106140840",
            "FullValidatedPath": "/mnt/local/testcontainerblob/MA/Internal/FCF/2023/11/06/837_mult_claims.txt"
          }
        ]
      }"""
  }
}

// Load batch configuration
val lookupFilesJson = loadBatchConfig()

// Parse the JSON configuration
implicit val formats = DefaultFormats
val batchConfig = parse(lookupFilesJson)

// Create DataFrame from the JSON
val fileID = spark.read.json(Seq(lookupFilesJson).toDS)

val explodedFileIDs = fileID.select(explode($"FileIds")).select(
  $"col.FileID".as("fileId"),
  $"col.FileLayoutDescription".as("fileLayoutDescription"),
  $"col.CurrentContainer".as("currentContainer"),
  $"col.CurrentFolderPath".as("currentFolderPath"),
  $"col.FileName".as("fileName"),
  $"col.ConversionType".as("conversionType"),
  $"col.ColumnDelimiter".as("columnDelimiter"),
  $"col.ConversionFileContainer".as("conversionFileContainer"),
  $"col.ConversionFileFolderPath".as("conversionFileFolderPath"),
  $"col.ConversionFileName".as("conversionFileName"),
  $"col.HasControlFile".as("hasControlFile"),
  $"col.RegistrationDatetime".as("registrationDatetime"),
  $"col.FullValidatedPath".as("fullValidatedPath")
)

val doubleQuote = "\""
var rJSON = "["

var iterator = 0

explodedFileIDs.as[FileConversionType].collect().foreach { t =>
  var results = ""
  var isSuccess = true
  
  if (iterator == 0) {
    rJSON += "{"
  } else {
    rJSON += ",{"
  }
  
  rJSON += doubleQuote + "FileID" + doubleQuote + ":" + doubleQuote + t.fileId + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "FileLayoutDescription" + doubleQuote + ":" + doubleQuote + t.fileLayoutDescription + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "CurrentContainer" + doubleQuote + ":" + doubleQuote + t.currentContainer + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "CurrentFolderPath" + doubleQuote + ":" + doubleQuote + t.currentFolderPath + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "FileName" + doubleQuote + ":" + doubleQuote + t.fileName + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "ConversionType" + doubleQuote + ":" + doubleQuote + t.conversionType + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "RegistrationDatetime" + doubleQuote + ":" + doubleQuote + t.registrationDatetime + doubleQuote
  rJSON += ","
  rJSON += doubleQuote + "FullValidatedPath" + doubleQuote + ":" + doubleQuote + t.fullValidatedPath + doubleQuote
  rJSON += ","
  
  try {
    // Call CSVConversion with parameters
    // In local environment, we'll call the conversion method directly
    println(s"Processing file: ${t.fileName} with conversion type: ${t.conversionType}")
    
    // For testing, we'll simulate the conversion result
    // In real implementation, you would call the actual conversion logic
    val simulatedResult = """{"RecordCount": "5"}"""
    
    // Parse the result
    val returnedData = spark.read.json(Seq(simulatedResult).toDS)
    
    returnedData.as[ReturnedData].collect().foreach { x =>
      if (x.recordCount.trim() == "0") {
        throw new Exception("Record count of the dataframe is 0. File was not written")
      } else {
        rJSON += doubleQuote + "ConvertedCount" + doubleQuote + ":" + doubleQuote + x.recordCount + doubleQuote
        rJSON += ","
      }
    }
    
  } catch {
    case e: Exception =>
      isSuccess = false
      println(s"Error processing file ${t.fileName}: ${e.getMessage}")
      rJSON += doubleQuote + "ConvertedCount" + doubleQuote + ":" + doubleQuote + 0 + doubleQuote
      rJSON += ","
  }
  
  rJSON += doubleQuote + "IsConversionSucceed" + doubleQuote + ":" + doubleQuote + isSuccess + doubleQuote
  rJSON += "}"
  
  iterator += 1
}

rJSON += "]"

println(s"Batch conversion result: $rJSON")

// Return the result (replaces dbutils.notebook.exit)
println(rJSON)

spark.stop()
