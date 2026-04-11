// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer") 

// COMMAND ----------

// DBTITLE 1,Setup Parameters and Variables
//Create environment variable to handle the database connection
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var envUser="_ETLUSER_SQL"
var clientFolder = ""
var blobKey = ""
//
if (dbEnv == "934226345849410") {envLetter = "d"; clientFolder = "devidap";envUser = "DEV"+envUser}
else if (dbEnv == "5826678703751685") {envLetter = "q"; clientFolder = "qaidap";envUser = "QA"+envUser}
else if (dbEnv == "7093677384385470") {envLetter = "s"; clientFolder = "bcbsks";envUser = "STG"+envUser}
else {envLetter = "p"; clientFolder = "bcbsks";envUser = "PRD"+envUser} 

if (dbEnv == "934226345849410") {blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="}

val jdbcUrl = "jdbc:sqlserver://sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net:1433;database=syn-c-"+envLetter+"-shrd-idap0000-01"
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val TempblobStorageAccount = "wasbs://stream-temp@svtss"+envLetter+"idap01s.blob.core.windows.net/temp"

// COMMAND ----------

// DBTITLE 1,Method to check path exists or not
def path_exists(path: String): Boolean =
{
  var stat = false
  try {
    dbutils.fs.ls(path)
    stat = true
      } 
    catch {
            case ex: java.io.FileNotFoundException => {
            println(s"File  not found")
            stat = false 
            }           
         }
  return stat
}

// COMMAND ----------

val GoldenClaimTbl = clientContainer.concat(".Vision837")
val newGoldenClaimTbl = clientContainer.concat(".Vision837_New")

// COMMAND ----------

def createNewGoldenClaimTable(): String =
{
    return s"""     
IF OBJECT_ID('$GoldenClaimTbl','U') IS NOT NULL
  DROP TABLE $GoldenClaimTbl;

CREATE TABLE $GoldenClaimTbl
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,
	DiagnosisCodesList varchar(128)  NULL,
	ServiceCode varchar(128)  NULL,
	DiagnosisCodeList varchar(128)  NULL,
	BillingProviderID varchar(128)  NULL,
	BillingProviderNPI varchar(128)  NULL,
	BillingProviderAddress1 varchar(128)  NULL,
	BillingProviderCity varchar(128)  NULL,
	BillingProviderState varchar(128)  NULL,
	BillingProviderZip varchar(128)  NULL,
	BillingProviderRef varchar(128)  NULL,
	RenderingProviderTaxonomy varchar(128)  NULL,
	RenderingProviderID varchar(128)  NULL,
	RenderingProviderNPI varchar(128)  NULL,
	ServicingProviderAddress1 varchar(128)  NULL,
	ServicingProviderAddress2 varchar(128)  NULL,
	ServicingProviderCity varchar(128)  NULL,
	ServicingProviderState varchar(128)  NULL,
	ServicingProviderZip varchar(128)  NULL,
	InsuredPayerName varchar(128)  NULL,
	InsuredID varchar(128)  NULL,
	ClaimNote varchar(128)  NULL,
	BatchControlNumber varchar(128)  NULL, 
	ClaimNum varchar(128)  NULL,
	ClaimUpdatedDate date  NULL,
	LineClaimNum varchar(128)  NULL,
	ClaimLineNum varchar(128)  NULL,
	TypeOfService varchar(128)  NULL,
	PlaceOfService varchar(128)  NULL,
	LineServiceFromDate date  NULL,
	LineServiceToDate date  NULL,
	GroupBase varchar(128)  NULL,
	PatientFirstName varchar(128)  NULL,
	PatientLastName varchar(128)  NULL,
	PatientMiddleName varchar(128)  NULL,
	PatientDateOfBirth date  NULL,
	PatientGender varchar(128)  NULL,
	PatientAddress1 varchar(128)  NULL,
	PatientAddress2 varchar(128)  NULL,
	PatientCity varchar(128)  NULL,
	PatientZip varchar(128)  NULL,
	PatientState varchar(128)  NULL,
	PatientRlseOfInfoInd varchar(128)  NULL,
	PatientAccountNum varchar(128)  NULL,
	PatientCondEmployment varchar(128)  NULL,
	PatientCondAutoAccident varchar(128)  NULL,
	PatientCondAutoAccidentState varchar(128)  NULL,
	PatientCondOtherAccident varchar(128)  NULL,
	PatientCurrentIllnessDate date  NULL,
	PatientSimilarIllnessDate date  NULL,
	PatientLastWorkedDate date  NULL,
	PatientReturnWorkDate date  NULL,
	BillingProviderAddressLine1 varchar(128)  NULL,
	PayToProviderCity varchar(128)  NULL,
	BillingProviderTypeCode varchar(128)  NULL,
	ITSAccessFeeAmount varchar(128)  NULL,
	ITSHomeHostInd varchar(128)  NULL,
	BeginningDateOfService date  NULL,
	DocCntlNum varchar(128)  NULL,
	SubscriberFirstName varchar(128)  NULL,
	SubscriberLastName varchar(128)  NULL,
	SubscriberMiddleName varchar(128)  NULL,
	SubscriberDateOfBirth date  NULL,
	SubscriberGender varchar(128)  NULL,
	SubscriberCompanyCode varchar(128)  NULL,
	SubscriberPatientRelCode varchar(128)  NULL,
	COBInd varchar(128)  NULL,
	SecSubscriberIDNum varchar(128)  NULL,
	SecSubscriberInsurPlanName varchar(128)  NULL,
	SecSubscriberInsurPlanID varchar(128)  NULL,
	SecSubscriberFirstName varchar(128)  NULL,
	SecSubscriberLastName varchar(128)  NULL,
	SecSubscriberMiddleName varchar(128)  NULL,
	SecSubscriberDateOfBirth date  NULL,
	SecSubscriberGender varchar(128)  NULL,
	SecSubscriberEmployer varchar(128)  NULL,
	SecSubscriberCOBInd varchar(128)  NULL,
	SecSubscriberPatientRelCode varchar(128)  NULL,
	TerSubscriberDateOfBirth date  NULL,
	TerSubscriberGender varchar(128)  NULL,
	RenderingProviderTypeCode varchar(128)  NULL,
	ReferringProviderAuthNum varchar(128)  NULL,
	AmbulatoryGroup varchar(128)  NULL,
	AcceptAssgnInd1 varchar(128)  NULL,
	ClaimSubmitterID varchar(128)  NULL,
	PhysicianSignature varchar(128)  NULL,
	ClaimICDVersionInd varchar(128)  NULL,
	AttendingProviderNPI varchar(128)  NULL,
	AttendingProviderLastName varchar(128)  NULL,
	AttendingProviderFirstName varchar(128)  NULL,
	AttendingProviderMiddleName varchar(128)  NULL,
	AttendingProviderNameSuffix varchar(128)  NULL,
	OperatingProviderNPI varchar(128)  NULL,
	OperatingProviderLastName varchar(128)  NULL,
	OperatingProviderFirstName varchar(128)  NULL,
	OperatingProviderMiddleName varchar(128)  NULL,
	OperatingProviderNameSuffix varchar(128)  NULL,
	OtherOperatingProviderNPI varchar(128)  NULL,
	OtherOperatingProviderLastName varchar(128)  NULL,
	OtherOperatingProviderFirstName varchar(128)  NULL,
	OtherOperatingProviderMiddleName varchar(128)  NULL,
	OtherOperatingProviderNameSuffix varchar(128)  NULL,
	LineProcCode varchar(128)  NULL,
	LineProcMod1 varchar(128)  NULL,
	LineProcMod2 varchar(128)  NULL,
	LineProcMod3 varchar(128)  NULL,
	LineProcMod4 varchar(128)  NULL,
	LineAuthorizationNum varchar(128)  NULL,
	LineNDCCodeList varchar(128)  NULL,
	LineQuantity varchar(128)  NULL,
	LineUnitType varchar(128)  NULL,
	LineDiagCode1 varchar(128)  NULL,
	LineDiagCode2 varchar(128)  NULL,
	LineDiagCode3 varchar(128)  NULL,
	LineDiagCode4 varchar(128)  NULL,
	LineDiagCode5 varchar(128)  NULL,
	LineDiagCode6 varchar(128)  NULL,
	LineDiagCode7 varchar(128)  NULL,
	LineDiagCode8 varchar(128)  NULL,
	LineDiagCode9 varchar(128)  NULL,
	LineDiagCode10 varchar(128)  NULL,
	LineDiagCode11 varchar(128)  NULL,
	LineDiagCode12 varchar(128) NULL
);
"""
  }

// COMMAND ----------

 def InsertIntoGoldenClaim(stageTableName: String): String =
 {    
    return s"""
    INSERT INTO $GoldenClaimTbl
    SELECT 
           LoadDateTime
          ,FileID
          ,ClientID
          ,FileLayoutID
          ,FileLayoutDescription
          ,DiagnosisCodesList
          ,ServiceCode
          ,DiagnosisCodeList
          ,BillingProviderID
          ,BillingProviderNPI
          ,BillingProviderAddress1
          ,BillingProviderCity
          ,BillingProviderState
          ,BillingProviderZip
          ,BillingProviderRef
          ,RenderingProviderTaxonomy
          ,RenderingProviderID
          ,RenderingProviderNPI
          ,ServicingProviderAddress1
          ,ServicingProviderAddress2
          ,ServicingProviderCity
          ,ServicingProviderState
          ,ServicingProviderZip
          ,InsuredPayerName
          ,InsuredID
          ,ClaimNote
          ,BatchControlNumber 
          ,ClaimNum
          ,ClaimUpdatedDate
          ,LineClaimNum
          ,ClaimLineNum
          ,TypeOfService
          ,PlaceOfService
          ,LineServiceFromDate
          ,LineServiceToDate
          ,GroupBase
          ,PatientFirstName
          ,PatientLastName
          ,PatientMiddleName
          ,PatientDateOfBirth
          ,PatientGender
          ,PatientAddress1
          ,PatientAddress2
          ,PatientCity
          ,PatientZip
          ,PatientState
          ,PatientRlseOfInfoInd
          ,PatientAccountNum
          ,PatientCondEmployment
          ,PatientCondAutoAccident
          ,PatientCondAutoAccidentState
          ,PatientCondOtherAccident
          ,PatientCurrentIllnessDate
          ,PatientSimilarIllnessDate
          ,PatientLastWorkedDate
          ,PatientReturnWorkDate
          ,BillingProviderAddressLine1
          ,PayToProviderCity
          ,BillingProviderTypeCode
          ,ITSAccessFeeAmount
          ,ITSHomeHostInd
          ,BeginningDateOfService
          ,DocCntlNum
          ,SubscriberFirstName
          ,SubscriberLastName
          ,SubscriberMiddleName
          ,SubscriberDateOfBirth
          ,SubscriberGender
          ,SubscriberCompanyCode
          ,SubscriberPatientRelCode
          ,COBInd
          ,SecSubscriberIDNum
          ,SecSubscriberInsurPlanName
          ,SecSubscriberInsurPlanID
          ,SecSubscriberFirstName
          ,SecSubscriberLastName
          ,SecSubscriberMiddleName
          ,SecSubscriberDateOfBirth
          ,SecSubscriberGender
          ,SecSubscriberEmployer
          ,SecSubscriberCOBInd
          ,SecSubscriberPatientRelCode
          ,TerSubscriberDateOfBirth
          ,TerSubscriberGender
          ,RenderingProviderTypeCode
          ,ReferringProviderAuthNum
          ,AmbulatoryGroup
          ,AcceptAssgnInd1
          ,ClaimSubmitterID
          ,PhysicianSignature
          ,ClaimICDVersionInd
          ,AttendingProviderNPI
          ,AttendingProviderLastName
          ,AttendingProviderFirstName
          ,AttendingProviderMiddleName
          ,AttendingProviderNameSuffix
          ,OperatingProviderNPI
          ,OperatingProviderLastName
          ,OperatingProviderFirstName
          ,OperatingProviderMiddleName
          ,OperatingProviderNameSuffix
          ,OtherOperatingProviderNPI
          ,OtherOperatingProviderLastName
          ,OtherOperatingProviderFirstName
          ,OtherOperatingProviderMiddleName
          ,OtherOperatingProviderNameSuffix
          ,LineProcCode
          ,LineProcMod1
          ,LineProcMod2
          ,LineProcMod3
          ,LineProcMod4
          ,LineAuthorizationNum
          ,LineNDCCodeList
          ,LineQuantity
          ,LineUnitType
          ,LineDiagCode1
          ,LineDiagCode2
          ,LineDiagCode3
          ,LineDiagCode4
          ,LineDiagCode5
          ,LineDiagCode6
          ,LineDiagCode7
          ,LineDiagCode8
          ,LineDiagCode9
          ,LineDiagCode10
          ,LineDiagCode11
          ,LineDiagCode12
    FROM $stageTableName;
    """
  } 
    

// COMMAND ----------

// DBTITLE 1,Start Streaming to Publish Data From Delta into Synapse
import org.apache.spark.sql.streaming.Trigger
import com.databricks.spark.sqldw._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._
import org.apache.spark.sql.Column

//val destTable = clientContainer.concat(".Vision837")

spark.conf.set("fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net", blobKey)

val processedPath = "/mnt/"+clientContainer+"/processed/MA/Data/Vision/837"

val pathExists = path_exists(processedPath)

if(pathExists == true)
{
  //Read the table as a stream source 
  var rawDf = spark.read.format("delta").load(processedPath)
  
  // select only FCF columns and meta data
  var fcfColumns = rawDf.select(rawDf.columns.filter(x => (x.equals("LOAD_DATETIME")                                                     
                                                           || x.equals("FILE_ID")
                                                           || x.equals("CLIENT_ID")
                                                           || x.equals("FILE_LAYOUT_ID")
                                                           || x.equals("FILE_LAYOUT_DESCRIPTION")
                                                           || x.equals("DIAGNOSIS_CODES_LIST")
                                                           || x.equals("SERVICE_CODE")
                                                           || x.equals("DIAGNOSIS_CODE_LIST")
                                                           || x.equals("BILL_PROVIDER_ID")
                                                           || x.equals("BILL_PROVIDER_NPI_ID")
                                                           || x.equals("BILL_PROVIDER_ADD1")
                                                           || x.equals("BILL_PROVIDER_CITY")
                                                           || x.equals("BILL_PROVIDER_STATE")
                                                           || x.equals("BILL_PROVIDER_ZIP")
                                                           || x.equals("BILL_PROVIDER_REF")
                                                           || x.equals("REN_PROVIDER_TAXONOMY")
                                                           || x.equals("REN_PROVIDER_ID")
                                                           || x.equals("REN_PROVIDER_NPI_ID")
                                                           || x.equals("SERVICE_PROV_ADD1")
                                                           || x.equals("SERVICE_PROV_ADD2")
                                                           || x.equals("SERVICE_PROV_CITY")
                                                           || x.equals("SERVICE_PROV_STATE")
                                                           || x.equals("SERVICE_PROV_ZIP")
                                                           || x.equals("INSURED_PAYER_NAME")
                                                           || x.equals("INSURED_ID")
                                                           || x.equals("CLAIM_NOTE")
                                                           || x.equals("BATCH_CONTROL_NUMBER")                                           
                                                           || x.startsWith("MA_"))).map(rawDf(_)) : _*)
 
  
  //Renamed columns to match model in synapse
  var processedDf = fcfColumns
    .withColumnRenamed("LOAD_DATETIME", "LoadDateTime")
    .withColumnRenamed("FILE_ID", "FileID")
    .withColumnRenamed("CLIENT_ID", "ClientID")
    .withColumnRenamed("FILE_LAYOUT_ID", "FileLayoutID")
    .withColumnRenamed("FILE_LAYOUT_DESCRIPTION", "FileLayoutDescription")
    // Additional Columns
    .withColumnRenamed("DIAGNOSIS_CODES_LIST", "DiagnosisCodesList")
    .withColumnRenamed("SERVICE_CODE", "ServiceCode") //date
    .withColumnRenamed("DIAGNOSIS_CODE_LIST", "DiagnosisCodeList")
    .withColumnRenamed("BILL_PROVIDER_ID", "BillingProviderID")
    .withColumnRenamed("BILL_PROVIDER_NPI_ID", "BillingProviderNPI")
    .withColumnRenamed("BILL_PROVIDER_ADD1", "BillingProviderAddress1")
    .withColumnRenamed("BILL_PROVIDER_CITY", "BillingProviderCity") //date
    .withColumnRenamed("BILL_PROVIDER_STATE", "BillingProviderState") //date
    .withColumnRenamed("BILL_PROVIDER_ZIP", "BillingProviderZip")
    .withColumnRenamed("BILL_PROVIDER_REF", "BillingProviderRef")
    .withColumnRenamed("REN_PROVIDER_TAXONOMY", "RenderingProviderTaxonomy")
    .withColumnRenamed("REN_PROVIDER_ID", "RenderingProviderID")
    .withColumnRenamed("REN_PROVIDER_NPI_ID", "RenderingProviderNPI") //date
    .withColumnRenamed("SERVICE_PROV_ADD1", "ServicingProviderAddress1")
    .withColumnRenamed("SERVICE_PROV_ADD2", "ServicingProviderAddress2")
    .withColumnRenamed("SERVICE_PROV_CITY", "ServicingProviderCity")
    .withColumnRenamed("SERVICE_PROV_STATE", "ServicingProviderState")
    .withColumnRenamed("SERVICE_PROV_ZIP", "ServicingProviderZip")
    .withColumnRenamed("INSURED_PAYER_NAME", "InsuredPayerName")
    .withColumnRenamed("INSURED_ID", "InsuredID")
    .withColumnRenamed("CLAIM_NOTE", "ClaimNote")
    .withColumnRenamed("BATCH_CONTROL_NUMBER", "BatchControlNumber")
    // FCF columns
    .withColumnRenamed("MA_CLAIM_NUM", "ClaimNum")
    .withColumnRenamed("MA_CLAIM_UPDATED_DT", "ClaimUpdatedDate") //date
    .withColumnRenamed("MA_LINE_CLAIM_NUM", "LineClaimNum")
    .withColumnRenamed("MA_CLAIM_LINE_NUM", "ClaimLineNum")
    .withColumnRenamed("MA_TYPE_OF_SERVICE", "TypeOfService")
    .withColumnRenamed("MA_PLACE_OF_SERVICE", "PlaceOfService")
    .withColumnRenamed("MA_LINE_SERVICE_FROM_DT", "LineServiceFromDate") //date
    .withColumnRenamed("MA_LINE_SERVICE_TO_DT", "LineServiceToDate") //date
    .withColumnRenamed("MA_GROUP_BASE", "GroupBase")
    .withColumnRenamed("MA_PATIENT_FIRST_NAME", "PatientFirstName")
    .withColumnRenamed("MA_PATIENT_LAST_NAME", "PatientLastName")
    .withColumnRenamed("MA_PATIENT_MIDDLE_NAME", "PatientMiddleName")
    .withColumnRenamed("MA_PATIENT_DOB", "PatientDateOfBirth") //date
    .withColumnRenamed("MA_PATIENT_GENDER", "PatientGender")
    .withColumnRenamed("MA_PATIENT_ADDR1", "PatientAddress1")
    .withColumnRenamed("MA_PATIENT_ADDR2", "PatientAddress2")
    .withColumnRenamed("MA_PATIENT_CITY", "PatientCity")
    .withColumnRenamed("MA_PATIENT_ZIPCODE", "PatientZip")
    .withColumnRenamed("MA_PATIENT_STATE", "PatientState")
    .withColumnRenamed("MA_PATIENT_RLSE_OF_INFO_IND", "PatientRlseOfInfoInd")
    .withColumnRenamed("MA_PATIENT_ACCOUNT_NUM", "PatientAccountNum")
    .withColumnRenamed("MA_PATIENT_COND_EMPLOYMENT", "PatientCondEmployment")
    .withColumnRenamed("MA_PATIENT_COND_AUTO_ACCIDENT", "PatientCondAutoAccident")
    .withColumnRenamed("MA_PATIENT_COND_AUTO_ACCDNT_ST", "PatientCondAutoAccidentState") 
    .withColumnRenamed("MA_PATIENT_COND_OTHER_ACCIDENT", "PatientCondOtherAccident")
    .withColumnRenamed("MA_PATIENT_CURRENT_ILLNESS_DT", "PatientCurrentIllnessDate") //date
    .withColumnRenamed("MA_PATIENT_SIMILAR_ILLNESS_DT", "PatientSimilarIllnessDate") //date
    .withColumnRenamed("MA_PATIENT_LAST_WORKED_DT", "PatientLastWorkedDate") //date
    .withColumnRenamed("MA_PATIENT_RETURN_WORK_DT", "PatientReturnWorkDate") //date
    .withColumnRenamed("MA_BILL_PROV_ADDRESS_LINE_1", "BillingProviderAddressLine1")
    .withColumnRenamed("MA_BILL_PROV_CITY", "PayToProviderCity")
    .withColumnRenamed("MA_BILL_PROV_TYPE_CODE", "BillingProviderTypeCode")
    .withColumnRenamed("MA_ITS_ACCESS_FEE_AMT", "ITSAccessFeeAmount")
    .withColumnRenamed("MA_ITS_HOME_HOST_IND", "ITSHomeHostInd")
    .withColumnRenamed("MA_BEGINNING_DOS", "BeginningDateOfService") //date
    .withColumnRenamed("MA_DOC_CNTL_NUM", "DocCntlNum")
    .withColumnRenamed("MA_SUBCRIBER_FIRST_NAME", "SubscriberFirstName")
    .withColumnRenamed("MA_SUBCRIBER_LAST_NAME", "SubscriberLastName")
    .withColumnRenamed("MA_SUBCRIBER_MIDDLE_NAME", "SubscriberMiddleName")
    .withColumnRenamed("MA_SUBCRIBER_BIRTH_DATE", "SubscriberDateOfBirth") //date
    .withColumnRenamed("MA_SUBCRIBER_GENDER", "SubscriberGender")
    .withColumnRenamed("MA_SUBCRIBER_COMPANY_CD", "SubscriberCompanyCode")  
    .withColumnRenamed("MA_SUBCRIBER_PATIENT_RELCODE", "SubscriberPatientRelCode")
    .withColumnRenamed("MA_COB_IND", "COBInd")
    .withColumnRenamed("MA_SEC_SBSCRBR_ID_NUM", "SecSubscriberIDNum")
    .withColumnRenamed("MA_SEC_SBSCRBR_INSUR_PLAN_NAME", "SecSubscriberInsurPlanName")
    .withColumnRenamed("MA_SEC_SBSCRBR_INSUR_PLAN_ID", "SecSubscriberInsurPlanID")
    .withColumnRenamed("MA_SEC_SBSCRBR_FIRST_NAME", "SecSubscriberFirstName")
    .withColumnRenamed("MA_SEC_SBSCRBR_LAST_NAME", "SecSubscriberLastName")
    .withColumnRenamed("MA_SEC_SBSCRBR_MIDDLE_NAME", "SecSubscriberMiddleName")
    .withColumnRenamed("MA_SEC_SBSCRBR_BIRTH_DATE", "SecSubscriberDateOfBirth") //date
    .withColumnRenamed("MA_SEC_SBSCRBR_GENDER", "SecSubscriberGender")
    .withColumnRenamed("MA_SEC_SBSCRBR_EMPLOYER", "SecSubscriberEmployer")
    .withColumnRenamed("MA_SEC_SBSCRBR_COB_IND", "SecSubscriberCOBInd")
    .withColumnRenamed("MA_SEC_SBSCRBR_PATIENT_RELCODE", "SecSubscriberPatientRelCode")
    .withColumnRenamed("MA_TER_SBSCRBR_BIRTH_DATE", "TerSubscriberDateOfBirth") //date
    .withColumnRenamed("MA_TER_SBSCRBR_GENDER", "TerSubscriberGender")
    .withColumnRenamed("MA_RNDR_PROV_TYPE_CODE", "RenderingProviderTypeCode") 
    .withColumnRenamed("MA_RFRG_PROV_AUTH_NUM", "ReferringProviderAuthNum")
    .withColumnRenamed("MA_AMBULATORY_GROUP", "AmbulatoryGroup") 
    .withColumnRenamed("MA_ACCEPT_ASSGN_IND1", "AcceptAssgnInd1")
    .withColumnRenamed("MA_CLAIM_SUBMITTER_ID", "ClaimSubmitterID")
    .withColumnRenamed("MA_PHYSICIAN_SIGNATURE", "PhysicianSignature")
    .withColumnRenamed("MA_CLAIM_ICD_VERSION_IND", "ClaimICDVersionInd")
    .withColumnRenamed("MA_ATTND_PROV_NPI", "AttendingProviderNPI")
    .withColumnRenamed("MA_ATTND_PROV_LAST_NAME", "AttendingProviderLastName")
    .withColumnRenamed("MA_ATTND_PROV_FIRST_NAME", "AttendingProviderFirstName")
    .withColumnRenamed("MA_ATTND_PROV_MIDDLE_NAME", "AttendingProviderMiddleName")
    .withColumnRenamed("MA_ATTND_PROV_NAME_SUFFIX", "AttendingProviderNameSuffix")
    .withColumnRenamed("MA_OPER_PROV_NPI", "OperatingProviderNPI")
    .withColumnRenamed("MA_OPER_PROV_LAST_NAME", "OperatingProviderLastName")
    .withColumnRenamed("MA_OPER_PROV_FIRST_NAME", "OperatingProviderFirstName")
    .withColumnRenamed("MA_OPER_PROV_MIDDLE_NAME", "OperatingProviderMiddleName")
    .withColumnRenamed("MA_OPER_PROV_NAME_SUFFIX", "OperatingProviderNameSuffix")
    .withColumnRenamed("MA_OTH_OPER_PROV_NPI", "OtherOperatingProviderNPI")
    .withColumnRenamed("MA_OTH_OPER_PROV_LAST_NAME", "OtherOperatingProviderLastName")
    .withColumnRenamed("MA_OTH_OPER_PROV_FIRST_NAME", "OtherOperatingProviderFirstName")
    .withColumnRenamed("MA_OTH_OPER_PROV_MIDDLE_NAME", "OtherOperatingProviderMiddleName")
    .withColumnRenamed("MA_OTH_OPER_PROV_NAME_SUFFIX", "OtherOperatingProviderNameSuffix") 
    .withColumnRenamed("MA_LINE_PROC_CD", "LineProcCode")
    .withColumnRenamed("MA_LINE_PROC_MOD1", "LineProcMod1")
    .withColumnRenamed("MA_LINE_PROC_MOD2", "LineProcMod2")
    .withColumnRenamed("MA_LINE_PROC_MOD3", "LineProcMod3")
    .withColumnRenamed("MA_LINE_PROC_MOD4", "LineProcMod4")
    .withColumnRenamed("MA_LINE_AUTHORIZATION_NUM", "LineAuthorizationNum")
    .withColumnRenamed("MA_LINE_NDC_CD_LIST", "LineNDCCodeList")
    .withColumnRenamed("MA_LINE_QUANTITY", "LineQuantity")
    .withColumnRenamed("MA_LINE_UNIT_TYPE", "LineUnitType") 
    .withColumnRenamed("MA_LINE_DIAG_CD1", "LineDiagCode1")
    .withColumnRenamed("MA_LINE_DIAG_CD2", "LineDiagCode2")
    .withColumnRenamed("MA_LINE_DIAG_CD3", "LineDiagCode3")
    .withColumnRenamed("MA_LINE_DIAG_CD4", "LineDiagCode4")
    .withColumnRenamed("MA_LINE_DIAG_CD5", "LineDiagCode5")
    .withColumnRenamed("MA_LINE_DIAG_CD6", "LineDiagCode6")
    .withColumnRenamed("MA_LINE_DIAG_CD7", "LineDiagCode7")
    .withColumnRenamed("MA_LINE_DIAG_CD8", "LineDiagCode8")
    .withColumnRenamed("MA_LINE_DIAG_CD9", "LineDiagCode9")
    .withColumnRenamed("MA_LINE_DIAG_CD10", "LineDiagCode10")
    .withColumnRenamed("MA_LINE_DIAG_CD11", "LineDiagCode11")
    .withColumnRenamed("MA_LINE_DIAG_CD12", "LineDiagCode12")
    // date format
    .withColumn("ClaimUpdatedDate", to_date($"ClaimUpdatedDate", "yyyy-MM-dd"))
    .withColumn("LineServiceFromDate", to_date($"LineServiceFromDate", "yyyy-MM-dd"))
    .withColumn("LineServiceToDate", to_date($"LineServiceToDate", "yyyy-MM-dd")) 
    .withColumn("PatientDateOfBirth", to_date($"PatientDateOfBirth", "yyyy-MM-dd")) 
    .withColumn("PatientCurrentIllnessDate", to_date($"PatientCurrentIllnessDate", "yyyy-MM-dd"))
    .withColumn("PatientSimilarIllnessDate", to_date($"PatientSimilarIllnessDate", "yyyy-MM-dd"))
    .withColumn("PatientLastWorkedDate", to_date($"PatientLastWorkedDate", "yyyy-MM-dd"))
    .withColumn("PatientReturnWorkDate", to_date($"PatientReturnWorkDate", "yyyy-MM-dd"))
    .withColumn("BeginningDateOfService", to_date($"BeginningDateOfService", "yyyy-MM-dd"))
    .withColumn("SubscriberDateOfBirth", to_date($"SubscriberDateOfBirth", "yyyy-MM-dd"))
    .withColumn("SecSubscriberDateOfBirth", to_date($"SecSubscriberDateOfBirth", "yyyy-MM-dd"))
    .withColumn("TerSubscriberDateOfBirth", to_date($"TerSubscriberDateOfBirth", "yyyy-MM-dd"))
 
processedDf.write
  .format("com.databricks.spark.sqldw")
  .option("url", jdbcUrl)
  .option("user",jdbcUsername)
  .option("password",jdbcPassword) 
  .option("tempDir", TempblobStorageAccount)
  .option("forwardSparkAzureStorageCredentials", "true")
  .option("dbTable", newGoldenClaimTbl)
  .option("postActions",  createNewGoldenClaimTable() + InsertIntoGoldenClaim(newGoldenClaimTbl) + s"DROP TABLE $newGoldenClaimTbl") 
  .save()
}
