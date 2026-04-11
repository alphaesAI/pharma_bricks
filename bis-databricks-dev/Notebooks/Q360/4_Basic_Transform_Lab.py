# Databricks notebook source
# MAGIC %md
# MAGIC ## 4_Basic_Transform_Lab

# COMMAND ----------

# DBTITLE 1,Required Libraries
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col,substring,expr,date_format,when
from pyspark.sql.types import StringType,StructType,StructField

# COMMAND ----------

# DBTITLE 1,Cell to receive location parameters from ADF pipeline through master notebook

clientName = dbutils.widgets.get("clientname")
q360_location = dbutils.widgets.get("location")
qsi_location = dbutils.widgets.get("location2")
destination_location = dbutils.widgets.get("destination_location")


# COMMAND ----------

# DBTITLE 1,Load Original Q360 Lab file to spark dataframe
#Assign the Original Q360 file path to a variable
file_path_Q360_lab = f'/mnt/{clientName}/Q360/Q360/{q360_location}'

#Create schema for the dataframe as per the Q360 Lab file layout
lab_schema = StructType([
    StructField("MemberID_q360", StringType(),True),
    StructField("CPT_Code_q360", StringType(), True),
    StructField("LOINC_Code_q360", StringType(), True),
    StructField("Test_Result_Value_q360", StringType(),True),
    StructField("Date_of_Service_q360", StringType(), True),
    StructField("Provider_ID_q360", StringType(), True),
    StructField("Data_Source_Name_q360", StringType(),True),
    StructField("Additional_coloumn_1_q360", StringType(), True),
    StructField("Additional_coloumn_2_q360", StringType(), True),
    StructField("Additional_coloumn_3_q360", StringType(), True),
    StructField("Additional_coloumn_4_q360", StringType(), True),
    StructField("Additional_coloumn_5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])

#Load the spark dataframe based on the schema
df_Q360_lab = spark.read.option("delimiter",'|').schema(lab_schema).csv(file_path_Q360_lab)


# COMMAND ----------

# DBTITLE 1,Load data from dataframe into Temp view
df_Q360_lab.createOrReplaceTempView("view_OriginalQ360_Lab_data")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360_Lab
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_Lab

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360_Lab
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_Lab
# MAGIC (
# MAGIC     MemberID VARCHAR(16),
# MAGIC     CPT_Code VARCHAR(5),
# MAGIC     LOINC_Code VARCHAR(7),
# MAGIC     TestResultValue VARCHAR(10),
# MAGIC     DateofService VARCHAR(8),
# MAGIC     ProviderID VARCHAR(25),
# MAGIC     DataSourceName VARCHAR(20),
# MAGIC     Additionalcoloumn1 VARCHAR(10),
# MAGIC     Additionalcoloumn2 VARCHAR(10),
# MAGIC     Additionalcoloumn3 VARCHAR(10),
# MAGIC     Additionalcoloumn4 VARCHAR(30),
# MAGIC     Additionalcoloumn5 VARCHAR(30),
# MAGIC     Filler VARCHAR(100)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp view into table OriginalQ360_Lab
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_Lab
# MAGIC SELECT DISTINCT 
# MAGIC     IFNULL(MemberID_q360,'') AS MemberID,
# MAGIC     IFNULL(CPT_Code_q360,'') AS CPT_Code,
# MAGIC     IFNULL(LOINC_Code_q360,'') AS LOINC_Code,
# MAGIC     IFNULL(Test_Result_Value_q360,'') AS TestResultValue,
# MAGIC     IFNULL(Date_of_Service_q360,'') AS DateofService,
# MAGIC     IFNULL(Provider_ID_q360,'') AS ProviderID,
# MAGIC     IFNULL(Data_Source_Name_q360,'') AS DataSourceName,
# MAGIC     IFNULL(Additional_coloumn_1_q360,'') AS Additionalcoloumn1,
# MAGIC     IFNULL(Additional_coloumn_2_q360,'') AS Additionalcoloumn2,
# MAGIC     IFNULL(Additional_coloumn_3_q360,'') AS Additionalcoloumn3,
# MAGIC     IFNULL(Additional_coloumn_4_q360,'') AS Additionalcoloumn4,
# MAGIC     IFNULL(Additional_coloumn_5_q360,'') AS Additionalcoloumn5,
# MAGIC     IFNULL(Filler_q360,'') AS Filler
# MAGIC
# MAGIC FROM view_OriginalQ360_Lab_data

# COMMAND ----------

# DBTITLE 1,Transform QSI Lab file and load to spark dataframe
# Assign QSI file from mounted location to a variable
file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location}'

#Load QSI file to the spark data frame 
df_lab_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)
#Store the list of columns needed from the QSI Lab file
lab_col_needed = ["MemberKey","CPTPx","LOINC","Result","DOS","ProviderKey","SuppSource"]

# # QSI dataframe with required columns for Transdformation (Source)
df_lab_qsi = df_lab_qsi.select(lab_col_needed)

# Renaming QSI columns with respect to Q360 files.
df_lab_qsi = df_lab_qsi.withColumnRenamed('CPTPx','CPT_Code')\
                        .withColumnRenamed('LOINC','LOINC_Code')\
                        .withColumnRenamed('Result','TestResultValue')\
                        .withColumnRenamed('ProviderKey','Provider_ID')\
                        .withColumnRenamed('SuppSource','DataSourceName')
                          

df_lab_qsi =  df_lab_qsi.withColumn("Member_ID",substring(col("MemberKey"),0,16))\
                        .withColumn("DateofService",date_format("DOS",'yyyyMMdd')) \
                        .drop("MemberKey","DOS")

# Columns ordered inside list to get same order as of Q360
final_column_qsi_to_q360 = ["Member_ID","CPT_Code","LOINC_Code","TestResultValue",
                            "DateofService","Provider_ID","DataSourceName"]

df_lab_qsi = df_lab_qsi.select(final_column_qsi_to_q360)

# display(df_lab_qsi)


# COMMAND ----------

# DBTITLE 1,Loading converted QSI to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#Convert spark dataframe into pandas dataframe
pandas_lab_qsi_df = df_lab_qsi.toPandas()

#Convert pandas dataframe into a csv file
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'
pandas_lab_qsi_df.to_csv(f'{file_destination}QSI_to_Q360_lab_converted_{date}.txt',
                     index = False,sep = '|') 


# COMMAND ----------

# DBTITLE 1,Join QSI and Q360 Dataframes
# Perform the full outer join operation with df_q360 and qsi
df_lab_full_join = df_lab_qsi.join(df_Q360_lab, (df_lab_qsi.Member_ID == df_Q360_lab.MemberID_q360), 'full')


# COMMAND ----------

# DBTITLE 1,Comparing Q360 and QSI dataframes
df_lab_full_join = df_lab_full_join.withColumn('Member_ID_status',\
                                        when(col('Member_ID') == col('MemberID_q360'),'Y') \
                                            .otherwise('N')) \
                                    .withColumn('CPT_Code_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('CPT_Code')== col('CPT_Code_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('LOINC_Code_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('LOINC_Code')== col('LOINC_Code_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('TestResultValue_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('TestResultValue')== col('Test_Result_Value_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('DateofService_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('DateofService')== col('Date_of_Service_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('Provider_ID_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('Provider_ID')== col('Provider_ID_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('DataSourceName_status',\
                                        when(col('Member_ID')== col('MemberID_q360'), \
                                            when(col('DataSourceName')== col('Data_Source_Name_q360'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) 
                                  

lab_status_columns = ['Member_ID',
                      'Member_ID_status','CPT_Code_status','LOINC_Code_status', 
                      'TestResultValue_status','DateofService_status',
                      'Provider_ID_status','DataSourceName_status']

df_lab_full_join = df_lab_full_join.select(lab_status_columns)

# display(df_lab_full_join)

# COMMAND ----------

# DBTITLE 1,Load Comparison results from spark dataframe to Temp view
df_lab_full_join.createOrReplaceTempView('view_LabComparison_Results')

# COMMAND ----------

# DBTITLE 1,Drop table tblM_LabComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_LabComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_LabComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_LabComparison_Results
# MAGIC (
# MAGIC
# MAGIC     Member_ID VARCHAR(16),
# MAGIC     IsRecordMatching CHAR(1),
# MAGIC     Member_ID_status CHAR(1),
# MAGIC     CPT_Code_status CHAR(1),
# MAGIC     LOINC_Code_status CHAR(1),
# MAGIC     TestResultValue_status CHAR(1),
# MAGIC     DateofService_status CHAR(1),
# MAGIC     Provider_ID_status CHAR(1),
# MAGIC     DataSourceName_status CHAR(1)
# MAGIC     
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp View into table tblM_LabComparison_Results
# MAGIC %sql
# MAGIC INSERT INTO tblM_LabComparison_Results
# MAGIC SELECT DISTINCT 
# MAGIC     Member_ID,
# MAGIC     'Y' AS IsRecordMatching,
# MAGIC     Member_ID_status,
# MAGIC     CPT_Code_status,
# MAGIC     LOINC_Code_status, 
# MAGIC     TestResultValue_status,
# MAGIC     DateofService_status,
# MAGIC     Provider_ID_status,
# MAGIC     DataSourceName_status
# MAGIC     
# MAGIC FROM view_LabComparison_Results

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the flags of the individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_LabComparison_Results
# MAGIC     SET IsRecordMatching = CASE 
# MAGIC                                 WHEN Member_ID_status = 'N' OR
# MAGIC                                       CPT_Code_status = 'N' OR
# MAGIC                                       LOINC_Code_status = 'N' OR 
# MAGIC                                       TestResultValue_status = 'N' OR
# MAGIC                                       DateofService_status = 'N' OR
# MAGIC                                       Provider_ID_status = 'N' OR
# MAGIC                                       DataSourceName_status = 'N'
# MAGIC                                   THEN 'N'
# MAGIC                               ELSE 'Y'
# MAGIC                             END

# COMMAND ----------

# DBTITLE 1,Drop table tblM_Q360_Comparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_Q360_Comparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_Q360_Comparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_Q360_Comparison_Results
# MAGIC (
# MAGIC     Client VARCHAR(20),
# MAGIC     RunDateTime TIMESTAMP,
# MAGIC     FileType VARCHAR(20),
# MAGIC     OrgQ360_Rowcount INT,
# MAGIC     MatchingRecords INT,
# MAGIC     MismatchRecords INT
# MAGIC )

# COMMAND ----------

# DBTITLE 1,To get the count of matched and mismatched records
# MAGIC %sql
# MAGIC INSERT INTO tblM_Q360_Comparison_Results
# MAGIC SELECT  
# MAGIC       'ABC' AS Client,
# MAGIC       getdate() AS RunDateTime,
# MAGIC       'LAB' AS FileType,
# MAGIC       (SELECT count(MemberID) FROM OriginalQ360_Lab) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_LabComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Lab
# MAGIC       INNER JOIN tblM_LabComparison_Results
# MAGIC       on OriginalQ360_Lab.MemberID = tblM_LabComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_LabComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Lab
# MAGIC       FULL OUTER JOIN tblM_LabComparison_Results
# MAGIC       on OriginalQ360_Lab.MemberID = tblM_LabComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords
# MAGIC       
# MAGIC       

# COMMAND ----------

# DBTITLE 1,Load the File level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')

#Convert spark dataframe into pandas dataframe
df_final_status = df_final.toPandas()

#Copy data from pandas dataframe to csv file
df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Lab_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Load the Record level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Lab = spark.sql('SELECT * FROM tblM_LabComparison_Results ORDER BY Member_ID')

#Convert spark dataframe into pandas dataframe
df_Lab_Pandas = df_Lab.toPandas()

#Copy data from pandas dataframe to csv file
df_Lab_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Lab_Comparison_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Notebook exit comment to show the status of the run
dbutils.notebook.exit("Success")
