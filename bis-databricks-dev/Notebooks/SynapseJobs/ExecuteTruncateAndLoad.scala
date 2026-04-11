// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConsolidatedPath","","")
dbutils.widgets.text("DestTable","","") 

val clientContainer = dbutils.widgets.get("ClientContainer")
val consolidatedPath = dbutils.widgets.get("ConsolidatedPath")
val destTable = dbutils.widgets.get("DestTable") 

// COMMAND ----------

// DBTITLE 1,Import libraries
import org.apache.spark.sql.streaming.Trigger
import org.apache.spark.sql.DataFrame
import scala.util.{Try, Success, Failure}
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Defined variables for JDBC connection
//Create environment variable to handle the database connection
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var envUser="_ETLUSER_SQL"
var blobKey = ""

if (dbEnv == "934226345849410") {envLetter = "d"; envUser = "DEV"+envUser; blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {envLetter = "q"; envUser = "QA"+envUser; blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {envLetter = "s"; envUser = "STG"+envUser; blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {envLetter = "p"; envUser = "PRD"+envUser; blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="} 

val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val sprakPath = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"
val jdbcString = "jdbc:sqlserver://sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net:1433;database=syn-c-"+envLetter+"-shrd-idap0000-01"
val tempDir = "wasbs://"+clientContainer+"@svtss"+envLetter+"idap01s.blob.core.windows.net/stream-temp"

import java.util.Properties
val jdbcProperties = new Properties()

jdbcProperties.put("user", s"${jdbcUsername}")
jdbcProperties.put("password", s"${jdbcPassword}")
jdbcProperties.put("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") 

// COMMAND ----------

// DBTITLE 1,Remove Empty Strings from all columns
import org.apache.spark.sql.Column

def replaceEmptyCols(columns:Array[String]):Array[Column]={
    columns.map(c=>{
      when(col(c)==="" ,null).otherwise(col(c)).alias(c)
    })
} 

// COMMAND ----------

// DBTITLE 1,Add to meet Required Columns from DataModel
import org.apache.spark.sql.functions._

def customSelect(availableCols: List[String], requiredCols: List[String]) = {
      val availableColsList = availableCols.map(_.toLowerCase)
  
      requiredCols.map(column => column match {
            case column if availableColsList.contains(column.toLowerCase) => col(column)
            case _ => lit(null).cast("string").as(column)
      })
}

// COMMAND ----------

def startTruncateAndLoad(destTable: String, consolidatedPath: String): String = {
    spark.conf.set(sprakPath, blobKey)
    val trunSQL = """TRUNCATE TABLE """ + destTable
  
    //Read the table as a stream source 
    val df = spark.read.format("delta").load(consolidatedPath)
  
    val pushdown_query = "(SELECT TOP 1 * FROM " + destTable + ") a" 
    //gets the table in ordinal position from source - just the first row
    val synapse = spark.read.jdbc(url=jdbcString, table=pushdown_query, properties=jdbcProperties)
    
    //val columnsAll = synapse.columns.map(m=>col(m))
    
    val newDF = df.select(  
           customSelect(
                                 df.columns.toList, //Available columns
                                 synapse.columns.toList //Required Columns 
                     ):_*
        )
  
    newDF.select(replaceEmptyCols(newDF.columns):_*)
       .write
      .format("com.databricks.spark.sqldw")
      .option("url", jdbcString)
      .option("user",jdbcUsername)
      .option("password",jdbcPassword) 
      .option("tempDir", tempDir)
      .option("forwardSparkAzureStorageCredentials", "true")
      .option("dbTable", destTable)
      .option("preActions", trunSQL)
      .mode("append")
      .save()
  
  return "SUCCESS"
}

// COMMAND ----------

//Configure the write semantics for Azure Synapse connector in the notebook session conf.
spark.conf.set("spark.databricks.sqldw.writeSemantics", "polybase")

// COMMAND ----------

// DBTITLE 1,Execute truncate and reload and return notebook output
var rJSON = ""

try{ 
  startTruncateAndLoad(destTable, consolidatedPath)
  rJSON = "SUCCESS"
}
catch{ 
  case ex: Throwable =>  { 
      rJSON = "FAILURE: " + ex.getMessage.toString 
      throw new Exception(rJSON);
    }
}
finally{
  dbutils.notebook.exit(rJSON)
}
