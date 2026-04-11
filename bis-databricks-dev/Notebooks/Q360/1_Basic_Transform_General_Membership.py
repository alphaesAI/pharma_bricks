# Databricks notebook source
# MAGIC %md 
# MAGIC ## 1_Basic_Transform_General_Membership

# COMMAND ----------

# DBTITLE 1,Required libraries
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

# DBTITLE 1,Load Original Q360 General Membership file to data frame
#store the mounted file path to a variable
member_q360 = f'/mnt/{clientName}/Q360/Q360/{q360_location}' 


#schema for Original Q360 file
schema = StructType([
    StructField("Member_ID_q360", StringType(),True),
    StructField("Gender_q360", StringType(), True),
    StructField("Date_of_Birth_q360", StringType(), True),
    StructField("Member_Last_Name_q360", StringType(),True),
    StructField("Member_First_Name_q360", StringType(), True),
    StructField("Member_Middle_Initial_q360", StringType(), True),
    StructField("Subscriber_or_Family_ID_Number_q360", StringType(),True),
    StructField("Mailing_Address_1_q360", StringType(), True),
    StructField("Mailing_Address_2_q360", StringType(), True),
    StructField("City_q360", StringType(),True),
    StructField("State_q360", StringType(), True),
    StructField("Zip_q360", StringType(), True),
    StructField("Telephone_Number_q360", StringType(),True),
    StructField("Parent_Caretaker_First_Name_q360", StringType(), True),
    StructField("Parent_Caretaker_Middle_Initial_q360", StringType(), True),
    StructField("Parent_Caretaker_Last_Name_q360", StringType(),True),
    StructField("Spoken_Language_q360", StringType(), True),
    StructField("Spoken_Language_Source_q360", StringType(), True),
    StructField("Written_Language_q360", StringType(),True),
    StructField("Written_Language_Source_q360", StringType(), True),
    StructField("Other_Language_q360", StringType(), True),
    StructField("Other_Language_Source_q360", StringType(),True),
    StructField("MBI_q360", StringType(), True),
    StructField("Contract_id_q360", StringType(), True),
    StructField("Race_q360", StringType(),True),
    StructField("Ethnicity_q360", StringType(), True),
    StructField("Race_Data_Source_q360", StringType(), True),
    StructField("Ethnicity_Data_Source_q360", StringType(),True),
    StructField("QHP_Issuer_Legal_Name_q360", StringType(), True),
    StructField("Enrollee_Education_q360", StringType(), True),
    StructField("Enrollee_Employment_q360", StringType(), True),
    StructField("Issuer_ID_q360", StringType(), True),
    StructField("QHP_State_q360", StringType(),True),
    StructField("Metal_Level_q360", StringType(), True),
    StructField("Variant_ID_q360", StringType(), True),
    StructField("APTC_Eligibility_Flag_q360", StringType(),True),
    StructField("Plan_Marketing_Name_q360", StringType(), True),
    StructField("MedicaidExpansionQHPEnrollee_q360", StringType(), True),
    StructField("Reporting_Status_q360", StringType(),True),
    StructField("Enrollee_Email_Address_q360", StringType(), True),
    StructField("Enrollee_Phone_2_q360", StringType(), True),
    StructField("Total_Enrollment_q360", StringType(), True),
    StructField("Parent_caretaker_email_address_q360", StringType(), True),
    StructField("Deceased_date_q360", StringType(),True),
    StructField("Additional_coloumn_1_q360", StringType(), True),
    StructField("Additional_coloumn_2_q360", StringType(), True),
    StructField("Additional_coloumn_3_q360", StringType(),True),
    StructField("Additional_coloumn_4_q360", StringType(), True),
    StructField("Additional_coloumn_5_q360", StringType(), True),
    StructField("Filler_q360", StringType(), True)
    ])
df_q360 = spark.read.option("delimiter",'|').schema(schema).csv(member_q360)


# COMMAND ----------

# DBTITLE 1,Loading data frame to the Temp View
df_q360.createOrReplaceTempView("view_OriginalQ360data")

