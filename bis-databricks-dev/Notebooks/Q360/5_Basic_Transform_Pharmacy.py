# Databricks notebook source
# MAGIC %md
# MAGIC ##5_Basic_Transform_Pharmacy

# COMMAND ----------

# DBTITLE 1,Required Libraries
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col,substring,expr,date_format,when,round
from pyspark.sql.types import StringType,StructType,StructField

# COMMAND ----------

# DBTITLE 1,Cell to receive location parameters from ADF pipeline through master notebook
clientName = dbutils.widgets.get("clientname")
q360_location = dbutils.widgets.get("location")
qsi_location = dbutils.widgets.get("location2")
destination_location = dbutils.widgets.get("destination_location")

# COMMAND ----------

# DBTITLE 1,Load Original Q360 Pharmacy file to spark dataframe
#Assign the Original Q360 file path to a variable
file_path_Q360_pharmacy = f'/mnt/{clientName}/Q360/Q360/{q360_location}'

#Create schema for the dataframe as per the Q360 Pharmacy file layout

pharmacy_schema = StructType([
    StructField("Member_ID_q360", StringType(),True),
    StructField("Dayssupply_q360", StringType(), True),
    StructField("ServiceDate_q360", StringType(), True),
    StructField("NDCDrugCode_q360", StringType(),True),
    StructField("Claimstatus_q360", StringType(), True),
    StructField("QuantityDispensed_q360", StringType(), True),
    StructField("SupplementalData_q360", StringType(),True),
    StructField("DataSourceName_q360", StringType(),True),
    StructField("ProviderID_q360", StringType(),True),
    StructField("ProviderNPI_q360", StringType(),True),
    StructField("PharmacyNPI_q360", StringType(),True),
    StructField("ClaimId_q360", StringType(),True),
    StructField("ClaimlineId_q360", StringType(),True),
    StructField("Additional_coloumn_1_q360", StringType(), True),
    StructField("Additional_coloumn_2_q360", StringType(), True),
    StructField("Additional_coloumn_3_q360", StringType(), True),
    StructField("Additional_coloumn_4_q360", StringType(), True),
    StructField("Additional_coloumn_5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])
#Load the spark dataframe based on the schema
df_Q360_pharmacy = spark.read.option("delimiter",'|').schema(pharmacy_schema).csv(file_path_Q360_pharmacy)


# COMMAND ----------

# DBTITLE 1,Load data from spark dataframe into Temp view
df_Q360_pharmacy.createOrReplaceTempView("view_OriginalQ360_Pharmacy")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360_Pharmacy
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_Pharmacy

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360_Pharmacy
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_Pharmacy
# MAGIC (
# MAGIC     MemberID VARCHAR(16),
# MAGIC     DaysSupply VARCHAR(3),
# MAGIC     ServiceDate VARCHAR(8),
# MAGIC     NDCDrugCode VARCHAR(11),
# MAGIC     ClaimStatus CHAR(1),
# MAGIC     QuantityDispensed VARCHAR(10),
# MAGIC     SupplementalData CHAR(1),
# MAGIC     DataSourceName VARCHAR(20),
# MAGIC     ProviderID VARCHAR(25),
# MAGIC     ProviderNPI VARCHAR(10),
# MAGIC     PharmacyNPI VARCHAR(10),
# MAGIC     ClaimID VARCHAR(20),
# MAGIC     ClaimlineID VARCHAR(10),
# MAGIC     Additionalcoloumn1 VARCHAR(10),
# MAGIC     Additionalcoloumn2 VARCHAR(10),
# MAGIC     Additionalcoloumn3 VARCHAR(10),
# MAGIC     Additionalcoloumn4 VARCHAR(30),
# MAGIC     Additionalcoloumn5 VARCHAR(30),
# MAGIC     Filler VARCHAR(100)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp View to the table OriginalQ360_Pharmacy
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_Pharmacy
# MAGIC SELECT DISTINCT
# MAGIC     IFNULL(Member_ID_q360,'') AS MemberID,
# MAGIC     IFNULL(Dayssupply_q360,'') AS Dayssupply,
# MAGIC     IFNULL(ServiceDate_q360,'') AS ServiceDate,
# MAGIC     IFNULL(NDCDrugCode_q360,'') AS NDCDrugCode,
# MAGIC     IFNULL(Claimstatus_q360,'') AS ClaimStatus,
# MAGIC     IFNULL(QuantityDispensed_q360,'') AS QuantityDispensed,
# MAGIC     IFNULL(SupplementalData_q360,'') AS SupplementalData,
# MAGIC     IFNULL(DataSourceName_q360,'') AS DataSourceName,
# MAGIC     IFNULL(ProviderID_q360,'') AS ProviderID,
# MAGIC     IFNULL(ProviderNPI_q360,'') AS ProviderNPI,
# MAGIC     IFNULL(PharmacyNPI_q360,'') AS PharmacyNPI,
# MAGIC     IFNULL(ClaimId_q360,'') AS ClaimID,
# MAGIC     IFNULL(ClaimlineId_q360,'') AS ClaimlineID,
# MAGIC     IFNULL(Additional_coloumn_1_q360,'') AS Additionalcoloumn1,
# MAGIC     IFNULL(Additional_coloumn_2_q360,'') AS Additionalcoloumn2,
# MAGIC     IFNULL(Additional_coloumn_3_q360,'') AS Additionalcoloumn3,
# MAGIC     IFNULL(Additional_coloumn_4_q360,'') AS Additionalcoloumn4,
# MAGIC     IFNULL(Additional_coloumn_5_q360,'') AS Additionalcoloumn5,
# MAGIC     IFNULL(Filler_q360,'') AS Filler
# MAGIC
# MAGIC FROM view_OriginalQ360_Pharmacy

# COMMAND ----------

# DBTITLE 1,Loading and Transforming QSI file
# Assign QSI file from mounted location to a variable
file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location}'


#Load QSI file to the spark data frame 
df_pharm_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#Store the list of columns needed from the QSI Lab file
pharm_col_needed = ["MemberKey","DaysSupply","NDC","ClaimStatus",
                    "QuantityDispensed","SuppSource","ProviderKey",
                    "Prescribing NPI","Dispensing NPI","ClaimNumber"]

# QSI dataframe with required columns for Transdformation (Source)
df_pharm_qsi = df_pharm_qsi.select(pharm_col_needed)

# Renaming QSI columns with respect to Q360 files.
df_pharm_qsi = df_pharm_qsi.withColumnRenamed('DaysSupply','Dayssupply')\
                        .withColumnRenamed('NDC','NDCDrugCode')\
                        .withColumnRenamed('ProviderKey','ProviderID')\
                        .withColumnRenamed('Prescribing NPI','ProviderNPI')\
                        .withColumnRenamed('Dispensing NPI','PharmacyNPI') \
                        .withColumnRenamed('SuppSource','DataSourceName')
                          

df_pharm_qsi =  df_pharm_qsi.withColumn("Member_ID",substring(col("MemberKey"),0,16))\
                                          .withColumn("ClaimId",substring(col("ClaimNumber"),0,20))\
                                          .withColumn('Claim_status',when(col('ClaimStatus') == 'D', 2)\
                                                      .when(col('ClaimStatus').isin(['I','A']),1)\
                                                      .when(col('ClaimStatus') == 'P',3) \
                                                      .otherwise(4)) \
                                          .withColumn("Quantity_Dispensed",round(col("QuantityDispensed"),7))\
                                                                .drop("MemberKey","ClaimStatus","QuantityDispensed","ClaimNumber")

# # Columns ordered inside list to get same order as of Q360
final_column_qsi_to_q360 = ["Member_ID","Dayssupply","NDCDrugCode",
                            "Claim_status","Quantity_Dispensed","DataSourceName",
                            "ProviderID","ProviderNPI","PharmacyNPI","ClaimId"]

df_pharm_qsi = df_pharm_qsi.select(final_column_qsi_to_q360)



# COMMAND ----------

# DBTITLE 1,Loading converted QSI to containers
#Convert spark dataframe into pandas dataframe
pandas_qsi_pharm_df = df_pharm_qsi.toPandas()
#Convert pandas dataframe into a csv file
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
pandas_qsi_pharm_df.to_csv(f'{file_destination}QSI_to_Q360_pharmacy_converted_{date}.txt',
                     index = False,sep = '|') 

# COMMAND ----------

# DBTITLE 1,Joining Q360 and QSI dataframe for comparison
df_full_join_pharmacy = df_pharm_qsi.join(df_Q360_pharmacy, \
                    (df_pharm_qsi.Member_ID == df_Q360_pharmacy.Member_ID_q360), 'full')

# COMMAND ----------

# DBTITLE 1,Compare data from Q360 dataframe against the Converted QSI dataframe
#Comparison logic based on Member_ID

df_full_join_pharmacy = df_full_join_pharmacy.withColumn('Member_ID_status',when(col('Member_ID')== col('Member_ID_q360'),'Y') \
  .otherwise('N'))\
  .withColumn('Dayssupply_status',when(col('Member_ID')== col('Member_ID_q360'), \
  when(col('Dayssupply')== col('Dayssupply_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('NDCDrugCode_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('NDCDrugCode') == col('NDCDrugCode_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('Claim_status_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Claim_status') == col('Claimstatus_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('Quantity_Dispensed_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Quantity_Dispensed') == col('QuantityDispensed_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('DataSourceName_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('DataSourceName') == col('DataSourceName_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('ProviderID_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ProviderID') == col('ProviderID_q360'),'Y')\
     .otherwise('N')).otherwise('N')) \
  .withColumn('ProviderNPI_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ProviderNPI') == col('ProviderNPI_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('PharmacyNPI_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('PharmacyNPI') == col('PharmacyNPI_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('ClaimId_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ClaimId') == col('ClaimId_q360'),'Y')\
      .otherwise('N')).otherwise('N')) 


pharmacy_status_col = ['Member_ID','Member_ID_status','Dayssupply_status',
                       'NDCDrugCode_status','Claim_status_status', 
                       'Quantity_Dispensed_status','DataSourceName_status',
                       'ProviderID_status','ProviderNPI_status','PharmacyNPI_status',
                       'ClaimId_status']
         
df_full_join_pharmacy = df_full_join_pharmacy.select(pharmacy_status_col)

# COMMAND ----------

df_full_join_pharmacy.createOrReplaceTempView("view_PharmacyComparison_Results")

# COMMAND ----------

# DBTITLE 1,Drop table tblM_PharmacyComparison_Results
# MAGIC %sql 
# MAGIC DROP TABLE IF EXISTS tblM_PharmacyComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_PharmacyComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_PharmacyComparison_Results
# MAGIC (
# MAGIC
# MAGIC     Member_ID VARCHAR(16),
# MAGIC     IsRecordMatching CHAR(1),
# MAGIC     Member_ID_status CHAR(1),
# MAGIC     Dayssupply_status CHAR(1),
# MAGIC     ServiceDate_status CHAR(1),
# MAGIC     NDCDrugCode_status CHAR(1),
# MAGIC     Claim_status_status CHAR(1),
# MAGIC     Quantity_Dispensed_status CHAR(1),
# MAGIC     Supplemental_data_status CHAR(1),
# MAGIC     DataSourceName_status CHAR(1),
# MAGIC     ProviderID_status CHAR(1),
# MAGIC     ProviderNPI_status CHAR(1),
# MAGIC     PharmacyNPI_status CHAR(1),
# MAGIC     ClaimId_status CHAR(1),
# MAGIC     ClaimlineId_status CHAR(1)
# MAGIC     
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp view into tblM_PharmacyComparison_Results
# MAGIC %sql
# MAGIC INSERT INTO tblM_PharmacyComparison_Results
# MAGIC SELECT DISTINCT
# MAGIC     Member_ID,
# MAGIC     'Y' AS IsRecordMatching,
# MAGIC     Member_ID_status,
# MAGIC     Dayssupply_status,
# MAGIC     '' AS ServiceDate_status,
# MAGIC     NDCDrugCode_status,
# MAGIC     Claim_status_status, 
# MAGIC     Quantity_Dispensed_status,
# MAGIC     '' AS Supplemental_data_status,
# MAGIC     DataSourceName_status,
# MAGIC     ProviderID_status,
# MAGIC     ProviderNPI_status,
# MAGIC     PharmacyNPI_status,
# MAGIC     ClaimId_status,
# MAGIC     '' AS ClaimlineId_status
# MAGIC
# MAGIC FROM view_PharmacyComparison_Results

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the flags of the individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_PharmacyComparison_Results
# MAGIC     SET IsRecordMatching = CASE 
# MAGIC                                 WHEN Member_ID_status = 'N' OR
# MAGIC                                       Dayssupply_status = 'N' OR
# MAGIC                                       --ServiceDate_status = 'N' OR 
# MAGIC                                       NDCDrugCode_status = 'N' OR
# MAGIC                                       Claim_status_status = 'N' OR
# MAGIC                                       Quantity_Dispensed_status = 'N' OR
# MAGIC                                       --Supplemental_data_status = 'N' OR
# MAGIC                                       DataSourceName_status = 'N' OR
# MAGIC                                       ProviderID_status = 'N' OR
# MAGIC                                       ProviderNPI_status = 'N' OR
# MAGIC                                       PharmacyNPI_status = 'N' OR
# MAGIC                                       ClaimId_status = 'N' 
# MAGIC                                       -- OR ClaimlineId_status = 'N'
# MAGIC                                   THEN 'N'
# MAGIC                               ELSE 'Y'
# MAGIC                             END
# MAGIC

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
# MAGIC       'PHARMACY' AS FileType,
# MAGIC       (SELECT count(MemberID) FROM OriginalQ360_Pharmacy) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_PharmacyComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Pharmacy
# MAGIC       INNER JOIN tblM_PharmacyComparison_Results
# MAGIC       on OriginalQ360_Pharmacy.MemberID = tblM_PharmacyComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_PharmacyComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Pharmacy
# MAGIC       FULL OUTER JOIN tblM_PharmacyComparison_Results
# MAGIC       on OriginalQ360_Pharmacy.MemberID = tblM_PharmacyComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords

# COMMAND ----------

# DBTITLE 1,Load the File level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')

#Convert spark dataframe into pandas dataframe
df_final_status = df_final.toPandas()

#Copy data from pandas dataframe to csv file
df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Pharmacy_final_status_{date}.csv')


# COMMAND ----------

# DBTITLE 1,Load the Record level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Pharmacy = spark.sql('SELECT * FROM tblM_PharmacyComparison_Results ORDER BY Member_ID')

#Convert spark dataframe into pandas dataframe
df_Pharmacy_Pandas = df_Pharmacy.toPandas()

#Copy data from pandas dataframe to csv file
df_Pharmacy_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Pharmacy_Comparison_{date}.csv')


# COMMAND ----------

# DBTITLE 1,Notebook exit comment to show the status of the run
dbutils.notebook.exit("Success")
