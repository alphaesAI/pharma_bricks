# Databricks notebook source
# MAGIC %md
# MAGIC ##3_Basic_Transform_Visit

# COMMAND ----------

# DBTITLE 1,Required Libraries
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col,substring,expr,date_format,when
from pyspark.sql.types import StringType,StructType,StructField

# COMMAND ----------

# DBTITLE 1, Cell to receive location parameters from ADF pipeline through master notebook
clientName = dbutils.widgets.get("clientname")
q360_location = dbutils.widgets.get("location")
vision_qsi_location = dbutils.widgets.get("location2")
agein_qsi_location = dbutils.widgets.get("location3")
EMR_qsi_location = dbutils.widgets.get("location4")
FCF_qsi_location = dbutils.widgets.get("location5")
destination_location = dbutils.widgets.get("destination_location")

# COMMAND ----------

# DBTITLE 1,Loading Original Q360 file and adding header columns
#Assign the mounted Q360 Visit file path to a variable
file_path_Q360_visit = f'/mnt/{clientName}/Q360/Q360/{q360_location}'

#Schema created as per Q360 Visit file layout
visit_schema = StructType([
    StructField("MemberID_q360", StringType(),True),
    StructField("DateofService_q360", StringType(), True),
    StructField("AdmissionDate_q360", StringType(), True),
    StructField("DischargeDate_q360", StringType(),True),
    StructField("CPT_q360", StringType(), True),
    StructField("CPT_Modifier1_q360", StringType(), True),
    StructField("CPT_Modifier2_q360", StringType(),True),
    StructField("HCPCS_CDT_q360", StringType(), True),
    StructField("CPT_II_q360", StringType(), True),
    StructField("CPT_II_Modifier_q360", StringType(),True),
    StructField("PrincipalDiag_q360", StringType(), True),
    StructField("Diag2_q360", StringType(), True),
    StructField("Diag3_q360", StringType(), True),
    StructField("Diag4_q360", StringType(), True),
    StructField("Diag5_q360", StringType(), True),
    StructField("Diag6_q360", StringType(), True),
    StructField("Diag7_q360", StringType(), True),
    StructField("Diag8_q360", StringType(), True),
    StructField("Diag9_q360", StringType(), True),
    StructField("Diag10_q360", StringType(), True),
    StructField("Diag11_q360", StringType(), True),
    StructField("Diag12_q360", StringType(), True),
    StructField("Diag13_q360", StringType(), True),
    StructField("Diag14_q360", StringType(), True),
    StructField("Diag15_q360", StringType(), True),
    StructField("Diag16_q360", StringType(), True),
    StructField("Diag17_q360", StringType(), True),
    StructField("Diag18_q360", StringType(), True),
    StructField("Diag19_q360", StringType(), True),
    StructField("Diag20_q360", StringType(), True),
    StructField("PrincipalProc_q360", StringType(), True),
    StructField("Proc2_q360", StringType(), True),
    StructField("Proc3_q360", StringType(), True),
    StructField("Proc4_q360", StringType(), True),
    StructField("Proc5_q360", StringType(), True),
    StructField("Proc6_q360", StringType(), True),
    StructField("ICD_Identifier_q360", StringType(), True),
    StructField("DischargeStatus_q360", StringType(), True),
    StructField("UBRevenue_q360", StringType(), True),
    StructField("UBTypeofBill_q360", StringType(), True),
    StructField("CMSPlaceofService_q360", StringType(), True),
    StructField("ClaimStatus_q360", StringType(), True),
    StructField("ProviderID_q360", StringType(), True),
    StructField("SupplementalDataFlag_q360", StringType(), True),
    StructField("ClaimID_q360", StringType(), True),
    StructField("ClaimlineID_q360", StringType(), True),
    StructField("DataSourceName_q360", StringType(), True),
    StructField("Additionalcoloumn1_q360", StringType(), True),
    StructField("Additionalcoloumn2_q360", StringType(), True),
    StructField("Additionalcoloumn3_q360", StringType(), True),
    StructField("Additionalcoloumn4_q360", StringType(), True),
    StructField("Additionalcoloumn5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])

#Load data to spark dataframe using the visit schema
df_Q360_visit  = spark.read.option("delimiter",'|').schema(visit_schema).csv(file_path_Q360_visit)



# COMMAND ----------

# DBTITLE 1,Load Original Q360 Visit data to Temp View
df_Q360_visit.createOrReplaceTempView("view_OriginalQ360_Visit")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360Visit
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360Visit

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360Visit
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360Visit
# MAGIC (
# MAGIC   MemberID VARCHAR(16),
# MAGIC   DateofService CHAR(8),
# MAGIC   AdmissionDate CHAR(8),
# MAGIC   DischargeDate CHAR(8),
# MAGIC   CPT CHAR(5),
# MAGIC   CPT_Modifier1 CHAR(2),
# MAGIC   CPT_Modifier2 CHAR(2),
# MAGIC   HCPCS_CDT CHAR(5),
# MAGIC   CPT_II VARCHAR(5),
# MAGIC   CPT_II_Modifier VARCHAR(2),
# MAGIC   Principal_ICD_Diagnosis VARCHAR(9),
# MAGIC   ICD_Diagnosis2	VARCHAR(9),
# MAGIC   ICD_Diagnosis3	VARCHAR(9),
# MAGIC   ICD_Diagnosis4	VARCHAR(9),
# MAGIC   ICD_Diagnosis5	VARCHAR(9),
# MAGIC   ICD_Diagnosis6	VARCHAR(9),
# MAGIC   ICD_Diagnosis7	VARCHAR(9),
# MAGIC   ICD_Diagnosis8	VARCHAR(9),
# MAGIC   ICD_Diagnosis9	VARCHAR(9),
# MAGIC   ICD_Diagnosis10	VARCHAR(9),
# MAGIC   ICD_Diagnosis11	VARCHAR(9),
# MAGIC   ICD_Diagnosis12	VARCHAR(9),
# MAGIC   ICD_Diagnosis13	VARCHAR(9),
# MAGIC   ICD_Diagnosis14	VARCHAR(9),
# MAGIC   ICD_Diagnosis15	VARCHAR(9),
# MAGIC   ICD_Diagnosis16	VARCHAR(9),
# MAGIC   ICD_Diagnosis17	VARCHAR(9),
# MAGIC   ICD_Diagnosis18	VARCHAR(9),
# MAGIC   ICD_Diagnosis19	VARCHAR(9),
# MAGIC   ICD_Diagnosis20	VARCHAR(9),
# MAGIC   Principal_ICD_Procedure VARCHAR(8),
# MAGIC   ICD_Procedure2 VARCHAR(8),
# MAGIC   ICD_Procedure3 VARCHAR(8),
# MAGIC   ICD_Procedure4 VARCHAR(8),
# MAGIC   ICD_Procedure5 VARCHAR(8),
# MAGIC   ICD_Procedure6 VARCHAR(8), 
# MAGIC   ICD_Identifier CHAR(1),
# MAGIC   DischargeStatus CHAR(2),
# MAGIC   UBRevenue CHAR(4),
# MAGIC   UBTypeofBill CHAR(4),
# MAGIC   CMSPlaceofService CHAR(2),
# MAGIC   ClaimStatus CHAR(1),
# MAGIC   ProviderID VARCHAR(25),
# MAGIC   SupplementalDataFlag CHAR(1),
# MAGIC   ClaimID VARCHAR(20),
# MAGIC   ClaimlineID VARCHAR(10),
# MAGIC   DataSourceName VARCHAR(20),
# MAGIC   Additionalcoloumn1 VARCHAR(10),
# MAGIC   Additionalcoloumn2 VARCHAR(10),
# MAGIC   Additionalcoloumn3 VARCHAR(10),
# MAGIC   Additionalcoloumn4 VARCHAR(30),
# MAGIC   Additionalcoloumn5 VARCHAR(30),
# MAGIC   Filler VARCHAR(200)
# MAGIC   
# MAGIC )
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Load data from Temp View into OriginalQ360_Visit
# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO OriginalQ360Visit
# MAGIC SELECT DISTINCT
# MAGIC     IFNULL(MemberID_q360, "") AS MemberID,
# MAGIC     IFNULL(DateofService_q360, "") AS DateofService,
# MAGIC     IFNULL(AdmissionDate_q360, "") AS AdmissionDate,
# MAGIC     IFNULL(DischargeDate_q360, "") AS DischargeDate,
# MAGIC     IFNULL(CPT_q360, "") AS CPT,
# MAGIC     IFNULL(CPT_Modifier1_q360, "") AS CPT_Modifier1,
# MAGIC     IFNULL(CPT_Modifier2_q360, "") AS CPT_Modifier2,
# MAGIC     IFNULL(HCPCS_CDT_q360, "") AS HCPCS_CDT,
# MAGIC     IFNULL(CPT_II_q360, "") AS CPT_II,
# MAGIC     IFNULL(CPT_II_Modifier_q360, "") AS CPT_II_Modifier,
# MAGIC     IFNULL(PrincipalDiag_q360, "") AS Principal_ICD_Diagnosis,
# MAGIC     IFNULL(Diag2_q360, "") AS ICD_Diagnosis2,
# MAGIC     IFNULL(Diag3_q360, "") AS ICD_Diagnosis3,
# MAGIC     IFNULL(Diag4_q360, "") AS ICD_Diagnosis4,
# MAGIC     IFNULL(Diag5_q360, "") AS ICD_Diagnosis5,
# MAGIC     IFNULL(Diag6_q360, "") AS ICD_Diagnosis6,
# MAGIC     IFNULL(Diag7_q360, "") AS ICD_Diagnosis7,
# MAGIC     IFNULL(Diag8_q360, "") AS ICD_Diagnosis8,
# MAGIC     IFNULL(Diag9_q360, "") AS ICD_Diagnosis9,
# MAGIC     IFNULL(Diag10_q360, "") AS ICD_Diagnosis10,
# MAGIC     IFNULL(Diag11_q360, "") AS ICD_Diagnosis11,
# MAGIC     IFNULL(Diag12_q360, "") AS ICD_Diagnosis12,
# MAGIC     IFNULL(Diag13_q360, "") AS ICD_Diagnosis13,
# MAGIC     IFNULL(Diag14_q360, "") AS ICD_Diagnosis14,
# MAGIC     IFNULL(Diag15_q360, "") AS ICD_Diagnosis15,
# MAGIC     IFNULL(Diag16_q360, "") AS ICD_Diagnosis16,
# MAGIC     IFNULL(Diag17_q360, "") AS ICD_Diagnosis17,
# MAGIC     IFNULL(Diag18_q360, "") AS ICD_Diagnosis18,
# MAGIC     IFNULL(Diag19_q360, "") AS ICD_Diagnosis19,
# MAGIC     IFNULL(Diag20_q360, "") AS ICD_Diagnosis20,
# MAGIC     IFNULL(PrincipalProc_q360, "") AS Principal_ICD_Procedure,
# MAGIC     IFNULL(Proc2_q360, "") AS ICD_Procedure2,
# MAGIC     IFNULL(Proc3_q360, "") AS ICD_Procedure3,
# MAGIC     IFNULL(Proc4_q360, "") AS ICD_Procedure4,
# MAGIC     IFNULL(Proc5_q360, "") AS ICD_Procedure5,
# MAGIC     IFNULL(Proc6_q360, "") AS ICD_Procedure6, 
# MAGIC     IFNULL(ICD_Identifier_q360, "") AS ICD_Identifier,
# MAGIC     IFNULL(DischargeStatus_q360, "") AS DischargeStatus,
# MAGIC     IFNULL(UBRevenue_q360, "") AS UBRevenue,
# MAGIC     IFNULL(UBTypeofBill_q360, "") AS UBTypeofBill,
# MAGIC     IFNULL(CMSPlaceofService_q360, "") AS CMSPlaceofService,
# MAGIC     IFNULL(ClaimStatus_q360, "") AS ClaimStatus,
# MAGIC     IFNULL(ProviderID_q360, "") AS ProviderID,
# MAGIC     IFNULL(SupplementalDataFlag_q360, "") AS SupplementalDataFlag,
# MAGIC     IFNULL(ClaimID_q360, "") AS ClaimID,
# MAGIC     IFNULL(ClaimlineID_q360, "") AS ClaimlineID,
# MAGIC     IFNULL(DataSourceName_q360, "") AS DataSourceName,
# MAGIC     IFNULL(Additionalcoloumn1_q360, "") AS Additionalcoloumn1,
# MAGIC     IFNULL(Additionalcoloumn2_q360, "") AS Additionalcoloumn2,
# MAGIC     IFNULL(Additionalcoloumn3_q360, "") AS Additionalcoloumn3,
# MAGIC     IFNULL(Additionalcoloumn4_q360, "") AS Additionalcoloumn4,
# MAGIC     IFNULL(Additionalcoloumn5_q360, "") AS Additionalcoloumn5,
# MAGIC     IFNULL(Filler_q360, "") AS Filler
# MAGIC
# MAGIC FROM view_OriginalQ360_Visit

# COMMAND ----------

# DBTITLE 1,Loading the other QSI claims files to union with master dataframe
file_path_vision_QSI = f'/mnt/{clientName}/Q360/QSI/{vision_qsi_location}'
file_path_agein_QSI = f'/mnt/{clientName}/Q360/QSI/{agein_qsi_location}'
file_path_EMR_QSI =  f'/mnt/{clientName}/Q360/QSI/{EMR_qsi_location}'
file_path_FCF_QSI =  f'/mnt/{clientName}/Q360/QSI/{FCF_qsi_location}'

# COMMAND ----------

# DBTITLE 1,Total of four claims makes visit file .Union of four dataframe required for master 
#Assign the mounted QSI Visit file path to a variable
df_vision_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_vision_QSI)
df_agein_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_agein_QSI)
df_EMR_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_EMR_QSI)
df_FCF_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_FCF_QSI)

