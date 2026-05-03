// Local Spark version of ConversionMain.scala
// Non-Databricks dependent Scala

import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.hadoop.fs._
import scala.util.{Try, Success, Failure}
import io.delta.tables._
import spark.implicits._
import java.io.File
import java.nio.file.{Files, Paths, StandardCopyOption}
import scala.collection.JavaConverters._

object ConversionMain {
  
  // Initialize Spark session if not already exists
  def getSparkSession(): SparkSession = {
    try {
      // Try to get existing spark session
      SparkSession.builder().getOrCreate()
    } catch {
      case _: Exception =>
        SparkSession.builder()
          .appName("ConversionMain")
          .master("local[*]")
          .getOrCreate()
    }
  }

  // Method: hasColumn
  def hasColumn(df: DataFrame, path: String): Boolean = {
    Try(df(path)).isSuccess
  }

  // Method: lSplit
  def lsplit(pos: List[Int], str: String): Row = {
    val (rest, result) = pos.foldLeft((str, List[String]())) {
      case ((s, res), curr) =>
        if (s.length <= curr) {
          val split = s.substring(0).trim()
          val rest = ""
          (rest, split :: res)
        } else if (s.length > curr) {
          val split = s.substring(0, curr).trim()
          val rest = s.substring(curr)
          (rest, split :: res)
        } else {
          val split = ""
          val rest = ""
          (rest, split :: res)
        }
    }
    Row.fromSeq(result.reverse)
  }

  // Method: getSortedSelect - Retrieves a Dynamic Select List in a Specific Order
  def getSortedSelect(json: DataFrame, selectTag: String, orderTag: String): Array[Column] = {
    val colNames = json.select(s"$selectTag")
                       .sort(s"$orderTag")
                       .collect()
                       .map(x => col(x(0).toString))
    return colNames
  }