# COMMAND ----------

# DBTITLE 1,Drop the table OriginalQ360_Member
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS OriginalQ360_Member 

# COMMAND ----------

# DBTITLE 1,Create the table OriginalQ360_Member
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS OriginalQ360_Member
# MAGIC (
# MAGIC MemberID VARCHAR(16),
# MAGIC Gender VARCHAR(1),
# MAGIC DateofBirth VARCHAR(8),
# MAGIC MemberLastName VARCHAR(20),
# MAGIC MemberFirstName VARCHAR(20),
# MAGIC MemberMiddleInitial VARCHAR(1),
# MAGIC SubscriberID VARCHAR(16),
# MAGIC MailingAddress1 VARCHAR(50),
# MAGIC MailingAddress2 VARCHAR(50),
# MAGIC City VARCHAR(30),
# MAGIC State VARCHAR(2),
# MAGIC Zip VARCHAR(5),
# MAGIC TelephoneNumber VARCHAR(10),
# MAGIC ParentFirstName VARCHAR(25),
# MAGIC ParentMiddleInitial VARCHAR(1),
# MAGIC ParentLastName VARCHAR(25),
# MAGIC SpokenLanguage VARCHAR(2),
# MAGIC SpokenLanguageSource VARCHAR(2),
# MAGIC WrittenLanguage VARCHAR(2),
# MAGIC WrittenLanguageSource VARCHAR(2),
# MAGIC OtherLanguage VARCHAR(2),
# MAGIC OtherLanguageSource VARCHAR(2),
# MAGIC MBI VARCHAR(12),
# MAGIC ContractID VARCHAR(10),
# MAGIC Race VARCHAR(6),
# MAGIC Ethnicity VARCHAR(6),
# MAGIC RaceDataSource VARCHAR(2),
# MAGIC EthnicityDataSource VARCHAR(2),
# MAGIC QHPIssuerLegalName CHAR(60),
# MAGIC EnrolleeEducation INT,
# MAGIC EnrolleeEmployment INT,
# MAGIC IssuerID INT,
# MAGIC QHPState INT,
# MAGIC MetalLevel INT,
# MAGIC VariantID CHAR(2),
# MAGIC APTCEligibilityFlag INT,
# MAGIC PlanMarketingName CHAR(250),
# MAGIC MedicaidExpansionQHPEnrollee INT,
# MAGIC ReportingStatus INT,
# MAGIC EnrolleeEmailAddress CHAR(320),
# MAGIC EnrolleePhone2 INT,
# MAGIC TotalEnrollment INT,
# MAGIC Parentemailaddress VARCHAR(25),
# MAGIC Deceaseddate DATE,
# MAGIC Additionalcoloumn1  VARCHAR(25),
# MAGIC Additionalcoloumn2 VARCHAR(25),
# MAGIC Additionalcoloumn3 VARCHAR(25),
# MAGIC Additionalcoloumn4 VARCHAR(25),
# MAGIC Additionalcoloumn5 VARCHAR(25),
# MAGIC Filler VARCHAR(200)
# MAGIC
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Load data from Temp View to the table OriginalQ360_Member
# MAGIC %sql
# MAGIC INSERT INTO OriginalQ360_Member
# MAGIC SELECT DISTINCT
# MAGIC     IFNULL(Member_ID_q360,"") AS Member_ID
# MAGIC     ,IFNULL(Gender_q360,"") AS Gender
# MAGIC     ,IFNULL(Date_of_Birth_q360,"") AS Date_of_Birth
# MAGIC     ,IFNULL(Member_Last_Name_q360,"") AS Member_Last_Name
# MAGIC     ,IFNULL(Member_First_Name_q360,"") AS Member_First_Name
# MAGIC     ,IFNULL(Member_Middle_Initial_q360,"") AS Member_Middle_Initial
# MAGIC     ,IFNULL(Subscriber_or_Family_ID_Number_q360,"") AS Subscriber_or_Family_ID_Number
# MAGIC     ,IFNULL(Mailing_Address_1_q360,"") AS Mailing_Address_1
# MAGIC     ,IFNULL(Mailing_Address_2_q360,"") AS Mailing_Address_2
# MAGIC     ,IFNULL(City_q360,"") AS City
# MAGIC     ,IFNULL(State_q360,"") AS State
# MAGIC     ,IFNULL(Zip_q360,"") AS Zip
# MAGIC     ,IFNULL(Telephone_Number_q360,"") AS Telephone_Number
# MAGIC     ,IFNULL(Parent_Caretaker_First_Name_q360,"") AS Parent_Caretaker_First_Name
# MAGIC     ,IFNULL(Parent_Caretaker_Middle_Initial_q360,"") AS Parent_Caretaker_Middle_Initial
# MAGIC     ,IFNULL(Parent_Caretaker_Last_Name_q360,"") AS Parent_Caretaker_Last_Name
# MAGIC     ,IFNULL(Spoken_Language_q360,"") AS Spoken_Language
# MAGIC     ,IFNULL(Spoken_Language_Source_q360,"") AS Spoken_Language_Source
# MAGIC     ,IFNULL(Written_Language_q360,"") AS Written_Language
# MAGIC     ,IFNULL(Written_Language_Source_q360,"") AS Written_Language_Source
# MAGIC     ,IFNULL(Other_Language_q360,"") AS Other_Language
# MAGIC     ,IFNULL(Other_Language_Source_q360,"") AS Other_Language_Source
# MAGIC     ,IFNULL(MBI_q360,"") AS MBI
# MAGIC     ,IFNULL(Contract_id_q360,"") AS Contract_id
# MAGIC     ,IFNULL(Race_q360,"") AS Race
# MAGIC     ,IFNULL(Ethnicity_q360,"") AS Ethnicity
# MAGIC     ,IFNULL(Race_Data_Source_q360,"") AS Race_Data_Source
# MAGIC     ,IFNULL(Ethnicity_Data_Source_q360,"") AS Ethnicity_Data_Source
# MAGIC     ,IFNULL(QHP_Issuer_Legal_Name_q360,"") AS QHP_Issuer_Legal_Name
# MAGIC     ,IFNULL(Enrollee_Education_q360,"") AS Enrollee_Education
# MAGIC     ,IFNULL(Enrollee_Employment_q360,"") AS Enrollee_Employment
# MAGIC     ,IFNULL(Issuer_ID_q360,"") AS Issuer_ID
# MAGIC     ,IFNULL(QHP_State_q360,"") AS QHP_State
# MAGIC     ,IFNULL(Metal_Level_q360,"") AS Metal_Level
# MAGIC     ,IFNULL(Variant_ID_q360,"") AS Variant_ID
# MAGIC     ,IFNULL(APTC_Eligibility_Flag_q360,"") AS APTC_Eligibility_Flag
# MAGIC     ,IFNULL(Plan_Marketing_Name_q360,"") AS Plan_Marketing_Name
# MAGIC     ,IFNULL(MedicaidExpansionQHPEnrollee_q360,"") AS MedicaidExpansionQHPEnrollee
# MAGIC     ,IFNULL(Reporting_Status_q360,"") AS Reporting_Status
# MAGIC     ,IFNULL(Enrollee_Email_Address_q360,"") AS Enrollee_Email_Address
# MAGIC     ,IFNULL(Enrollee_Phone_2_q360,"") AS Enrollee_Phone_2
# MAGIC     ,IFNULL(Total_Enrollment_q360,"") AS Total_Enrollment
# MAGIC     ,IFNULL(Parent_caretaker_email_address_q360,"") AS Parent_caretaker_email_address
# MAGIC     ,IFNULL(Deceased_date_q360,"") AS Deceased_date
# MAGIC     ,IFNULL(Additional_coloumn_1_q360,"") AS Additional_coloumn_1
# MAGIC     ,IFNULL(Additional_coloumn_2_q360,"") AS Additional_coloumn_2
# MAGIC     ,IFNULL(Additional_coloumn_3_q360,"") AS Additional_coloumn_3
# MAGIC     ,IFNULL(Additional_coloumn_4_q360,"") AS Additional_coloumn_4
# MAGIC     ,IFNULL(Additional_coloumn_5_q360,"") AS Additional_coloumn_5
# MAGIC     ,IFNULL(Filler_q360,"") AS Filler
# MAGIC
# MAGIC FROM view_OriginalQ360data