# This datframe is used to get ICD diagnosis status and ICD procedure status
visit_master_df_principle_icd_filter  = df_vision_qsi.union(df_agein_qsi).union(df_EMR_qsi).union(df_FCF_qsi)

#List of columns required from the QSI file
qsi_visit_col_needed = ['MemberKey',
                        'DOS','DOSThru','CPTPx_00','CPTMod_00','CPTMod_01','HCPCSPx_00','HomeGrownPx_00',
                        'ICDDx_00','ICDDx_02','ICDDx_03','ICDDx_04','ICDDx_05',
                        'ICDDx_06','ICDDx_07','ICDDx_08','ICDDx_09','ICDDx_10',
                        'ICDDx_11','ICDDx_12','ICDDx_13','ICDDx_14','ICDDx_15',
                        'ICDDx_16','ICDDx_17','ICDDx_18','ICDDx_19', 'ICDDx_20',
                        'ICDDx10_00','ICDDx10_02','ICDDx10_03','ICDDx10_04','ICDDx10_05',
                        'ICDDx10_06','ICDDx10_07','ICDDx10_08','ICDDx10_09','ICDDx10_10',
                        'ICDDx10_11','ICDDx10_12','ICDDx10_13','ICDDx10_14','ICDDx10_15',
                        'ICDDx10_16','ICDDx10_17','ICDDx10_18','ICDDx10_19','ICDDx10_20',
                        'ICDPx_00','ICDPx_02','ICDPx_03','ICDPx_04','ICDPx_05','ICDPx_06', 
                        'ICDPx10_00','ICDPx10_02','ICDPx10_03','ICDPx10_04','ICDPx10_05','ICDPx10_06',
                        'DischargeStatus','UBRevenueCode_00','TOB_00','HCFAPos_00',
                        'ClaimStatus','SuppSource','ClaimLineNumber','ClaimNumber']

