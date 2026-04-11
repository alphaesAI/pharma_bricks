// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ConsolidatedPath","","")
dbutils.widgets.text("DestTable","","")
dbutils.widgets.text("CheckPoint","","")

val consolidatedPath = dbutils.widgets.get("ConsolidatedPath")
val destTable = dbutils.widgets.get("DestTable")
val checkPoint = dbutils.widgets.get("CheckPoint")

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
val tempDir = "wasbs://stream-temp@svtss"+envLetter+"idap01s.blob.core.windows.net/temp"

// COMMAND ----------

// DBTITLE 1,Create streaming method
def startStreaming(df: DataFrame): Try[org.apache.spark.sql.streaming.StreamingQuery] = {
  try{
    spark.conf.set(sprakPath, blobKey)
    
    val stream = df.writeStream
                  .format("com.databricks.spark.sqldw")  
                  .option("url", jdbcString)
                  .option("user", jdbcUsername)
                  .option("password", jdbcPassword)
                  .option("tempDir", tempDir)
                  .option("forwardSparkAzureStorageCredentials", "true")
                  .option("dbTable", destTable) 
                  .option("checkpointLocation", checkPoint) 
                  .trigger(Trigger.Once) // make sure iterate just one time
                  .outputMode("append")
                  .start()
    
    stream.awaitTermination()
    
    Success(stream)
    
    } 
  catch {
      case unknown: Exception => {
        Failure(unknown)
      }
    }
}

// COMMAND ----------

// DBTITLE 1,Execute streaming and return notebook output
var rJSON = ""

//Read the table as a stream source 
var rawDf = spark.readStream.format("delta").load(consolidatedPath)

//Renamed columns to match model in synapse
var consolidated = rawDf
    .withColumnRenamed("LOAD_DATETIME", "LoadDateTime")
    .withColumnRenamed("FILE_ID", "FileID")
    .withColumnRenamed("CLIENT_ID", "ClientID")
    .withColumnRenamed("FILE_LAYOUT_ID", "FileLayoutID")
    .withColumnRenamed("FILE_LAYOUT_DESCRIPTION", "FileLayoutDescription")
    //data format
    .withColumn("Quantity", col("Quantity").cast("double"))
    .withColumn("RxFillDate", to_date($"RxFillDate", "yyyyMMdd")) 

startStreaming(consolidated) match {
                    case Success(df) => {
                           rJSON = "SUCCESS"
                    }
                    case Failure(ex) => { //handle exception
                        rJSON = "FAILURE: " + ex.getMessage.toString
                    }
            }

dbutils.notebook.exit(rJSON)