# COMMAND ----------

# DBTITLE 1, Load and transform data from the QSI Member file
# Assign QSI file from mounted location to a variable

file_path_QSI = f'/mnt/{clientName}/Q360/QSI/{qsi_location}'
#Load QSI file to the spark data frame 
df_qsi = spark.read.option("delimiter","\t").option("header","true").csv(file_path_QSI)

membercol_needed = ["MemberKey","Sex","DOB",
                    "MemberLastName","MemberFirstName","MemberMiddleName",
                    "SubscriberKey","MemberAddress1","MemberAddress2",
                    "MemberCity","MemberState","MemberZip","MemberPhone1",
                    "LanguageSpoken","LanguageSpokenSource",
                    "LanguageWritten","LanguageWrittenSource",
                    "LanguageOther","LanguageOtherSource",
                    "MedicareID","CMSPlanID",
                    "RaceType","EthnicityType",
                    "RaceSource","EthnicitySource",
                    "QHPEnrolleeEducation","QHPEnrolleeEmployment","DeathDate"]

# QSI dataframe with required columns for Transdformation (Source)
df_qsi = df_qsi.select(membercol_needed)


# Renaming QSI columns with respect to Q360 files.
df_qsi = df_qsi.withColumnRenamed('Sex','Gender')\
                          .withColumnRenamed('MemberAddress1','MailingAddress1') \
                          .withColumnRenamed('MemberAddress2','MailingAddress2') \
                          .withColumnRenamed('MemberState','State')\
                          .withColumnRenamed('CMSPlanID','ContractID') \
                          .withColumnRenamed('EthnicityType','Ethnicity') \
                          .withColumnRenamed('QHPEnrolleeEducation','EnrolleeEducation')\
                          .withColumnRenamed('QHPEnrolleeEmployment','EnrolleeEmployment')  


