// Databricks notebook source
import org.apache.spark.sql.types._
import org.apache.spark.sql.DataFrame

// COMMAND ----------

// DBTITLE 1,Method: Get DataTypes for DataModel (SQLTypes)
def getSQLType(dTypeString: String): String = {
//https://spark.apache.org/docs/latest/sql-ref-datatypes.html
  
  val dType = dTypeString match {  
     case "ByteType" => "BYTE"
     case "ShortType" => "SMALLINT"
     case "IntegerType" => "INTEGER" 
     case "LongType" => "BIGINT"
     case "FloatType" => "FLOAT"
     case "DoubleType" => "DOUBLE"
     case "StringType" => "STRING" 
     case "BinaryType" => "BINARY" 
     case "BooleanType" => "BOOLEAN" 
     case "TimestampType" => "TIMESTAMP" 
     case "DateType" => "DATE" 
     case _ => "STRING"  
   }

  return dType
}

// COMMAND ----------

// DBTITLE 1,Method: Get DataTypes for DataModel (Scala Types)
def getDataType(dTypeString: Any): DataType = {

  val dType = dTypeString match {  
     case "ByteType" => ByteType
     case "ShortType" => ShortType
     case "IntegerType" => IntegerType 
     case "LongType" => LongType
     case "FloatType" => FloatType
     case "DoubleType" => DoubleType
     case "StringType" => StringType
     case "BinaryType" => BinaryType 
     case "BooleanType" => BooleanType 
     case "TimestampType" => TimestampType 
     case "DateType" => DateType 
     case _ => StringType
   }

  return dType
}

// COMMAND ----------

// DBTITLE 1,Method: getStruct
def getStruct(dataModel: DataFrame): StructType = {
  val header = dataModel.select("FieldName","DataType","Ordinal").collect.map(_.toSeq) 
  val structString = StructType(header.map(x=>StructField(x(0).toString.trim(), getDataType(x(1)), nullable = true)))
  return structString
}
