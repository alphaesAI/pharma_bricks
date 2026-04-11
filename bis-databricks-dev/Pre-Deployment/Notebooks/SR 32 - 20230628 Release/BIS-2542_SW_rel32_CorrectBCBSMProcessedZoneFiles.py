# Databricks notebook source
# MAGIC %md
# MAGIC ####This needs to be executed anytime (before or after) the create databricks job as there isn't a dependancy

# COMMAND ----------

# DBTITLE 1,ClientConfig
clientAppendJSON = """{
    "Environments": [
        {
            "EnvironmentLetter": "d",
            "Clients": [
                {
                    "ClientCode": "devidap1",
                    "Entity": "Member",
                    "DatalakePath": "/processed/MA/Data/Member/7.9/Member",
                    "DestlakePath": "/processed/MA/Data/Member/7.9/BcbsmMember"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "MemberEnrollment",
                    "DatalakePath": "/processed/MA/Data/MemberEnrollment/7.10/BcbsmEnrollment"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "Lab",
                    "DatalakePath": "/processed/MA/Data/Lab/7.10/BcbsmLab"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "Pharmacy",
                    "DatalakePath": "/processed/MA/Data/Pharmacy/7.9/BcbsmPharmacy"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "Product",
                    "DatalakePath": "/processed/MA/Data/Product/7.9/BcbsmProduct"
                }
            ]
        },
        {
            "EnvironmentLetter": "q",
            "Clients": [
                {
                    "ClientCode": "qaidap1",
                    "Entity": "Member",
                    "DatalakePath": "/processed/MA/Data/Member/7.9/Member",
                    "DestlakePath": "/processed/MA/Data/Member/7.9/BcbsmMember"
                },
                {
                    "ClientCode": "qaidap1",
                    "Entity": "MemberEnrollment",
                    "DatalakePath": "/processed/MA/Data/MemberEnrollment/7.10/BcbsmEnrollment"
                },
                {
                    "ClientCode": "qaidap1",
                    "Entity": "Lab",
                    "DatalakePath": "/processed/MA/Data/Lab/7.10/BcbsmLab"
                },
                {
                    "ClientCode": "qaidap1",
                    "Entity": "Pharmacy",
                    "DatalakePath": "/processed/MA/Data/Pharmacy/7.9/BcbsmPharmacy"
                },
                {
                    "ClientCode": "qaidap1",
                    "Entity": "Product",
                    "DatalakePath": "/processed/MA/Data/Product/7.9/BcbsmProduct"
                }
            ]
        },
        {
            "EnvironmentLetter": "s",
            "Clients": [
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Member",
                    "DestlakePath": "/processed/MA/Data/Member/7.9/BcbsmMember"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "MemberEnrollment",
                    "DatalakePath": "/processed/MA/Data/MemberEnrollment/7.10/BcbsmEnrollment"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Lab",
                    "DatalakePath": "/processed/MA/Data/Lab/7.10/BcbsmLab"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Pharmacy",
                    "DatalakePath": "/processed/MA/Data/Pharmacy/7.9/BcbsmPharmacy"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Product",
                    "DatalakePath": "/processed/MA/Data/Product/7.9/BcbsmProduct"
                }
            ]
        },
        {
            "EnvironmentLetter": "p",
            "Clients": [
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Member",
                    "DestlakePath": "/processed/MA/Data/Member/7.9/BcbsmMember"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "MemberEnrollment",
                    "DatalakePath": "/processed/MA/Data/MemberEnrollment/7.10/BcbsmEnrollment"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Lab",
                    "DatalakePath": "/processed/MA/Data/Lab/7.10/BcbsmLab"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Pharmacy",
                    "DatalakePath": "/processed/MA/Data/Pharmacy/7.9/BcbsmPharmacy"
                },
                {
                    "ClientCode": "bcbsm",
                    "Entity": "Product",
                    "DatalakePath": "/processed/MA/Data/Product/7.9/BcbsmProduct"
                }
            ]
        }
    ]
}
"""
# print(clientJSON)

# COMMAND ----------

