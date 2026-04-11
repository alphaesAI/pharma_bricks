// Databricks notebook source
// DBTITLE 1,Setup Parameters
//Actual File Parameters
dbutils.widgets.text("FileID","","") //0 
dbutils.widgets.text("CurrentContainer","","") //validate
dbutils.widgets.text("CurrentFolderPath","","") ///MA/Internal/FCF/2020/05/06/
dbutils.widgets.text("FileName","","") //PBC_VIS_FCF_prod_20200227070003.TXT
dbutils.widgets.text("Delimiter","","") //"|"
dbutils.widgets.text("HasHeaders","","") //"|"
dbutils.widgets.text("IgnoreHeader","","") //"|"
dbutils.widgets.text("TextQualifier","","") //"""

//Validated Zone Parameters
dbutils.widgets.text("ValidatedFolderPath","","")   //validate

//Configuration File Parameters
dbutils.widgets.text("ValidationContainer","","")   //validate
dbutils.widgets.text("ValidationFileFolderPath","","") //ValidationRules
dbutils.widgets.text("ValidationFileName","","") //fcf_schema.json 


// COMMAND ----------

// DBTITLE 1,Set Variables
val mountPoint = "/mnt/"
val fileId = dbutils.widgets.get("FileID")  
val currentContainer = dbutils.widgets.get("CurrentContainer") 
val currentFolderPath = dbutils.widgets.get("CurrentFolderPath") 
val fileName = dbutils.widgets.get("FileName") 

//Validated Zone
val validatedFolderPath = dbutils.widgets.get("ValidatedFolderPath") 

//Schema File
val validationContainer = dbutils.widgets.get("ValidationContainer") 
val validationFileFolderPath = dbutils.widgets.get("ValidationFileFolderPath") 
val validationFileName = dbutils.widgets.get("ValidationFileName")
var delimiter = dbutils.widgets.get("Delimiter")
if (delimiter == "") delimiter ="|"
val header = dbutils.widgets.get("HasHeaders")
val ignoreHeader = dbutils.widgets.get("IgnoreHeader")
val textQualifier = dbutils.widgets.get("TextQualifier")

// get FileName without extension '.txt'
var errorFolderName = fileName
if (fileName.contains(".txt") || fileName.contains(".TXT") || fileName.contains(".csv") || fileName.contains(".CSV")) 
  errorFolderName = fileName.slice(0, fileName.lastIndexOf("."))

val fullFile = mountPoint + currentContainer + currentFolderPath + "/"+ fileName
val fullValidation = mountPoint + validationContainer + validationFileFolderPath + "/"+  validationFileName
val fullError = mountPoint +validatedFolderPath + "/Error/" + errorFolderName + ".err"

//User For JSON Returned
var RecordCount: Long = 0 
var ErrorCount: Long = 0
var ReturnJSON: String  = ""

// COMMAND ----------

// DBTITLE 1,Import Libraries
import java.time.LocalDate
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit.DAYS

import org.apache.spark.sql.functions.monotonically_increasing_id
import org.apache.spark.sql._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions.row_number
import spark.implicits._

//case class cls_explodedValidationsLevel2(FieldName:String, Name: String, InputValue: String)
case class cls_explodedValidationsLevel2(FieldName:String, Name: String, Value: String, InputValue: Array[String], ConditionCol: String, ConditionVal: Array[String])

// COMMAND ----------

// DBTITLE 1,Call FileHandling Notebook
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Call ErrorHandling Methods
// MAGIC %run "../CommonMethods/ABC/ErrorHandling"

// COMMAND ----------

// DBTITLE 1,Call UserDefined function Methods
// MAGIC %run "../CommonMethods/ABC/CreateUserDefinedFunctions"

// COMMAND ----------

// DBTITLE 1,Method: IsRequired
  def IsRequired(dfData: DataFrame, filterColName: String, validator: String, ErrorPath: String ): Long =
  {    
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Field Missing"))
            .filter((col(filterColName).isNull) || (col(filterColName).cast("String") ===""))
   
    //if errors write to file     
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)
 
    return df.count()
  }