df_qsi =  df_qsi.withColumn("Member_ID",substring(col("MemberKey"),0,16))\
                          .withColumn("DateofBirth",date_format("DOB",'yyyyMMdd')) \
                          .withColumn("Member_lastname",substring(col("MemberLastName"),0,20))\
                          .withColumn("Member_firstname",substring(col("MemberFirstName"),0,20))\
                          .withColumn("MemberMiddleInitial",substring(col("MemberMiddleName"),0,1)) \
                          .withColumn("SubscriberorFamilyIDNumber",substring(col("SubscriberKey"),0,16)) \
                          .withColumn("City",substring(col("MemberCity"),0,30)) \
                          .withColumn("Zip",substring(col("MemberZip"),0,5)) \
                          .withColumn("TelephoneNumber",substring(col("MemberPhone1"),0,10)) \
                          .withColumn('Deceaseddate',date_format('DeathDate','yyyyMMdd')) \
                          .withColumn('SpokenLanguage',when(col('LanguageSpoken') == 'E', 31)\
                                                      .when(col('LanguageSpoken').isin(['C','S','M','N']),32)\
                                                      .when(col('LanguageSpoken') == 'D',38) \
                                                      .otherwise(39)) \
                          .withColumn('OtherLanguage',when(col('LanguageOther') == 'E',71) \
                                                      .when(col('LanguageSpoken').isin(['C','S','M','N']),72)\
                                                      .when(col('LanguageSpoken') == 'D',78) \
                                                      .otherwise(79)) \
                          .withColumn('SpokenLanguageSource',when(col('LanguageSpokenSource')== 'D',41) \
                                                            .when(col('LanguageSpokenSource') == 'c',42)\
                                                            .when(col('LanguageSpokenSource') == 'S',43) \
                                                            .otherwise(49)) \
                          .withColumn('WrittenLanguage',when(col('LanguageWritten') == 'E', 51) \
                                                        .when(col('LanguageWritten').isin(['C','S','M','N']),52)\
                                                        .when(col('LanguageWritten') == 'D',58) \
                                                        .otherwise(59)) \
                          .withColumn('WrittenLanguageSource',when(col('LanguageWrittenSource') == 'D',61) \
                                                              .when(col('LanguageWrittenSource') == 'C',62)\
                                                              .when(col('LanguageWrittenSource') == 'S', 63) \
                                                              .otherwise(69)) \
                          .withColumn('OtherLanguageSource',when(col('LanguageOtherSource') == 'D',81)\
                                                            .when(col('LanguageOtherSource') == 'C',82)\
                                                            .when(col('LanguageOtherSource') =='S',83) \
                                                            .otherwise(89)) \
                          .withColumn('MBI',substring(col('MedicareID'),0,12)) \
                          .withColumn('Race',expr('substring(RaceType,-1,1)')) \
                          .withColumn('RaceDataSource',when(col('RaceSource') == 'C',21)\
                                                      .when(col('RaceSource') == 'S',22)\
                                                      .when(col('RaceSource') == 'N',23)\
                                                      .when(col('RaceSource') == 'G',24)\
                                                      .when(col('RaceSource') == 'D',25)\
                                                      .when(col('RaceSource') == 'U',28)\
                                                      .otherwise(29)) \
                          .withColumn('EthnicityDataSource', when(col('EthnicitySource') == 'C',91) \
                                                            .when(col('EthnicitySource') == 'S',92)\
                                                            .when(col('EthnicitySource') == 'N', 93)\
                                                            .when(col('EthnicitySource') == 'G',94)\
                                                            .when(col('EthnicitySource') == 'D',95)\
                                                            .when(col('EthnicitySource') == 'U',98)\
                                                            .otherwise(99)) \
                          .drop("MemberKey","DOB","MemberLastName",
                                "DeathDate","MemberFirstName","MemberMiddleName",
                                "SubscriberKey","MemberZip","MemberPhone1",
                                "LanguageSpoken","LanguageSpokenSource",
                                "LanguageWritten","LanguageWrittenSource",
                                "LanguageOtherSource","LanguageOtherSource",
                                "MedicareID","RaceType","MemberCity",
                                "RaceSource","EthnicitySource","LanguageOther")


