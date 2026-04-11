// Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

// COMMAND ----------

val clientContainer = dbutils.widgets.get("ClientContainer")
val subGroupConfigPath = dbutils.widgets.get("SubGroupConfigPath")

val mountPoint = "/mnt/"

val fullConfigPath = mountPoint + subGroupConfigPath

// COMMAND ----------

import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Import aux notebooks *****FIX Client stuff
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

val SubGroupJsonExtracted =  spark.read.format("json").option("multiline", "true").load(fullConfigPath)
val explodedSubGroup = SubGroupJsonExtracted.select(explode($"SubLayerProcessing")).select(
              $"col.SubGroupEntity" 
             ,$"col.DestinationTable"
             ,$"col.SourceTables"
             ,$"col.SQLScript"
             ,$"col.DupScript"
             ,$"col.MergeScript" 
              )

case class TableReferences(
            Entity: String
            ,SourceTable: String
            ,SourceFormat: String
)

case class EntityReferences(
            SubGroupEntity: String
            ,DestinationTable: String
            ,SourceTables: Array[TableReferences]
            ,SQLScript: String
            ,DupScript: String
            ,MergeScript: String
)

// COMMAND ----------

/*
  Make it so the source is optional -- reason dimDate / dimMonth
  Figure out how to make it run in order
  Test Stuff
*/
explodedSubGroup.as[EntityReferences].take(explodedSubGroup.count.toInt).foreach(e =>
          {
            val subGroupEntity = e.SubGroupEntity
            //Operation canceler.  used to determine if all sources are defined
            var c = true
            
            //Check Destination Path
            val DestinationPath = mountPoint + e.DestinationTable.replaceAll("#clientCode",clientContainer) 

            val b = path_exists(DestinationPath)
            
            val explodedSourceTables = explodedSubGroup.filter($"SubGroupEntity" === subGroupEntity).select($"SubGroupEntity", explode($"SourceTables"))
            .select(
              $"SubGroupEntity"
             ,$"col.Entity"
             ,$"col.SourceTable"
             ,$"col.SourceFormat"
              )
            
            //Loop through and Load SourceTable
            explodedSourceTables.as[TableReferences].take(explodedSourceTables.count.toInt).foreach(t =>
            {
                //Check Source Path
                val SourcePath = mountPoint + t.SourceTable.replaceAll("#clientCode",clientContainer) 
                val a = path_exists(SourcePath)

                //Check if Sources Exist and if not flag c to false.
                if(a == true){
                    val dfFile = spark.read.format(t.SourceFormat).option("header", "true").load(SourcePath) 
                    dfFile.createOrReplaceTempView(t.Entity) //create view to run sql querries on 
                    println(t.Entity + " temp view created")
                  }
                 else{
                   c = false
                   println("Folder path(s) for " + t.Entity + " does not exist")
                 }
            }
            )
            
            if (c == true) {
                //Run SQL Script
                val mainSQLQuery = e.SQLScript.replaceAll("#clientCode",clientContainer)
                val sqlContext = spark.sqlContext
                val mDF = sqlContext.sql(mainSQLQuery).cache()
                mDF.createOrReplaceTempView("tempSQLScript") //do not remove the FinalOutput will use this
                println("tempSQLScript temp view created")
             
                if (sqlContext.sql(e.DupScript).count() >= 1){
                    throw new Exception("duplicates in source query result")
                }
                
                //load datamodel
                val finalDataModel = spark.read.format("delta").option("header", "true").load(DestinationPath) //on disk
                finalDataModel.createOrReplaceTempView("DestinationTable") //do not remove the FinalOutput will use this --pointer to the disk -- so that it can be used in sql
              
                //Run Merge script to destination
                val MergeScript = e.MergeScript //.replace("DestinationTable", finalDataModel)
                val fsqlContext = spark.sqlContext 
                fsqlContext.sql(MergeScript)
                
             }
             else {
              val ErrorMessage = "Folder path(s) do not exist: See above"
              //throw new Exception(ErrorMessage);
             }
          }
 )
 
