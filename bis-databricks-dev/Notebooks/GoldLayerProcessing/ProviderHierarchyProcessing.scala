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

val ConsolidatePath = "/mnt/"+ Container + "/consolidated/MA/Data/ProviderHierarchy"
val GoldPath = "/mnt/"+ Container + "/Gold/MA/Client/ProviderHierarchy"

val df_orig = spark.read.format("delta").load(ConsolidatePath)
df_orig.createOrReplaceTempView("df_orig_vw")

val PathToDelete = "/mnt/" + Container + "/Gold/MA/Client/ToDelete"
val df_latest = spark.sql(""" select a.* from df_orig_vw a join (select max(FileID) as max_FileID from df_orig_vw)b on a.FileID = b.max_FileID """)
if(path_exists(GoldPath) == true){dbutils.fs.mv(GoldPath, PathToDelete,true)}
df_latest.write.format("delta").save(GoldPath)
/*
val df_latest = spark.sql(""" select * from (select a.*, row_number() over(partition by a.ProviderID order by ProviderID) as rownum 
                            from df_orig_vw a join (select max(FileID) as max_FileID from df_orig_vw)b on a.FileID = b.max_FileID)der where rownum=1 """).drop($"rownum")
                      .repartition(df_orig.rdd.getNumPartitions)

if(path_exists(GoldPath+"/_delta_log") == false){  // gold layer table not created yet
  df_latest.write.format("delta").save(GoldPath)
 }
else{
  println("merge logic for gold layer table")
  
  val df_tgt = spark.read.format("delta").load(GoldPath)
  
  val df_src_hash = df_latest.withColumn("HashVal",hash(concat_ws("|",
                df_latest.columns
               .filter(x => !(x.equals("ClientID") || x.equals("FileID") || x.equals("LoadDateTime") || x.equals("FileLayoutID") || x.equals("FileLayoutDescription")))
               .map(c => col(c)):_*)))
  
  val df_tgt_hash = df_tgt.withColumn("HashVal",hash(concat_ws("|",
                df_tgt.columns
               .filter(x => !(x.equals("ClientID") || x.equals("FileID") || x.equals("LoadDateTime") || x.equals("FileLayoutID") || x.equals("FileLayoutDescription")))
               .map(c => col(c)):_*)))
  
  val df_ins_upd = df_src_hash.join(df_tgt_hash, df_src_hash("ProviderID") === df_tgt_hash("ProviderID"), "left_outer")
                              .filter(df_tgt_hash("ProviderID").isNull || df_src_hash("HashVal") =!= df_tgt_hash("HashVal"))
                              .select(df_src_hash.col("*")).drop($"HashVal")
  //merging into taget delta table
  if(df_ins_upd.count()>0)
  {
    println("updating gold layer table")
      DeltaTable.forPath(spark,GoldPath)
        .as("tgt_delta_tbl")
        .merge(df_ins_upd.as("updates"),"tgt_delta_tbl.ProviderID = updates.ProviderID")
        .whenMatched().updateAll()
        .whenNotMatched().insertAll()
        .execute()
  }
  else
  {
    println("no changes found to be applied in gold layer")
  }
} 
 */

