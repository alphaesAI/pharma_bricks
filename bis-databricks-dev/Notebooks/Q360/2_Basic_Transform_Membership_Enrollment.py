# Databricks notebook source
# MAGIC %md 
# MAGIC ##2_Basic_Transform_Membership_Enrollment

# COMMAND ----------

# DBTITLE 1,Import Python Libraries
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col,substring,expr,date_format,when
from pyspark.sql.types import StringType,StructType,StructField

# COMMAND ----------

# DBTITLE 1, Cell to receive location parameters from  master notebook
clientName = dbutils.widgets.get("clientname")
q360_location = dbutils.widgets.get("location")
qsi_location = dbutils.widgets.get("location2")
destination_location = dbutils.widgets.get("destination_location")

# COMMAND ----------

# DBTITLE 1,Loading member_enroll QSI file and Transforming
# Assign QSI file from mounted location to a variable

file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location}'
#Load QSI file to the spark data frame 
df_member_enroll_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

qsi_mem_enroll_col_needed = ['MemberKey',
                            'EffectiveDate','TerminationDate',
                            'DentalFlag','RxFlag',
                            'MentalHealthInpatientFlag','MentalHealthDayNightFlag','MentalHealthAmbulFlag','ChemDependInpatientFlag','ChemDependDayNightFlag','ChemDependAmbulFlag', 'LTSSBenefitFlag']

df_member_enroll_qsi = df_member_enroll_qsi.select(qsi_mem_enroll_col_needed)


# Transforming the QSI dataframe to Q360 format
df_member_enroll_qsi = df_member_enroll_qsi.withColumn("Member_ID",substring(col("MemberKey"),0,16))\
                          .withColumn("Enrolment_Start_Date",date_format("EffectiveDate",'yyyyMMdd'))\
                          .withColumn("DisEnrolment_Date",date_format("TerminationDate",'yyyyMMdd')) \
                          .withColumn("Dental_Benefit",when(col("DentalFlag") == 1,'Y').otherwise('N')) \
                          .withColumn("Drug_Benefit",when(col("RxFlag") == 1,'Y').otherwise('N')) \
                          .withColumn("Mental_Health_Benefit_Inpatient",\
                            when(col("MentalHealthInpatientFlag") == 1,'Y')\
                            .otherwise('N')) \
                          .withColumn("Mental_Health_Benefit_Intensive_Outpatient",\
                            when(col("MentalHealthDayNightFlag") == 1,'Y')\
                            .otherwise('N')) \
                          .withColumn("Mental_Health_Benefit_Outpatient_ED",\
                            when(col("MentalHealthAmbulFlag") == 1,'Y')\
                            .otherwise('N'))\
                          .withColumn("ChemDep_Benefit_Inpatient",\
                            when(col("ChemDependInpatientFlag") == 1,'Y')\
                            .otherwise('N')) \
                          .withColumn("ChemDep_Benefit_Intensive_Outpatient",\
                            when(col("ChemDependDayNightFlag") == 1,'Y')\
                            .otherwise('N'))\
                          .withColumn("ChemDep_Benefit_Outpatient_ED",\
                            when(col("ChemDependAmbulFlag") == 1,'Y')\
                            .otherwise('N'))\
                          .withColumn("Institutional_LTSS_Benefit",\
                            when(col("LTSSBenefitFlag") == 1,'Y')\
                            .otherwise('N'))\
                          .drop("MemberKey",
                                "EffectiveDate","TerminationDate",
                                "DentalFlag","RxFlag",
                                "MentalHealthInpatientFlag","MentalHealthDayNightFlag","MentalHealthAmbulFlag","ChemDependInpatientFlag","ChemDependDayNightFlag","ChemDependAmbulFlag","LTSSBenefitFlag")

#display(df_member_enroll_qsi)


# COMMAND ----------

# DBTITLE 1,Saving the transformed QSI dataframe to container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'
df_member_enroll_qsi_toContainer = df_member_enroll_qsi.toPandas()
df_member_enroll_qsi_toContainer.to_csv(f'{file_destination}QSI_to_Q360_member_enroll_converted_{date}.txt',
                     index = False,sep = '|') 