df_vision_qsi = df_vision_qsi.select(qsi_visit_col_needed)
df_agein_qsi = df_agein_qsi.select(qsi_visit_col_needed)
df_EMR_qsi = df_EMR_qsi.select(qsi_visit_col_needed)
df_FCF_qsi = df_FCF_qsi.select(qsi_visit_col_needed)

## Merging all to claims dataframe to get a master dataframe

visit_master_df = df_vision_qsi.union(df_agein_qsi).union(df_EMR_qsi).union(df_FCF_qsi)



# COMMAND ----------

# DBTITLE 1,Load Mergerd QSI Visit file to dataframe and set ICD_Diagnosis_status

principle_icd_columns = ['MemberKey',
                         'ICDDx_00','ICDDx_02','ICDDx_03','ICDDx_04','ICDDx_05',
                         'ICDDx_06','ICDDx_07','ICDDx_08','ICDDx_09','ICDDx_10',
                         'ICDDx_11','ICDDx_12','ICDDx_13','ICDDx_14','ICDDx_15',
                         'ICDDx_16','ICDDx_17','ICDDx_18','ICDDx_19','ICDDx_20',
                         'ICDPx_00','ICDPx_02','ICDPx_03','ICDPx_04','ICDPx_05','ICDPx_06']

visit_master_df_principle_icd_filter = visit_master_df_principle_icd_filter.select(principle_icd_columns)
visit_master_df_principle_icd_filter = visit_master_df_principle_icd_filter.withColumnRenamed("MemberKey","member_key")

