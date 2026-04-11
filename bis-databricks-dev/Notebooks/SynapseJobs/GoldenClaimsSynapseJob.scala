// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer")

// COMMAND ----------

// DBTITLE 1,Import libraries
import java.sql.DriverManager
import java.util.Properties
import org.apache.spark.sql.DataFrame

// COMMAND ----------

// DBTITLE 1,Call Synapse JSON Creator Class
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Setup variables
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var envUser="_ETLUSER_SQL"
var blobKey = ""

if (dbEnv == "934226345849410") {envLetter = "d"; envUser = "DEV"+envUser; blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {envLetter = "q"; envUser = "QA"+envUser; blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {envLetter = "s"; envUser = "STG"+envUser; blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {envLetter = "p"; envUser = "PRD"+envUser; blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="} 

Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
val jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
val jdbcPort = 1433
val jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val GoldenClaimFolder = "/mnt/"+clientContainer+"/consolidated/MA/Data/GoldenClaim"
val TempblobStorageAccount = "wasbs://stream-temp@svtss"+envLetter+"idap01s.blob.core.windows.net/temp"
val SparkBlobSetup = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"
val jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase

// Create a Properties() object to hold the parameters.
val connectionProperties = new Properties()
val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"

connectionProperties.put("user", s"$jdbcUsername")      //s"${jdbcUsername}")
connectionProperties.put("password", s"$jdbcPassword")  //s"${jdbcPassword}")
connectionProperties.setProperty("Driver", driverClass)

//Identify Synapse Table
val gcTbl = clientContainer.concat(".GoldenClaim")
val gcHistory = clientContainer.concat(".GoldenClaimHistory")
val checkPoint = GoldenClaimFolder + "/Checkpoint-GoldenClaimsHistory/"

//mounting blob using
spark.conf.set(SparkBlobSetup,blobKey)

// COMMAND ----------

import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Execute GCSynapse method
def executeGCSynapse(df: DataFrame, gcTbl: String) = {
   val trunSQL = """TRUNCATE TABLE """ + gcTbl
  
   val pushdown_query = "(SELECT TOP 1 * FROM " + gcTbl + ") a" 
   //gets the table in ordinal position from source - just the first row
   val synapse = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=connectionProperties)
    
   val columnsAll = synapse.columns.map(m=>col(m))
  
   df.select(
          columnsAll:_*
   )
  .write
  .mode(SaveMode.Append)
  .format("com.databricks.spark.sqldw")
  .option("url", jdbcUrl)
  .option("user",jdbcUsername)
  .option("password",jdbcPassword)
  .option("tempDir", TempblobStorageAccount)
  .option("forwardSparkAzureStorageCredentials", "true")
  .option("dbTable", gcTbl)
  .option("preActions", trunSQL)
  .save()
}

// COMMAND ----------

def executeGCHistorySynapse(df: DataFrame, gcHistory: String) = {
  val pushdown_query = "(SELECT TOP 1 * FROM " + gcHistory + ") a" 
  //gets the table in ordinal position from source - just the first row
  val synapse = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=connectionProperties)
    
  val columnsAll = synapse.columns.map(m=>col(m))
  val consolidated = df.withColumnRenamed("GeneratedGoldenUniqueClaimsKey", "GeneratedGoldenClaimsUniqueKey")
                       .withColumn("LoadTimestamp", to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))
  
  consolidated.select( 
    columnsAll:_*
   )
  .write
  .mode(SaveMode.Append)
  .format("com.databricks.spark.sqldw")
  .option("url", jdbcUrl)
  .option("user",jdbcUsername)
  .option("password",jdbcPassword)
  .option("tempDir", TempblobStorageAccount)
  .option("forwardSparkAzureStorageCredentials", "true")
  .option("dbTable", gcHistory)
  .save()
}

// COMMAND ----------

// DBTITLE 1,Call  Streaming to Golden Claims History Table
var rJSON = new synJSONCreator
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

try {
    val con = DriverManager.getConnection(jdbcUrl, connectionProperties)
    val stmt = con.createStatement()

    //Read the table in delta lake for Golden Claims
    var consolidatedClaims = spark.read.format("delta").load(GoldenClaimFolder) 
    //truncate and load
    val result = executeGCSynapse(consolidatedClaims, gcTbl)
    
    //GC History Load append only -- no truncate
    val resultAll = executeGCHistorySynapse(consolidatedClaims, gcHistory)
  
    rJSON.addNewEntry("Status", "SUCCESS" )
    rJSON.addNewEntry("ErrorMessage", "", false)
}
catch{
      case unknown: Exception =>  {
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(unknown.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
    }
}
finally{
    rJSON.addBraceEnd()
    dbutils.notebook.exit(rJSON.getJSON())
}
