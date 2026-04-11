// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer") 

val consolidatedPath = "/mnt/"+clientContainer+"/consolidated/MA/Data/MMR"
val checkPoint = "/mnt/"+clientContainer+"/consolidated/MA/Data/MMR/Checkpoint-MMR/"
val destTable = clientContainer.concat(".CMS_MMR")

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

val SynapseNotebook = "./ExecuteStreaming-MMR"

try {
   var result = dbutils.notebook.run(SynapseNotebook, 0, Map( 
                                                      "ClientContainer" -> clientContainer
                                                     ,"ConsolidatedPath" -> consolidatedPath 
                                                     ,"DestTable" -> destTable
                                                     ,"CheckPoint" -> checkPoint)
                                    )
  
  if (result == null) {result = "SUCCESS"}
  
  rJSON.addNewEntry("Status", result)
  rJSON.addNewEntry("ErrorMessage", "", false) 
}
catch{
      case e: Throwable =>  {
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
    }
}
finally{
    rJSON.addBraceEnd()  
    dbutils.notebook.exit(rJSON.getJSON()) 
}
