# Databricks notebook source
# MAGIC %md
# MAGIC ## 7_Basic_Transform_MMDF

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
qsi_location_mem_gen = dbutils.widgets.get("location2")
qsi_location_mem_enroll = dbutils.widgets.get("location3")
destination_location = dbutils.widgets.get("destination_location")

# COMMAND ----------

# DBTITLE 1,Load Original Q360 MMDF file to spark dataframe
#Assign the Original Q360 file path to a variable
file_path_Q360_mmdf = f'/mnt/{clientName}/Q360/Q360/{q360_location}'

#Create schema for the dataframe as per the Q360 MMDF file layout
mmdf_schema = StructType([
    StructField("Contract_Number", StringType(),True),
    StructField("Run_Date", StringType(),True),
    StructField("Payment_Date", StringType(),True),
    StructField("Beneficiary_ID", StringType(),True),
    StructField("Surname", StringType(),True),
    StructField("First_Initial", StringType(),True),
    StructField("Gender_Code", StringType(),True),
    StructField("Date_of_Birth", StringType(),True),
    StructField("Filler01", StringType(),True),
    StructField("State_and_County_Code", StringType(),True),
    StructField("Out_of_Area_Indicator", StringType(),True),
    StructField("Part_A_Entitlement", StringType(),True),
    StructField("Part_B_Entitlement", StringType(),True),
    StructField("HospiceFlag", StringType(),True),
    StructField("ESRD", StringType(),True),
    StructField("Aged_or_Disabled_MSP", StringType(),True),
    StructField("Filler02", StringType(),True),
    StructField("Filler03", StringType(),True),
    StructField("New_Medicare_Beneficiary_Medicaid_Status_Flag", StringType(),True),
    StructField("LTI_Flag", StringType(),True),
    StructField("Medicaid_Addon_Factor_Indicator", StringType(),True),
    StructField("Filler04", StringType(),True),
    StructField("Default_Risk_Factor_Code", StringType(),True),
    StructField("Risk_Adjustment_Factor_A", StringType(),True),
    StructField("Risk_Adjustment_Factor_B", StringType(),True),
    StructField("Number_of_Payment_or_Adjustment_Months_Part_A", StringType(),True),
    StructField("Number_of_Payment_or_Adjustment_Months_Part_B", StringType(),True),
    StructField("Adjustment_Reason_Code", StringType(),True),
    StructField("Payment_or_Adjustment_Start_Date", StringType(),True),
    StructField("Payment_or_Adjustment_End_Date", StringType(),True),
    StructField("Filler05", StringType(),True),
    StructField("Filler06", StringType(),True),
    StructField("Monthly_Risk_Adjusted_Amount_Part_A", StringType(),True),
    StructField("Monthly_Risk_Adjusted_Amount_Part_B", StringType(),True),
    StructField("LIS_Premium_Subsidy", StringType(),True),
    StructField("ESRD_MSP_Flag", StringType(),True),
    StructField("Medication_Therapy_Management_Add_On", StringType(),True),
    StructField("Filler07", StringType(),True),
    StructField("Medicaid_Full_or_Partial_or_Non_dual", StringType(),True),
    StructField("Risk_Adjustment_Age_Group_RAAG", StringType(),True),
    StructField("Filler08", StringType(),True),
    StructField("Filler09", StringType(),True),
    StructField("Filler10", StringType(),True),
    StructField("Plan_Benefit_Package_ID", StringType(),True),
    StructField("Filler11", StringType(),True),
    StructField("Risk_Adjustment_Factor_Type_Code", StringType(),True),
    StructField("Frailty_Indicator_PACE_or_FIDE_SNP_only", StringType(),True),
    StructField("Original_Reason_for_Entitlement_Code_OREC", StringType(),True),
    StructField("Filler12", StringType(),True),
    StructField("Segment_Number", StringType(),True),
    StructField("Filler13", StringType(),True),
    StructField("EGHP_Flag", StringType(),True),
    StructField("Part_C_Basic_Premium_Part_A_Amount", StringType(),True),
    StructField("Part_C_Basic_Premium_Part_B_Amount", StringType(),True),
    StructField("Rebate_for_Part_A_Cost_Sharing_Reduction", StringType(),True),
    StructField("Rebate_for_Part_B_Cost_Sharing_Reduction", StringType(),True),
    StructField("Rebate_for_Other_Part_A_Mandatory_Supplemental_Benefits", StringType(),True),
    StructField("Rebate_for_Other_Part_B_Mandatory_Supplemental_Benefits", StringType(),True),
    StructField("Rebate_for_Part_B_Premium_Reduction_Part_A_Amount", StringType(),True),
    StructField("Rebate_for_Part_B_Premium_Reduction_Part_B_Amount", StringType(),True),
    StructField("Rebate_for_Part_D_Supplemental_Benefits_Part_A_Amount", StringType(),True),
    StructField("Rebate_for_Part_D_Supplemental_Benefits_Part_B_Amount", StringType(),True),
    StructField("Total_MA_Payment_or_Adjustment_Part_A", StringType(),True),
    StructField("Total_MA_Payment_or_Adjustment_Part_B", StringType(),True),
    StructField("Total_MA_Part_C_Payment_or_Adjustment", StringType(),True),
    StructField("Risk_Adjustment_Factor_D", StringType(),True),
    StructField("Part_D_Low-Income_Indicator", StringType(),True),
    StructField("Part_D_Low-Income_Multiplier", StringType(),True),
    StructField("Part_D_Long_Term_Institutional_Indicator", StringType(),True),
    StructField("Part_D_Long_Term_Institutional_Multiplier", StringType(),True),
    StructField("Rebate_for_Part_D_Basic_Premium_Reduction", StringType(),True),
    StructField("Part_D_Basic_Premium_Amount", StringType(),True),
    StructField("Part_D_Direct_Subsidy_Amount", StringType(),True),
    StructField("Reinsurance_Subsidy_Amount", StringType(),True),
    StructField("Low_Income_Subsidy_Cost_Sharing_Amount", StringType(),True),
    StructField("Total_Part_D_Payment_or_Adjustment", StringType(),True),
    StructField("Number_of_Payment_or_Adjustment_Months_Part_D", StringType(),True),
    StructField("PACE_Premium_Add_On", StringType(),True),
    StructField("PACE_Cost_Sharing_Addon", StringType(),True),
    StructField("Part_C_Frailty_Factor", StringType(),True),
    StructField("MSP_Reduction_Factor", StringType(),True),
    StructField("MSP_Reduction_Amount_Part_A", StringType(),True),
    StructField("MSP_Reduction_Amount_Part_B", StringType(),True),
    StructField("Medicaid_Dual_Status_Code", StringType(),True),
    StructField("Part_D_Coverage_Gap_Discount_Amount", StringType(),True),
    StructField("Part_D_Risk_Adjustment_Factor_Type", StringType(),True),
    StructField("Part_D_Default_Risk_Factor_Code", StringType(),True),
    StructField("Part_A_Monthly_Rate_for_Payment_or_Adjustment", StringType(),True),
    StructField("Part_B_Monthly_Rate_for_Payment_or_Adjustment", StringType(),True),
    StructField("Part_D_Monthly_Rate_for_Payment_or_Adjustment", StringType(),True),
    StructField("Cleanup_ID", StringType(),True)

    ])