  // Method: createFixedWidthDF with Overloads
  // Use for converting fixed width to delimited
  def createFixedWidthDF(fileDf: org.apache.spark.rdd.RDD[String], schemaDf: DataFrame): DataFrame = {
    // Get list of columns from JSON 
    val dfColumns = schemaDf.select("FieldName").map(x => x.getString(0).trim()).collect()
    val columnLengthList = schemaDf.select("Length").map(x => x.getString(0).trim()).collect().map(_.toInt).toList

    // Build dataframe with schema structure
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true))
    val schema = StructType(fields)
    val dfFile = getSparkSession().createDataFrame(fileDf.map { x => lsplit(columnLengthList, x) }, schema)

    return dfFile
  }

  // Use if file has record types
  def createFixedWidthDF(fileDf: org.apache.spark.rdd.RDD[String], schemaDf: DataFrame, recordType: String): DataFrame = {
    // Get list of columns from JSON 
    val dfColumns = schemaDf.select("FieldName").filter($"Type" === recordType).map(x => x.getString(0).trim()).collect()
    val columnLengthList = schemaDf.select("Length").filter($"Type" === recordType).map(x => x.getString(0).trim()).collect().map(_.toInt).toList

    // Build dataframe with schema structure
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true))
    val schema = StructType(fields)
    val dfFile = getSparkSession().createDataFrame(fileDf.map { x => lsplit(columnLengthList, x) }, schema).filter($"RecordType" === recordType)

    // Build select list
    val dfSelect = if (hasColumn(schemaDf, "ControlFile")) {
      schemaDf.select("FieldName").filter($"Type" === recordType && $"ControlFile" === true).map(x => x.getString(0).trim()).collect()
    } else {
      dfColumns
    }

    // Return dataframe with select list
    return dfFile.select(dfSelect.map(col): _*)
  }

  // Method: create Delimited DF
  def createDelimitedDF(schemaDf: DataFrame, recordType: String, delimiter: String, controlFile: Boolean, FullFile: String): DataFrame = {
    val dfColumns = schemaDf.select("FieldName").filter($"Type" === recordType).map(x => x.getString(0).trim()).collect()
    val fields = dfColumns.map(fieldName => StructField(fieldName, StringType, nullable = true))
    val schema = StructType(fields)
    val dfFile = getSparkSession().read.format("csv").schema(schema).option("delimiter", delimiter).load(FullFile).filter($"RecordType" === recordType)

    // Build select list
    val dfSelect = if (schemaDf.filter($"Type" === recordType && $"ControlFile" === true).count() > 0) {
      schemaDf.select("FieldName").filter($"Type" === recordType && $"ControlFile" === true).map(x => x.getString(0).trim()).collect()
    } else {
      dfColumns
    }

    var df = dfFile.select(dfSelect.map(col): _*)
    df
  }

  // Method: removeFile - Removes specific files
  def removeFile(fPath: String): Unit = {
    Try {
      val file = new File(fPath)
      if (file.exists()) {
        file.delete()
        println(s"\nFile removed successfully from $fPath")
      } else {
        println(s"\nFile not found at $fPath")
      }
    }.recover {
      case e => println(s"\nError removing file $fPath: ${e.getMessage}")
    }
  }

  // Method: removeFilesInPath- Removes all the files in a folder path
  def removeFilesInPath(fPath: String): Unit = {
    Try {
      val folder = new File(fPath)
      if (folder.exists()) {
        folder.listFiles().foreach { file =>
          if (file.delete()) {
            println(s"\nFile was removed: ${file.getPath}")
          }
        }
        if (folder.delete()) {
          println(s"\nAll files were removed in: $fPath")
        }
      } else {
        println(s"\nPath not found: $fPath")
      }
    }.recover {
      case e => println(s"\nError removing files in $fPath: ${e.getMessage}")
    }
  }

  // Method: copyFile- Renames Data File From Part% to FileName by copying it
  def copyFile(fPath: String, uPath: String, fName: String): Unit = {
    Try {
      val folder = new File(uPath)
      if (folder.exists()) {
        val partFiles = folder.listFiles().filter(_.getName.startsWith("part-"))
        if (partFiles.nonEmpty) {
          val partFile = partFiles.head
          val partFilePath = partFile.getPath
          val destinationPath = fPath + "/" + fName
          
          // Ensure destination directory exists
          val destFolder = new File(fPath)
          if (!destFolder.exists()) {
            destFolder.mkdirs()
          }
          
          // Copy file
          Files.copy(Paths.get(partFilePath), Paths.get(destinationPath), StandardCopyOption.REPLACE_EXISTING)
          println(s"\nFile was copied from: $partFilePath to $destinationPath")
        } else {
          println(s"\nNo part files found in $uPath")
        }
      } else {
        println(s"\nSource folder not found: $uPath")
      }
    }.recover {
      case e => println(s"\nError copying file: ${e.getMessage}")
    }
  }

  // Method: moveFile
  def moveFile(source: String, dest: String): Unit = {
    Try {
      val sourceFile = new File(source)
      val destFile = new File(dest)
      
      // Ensure destination directory exists
      val destFolder = destFile.getParentFile
      if (destFolder != null && !destFolder.exists()) {
        destFolder.mkdirs()
      }
      
      Files.move(Paths.get(source), Paths.get(dest), StandardCopyOption.REPLACE_EXISTING)
      println(s"\nFile was moved from: $source to $dest")
    }.recover {
      case e => println(s"\nError moving file: ${e.getMessage}")
    }
  }

  // Method: writeDfCSV - Exports Data Frame to CSV
  def writeDfCSV(df: DataFrame, path: String, file: String, delimiter: String): Boolean = {
    if (df.rdd.isEmpty() == false) {
      // Push file down one level using the filename
      val updatedPath = path + "/ParqFolder/"

      // Create directory if it doesn't exist
      val folder = new File(updatedPath)
      if (!folder.exists()) {
        folder.mkdirs()
      }

      df.repartition(1)
        .write
        .format("csv")
        .option("header", "true")
        .option("delimiter", delimiter)
        .option("quote", "\u0000")
        .mode(SaveMode.Overwrite)
        .save(updatedPath)

      println(s"\nDestination file created in: $updatedPath")

      // Move the file that is created from the updated path to the path
      copyFile(path, updatedPath, file)
      // Remove files in ParqFolder 
      removeFilesInPath(updatedPath)
      println("\nFiles in subfolder removed successfully!\n")

      true
    } else {
      false
    }
  }
}
