# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

clientContainer = dbutils.widgets.get("ClientContainer")

dateMonthYearStart = '200001' #2000 Year and 01 Jan as the month
dateMonthYearEnd = '210012'#2200 Year and 12 Dec as the month

mountPoint = "/mnt/"
platinumPath = "/Platinum/dimQualityYearMonth"
fullDatePath = mountPoint + clientContainer + platinumPath
print(fullDatePath)

# COMMAND ----------

# DBTITLE 1,Method : Split to Monthly
from dateutil.relativedelta import relativedelta
import pyspark.sql.functions as psf
from pyspark.sql.types import *

def month_range(startDate, endDate):
  return [startDate + relativedelta(months=+x) for x in range((endDate.year - startDate.year)*12 + endDate.month - startDate.month + 1)]

month_range_udf = psf.udf(month_range, ArrayType(DateType()))
spark.udf.register("month_range", month_range_udf) #registers as a spark sql function

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

dfFile = spark.read.format("delta").option("header","true").load(fullDatePath)
dfFile.createOrReplaceTempView("CheckTableCount")

checkCountSQL = """
  SELECT COUNT(1) AS NumberOfRecords
  FROM CheckTableCount
"""

destCheckDate = spark.sql(checkCountSQL).first()[0]

if(destCheckDate == 0):
  sqlStatement = f"""
  WITH YearMonths AS(
  SELECT  
  explode(month_range(to_date('{dateMonthYearStart}','yyyyMM'), to_date('{dateMonthYearEnd}','yyyyMM'))) AS StartDate
  ),
  CreateGenericRunoutMonths AS (
  SELECT 13 AS MonthNumber
  UNION ALL 
  SELECT 14 AS MonthNumber
  ),
  CreateRunoutMonths AS (
  SELECT DISTINCT
    gr.MonthNumber
    ,YEAR(StartDate) AS YearNumber
  FROM YearMonths
    CROSS JOIN CreateGenericRunoutMonths gr
  ),
  CreateRunoutDates AS (
  SELECT
    CAST(CONCAT(YearNumber,MonthNumber) AS INT) AS monthKey
    ,MonthNumber AS MonthNumber
    ,CASE 
      WHEN MonthNumber = 13 THEN 'Year End (Jan. Runout)'
      WHEN MonthNumber = 14 THEN 'Year End (Final)'
    END AS MonthName
    ,YearNumber AS YearNumber
    ,1 AS IsRunout
  FROM CreateRunoutMonths
  ),
  ActualYearMonths AS(
  SELECT 
    CAST(date_format(StartDate, 'yyyyMM') AS INT) AS monthKey
    ,MONTH(StartDate) AS MonthNumber
    ,date_format(StartDate, 'MMMM') AS MonthName
    ,year(StartDate) AS YearNumber
    ,0 AS IsRunout
  FROM YearMonths
  ),
  DefaultYearMonths AS(
  SELECT 
    CAST('999912' AS INT) AS monthKey
    ,12 AS MonthNumber
    ,'UNKNOWN' AS MonthName
    ,9999 AS YearNumber
    ,0 AS IsRunout
  FROM YearMonths
  ),
  Final AS(
  SELECT 
    monthKey AS qualityYearMonthKey
    ,MonthNumber
    ,MonthName
    ,YearNumber
    ,IsRunout
  FROM ActualYearMonths
  UNION ALL
  SELECT
    monthKey  AS qualityYearMonthKey
    ,MonthNumber
    ,MonthName
    ,YearNumber
    ,IsRunout
  FROM CreateRunoutDates
  UNION ALL 
  SELECT
    monthKey  AS qualityYearMonthKey
    ,MonthNumber
    ,MonthName
    ,YearNumber
    ,IsRunout
  FROM DefaultYearMonths
  )
  SELECT DISTINCT
    qualityYearMonthKey
    ,MonthNumber AS monthNumber
    ,MonthName AS monthName
    ,YearNumber AS yearNumber
    ,CAST(IsRunout AS BOOLEAN) AS isRunout
  FROM Final
  ORDER BY 
    qualityYearMonthKey
    ,MonthNumber
  """

  dfQualityYearMonth = spark.sql(sqlStatement)
  # dfQualityYearMonth.createOrReplaceTempView("FinalQualityYearMonth")
  dfQualityYearMonth.repartition(1).write.format("delta").option("mergeSchema","true").mode("append").save(fullDatePath)
