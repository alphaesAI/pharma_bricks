// Databricks notebook source
// DBTITLE 1,Define Parameters
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

val clientContainer = dbutils.widgets.get("ClientContainer") 

// COMMAND ----------

// DBTITLE 1,Declare Variables
val goldPath = clientContainer+"/Platinum/"
val mountPoint = "/mnt/"
val dateName = "dimDate"
val monthName = "dimMonth"
val fullDatePath = mountPoint+goldPath+dateName
val fullMonPath = mountPoint+goldPath+monthName
val startDate = "1900-01-01"
val endDate = "9999-12-31"
var currDate = startDate

// COMMAND ----------

// DBTITLE 1,Import Libraries
import org.apache.spark.sql.functions._
import java.time.LocalDate

// COMMAND ----------

// DBTITLE 1,Import aux notebooks *****FIX Client stuff
// MAGIC %run "../CommonMethods/ABC/FileHandling"

// COMMAND ----------

// DBTITLE 1,Create schemas and dataframes
val dimDateSchema = StructType(Array(
        StructField("dateKey",IntegerType,false)
        ,StructField("date",DateType,false)
        ,StructField("shortDateName",StringType,false)
        ,StructField("longDateName",StringType,false)
        ,StructField("yearNumber",IntegerType,false)
        ,StructField("yearName",StringType,false)
        ,StructField("quarterKey",IntegerType,false)
        ,StructField("quarterNumber",IntegerType,false)
        ,StructField("quarterName",StringType,false)
        ,StructField("quarterOfYearNumber",IntegerType,false)
        ,StructField("quarterOfYearName",StringType,false)
        ,StructField("monthKey",IntegerType,false)
        ,StructField("monthNumber",IntegerType,false)
        ,StructField("monthName",StringType,false)
        ,StructField("monthOfQuarterNumber",IntegerType,false)
        ,StructField("monthOfQuarterName",StringType,false)
        ,StructField("monthOfYearShortName",StringType,false)
        ,StructField("weekKey",IntegerType,false)
        ,StructField("weekNumber",IntegerType,false)
        ,StructField("weekName",StringType,false)
        ,StructField("dayOfWeekNumber",IntegerType,false)
        ,StructField("dayOfWeekName",StringType,false)
        ,StructField("dayOfYear",IntegerType,false)
        ,StructField("isWorkDay",BooleanType,false)
  ))

val dimMonSchema = StructType(Array(
        StructField("monthKey",IntegerType,false)
        ,StructField("monthNumber",IntegerType,false)
        ,StructField("monthName",StringType,false)
        ,StructField("yearNumber",IntegerType,false)
        ,StructField("yearName",StringType,false)
        ,StructField("quarterNumber",IntegerType,false)
        ,StructField("quarterName",StringType,false)
  ))

// COMMAND ----------

// DBTITLE 1,Method: initDateDF- Default Record 
def initDateDF(): DataFrame ={
    var initialDF = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], dimDateSchema)

    initialDF = spark.sql(
             "SELECT 0 as dateKey, to_date('1900-01-01 00:00:00') as date, 'Jan 1, 1900' as shortDateName, 'January 1, 1900' as longDateName, 1900 as yearNumber, '1900' as yearName, 19001 as quarterKey, 1 as quarterNumber, 'Q1' as quarterName, 1 as quarterOfYearNumber, 'Q1, 1900' as quarterOfYearName, 190001 as monthKey, 1 as monthNumber, 'January' as monthName, 1 as monthOfQuarterNumber, 'Month 1' as monthOfQuarterName, 'Jan-1900' as monthOfYearShortName, 1900001 as weekKey, 1 as weekNumber, 'Week 1' as weekName, 2 as dayOfWeekNumber, 'Monday' as dayOfWeekName, 1 as dayOfYear, true as isWorkDay")

    return initialDF
}

// COMMAND ----------

// DBTITLE 1,Method: initMonDF- Default Record 
def initMonDF(): DataFrame ={
    var initialDF = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], dimMonSchema)

    initialDF = spark.sql(
             "SELECT 190001 as monthKey, 1 as monthNumber, 'January' as monthName, 1900 as yearNumber, '1900' as yearName, 1 as quarterNumber, 'Q1' as quarterName")

    return initialDF
}

// COMMAND ----------

// DBTITLE 1,Date Range Dataframe
//pass start and end dates into dataframe to get a dataframe with a record for all days between
var df = Seq((startDate, endDate))
    .toDF("startDate", "endDate")
    .select(col("startDate").cast("date"), col("endDate").cast("date"), datediff(col("endDate"),col("startDate")).as("diffDays"))

// COMMAND ----------