# COMMAND ----------

# DBTITLE 1,Load the Original Q360 Member Enrollment files
file_path_Q360_member_enroll = f'/mnt/{clientName}/Q360/Q360/{q360_location}' 

member_enroll_schema = StructType([
    StructField("Member_ID_q360", StringType(),True),
    StructField("Enrolment_Start_Date_q360", StringType(), True),
    StructField("DisEnrolment_Date_q360", StringType(), True),
    StructField("Dental_Benefit_q360", StringType(),True),
    StructField("Drug_Benefit_q360", StringType(), True),
    StructField("Mental_Health_Benefit_Inpatient_q360", StringType(), True),
    StructField("Mental_Health_Benefit_Intensive_Outpatient_q360", StringType(),True),
    StructField("Mental_Health_Benefit_Outpatient_ED_q360", StringType(), True),
    StructField("ChemDep_Benefit_Inpatient_q360", StringType(), True),
    StructField("ChemDep_Benefit_Intensive_Outpatient_q360", StringType(),True),
    StructField("ChemDep_Benefit_Outpatient_ED_q360", StringType(), True),
    StructField("Medical_Benefit_q360", StringType(), True),
    StructField("Institutional_LTSS_Benefit_q360", StringType(),True),
    StructField("Home_and_Community_LTSS_Benefit_q360", StringType(), True),
    StructField("Payer_q360", StringType(), True),
    StructField("Health_Plan_Employee_dependant_Flag_q360", StringType(),True),
    StructField("Indicator_q360", StringType(), True),
    StructField("Primary_Enrolment_Flag_q360", StringType(), True),
    StructField("Product_ID_q360", StringType(),True),
    StructField("Reporting_ID_q360", StringType(), True),
    StructField("Member_Group_Code_q360", StringType(), True),
    StructField("Additional_coloumn_1_q360", StringType(),True),
    StructField("Additional_coloumn_2_q360", StringType(), True),
    StructField("Additional_coloumn_3_q360", StringType(), True),
    StructField("Additional_coloumn_4_q360", StringType(),True),
    StructField("Additional_coloumn_5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])

df_Q360_member_enroll  = spark.read.option("delimiter",'|').schema(member_enroll_schema).csv(file_path_Q360_member_enroll)
#display(df_Q360_member_enroll)

# COMMAND ----------

# DBTITLE 1,Load Original Q360 Member Enrollment data into Temp View
df_Q360_member_enroll.createOrReplaceTempView("view_OriginalMemberEnrollData")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360_MemberEnrollment
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_MemberEnrollment

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360_MemberEnrollment
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_MemberEnrollment
# MAGIC (
# MAGIC   MemberID VARCHAR(16),
# MAGIC   EnrollmentStartDate VARCHAR(8),
# MAGIC   DisEnrollmentDate VARCHAR(8),
# MAGIC   DentalBenefit CHAR(1),
# MAGIC   DrugBenefit CHAR(1),
# MAGIC   MHBInpatient CHAR(1),
# MAGIC   MHBIntensiveOutpatient CHAR(1),
# MAGIC   MHBOutpatient CHAR(1),
# MAGIC   CDBInpatient CHAR(1),
# MAGIC   CDBIntensiveOutpatient CHAR(1),
# MAGIC   CDBOutpatientED CHAR(1),
# MAGIC   MedicalBenefit CHAR(1),
# MAGIC   InstitutionalLTSSBenefit CHAR(1),
# MAGIC   HomeandCommunityLTSSBenefit CHAR(1),
# MAGIC   Payer VARCHAR(3),
# MAGIC   HealthPlanEmployeedependantFlag CHAR(1),
# MAGIC   Indicator VARCHAR(10),
# MAGIC   PrimaryEnrolmentFlag CHAR(1),
# MAGIC   ProductID VARCHAR(3),
# MAGIC   ReportingID VARCHAR(3),
# MAGIC   MemberGroupCode VARCHAR(10),
# MAGIC   Additionalcoloumn1 VARCHAR(10),
# MAGIC   Additionalcoloumn2 VARCHAR(10),
# MAGIC   Additionalcoloumn3 VARCHAR(10),
# MAGIC   Additionalcoloumn4 VARCHAR(30),
# MAGIC   Additionalcoloumn5 VARCHAR(30),
# MAGIC   Filler VARCHAR(200)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp View into OriginalQ360_MemberEnrollment
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_MemberEnrollment
# MAGIC SELECT DISTINCT
# MAGIC   Member_ID_q360 AS MemberID,
# MAGIC   Enrolment_Start_Date_q360 AS EnrollmentStartDate,
# MAGIC   DisEnrolment_Date_q360 AS DisEnrollmentDate,
# MAGIC   Dental_Benefit_q360 AS DentalBenefit,
# MAGIC   Drug_Benefit_q360 AS DrugBenefit,
# MAGIC   Mental_Health_Benefit_Inpatient_q360 AS MHBInpatient,
# MAGIC   Mental_Health_Benefit_Intensive_Outpatient_q360 AS MHBIntensiveOutpatient,
# MAGIC   Mental_Health_Benefit_Outpatient_ED_q360 AS MHBOutpatient,
# MAGIC   ChemDep_Benefit_Inpatient_q360 AS CDBInpatient,
# MAGIC   ChemDep_Benefit_Intensive_Outpatient_q360 AS CDBIntensiveOutpatient,
# MAGIC   ChemDep_Benefit_Outpatient_ED_q360 AS CDBOutpatientED,
# MAGIC   Medical_Benefit_q360 AS MedicalBenefit,
# MAGIC   Institutional_LTSS_Benefit_q360 AS InstitutionalLTSSBenefit,
# MAGIC   Home_and_Community_LTSS_Benefit_q360 AS HomeandCommunityLTSSBenefit,
# MAGIC   Payer_q360 AS Payer,
# MAGIC   Health_Plan_Employee_dependant_Flag_q360 AS HealthPlanEmployeedependantFlag,
# MAGIC   Indicator_q360 AS Indicator,
# MAGIC   Primary_Enrolment_Flag_q360 AS PrimaryEnrolmentFlag,
# MAGIC   Product_ID_q360 AS ProductID,
# MAGIC   Reporting_ID_q360 AS ReportingID,
# MAGIC   Member_Group_Code_q360 AS MemberGroupCode,
# MAGIC   Additional_coloumn_1_q360 AS Additionalcoloumn1,
# MAGIC   Additional_coloumn_2_q360 AS Additionalcoloumn2,
# MAGIC   Additional_coloumn_3_q360 AS Additionalcoloumn3,
# MAGIC   Additional_coloumn_4_q360 AS Additionalcoloumn4,
# MAGIC   Additional_coloumn_5_q360 AS Additionalcoloumn5,
# MAGIC   Filler_q360 AS Filler
# MAGIC   
# MAGIC FROM view_OriginalMemberEnrollData

# COMMAND ----------

# DBTITLE 1,Joining Q360 member_enroll with QSI converted file for comparison
df_full_join_member_enroll = df_member_enroll_qsi.join(df_Q360_member_enroll, \
                    (df_member_enroll_qsi.Member_ID == df_Q360_member_enroll.Member_ID_q360), 'full')
#display(df_full_join_member_enroll)

# COMMAND ----------

# DBTITLE 1,Compare data from Q360 dataframe against the Converted QSI dataframe
#Comparison logic based on Member_ID

df_full_join_member_enroll = df_full_join_member_enroll.withColumn('Member_ID_status',when(col('Member_ID')== col('Member_ID_q360'),'Y') \
  .otherwise('N'))\
  .withColumn('Enrolment_Start_Date_status',when(col('Member_ID')== col('Member_ID_q360'), \
  when(col('Enrolment_Start_Date')== col('Enrolment_Start_Date_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('DisEnrolment_Date_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('DisEnrolment_Date') == col('DisEnrolment_Date_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('Dental_Benefit_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Dental_Benefit') == col('Dental_Benefit_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('Drug_Benefit_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Drug_Benefit') == col('Drug_Benefit_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('Mental_Health_Benefit_Inpatient_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Mental_Health_Benefit_Inpatient') == col('Mental_Health_Benefit_Inpatient_q360'),'Y').otherwise('N')).otherwise('N'))\
  .withColumn('Mental_Health_Benefit_Intensive_Outpatient_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Mental_Health_Benefit_Intensive_Outpatient') == col('Mental_Health_Benefit_Intensive_Outpatient_q360'),'Y')\
     .otherwise('N')).otherwise('N')) \
  .withColumn('Mental_Health_Benefit_Outpatient_ED_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Mental_Health_Benefit_Outpatient_ED') == col('Mental_Health_Benefit_Outpatient_ED_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('ChemDep_Benefit_Inpatient_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ChemDep_Benefit_Inpatient') == col('ChemDep_Benefit_Inpatient_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('ChemDep_Benefit_Intensive_Outpatient_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ChemDep_Benefit_Intensive_Outpatient') == col('ChemDep_Benefit_Intensive_Outpatient_q360'),'Y')\
      .otherwise('N')).otherwise('N')) \
  .withColumn('ChemDep_Benefit_Outpatient_ED_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('ChemDep_Benefit_Outpatient_ED') == col('ChemDep_Benefit_Outpatient_ED_q360'),'Y').otherwise('N')).otherwise('N')) \
  .withColumn('Institutional_LTSS_Benefit_status',when(col('Member_ID')== col('Member_ID_q360'),\
    when(col('Institutional_LTSS_Benefit') == col('Institutional_LTSS_Benefit_q360'),'Y').otherwise('N')).otherwise('N')) 
  

mem_enroll_status_col = ['Member_ID','Member_ID_status','Enrolment_Start_Date_status','DisEnrolment_Date_status','Dental_Benefit_status', 
        'Drug_Benefit_status','Mental_Health_Benefit_Inpatient_status','Mental_Health_Benefit_Intensive_Outpatient_status','Mental_Health_Benefit_Outpatient_ED_status','ChemDep_Benefit_Inpatient_status','ChemDep_Benefit_Intensive_Outpatient_status',
         'ChemDep_Benefit_Outpatient_ED_status','Institutional_LTSS_Benefit_status']
         
df_full_join_member_enroll = df_full_join_member_enroll.select(mem_enroll_status_col)
#display(df_full_join_member_enroll)

# COMMAND ----------

# DBTITLE 1,Load comparison results into Temp View
df_full_join_member_enroll.createOrReplaceTempView("view_MemberEnrollmentComparison_Results")

# COMMAND ----------

# DBTITLE 1,Drop table tblM_MemberEnrollmentComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_MemberEnrollmentComparison_Results 

# COMMAND ----------

# DBTITLE 1,Create table tblM_MemberEnrollmentComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_MemberEnrollmentComparison_Results
# MAGIC (
# MAGIC   Member_ID VARCHAR(16),
# MAGIC   IsRecordMatching CHAR(1),
# MAGIC   Member_ID_status CHAR(1),
# MAGIC   Enrolment_Start_Date_status CHAR(1),
# MAGIC   DisEnrolment_Date_status CHAR(1),
# MAGIC   Dental_Benefit_status CHAR(1),
# MAGIC   Drug_Benefit_status CHAR(1),
# MAGIC   Mental_Health_Benefit_Inpatient_status CHAR(1),
# MAGIC   Mental_Health_Benefit_Intensive_Outpatient_status CHAR(1),
# MAGIC   Mental_Health_Benefit_Outpatient_ED_status CHAR(1),
# MAGIC   ChemDep_Benefit_Inpatient_status CHAR(1),
# MAGIC   ChemDep_Benefit_Intensive_Outpatient_status CHAR(1),
# MAGIC   ChemDep_Benefit_Outpatient_ED_status CHAR(1),
# MAGIC   Institutional_LTSS_Benefit_status CHAR(1)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load comparison results from Temp View into table tblM_MemberEnrollmentComparison_Results
# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO tblM_MemberEnrollmentComparison_Results
# MAGIC SELECT DISTINCT
# MAGIC   Member_ID,
# MAGIC   'Y' AS IsRecordMatching ,
# MAGIC   Member_ID_status ,
# MAGIC   Enrolment_Start_Date_status ,
# MAGIC   DisEnrolment_Date_status ,
# MAGIC   Dental_Benefit_status ,
# MAGIC   Drug_Benefit_status ,
# MAGIC   Mental_Health_Benefit_Inpatient_status ,
# MAGIC   Mental_Health_Benefit_Intensive_Outpatient_status ,
# MAGIC   Mental_Health_Benefit_Outpatient_ED_status ,
# MAGIC   ChemDep_Benefit_Inpatient_status ,
# MAGIC   ChemDep_Benefit_Intensive_Outpatient_status ,
# MAGIC   ChemDep_Benefit_Outpatient_ED_status ,
# MAGIC   Institutional_LTSS_Benefit_status
# MAGIC
# MAGIC FROM view_MemberEnrollmentComparison_Results
# MAGIC

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the status of individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_MemberEnrollmentComparison_Results
# MAGIC   SET IsRecordMatching = CASE 
# MAGIC                             WHEN Member_ID_status  = 'N' OR
# MAGIC                                 Enrolment_Start_Date_status  = 'N' OR
# MAGIC                                 DisEnrolment_Date_status  = 'N' OR
# MAGIC                                 Dental_Benefit_status  = 'N' OR
# MAGIC                                 Drug_Benefit_status  = 'N' OR
# MAGIC                                 Mental_Health_Benefit_Inpatient_status  = 'N' OR
# MAGIC                                 Mental_Health_Benefit_Intensive_Outpatient_status  = 'N' OR
# MAGIC                                 Mental_Health_Benefit_Outpatient_ED_status  = 'N' OR
# MAGIC                                 ChemDep_Benefit_Inpatient_status  = 'N' OR
# MAGIC                                 ChemDep_Benefit_Intensive_Outpatient_status  = 'N' OR
# MAGIC                                 ChemDep_Benefit_Outpatient_ED_status  = 'N' OR
# MAGIC                                 Institutional_LTSS_Benefit_status  = 'N'
# MAGIC                               THEN 'N'
# MAGIC                             ELSE 'Y'
# MAGIC                         END

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

# DBTITLE 1,Load Comparison results to table tblM_Q360_Comparison_Results
# MAGIC %sql
# MAGIC INSERT INTO tblM_Q360_Comparison_Results
# MAGIC SELECT  
# MAGIC       'ABC' AS Client,
# MAGIC       getdate() AS RunDateTime,
# MAGIC       'MEMBER_ENROLLMENT' AS FileType,
# MAGIC       (SELECT count(MemberID) FROM OriginalQ360_MemberEnrollment) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_MemberEnrollmentComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_MemberEnrollment
# MAGIC       INNER JOIN tblM_MemberEnrollmentComparison_Results
# MAGIC       on OriginalQ360_MemberEnrollment.MemberID = tblM_MemberEnrollmentComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_MemberEnrollmentComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_MemberEnrollment
# MAGIC       FULL OUTER JOIN tblM_MemberEnrollmentComparison_Results
# MAGIC       on OriginalQ360_MemberEnrollment.MemberID = tblM_MemberEnrollmentComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords
# MAGIC

# COMMAND ----------

# DBTITLE 1,Saving the Q360 Comparison results to a csv file 
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')
df_final_status = df_final.toPandas()
df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/MemberEnrollment_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Save the Member Enrollment Comparison results to a csv file
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_MemberEnrollment = spark.sql('SELECT * FROM tblM_MemberEnrollmentComparison_Results ORDER BY Member_ID')
df_MemberEnrollment_Pandas = df_MemberEnrollment.toPandas()

df_MemberEnrollment_Pandas\
  .to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/MemberEnrollment_Comparison_{date}.csv') 

# COMMAND ----------

# DBTITLE 1,Notebook exit comment to give status of notebook run
dbutils.notebook.exit("Success")
