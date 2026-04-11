// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
dbutils.widgets.text("ConfigPath","","")

val clientContainer = dbutils.widgets.get("ClientContainer")
val configPath = dbutils.widgets.get("ConfigPath")

val mountPoint = "/mnt/"
val fullConfigPath = mountPoint + configPath

// COMMAND ----------

// DBTITLE 1,Import libraries
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions.{explode, lit}
// import org.apache.spark.sql.functions.explode

// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Create initial and exploded dataframes
//Initial dataframe
val synapseJsonExtracted = spark.read.format("json").option("multiline", "true").load(fullConfigPath)

val explodedSynapse = synapseJsonExtracted.select(explode($"Synapse")).select(
              $"col.ClientOrder"
             ,$"col.ClientGrouping" 
             ,$"col.SubGrouping" 
              )

case class SynapseProcess(
         ClientOrder: Long 
        ,ClientGrouping: String
        ,SubGrouping: Array[String]
)

case class subSynapseProcess(
         TableName: String 
        ,ProcessingOrder: Long 
        ,Datamodel: String
        ,SourcePath: String 
        ,SynpaseNotebook: String
)

// COMMAND ----------

// DBTITLE 1,Get current JobID
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

// COMMAND ----------

// DBTITLE 1,Call streaming to publish data from delta into synapse
var rJSON = new synJSONCreator

rJSON.addBracketStart()
var iterator = 0;

// determines which section in the JSON to use (Client or Global)
explodedSynapse.filter((lit(clientContainer) === "global" && explodedSynapse("ClientGrouping") === "GlobalRefData") || (lit(clientContainer) =!= "global" && explodedSynapse("ClientGrouping") =!= "GlobalRefData")).sort($"ClientOrder").as[SynapseProcess].take(explodedSynapse.count.toInt).foreach(t =>
    { 

   val clientGrouping = t.ClientGrouping
            
    //Exploded subgroups within the ClientGrouping
    val explodedSubGroup = explodedSynapse.select(explode($"SubGrouping")).filter($"ClientGrouping" === clientGrouping).select(
                  $"col.TableName"
                 ,$"col.ProcessingOrder"
                 ,$"col.Datamodel"
                 ,$"col.SourcePath"
                 ,$"col.SynpaseNotebook"
                  )
   
     explodedSubGroup.sort($"ProcessingOrder").as[subSynapseProcess].take(explodedSubGroup.count.toInt).foreach(s =>
            {
     
            println(s"Begin ${s.TableName}")

            rJSON.addBraceStart()
            rJSON.addNewEntry("CurrentJobId", currentJobId) 


            //streaming values
            val synapseNotebook = s"./${s.SynpaseNotebook}"
            val sourcePath = s"${mountPoint}${clientContainer}${s.SourcePath}"
            val destTable = clientContainer.concat(".").concat(s.TableName) //"devidap1.Member"
            val checkPoint = s"${sourcePath}/Checkpoint-${s.TableName}" 

            try{   
                 var result = dbutils.notebook.run(synapseNotebook, 0, Map( 
                                                                    "ClientContainer" -> clientContainer
                                                                   ,"ConsolidatedPath" -> sourcePath 
                                                                   ,"DestTable" -> destTable
                                                                   ,"CheckPoint" -> checkPoint)
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
                rJSON.addBraceEnd()

                iterator+=1
          }
        )
    }
)           
rJSON.addBracketEnd()

val returnVal = rJSON.getJSON()
dbutils.notebook.exit(returnVal)
