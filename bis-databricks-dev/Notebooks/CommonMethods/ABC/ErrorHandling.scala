// Databricks notebook source
// DBTITLE 1,Method: outputValidationError
import org.apache.spark.sql.SaveMode
import org.apache.spark.sql._
def outputValidationError(dfError: DataFrame, errorPath: String) = {

    val tsvWithHeaderOptions: Map[String, String] = Map(
      ("delimiter",",")
      ,("filetype", "csv")  
      ,("header", "true"))  // Writes a header record with column names

    dfError.coalesce(1)
      .write
      .mode(SaveMode.Append)
      .options(tsvWithHeaderOptions)
      .csv(errorPath)
}

// COMMAND ----------

// MAGIC %py
// MAGIC def consolidateError(dfError, errorPath):
// MAGIC
// MAGIC   dfError.coalesce(1) \
// MAGIC     .write \
// MAGIC     .mode("append") \
// MAGIC     .option("delimiter",",") \
// MAGIC     .option("filetype", "csv") \
// MAGIC     .option("header", "true") \
// MAGIC     .csv(errorPath)