df_visit_principle_icd_filter = visit_master_df_principle_icd_filter.withColumn("ICD_Diagnosis_status",\
                                                when(col('ICDDx_00').isNotNull(),\
                                                when(col('ICDDx_02').isNotNull(),\
                                                when(col('ICDDx_03').isNotNull(),\
                                                when(col('ICDDx_04').isNotNull(),\
                                                when(col('ICDDx_05').isNotNull(),\
                                                when(col('ICDDx_06').isNotNull(),\
                                                when(col('ICDDx_07').isNotNull(),\
                                                when(col('ICDDx_08').isNotNull(),\
                                                when(col('ICDDx_09').isNotNull(),\
                                                when(col('ICDDx_10').isNotNull(),\
                                                when(col('ICDDx_11').isNotNull(),\
                                                when(col('ICDDx_12').isNotNull(),\
                                                when(col('ICDDx_13').isNotNull(),\
                                                when(col('ICDDx_14').isNotNull(),
                                                when(col('ICDDx_15').isNotNull(),\
                                                when(col('ICDDx_16').isNotNull(),\
                                                when(col('ICDDx_17').isNotNull(),\
                                                when(col('ICDDx_18').isNotNull(),\
                                                when(col('ICDDx_19').isNotNull(),\
                                                when(col('ICDDx_20').isNotNull(),'X'))))))))))))))))))))\
                                                  .otherwise(9)) \
                                              .withColumn("ICD_Procedure_status",when(col('ICDPx_00').isNotNull(),\
                                                when(col('ICDPx_02').isNotNull(),\
                                                when(col('ICDPx_03').isNotNull(),\
                                                when(col('ICDPx_04').isNotNull(),\
                                                when(col('ICDPx_05').isNotNull(),\
                                                when(col('ICDPx_06').isNotNull(),'X'))))))\
                                                  .otherwise(9))
                                       

df_visit_principle_icd_filter = df_visit_principle_icd_filter.select("member_key","ICD_Diagnosis_status","ICD_Procedure_status")


                                                                                                          

# COMMAND ----------

# DBTITLE 1,Transforming QSI dataframe to Q360 dataframe

#Join the dataframes df_visit_qsi and df_visit_principle_icd_filter to set the ICD Diagnosis Identifier
df_visit_qsi=visit_master_df.join(df_visit_principle_icd_filter,(visit_master_df.MemberKey == df_visit_principle_icd_filter.member_key),'full')

# Renaming the columns in QSI dataframe to Q360 format
df_visit_qsi = df_visit_qsi.withColumnRenamed('CPTPx_00','CPT')\
                          .withColumnRenamed('CPTMod_00','CPT_Modifier_1')\
                          .withColumnRenamed('CPTMod_01','CPT_Modifier_2')\
                          .withColumnRenamed('HCPCSPx_00','HCPCS_CDT')\
                          .withColumnRenamed('DischargeStatus','Discharge_Status')\
                          .withColumnRenamed('UBRevenueCode_00','UB_Revenue')\
                          .withColumnRenamed('TOB_00','UB_Type_of_Bill')\
                          .withColumnRenamed('HCFAPos_00','CMS_Place_of_Service')\
                          .withColumnRenamed('ClaimNumber','Claim_ID') \
                          .withColumnRenamed('ClaimLineNumber','Claim_line_ID') \
                          .withColumnRenamed('ClaimStatus','ClaimStatus_qsi') 
                # since Q360 and QSI has same column name, column is renamed to drop the QSI column without confusion


