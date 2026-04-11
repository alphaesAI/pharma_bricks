// Databricks notebook source
// DBTITLE 1,Create and setup parameters
//Actual File Parameters
dbutils.widgets.text("FileId","","") //0  
//Current folder path for the file
dbutils.widgets.text("CurrentContainer","","") //validate
dbutils.widgets.text("CurrentFolderPath","","") ///MA/Internal/FCF/2020/05/06/ 
//DataModel
dbutils.widgets.text("ConsolidatedLayerDataModel","","") //
dbutils.widgets.text("ConsolidatedLayerDataModelFilePath","","") //
//FileLayout to DataModel mapping
dbutils.widgets.text("ConsolidatedMappingFileName","","") //
dbutils.widgets.text("ConsolidatedMappingFilePath","","") //

//ConsolidatedFolderPath -- may put this into the json schema for mappings
dbutils.widgets.text("ConsolidatedFolderPath","","")   //proessed 

val MountPoint = "/mnt/"
val FileId = dbutils.widgets.get("FileId")   
val CurrentContainer = dbutils.widgets.get("CurrentContainer") 
val CurrentFolderPath = dbutils.widgets.get("CurrentFolderPath")   
val ConsolidatedLayerDataModel = dbutils.widgets.get("ConsolidatedLayerDataModel") 
val ConsolidatedLayerDataModelFilePath = dbutils.widgets.get("ConsolidatedLayerDataModelFilePath") 
val ConsolidatedMappingFileName = dbutils.widgets.get("ConsolidatedMappingFileName") 
val ConsolidatedMappingFilePath = dbutils.widgets.get("ConsolidatedMappingFilePath")
val ConsolidatedFolderPath = dbutils.widgets.get("ConsolidatedFolderPath")


//Processed Folder Path (will have all FileIds in them)
val FullProcessed = MountPoint + CurrentContainer + CurrentFolderPath + "/"
val FullConsolidatedFolderPath = MountPoint + ConsolidatedFolderPath + "/"
val DataModelFile = MountPoint + ConsolidatedLayerDataModelFilePath + "/" + ConsolidatedLayerDataModel
val ConsolidationMapping = MountPoint + ConsolidatedMappingFilePath + "/" + ConsolidatedMappingFileName

// COMMAND ----------

// DBTITLE 1,Call libraries
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

// DBTITLE 1,Call FileHandling Notebook
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Call GetTypes Notebook
// MAGIC %run "../CommonMethods/ABC/GetTypes"

// COMMAND ----------

// DBTITLE 1,Call UDF Notebook
// MAGIC %run "../CommonMethods/ABC/CreateUserDefinedFunctions"

// COMMAND ----------

// DBTITLE 1,Map Select Expr Columns (returns for select converts to DataModel)
case class selectColumns(
          FieldName: String
         ,DataType: String
         ,Ordinal: String
         ,SourceColumn: String
         ,DestinationColumn: String
         ,SourceColumnFormat: String 
         ,ColumnQuery: String
) 