#Load the spark dataframe based on the schema
df_Q360_mmdf = spark.read.option("delimiter",'|').schema(mmdf_schema).csv(file_path_Q360_mmdf)

df_Q360_mmdf = df_Q360_mmdf.select("Beneficiary_ID","Payment_or_Adjustment_Start_Date",\
                                    "Payment_or_Adjustment_End_Date","HospiceFlag","ESRD",\
                                    "LTI_Flag","Original_Reason_for_Entitlement_Code_OREC")



# COMMAND ----------

# DBTITLE 1,Load data from dataframe into Temp view
df_Q360_mmdf.createOrReplaceTempView("view_OriginalQ360_MMDF_data")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360_MMDF
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_MMDF

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360_MMDF
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_MMDF
# MAGIC (
# MAGIC     MBI VARCHAR(12),
# MAGIC     Startdate VARCHAR(8),
# MAGIC     Enddate VARCHAR(8),
# MAGIC     Hospice CHAR(1),
# MAGIC     --ESRD CHAR(1),
# MAGIC     LTI CHAR(1),
# MAGIC     OREC CHAR(1)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp view into table OriginalQ360_Lab
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_MMDF
# MAGIC SELECT DISTINCT 
# MAGIC     IFNULL(Beneficiary_ID,'') AS MBI,
# MAGIC     IFNULL(Payment_or_Adjustment_Start_Date,'') AS Startdate,
# MAGIC     IFNULL(Payment_or_Adjustment_End_Date,'') AS Enddate,
# MAGIC     IFNULL(HospiceFlag,'') AS Hospice,
# MAGIC     --IFNULL(ESRD,'') AS ESRD,
# MAGIC     IFNULL(LTI_Flag,'') AS LTI,
# MAGIC     IFNULL(Original_Reason_for_Entitlement_Code_OREC,'') AS OREC
# MAGIC
# MAGIC FROM view_OriginalQ360_MMDF_data