# Transforming the columns in QSI dataframe to Q360 format
df_visit_qsi = df_visit_qsi.withColumn("Member_ID",substring(col("MemberKey"),0,16))\
                          .withColumn("Date_of_Service",date_format("DOS",'yyyyMMdd'))\
                          .withColumn("Discharge_Date",date_format("DOSThru",'yyyyMMdd')) \
                          .withColumn("Principal_ICD_Diagnosis",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_00'))\
                              .otherwise(col('ICDDx_00')))\
                          .withColumn("ICD_Diagnosis2",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_02'))\
                              .otherwise(col('ICDDx_02'))) \
                          .withColumn("ICD_Diagnosis3",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_03'))\
                              .otherwise(col('ICDDx_03'))) \
                          .withColumn("ICD_Diagnosis4",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_04'))\
                              .otherwise(col('ICDDx_04'))) \
                          .withColumn("ICD_Diagnosis5",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_05'))\
                              .otherwise(col('ICDDx_05'))) \
                          .withColumn("ICD_Diagnosis6",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_06'))\
                              .otherwise(col('ICDDx_06'))) \
                          .withColumn("ICD_Diagnosis7",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_07'))\
                              .otherwise(col('ICDDx_07'))) \
                          .withColumn("ICD_Diagnosis8",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_08'))\
                              .otherwise(col('ICDDx_08'))) \
                          .withColumn("ICD_Diagnosis9",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_09'))\
                              .otherwise(col('ICDDx_09'))) \
                          .withColumn("ICD_Diagnosis10",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_10'))\
                              .otherwise(col('ICDDx_10'))) \
                          .withColumn("ICD_Diagnosis11",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_11'))\
                              .otherwise(col('ICDDx_11'))) \
                          .withColumn("ICD_Diagnosis12",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_12'))\
                              .otherwise(col('ICDDx_12'))) \
                          .withColumn("ICD_Diagnosis13",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_13'))\
                              .otherwise(col('ICDDx_13'))) \
                          .withColumn("ICD_Diagnosis14",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_14'))\
                              .otherwise(col('ICDDx_14'))) \
                          .withColumn("ICD_Diagnosis15",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_15'))\
                              .otherwise(col('ICDDx_15'))) \
                          .withColumn("ICD_Diagnosis16",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_16'))\
                              .otherwise(col('ICDDx_16'))) \
                          .withColumn("ICD_Diagnosis17",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_17'))\
                              .otherwise(col('ICDDx_17'))) \
                          .withColumn("ICD_Diagnosis18",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_18'))\
                              .otherwise(col('ICDDx_18'))) \
                          .withColumn("ICD_Diagnosis19",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_19'))\
                              .otherwise(col('ICDDx_19'))) \
                          .withColumn("ICD_Diagnosis20",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDDx10_20'))\
                              .otherwise(col('ICDDx_20'))) \
                          .withColumn("Principal_ICD_Procedure",\
                            when(col("ICD_Procedure_status") == 'X',col('ICDPx10_00'))\
                              .otherwise(col('ICDPx_00'))) \
                          .withColumn("ICD_Procedure2",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDPx10_02'))\
                              .otherwise(col('ICDPx_02'))) \
                          .withColumn("ICD_Procedure3",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDPx10_03'))\
                              .otherwise(col('ICDPx_03'))) \
                          .withColumn("ICD_Procedure4",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDPx10_04'))\
                              .otherwise(col('ICDPx_04'))) \
                          .withColumn("ICD_Procedure5",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDPx10_05'))\
                              .otherwise(col('ICDPx_05'))) \
                          .withColumn("ICD_Procedure6",\
                            when(col("ICD_Diagnosis_status") == 'X',col('ICDPx10_06'))\
                              .otherwise(col('ICDPx_06'))) \
                          .withColumn("ClaimStatus",\
                            when(col("ClaimStatus_qsi").isin(['A','I']),1)\
                              .when(col("ClaimStatus_qsi") == 'D',2)\
                              .when(col("ClaimStatus_qsi") == 'P',3)\
                              .when(col("ClaimStatus_qsi") == 'R',4))\
                          .withColumn("SupplementalDataFlag",\
                            when(col("SuppSource").isin(['S','N','E','M']),'Y')\
                              .otherwise('N')) \
                          .drop("member_key","MemberKey",
                                "DOS","DOSThru",
                                "ICDDx10_00","ICDDx10_02","ICDDx10_03","ICDDx10_04","ICDDx10_05",
                                "ICDDx10_06","ICDDx10_07","ICDDx10_08","ICDDx10_09","ICDDx10_10",
                                "ICDDx10_11","ICDDx10_12","ICDDx10_13","ICDDx10_14","ICDDx10_15",
                                "ICDDx10_16","ICDDx10_17","ICDDx10_18","ICDDx10_19","ICDDx10_20",
                                "ICDPx10_00","ICDPx10_02","ICDPx10_03","ICDPx10_04", "ICDPx10_05","ICDPx10_06","ICDDx_00","ICDDx_02","ICDDx_03","ICDDx_04","ICDDx_05",
                                "ICDDx_06","ICDDx_07","ICDDx_08","ICDDx_09","ICDDx_10",
                                "ICDDx_11","ICDDx_12","ICDDx_13","ICDDx_14","ICDDx_15",
                                "ICDDx_16","ICDDx_17","ICDDx_18","ICDDx_19","ICDDx_20",
                                "ICDPx_00","ICDPx_02","ICDPx_03","ICDPx_04","ICDPx_05","ICDPx_06",
                                "ClaimStatus_qsi","SuppSource")

visit_column_order = ['Member_ID',
                      'Date_of_Service','Discharge_Date',
                      'CPT','CPT_Modifier_1','CPT_Modifier_2','HCPCS_CDT',
                      'Principal_ICD_Diagnosis','ICD_Diagnosis2','ICD_Diagnosis3',
                      'ICD_Diagnosis4','ICD_Diagnosis5','ICD_Diagnosis6',
                      'ICD_Diagnosis7','ICD_Diagnosis8','ICD_Diagnosis9',
                      'ICD_Diagnosis10','ICD_Diagnosis11','ICD_Diagnosis12',
                      'ICD_Diagnosis13','ICD_Diagnosis14','ICD_Diagnosis15',
                      'ICD_Diagnosis16','ICD_Diagnosis17','ICD_Diagnosis18',
                      'ICD_Diagnosis19','ICD_Diagnosis20',
                      'Principal_ICD_Procedure','ICD_Procedure2','ICD_Procedure3',
                      'ICD_Procedure4','ICD_Procedure5','ICD_Procedure6',
                      'ICD_Diagnosis_status','Discharge_Status',
                      'UB_Revenue','UB_Type_of_Bill',
                      'CMS_Place_of_Service','ClaimStatus',
                      'SupplementalDataFlag','Claim_ID','Claim_line_ID']

