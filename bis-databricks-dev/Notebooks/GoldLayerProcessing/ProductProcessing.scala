// Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

val Container = dbutils.widgets.get("ClientContainer")

// COMMAND ----------

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

import  org.apache.hadoop.fs.{FileSystem,Path}

def path_exists(pathToCheck: String): Boolean =
{ 
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val IsExists = fs.exists(new org.apache.hadoop.fs.Path(pathToCheck)) 
  return IsExists 
}

// COMMAND ----------

val ConsolidatePath = "/mnt/"+ Container + "/consolidated/MA/Data/Product"
val GoldPath = "/mnt/"+ Container + "/Gold/MA/Client/Product"
val PathToDelete = "/mnt/" + Container + "/Gold/MA/Client/ToDelete"

if(path_exists(ConsolidatePath) == true){
val df_orig = spark.read.format("delta").load(ConsolidatePath)
df_orig.createOrReplaceTempView("df_orig_vw")

val df_latest = spark.sql(""" select a.* from df_orig_vw a join (select max(FileID) as max_FileID from df_orig_vw)b on a.FileID = b.max_FileID """)
if(path_exists(GoldPath) == true){dbutils.fs.mv(GoldPath, PathToDelete,true)}
df_latest.write.format("delta").save(GoldPath)
}

