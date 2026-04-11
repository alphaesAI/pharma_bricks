# Databricks notebook source
# MAGIC %md
# MAGIC ## 6_Basic_Transform_Provider

# COMMAND ----------

# DBTITLE 1,Python Libraries
import numpy as np
import pandas as pd
from datetime import datetime
from pyspark.sql.functions import col,substring,expr,date_format,when,expr,isnull
from pyspark.sql.types import StringType,StructType,StructField


# COMMAND ----------

# DBTITLE 1,Cell to receive location parameters from ADF pipeline through master notebook
clientName = dbutils.widgets.get("clientname")
q360_location = dbutils.widgets.get("location")
pharmacy_qsi_location = dbutils.widgets.get("location2")
vision_qsi_location = dbutils.widgets.get("location3")
agein_qsi_location = dbutils.widgets.get("location4")
EMR_qsi_location = dbutils.widgets.get("location5")
FCF_qsi_location = dbutils.widgets.get("location6")
destination_location = dbutils.widgets.get("destination_location")

# COMMAND ----------

# DBTITLE 1,Loading and naming Q360 Provider files
file_path_Q360_provider = f'/mnt/{clientName}/Q360/Q360/{q360_location}'

provider_schema = StructType([
    StructField("Provider_ID_q360", StringType(),True),
    StructField("PCP_Flag_q360", StringType(), True),
    StructField("OBGYN_Flag_q360", StringType(), True),
    StructField("MH_Provider_Flag_q360", StringType(),True),
    StructField("Eye_Care_Provider_Flag_q360", StringType(), True),
    StructField("Dentist_Flag_q360", StringType(), True),
    StructField("Nephrologist_Flag_q360", StringType(),True),
    StructField("Anesthesiologist_Flag_q360", StringType(), True),
    StructField("NPR_Provider_Flag_q360", StringType(), True),
    StructField("PAS_Provider_Flag_q360", StringType(),True),
    StructField("Provider_Prescribing_Privileges_Flag_q360", StringType(), True),
    StructField("Clinical_Pharmacist_Flag_q360", StringType(), True),
    StructField("Hospital_Flag_q360", StringType(),True),
    StructField("SNF_Flag_q360", StringType(), True),
    StructField("Surgeon_Flag_q360", StringType(), True),
    StructField("Registered_Nurse_Flag_q360", StringType(),True),
    StructField("Pediatrician_Flag_q360", StringType(), True),
    StructField("Diabetologist_Flag_q360", StringType(), True),
    StructField("Dietician_Flag_q360", StringType(),True),
    StructField("Physiotherapist_Flag_q360", StringType(), True),
    StructField("Nutritionist_Flag_q360", StringType(), True),
    StructField("Endocrinologist_q360", StringType(), True),
    StructField("Urologist_q360", StringType(), True),
    StructField("Cardiologist_q360", StringType(), True),
    StructField("Radiologist_q360", StringType(), True),
    StructField("Oncologist_q360", StringType(), True),
    StructField("Pain_Specialist_q360", StringType(), True),
    StructField("Medical_Lab_Technician_q360", StringType(), True),
    StructField("Clinical_Lab_Technician_q360", StringType(), True),
    StructField("Provider_NPI_q360", StringType(), True),
    StructField("Additional_coloumn_1_q360", StringType(),True),
    StructField("Additional_coloumn_2_q360", StringType(), True),
    StructField("Additional_coloumn_3_q360", StringType(), True),
    StructField("Additional_coloumn_4_q360", StringType(),True),
    StructField("Additional_coloumn_5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])

df_Q360_provider = spark.read.option("delimiter",'|').schema(provider_schema).csv(file_path_Q360_provider)


# COMMAND ----------

# DBTITLE 1,Load Q360 Provider dataframe into Temp view
df_Q360_provider.createOrReplaceTempView("view_OriginalQ360_Provider")

# COMMAND ----------

# DBTITLE 1,Drop table OriginalQ360_Provider
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_Provider

# COMMAND ----------

# DBTITLE 1,Create table OriginalQ360_Provider
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_Provider
# MAGIC (
# MAGIC   ProviderID VARCHAR(25),
# MAGIC   PCPFlag CHAR(1),
# MAGIC   OBGYNFlag CHAR(1),
# MAGIC   MHProviderFlag CHAR(1),
# MAGIC   EyeCareProviderFlag CHAR(1),
# MAGIC   DentistFlag CHAR(1),
# MAGIC   NephrologistFlag CHAR(1),
# MAGIC   AnesthesiologistFlag CHAR(1),
# MAGIC   NPRProviderFlag CHAR(1),
# MAGIC   PASProviderFlag CHAR(1),
# MAGIC   ProviderPrescribingPrivilegesFlag CHAR(1),
# MAGIC   ClinicalPharmacistFlag CHAR(1),
# MAGIC   HospitalFlag CHAR(1),
# MAGIC   SNFFlag CHAR(1),
# MAGIC   SurgeonFlag CHAR(1),
# MAGIC   RegisteredNurseFlag CHAR(1),
# MAGIC   PediatricianFlag CHAR(1),
# MAGIC   DiabetologistFlag CHAR(1),
# MAGIC   DieticianFlag CHAR(1),
# MAGIC   PhysiotherapistFlag CHAR(1),
# MAGIC   NutritionistFlag CHAR(1),
# MAGIC   Endocrinologist CHAR(1),
# MAGIC   Urologist CHAR(1),
# MAGIC   Cardiologist CHAR(1),
# MAGIC   Radiologist CHAR(1),
# MAGIC   Oncologist CHAR(1),
# MAGIC   PainSpecialist CHAR(1),
# MAGIC   MedicalLabTechnician CHAR(1),
# MAGIC   ClinicalLabTechnician CHAR(1),
# MAGIC   ProviderNPI VARCHAR(10),
# MAGIC   Additionalcoloumn1 VARCHAR(10),
# MAGIC   Additionalcoloumn2 VARCHAR(10),
# MAGIC   Additionalcoloumn3 VARCHAR(10),
# MAGIC   Additionalcoloumn4 VARCHAR(30),
# MAGIC   Additionalcoloumn5 VARCHAR(30),
# MAGIC   Filler VARCHAR(200)
# MAGIC   
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from temp view to table OriginalQ360_Provider
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_Provider
# MAGIC SELECT DISTINCT 
# MAGIC   IFNULL(Provider_ID_q360, "") AS ProviderID,
# MAGIC   IFNULL(PCP_Flag_q360, "") AS PCPFlag,
# MAGIC   IFNULL(OBGYN_Flag_q360, "") AS OBGYNFlag,
# MAGIC   IFNULL(MH_Provider_Flag_q360, "") AS MHProviderFlag,
# MAGIC   IFNULL(Eye_Care_Provider_Flag_q360, "") AS EyeCareProviderFlag,
# MAGIC   IFNULL(Dentist_Flag_q360, "") AS DentistFlag,
# MAGIC   IFNULL(Nephrologist_Flag_q360, "") AS NephrologistFlag,
# MAGIC   IFNULL(Anesthesiologist_Flag_q360, "") AS AnesthesiologistFlag,
# MAGIC   IFNULL(NPR_Provider_Flag_q360, "") AS NPRProviderFlag,
# MAGIC   IFNULL(PAS_Provider_Flag_q360, "") AS PASProviderFlag,
# MAGIC   IFNULL(Provider_Prescribing_Privileges_Flag_q360, "") AS ProviderPrescribingPrivilegesFlag,
# MAGIC   IFNULL(Clinical_Pharmacist_Flag_q360, "") AS ClinicalPharmacistFlag,
# MAGIC   IFNULL(Hospital_Flag_q360, "") AS HospitalFlag,
# MAGIC   IFNULL(SNF_Flag_q360, "") AS SNFFlag,
# MAGIC   IFNULL(Surgeon_Flag_q360, "") AS SurgeonFlag,
# MAGIC   IFNULL(Registered_Nurse_Flag_q360, "") AS RegisteredNurseFlag,
# MAGIC   IFNULL(Pediatrician_Flag_q360, "") AS PediatricianFlag,
# MAGIC   IFNULL(Diabetologist_Flag_q360, "") AS DiabetologistFlag,
# MAGIC   IFNULL(Dietician_Flag_q360, "") AS DieticianFlag,
# MAGIC   IFNULL(Physiotherapist_Flag_q360, "") AS PhysiotherapistFlag,
# MAGIC   IFNULL(Nutritionist_Flag_q360, "") AS NutritionistFlag,
# MAGIC   IFNULL(Endocrinologist_q360, "") AS Endocrinologist,
# MAGIC   IFNULL(Urologist_q360, "") AS Urologist,
# MAGIC   IFNULL(Cardiologist_q360, "") AS Cardiologist,
# MAGIC   IFNULL(Radiologist_q360, "") AS Radiologist,
# MAGIC   IFNULL(Oncologist_q360, "") AS Oncologist,
# MAGIC   IFNULL(Pain_Specialist_q360, "") AS PainSpecialist,
# MAGIC   IFNULL(Medical_Lab_Technician_q360, "") AS MedicalLabTechnician,
# MAGIC   IFNULL(Clinical_Lab_Technician_q360, "") AS ClinicalLabTechnician,
# MAGIC   IFNULL(Provider_NPI_q360, "") AS ProviderNPI,
# MAGIC   IFNULL(Additional_coloumn_1_q360, "") AS Additionalcoloumn1,
# MAGIC   IFNULL(Additional_coloumn_2_q360, "") AS Additionalcoloumn2,
# MAGIC   IFNULL(Additional_coloumn_3_q360, "") AS Additionalcoloumn3,
# MAGIC   IFNULL(Additional_coloumn_4_q360, "") AS Additionalcoloumn4,
# MAGIC   IFNULL(Additional_coloumn_5_q360, "") AS Additionalcoloumn5,
# MAGIC   IFNULL(Filler_q360, "") AS Filler
# MAGIC
# MAGIC FROM view_OriginalQ360_Provider  

# COMMAND ----------

# DBTITLE 1,Load QSI Vision file to dataframe
#Assign the mounted QSI Visit file path to a variable

file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{vision_qsi_location}'

#Load QSI Vist file to spark dataframe
df_vision_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#List of columns required from the QSI file
qsi_vision_col_needed = ['ProviderKey','PCPFlag',
                        'ProviderSpecialty_00','RxProviderFlag',
                        'ProviderType_00','ProviderTaxonomy',
                        'Rendering_Provider_NPI']

df_vision_qsi = df_vision_qsi.select(qsi_vision_col_needed)



# COMMAND ----------

# DBTITLE 1,Load QSI AgeIn file to dataframe
#Assign the mounted QSI AgeIn file path to a variable
file_path_QSI = f'/mnt/{clientName}//Q360/QSI/{agein_qsi_location}'

#Load QSI Vist file to spark dataframe
df_agein_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#List of columns required from the QSI file
qsi_agein_col_needed = ['ProviderKey','PCPFlag',
                        'ProviderSpecialty_00','RxProviderFlag',
                        'ProviderType_00','ProviderTaxonomy',
                        'Rendering_Provider_NPI']

df_agein_qsi = df_agein_qsi.select(qsi_agein_col_needed)



# COMMAND ----------

# DBTITLE 1,Load QSI EMR file to dataframe
#Assign the mounted QSI EMR file path to a variable
file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{EMR_qsi_location}'

#Load QSI Vist file to spark dataframe
df_emr_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#List of columns required from the QSI file
qsi_emr_col_needed = ['ProviderKey','PCPFlag',
                        'ProviderSpecialty_00','RxProviderFlag',
                        'ProviderType_00','ProviderTaxonomy',
                        'Rendering_Provider_NPI']

df_emr_qsi = df_emr_qsi.select(qsi_emr_col_needed)



# COMMAND ----------

# DBTITLE 1,Load QSI FCF file to dataframe
#Assign the mounted QSI FCF file path to a variable

file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{FCF_qsi_location}'

#Load QSI Vist file to spark dataframe
df_fcf_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#List of columns required from the QSI file
qsi_fcf_col_needed = ['ProviderKey','PCPFlag',
                        'ProviderSpecialty_00','RxProviderFlag',
                        'ProviderType_00','ProviderTaxonomy',
                        'Rendering_Provider_NPI']

df_fcf_qsi = df_fcf_qsi.select(qsi_fcf_col_needed)

display (df_fcf_qsi)

# COMMAND ----------

# DBTITLE 1,Union all provider ids into one dataframe
import pyspark
from functools import reduce

list_of_claimsdf = [df_vision_qsi, df_agein_qsi, df_emr_qsi,df_fcf_qsi]
union_qsi_df = reduce(pyspark.sql.dataframe.DataFrame.unionByName, list_of_claimsdf)

display(union_qsi_df)

# COMMAND ----------

# DBTITLE 1,Load QSI Pharmacy file to dataframe
#Assign the mounted QSI Pharmacy file path to a variable

file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{pharmacy_qsi_location}'

#Load QSI Vist file to spark dataframe
df_pharm_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

#List of columns required from the QSI file
qsi_pharm_col_needed = ['ProviderKey']

df_pharm_qsi = df_pharm_qsi.select(qsi_pharm_col_needed)

df_pharm_qsi = df_pharm_qsi.withColumnRenamed("ProviderKey","Pharm_ProviderKey")



# COMMAND ----------

final_qsi_df = union_qsi_df.join(df_pharm_qsi,
                                        (union_qsi_df.ProviderKey == df_pharm_qsi.Pharm_ProviderKey),
                                        'left')

final_qsi_df = final_qsi_df.withColumn("PPPflag",\
                                        when (col("Pharm_ProviderKey").isNotNull(),'Y')\
                                        .otherwise('N')
                                      )

display(final_qsi_df)

# COMMAND ----------

# DBTITLE 1,Transforming QSI dataframe to Q360 dataframe 
# Renaming the columns in QSI dataframe to Q360 format
final_qsi_df = final_qsi_df.withColumnRenamed('ProviderKey','ProviderID')\
                            .withColumnRenamed('Rendering_Provider_NPI','ProviderNPI')\
                            .withColumnRenamed('ProviderTaxonomy','Additionalcoloumn1')\
                            .withColumnRenamed('ProviderSpecialty_00','Additionalcoloumn2')
#final_qsi_df = final_qsi_df.distinct()
display(final_qsi_df)


# COMMAND ----------

# DBTITLE 1,QSI to Q360 transformation
# Transforming the columns in QSI dataframe to Q360 format
final_qsi_df = final_qsi_df.withColumn("PCPflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('08','11','27','37','38','50','99','D8') THEN 'Y' \
                                                  ELSE 'N'  END AS PCPflag")\
                                      )\
                            .withColumn("OBGYNflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('16','98') THEN 'Y' \
                                                  ELSE 'N' END AS OBGYNflag")\
                                      )\
                            .withColumn("MHProviderflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('26','62','68','80','86') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('101Y00000X','101YA0400X',\
                                                                                '101YM0800X','101YP2500X',\
                                                                                '101YS0200X','102L00000X',\
                                                                                '103G00000X','103K00000X',\
                                                                                '104100000X','1041S0200X',\
                                                                                '106H00000X')  THEN 'Y' \
                                                  ELSE 'N' END AS MHProviderflag")\
                                      )\
                            .withColumn("EyeCareProviderflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('18','41') THEN 'Y' \
                                                  ELSE 'N' END AS EyeCareProviderflag")\
                                      )\
                            .withColumn("Dentistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('19','C5') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('1223E0200X','1223P0106X',\
                                                                                '1223P0300X','1223P0700X',\
                                                                                '1223X0400X','1223D0001X',\
                                                                                '1223X0008X','1223X2210X',\
                                                                                '125K00000X','126800000X')\
                                                                                   THEN 'Y' \
                                                  ELSE 'N' END AS Dentistflag")\
                                      )\
                            .withColumn("Nephrologistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('39') THEN 'Y' \
                                                  ELSE 'N' END AS Nephrologistflag")\
                                      )\
                            .withColumn("Anesthesiologistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('05','32') THEN 'Y' \
                                                  ELSE 'N' END AS Anesthesiologistflag")\
                                      )\
                            .withColumn("NPRProviderflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('50') THEN 'Y' \
                                                  ELSE 'N' END AS NPRProviderflag")\
                                      )\
                            .withColumn("PASProviderflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('97') THEN 'Y' \
                                                  ELSE 'N' END AS PASProviderflag")\
                                      )\
                            .withColumn("ProviderPrescribingPrivilegesflag",\
                                        expr("CASE WHEN PPPFlag = 'Y' THEN 'Y' \
                                                   WHEN Additionalcoloumn2 in ('08','11','27','37','38','50',\
                                                                          '99','D8','26','86','A0') THEN 'Y' \
                                          ELSE 'N' END AS ProviderPrescribingPrivilegesflag")\
                                      )\
                            .withColumn("ClinicalPharmacistflag",\
                                        expr("CASE WHEN Additionalcoloumn1 in ('183500000X','1835P0018X',\
                                                                                '1835P1200X','1835P1300X',\
                                                                                '1835P2201X','1835X0200X')\
                                                                                  THEN 'Y' \
                                                  ELSE 'N' END AS ClinicalPharmacistflag")\
                                      )\
                            .withColumn("Hospitalflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('A0') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('273100000X','276400000X',\
                                                                                '282NR1301X','282NW0100X',\
                                                                                '286500000X') THEN 'Y' \
                                                  ELSE 'N' END AS Hospitalflag")\
                                      )\
                            .withColumn("SNFflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('A1') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('315P00000X') THEN 'Y' \
                                                  ELSE 'N' END AS SNFflag")\
                                      )\
                            .withColumn("Surgeonflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('02','14','19','20','24','28','33','40','76','77','78','85','91','D7') THEN 'Y' \
                                                    ELSE 'N' END AS Surgeonflag")\
                                      )\
                            .withColumn("RegisteredNurseflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('31','43') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('163W00000X','163WC0200X',\
                                                                                '163WC0400X','163WC1500X',\
                                                                                '163WD0400X','163WG0000X',\
                                                                                '163WL0100X','163WM0705X',\
                                                                                '163WP0200X','163WP0808X',\
                                                                                '163WP0809X','163WS0200X',\
                                                                                '163WW0101X') THEN 'Y' \
                                                  ELSE 'N' END AS RegisteredNurseflag")\
                                      )\
                            .withColumn("Pediatricianflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('37') THEN 'Y' \
                                                  ELSE 'N' END AS Pediatricianflag")\
                                      )\
                            .withColumn("Diabetologistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('46') THEN 'Y' \
                                                  ELSE 'N' END AS Diabetologistflag")\
                                      )\
                            .withColumn("Dieticianflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('71') THEN 'Y' \
                                                  ELSE 'N' END AS Dieticianflag")\
                                      )\
                            .withColumn("Physiotherapistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('25','65') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('224Z00000X','225200000X',\
                                                                                '225400000X','225500000X',\
                                                                                '2255A2300X') THEN 'Y' \
                                                  ELSE 'N' END AS Physiotherapistflag")\
                                      )\
                            .withColumn("Nutritionistflag",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('71') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('133N00000X','133NN1002X',\
                                                                                '136A00000X') THEN 'Y' \
                                                  ELSE 'N' END AS Nutritionistflag")\
                                      )\
                            .withColumn("Endocrinologist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('46') THEN 'Y' \
                                                  ELSE 'N' END AS Endocrinologist")\
                                      )\
                            .withColumn("Urologist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('34') THEN 'Y' \
                                                  ELSE 'N' END AS Urologist")\
                                      )\
                            .withColumn("Cardiologist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('06','21','C3','C4') THEN 'Y' \
                                                  ELSE 'N' END AS Cardiologist")\
                                      )\
                            .withColumn("Radiologist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('45','74','92','94','95') THEN 'Y' \
                                                    WHEN Additionalcoloumn1 in ('2085B0100X','2085R0203X')\
                                                                                THEN 'Y' \
                                                  ELSE 'N' END AS Radiologist")\
                                      )\
                            .withColumn("Oncologist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('83','89','90','91') THEN 'Y' \
                                                  ELSE 'N' END AS Oncologist")\
                                      )\
                            .withColumn("PainSpecialist",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('09','72') THEN 'Y' \
                                                  ELSE 'N' END AS PainSpecialist")\
                                      )\
                            .withColumn("MedicalLabTechnician",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('47') THEN 'Y' \
                                                  ELSE 'N' END AS MedicalLabTechnician")\
                                      )\
                            .withColumn("ClinicalLabTechnician",\
                                        expr("CASE WHEN Additionalcoloumn2 in ('69') THEN 'Y' \
                                                  ELSE 'N' END AS ClinicalLabTechnician")\
                                      )
                            

provider_col_order = ['ProviderID',	'PCPFlag',	'OBGYNFlag',	'MHProviderFlag',	
                      'EyeCareProviderFlag',	'DentistFlag',	'NephrologistFlag',	
                      'AnesthesiologistFlag',	'NPRProviderFlag',	'PASProviderFlag',
                      'ProviderPrescribingPrivilegesFlag',	'ClinicalPharmacistFlag',	
                      'HospitalFlag',	'SNFFlag',	'SurgeonFlag',	'RegisteredNurseFlag',	
                      'PediatricianFlag',	'DiabetologistFlag',	'DieticianFlag',	
                      'PhysiotherapistFlag',	'NutritionistFlag',	'Endocrinologist',	
                      'Urologist',	'Cardiologist',	'Radiologist',	'Oncologist',	
                      'PainSpecialist',	'MedicalLabTechnician',	'ClinicalLabTechnician',	
                      'ProviderNPI',	'Additionalcoloumn1',	'Additionalcoloumn2']

final_qsi_df = final_qsi_df.select(provider_col_order)


# COMMAND ----------

# DBTITLE 1,Saving the converted QSI to containers
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#Assign the destination path for the Converted QSI file to a variable
file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'
#Convert spark dataframe to pandas dataframe
pandas_qsi_provider_df = final_qsi_df.toPandas()
#Copy data from pandas dataframe to csv file
pandas_qsi_provider_df.to_csv(f'{file_destination}QSI_to_Q360_provider_converted_{date}.txt',
                     index = False,sep = '|') 

# COMMAND ----------

# DBTITLE 1,Joining Original Q360 and converted QSI dfs
df_provider_join = df_Q360_provider.join(final_qsi_df,
                                        (df_Q360_provider.Provider_ID_q360 == final_qsi_df.ProviderID),
                                        'full')




# COMMAND ----------

# DBTITLE 1,Comparing Original Q360 and converted QSI dataframes
#Compare the Q360 and Converted QSI Dataframes based on the ProviderID
df_provider_join = df_provider_join.withColumn('ProviderID_status',\
                              when(col('ProviderID') == col('Provider_ID_q360'),'Y')\
                                .otherwise('N')) \
                            .withColumn('PCPFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('PCPFlag')== col('PCP_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('OBGYNFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('OBGYNFlag')== col('OBGYN_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('MHProviderFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('MHProviderFlag')== col('MH_Provider_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('EyeCareProviderFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('EyeCareProviderFlag')== col('Eye_Care_Provider_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('DentistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('DentistFlag')== col('Dentist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('NephrologistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('NephrologistFlag')== col('Nephrologist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('AnesthesiologistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('AnesthesiologistFlag')== col('Anesthesiologist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('NPRProviderFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('NPRProviderFlag')== col('NPR_Provider_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PASProviderFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('PASProviderFlag')== col('PAS_Provider_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('ProviderPrescribingPrivilegesFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('ProviderPrescribingPrivilegesFlag')== col('Provider_Prescribing_Privileges_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('ClinicalPharmacistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('ClinicalPharmacistFlag')== col('Clinical_Pharmacist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('HospitalFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('HospitalFlag')== col('Hospital_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('SNFFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('SNFFlag')== col('SNF_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('SurgeonFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('SurgeonFlag')== col('Surgeon_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('RegisteredNurseFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('RegisteredNurseFlag')== col('Registered_Nurse_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PediatricianFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('PediatricianFlag')== col('Pediatrician_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('DiabetologistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('DiabetologistFlag')== col('Diabetologist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('DieticianFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('DieticianFlag')== col('Dietician_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PhysiotherapistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('PhysiotherapistFlag')== col('Physiotherapist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('NutritionistFlag_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('NutritionistFlag')== col('Nutritionist_Flag_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Endocrinologist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Endocrinologist')== col('Endocrinologist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Urologist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Urologist')== col('Urologist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Cardiologist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Cardiologist')== col('Cardiologist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Radiologist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Radiologist')== col('Radiologist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Oncologist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Oncologist')== col('Oncologist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('PainSpecialist_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('PainSpecialist')== col('Pain_Specialist_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('MedicalLabTechnician_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('MedicalLabTechnician')== col('Medical_Lab_Technician_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('ClinicalLabTechnician_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('ClinicalLabTechnician')== col('Clinical_Lab_Technician_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('ProviderNPI_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('ProviderNPI')== col('Provider_NPI_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Additionalcoloumn1_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Additionalcoloumn1')== col('Additional_coloumn_1_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) \
                            .withColumn('Additionalcoloumn2_status',\
                              when(col('ProviderID')== col('Provider_ID_q360'), \
                                  when(col('Additionalcoloumn2')== col('Additional_coloumn_2_q360'),'Y')\
                                    .otherwise('N'))\
                              .otherwise('N')) 
                            
                            
status_columns = ['ProviderID',
                    'ProviderID_status','PCPFlag_status','OBGYNFlag_status',
                    'MHProviderFlag_status','EyeCareProviderFlag_status',
                    'DentistFlag_status','NephrologistFlag_status',
                    'AnesthesiologistFlag_status','NPRProviderFlag_status',
                    'PASProviderFlag_status','ProviderPrescribingPrivilegesFlag_status',
                    'ClinicalPharmacistFlag_status','HospitalFlag_status',
                    'SNFFlag_status','SurgeonFlag_status',
                    'RegisteredNurseFlag_status','PediatricianFlag_status',
                    'DiabetologistFlag_status','DieticianFlag_status',
                    'PhysiotherapistFlag_status','NutritionistFlag_status',
                    'Endocrinologist_status','Urologist_status',
                    'Cardiologist_status','Radiologist_status',
                    'Oncologist_status','PainSpecialist_status',
                    'MedicalLabTechnician_status','ClinicalLabTechnician_status',
                    'ProviderNPI_status','Additionalcoloumn1_status',
                    'Additionalcoloumn2_status']
                  
                  
df_comparison_results = df_provider_join.select(status_columns)



# COMMAND ----------

# DBTITLE 1,Load Comparison results to Temp View
df_comparison_results.createOrReplaceTempView("view_ProviderComparison_Results")

# COMMAND ----------

# DBTITLE 1,Drop table tblM_ProviderComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_ProviderComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_ProviderComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_ProviderComparison_Results
# MAGIC (
# MAGIC
# MAGIC   ProviderID VARCHAR(25),
# MAGIC   IsRecordMatching CHAR(1),
# MAGIC   ProviderID_status CHAR(1),
# MAGIC   PCPFlag_status CHAR(1),
# MAGIC   OBGYNFlag_status CHAR(1),
# MAGIC   MHProviderFlag_status CHAR(1),
# MAGIC   EyeCareProviderFlag_status CHAR(1),
# MAGIC   DentistFlag_status CHAR(1),
# MAGIC   NephrologistFlag_status CHAR(1),
# MAGIC   AnesthesiologistFlag_status CHAR(1),
# MAGIC   NPRProviderFlag_status CHAR(1),
# MAGIC   PASProviderFlag_status CHAR(1),
# MAGIC   ProviderPrescribingPrivilegesFlag_status CHAR(1),
# MAGIC   ClinicalPharmacistFlag_status CHAR(1),
# MAGIC   HospitalFlag_status CHAR(1),
# MAGIC   SNFFlag_status CHAR(1),
# MAGIC   SurgeonFlag_status CHAR(1),
# MAGIC   RegisteredNurseFlag_status CHAR(1),
# MAGIC   PediatricianFlag_status CHAR(1),
# MAGIC   DiabetologistFlag_status CHAR(1),
# MAGIC   DieticianFlag_status CHAR(1),
# MAGIC   PhysiotherapistFlag_status CHAR(1),
# MAGIC   NutritionistFlag_status CHAR(1),
# MAGIC   Endocrinologist_status CHAR(1),
# MAGIC   Urologist_status CHAR(1),
# MAGIC   Cardiologist_status CHAR(1),
# MAGIC   Radiologist_status CHAR(1),
# MAGIC   Oncologist_status CHAR(1),
# MAGIC   PainSpecialist_status CHAR(1),
# MAGIC   MedicalLabTechnician_status CHAR(1),
# MAGIC   ClinicalLabTechnician_status CHAR(1),
# MAGIC   ProviderNPI_status CHAR(1),
# MAGIC   Additionalcoloumn1_status CHAR(1),
# MAGIC   Additionalcoloumn2_status CHAR(1)
# MAGIC   
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Insert data from Temp View into tblM_ProviderComparison_Results
# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO tblM_ProviderComparison_Results 
# MAGIC SELECT DISTINCT
# MAGIC     ProviderID,
# MAGIC     'Y' AS IsRecordMatching,
# MAGIC     ProviderID_status,
# MAGIC     PCPFlag_status,
# MAGIC     OBGYNFlag_status,
# MAGIC     MHProviderFlag_status,
# MAGIC     EyeCareProviderFlag_status,
# MAGIC     DentistFlag_status,
# MAGIC     NephrologistFlag_status,
# MAGIC     AnesthesiologistFlag_status,
# MAGIC     NPRProviderFlag_status,
# MAGIC     PASProviderFlag_status,
# MAGIC     ProviderPrescribingPrivilegesFlag_status,
# MAGIC     ClinicalPharmacistFlag_status,
# MAGIC     HospitalFlag_status,
# MAGIC     SNFFlag_status,
# MAGIC     SurgeonFlag_status,
# MAGIC     RegisteredNurseFlag_status,
# MAGIC     PediatricianFlag_status,
# MAGIC     DiabetologistFlag_status,
# MAGIC     DieticianFlag_status,
# MAGIC     PhysiotherapistFlag_status,
# MAGIC     NutritionistFlag_status,
# MAGIC     Endocrinologist_status,
# MAGIC     Urologist_status,
# MAGIC     Cardiologist_status,
# MAGIC     Radiologist_status,
# MAGIC     Oncologist_status,
# MAGIC     PainSpecialist_status,
# MAGIC     MedicalLabTechnician_status,
# MAGIC     ClinicalLabTechnician_status,
# MAGIC     ProviderNPI_status,
# MAGIC     Additionalcoloumn1_status,
# MAGIC     Additionalcoloumn2_status
# MAGIC
# MAGIC FROM view_ProviderComparison_Results
# MAGIC
# MAGIC

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the status of individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_ProviderComparison_Results
# MAGIC   SET IsRecordMatching = CASE 
# MAGIC                               WHEN ProviderID_status = 'N' OR 
# MAGIC                                     PCPFlag_status = 'N' OR 
# MAGIC                                     OBGYNFlag_status = 'N' OR 
# MAGIC                                     MHProviderFlag_status = 'N' OR 
# MAGIC                                     EyeCareProviderFlag_status = 'N' OR 
# MAGIC                                     DentistFlag_status = 'N' OR 
# MAGIC                                     NephrologistFlag_status = 'N' OR 
# MAGIC                                     AnesthesiologistFlag_status = 'N' OR 
# MAGIC                                     NPRProviderFlag_status = 'N' OR 
# MAGIC                                     PASProviderFlag_status = 'N' OR 
# MAGIC                                     ProviderPrescribingPrivilegesFlag_status = 'N' OR 
# MAGIC                                     ClinicalPharmacistFlag_status = 'N' OR 
# MAGIC                                     HospitalFlag_status = 'N' OR 
# MAGIC                                     SNFFlag_status = 'N' OR 
# MAGIC                                     SurgeonFlag_status = 'N' OR 
# MAGIC                                     RegisteredNurseFlag_status = 'N' OR 
# MAGIC                                     PediatricianFlag_status = 'N' OR 
# MAGIC                                     DiabetologistFlag_status = 'N' OR
# MAGIC                                     DieticianFlag_status = 'N' OR 
# MAGIC                                     PhysiotherapistFlag_status = 'N' OR 
# MAGIC                                     NutritionistFlag_status = 'N' OR 
# MAGIC                                     Endocrinologist_status = 'N' OR 
# MAGIC                                     Urologist_status = 'N' OR 
# MAGIC                                     Cardiologist_status = 'N' OR 
# MAGIC                                     Radiologist_status = 'N' OR 
# MAGIC                                     Oncologist_status = 'N' OR 
# MAGIC                                     PainSpecialist_status = 'N' OR 
# MAGIC                                     MedicalLabTechnician_status = 'N' OR 
# MAGIC                                     ClinicalLabTechnician_status = 'N' OR 
# MAGIC                                     ProviderNPI_status = 'N' OR 
# MAGIC                                     Additionalcoloumn1_status = 'N' OR 
# MAGIC                                     Additionalcoloumn2_status = 'N'  
# MAGIC                                   THEN 'N'
# MAGIC                                 ELSE 'Y'
# MAGIC                               END

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
# MAGIC       'PROVIDER' AS FileType,
# MAGIC       (SELECT count(ProviderID) FROM OriginalQ360_Provider) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_ProviderComparison_Results.ProviderID) 
# MAGIC       FROM OriginalQ360_Provider
# MAGIC       INNER JOIN tblM_ProviderComparison_Results
# MAGIC       on OriginalQ360_Provider.ProviderID = tblM_ProviderComparison_Results.ProviderID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_ProviderComparison_Results.ProviderID) 
# MAGIC       FROM OriginalQ360_Provider
# MAGIC       FULL OUTER JOIN tblM_ProviderComparison_Results
# MAGIC       on OriginalQ360_Provider.ProviderID = tblM_ProviderComparison_Results.ProviderID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords
# MAGIC
# MAGIC   
# MAGIC

# COMMAND ----------

# DBTITLE 1,Saving the Q360 Comparison results to a csv file 
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')
df_final_status = df_final.toPandas()

df_final_status.to_csv(f'/dbfs/mnt/{clientName}Q360/Results/{destination_location}/Provider_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Save the Provider Comparison results to a csv file
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Provider = spark.sql('SELECT * FROM tblM_ProviderComparison_Results ORDER BY ProviderID')
df_Provider_Pandas = df_Provider.toPandas()

df_Provider_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Result/{destination_location}/Provider_Comparison_{date}.csv')  


# COMMAND ----------

# DBTITLE 1,Notebook exit comment to get the status of notebook run
dbutils.notebook.exit("Success")