def getSelectExpr (cols: DataFrame): Array[String] = {
  
var SQLCommand = ""
var iterator = 0
val doubleQuote = """ " """.trim()
val singleQuote = """ ' """.trim()

cols.as[selectColumns].take(cols.count.toInt).foreach(t =>
        {    
          val FieldName =	t.FieldName
          val DataType =	t.DataType
          val Ordinal =	t.Ordinal
          val SourceColumn =	t.SourceColumn
          val DestinationColumn =	t.DestinationColumn
          val SourceColumnFormat =	t.SourceColumnFormat
          val ColumnQuery =	t.ColumnQuery  
          
          
          if(iterator != 0)
          {
            SQLCommand = SQLCommand + "!" //split command for SQL select expr
          }
          
          if(ColumnQuery != null && !ColumnQuery.isEmpty()){
                SQLCommand = SQLCommand + "NULLIF(CAST(" + ColumnQuery + " AS " +  getSQLType(DataType) + "),'') AS " + DestinationColumn
          }else if(DataType == "DateType" && SourceColumnFormat != ""){ 
                SQLCommand = SQLCommand + "to_date(" + SourceColumn + "," + singleQuote + SourceColumnFormat + singleQuote + ")  AS " + DestinationColumn 
          }else if(DataType == "TimestampType" && SourceColumnFormat != ""){ 
                SQLCommand = SQLCommand + "to_timestamp(" + SourceColumn + "," + singleQuote + SourceColumnFormat + singleQuote + ")  AS " + DestinationColumn 
          }else{
                SQLCommand = SQLCommand + "CAST(" + SourceColumn + " AS " +  getSQLType(DataType) + ")  AS " + DestinationColumn
          } 

           iterator = iterator + 1
        }
      ) 
  return SQLCommand.split("!")
}


// COMMAND ----------

// DBTITLE 1,Map Select Columns (returns for select converts to DataModel)
def getSelect (cols: Array[Row]): Array[org.apache.spark.sql.Column] = {
    val arrayMap = scala.collection.mutable.LinkedHashMap[String,String]()
    val colAlias = cols.foreach(x=> arrayMap += (x(3).toString ->x(4).toString))
    val selCols = cols.map(name => arrayMap.get(name(3).toString) match { 
                            case Some(newname) => {
                                      if(name(1) == "DateType" && name(5).toString != ""){
                                          to_date(col(name(3).toString), name(5).toString).as(newname).cast(getDataType(name(1)))
                                      }else{
                                          col(name(3).toString).as(newname).cast(getDataType(name(1)))
                                      } 
                                    }
                            case None => col(name(3).toString).cast(getDataType(name(1)))
                                     }
                                 )
  return selCols
}

// COMMAND ----------

// DBTITLE 1,Add to meet Required Columns from DataModel
def customSelect(availableCols: List[String], requiredCols: List[String]) = {
      requiredCols.map(column => column match {
            case column if availableCols.contains(column) => col(column)
            case _ => lit(null).as(column)
      })
}

// COMMAND ----------

// DBTITLE 1,Gather File specific Mappings and DataModel for File, Copy Dataframe to Delta Parquet Format into Consolidated Zone
var rJSON = ""
val doubleQuote = """ " """.trim()
var ErrorMessage = "";

