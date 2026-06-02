# Databricks notebook source
from pyspark.sql import DataFrame
from pyspark.sql.functions import explode, col
from pyspark.sql.types import StructType, StructField, StringType

# COMMAND ----------

# DBTITLE 1,Method:IsIgnoreHeader
def isIgnoreHeader(file: str, validation: str, delimiter: str, textQualifier: str) -> DataFrame:
  
  fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  parsedSchema = fullSchema.select(explode(col("columnNames"))).select(col("col.FieldName"), col("col.DataType")).filter(col("col.FieldName") != "TEMPLATE")
  
  # Pulls text values out into a native local Python array
  header = [row[0].strip() for row in parsedSchema.select("FieldName").collect()]
  fields = [StructField(fieldName, StringType(), nullable=True) for fieldName in header] 
  schema = StructType(fields)
  
  dfFile1 = spark.read.format("csv").schema(schema).option("header", False).option("delimiter", delimiter).option("quote", textQualifier).load(file)
  
  # Captures the very first row object to drop it from the dataset matching Scala row comparison logic
  firstLine = dfFile1.first() 
  dfFile = dfFile1.filter(lambda row: row != firstLine)
  
  return dfFile

# COMMAND ----------

# DBTITLE 1,Method: WithoutHeader
def withoutHeader(file: str, validation: str, delimiter: str, textQualifier: str) -> DataFrame:

  fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  parsedSchema = fullSchema.select(explode(col("columnNames"))).select(col("col.FieldName"), col("col.DataType")).filter(col("col.FieldName") != "TEMPLATE")
  
  header = [row[0].strip() for row in parsedSchema.select("FieldName").collect()]
  fields = [StructField(fieldName, StringType(), nullable=True) for fieldName in header] 
  schema = StructType(fields)
  
  dfFile = spark.read.format("csv").schema(schema).option("header", False).option("delimiter", delimiter).option("quote", textQualifier).load(file) 
  
  return dfFile

# COMMAND ----------

# DBTITLE 1,Method: DelimitedFile
def delimitedFile(file: str, validation: str, header: str, delimiter: str, textQualifier: str) -> DataFrame:
  
  fullSchema = spark.read.format("json").option("multiline", "true").load(validation)
  parsedSchema = fullSchema.select(explode(col("columnNames"))).select(col("col.FieldName"), col("col.DataType")).filter(col("col.FieldName") != "TEMPLATE")
  
  schemHeader = [row[0].strip() for row in parsedSchema.select("FieldName").collect()]
  fields = [StructField(fieldName, StringType(), nullable=True) for fieldName in schemHeader] 
  schema = StructType(fields)
  
  dfFile = spark.read.format("csv") \
      .schema(schema) \
      .option("header", header) \
      .option("delimiter", delimiter) \
      .option("quote", textQualifier) \
      .load(file)
  
  return dfFile

# COMMAND ----------

# DBTITLE 1,Method: Path_Exists
def path_exists(pathToCheck: str) -> bool:
  
  # References the JVM gateway on the cluster via PySpark sparkContext to securely invoke the Hadoop FileSystem APIs
  sc = spark.sparkContext
  path_class = sc._gateway.jvm.org.apache.hadoop.fs.Path
  fs_class = sc._gateway.jvm.org.apache.hadoop.fs.FileSystem
  
  fs = fs_class.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(path_class(pathToCheck))
  
  return IsExists