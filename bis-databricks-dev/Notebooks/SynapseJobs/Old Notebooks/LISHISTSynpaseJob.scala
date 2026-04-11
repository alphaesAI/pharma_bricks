// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","") //"devidap1"
val clientContainer = dbutils.widgets.get("ClientContainer") 

// COMMAND ----------

// DBTITLE 1,Import libraries
import com.databricks.spark.sqldw._
import java.sql.DriverManager
import java.time.LocalDateTime 
import java.time.format.DateTimeFormatter
import java.util.Calendar
import java.util.Properties
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Call Synapse JSON Creator Class
// MAGIC %run "../CommonMethods/ABC/SynJSONCreatorClass"

// COMMAND ----------

val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var clientFolder = ""
var envUser="_ETLUSER_SQL"
var blobKey = ""
if (dbEnv == "934226345849410") {envLetter = "d"; clientFolder = "devidap";envUser = "DEV"+envUser}
else if (dbEnv == "5826678703751685") {envLetter = "q"; clientFolder = "qaidap";envUser = "QA"+envUser}
else if (dbEnv == "7093677384385470") {envLetter = "s"; clientFolder = "bcbsks";envUser = "STG"+envUser}
else {envLetter = "p"; clientFolder = "bcbsks";envUser = "PRD"+envUser} 

Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
val jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
val jdbcPort = 1433
val jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val SourceFolder = "/mnt/"+clientContainer+"/consolidated/MA/Data/LISHIST"
val TempblobStorageAccount = "wasbs://stream-temp@svtss"+envLetter+"idap01s.blob.core.windows.net/temp"
val SparkBlobSetup = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"