final_column_qsi_to_q360 = ["Member_ID","Gender","DateofBirth",
                            "Member_LastName","Member_FirstName","MemberMiddleInitial","SubscriberorFamilyIDNumber","MailingAddress1","MailingAddress2",
                            "City","State","Zip","TelephoneNumber",
                            "SpokenLanguage","SpokenLanguageSource",
                            "WrittenLanguage","WrittenLanguageSource",
                            "OtherLanguage","OtherLanguageSource",
                            "MBI","ContractID",
                            "Race","Ethnicity",
                            "RaceDataSource","EthnicityDataSource",
                            "EnrolleeEducation","EnrolleeEmployment","Deceaseddate"]

df_qsi = df_qsi.select(final_column_qsi_to_q360)



# COMMAND ----------

# DBTITLE 1,Loading converted QSI to storage container
#Convert spark dataframe into pandas dataframe
pandas_qsi_df = df_qsi.toPandas()
#Convert pandas dataframe into a csv file

file_destination = f'/dbfs/mnt/{clientName}/Q360/QSI_Converted/'

date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
pandas_qsi_df.to_csv(f'{file_destination}QSI_to_Q360_member_converted_{date}.txt',
                     index = False,sep = '|')


# COMMAND ----------

# DBTITLE 1,Join data frames of Q360 data and Converted QSI data
# Perform the full outer join operation with df_q360 and qsi
df_full_join = df_qsi.join(df_q360, (df_qsi.Member_ID == df_q360.Member_ID_q360), 'full')