try{
  //Get notebook context -- to get RunId and JobId
  val ctx = dbutils.notebook.getContext 
  //val currentRunId = ctx.currentRunId.toString.replace("Some(RunId(","").replace(")","")//Always there in the return json  
  val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

  rJSON += "{" 
  //rJSON += doubleQuote + "CurrentRunId"  + doubleQuote + ":"  + doubleQuote + currentRunId.toString + doubleQuote
  //rJSON += "," 
  rJSON += doubleQuote + "CurrentJobId"  + doubleQuote + ":"  + doubleQuote + currentJobId.toString + doubleQuote 
  rJSON += ","
  
  //Load DataModel JSON into Dataframe
  val tempDataModel = spark.read.format("json").option("multiline", "true").load(DataModelFile)
  val dataModel = tempDataModel.select(explode($"Fields")).select($"col.FieldName",$"col.DataType", $"col.Ordinal") 
  //create the destination schema from the datamodel
  val destSchema = getStruct(dataModel)
  //Create an empty DataFrame with the datamodel
  var dfDataModel = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], destSchema) 
  //load ConsolidatedMapping file
  val ConsolidatedMappings = spark.read.format("json").option("multiline", "true").load(ConsolidationMapping)
  //select out RecordType and selectColumns
  val tempMappings = ConsolidatedMappings.select(explode($"columnMapping")).select($"col.recordType",$"col.selectColumns")
  //Explode RecordType
  val sRecordType = tempMappings.select(explode($"recordType")).select($"col.Field",$"col.Value")
  //Explode selectColumns
  val sColumns = tempMappings.select(explode($"selectColumns")).select($"col.SourceColumn",$"col.DestinationColumn", $"col.SourceColumnFormat", $"col.ColumnQuery")

  //merge mapping columns to datamodel based on Destination column
  val seqColumns = dataModel
    .join(sColumns, dataModel("FieldName") === sColumns("DestinationColumn"),"inner")
    .select(
          dataModel("FieldName"), 
          dataModel("DataType"), 
          dataModel("Ordinal"), 
          sColumns("SourceColumn"), 
          sColumns("DestinationColumn"),
          sColumns("SourceColumnFormat"), 
          sColumns("ColumnQuery")
        )

  val selCols = getSelectExpr(seqColumns.select("FieldName" ,"DataType" ,"Ordinal" ,"SourceColumn" ,"DestinationColumn" ,"SourceColumnFormat" ,"ColumnQuery"))

  //Create a Row array from selectColumns
  //val selectArray: Array[Row] = seqColumns.select("FieldName", "DataType", "Ordinal","SourceColumn","DestinationColumn", "SourceColumnFormat").collect()
  //Convert RowArray into ColumnArray
  //val selCols = getSelect(selectArray)

  //Create filter expression
  val newType: Row = sRecordType.select("Field","Value").collect().last
  //make filter expression dynamic
  val Field = if(newType(0).toString == ""){"FileId"}else{newType(0).toString}
  val Value = if(newType(1).toString == ""){FileId}else{newType(1).toString}

  //Load parq file into dataframe remapping the columns to the selCols. Filtering on FileID.
  val dfFileReformatted = spark.read.format("parquet").load(FullProcessed)
                   //.select(selCols:_*) //Convert Columns first so that they are always FileID
                   .selectExpr(selCols:_*)
                   .filter($"FileID" === FileId)
                   .filter(col(Field) === Value)
                   //.withColumn("LoadDateTime",to_date(current_timestamp(), "MM/dd/yyyy HH:mm:ss"))

  //Union file into the data model created earlier to enforce datatypes and layout
  val dfFile =  dfDataModel
                        .union(
                                 dfFileReformatted 
                                    .select(customSelect(
                                                   dfFileReformatted.columns.toList, //Available columns
                                                   dfDataModel.columns.toList //Required Columns 
                                                   ):_*)
                              )

  //Check the data
  //dfFileReformatted.createOrReplaceTempView("FileData")  
  //dfFile.createOrReplaceTempView("FileConvertedData") 
  
  //write file to delta with mergeSchema = true
  if (dfFile.rdd.isEmpty == false)
  {
    dfFile.write.format("delta").option("mergeSchema", "true").mode("append").save(FullConsolidatedFolderPath) 
  }
  
  rJSON += doubleQuote + "ConsolidatedCount"  + doubleQuote + ":"  + doubleQuote + dfFile.count().toString + doubleQuote 
  rJSON += "," 
  rJSON += doubleQuote + "Status"  + doubleQuote + ":"  + doubleQuote + "SUCCESS" + doubleQuote  
  rJSON += "," 
  rJSON += doubleQuote + "ErrorMessage"  + doubleQuote + ":"  + doubleQuote + "" + doubleQuote 
}
catch {
      case e: Throwable =>  { 
        rJSON += doubleQuote + "ConsolidatedCount"  + doubleQuote + ":"  + doubleQuote + 0 + doubleQuote  
        rJSON += "," 
        rJSON += doubleQuote + "Status"  + doubleQuote + ":"  + doubleQuote + "FAILED" + doubleQuote 
        rJSON += "," 
        rJSON += doubleQuote + "ErrorMessage"  + doubleQuote + ":"  + doubleQuote + StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,"") + doubleQuote 
    }
}
finally{ 
  rJSON += "}"
  dbutils.notebook.exit(rJSON)
}