def getEnvLetter():
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
  envLetter = ""  

  if(dbEnv == "934226345849410"):
    envLetter = "d" 
  elif(dbEnv == "5826678703751685"):
    envLetter = "q" 
  elif(dbEnv == "7093677384385470"):
    envLetter = "s" 
  else:
    envLetter = "p" 
    
  return envLetter

envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Clients and entities for Updating
from pyspark.sql.functions import explode, col

#Read the config file
# dfConfigFile = spark.read.format("json").option("multiline",True).load(clientJSON)
rddAppendJSON = sc.parallelize([clientAppendJSON]) 
dfAppendConfigFile = sqlContext.read.json(rddAppendJSON)
#Split out environments into column
dfAppendEnvironmentsConfigFile = dfAppendConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfAppendEnvironmentConfigFile = dfAppendEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfAppendClientsForEnvironment = dfAppendEnvironmentConfigFile.select(explode("Clients").alias("Clients")).select("Clients.ClientCode","Clients.Entity","Clients.DatalakePath","Clients.DestlakePath")

display(dfAppendClientsForEnvironment)
#dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Map BcbsmMember
def updateBCBSMMember(path, newPath):
  p = path
  np = newPath

  oldDf = spark.read.format("parquet").load(p)
  print("INFO: Checking if BcbsmMember needs updating")

  if 'HIC_NUM' in oldDf.columns:
    print("  INFO: Updating BcbsmMember")
    newDf = oldDf.withColumnRenamed('RAN_CTRC_NUM', 'MemberNumber')\
            .withColumnRenamed('HIC_NUM', 'HICNumber')\
            .withColumnRenamed('MCAD_ID', 'MedicaidID')\
            .withColumnRenamed('MEM_LST_NME', 'LastName')\
            .withColumnRenamed('MEM_FST_NME', 'FirstName')\
            .withColumnRenamed('MEM_MID_NME', 'MiddleInitial')\
            .withColumnRenamed('MEM_BRTH_DT_KEY', 'DateOfBirth')\
            .withColumnRenamed('MEM_GNDR_CD', 'Gender')\
            .withColumnRenamed('SUBS_ID', 'SubscriberID')\
            .withColumnRenamed('UNQ_ID', 'EnrolleeUniqueID')\
            .withColumnRenamed('PERM_ADR_LINE_1_TXT', 'PermanentAddressLine1')\
            .withColumnRenamed('PERM_ADR_LINE_2_TXT', 'PermanentAddressLine2')\
            .withColumnRenamed('PERM_CY_NME', 'PermanentCity')\
            .withColumnRenamed('PERM_STT_CD', 'PermanentState')\
            .withColumnRenamed('PERM_ZIP_CD', 'PermanentZipCode')\
            .withColumnRenamed('PERM_CNTY_NME', 'PermanentCounty')\
            .withColumnRenamed('MEM_HM_PH_NUM', 'TelephoneNumber')\
            .withColumnRenamed('MEM_EMAIL_ADR', 'Email')\
            .withColumnRenamed('MEM_FAX_PH_NUM', 'Fax')\
            .withColumnRenamed('MAIL_ADR_LINE_1_TXT', 'MailingAddressLine1')\
            .withColumnRenamed('MAIL_ADR_LINE_2_TXT', 'MailingAddressLine2')\
            .withColumnRenamed('MAIL_CY_NME', 'MailingCity')\
            .withColumnRenamed('MAIL_STT_CD', 'MailingState')\
            .withColumnRenamed('MAIL_ZIP_CD', 'MailingZipCode')\
            .withColumnRenamed('MAIL_CNTY_NME', 'MailingCounty')\
            .withColumnRenamed('CARTKR_FST_NME', 'CaretakerFirstName')\
            .withColumnRenamed('CARTKR_LST_NME', 'CareTakerLastName')\
            .withColumnRenamed('CARTKR_MID_NME', 'CareTakerMiddleInitial')\
            .withColumnRenamed('RACE_CD', 'Race')\
            .withColumnRenamed('RACE_DATA_SRC_CD', 'RaceDataSource')\
            .withColumnRenamed('ETHN_CD', 'Ethnicity')\
            .withColumnRenamed('ETHN_DATA_SRC_CD', 'EthnicityDatasource')\
            .withColumnRenamed('SPKN_LANG_CD', 'SpokenLanguage')\
            .withColumnRenamed('SPKN_LANG_SRC_CD', 'SpokenLanguageSource')\
            .withColumnRenamed('WTN_LANG_CD', 'WrittenLanguage')\
            .withColumnRenamed('WTN_LANG_SRC_CD', 'WrittenLanguageSource')\
            .withColumnRenamed('OTHR_LANG_CD', 'OtherLanguage')\
            .withColumnRenamed('OTHR_LANG_SRC_CD', 'OtherLanguageSource')\
            .withColumnRenamed('US_CITIZN_CD', 'USCitizen')\
            .withColumnRenamed('MEM_ALT_KEY_1', 'AlternateKey1')\
            .withColumnRenamed('MEM_ALT_KEY_2', 'AlternateKey2')\
            .withColumnRenamed('MEM_ALT_KEY_3', 'AlternateKey3')\
            .withColumnRenamed('MEM_ALT_KEY_4', 'AlternateKey4')\
            .withColumnRenamed('MEM_ALT_KEY_5', 'AlternateKey5')\
            .withColumnRenamed('MEM_ALT_KEY_6', 'AlternateKey6')\
            .withColumnRenamed('MEM_ALT_KEY_7', 'AlternateKey7')\
            .withColumnRenamed('MEM_ALT_KEY_8', 'AlternateKey8')\
            .withColumnRenamed('MEM_ALT_KEY_9', 'AlternateKey9')\
            .withColumnRenamed('MEM_ALT_KEY_10', 'AlternateKey10')

    print("  INFO: Writing BcbsmMember to Datalake")
    newDf.write.format("parquet").save(np)

    print("  INFO: Deleting Original Member from Datalake")
    dbutils.fs.rm(p, recurse=True)
  else:
    print("  INFO: BcbsmMember has previously been updated")