# COMMAND ----------

# DBTITLE 1,Compare data from QSI and Q360 Data frames
#Comparison logic based on the Member_ID
df_full_join = df_full_join.withColumn('Member_ID_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),'Y') \
                                        .otherwise('N'))\
                                      .withColumn('Date_of_birth_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('DateofBirth') == col('Date_of_Birth_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N'))\
                                      .withColumn('Gender_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('Gender') == col('Gender_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N'))\
                                      .withColumn('Member_Last_Name_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('Member_lastname') == col('Member_Last_Name_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Member_First_Name_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('Member_firstname') == col('Member_First_Name_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N'))\
                                      .withColumn('Member_Middle_initial_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('MemberMiddleInitial') == col('Member_Middle_Initial_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N'))\
                                      .withColumn('Subscriber_or_Family_ID_Number_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('SubscriberorFamilyIDNumber') == col('Subscriber_or_Family_ID_Number_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Mailing_Address_1_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('MailingAddress1') == col('Mailing_Address_1_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Mailing_Address_2_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('MailingAddress2') == col('Mailing_Address_2_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('City_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('City') == col('City_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('State_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('State') == col('State_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Zip_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('Zip') == col('Zip_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Telephone_Number_status'\
                                        ,when(col('Member_ID')== col('Member_ID_q360'),\
                                          when(col('TelephoneNumber') == col('Telephone_Number_q360'),'Y')\
                                          .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Spoken_Language_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('SpokenLanguage') == col('Spoken_Language_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Spoken_Language_Sources_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('SpokenLanguageSource') == col('Spoken_Language_Source_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Written_Language_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('WrittenLanguage') == col('Written_Language_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Written_Language_Source_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('WrittenLanguageSource') == col('Written_Language_Source_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Other_Language_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('OtherLanguage') == col('Other_Language_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Other_Language_Source_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('OtherLanguageSource') == col('Other_Language_Source_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('MBI_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('MBI') == col('MBI_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Contract_id_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('Contractid') == col('Contract_id_q360'),'Y')\
                                              .otherwise('N'))\
                                          .otherwise('N'))\
                                      .withColumn('Race_q360_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('Race') == col('Race_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Ethnicity_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('Ethnicity') == col('Ethnicity_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Race_Data_Source_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('RaceDataSource') == col('Race_Data_Source_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Ethnicity_Data_Source_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('EthnicityDataSource') == col('Ethnicity_Data_Source_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Enrollee_Education_status',\
                                        when(col('Member_ID') == col('Member_ID_q360'),\
                                            when(col('EnrolleeEducation') == col('Enrollee_Education_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Enrollee_Employment_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('EnrolleeEmployment') == col('Enrollee_Employment_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N')) \
                                      .withColumn('Deceased_date_status',\
                                        when(col('Member_ID')== col('Member_ID_q360'),\
                                            when(col('Deceaseddate') == col('Deceased_date_q360'),'Y')\
                                            .otherwise('N'))\
                                        .otherwise('N'))

status_columns = ['Member_ID',
                  'Member_ID_status','Gender_status','Date_of_birth_status',
                  'Member_Last_Name_status','Member_First_Name_status','Member_Middle_initial_status','Subscriber_or_Family_ID_Number_status',
                  'Mailing_Address_1_status','Mailing_Address_2_status',
                  'City_status','State_status','Zip_status','Telephone_Number_status',
                  'Spoken_Language_status','Spoken_Language_Sources_status',
                  'Written_Language_status','Written_Language_Source_status',
                  'Other_Language_status','Other_Language_Source_status',
                  'MBI_status','Contract_id_status',
                  'Race_q360_status','Ethnicity_status',
                  'Race_Data_Source_status','Ethnicity_Data_Source_status',
                  'Enrollee_Education_status','Enrollee_Employment_status',
                  'Deceased_date_status']

df_qsi_q360_status = df_full_join.select(status_columns)

#display(df_qsi_q360_status.select('*'))


# COMMAND ----------

# DBTITLE 1,Load Comparison results to Temp View
df_qsi_q360_status.createOrReplaceTempView("view_MemberComparison_Results")

# COMMAND ----------

# DBTITLE 1,Drop table tblM_MemberComparison_Results
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tblM_MemberComparison_Results

# COMMAND ----------

# DBTITLE 1,Create table tblM_MemberComparison_Results
# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS tblM_MemberComparison_Results
# MAGIC (
# MAGIC
# MAGIC     Member_ID VARCHAR(16),
# MAGIC     IsRecordMatching CHAR(1),
# MAGIC     Member_ID_status CHAR(1),
# MAGIC     Gender_status CHAR(1),
# MAGIC     Date_of_birth_status CHAR(1),
# MAGIC     Member_Last_Name_status CHAR(1),
# MAGIC     Member_First_Name_status CHAR(1),
# MAGIC     Member_Middle_initial_status CHAR(1),
# MAGIC     Subscriber_or_Family_ID_Number_status CHAR(1),
# MAGIC     Mailing_Address_1_status CHAR(1),
# MAGIC     Mailing_Address_2_status CHAR(1),
# MAGIC     City_status CHAR(1),
# MAGIC     State_status CHAR(1),
# MAGIC     Zip_status CHAR(1),
# MAGIC     Telephone_Number_status CHAR(1),
# MAGIC     Spoken_Language_status CHAR(1),
# MAGIC     Spoken_Language_Sources_status CHAR(1),
# MAGIC     Written_Language_status CHAR(1),
# MAGIC     Written_Language_Source_status CHAR(1),
# MAGIC     Other_Language_status CHAR(1),
# MAGIC     Other_Language_Source_status CHAR(1),
# MAGIC     MBI_status CHAR(1),
# MAGIC     Contract_id_status CHAR(1),
# MAGIC     Race_q360_status CHAR(1),
# MAGIC     Ethnicity_status CHAR(1),
# MAGIC     Race_Data_Source_status CHAR(1),
# MAGIC     Ethnicity_Data_Source_status CHAR(1),
# MAGIC     Enrollee_Education_status CHAR(1),
# MAGIC     Enrollee_Employment_status CHAR(1),
# MAGIC     Deceased_date_status CHAR(1)
# MAGIC )

# COMMAND ----------

# DBTITLE 1,Insert data from Temp View into tblM_MemberComparison_Results
# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO tblM_MemberComparison_Results 
# MAGIC SELECT DISTINCT
# MAGIC     Member_ID,
# MAGIC     'Y' AS IsRecordMatching ,
# MAGIC     Member_ID_status ,
# MAGIC     Gender_status ,
# MAGIC     Date_of_birth_status ,
# MAGIC     Member_Last_Name_status ,
# MAGIC     Member_First_Name_status ,
# MAGIC     Member_Middle_initial_status ,
# MAGIC     Subscriber_or_Family_ID_Number_status ,
# MAGIC     Mailing_Address_1_status ,
# MAGIC     Mailing_Address_2_status ,
# MAGIC     City_status ,
# MAGIC     State_status ,
# MAGIC     Zip_status ,
# MAGIC     Telephone_Number_status ,
# MAGIC     Spoken_Language_status ,
# MAGIC     Spoken_Language_Sources_status ,
# MAGIC     Written_Language_status ,
# MAGIC     Written_Language_Source_status ,
# MAGIC     Other_Language_status ,
# MAGIC     Other_Language_Source_status ,
# MAGIC     MBI_status ,
# MAGIC     Contract_id_status ,
# MAGIC     Race_q360_status ,
# MAGIC     Ethnicity_status ,
# MAGIC     Race_Data_Source_status ,
# MAGIC     Ethnicity_Data_Source_status ,
# MAGIC     Enrollee_Education_status ,
# MAGIC     Enrollee_Employment_status ,
# MAGIC     Deceased_date_status  
# MAGIC
# MAGIC FROM view_MemberComparison_Results

# COMMAND ----------

# DBTITLE 1,Update the flag IsRecordMatching based on the status of individual columns
# MAGIC %sql
# MAGIC UPDATE tblM_MemberComparison_Results
# MAGIC   SET IsRecordMatching = CASE 
# MAGIC                               WHEN Member_ID_status = 'N' OR 
# MAGIC                                     Gender_status = 'N' OR 
# MAGIC                                     Date_of_birth_status = 'N' OR 
# MAGIC                                     Member_Last_Name_status = 'N' OR 
# MAGIC                                     Member_First_Name_status = 'N' OR 
# MAGIC                                     Member_Middle_initial_status = 'N' OR 
# MAGIC                                     Subscriber_or_Family_ID_Number_status = 'N' OR 
# MAGIC                                     Mailing_Address_1_status = 'N' OR 
# MAGIC                                     Mailing_Address_2_status = 'N' OR 
# MAGIC                                     City_status = 'N' OR 
# MAGIC                                     State_status = 'N' OR 
# MAGIC                                     Zip_status = 'N' OR 
# MAGIC                                     Telephone_Number_status = 'N' OR 
# MAGIC                                     Spoken_Language_status = 'N' OR 
# MAGIC                                     Spoken_Language_Sources_status = 'N' OR 
# MAGIC                                     Written_Language_status = 'N' OR 
# MAGIC                                     Written_Language_Source_status = 'N' OR 
# MAGIC                                     Other_Language_status = 'N' OR 
# MAGIC                                     Other_Language_Source_status = 'N' OR 
# MAGIC                                     MBI_status = 'N' OR 
# MAGIC                                     Contract_id_status = 'N' OR 
# MAGIC                                     Race_q360_status = 'N' OR 
# MAGIC                                     Ethnicity_status = 'N' OR 
# MAGIC                                     Race_Data_Source_status = 'N' OR 
# MAGIC                                     Ethnicity_Data_Source_status = 'N' OR 
# MAGIC                                     Enrollee_Education_status = 'N' OR 
# MAGIC                                     Enrollee_Employment_status = 'N' OR 
# MAGIC                                     Deceased_date_status = 'N' 
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
# MAGIC       'MEMBER' AS FileType,
# MAGIC       (SELECT count(MemberID) FROM OriginalQ360_Member) AS OrgQ360_Rowcount,
# MAGIC       (SELECT count(tblM_MemberComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Member
# MAGIC       INNER JOIN tblM_MemberComparison_Results
# MAGIC       on originalq360_member.MemberID = tblM_MemberComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'Y') AS MatchingRecords,
# MAGIC       (SELECT count(tblM_MemberComparison_Results.Member_ID) 
# MAGIC       FROM OriginalQ360_Member
# MAGIC       FULL OUTER JOIN tblM_MemberComparison_Results
# MAGIC       on originalq360_member.MemberID = tblM_MemberComparison_Results.Member_ID
# MAGIC       AND IsRecordMatching = 'N') AS MismatchRecords
# MAGIC
# MAGIC   
# MAGIC

# COMMAND ----------

# DBTITLE 1,Saving the Q360 Comparison results to a csv file 
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_final = spark.sql('SELECT DISTINCT * FROM tblM_Q360_Comparison_Results')
df_final_status = df_final.toPandas()

df_final_status.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Member_final_status_{date}.csv')

# COMMAND ----------

# DBTITLE 1,Save the Member Comparison results to a csv file
date = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
df_Member = spark.sql('SELECT * FROM tblM_MemberComparison_Results ORDER BY Member_ID')
df_Member_Pandas = df_Member.toPandas()

df_Member_Pandas.to_csv(f'/dbfs/mnt/{clientName}/Q360/Results/{destination_location}/Member_Comparison_{date}.csv')  


# COMMAND ----------

# DBTITLE 1,Notebook exit comment to get the status of notebook run
dbutils.notebook.exit("Success")