# COMMAND ----------

# DBTITLE 1,Transform QSI Member general and enrollment file and load to spark dataframe
# Assign QSI file from mounted location to a variable
file_path_MemGen_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location_mem_gen}'
file_path_MemEnroll_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location_mem_enroll}'

#Assign destination path for Converted QSI file to a variable
file_destination = f'/mnt/{clientName}/Q360/QSI_Converted/'

#Load Member General QSI file to the spark data frame 
df_mem_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_MemGen_QSI)

#Store the list of columns needed from the QSI Member General file
mem_col_needed = ["MemberKey","MedicareID"]

# QSI dataframe with required columns for Transformation (Source1)
df_mem_qsi = df_mem_qsi.select(mem_col_needed)

#Load Member enrollment QSI file to the spark data frame 
df_memenroll_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_MemEnroll_QSI)

#Store the list of columns needed from the QSI Member enrollment file
memenroll_col_needed = ["MemberKey","EffectiveDate","TerminationDate","HospiceFlag","LTIFlag","OREC"]

# QSI dataframe with required columns for Transformation (Source2)
df_memenroll_qsi = df_memenroll_qsi.select(memenroll_col_needed)

# Perform the inner join operation with df_mem_qsi and df_memenroll_qsi
df_mmdf_qsi = df_mem_qsi.join(df_memenroll_qsi, (df_mem_qsi.MemberKey == df_memenroll_qsi.MemberKey), 'inner')


#Transforming QSI data into Q360 format
df_mmdf_qsi =  df_mmdf_qsi.withColumn("BeneficiaryID",substring(col("MedicareID"),0,12))\
                          .withColumn("Startdate",date_format("EffectiveDate",'yyyyMMdd')) \
                          .withColumn("Enddate",date_format("TerminationDate",'yyyyMMdd')) \
                          .withColumn("Hospice",when(col('HospiceFlag') == '1','Y').otherwise(' '))\
                          .withColumn("LTI",when(col('LTIFlag') == '1','Y').otherwise(' '))

final_col = ["BeneficiaryID","Startdate","Enddate","Hospice","LTI","OREC"]

df_mmdf_qsi = df_mmdf_qsi.select(final_col)

#display(df_mmdf_qsi)


# COMMAND ----------

# DBTITLE 1,Saving the converted QSI to containers
#Convert spark dataframe into pandas dataframe
pandas_qsi_df = df_mmdf_qsi.toPandas()

#Convert pandas dataframe into a csv file
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
pandas_qsi_df.to_csv(f'{file_destination}QSI_to_Q360_mmdf_converted_{date}.txt',
                     index = False,sep = '|') 

# COMMAND ----------

# DBTITLE 1,Join QSI and Q360 Dataframes
# Perform the full outer join operation with df_q360 and qsi
df_mmdf_full_join = df_Q360_mmdf.join(df_mmdf_qsi,
                                      (df_Q360_mmdf.Beneficiary_ID == df_mmdf_qsi.BeneficiaryID), 'full')

#display(df_mmdf_full_join)


# COMMAND ----------