# COMMAND ----------

# DBTITLE 1,Map BcbsmEnrollment
def updateBCBSMEnrollment(path):
  p = path

  oldDf = spark.read.format("parquet").load(p)
  print("INFO: Checking if BcbsmEnrollment needs updating")

  if 'HIC_NUM' in oldDf.columns:
    print("  INFO: Updating BcbsmEnrollment")
    newDf = oldDf.withColumnRenamed('HIC_NUM', 'HICNUMBER')\
              .withColumnRenamed('NRLE_UNQ_ID', 'MEMBERNUMBER')\
              .withColumnRenamed('MCAD_ID', 'MEDICAIDID')\
              .withColumnRenamed('PLAN_ID', 'PLANID')\
              .withColumnRenamed('PDT_LINE_NME', 'PRODUCTLINE')\
              .withColumnRenamed('PDT_ID', 'PRODUCTID')\
              .withColumnRenamed('SUBS_PDT_ID', 'SECONDPRODUCTID')\
              .withColumnRenamed('SPAN_TYPE_CD', 'SPANTYPE')\
              .withColumnRenamed('SPAN_VAL_NUM', 'SPANVALUE')\
              .withColumnRenamed('EFF_DT_KEY', 'STARTDATE')\
              .withColumnRenamed('TRMN_DT_KEY', 'ENDDATE')\
              .withColumnRenamed('ADDL_SPAN_VAL_NUM', 'ADDITIONALSPANVALUE')\
              .withColumnRenamed('PBP_NUM', 'PBP')\
              .withColumnRenamed('ECDS_IND', 'ECDSFLAG')\
              .withColumnRenamed('ALPH_PFX_CD', 'ALPHAPREFIX')\
              .withColumnRenamed('RX_BNFT_IND', 'PHARMACY')\
              .withColumnRenamed('DEN_BNFT_IND', 'DENTAL')\
              .withColumnRenamed('VIS_BNFT_IND', 'VISION')\
              .withColumnRenamed('MH_BNFT_IND', 'MH')\
              .withColumnRenamed('MH_IPAT_BNFT_IND', 'MHIP')\
              .withColumnRenamed('MH_OPAT_BNFT_IND', 'MHDN')\
              .withColumnRenamed('MH_AMBL_BNFT_IND', 'MHAMB')\
              .withColumnRenamed('CHEM_DPCY_BNFT_IND', 'CD')\
              .withColumnRenamed('CHEM_DPCY_IPAT_BNFT_IND', 'CDIP')\
              .withColumnRenamed('CHEM_DPCY_INTNS_OPAT_BNFT_IND', 'CDDN')\
              .withColumnRenamed('CHEM_DPCY_AMBL_BNFT_IND', 'CDAMB')\
              .withColumnRenamed('HSPC_IND', 'HOSPICEFLAG')\
              .withColumnRenamed('SNP_NRL_IND', 'SNPFLAG')\
              .withColumnRenamed('SNP_NRL_TYPE_CD', 'SNPENROLLEETYPE')\
              .withColumnRenamed('ISUR_ID', 'ISSUERID')\
              .withColumnRenamed('MTL_LVL_CD', 'METALLEVEL')\
              .withColumnRenamed('CSHR_RDCT_VAR_CD', 'COSTSHARINGVARIANT')\
              .withColumnRenamed('MKT_CVG_CD', 'MARKETCOVERAGE')\
              .withColumnRenamed('CSHR_RDCT_ELGB_IND', 'CSRELIGIBILITYFLAG')\
              .withColumnRenamed('MEM_QHP_STT_CD', 'MEMBERENROLLMENTQHPSTATE')\
              .withColumnRenamed('LTRM_IST_IND', 'LONGTERMINSTITUTIONALFLAG')\
              .withColumnRenamed('ALT_MEM_1_ID', 'ALTERNATEMEMBERKEY1')\
              .withColumnRenamed('ALT_MEM_2_ID', 'ALTERNATEMEMBERKEY2')\
              .withColumnRenamed('ALT_MEM_3_ID', 'ALTERNATEMEMBERKEY3')\
              .withColumnRenamed('ALT_MEM_4_ID', 'ALTERNATEMEMBERKEY4')\
              .withColumnRenamed('ALT_MEM_5_ID', 'ALTERNATEMEMBERKEY5')\
              .withColumnRenamed('PLAN_EMP_IND', 'PLANEMPLOYEEFLAG')\
              .withColumnRenamed('MCAD_QHP_IND', 'MEDICAIDEXPANSIONQHPENROLLEE')

    print("  INFO: Writing BcbsmEnrollment to Datalake")
    newDf.write.format("parquet").mode("overwrite").save(p)
  else:
    print("  INFO: BcbsmEnrollment has previously been updated")

