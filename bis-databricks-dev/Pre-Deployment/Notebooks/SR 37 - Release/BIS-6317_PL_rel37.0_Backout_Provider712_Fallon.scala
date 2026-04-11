// Databricks notebook source
// MAGIC %md
// MAGIC ## This notebook will run pre deployment to back out data and update Databases
// MAGIC - Update file status as ProcessingError for the FileLayoutId = 6003
// MAGIC - Back out data in processed and consolidated zone as requried (will delete the folder in datalake as well)
// MAGIC - Should run this notebook before DB creation Job. 

// COMMAND ----------

// DBTITLE 1,Imports
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._ 
import java.sql.DriverManager
import java.sql.Connection
import java.util.Properties

// COMMAND ----------

// DBTITLE 1,Setup Connection Parameters
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter ="" 
var envUser="_ETLUSER_SQL"
var clientFolder = ""

if (dbEnv == "934226345849410") {envLetter = "d";envUser = "DEV"+envUser;  clientFolder = "devidap1"}
else if (dbEnv == "5826678703751685") {envLetter = "q";envUser = "QA"+envUser; clientFolder = "qaidap2"}
else if (dbEnv == "7093677384385470") {envLetter = "s";envUser = "STG"+envUser;clientFolder = "fallon" }
else {envLetter = "p";envUser = "PRD"+envUser; clientFolder = "fallon"} 

Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
val jdbcHostname = "sql-c-" + envLetter + "-shrd-idap0000-01.database.windows.net"
val jdbcPort = 1433
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

// Create a Properties() object to hold the parameters.
import java.util.Properties
val connectionProperties = new Properties()

connectionProperties.put("user", s"$jdbcUsername")       
connectionProperties.put("password", s"$jdbcPassword") 

val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
connectionProperties.setProperty("Driver", driverClass)

// COMMAND ----------

// DBTITLE 1,Setup DB Connection
// Config
val configDBDatabase = "Configuration_DB_"+ clientFolder.toUpperCase()
val configDBUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+configDBDatabase 

// COMMAND ----------

// DBTITLE 1,Connect to ConfigDB and update the file statuses in FileTracking table
val con = DriverManager.getConnection(configDBUrl, connectionProperties)
val stmt = con.createStatement()

val updateSql = s"""
  WITH FileIDs AS
    (SELECT FileID
    FROM LatestFileWorkflowState
    WHERE FileLayoutID = 6003
    )
  UPDATE FileTracking
  SET WorkflowStateID = 19
  WHERE FileID IN 
    (SELECT FileID from FileIDs)
  AND WorkflowStateID = 34
                   """

// delete the tracking in dataGroupTracking to update LatestFileWorkflowState
val deleteSql = s"""
  WITH FileIDs AS
    (SELECT FileID
    FROM LatestFileWorkflowState
    WHERE FileLayoutID = 6003
    )
  DELETE FROM DataGroupTracking
  WHERE FileID IN 
  (SELECT FileID from FileIDs)
                   """

stmt.execute(updateSql)
stmt.execute(deleteSql)
stmt.close()

// COMMAND ----------

// MAGIC %md
// MAGIC ### Below is back out data in processed and consolidated zone

// COMMAND ----------

// DBTITLE 1,Method -- Back out data
def backOutData (path : String){
  try {
    var files = dbutils.fs.ls(path)
  
    for (f <- files){
      if (f.isDir) {
        backOutData(f.path)
      }  
      else {
        dbutils.fs.rm(f.path, recurse = true)
      }
    }  
    // Remove root level folder path
    dbutils.fs.rm(path, recurse = true)
    println("Completed back out Data in : " + path) 
  }
  catch {
    case e: Exception => println("Exception occurred in back out Delta : " + e)
  }
}

// COMMAND ----------

// DBTITLE 1,Back out data in processed and consolidated
val processedPath = "/mnt/" + clientFolder + "/processed/MA/Data/Provider/7.12/Provider"
val consolidatedPath = "/mnt/" + clientFolder + "/consolidated/MA/Data/Provider"   

backOutData(processedPath)
backOutData(consolidatedPath)

