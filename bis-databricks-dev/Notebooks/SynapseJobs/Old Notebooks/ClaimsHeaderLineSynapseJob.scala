// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer") 

// COMMAND ----------

// DBTITLE 1,Import libraries
import java.sql.DriverManager
import java.util.Properties

// COMMAND ----------

// DBTITLE 1,Call Synapse JSON Creator Class
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

// DBTITLE 1,Setup variables
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var clientFolder = ""
var envUser="_ETLUSER_SQL"
var blobKey = ""

if (dbEnv == "934226345849410") {envLetter = "d"; clientFolder = "devidap" ;envUser = "DEV"+envUser; blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {envLetter = "q"; clientFolder = "qaidap";envUser = "QA"+envUser; blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {envLetter = "s"; clientFolder = "bcbsks";envUser = "STG"+envUser; blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {envLetter = "p"; clientFolder = "bcbsks";envUser = "PRD"+envUser; blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="} 

Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
val jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
val jdbcPort = 1433
val jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val ClaimHeader = "/mnt/"+clientContainer+"/consolidated/MA/Data/MedicalClaimHeader/"
val ClaimLine = "/mnt/"+clientContainer+"/consolidated/MA/Data/MedicalClaimLine/"
val TempblobStorageAccount = "wasbs://stream-temp@svtss"+envLetter+"idap01s.blob.core.windows.net/temp"
val SparkBlobSetup = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"

// Create a Properties() object to hold the parameters.
val connectionProperties = new Properties()

connectionProperties.put("user", s"$jdbcUsername")      //s"${jdbcUsername}")
connectionProperties.put("password", s"$jdbcPassword")  //s"${jdbcPassword}")

val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
connectionProperties.setProperty("Driver", driverClass)

val jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase

//mounting blob using
spark.conf.set(SparkBlobSetup,blobKey)

val con = DriverManager.getConnection(jdbcUrl, connectionProperties)
val stmt = con.createStatement()

val tempMedicalClaimHeader =  clientContainer.concat(".MedicalClaimHeader")
val tempMedicalClaimLine = clientContainer.concat(".MedicalClaimLine")

// COMMAND ----------

// DBTITLE 1,Start building JSON
var rJSON = new synJSONCreator
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId.toString) 

// COMMAND ----------

// DBTITLE 1,Create empty dataframes
var headerRawData = spark.emptyDataFrame
var lineRawData = spark.emptyDataFrame
var rawData_CH = spark.emptyDataFrame
var rawData_CL = spark.emptyDataFrame

// COMMAND ----------

// DBTITLE 1,Create HeaderRawData and LineRawData DataFrame
try{
headerRawData = spark.read.format("delta").load(ClaimHeader)
lineRawData = spark.read.format("delta").load(ClaimLine)
}
catch{
      case e: Throwable =>  { 
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
            rJSON.addBraceEnd()
            dbutils.notebook.exit(rJSON.getJSON())
    }
}

// COMMAND ----------

// DBTITLE 1,Select from HeaderRawData DataFrame
try{
rawData_CH = headerRawData.selectExpr("GeneratedMedicalClaimsUniqueKey",
"ClientID",
"FileID",
"FileLayoutID",
"FileLayoutDescription", 
"LoadDateTime",                             
"ClaimNumber",
"OriginalClaimNumber",
"BeneficiaryID",
"PlanMemberID",
"CMSContractNumber",
"ClaimFormType",
"BillTypeCode",
"ClaimTypeInd",
"ClaimStatus",
"DetailServiceDate",
"ClaimEntryDate",
"ClaimProcessDate",
"ClaimReceivedDate",
"ClaimTotalChargeAmount",
"ClaimAllowedAmount",
"CheckDate",
"ClaimFinalizedDate",
"CoinsuranceAmt",
"DeductibleAmt",
"CopayAmt",
"OtherPrimaryPayerAllowedAmt",
"OtherHealthPlan",
"ClaimWeight",
"ClaimSource",
"AdmissionDate",
"ServiceFacilityNPI",
"ServiceFacilityID",
"ServiceFacilityLocation",
"ServiceFacilityAddress1",
"ServiceFacilityAddress2",
"ServiceFacilityCity",
"ServiceFacilityState",
"ServiceFacilityZip",
"ServiceFacilityCountry",
"RenderingProviderID",
"RenderingProviderNPI",
"RenderingProviderTIN",
"RenderingProviderSpecialtyCode",
"BillingProviderID",
"BillingProviderTIN",
"BillingProviderTaxonomy",
"BillingProviderAddress1",
"BillingProviderAddress2",
"BillingProviderCity",
"BillingProviderState",
"BillingProviderZip",
"BillingProviderCountry",
"AttendingProviderNPI",
"PlaceOfService",
"DischargeStatusCode",
"DischargeDate",
"MSDRG",
"MSDRG2",
"ICDVersion",
"PrimaryDiagCode",
"AdmitDiagCode",
"DiagCode2",
"DiagCode3",
"DiagCode4",
"DiagCode5",
"DiagCode6",
"DiagCode7",
"DiagCode8",
"DiagCode9",
"DiagCode10",
"DiagCode11",
"DiagCode12",
"DiagCode13",
"DiagCode14",
"DiagCode15",
"DiagCode16",
"DiagCode17",
"DiagCode18",
"DiagCode19",
"DiagCode20",
"DiagCode21",
"DiagCode22",
"DiagCode23",
"DiagCode24",
"DiagCode25",
"DiagCode26",
"DiagCode27",
"DiagCode28",
"DiagCode29",
"DiagCode30",
"DiagCode31",
"DiagCode32",
"DiagCode33",
"DiagCode34",
"DiagCode35",
"DiagCode36",
"DiagCode37",
"DiagCode38",
"AdmitPOA",
"PrimaryPOA",
"PrimaryProcCode",
"PrimaryProcCodeDate",
"ProcCode2",
"ProcCode2Date",
"ProcCode3",
"ProcCode3Date",
"ProcCode4",
"ProcCode4Date",
"ProcCode5",
"ProcCode5Date",
"ProcCode6",
"ProcCode6Date",
"ProcCode7",
"ProcCode7Date",
"ProcCode8",
"ProcCode8Date",
"ProcCode9",
"ProcCode9Date",
"ProcCode10",
"ProcCode10Date",
"ProcCode11",
"ProcCode11Date",
"ProcCode12",
"ProcCode12Date",
"ProcCode13",
"ProcCode13Date",
"ProcCode14",
"ProcCode14Date",
"ProcCode15",
"ProcCode15Date",
"ProcCode16",
"ProcCode16Date",
"ProcCode17",
"ProcCode17Date",
"ProcCode18",
"ProcCode18Date",
"ProcCode19",
"ProcCode19Date",
"ProcCode20",
"ProcCode20Date",
"ProcCode21",
"ProcCode21Date",
"ProcCode22",
"ProcCode22Date",
"ProcCode23",
"ProcCode23Date",
"ProcCode24",
"ProcCode24Date",
"ProcCode25",
"'' as ProcCode25Date",                 
"ProcCode26",
"'' as ProcCode26Date",                       
"ProcCode27",
"'' as ProcCode27Date",                      
"ProcCode28",
"'' as ProcCode28Date",                      
"ProcCode29",
"'' as ProcCode29Date",                      
"ProcCode30",
"'' as ProcCode30Date",                       
"ProcCode31",
"'' as ProcCode31Date",                       
"ProcCode32",
"'' as ProcCode32Date",                     
"ProcCode33",
"'' as ProcCode33Date",                         
"ProcCode34",
"'' as ProcCode34Date",                       
"ProcCode35",
"'' as ProcCode35Date",                   
"ProcCode36",
"'' as ProcCode36Date",                     
"ProcCode37",
"'' as ProcCode37Date",                        
"ProcCode38",
"'' as ProcCode38Date",                         
"OccurCode1",
"OccurCode2",
"OccurCode3",
"OccurCode4",
"OccurCode5",
"OccurCode6",
"OccurCode7",
"OccurCode8",
"OccurCode9",
"OccurCode10",
"OccurCode11",
"OccurCode12",
"OccurCode13",
"OccurCode14",
"OccurCode15",
"OccurCode16",
"OccurCode17",
"OccurCode18",
"OccurCode19",
"OccurCode20",
"OccurCode21",
"OccurCode22",
"OccurCode23",
"OccurCode24",
"StatementFromDate",
"StatementToDate",
"SCCFClaimIdentifier",
"UniquePersonKey",
"ProductID",
"CVX",
"DaysDenied",
"RoomBoard",
"RRUUnitsofService",
"MajorSurgery",
"LocationID",
"PCPIndicator",
"ClaimSourceInd",
"EyeExamResult",
"SourceName",
"AlternateClaimIdentifier1",
"PaidDate",
"PayStatus",
"IsDeniedDuplicate",
"IsSplitClaim")
}
catch{
      case e: Throwable =>  { 
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
            rJSON.addBraceEnd()
            dbutils.notebook.exit(rJSON.getJSON())
    }
}

// COMMAND ----------

// DBTITLE 1,Select from LineRawData DataFrame
try{
rawData_CL = lineRawData.select("GeneratedMedicalClaimsUniqueKey"
,"FileID"
,"LineNumber"
,"TypeOfService"
,"PlaceOfService"
,"StatusCode"
,"TotalChargeAmt"
,"AllowedAmt"
,"PurePaymentAmt"
,"InterestAmt"
,"CopayAmt"
,"DeductibleAmt"
,"OOPAmt"
,"CPTTypeService"
,"ServiceFromDate"
,"ServiceToDate"
,"ProcCodeOrig"
,"ProcMod1Orig"
,"ProcMod2Orig"
,"ProcMod3Orig"
,"ProcMod4Orig"
,"DiagCode1"
,"DiagCode2"
,"DiagCode3"
,"DiagCode4"
,"DiagCode5"
,"DiagCode6"
,"DiagCode7"
,"DiagCode8"
,"DiagCode9"
,"DiagCode10"
,"DiagCode11"
,"DiagCode12"
,"EmergencyInd"
,"RevenueCode"
,"NoncoveredChargesTotal"
,"ProcCode"
,"ProcCodeType"
,"ProcMod1"
,"ProcMod2"
,"ProcMod3"
,"ProcMod4"
,"ProcCode1"
,"ProcCode1Type"
,"ProcCode1Mod1"
,"CategoryNum"
,"MultiCategoryNum"
,"Classification"
,"ClassificationAddtnl"
,"EDIAdjustCodeList"
,"EventCode1"
,"EventCode2"
,"EventCode3"
,"EventCode4"
,"EventCode5"
,"EventCode6"
,"EventCode7"
,"EventCode8"
,"EventCode9"
,"EventCode10"
,"EventCode11"
,"EventCode12"
,"EventCode13"
,"EventCode14"
,"HIPAAAdjustReasonCode"
,"RemitAdviceCode"
,"AuthorizationNum"
,"AuthorizationOverride"
,"NDCCodeList"
,"EncounterFlag"
,"CEOverride"
,"CEAction"
,"CEEventCode"
,"CELineDisp"
,"EPSDT"
,"FamilyPlanInd"
,"TotalChargeAmtOrig"
,"AllowedAmtOrig"
,"ContractAllowedAmt"
,"Quantity"
,"UnitType"
,"UnitRate"
,"COBSavingsAmt"
,"COBPaidAmt"
,"DuplicateInd"
,"DuplicateOption"
,"GLCode"
,"GLDate"
,"Profile"
,"AdjustCode1"
,"AdjustCode2"
,"AdjustCode3"
,"AdjustCode4"
,"AdjustCode5"
,"AdjustCode6"
,"AdjustCode7"
,"AdjustCode8"
,"AdjustCode9"
,"AdjustCode10"
,"AdjustCode11"
,"AdjustCode12"
,"AdjustCode13"
,"AdjustCode14"
,"AdjustCode15"
,"AdjustCode16"
,"AdjustCode17"
,"AdjustCode18"
,"AdjustCode19"
,"AdjustCode20"
,"MemberObligationAmt"
,"OriginalLineNum"
,"PrimaryAllowedAmt"
,"PrimaryDeductAmt"
,"PrimaryCopayAmt"
,"PrimaryCoinsAmt"
,"PrimaryNoncoveredAmt"
,"PrimaryPaidAmt"
,"PrimaryMemberObligation"
,"PrimaryContractAdjstAmt"
,"PrimaryEOBCode"
,"PrimaryDiscount"
,"PricingScheduleCode"
,"WithholdAmt"
,"RebundleAmt"
,"Rider"
,"APCCode"
)
}
catch{
      case e: Throwable =>  { 
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
            rJSON.addBraceEnd()
            dbutils.notebook.exit(rJSON.getJSON())
    }
}

// COMMAND ----------

// DBTITLE 1,Truncate and Reload into MedicalClaimHeader and MedicalClaimLine
try {
      val sqlStatment = """ 
        TRUNCATE TABLE """ + tempMedicalClaimHeader + """
        TRUNCATE TABLE """ + tempMedicalClaimLine 

      stmt.execute(sqlStatment)
      con.close() //closing connection

      val writeQuery = rawData_CH.write
        .mode(SaveMode.Append)
        .format("com.databricks.spark.sqldw")
        .option("url", jdbcUrl)
        .option("user",jdbcUsername)
        .option("password",jdbcPassword)
        .option("tempDir", TempblobStorageAccount)
        .option("forwardSparkAzureStorageCredentials", "true")
        .option("dbTable", tempMedicalClaimHeader) 
        .save()

      val writeQuery2 = rawData_CL.write
        .mode(SaveMode.Append)
        .format("com.databricks.spark.sqldw")
        .option("url", jdbcUrl)
        .option("user",jdbcUsername)
        .option("password",jdbcPassword)
        .option("tempDir", TempblobStorageAccount)
        .option("forwardSparkAzureStorageCredentials", "true")
        .option("dbTable", tempMedicalClaimLine) 
        .save() 

       rJSON.addNewEntry("Status", "SUCCESS")
       rJSON.addNewEntry("ErrorMessage", "", false) 
}
catch{
      case e: Throwable =>  { 
            rJSON.addNewEntry("Status", "FAILURE")
            rJSON.addNewEntry("ErrorMessage", StringContext.processEscapes(e.getMessage.toString).filter(_ >= ' ').replace(doubleQuote,""), false)
    }
}
finally{
    rJSON.addBraceEnd()
    dbutils.notebook.exit(rJSON.getJSON())
}