// DBTITLE 1,dimDate Load
val destCheckDate = path_exists(fullDatePath)

if(destCheckDate==false) {
    //insert default values into destination dataframe
    var destinationDataModel = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], dimDateSchema)
  
    // val initialRecs = initDateDF()
    // destinationDataModel = initialRecs
    
    //explode the range to create a new column with each date
    val datesDF = df.withColumn("newDate", explode(expr("sequence(startDate, endDate, interval 1 day)")))

    //date range inserts
    val currDateDF = datesDF.select( 
                      date_format(col("newDate"), "yyyyMMdd").cast("integer").as("dateKey") 
                      ,date_format(col("newDate"), "yyyy-MM-dd HH:mm:ss").cast("date").as("date")
                      ,date_format(col("newDate"), "MMM d, yyyy").as("shortDateName")
                      ,date_format(col("newDate"), "MMMM d, yyyy").as("longDateName")
                      //year columns
                      ,year(col("newDate")).as("YearNumber")
                      ,year(col("newDate")).as("YearName")
                      //qtr columns
                      ,concat(year(col("newDate")),quarter(col("newDate"))).cast("integer").as("QuarterKey")
                      ,quarter(col("newDate")).as("QuarterNumber")
                      ,concat(lit("Q"),quarter(col("newDate"))).as("QuarterName")
                      ,quarter(col("newDate")).as("QuarterOfYearNumber")
                      ,concat(lit("Q"),quarter(col("newDate")),lit(", "),year(col("newDate"))).as("QuarterOfYearName")
                      //mth columns
                      ,date_format(col("newDate"), "yyyyMM").cast("integer").as("monthKey")
                      ,month(col("newDate")).as("monthNumber")
                      ,date_format(col("newDate"), "MMMM").as("monthName")
                      ,expr("""case when month("""+col("newDate")+""") in (1,4,7,10) then 1 """ +
                            """when month("""+col("newDate")+""") in (2,5,8,11) then 2 """+
                            """else 3 end""").as("monthOfQuarterNumber")
                      ,concat(lit("Month "),expr("""case when month("""+col("newDate")+""") in (1,4,7,10) then 1 """ +
                            """when month("""+col("newDate")+""") in (2,5,8,11) then 2 """+
                            """else 3 end""")).as("MonthOfQuarterName")
                      ,concat(date_format(col("newDate"), "MMM"),lit("-"),year(col("newDate"))).as("monthOfYearShortName")
                      //week columns
                      ,((year(col("newDate"))*1000)+weekofyear(col("newDate"))).as("weekKey")
                      ,weekofyear(col("newDate")).as("weekNumber")
                      ,concat(lit("Week "),weekofyear(col("newDate"))).as("weekName")
                      //day columns
                      ,dayofweek(col("newDate")).as("dayOfWeekNumber")
                      ,date_format(col("newDate"), "EEEE").as("dayOfWeekName")
                      ,dayofyear(col("newDate")).as("dayOfYear")
                      ,expr("""case when dayofweek("""+col("newDate")+""") in (1,7) then false """ +
                           """else true end""").as("IsWorkDay")
                    )

   destinationDataModel = destinationDataModel.union(currDateDF)

   destinationDataModel.repartition(1).write.format("delta").option("mergeSchema","true").mode("append").save(fullDatePath)
}
// destinationDataModel.show(100)

// COMMAND ----------

// DBTITLE 1,dimMonth Load
val destCheckMon = path_exists(fullMonPath)

if(destCheckMon==false) {
    var destinationDataModelMon = spark.createDataFrame(spark.sparkContext.emptyRDD[Row], dimMonSchema)
  
    // //insert default values into destination dataframe
    // val initialRecs = initMonDF()
    // destinationDataModelMon = initialRecs
   
    //explode the range to create a new column with each date
    val monthsDF = df.withColumn("newDate", explode(expr("sequence(startDate, endDate, interval 1 month)")))
  
    //date range inserts
    val currMonDF = monthsDF.select( 
                      date_format(col("newDate"), "yyyyMM").cast("integer").as("monthKey")
                      ,month(col("newDate")).as("monthNumber")
                      ,date_format(col("newDate"), "MMMM").as("monthName")
                      //year columns
                      ,year(col("newDate")).as("YearNumber")
                      ,year(col("newDate")).as("YearName")
                      //qtr columns
                      ,quarter(col("newDate")).as("QuarterNumber")
                      ,concat(lit("Q"),quarter(col("newDate"))).as("QuarterName")
                    )

    destinationDataModelMon = destinationDataModelMon.union(currMonDF)
    
    destinationDataModelMon.repartition(1).write.format("delta").option("mergeSchema","true").mode("append").save(fullMonPath)
}

