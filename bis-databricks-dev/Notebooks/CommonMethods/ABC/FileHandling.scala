// Databricks notebook source
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

// COMMAND ----------

// DBTITLE 1,Method:IsIgnoreHeader
def isIgnoreHeader(file: String, validation: String, delimiter: String, textQualifier: String): DataFrame = {
  
  val fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  val parsedSchema = fullSchema.select( explode($"columnNames")).select($"col.FieldName",$"col.DataType").filter($"col.FieldName" =!= "TEMPLATE")
  val header = parsedSchema.select("FieldName").map(x=>x.getString(0).trim()).collect()
  val fields = header.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
  val schema = StructType(fields)
  
  var dfFile1 = spark.read.format("csv").schema(schema).option("header", false).option("delimiter", delimiter).option("quote", textQualifier).load(file)
  
  val firstLine = dfFile1.first() 
  var dfFile = dfFile1.filter(row => row != firstLine)
  
  dfFile
}

// COMMAND ----------

// DBTITLE 1,Method: WithoutHeader
def withoutHeader(file: String, validation: String, delimiter: String, textQualifier: String): DataFrame = {

  val fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  val parsedSchema = fullSchema.select( explode($"columnNames")).select($"col.FieldName",$"col.DataType").filter($"col.FieldName" =!= "TEMPLATE")
  val header = parsedSchema.select("FieldName").map(x=>x.getString(0).trim()).collect()
  val fields = header.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
  val schema = StructType(fields)
  
  var dfFile = spark.read.format("csv").schema(schema).option("header", false).option("delimiter", delimiter).option("quote",textQualifier).load(file) 
  
  dfFile
}

// COMMAND ----------

// DBTITLE 1,Method: DelimitedFile
def delimitedFile(file: String, validation: String, header: String, delimiter: String, textQualifier: String): DataFrame = {
  
  val fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  val parsedSchema = fullSchema.select( explode($"columnNames")).select($"col.FieldName",$"col.DataType").filter($"col.FieldName" =!= "TEMPLATE")
  val schemHeader = parsedSchema.select("FieldName").map(x=>x.getString(0).trim()).collect()
  val fields = schemHeader.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
  val schema = StructType(fields)
  
  val dfFile = spark.read.format("csv")
      .schema(schema)
      .option("header", header)
      .option("delimiter", delimiter)
      .option("quote",textQualifier)
      .load(file)
  
  dfFile
}

// COMMAND ----------

// DBTITLE 1,Method: Path_Exists
import  org.apache.hadoop.fs.{FileSystem,Path}

def path_exists(pathToCheck: String): Boolean =
{ 
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val IsExists = fs.exists(new org.apache.hadoop.fs.Path(pathToCheck)) 
  return IsExists 
}
