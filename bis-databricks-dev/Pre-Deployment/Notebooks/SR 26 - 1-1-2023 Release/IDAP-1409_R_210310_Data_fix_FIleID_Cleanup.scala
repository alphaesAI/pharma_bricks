// Databricks notebook source
import io.delta.tables._
import org.apache.spark.sql.functions._
import spark.implicits._

//Get clientName
val clientName: String = "bcbsks"

var claimsPath: String = "/mnt/"+clientName+"/processed/MA/Data/Claims"
var df = spark.read.format("delta").load(claimsPath).filter($"File_ID"==="167")

if(df.count()>0)
  {
    val deltaTable = DeltaTable.forPath(spark, claimsPath)
    deltaTable.delete("FILE_ID = '167'")
  }


// COMMAND ----------

val claimsSetPath: String = "/mnt/"+clientName+"/processed/MA/Data/FCFCodeSet"

var df = spark.read.format("delta").load(claimsSetPath).filter($"File_ID"==="163")

if(df.count()>0)
  {
    val deltaTable = DeltaTable.forPath(spark, claimsSetPath)
    deltaTable.delete("FILE_ID = '163'")    
  }