if (dbEnv == "934226345849410") {blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="}

val jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase

// Create a Properties() object to hold the parameters.
val connectionProperties = new Properties()

connectionProperties.put("user", s"$jdbcUsername")      //s"${jdbcUsername}")
connectionProperties.put("password", s"$jdbcPassword")  //s"${jdbcPassword}")

val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
connectionProperties.setProperty("Driver", driverClass)

//mounting blob using
spark.conf.set(SparkBlobSetup,blobKey)

// COMMAND ----------

// DBTITLE 1,Identify Synapse Tables
val tempLishistTbl = clientContainer.concat(".CMS_LISHIST_temp")
val newLishistTbl = clientContainer.concat(".CMS_LISHIST_New")
val lishistTbl = clientContainer.concat(".CMS_LISHIST")
val oldLishistTbl = clientContainer.concat(".CMS_LISHIST_Old")

// COMMAND ----------

val connection = DriverManager.getConnection(jdbcUrl, jdbcUsername, jdbcPassword)
val stmt = connection.createStatement()
val sql = s"""
IF OBJECT_ID('$tempLishistTbl','U') IS NOT NULL DROP TABLE $tempLishistTbl
"""
stmt.execute(sql)
connection.close()

// COMMAND ----------

def createCMS_LISHIST_New(): String =
  {    
    return s"""  
IF OBJECT_ID('$newLishistTbl','U') IS NOT NULL
DROP TABLE $newLishistTbl;

create table $newLishistTbl
(
	[LoadDateTime] datetime2(7) NOT NULL, 
	[FileID]       bigint  NOT NULL,
	[ClientID]  varchar(20)  NOT NULL,
	[FileLayoutID]       integer  NOT NULL,
	[FileLayoutDescription]  varchar(255)  NOT NULL,
	[RecordType] varchar(1) NOT NULL,
	[MCOContractNumber] varchar(5) NOT NULL ,
	[PBPNumber]       varchar(3)  NOT NULL,
	[BeneficiaryID]  varchar(12)  NOT NULL,
	[Surname] varchar(12)  NOT NULL,
	[FirstName]        varchar(7)  NOT NULL,
	[MiddleInitial] varchar(1)  NULL,
	[Sex]                varchar(1)  NULL,
	[DateOfBirth]          integer  NULL,
	[LowIncomePeriodStartDate]  integer  NULL,
	[LowIncomePeriodEndDate]  integer  NULL,
	[LIPSPercentage]       varchar(3)  NULL,
	[PremiumLISAmount] decimal(7,2)  NULL,
	[LowIncomeCoPayLevelID]  integer  NOT NULL ,
	[BeneficiarySourceofSubsidyCode] varchar(1)  NULL,
	[LISActivityFlag]	varchar(1) NULL,
	[PBPStartDate]   integer  NULL,
	[NetPartDPremiumAmount]  decimal(7,2)  NULL,
	[ContractYear]       integer  NULL,
	[InstitutionalStatusIndicator]       integer  NULL,
	[PBPEnrollmentTerminationDate]         integer  NULL,
	[Filler]             varchar(56)  NULL
) ;"""
  }

// COMMAND ----------

 def InsertIntoCMS_LISHIST(stageTableName: String): String =
  {    
    return s"""
insert into $newLishistTbl SELECT 
        isnull(LOADDATETIME,Getdate()) LOADDATETIME,
FileID,
ClientID,
FileLayoutID,
FileLayoutDescription,
RecordType ,
MCOContractNumber  ,
PBPNumber        ,
BeneficiaryID   ,
Surname  ,
FirstName         ,
MiddleInitial  ,
Sex                 ,
case when DateOfBirth='' then null else DateOfBirth end  DateOfBirth,
case when LowIncomePeriodStartDate ='' then null else LowIncomePeriodStartDate end LowIncomePeriodStartDate,
case when LowIncomePeriodEndDate='' then null else LowIncomePeriodEndDate end LowIncomePeriodEndDate ,
LIPSPercentage        ,
case when PremiumLISAmount='' then null else PremiumLISAmount end PremiumLISAmount ,
case when LowIncomeCoPayLevelID ='' then null else LowIncomeCoPayLevelID end LowIncomeCoPayLevelID ,
BeneficiarySourceofSubsidyCode  ,
LISActivityFlag	,
case when PBPStartDate='' then null else  PBPStartDate end PBPStartDate,
case when NetPartDPremiumAmount='' then null else NetPartDPremiumAmount end NetPartDPremiumAmount ,
case when ContractYear='' then null else ContractYear end ContractYear,
case when InstitutionalStatusIndicator='' then null else InstitutionalStatusIndicator end InstitutionalStatusIndicator,
case when PBPEnrollmentTerminationDate='' then null else PBPEnrollmentTerminationDate end PBPEnrollmentTerminationDate,
Filler      
 FROM $stageTableName; """ 
  }

// COMMAND ----------

def RenameTables(): String =
  {    
    return s"""
RENAME OBJECT $lishistTbl TO [CMS_LISHIST_Old];
RENAME OBJECT $newLishistTbl TO [CMS_LISHIST];
DROP TABLE $oldLishistTbl;
"""
  }

// COMMAND ----------

def dropobjects(): String = 
{
  return s"""
IF OBJECT_ID('$tempLishistTbl','U') IS NOT NULL
DROP TABLE $tempLishistTbl;
  """
}

// COMMAND ----------

// DBTITLE 1,Execute Method
def executeSave(df: DataFrame) = {
  df.write
    .format("com.databricks.spark.sqldw")
    .option("url", jdbcUrl)
    .option("user",jdbcUsername)
    .option("password",jdbcPassword)
    //.option("preActions", dropobjects())
    .option("tempDir", TempblobStorageAccount)
    .option("forwardSparkAzureStorageCredentials", "true")
    .option("dbTable", tempLishistTbl)
    .option("postActions", createCMS_LISHIST_New() + InsertIntoCMS_LISHIST(tempLishistTbl) + s"DROP TABLE $tempLishistTbl" + RenameTables() )
    .save()
}

// COMMAND ----------

var rJSON = new synJSONCreator
var ErrorMessage = ""
val doubleQuote = """ " """.trim()

//Get notebook context -- to get RunId and JobId
val ctx = dbutils.notebook.getContext 
val currentJobId = ctx.tags("jobId") //not there when you dont run it from the dbutils command

rJSON.addBraceStart()
rJSON.addNewEntry("CurrentJobId", currentJobId)

try{
  var fmt = DateTimeFormatter.ofPattern("yMdHms")
  val folderDate = LocalDateTime.now().format(fmt).toString

  val rawData = spark.read.format("delta").load(SourceFolder)
  
  val rawData_LH = rawData.select("FILEID",
                                "FILELAYOUTID",
                                "FILELAYOUTDESCRIPTION",
                                "CLIENTID",
								"LOADDATETIME",
                                "RecordType",
                                "MCOContractNumber",
                                "PBPNumber",
                                "BeneficiaryID",
                                "Surname",
                                "FirstName",
                                "MiddleInitial",
                                "Sex",
                                "DateOfBirth",
                                "LowIncomePeriodStartDate",
                                "LowIncomePeriodEndDate",
                                "LIPSPercentage",
                                "PremiumLISAmount",
                                "LowIncomeCoPayLevelID",
                                "BeneficiarySourceofSubsidyCode",
                                "LISActivityFlag",
                                "PBPStartDate",
                                "NetPartDPremiumAmount",
                                "ContractYear",
                                "InstitutionalStatusIndicator",
                                "PBPEnrollmentTerminationDate",
                                "Filler")

  val result =  executeSave(rawData_LH)

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
