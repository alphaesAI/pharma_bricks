// Databricks notebook source
// DBTITLE 1,Setup Parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer") 

// COMMAND ----------

// DBTITLE 1,Call Synapse JSON Creator Class
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Setup Variables
val consolidatedPath = "/mnt/"+clientContainer+"/consolidated/MA/Data/ProviderHierarchy/"
val checkPoint = "/mnt/"+clientContainer+"/consolidated/MA/Data/ProviderHierarchy/Checkpoint-ProviderHierarchy"
val destTable = clientContainer.concat(".ProviderHierarchy")

// COMMAND ----------

// DBTITLE 1,Start Streaming to Publish Data From Delta into Synapse
var rJSON = new synJSONCreator
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

val SynapseNotebook = "./ExecuteStreaming"

try{   
   var result = dbutils.notebook.run(SynapseNotebook, 0, Map( 
                                                     "ConsolidatedPath" -> consolidatedPath 
                                                     ,"DestTable" -> destTable
                                                     ,"CheckPoint" -> checkPoint)
                                    )
  
  if (result == null) {result = "Success"}
  
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