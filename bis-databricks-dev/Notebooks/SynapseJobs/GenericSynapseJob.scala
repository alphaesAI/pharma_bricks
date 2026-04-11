// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
dbutils.widgets.text("SynapseTableName","","") //"Member"
dbutils.widgets.text("ConsolidatedLayerDataModel","","") //"MemberDataModel.json"
dbutils.widgets.text("ConsolidatedFolderPath","","") //"devidap1/consolidated/MA/Data/Member"

val clientContainer = dbutils.widgets.get("ClientContainer")
val synapseTableName = dbutils.widgets.get("SynapseTableName")
val consolidatedLayerDataModel = clientContainer + "/fileconfig/JSON/Consolidation/DataModels/" + dbutils.widgets.get("ConsolidatedLayerDataModel") 
val consolidatedFolderPath = dbutils.widgets.get("ConsolidatedFolderPath") //"/consolidated/MA/Data/Member"
val consolidatedPath = "/mnt/" + clientContainer + consolidatedFolderPath

//streaming values
val destTable = clientContainer.concat(".").concat(synapseTableName)//"devidap1.Member"
val checkPoint = consolidatedPath + "/Checkpoint-" + synapseTableName 

// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Call streaming to publish data from delta into synapse
var rJSON = new synJSONCreator
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId) 

val SynapseNotebook = "./ExecuteTruncateAndLoad"

try{   
   var result = dbutils.notebook.run(SynapseNotebook, 0, Map( 
                                                      "ClientContainer" -> clientContainer
                                                     ,"ConsolidatedPath" -> consolidatedPath 
                                                     ,"DestTable" -> destTable
                                               )
                                    )
  
  if (result == null) {result = "SUCCESS"}
  
  rJSON.addNewEntry("Status", result)
  rJSON.addNewEntry("ErrorMessage", "", false) 
}
catch {
    case unknown: Exception => { 
        rJSON.addNewEntry("Status", "FAILURE")
        rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(unknown.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false) 
      }
}
finally{
    rJSON.addBraceEnd()  
    dbutils.notebook.exit(rJSON.getJSON()) 
}

