// Databricks notebook source
// MAGIC %md
// MAGIC #This script is to be used to call Pre-Deployment scripts
// MAGIC 
// MAGIC **This script should not be removed**
// MAGIC 
// MAGIC To use this script, call Notebooks from within a release folder to be executed after a deployment.  The scripts should be setup in a way so that they are only executed when needed.
// MAGIC 
// MAGIC Older scripts should be remove once their release has been completed

// COMMAND ----------

// DBTITLE 1,Import Libraries
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Define method
def ExecuteScripts(Record: org.apache.spark.sql.Row): Boolean = {
          val Notebook = "./Notebooks/" + Record(0).toString
          println(Notebook)
  
          /*
              Run notebooks
          */
  
          dbutils.notebook.run(Notebook, 0)
          
    return true
}

// COMMAND ----------

// DBTITLE 1,Add notebook references below
val NoteBooks = """
{
  "Notebook": [
  
  ]
}
"""
 
val notebooks = spark.read.json(Seq(NoteBooks).toDS())
val notebookDF = notebooks.select(explode($"Notebook")).selectExpr("col AS Notebook")  
notebookDF.collect().foreach(row => ExecuteScripts(row))