df_visit_qsi = df_visit_qsi.select(visit_column_order) 


# COMMAND ----------

# DBTITLE 1,Saving the converted QSI to containers
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#Assign the destination path for the Converted QSI file to a variable
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'
#Convert spark dataframe to pandas dataframe
pandas_qsi_visit_df = df_visit_qsi.toPandas()
#Copy data from pandas dataframe to csv file
pandas_qsi_visit_df.to_csv(f'{file_destination}QSI_to_Q360_visit_converted_{date}.txt',
                     index = False,sep = '|') 

# COMMAND ----------

# DBTITLE 1,Joining source Q360 and transformed QSI
df_vist_join = df_Q360_visit.join(df_visit_qsi,(df_Q360_visit.MemberID_q360 == df_visit_qsi.Member_ID),'full')

# COMMAND ----------

# DBTITLE 1,Comparing Q360 and converted QSI dataframe 
#Compare the Q360 and Converted QSI Dataframes based on the Member_ID
df_vist_join = df_vist_join.withColumn('Member_ID_status',\
                              when(col('Member_ID') == col('MemberID_q360'),'Y')\
                                .otherwise('N')) \
                            .withColumn('Date_of_Service_status',\
                              when(col('Member_ID')== col('MemberID_q360'), \
                                  when(col('Date_of_Service')== col('DateofService_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('DischargeDate_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Discharge_Date') == col('DischargeDate_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('CPT_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('CPT') == col('CPT_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('CPT_Modifier_1_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('CPT_Modifier_1') == col('CPT_Modifier1_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('CPT_Modifier_2_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('CPT_Modifier_2') == col('CPT_Modifier2_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn("HCPCS_CDT_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('HCPCS_CDT') == col('HCPCS_CDT_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PrincipalDiag_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Principal_ICD_Diagnosis') == col('PrincipalDiag_q360'),'Y')\
                                    .otherwise('N') )\
                              .otherwise('N')) \
                            .withColumn('Diag2_status',when(col('Member_ID')== col('MemberID_q360'),\
                              when(col('ICD_Diagnosis2') == col('Diag2_q360'),'Y')\
                              .otherwise('N')).otherwise('N')) \
                            .withColumn('Diag3_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis3') == col('Diag3_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag4_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis4') == col('Diag4_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag5_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis5') == col('Diag5_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag6_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                when(col('ICD_Diagnosis6') == col('Diag6_q360'),'Y')\
                                .otherwise('N'))\
                            .otherwise('N')) \
                            .withColumn('Diag7_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis7') == col('Diag7_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag8_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis8') == col('Diag8_q360'),'Y')\
                                      .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag9_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis9') == col('Diag9_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag10_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis10') == col('Diag10_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag11_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis11') == col('Diag11_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag12_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis12') == col('Diag12_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag13_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis13') == col('Diag13_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag14_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis14') == col('Diag14_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag15_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis15') == col('Diag15_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag16_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis16') == col('Diag16_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag17_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis17') == col('Diag17_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag18_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis18') == col('Diag18_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag19_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis19') == col('Diag19_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Diag20_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Diagnosis20') == col('Diag20_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PrincipalProc_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Principal_ICD_Procedure') == col('PrincipalProc_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Proc2_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Procedure2') == col('Proc2_q360'),'Y')\
                                  .otherwise('N') )\
                              .otherwise('N')) \
                            .withColumn('Proc3_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Procedure3') == col('Proc3_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Proc4_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Procedure4') == col('Proc4_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Proc5_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Procedure5') == col('Proc5_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Proc6_status',\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ICD_Procedure6') == col('Proc6_q360'),'Y')\
                                  .otherwise('N') )\
                              .otherwise('N'))  \
                            .withColumn("Discharge_Status_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Discharge_Status') == col('DischargeStatus_q360'),'Y')\
                                    .otherwise('N') )\
                              .otherwise('N'))  \
                            .withColumn("UBRevenue_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('UB_Revenue') == col('UBRevenue_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("UB_Type_of_Bill_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('UB_Type_of_Bill') == col('UBTypeofBill_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("CMSPlaceofService_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('CMS_Place_of_Service') == col('CMSPlaceofService_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("ClaimStatus_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('ClaimStatus') == col('ClaimStatus_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("SupplementalDataFlag_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('SupplementalDataFlag') == col('SupplementalDataFlag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("ClaimID_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Claim_ID') == col('ClaimID_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  \
                            .withColumn("Claim_line_ID_status",\
                              when(col('Member_ID')== col('MemberID_q360'),\
                                  when(col('Claim_line_ID') == col('ClaimlineID_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N'))  
   

status_columns = ['Member_ID',
                  'Member_ID_status','Date_of_Service_status','DischargeDate_status',
                  'CPT_status','CPT_Modifier_1_status','CPT_Modifier_2_status','HCPCS_CDT_status',
                  'PrincipalDiag_status','Diag2_status','Diag3_status','Diag4_status',
                  'Diag5_status','Diag6_status','Diag7_status','Diag8_status',
                  'Diag9_status','Diag10_status','Diag11_status','Diag12_status',
                  'Diag13_status','Diag14_status','Diag15_status','Diag16_status',
                  'Diag17_status','Diag18_status','Diag19_status','Diag20_status',
                  'PrincipalProc_status','Proc2_status','Proc3_status',
                  'Proc4_status','Proc5_status','Proc6_status',
                  'Discharge_Status_status','UBRevenue_status',
                  'UB_Type_of_Bill_status','CMSPlaceofService_status',
                  'ClaimStatus_status','SupplementalDataFlag_status',
                  'ClaimID_status','Claim_line_ID_status']

df_vist_join = df_vist_join.select(status_columns)



# COMMAND ----------

# DBTITLE 1,Load Comparison results from spark dataframe to Temp view
df_vist_join.createOrReplaceTempView("view_VisitComparison_Results")

# COMMAND ----------

# DBTITLE 1,Drop table tblM_VisitComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_VisitComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_VisitComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE tblM_VisitComparison_Results
# MAGIC (
# MAGIC   Member_ID VARCHAR(16),
# MAGIC   IsRecordMatching CHAR(1),
# MAGIC   Member_ID_status CHAR(1),
# MAGIC   Date_of_Service_status CHAR(1),
# MAGIC   DischargeDate_status CHAR(1),
# MAGIC   CPT_status CHAR(1),
# MAGIC   CPT_Modifier_1_status CHAR(1),
# MAGIC   CPT_Modifier_2_status CHAR(1),
# MAGIC   HCPCS_CDT_status CHAR(1),
# MAGIC   Principal_ICD_Diagnosis_status CHAR(1),
# MAGIC   ICD_Diagnosis2_status CHAR(1),
# MAGIC   ICD_Diagnosis3_status CHAR(1),
# MAGIC   ICD_Diagnosis4_status CHAR(1),
# MAGIC   ICD_Diagnosis5_status CHAR(1),
# MAGIC   ICD_Diagnosis6_status CHAR(1),
# MAGIC   ICD_Diagnosis7_status CHAR(1),
# MAGIC   ICD_Diagnosis8_status CHAR(1),
# MAGIC   ICD_Diagnosis9_status CHAR(1),
# MAGIC   ICD_Diagnosis10_status CHAR(1),
# MAGIC   ICD_Diagnosis11_status CHAR(1),
# MAGIC   ICD_Diagnosis12_status CHAR(1),
# MAGIC   ICD_Diagnosis13_status CHAR(1),
# MAGIC   ICD_Diagnosis14_status CHAR(1),
# MAGIC   ICD_Diagnosis15_status CHAR(1),
# MAGIC   ICD_Diagnosis16_status CHAR(1),
# MAGIC   ICD_Diagnosis17_status CHAR(1),
# MAGIC   ICD_Diagnosis18_status CHAR(1),
# MAGIC   ICD_Diagnosis19_status CHAR(1),
# MAGIC   ICD_Diagnosis20_status CHAR(1),
# MAGIC   Principal_ICD_Procedure_status CHAR(1),
# MAGIC   ICD_Procedure2_status CHAR(1),
# MAGIC   ICD_Procedure3_status CHAR(1),
# MAGIC   ICD_Procedure4_status CHAR(1),
# MAGIC   ICD_Procedure5_status CHAR(1),
# MAGIC   ICD_Procedure6_status CHAR(1),
# MAGIC   Discharge_Status_status CHAR(1),
# MAGIC   UBRevenue_status CHAR(1),
# MAGIC   UB_Type_of_Bill_status CHAR(1),
# MAGIC   CMSPlaceofService_status CHAR(1),
# MAGIC   ClaimStatus_status CHAR(1),
# MAGIC   SupplementalDataFlag_status CHAR(1),
# MAGIC   ClaimID_status CHAR(1),
# MAGIC   Claim_line_ID_status CHAR(1)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp view into table tblM_VisitComparison_Results
# MAGIC %sql
# MAGIC INSERT INTO tblM_VisitComparison_Results
# MAGIC SELECT DISTINCT
# MAGIC   Member_ID,
# MAGIC   'Y' AS IsRecordMatching,
# MAGIC   Member_ID_status,
# MAGIC   Date_of_Service_status,
# MAGIC   DischargeDate_status,
# MAGIC   CPT_status,
# MAGIC   CPT_Modifier_1_status,
# MAGIC   CPT_Modifier_2_status,
# MAGIC   HCPCS_CDT_status,
# MAGIC   PrincipalDiag_status AS Principal_ICD_Diagnosis_status,
# MAGIC   Diag2_status AS ICD_Diagnosis2_status,
# MAGIC   Diag3_status AS ICD_Diagnosis3_status,
# MAGIC   Diag4_status AS ICD_Diagnosis4_status,
# MAGIC   Diag5_status AS ICD_Diagnosis5_status,
# MAGIC   Diag6_status AS ICD_Diagnosis6_status,
# MAGIC   Diag7_status AS ICD_Diagnosis7_status,
# MAGIC   Diag8_status AS ICD_Diagnosis8_status,
# MAGIC   Diag9_status AS ICD_Diagnosis9_status,
# MAGIC   Diag10_status AS ICD_Diagnosis10_status,
# MAGIC   Diag11_status AS ICD_Diagnosis11_status,
# MAGIC   Diag12_status AS ICD_Diagnosis12_status,
# MAGIC   Diag13_status AS ICD_Diagnosis13_status,
# MAGIC   Diag14_status AS ICD_Diagnosis14_status,
# MAGIC   Diag15_status AS ICD_Diagnosis15_status,
# MAGIC   Diag16_status AS ICD_Diagnosis16_status,
# MAGIC   Diag17_status AS ICD_Diagnosis17_status,
# MAGIC   Diag18_status AS ICD_Diagnosis18_status,
# MAGIC   Diag19_status AS ICD_Diagnosis19_status,
# MAGIC   Diag20_status AS ICD_Diagnosis20_status,
# MAGIC   PrincipalProc_status AS Principal_ICD_Procedure_status,
# MAGIC   Proc2_status AS ICD_Procedure2_status,
# MAGIC   Proc3_status AS ICD_Procedure3_status,
# MAGIC   Proc4_status AS ICD_Procedure4_status,
# MAGIC   Proc5_status AS ICD_Procedure5_status,
# MAGIC   Proc6_status AS ICD_Procedure6_status,
# MAGIC   Discharge_Status_status,
# MAGIC   UBRevenue_status,
# MAGIC   UB_Type_of_Bill_status,
# MAGIC   CMSPlaceofService_status,
# MAGIC   ClaimStatus_status,
# MAGIC   SupplementalDataFlag_status,
# MAGIC   ClaimID_status,
# MAGIC   Claim_line_ID_status
# MAGIC
# MAGIC   FROM view_VisitComparison_Results

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the flags of the individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_VisitComparison_Results
# MAGIC   SET IsRecordMatching = CASE 
# MAGIC                                 WHEN Member_ID_status = 'N' OR
# MAGIC                                 Date_of_Service_status = 'N' OR
# MAGIC                                 DischargeDate_status = 'N' OR
# MAGIC                                 CPT_status = 'N' OR
# MAGIC                                 CPT_Modifier_1_status = 'N' OR
# MAGIC                                 CPT_Modifier_2_status = 'N' OR
# MAGIC                                 HCPCS_CDT_status = 'N' OR
# MAGIC                                 Principal_ICD_Diagnosis_status = 'N' OR
# MAGIC                                 ICD_Diagnosis2_status = 'N' OR
# MAGIC                                 ICD_Diagnosis3_status = 'N' OR
# MAGIC                                 ICD_Diagnosis4_status = 'N' OR
# MAGIC                                 ICD_Diagnosis5_status = 'N' OR
# MAGIC                                 ICD_Diagnosis6_status = 'N' OR
# MAGIC                                 ICD_Diagnosis7_status = 'N' OR
# MAGIC                                 ICD_Diagnosis8_status = 'N' OR
# MAGIC                                 ICD_Diagnosis9_status = 'N' OR
# MAGIC                                 ICD_Diagnosis10_status = 'N' OR
# MAGIC                                 ICD_Diagnosis11_status = 'N' OR
# MAGIC                                 ICD_Diagnosis12_status = 'N' OR
# MAGIC                                 ICD_Diagnosis13_status = 'N' OR
# MAGIC                                 ICD_Diagnosis14_status = 'N' OR
# MAGIC                                 ICD_Diagnosis15_status = 'N' OR
# MAGIC                                 ICD_Diagnosis16_status = 'N' OR
# MAGIC                                 ICD_Diagnosis17_status = 'N' OR
# MAGIC                                 ICD_Diagnosis18_status = 'N' OR
# MAGIC                                 ICD_Diagnosis19_status = 'N' OR
# MAGIC                                 ICD_Diagnosis20_status = 'N' OR
# MAGIC                                 Principal_ICD_Procedure_status = 'N' OR
# MAGIC                                 ICD_Procedure2_status = 'N' OR
# MAGIC                                 ICD_Procedure3_status = 'N' OR
# MAGIC                                 ICD_Procedure4_status = 'N' OR
# MAGIC                                 ICD_Procedure5_status = 'N' OR
# MAGIC                                 ICD_Procedure6_status = 'N' OR
# MAGIC                                 Discharge_Status_status = 'N' OR
# MAGIC                                 UBRevenue_status = 'N' OR
# MAGIC                                 UB_Type_of_Bill_status = 'N' OR
# MAGIC                                 CMSPlaceofService_status = 'N' OR
# MAGIC                                 ClaimStatus_status = 'N' OR
# MAGIC                                 SupplementalDataFlag_status = 'N' OR
# MAGIC                                 ClaimID_status = 'N' OR
# MAGIC                                 Claim_line_ID_status = 'N'
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

# DBTITLE 1,To get the count of matched and mismatched records
# MAGIC %sql
# MAGIC INSERT INTO tblM_Q360_Comparison_Results
# MAGIC SELECT  
# MAGIC       'ABC' AS Client,
# MAGIC       getdate() AS RunDateTime,
# MAGIC       'VISIT_CLAIM' AS FileType,
# MAGIC       (SELECT count(MemberID) FROM OriginalQ360Visit) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_VisitComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360Visit
# MAGIC       INNER JOIN tblM_VisitComparison_Results
# MAGIC       on OriginalQ360Visit.MemberID = tblM_VisitComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_VisitComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360Visit
# MAGIC       FULL OUTER JOIN tblM_VisitComparison_Results
# MAGIC       on OriginalQ360Visit.MemberID = tblM_VisitComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords
# MAGIC       

# COMMAND ----------

# DBTITLE 1,Load the File level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')

#Convert spark dataframe into pandas dataframe
df_final_status = df_final.toPandas()

#Copy data from pandas dataframe to csv file
df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Visit_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Load the Record level Comparison results to storage container
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Visit = spark.sql('SELECT * FROM tblM_VisitComparison_Results ORDER BY Member_ID')

#Convert spark dataframe into pandas dataframe
df_Visit_Pandas = df_Visit.toPandas()

#Copy data from pandas dataframe to csv file
df_Visit_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Visit_Comparison_{date}.csv') 

# COMMAND ----------

# DBTITLE 1,Notebook exit comment to show the status of the run
dbutils.notebook.exit("Success")
