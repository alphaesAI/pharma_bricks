// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("SynapseJSON","","")

val synapseJSON = dbutils.widgets.get("SynapseJSON")

// COMMAND ----------

// DBTITLE 1,Import libraries
import scala.collection.mutable

// COMMAND ----------

// DBTITLE 1,Call FileHandling notebook for helper methods.
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Call SynJSONCreatorClass
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Create initial and exploded dataframes
//Initial dataframe
val synapseDF = spark.read.json(Seq(synapseJSON).toDS)

//Exploded datagroups
val explodedDGs = synapseDF.select(explode($"DataGroups")).select(
              $"col.DataGroup"
             ,$"col.SynapseNotebook"
             ,$"col.Parameters"
              )

// COMMAND ----------

// DBTITLE 1,Explode one more time to remove an array level on parameters
var explodedParms = explodedDGs.select(
                    col("DataGroup")
                   ,col("SynapseNotebook")
                   ,col("Parameters.ClientContainer")(0).as("ClientContainer")
                   ,col("Parameters.ConsolidatedFolderPath")(0).as("ConsolidatedFolderPath")
                   ,explode($"Parameters").as("Parameters")
)

// COMMAND ----------

// DBTITLE 1,Create a parameter map column
//Get the parameters index
val index = explodedParms.schema.fieldIndex("Parameters")

//Get the parameters based on the index
val parmSchema = explodedParms.schema(index).dataType.asInstanceOf[StructType]

//Get list of columns for the mapping.  This creates the key value pairing
var columns = mutable.LinkedHashSet[Column]()
parmSchema.fields.foreach(field =>{
  columns.add(lit(field.name))
  columns.add(col("Parameters." + field.name))
})

//Adds the Map() KPV to the explodedParms dataframe
explodedParms = explodedParms.withColumn("ParameterMap",map(columns.toSeq:_*))
explodedParms = explodedParms.drop("Parameters")

// COMMAND ----------

// DBTITLE 1,Get current JobID
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

// COMMAND ----------

// DBTITLE 1,Execute each needed notebook based on the json input / dataframes
case class DataGroup(
         DataGroup: String 
        ,SynapseNotebook: String 
        ,ClientContainer: String
        ,ConsolidatedFolderPath: String 
        ,ParameterMap: Map[String, String]
)

case class ReturnedData(
         CurrentJobId: String 
        ,Status: String 
        ,ErrorMessage: String 
)

var rJSON = new synJSONCreator

rJSON.addBracketStart()

var iterator = 0;


explodedParms.as[DataGroup].take(explodedParms.count.toInt).foreach(t =>
          { 
println(s"Begin ${t.DataGroup}")
            
            var results = ""
            
            val mnt = "/mnt/"
            val path = s"${mnt}${t.ClientContainer}${t.ConsolidatedFolderPath}"
            val pathExists = path_exists(path)
             
            if(pathExists == true)
            {
               if (iterator != 0) {rJSON.addComma()}
              
              rJSON.addBraceStart()
              rJSON.addNewEntry("DataGroup", t.DataGroup)
              
              try{              
                 //run the notebook associated to the record
                 results = dbutils.notebook.run(t.SynapseNotebook, 0, t.ParameterMap)

                 //read output into a json table
                 val returnedJson = spark.read.json(Seq(results.toString).toDS)

println(results.toString)

                 returnedJson.as[ReturnedData].take(returnedJson.count.toInt).foreach(x =>
                          {
                                 rJSON.addNewEntry("CurrentJobId", x.CurrentJobId)
                                 rJSON.addNewEntry("Notebook",t.SynapseNotebook)
                                 rJSON.addNewEntry("Status", x.Status)      
                                 rJSON.addNewEntry("ErrorMessage",x.ErrorMessage, false)                                    
                          }
                 )
               }
               catch{ case e: Exception =>  {
                               rJSON.addNewEntry("CurrentJobId", "Undefined")
                               rJSON.addNewEntry("Notebook",t.SynapseNotebook)
                               rJSON.addNewEntry("Status", "FAILURE")
                               rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false) 
                   }  
               }
                rJSON.addBraceEnd()

                iterator+=1
            }
          }
)

rJSON.addBracketEnd()

val returnVal = rJSON.getJSON()
dbutils.notebook.exit(returnVal)