# COMMAND ----------

# DBTITLE 1,Map BcbsmLab
def updateBCBSMLab(path):
  p = path

  oldDf = spark.read.format("parquet").load(p)
  print("INFO: Checking if BcbsmLab needs updating")

  if 'UNQ_ID' in oldDf.columns:
    print("  INFO: Updating BcbsmLab")
    newDf = oldDf.withColumnRenamed('UNQ_ID', 'MemberNumber')\
                .withColumnRenamed('ORD_PHYN_ID', 'ProviderID')\
                .withColumnRenamed('CLM_ID', 'ClaimNumber')\
                .withColumnRenamed('SRVLN_NUM', 'ClaimLineNumber')\
                .withColumnRenamed('ORD_PHYN_NPI_ID', 'ProviderNPI')\
                .withColumnRenamed('LOC_ID', 'LocationID')\
                .withColumnRenamed('SERV_FR_DT_KEY', 'DOS')\
                .withColumnRenamed('PDT_ID', 'ProductID')\
                .withColumnRenamed('PROV_SPTY_CD', 'ProviderSpecialty')\
                .withColumnRenamed('CLM_STU_CD', 'ClaimStatus')\
                .withColumnRenamed('RD_PROV_ORG_NME', 'LabCode')\
                .withColumnRenamed('BILL_PROV_ID', 'BillingIden')\
                .withColumnRenamed('RD_PROV_ID', 'ClientNumber')\
                .withColumnRenamed('REF_PROV_ID', 'RefPCP')\
                .withColumnRenamed('RD_PROV_UPIN', 'UPIN')\
                .withColumnRenamed('PRIN_ICD_DGN_CD', 'Diagcode')\
                .withColumnRenamed('ORD_CD', 'OrderCode')\
                .withColumnRenamed('ORD_NME', 'OrderName')\
                .withColumnRenamed('PROC_CPT_CD', 'CPTCode')\
                .withColumnRenamed('PROC_HCPCS_CD', 'HCPCSCode')\
                .withColumnRenamed('PROC_MOD_CD', 'HCPCSModifier')\
                .withColumnRenamed('SNO_MED_CD', 'SNOMEDCode')\
                .withColumnRenamed('NAT_LAB_RSLT_CD', 'LOINCode')\
                .withColumnRenamed('NAT_LAB_RSLT1_CD', 'ResultCode')\
                .withColumnRenamed('NAT_LAB_RSLT_NME', 'ResultName')\
                .withColumnRenamed('LAB_RSLT_NUM', 'ResultValue')\
                .withColumnRenamed('LAB_RSLT_UNITS_TXT', 'ResultUnit')\
                .withColumnRenamed('LAB_RSLT_LOW_RNGE_NUM', 'RefRangeLow')\
                .withColumnRenamed('LAB_RSLT_HIGH_RNGE_NUM', 'RefRangeHigh')\
                .withColumnRenamed('LAB_RSLT_RNGE_TXT', 'RefRangeAlpha')\
                .withColumnRenamed('LAB_RSLT_CMT_TXT', 'Comments')\
                .withColumnRenamed('CLM_SRC_IND', 'ClaimSourceIndicator')\
                .withColumnRenamed('SERV_TO_DT_KEY', 'DateEnd')\
                .withColumnRenamed('SRC_SYS_CD', 'SourceName')

    print("  INFO: Writing BcbsmLab to Datalake")
    newDf.write.format("parquet").mode("overwrite").save(p)
  else:
    print("  INFO: BcbsmLab has previously been updated")

