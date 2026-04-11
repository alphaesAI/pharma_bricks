// Databricks notebook source
//File Parameters
dbutils.widgets.text("FileId","","") //0 
dbutils.widgets.text("FileLayoutDescription","","") //0 
dbutils.widgets.text("CurrentContainer","","") //validate
dbutils.widgets.text("CurrentFolderPath","","") ///MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("ConversionType","","")
dbutils.widgets.text("FileName","","") //PBC_VIS_FCF_prod_20200227070003.TXT
dbutils.widgets.text("Delimiter","","") //"|"
dbutils.widgets.text("ConversionJsonContainer","","")   //fileconfig
dbutils.widgets.text("ConversionJsonFolderPath","","") // /JSON/Conversion
dbutils.widgets.text("ConversionJsonFileName","","") //lishist_conversion.json
dbutils.widgets.text("HasControlFile","","") //lishist_conversion.json

                     
//capture values passed into from ADF
val fileId = dbutils.widgets.get("FileId") 
val FileLayoutDescription = dbutils.widgets.get("FileLayoutDescription") 
val currentContainer = dbutils.widgets.get("CurrentContainer") 
val currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
val fileName = dbutils.widgets.get("FileName") 
val delimiter = dbutils.widgets.get("Delimiter")
val conversionType = dbutils.widgets.get("ConversionType")
val conversionJsonContainer = dbutils.widgets.get("ConversionJsonContainer") 
val conversionJsonFolderPath: String = dbutils.widgets.get("ConversionJsonFolderPath") 
val conversionJsonFileName = dbutils.widgets.get("ConversionJsonFileName")
val hasControlFile = dbutils.widgets.get("HasControlFile")

//create folder and file variables
val mountPoint = "/mnt/"
val blobPath = mountPoint + currentContainer + "blob" //blob storage reference
val toProcessPath = blobPath + currentFolderPath 
val dataFilePath = toProcessPath + "/" + fileName //datafile reference
val conversionJsonPath = mountPoint + conversionJsonContainer + conversionJsonFolderPath + "/" +  conversionJsonFileName //conversion json reference

var convertedFilePath = ""

if(conversionType == "Generic"){
  convertedFilePath = blobPath + "/ConvertedFiles/" + FileLayoutDescription 
}
else{
  convertedFilePath = blobPath + "/ConvertedFiles/" + conversionType 
}

val fullconvertedFilePath = convertedFilePath + "/" + fileName

val controlFileName = fileName+".ctl"
val controlFilePath = convertedFilePath + "/" + controlFileName
val fullcontrolFilePath = controlFilePath + "/" + controlFileName
val ctlProcessPath = toProcessPath + "/" + controlFileName

var returnJSON: String  = ""

// COMMAND ----------

var noteBook = ""

if (conversionType == "HICN_MBI")
  {noteBook = "../Conversion/HICNMBIConversion"}

if (conversionType == "LISHIST")
  {noteBook = "../Conversion/LISHISTConversion"}

if (conversionType == "MAO002")
  {noteBook = "../Conversion/MAO002Conversion"}

if (conversionType == "MAO004")
  {noteBook = "../Conversion/MAO004Conversion"}

if (conversionType == "MMR")
  {noteBook = "../Conversion/MMRConversion"}

if (conversionType == "MOR")
  {noteBook = "../Conversion/MORConversion"}

if (conversionType == "MORD")
  {noteBook = "../Conversion/MORDConversion"}

if (conversionType == "PDERETURN")
  {noteBook = "../Conversion/PDEReturnConversion"}

if (conversionType == "RAPS_RETURN")
  {noteBook = "../Conversion/RAPSReturnConversion"}

if (conversionType == "MEMSD")
  {noteBook = "../Conversion/MEMSDConversion"}

if (conversionType == "PPRD")
  {noteBook = "../Conversion/PPRDConversion"}

if (conversionType == "DTRRD")
  {noteBook = "../Conversion/DTRRDConversion"}

if (conversionType == "Generic")
  {noteBook = "../Conversion/GenericConversion"}

if (conversionType == "OMIGPAL")
  {noteBook = "../Conversion/OMIGPALConversion"}

if (conversionType == "HEDIS")
  {noteBook = "../Conversion/HEDISConversion"}

if (conversionType == "Submitted837OutboundClaims")
  {noteBook = "../Conversion/Submitted837OutboundClaimsConversion"}

// COMMAND ----------

var returnJSON = dbutils.notebook.run(noteBook,0,Map("FileId"->fileId
                                    ,"FileLayoutDescription"->FileLayoutDescription
                                    ,"CurrentContainer"->currentContainer
                                    ,"CurrentFolderPath"->currentFolderPath
                                    ,"FileName"->fileName 
                                    ,"Delimiter"->delimiter
                                    ,"ConversionType"->conversionType
                                    ,"ConversionJsonContainer"->conversionJsonContainer
                                    ,"ConversionJsonFolderPath"->conversionJsonFolderPath
                                    ,"ConversionJsonFileName"->conversionJsonFileName
                                    ,"HasControlFile"->hasControlFile))


// COMMAND ----------

dbutils.notebook.exit(returnJSON)