// COMMAND ----------

// DBTITLE 1,Method-- IsRequiredWithCondition
// This method will check value is not null or empty when match required conditions
// Memout file will have the cofig as below:
// "FieldName": "ContractNumber",
//             "OrdinalPosition": "108",
//             "DataType": "string",
//             "Validators": [
//                 {
//                     "Name": "isRequiredWithCondition", // validator name
//                     "ConditionCol": "TransactionType", // condition column name
//                     "ConditionVal": ["PLN"]            // condition column values                           
//                 }
//             ]
def isRequiredWithCondition(dfData: DataFrame, filterColName: String, validator: String, conditionCol: String, conditionVal:Array[String], errorPath: String): Long =
  {    
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName,conditionCol)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")           
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",concat(lit("Field Missing when "), lit(conditionCol), lit(" is "), lit(conditionVal.mkString(", "))))
            .where(col(conditionCol).isin(conditionVal:_*))
            .filter((col(filterColName).isNull) || (trim(col(filterColName)) ===""))
    
    // reorder the cols in error message to make sure the same layout with other validators
    val dfReorder = df.select("FILE_ID", "ROW_ID", "VALUE", "FIELD_NAME","VALIDATOR", "ERROR_DESCRIPTION")
    
    //if errors write to file     
    if (dfReorder.count() > 0)
      outputValidationError(dfReorder, errorPath)      
 
    return dfReorder.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: IsDate
 def IsDate(dfData:DataFrame, filterColName:String, validator: String, dateFormat: String, ErrorPath: String ): Long  =
  {
    val  df = dfData.select("FILE_ID","ROW_ID",filterColName)
               .filter(!(col(filterColName).isNull) || !(col(filterColName).cast("String") ===""))
               .withColumn("new_date",from_unixtime(unix_timestamp(col(filterColName).cast(StringType), dateFormat),"yyyy-MM-dd"))
               .withColumn("FIELD_NAME",lit(filterColName))
               .withColumnRenamed(filterColName,"VALUE")
               .withColumn("VALIDATOR",lit(validator))
               .withColumn("ERROR_DESCRIPTION",lit("Not a valid date or format"))
               .filter("new_date is null")
               .drop(col("new_date"))
   
    //if errors write to file     
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)  

    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: isDateNotRequired
 def isDateNotRequired(dfData:DataFrame, filterColName:String, validator: String, dateFormat: String, ErrorPath: String ): Long  =
  {
    val  df = dfData.select("FILE_ID","ROW_ID",filterColName)
               .withColumn("new_date",from_unixtime(unix_timestamp(col(filterColName).cast(StringType), dateFormat),"yyyy-MM-dd"))
               .withColumn("FIELD_NAME",lit(filterColName))
               .withColumnRenamed(filterColName,"VALUE")
               .withColumn("VALIDATOR",lit(validator))
               .withColumn("ERROR_DESCRIPTION",lit("Not a valid date or format when populated"))
               .where(trim(col(filterColName)) =!= "")
               .filter("new_date is null")
               .drop(col("new_date"))
   
    //if errors write to file     
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)  

    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: IsDataType
  def IsDataType(dfData: DataFrame, filterColName: String, validator: String, dataType: String, ErrorPath: String  ): Long =
  {
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Incorrect Datatype"))
            .filter(col(filterColName).cast(dataType).isNull) 
   
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }
    

// COMMAND ----------

// DBTITLE 1,Method: IsDataTypeNotRequired
  def IsDataTypeNotRequired(dfData: DataFrame, filterColName: String, validator: String, dataType: String, ErrorPath: String  ): Long =
  {
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Incorrect Datatype"))
            .where(trim(col(filterColName)) =!= "''")
            .filter(col(filterColName).cast(dataType).isNull) 
   
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }
    

// COMMAND ----------

