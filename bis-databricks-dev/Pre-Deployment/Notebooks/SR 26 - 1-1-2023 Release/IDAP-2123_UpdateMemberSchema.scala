// Databricks notebook source
// DBTITLE 1,Imports
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._ 
import io.delta.tables._ 

// COMMAND ----------

// DBTITLE 1,Setup Environment Specific Variables
//Create environment variable to handle the database connection
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var blobKey = ""

var envUser="_ETLUSER_SQL"

if (dbEnv == "934226345849410") {envLetter = "d";envUser = "DEV"+envUser}
else if (dbEnv == "5826678703751685") {envLetter = "q"; envUser = "QA"+envUser}
else if (dbEnv == "7093677384385470") {envLetter = "s"; envUser = "STG"+envUser}
else {envLetter = "p";envUser = "PRD"+envUser} 

if (dbEnv == "934226345849410") {blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="}

// COMMAND ----------

// DBTITLE 1,Gather Clients for Environments
val doubleQuote = """ " """.trim()
val singleQuote = """ ' """.trim()

var clientContainers = ""

if(envLetter == "d"){
clientContainers = """{
                "Clients": [
                  "devidap1",
                  "devidap2"
                ]
              } 
            """ 
}
else if (envLetter == "q"){
clientContainers = """{
                "Clients": [
                  "qaidap1",
                  "qaidap2"
                ]
              } 
            """ 
}
else if (envLetter == "s"){
clientContainers =  """{
                "Clients": [
                  "bcbsks",
                  "bcbsm",
                  "vba",
                  "nbnd"
                ]
              } 
            """
}
else if (envLetter == "p"){
clientContainers = """{
                "Clients": [
                  "bcbsks",
                  "bcbsm",
                  "vba",
                  "nbnd"
                ]
              } 
            """
}

val dfEnvClients = spark.read.json(Seq(clientContainers).toDS())
val explodedClients = dfEnvClients.select(explode($"Clients")).selectExpr("col AS ClientCode")
case class Clients(ClientCode:String)

// COMMAND ----------

// DBTITLE 1,Check if Path Exists
def path_exists(path: String): Boolean =
{
  var state = false
  try {
    dbutils.fs.ls(path)
    state = true
      } 
    catch {
            case ex: java.io.FileNotFoundException => {
            println(s"Filepath: " + path +  s"  not found")
            state = false 
            }
         }
  return state
}

// COMMAND ----------

// DBTITLE 1,Method: Alter table Schema in consolidated and processed delta lake for member files
def renameColumns(ClientCode: String): Boolean = {
          val memberProcessedPath = "/mnt/" + ClientCode + "/processed/MA/Data/Member/7.12"
          val memberConsolidatedPath = "/mnt/" + ClientCode + "/consolidated/MA/Data/Member"          
          val memberConsolidatedCheckpointPath = "/mnt/" + ClientCode + "/consolidated/MA/Data/Member/Checkpoint-Member/"
  
          val processedExists = path_exists(memberProcessedPath)
          val consolidatedExists = path_exists(memberConsolidatedPath)
          val checkpointExists = path_exists(memberConsolidatedCheckpointPath)
  
          if(processedExists == true){  
                    //renamed the cols in processed delta 
                   spark.read.format("delta").load(memberProcessedPath)
                    .withColumnRenamed("ENROLEEEDUCATION", "ENROLLEEEDUCATION")
                    .withColumnRenamed("ENROLEEEMPLOYMENT", "ENROLLEEEMPLOYMENT")
                    .write
                    .format("delta")
                    .mode("overwrite")
                    .option("overwriteSchema", "true")
                    .save(memberProcessedPath)
          }
          if(consolidatedExists == true){  
                    //renamed the cols in consolidated delta 
                    spark.read.format("delta").load(memberConsolidatedPath)
                      .withColumnRenamed("BillingAddreessLine1", "BillingAddressLine1")
                      .withColumnRenamed("BillingAddreessLine2", "BillingAddressLine2")
                      .withColumnRenamed("BillingAddreessLine3", "BillingAddressLine3")
                      .withColumnRenamed("CaretakerMiddleIntial", "CaretakerMiddleInitial")
                      .write
                      .format("delta")
                      .mode("overwrite")
                      .option("overwriteSchema", "true")
                      .save(memberConsolidatedPath) 
          }
          // Remove the checkpoint-member folder in consolidated
          if(checkpointExists == true){  
                    // remove all the files in the folder
                    dbutils.fs.ls(memberConsolidatedCheckpointPath)
                      .map(_.name)
                      .foreach((file: String) => dbutils.fs.rm(memberConsolidatedCheckpointPath + file, true))
                    // remove the folder
                    dbutils.fs.rm(memberConsolidatedCheckpointPath, true)
          }
  return true
}

// COMMAND ----------

// DBTITLE 1,Method : executeScripts
def executeScripts(Record: org.apache.spark.sql.Row): Boolean = {
          val clientCode = Record(0).toString
//           println(clientCode)
          
          renameColumns(clientCode)         
    return true
}

// COMMAND ----------

// DBTITLE 1,Run Scripts
explodedClients.collect().foreach(row => executeScripts(row))