# COMMAND ----------

# DBTITLE 1,Map BcbsmPharmacy
def updateBCBSMPharmacy(path):
  p = path

  oldDf = spark.read.format("parquet").load(p)
  print("INFO: Checking if BcbsmPharmacy needs updating")

  if 'UNQ_ID' in oldDf.columns:
    print("  INFO: Updating BcbsmPharmacy")
    newDf = oldDf.withColumnRenamed('UNQ_ID', 'MemberNumber')\
                .withColumnRenamed('HIC_NUM', 'HICNBenID')\
                .withColumnRenamed('PROV_ID', 'ProviderID')\
                .withColumnRenamed('PROV_NPI', 'ProviderNPI')\
                .withColumnRenamed('CLM_ID', 'ClaimNumber')\
                .withColumnRenamed('PDT_ID', 'ProductID')\
                .withColumnRenamed('CHG_AMT', 'AmountCharged')\
                .withColumnRenamed('ALLOW_AMT', 'AmtEligible')\
                .withColumnRenamed('PAID_AMT', 'AmountPaid')\
                .withColumnRenamed('NDC', 'NDCCodeSTD')\
                .withColumnRenamed('PCH_DT', 'RxFillDate')\
                .withColumnRenamed('D_SPLY_CNT', 'RxDaysSupply')\
                .withColumnRenamed('RX_TYPE_CD', 'RxCodeType')\
                .withColumnRenamed('USC_CD', 'USCCode')\
                .withColumnRenamed('GEN_PDT_ID', 'GPI')\
                .withColumnRenamed('GEN_PDT_NME', 'GPIName')\
                .withColumnRenamed('QTY_DISP_CNT', 'Quantity')\
                .withColumnRenamed('QTY_UNIT', 'UnitsofMeasure')\
                .withColumnRenamed('PRSB_ID', 'PrescriberNumber')\
                .withColumnRenamed('PRSB_NPI', 'PrescriberID')\
                .withColumnRenamed('PRSB_DEA_NUM', 'DEANumber')\
                .withColumnRenamed('ADJ_TYPE_CD', 'ClaimStatus')\
                .withColumnRenamed('PAID_DT', 'AdjudicationDate')\
                .withColumnRenamed('DISP_FEE_AMT', 'DispensingFee')\
                .withColumnRenamed('COPAY_AMT', 'CoPay')\
                .withColumnRenamed('CINS_AMT', 'CoInsurance')\
                .withColumnRenamed('DED_AMT', 'Deductible')\
                .withColumnRenamed('DAW_CD', 'DispenseAsWritten')\
                .withColumnRenamed('MAIL_ORD_IND', 'MailOrder')\
                .withColumnRenamed('SALES_TAX_AMT', 'SalesTax')\
                .withColumnRenamed('PHRM_NPI', 'PharmacyNPI')\
                .withColumnRenamed('PRSC_NUM', 'PrescriptionReferenceNumber')\
                .withColumnRenamed('PLACE_CD', 'PlaceOfService')\
                .withColumnRenamed('SUPP_CLM_IND', 'SuppliesClaim')\
                .withColumnRenamed('CLM_SRC_CD', 'ClaimSourceIndicator')\
                .withColumnRenamed('ALT_KEY_1', 'AlternateKey1')\
                .withColumnRenamed('ALT_KEY_2', 'AlternateKey2')\
                .withColumnRenamed('PROV_SPTY_CD', 'ProviderSpecialty')\
                .withColumnRenamed('SRC_SYS_CD', 'SourceName')

    print("  INFO: Writing BcbsmPharmacy to Datalake")
    newDf.write.format("parquet").mode("overwrite").save(p)
  else:
    print("  INFO: BcbsmPharmacy has previously been updated")