// DBTITLE 1,Method: IsInAllowedValues
def IsInAllowedValues(dfData: DataFrame, filterColName: String, validator: String, AllowedValues:Array[String], ErrorPath: String  ): Long =
  {
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Not in Allowed Values"))
            .filter(!col(filterColName).isin(AllowedValues:_*)) 

    
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: IsMinValue
import org.apache.spark.sql
def IsMinValue(dfData: DataFrame, filterColName: String, validator: String, MinValue: String, ErrorPath: String  ): Long =
  {
    val MinVal = MinValue.toInt
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Incorrect MinValue"))
            .filter(col(filterColName).cast(sql.types.IntegerType) < MinVal) 

    
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: IsMaxValue
import org.apache.spark.sql
def IsMaxValue(dfData: DataFrame, filterColName: String, validator: String, MaxValue:String, ErrorPath: String  ): Long =
  {
    val MaxVal = MaxValue.toInt
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Incorrect MaxValue"))
            .filter(col(filterColName).cast(sql.types.IntegerType) > MaxVal) 

    
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: IsMaxDate
def IsMaxDate(dfData:DataFrame, filterColName:String, validator: String, dateFormat: String, ErrorPath: String ): Long  =
  {
    val  df = dfData.select("FILE_ID","ROW_ID",filterColName)
               .filter(!(col(filterColName).isNull) || !(col(filterColName).cast("String") ===""))
               .withColumn("new_date",from_unixtime(unix_timestamp(col(filterColName).cast(StringType), dateFormat),"yyyy-MM-dd"))
               .withColumn("FIELD_NAME",lit(filterColName))
               .withColumnRenamed(filterColName,"VALUE")
               .withColumn("VALIDATOR",lit(validator))
               .withColumn("ERROR_DESCRIPTION",lit("Not a valid date, greater than current date"))
               .filter($"new_date" > current_date())
               .drop(col("new_date"))
   
    //if errors write to file     
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)  

    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: DataLengthCheck
def dataLengthCheck (dfData: DataFrame, filterColName: String, validator: String, dataLength: Int, ErrorPath: String): Long =
  {
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Incorrect Data Length"))
            .withColumn("VALUE", regexp_replace(col("VALUE"), "\\s+", ""))
            .withColumn("ACTUAL_DATA_LENGTH", length('VALUE))
            .withColumn("EXPECTED_DATA_LENGTH", lit(dataLength))            
            .filter(col("ACTUAL_DATA_LENGTH") =!= dataLength && col("ACTUAL_DATA_LENGTH") =!= 0) 
   
//     if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)
      
    return df.count()
  }
  

// COMMAND ----------

// DBTITLE 1,Method: isMONCCYYValid
 def IsMONCCYYValid(dfData:DataFrame, filterColName:String, validator: String, ErrorPath: String ): Long  =
  {
    val  df = dfData.select("FILE_ID","ROW_ID",filterColName)
               .filter(!(col(filterColName).isNull) || !(col(filterColName).cast("String") ===""))
               .withColumn("FIELD_NAME",lit(filterColName))
               .withColumn("MON",substring(col(filterColName),0,3))
               .withColumn("YEAR",substring(col(filterColName),-4,4))
               .withColumn("VALIDATOR",lit("isMONCCYYValid"))
               .withColumn("ERROR_DESCRIPTION",lit("Not a valid MONCCYY"))
               .filter(!col("YEAR").rlike("^[0-9]*$") || (col("YEAR").rlike("^[0-9]*$") && col("YEAR").cast(sql.types.IntegerType) < 1900) || !(upper(col("MON")).rlike("JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC")) || !(length(col(filterColName))  === 7))
               .drop(col("YEAR"))
               .drop(col("MON"))               
               
            
   
    //if errors write to file     
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)  

    return df.count()
  }

// COMMAND ----------

def IsInAllowedValuesAndNull(dfData: DataFrame, filterColName: String, validator: String, AllowedValues:Array[String], ErrorPath: String  ): Long =
  {
    val df = dfData
            .select("FILE_ID","ROW_ID",filterColName)
            .filter(!(col(filterColName).isNull) && !(col(filterColName).cast("String") ===""))  //this is for exclude empty null/blank and only validate rest of data            
            .withColumn("FIELD_NAME",lit(filterColName))
            .withColumnRenamed(filterColName,"VALUE")
            .withColumn("VALIDATOR",lit(validator))
            .withColumn("ERROR_DESCRIPTION",lit("Not in Allowed Values"))
            .filter(!col(filterColName).isin(AllowedValues:_*)) 

    
    //if errors write to file 
    if (df.count() > 0)
      outputValidationError(df, ErrorPath) 
    
    return df.count()
  }

// COMMAND ----------

import org.apache.spark.sql.functions.expr

def IsOverPunch(dfData: DataFrame, filterColName: String, validator: String, ErrorPath: String ): Long =
  {
    val tempDF = dfData
                .select("FILE_ID","ROW_ID",filterColName)
                .filter(!(col(filterColName).isNull) && !(col(filterColName).cast("String") ===""))
                .withColumn("FIELD_NAME",lit(filterColName))
                .withColumnRenamed(filterColName,"VALUE")
                .withColumn("VALIDATOR",lit(validator))

    tempDF.createOrReplaceTempView("TestDF")

    val validationSQL = """
                SELECT 
                   FILE_ID
                  ,ROW_ID
                  ,VALUE
                  ,FIELD_NAME
                  ,VALIDATOR
                  ,'Is not an overpunch character' AS ERROR_DESCRIPTION
                  ,overpunch(VALUE) AS IsOverpunch
                FROM TestDF
        """

    val df = spark.sql(validationSQL).filter(col("IsOverpunch").isNull)
   
    //if errors write to file
    if (df.count() > 0)
      outputValidationError(df, ErrorPath)
 
    return df.count()
  }

// COMMAND ----------

// DBTITLE 1,Method: level2Validator
def level2Validator(SchemaFilePath:String,dataFilePath:String) = {
  
  var rJSON = ""
  val doubleQuote = """ " """.trim()
  var ErrorMessage = "";
  //set variables with the arguments passed in
  val dataFile = dataFilePath
  val dataSchema = SchemaFilePath
  var dfFile: DataFrame = sqlContext.emptyDataFrame
  
  try {
     //Get notebook context -- to get RunId and JobId
    val ctx = dbutils.notebook.getContext 
    val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

    rJSON += "{" 
    rJSON += doubleQuote + "CurrentJobId"  + doubleQuote + ":"  + doubleQuote + currentJobId.toString + doubleQuote 
    rJSON += ","
    //create data file and schema file dataframes
    if(ignoreHeader=="true" && header=="true")//ordinal based
      {
          dfFile=isIgnoreHeader(dataFile,dataSchema,delimiter,textQualifier)
      }
    else if(ignoreHeader=="false" && header=="false")//ordinal based
      {
          dfFile = withoutHeader(dataFile,dataSchema,delimiter,textQualifier)
      }
    else
      { //Loads header from file
         dfFile = spark.read.option("header", header).format("csv").option("delimiter", delimiter).option("quote", textQualifier).option("inferSchema", "true").load(dataFile)
      }
   
    var dfData1 = dfFile.withColumn("FILE_ID",lit(fileId)).withColumn("ROW_ID1",(monotonically_increasing_id()+1))
    val windowSpec = Window.partitionBy("FILE_ID").orderBy("ROW_ID1")
    var dfData2 = dfData1.withColumn("ROW_ID", row_number().over(windowSpec))
    var dfData = dfData2.drop("ROW_ID1")
    val dfDataSchema = spark.read.format("json").option("multiline", "true").load(dataSchema)
    
    
    //get list of columns, validators and format from schema dataframe
    val explodedValidations = dfDataSchema.select( explode($"ColumnNames")).select($"col.FieldName",$"col.Validators").filter($"col.FieldName" =!= "TEMPLATE")
                                                                                   
    //set variables for error capturing
    var validationOutcome: Long = 0
    var nonValidator: String = ""
  
    //Exploding the columns created
    val dfValidators = explodedValidations.withColumn("Validators",explode((col("Validators")))).select(col("FieldName"),col("Validators.Name").as("Name"),col("Validators.Value").as("Value"),col("Validators.InputValue").as("InputValue"),col("Validators.ConditionCol").as("ConditionCol"), col("Validators.ConditionVal").as("ConditionVal"))
  
    //iterate through schema json to get validators for each column and run the validations
    dfValidators.as[cls_explodedValidationsLevel2].take(dfValidators.count.toInt).foreach(t =>
         t.Name.toString match {
            case "isRequired"  => {validationOutcome+=IsRequired(dfData, t.FieldName.toString, t.Name.toString, fullError)}
            case "isDate" => {validationOutcome+=IsDate(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isMaxDate" => {validationOutcome+=IsMaxDate(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isDateNotRequired" => {validationOutcome+=isDateNotRequired(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isDataType" => {validationOutcome+=IsDataType(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isDataTypeNotRequired" => {validationOutcome+=IsDataTypeNotRequired(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isMinValue" => {validationOutcome+=IsMinValue(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "isMaxValue" => {validationOutcome+=IsMaxValue(dfData, t.FieldName.toString, t.Name.toString, t.Value.toString, fullError)}
            case "IsInAllowedValues" => {validationOutcome+=IsInAllowedValues(dfData, t.FieldName.toString, t.Name.toString,t.InputValue, fullError)}
            case "dataLengthCheck" => {validationOutcome+=dataLengthCheck(dfData, t.FieldName.toString, t.Name.toString, t.Value.toInt, fullError)}
            case "isMONCCYYValid" => {validationOutcome+=IsMONCCYYValid(dfData, t.FieldName.toString, t.Name.toString, fullError)}
            case "IsInAllowedValuesAndNull" => {validationOutcome+=IsInAllowedValuesAndNull(dfData, t.FieldName.toString, t.Name.toString,t.InputValue, fullError)}
            case "isRequiredWithCondition" => {validationOutcome+=isRequiredWithCondition(dfData, t.FieldName.toString, t.Name.toString,t.ConditionCol, t.ConditionVal, fullError)}
            case "IsOverPunch" => {validationOutcome+=IsOverPunch(dfData, t.FieldName.toString, t.Name.toString, fullError)}
            case _  => {nonValidator = "Unimplemented Function"}
          }
      )
    rJSON += doubleQuote + "Status"  + doubleQuote + ":"  + doubleQuote + "SUCCESS" + doubleQuote  
    rJSON += ","
    rJSON += doubleQuote + "RecordCount"  + doubleQuote + ":"  + doubleQuote + dfData.count().toString + doubleQuote 
    rJSON += ","
    rJSON += doubleQuote + "ErrorCount"  + doubleQuote + ":"  + doubleQuote + validationOutcome.toString + doubleQuote 
    rJSON += ","
    rJSON += doubleQuote + "ErrorPathSchema"  + doubleQuote + ":"  + doubleQuote + fullError + doubleQuote 
    rJSON += ","
    rJSON += doubleQuote + "ErrorMessage"  + doubleQuote + ":"  + doubleQuote + "" + doubleQuote
  }
  catch {
     case e: Throwable =>  {      
        rJSON += doubleQuote + "Status"  + doubleQuote + ":"  + doubleQuote + "FAILED" + doubleQuote  
        rJSON += "," 
        rJSON += doubleQuote + "RecordCount"  + doubleQuote + ":"  + doubleQuote + "0" + doubleQuote  
        rJSON += "," 
        rJSON += doubleQuote + "ErrorCount"  + doubleQuote + ":"  + doubleQuote + "0" + doubleQuote 
        rJSON += "," 
        rJSON += doubleQuote + "ErrorPathSchema"  + doubleQuote + ":"  + doubleQuote + fullError + doubleQuote 
        rJSON += ","
        rJSON += doubleQuote + "ErrorMessage"  + doubleQuote + ":"  + doubleQuote + StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,"") + doubleQuote 
    }
  }
  finally {
    rJSON += "}"
    dbutils.notebook.exit(rJSON)
  }

} 

// COMMAND ----------

// DBTITLE 1,Executing Level 2 Validations
//Execute level 2 validations
level2Validator(fullValidation,fullFile)

