// Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("GroupConfigPath","","")

// COMMAND ----------

val clientContainer = dbutils.widgets.get("ClientContainer") //"fileconfig/JSON/Gold/GoldLayerGrouping.json"
val configPath = dbutils.widgets.get("GroupConfigPath")

val mountPoint = "/mnt/"

val fullConfigPath = mountPoint + configPath

// COMMAND ----------

import org.apache.spark.sql.functions._

// COMMAND ----------

val layerJsonExtracted = spark.read.format("json").option("multiline", "true").load(fullConfigPath)
val explodedLayer = layerJsonExtracted.select(explode($"LayerGrouping")).select(
              $"col.LayerOrder"
             ,$"col.LayerGrouping" 
             ,$"col.SubGrouping" 
              )

case class subGroupReferences(
         SubGroupEntity: String
        ,SubGroupingOrder: Long
        ,SubConfigPath: String
        ,Notebook: String
)

case class GroupReferences(
         LayerOrder: Long
        ,LayerGrouping: String
        ,SubGrouping: Array[subGroupReferences]
)

// COMMAND ----------

explodedLayer.filter((lit(clientContainer) === "global" && explodedLayer("LayerGrouping") === "GlobalRefData") || (lit(clientContainer) =!= "global" && explodedLayer("LayerGrouping") =!= "GlobalRefData")).sort($"LayerOrder").as[GroupReferences].take(explodedLayer.count.toInt).foreach(t =>
          {
            val layerGrouping = t.LayerGrouping
            
            val explodedSubGroups = explodedLayer.select(explode($"SubGrouping")).filter($"LayerGrouping" === layerGrouping).select(
              $"col.SubGroupEntity"
             ,$"col.SubGroupingOrder" 
             ,$"col.SubConfigPath" 
             ,$"col.Notebook" 
              )
// explodedSubGroups.show()            
            explodedSubGroups.sort($"SubGroupingOrder").as[subGroupReferences].take(explodedSubGroups.count.toInt).foreach(s =>
            {
// println(s.SubGroupEntity)
              val notebook = s.Notebook
              val subGroupPath = s.SubConfigPath
              
              val results = dbutils.notebook.run(notebook, 0, Map("ClientContainer" -> clientContainer, "SubGroupConfigPath" -> subGroupPath))
            })
      }//End of foreach
)
val returnVal = "Completed"
dbutils.notebook.exit(returnVal)