# COMMAND ----------

# DBTITLE 1,Map BcbsmProduct
def updateBCBSMProduct(path):
  p = path

  oldDf = spark.read.format("parquet").load(p)
  print("INFO: Checking if BcbsmProduct needs updating")

  if 'PRODUCTID' in oldDf.columns:
    print("  INFO: Updating BcbsmProduct")
    newDf = oldDf.withColumnRenamed('PRODUCTID', 'ProductID')\
                .withColumnRenamed('PLANID', 'PlanID')\
                .withColumnRenamed('PRODUCTLINE', 'ProductLine')\
                .withColumnRenamed('PLANGRPID', 'PlanGroupID')\
                .withColumnRenamed('PLANGRPNAME', 'PlanGroupName')\
                .withColumnRenamed('PLANSUBGRP', 'PlanSubGroup')\
                .withColumnRenamed('PLANTYPE', 'PlanType')\
                .withColumnRenamed('PLANSUBTYPE', 'PlanSubType')\
                .withColumnRenamed('PLANBEGDT', 'StartDate')\
                .withColumnRenamed('PLANENDDT', 'EndDate')\
                .withColumnRenamed('PBPID', 'PBP')\
                .withColumnRenamed('ECDSFLAG', 'ECDSFlag')\
                .withColumnRenamed('PRODTYPE', 'ProductType')\
                .withColumnRenamed('MRKTCOVRG', 'MarketCoverage')\
                .withColumnRenamed('PLANMRKTNAME', 'PlanMarketingName')\
                .withColumnRenamed('NCQASUBMISSIONID', 'NCQASubmissionID')


    print("  INFO: Writing BcbsmProduct to Datalake")
    newDf.write.format("parquet").mode("overwrite").save(p)
  else:
    print("  INFO: BcbsmProduct has previously been updated")

# COMMAND ----------

# DBTITLE 1,Main
MountPoint = "/mnt/"

EntityAppCollect = dfAppendClientsForEnvironment.collect()

for ent in EntityAppCollect:
  clientCode = ent["ClientCode"]
  entity = ent["Entity"]
  dlPath = ent["DatalakePath"]
  destPath = ent["DestlakePath"]

  #use the below to pass into each function
  fullPath = f"{MountPoint}{clientCode}{dlPath}"
  fullDestPath = f"{MountPoint}{clientCode}{destPath}"
  
  #run updates for each entity
  try:
    if entity == "Member" and path_exists(fullDestPath) == True:
      print("INFO: Checking if BcbsmMember needs updating")
      print("  INFO: BcbsmMember has previously been updated")
    elif entity == "Member" and path_exists(fullDestPath) == False:
      updateBCBSMMember(fullPath, fullDestPath)
    elif entity == "MemberEnrollment":
      updateBCBSMEnrollment(fullPath)
    elif entity ==  "Lab":
      updateBCBSMLab(fullPath)
    elif entity ==  "Pharmacy":
      updateBCBSMPharmacy(fullPath)
    elif entity ==  "Product":
      updateBCBSMProduct(fullPath)

  except Exception as e:
    print(f"  ERROR: {str(e)}")