# DBTITLE 1,Comparing Q360 and QSI dataframes
df_mmdf_full_join = df_mmdf_full_join.withColumn('Beneficiary_ID_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'),'Y') \
                                            .otherwise('N')) \
                                    .withColumn('Startdate_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'), \
                                            when(col('Payment_or_Adjustment_Start_Date')== col('Startdate'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('Enddate_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'), \
                                            when(col('Payment_or_Adjustment_End_Date')== col('Enddate'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('Hospice_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'), \
                                            when(col('HospiceFlag')== col('Hospice'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('LTI_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'), \
                                            when(col('LTI_Flag')== col('LTI'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) \
                                    .withColumn('OREC_status',\
                                        when(col('Beneficiary_ID') == col('BeneficiaryID'), \
                                            when(col('Original_Reason_for_Entitlement_Code_OREC')== col('OREC'),'Y')\
                                                .otherwise('N'))\
                                        .otherwise('N')) 
                                  

mmdf_status_columns = ['Beneficiary_ID','Beneficiary_ID_status',
                      'Startdate_status','Enddate_status', 
                      'Hospice_status','LTI_status','OREC_status']

df_mmdf_full_join = df_mmdf_full_join.select(mmdf_status_columns)

# display(df_mmdf_full_join)

# COMMAND ----------

# DBTITLE 1,Load Comparison results from spark dataframe to Temp view
df_mmdf_full_join.createOrReplaceTempView('view_MmdfComparison_Results')

# COMMAND ----------

# DBTITLE 1,Drop table tblM_MmdfComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_MmdfComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_MmdfComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_MmdfComparison_Results
# MAGIC (
# MAGIC
# MAGIC     Beneficiary_ID VARCHAR(12),
# MAGIC     IsRecordMatching CHAR(1),
# MAGIC     Beneficiary_ID_status CHAR(1),
# MAGIC     Startdate_status CHAR(1),
# MAGIC     Enddate_status CHAR(1),
# MAGIC     Hospice_status CHAR(1),
# MAGIC     LTI_status CHAR(1),
# MAGIC     OREC_status CHAR(1)
# MAGIC     
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp View into table tblM_MmdfComparison_Results
# MAGIC %sql
# MAGIC INSERT INTO tblM_MmdfComparison_Results
# MAGIC SELECT DISTINCT 
# MAGIC     Beneficiary_ID,
# MAGIC     'Y' AS IsRecordMatching,
# MAGIC     Beneficiary_ID_status,
# MAGIC     Startdate_status,
# MAGIC     Enddate_status,
# MAGIC     Hospice_status,
# MAGIC     LTI_status,
# MAGIC     OREC_status
# MAGIC     
# MAGIC FROM view_MmdfComparison_Results

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the flags of the individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_MmdfComparison_Results
# MAGIC     SET IsRecordMatching = CASE 
# MAGIC                                 WHEN Beneficiary_ID_status = 'N' OR
# MAGIC                                       Startdate_status = 'N' OR
# MAGIC                                       Enddate_status = 'N' OR
# MAGIC                                       Hospice_status = 'N' OR
# MAGIC                                       LTI_status = 'N' OR
# MAGIC                                       OREC_status = 'N'
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
# MAGIC       'MMDF' AS FileType,
# MAGIC       (SELECT count(MBI) FROM OriginalQ360_MMDF) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_MmdfComparison_Results.Beneficiary_ID) 
# MAGIC       FROM OriginalQ360_MMDF
# MAGIC       INNER JOIN tblM_MmdfComparison_Results
# MAGIC       on OriginalQ360_MMDF.MBI = tblM_MmdfComparison_Results.Beneficiary_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_MmdfComparison_Results.Beneficiary_ID) 
# MAGIC       FROM OriginalQ360_MMDF
# MAGIC       FULL OUTER JOIN tblM_MmdfComparison_Results
# MAGIC       on OriginalQ360_MMDF.MBI = tblM_MmdfComparison_Results.Beneficiary_ID
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
df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/MMDF_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Load the Record level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Mmdf = spark.sql('SELECT * FROM tblM_MmdfComparison_Results ORDER BY Beneficiary_ID')

#Convert spark dataframe into pandas dataframe
df_Mmdf_Pandas = df_Mmdf.toPandas()

#Copy data from pandas dataframe to csv file
df_Mmdf_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/MMDF_Comparison_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Notebook exit comment to show the status of the run
dbutils.notebook.exit("Success")
