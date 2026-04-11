// Databricks notebook source
// DBTITLE 1,Call Libraries
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.hadoop.fs._
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

// DBTITLE 1,Method: hasColumn
def hasColumn (df:DataFrame, path:String) = Try(df(path)).isSuccess

// COMMAND ----------

// DBTITLE 1,Method: lSplit
def lsplit(pos: List[Int], str: String): Row = {
  
  val (rest, result) = pos.foldLeft((str, List[String]())) {
    case ((s, res),curr) =>
      if(s.length()<=curr)
      {
        val split=s.substring(0).trim()
        val rest=""
        (rest, split :: res)
      }
      else if(s.length()>curr)
      {
        val split=s.substring(0, curr).trim()
        val rest=s.substring(curr)
        (rest, split :: res)
      }
      else
      {
        val split=""
        val rest=""
        (rest, split :: res)
      }
  }
  Row.fromSeq(result.reverse)
}

// COMMAND ----------

// DBTITLE 1,Method: getSortedSelect - Retrieves a Dynamic Select List in a Specific Order
def getSortedSelect (json: DataFrame, selectTag: String, orderTag: String): Array[org.apache.spark.sql.Column] = {
  val colNames = json.select(s"$selectTag")
                     .sort(s"$orderTag")
                     .collect()
                     .map(x=>col(x(0).toString))
  return colNames
}

// COMMAND ----------

// DBTITLE 1,Method: createFixedWidthDF with Overloads
//Use for converting fixed width to delimited
def createFixedWidthDF(fileDf: RDD[String], schemaDf: DataFrame): DataFrame = {
  //get list of columns from JSON 
    val dfColumns = schemaDf.select("FieldName").map(x=>x.getString(0).trim()).collect()
    val columnLengthList = schemaDf.select("Length").map(x=>x.getString(0).trim()).collect().map(_.toInt).toList
  
  //build dataframe with schma structure
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
    val schema = StructType(fields)
    val dfFile = spark.createDataFrame(fileDf.map { x => lsplit(columnLengthList,x) }, schema)

    return dfFile
}

//Use if file has record types
def createFixedWidthDF(fileDf: RDD[String], schemaDf: DataFrame, recordType: String): DataFrame = {
  //get list of columns from JSON 
    val dfColumns = schemaDf.select("FieldName").filter($"Type"===recordType).map(x=>x.getString(0).trim()).collect()
    val columnLengthList = schemaDf.select("Length").filter($"Type"===recordType).map(x=>x.getString(0).trim()).collect().map(_.toInt).toList

  //build dataframe with schma structure
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
    val schema = StructType(fields)
    val dfFile = spark.createDataFrame(fileDf.map { x => lsplit(columnLengthList,x) }, schema).filter($"RecordType"===recordType)

  //build select list
    val dfSelect = if (hasColumn(schemaDf,"ControlFile")) 
                    {schemaDf.select("FieldName").filter($"Type"===recordType and $"ControlFile"===true).map(x=>x.getString(0).trim()).collect()}
                   else 
                    {dfColumns}    
                                 
  //return dataframe with select list
    return dfFile.select(dfSelect.map(col):_*)
}



// COMMAND ----------

// DBTITLE 1,Method: create Delimited DF
def createDelimitedDF(schemaDf: DataFrame, recordType: String, delimiter: String, controlFile: Boolean, FullFile: String): DataFrame = {
    val dfColumns = schemaDf.select("FieldName").filter($"Type"===recordType).map(x=>x.getString(0).trim()).collect()
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true)) 
    val schema = StructType(fields)
    val dfFile = spark.read.format("csv").schema(schema).option("delimiter", delimiter).load(FullFile).filter($"RecordType"===recordType)
  
   //build select list
    val dfSelect = if (schemaDf.filter($"Type"===recordType and $"ControlFile"===true).count()>0) 
            {schemaDf.select("FieldName").filter($"Type"===recordType and $"ControlFile"===true).map(x=>x.getString(0).trim()).collect()}
                   else 
            {dfColumns}

    var df = dfFile.select(dfSelect.map(col):_*)
df
}

// COMMAND ----------

// DBTITLE 1,Method: removeFile - Removes specific files
def removeFile(fPath: String) {
    Try(dbutils.fs.rm(fPath))
    
    print("\nFiles in subfolder removed succefully from "+fPath)
}

// COMMAND ----------

// DBTITLE 1,Method: removeFilesInPath- Removes all the files in a folder path
def removeFilesInPath(fPath: String) {
    Try(dbutils.fs.ls(fPath).map(_.path).foreach { p =>
      dbutils.fs.rm(p)
      print("\nFile was removed: " + p)
  })
  dbutils.fs.rm(fPath, true)
  print("\nAll files were removed in: " + fPath)
}

// COMMAND ----------

// DBTITLE 1,Method: copyFile- Renames Data File From Part% to FileName by copying it
def copyFile(fPath: String,uPath: String, fName: String) {
  //get hadoop file system
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val partFileName = fs.globStatus(new Path(uPath+"/part*"))(0).getPath.getName
  val partFilePath = uPath + "/" + partFileName
  val destinationPath = fPath + "/" + fName

  //moving part file from path to new path
  dbutils.fs.cp(partFilePath,destinationPath)
  print("\nFile was moved from: " + partFilePath + " to " + destinationPath)
}

// COMMAND ----------

// DBTITLE 1,Method: moveFile
def moveFile(source: String, dest: String) {
  dbutils.fs.mv(source, dest)
  
  print("\nFile was moved from: " + source + " to " + dest)
}

// COMMAND ----------

// DBTITLE 1,Method: writeDfCSV - Exports Data Frame to CSV
def writeDfCSV(df: DataFrame, path: String, file: String, delimiter: String): Boolean = {
    if (df.rdd.isEmpty == false) {
       //Push file down one level using the filename
       val updatedPath = path + "/ParqFolder/"

       df.repartition(1)
         .write
         .format("com.databricks.spark.csv")
         .option("header", "true")
         .option("delimiter", delimiter)
         .option("quote", "\u0000")
         .mode(SaveMode.Overwrite)
         .save(updatedPath)

       print("\nDestination file created in: " + updatedPath)

       //Move the file that is created from the updated path to the path
       copyFile(path: String,updatedPath: String, file: String) // file logging is inside of the method (after the file gets moved)
       //remove files in ParqFolder 
       removeFilesInPath(updatedPath: String)
       print("\nFiles in subfolder removed succefully!\n")

       true
    }
    else false
}
