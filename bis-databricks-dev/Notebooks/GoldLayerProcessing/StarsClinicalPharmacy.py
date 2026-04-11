# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigPath","","")

ClientCode = dbutils.widgets.get("ClientContainer")
SourceConfigPath = dbutils.widgets.get("ConfigPath")

MountPoint = "/mnt/"
FullConfigPath = MountPoint + SourceConfigPath

ClientCodeLower = ClientCode.lower()
ClientCodeUpper = ClientCode.upper()

print(ClientCode)
print(ClientCodeLower)
print(ClientCodeUpper)
print(SourceConfigPath)
print(FullConfigPath)

# COMMAND ----------

# DBTITLE 1,Loading Source Data
def mountSource():
  SourcePath = MountPoint + f"{ClientCodeLower}/consolidated/MA/Data/StarsClinicalPharmacy"
  Sourcedf = spark.read.format("delta").option("header","true").load(SourcePath)
  Sourcedf.createOrReplaceTempView("ConsolidatedStarsClinicalPharmacy")
  print(SourcePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Loading Destination Path
def mountDestination():
  DestinationPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Quality/StarsClinicalPharmacy"
  Destinationdf = spark.read.format("delta").option("header","true").load(DestinationPath)
  Destinationdf.createOrReplaceTempView("StarsClinicalPharmacy")
  print(DestinationPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Creating connection to ConfigDB
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
  blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
  blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
  blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="
else:
  envLetter = "p"
  envUser = "PRD"+envUser
  blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
jdbcDatabase = "Configuration_DB_"+ ClientCodeUpper
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
                "user" : jdbcUsername,
                "password" : jdbcPassword,
                "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
              }

# COMMAND ----------

# DBTITLE 1,Executing ConfigDB Query
def RunConfigFileQuery():
  ConfigSQLQuery = f"""
SELECT 
	 FileId
	,FileName
	,RegistrationDatetime
	,YearMonth
	,YearOfService
	,MonthOfService
FROM (
	SELECT 
		 FileId
		,FileName
		,RegistrationDatetime 
		,CASE
			WHEN SUBSTRING(FileName,40,4) + SUBSTRING(FileName,37,2)= CONCAT(YEAR(GETDATE()),'01') THEN CONCAT(YEAR(GETDATE())-1,'13')
			WHEN SUBSTRING(FileName,40,4) + SUBSTRING(FileName,37,2)= CONCAT(YEAR(GETDATE()),'02') THEN CONCAT(YEAR(GETDATE())-1,'14')
			ELSE SUBSTRING(FileName,40,4) + SUBSTRING(FileName,37,2) 
		 END YearMonth
		,SUBSTRING(filename,32,4) AS YearOfService
		,SUBSTRING(FileName,37,2)  AS MonthOfService
	FROM (
		SELECT 
			 FileId
			,FileName
			,RegistrationDatetime 
		FROM LatestFileWorkflowState 
		WHERE 
		FileLayoutID IN(
			SELECT FileLayoutID 
			FROM refFileLayout 
			WHERE 
			FileEntity = 'StarsClinicalPharmacy')
		AND
		WorkflowStateDescription = 'ConsolidationCompleted'
		) a
	WHERE
	FileName LIKE '%_Adherence_Denominator_%'
	UNION ALL
	SELECT 
		 FileId
		,FileName
		,RegistrationDatetime
		,CASE 
			WHEN SUBSTRING(FileName,35,4) + SUBSTRING(FileName,32,2) = CONCAT(YEAR(GETDATE()),'01') THEN CONCAT(YEAR(GETDATE())-1,'13')
			WHEN SUBSTRING(FileName,35,4) + SUBSTRING(FileName,32,2) = CONCAT(YEAR(GETDATE()),'02') THEN CONCAT(YEAR(GETDATE())-1,'14')
			ELSE SUBSTRING(FileName,35,4) + SUBSTRING(FileName,32,2) 
		 END YearMonth
		,SUBSTRING(FileName,27,4) AS YearOfService
		,SUBSTRING(FileName,32,2) AS MonthOfService
	FROM (
		SELECT 
			 FileId
			,FileName
			,RegistrationDatetime 
		FROM LatestFileWorkflowState 
		WHERE 
		FileLayoutID IN(
			SELECT FileLayoutID 
			FROM refFileLayout 
			WHERE 
			FileEntity = 'StarsClinicalPharmacy')
		AND
		WorkflowStateDescription = 'ConsolidationCompleted'
		) a
	WHERE
	FileName LIKE '%_SUPD_Denominator_%'
) a
WHERE
CASE
	WHEN YearOfService = CAST(YEAR(GETDATE()) AS VARCHAR(4)) AND MonthOfService IN ('03','04','05','06','07','08','09','10') THEN 1
	WHEN YearOfService = CAST(year(GETDATE()) - 1 AS VARCHAR(4)) AND MonthOfService in ('01','02','11','12') THEN 1
END = 1
"""

  pushdown_query = "(" + ConfigSQLQuery + ") a"
  ConfigDBFileDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  ConfigDBFileDF.createOrReplaceTempView("ConfigDBFiles")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Run StarsClinicalPharmacy Querry
def RunTempSQLScript():
  tempSQLScript="""
WITH StarsClinicalPharmacyAdherence AS(
SELECT 
   sa.ClientID
  ,sa.FileID
  ,sa.LoadDateTime
  ,sa.FileLayoutID
  ,sa.FileLayoutDescription
  ,sa.MBI
  ,sa.MemberID
  ,sa.DOB
  ,sa.Gender
  ,sa.LIS
  ,sa.EnrollmentStart
  ,sa.EnrollmentEnd
  ,sa.DualEligible
  ,sa.Disability
  ,sa.DaysInIPDiab
  ,sa.DaysInSNFDiab
  ,sa.DiabPDCDenominator
  ,sa.DiabPDCNumerator
  ,sa.DiabPDCRate
  ,sa.DiabPDCDenominatorUnadj
  ,sa.DiabPDCNumeratorUnadj
  ,sa.DiabPDCRateUnadj
  ,sa.DiabNumeratorflag
  ,sa.DaysInIPRAS
  ,sa.DaysInSNFRAS
  ,sa.RASPDCDenominator
  ,sa.RASPDCNumerator
  ,sa.RASPDCRate
  ,sa.RASPDCDenominatorUnadj
  ,sa.RASPDCNumeratorUnadj
  ,sa.RASPDCRateUnadj
  ,sa.RASNumeratorflag
  ,sa.DaysInIPStatin
  ,sa.DaysInSNFStatin
  ,sa.StatinPDCDenominator
  ,sa.StatinPDCNumerator
  ,sa.StatinPDCRate
  ,sa.StatinPDCDenominatorUnadj
  ,sa.StatinPDCNumeratorUnadj
  ,sa.StatinPDCRateUnadj
  ,sa.StatinNumeratorflag
  ,null AS SUPDNumeratorFlag
  ,sa.RunID
  ,cf.YearMonth
  ,ROW_NUMBER() OVER(PARTITION BY sa.MemberID,sa.DOB,sa.Gender,sa.FileLayoutDescription ORDER BY sa.EnrollmentStart DESC, sa.EnrollmentEnd DESC, sa.FileID DESC) AS RowNumber
FROM ConsolidatedStarsClinicalPharmacy sa
    LEFT JOIN ConfigDBFiles cf 
      ON sa.FileID = cf.FileID
WHERE
FileLayoutDescription = 'StarsClinicalPharmacyAdherence'
),
StarsClinicalPharmacySUPD AS(
SELECT 
  sp.ClientID
  ,sp.FileID
  ,sp.LoadDateTime
  ,sp.FileLayoutID
  ,sp.FileLayoutDescription
  ,sp.MBI
  ,sp.MemberID
  ,sp.DOB
  ,sp.Gender
  ,sp.LIS
  ,sp.EnrollmentStart
  ,sp.EnrollmentEnd
  ,null AS DualEligible
  ,null AS Disability
  ,null AS DaysInIPDiab
  ,null AS DaysInSNFDiab
  ,null AS DiabPDCDenominator
  ,null AS DiabPDCNumerator
  ,null AS DiabPDCRate
  ,null AS DiabPDCDenominatorUnadj
  ,null AS DiabPDCNumeratorUnadj
  ,null AS DiabPDCRateUnadj
  ,null AS DiabNumeratorflag
  ,null AS DaysInIPRAS
  ,null AS DaysInSNFRAS
  ,null AS RASPDCDenominator
  ,null AS RASPDCNumerator
  ,null AS RASPDCRate
  ,null AS RASPDCDenominatorUnadj
  ,null AS RASPDCNumeratorUnadj
  ,null AS RASPDCRateUnadj
  ,null AS RASNumeratorflag
  ,null AS DaysInIPStatin
  ,null AS DaysInSNFStatin
  ,null AS StatinPDCDenominator
  ,null AS StatinPDCNumerator
  ,null AS StatinPDCRate
  ,null AS StatinPDCDenominatorUnadj
  ,null AS StatinPDCNumeratorUnadj
  ,null AS StatinPDCRateUnadj
  ,null AS StatinNumeratorflag
  ,sp.SUPDNumeratorFlag
  ,sp.RunID
  ,cf.YearMonth
  ,ROW_NUMBER() OVER(PARTITION BY sp.MemberID,sp.DOB,sp.Gender,sp.FileLayoutDescription ORDER BY sp.EnrollmentStart DESC, sp.EnrollmentEnd DESC, sp.FileID DESC) AS RowNumber
FROM ConsolidatedStarsClinicalPharmacy sp
    LEFT JOIN ConfigDBFiles cf 
      ON sp.FileID = cf.FileID
WHERE
FileLayoutDescription = 'StarsClinicalPharmacySUPD'
),
StarsClinicalPharmacyFinal AS(
SELECT 
   ClientID
  ,FileID
  ,LoadDateTime
  ,FileLayoutID
  ,FileLayoutDescription
  ,MBI
  ,MemberID
  ,DOB
  ,Gender
  ,LIS
  ,EnrollmentStart
  ,EnrollmentEnd
  ,DualEligible
  ,Disability
  ,DaysInIPDiab
  ,DaysInSNFDiab
  ,DiabPDCDenominator
  ,DiabPDCNumerator
  ,DiabPDCRate
  ,DiabPDCDenominatorUnadj
  ,DiabPDCNumeratorUnadj
  ,DiabPDCRateUnadj
  ,DiabNumeratorflag
  ,DaysInIPRAS
  ,DaysInSNFRAS
  ,RASPDCDenominator
  ,RASPDCNumerator
  ,RASPDCRate
  ,RASPDCDenominatorUnadj
  ,RASPDCNumeratorUnadj
  ,RASPDCRateUnadj
  ,RASNumeratorflag
  ,DaysInIPStatin
  ,DaysInSNFStatin
  ,StatinPDCDenominator
  ,StatinPDCNumerator
  ,StatinPDCRate
  ,StatinPDCDenominatorUnadj
  ,StatinPDCNumeratorUnadj
  ,StatinPDCRateUnadj
  ,StatinNumeratorflag
  ,SUPDNumeratorFlag
  ,RunID
  ,YearMonth
FROM StarsClinicalPharmacySUPD
WHERE
RowNumber = 1
UNION ALL
SELECT 
   ClientID
  ,FileID
  ,LoadDateTime
  ,FileLayoutID
  ,FileLayoutDescription
  ,MBI
  ,MemberID
  ,DOB
  ,Gender
  ,LIS
  ,EnrollmentStart
  ,EnrollmentEnd
  ,DualEligible
  ,Disability
  ,DaysInIPDiab
  ,DaysInSNFDiab
  ,DiabPDCDenominator
  ,DiabPDCNumerator
  ,DiabPDCRate
  ,DiabPDCDenominatorUnadj
  ,DiabPDCNumeratorUnadj
  ,DiabPDCRateUnadj
  ,DiabNumeratorflag
  ,DaysInIPRAS
  ,DaysInSNFRAS
  ,RASPDCDenominator
  ,RASPDCNumerator
  ,RASPDCRate
  ,RASPDCDenominatorUnadj
  ,RASPDCNumeratorUnadj
  ,RASPDCRateUnadj
  ,RASNumeratorflag
  ,DaysInIPStatin
  ,DaysInSNFStatin
  ,StatinPDCDenominator
  ,StatinPDCNumerator
  ,StatinPDCRate
  ,StatinPDCDenominatorUnadj
  ,StatinPDCNumeratorUnadj
  ,StatinPDCRateUnadj
  ,StatinNumeratorflag
  ,SUPDNumeratorFlag
  ,RunID
  ,YearMonth
FROM StarsClinicalPharmacyAdherence
WHERE
RowNumber = 1
)
SELECT 
   ClientID
  ,FileID
  ,LoadDateTime
  ,FileLayoutID
  ,FileLayoutDescription
  ,MBI
  ,MemberID
  ,DOB
  ,Gender
  ,LIS
  ,EnrollmentStart
  ,EnrollmentEnd
  ,DualEligible
  ,Disability
  ,DaysInIPDiab
  ,DaysInSNFDiab
  ,DiabPDCDenominator
  ,DiabPDCNumerator
  ,DiabPDCRate
  ,DiabPDCDenominatorUnadj
  ,DiabPDCNumeratorUnadj
  ,DiabPDCRateUnadj
  ,DiabNumeratorflag
  ,DaysInIPRAS
  ,DaysInSNFRAS
  ,RASPDCDenominator
  ,RASPDCNumerator
  ,RASPDCRate
  ,RASPDCDenominatorUnadj
  ,RASPDCNumeratorUnadj
  ,RASPDCRateUnadj
  ,RASNumeratorflag
  ,DaysInIPStatin
  ,DaysInSNFStatin
  ,StatinPDCDenominator
  ,StatinPDCNumerator
  ,StatinPDCRate
  ,StatinPDCDenominatorUnadj
  ,StatinPDCNumeratorUnadj
  ,StatinPDCRateUnadj
  ,StatinNumeratorflag
  ,SUPDNumeratorFlag
  ,RunID
  ,YearMonth
FROM StarsClinicalPharmacyFinal
"""
  print("Running main sql query")
  dfData = spark.sql(tempSQLScript)
  dfData.createOrReplaceTempView("tempSQLScript")
  
  return "SUCCESS"

# COMMAND ----------

def RunDupCheck():
  print("Checking duplicates")
  checkVar = 0
  dupSQLScript="""
SELECT COUNT(1)
FROM (
  SELECT 
    FileLayoutDescription
    ,YearMonth
    ,MemberId
    ,DOB
    ,Gender
  FROM tempSQLScript
  GROUP BY
    FileLayoutDescription
    ,YearMonth
    ,MemberId
    ,DOB
    ,Gender
  HAVING COUNT(1) > 1
  ) a
"""

  checkVar = spark.sql(dupSQLScript).first()[0]
  
  print(f"Duplicates found: {str(checkVar)}")
  if(checkVar > 1):
    raise Exception('Duplicates Detected from BusinessKey')

  return "SUCCESS"

# COMMAND ----------

def Merge(): 
  print("Running merge script")
  mergeSQL = """
MERGE INTO StarsClinicalPharmacy t 
USING (
	SELECT 
     ClientID
    ,FileID
    ,LoadDateTime
    ,FileLayoutID
    ,FileLayoutDescription
    ,MBI
    ,MemberID
    ,DOB
    ,Gender
    ,LIS
    ,EnrollmentStart
    ,EnrollmentEnd
    ,DualEligible
    ,Disability
    ,DaysInIPDiab
    ,DaysInSNFDiab
    ,DiabPDCDenominator
    ,DiabPDCNumerator
    ,DiabPDCRate
    ,DiabPDCDenominatorUnadj
    ,DiabPDCNumeratorUnadj
    ,DiabPDCRateUnadj
    ,DiabNumeratorflag
    ,DaysInIPRAS
    ,DaysInSNFRAS
    ,RASPDCDenominator
    ,RASPDCNumerator
    ,RASPDCRate
    ,RASPDCDenominatorUnadj
    ,RASPDCNumeratorUnadj
    ,RASPDCRateUnadj
    ,RASNumeratorflag
    ,DaysInIPStatin
    ,DaysInSNFStatin
    ,StatinPDCDenominator
    ,StatinPDCNumerator
    ,StatinPDCRate
    ,StatinPDCDenominatorUnadj
    ,StatinPDCNumeratorUnadj
    ,StatinPDCRateUnadj
    ,StatinNumeratorflag
    ,SUPDNumeratorFlag
    ,RunID
    ,YearMonth
	FROM tempSQLScript 
) s 
    ON  t.FileLayoutDescription = s.FileLayoutDescription
    AND t.YearMonth = s.YearMonth
    AND t.MemberId = s.MemberId
    AND t.DOB = s.DOB
    AND t.Gender = s.Gender
WHEN NOT MATCHED THEN 
INSERT (
     ClientID
    ,FileID
    ,LoadDateTime
    ,FileLayoutID
    ,FileLayoutDescription
    ,MBI
    ,MemberID
    ,DOB
    ,Gender
    ,LIS
    ,EnrollmentStart
    ,EnrollmentEnd
    ,DualEligible
    ,Disability
    ,DaysInIPDiab
    ,DaysInSNFDiab
    ,DiabPDCDenominator
    ,DiabPDCNumerator
    ,DiabPDCRate
    ,DiabPDCDenominatorUnadj
    ,DiabPDCNumeratorUnadj
    ,DiabPDCRateUnadj
    ,DiabNumeratorflag
    ,DaysInIPRAS
    ,DaysInSNFRAS
    ,RASPDCDenominator
    ,RASPDCNumerator
    ,RASPDCRate
    ,RASPDCDenominatorUnadj
    ,RASPDCNumeratorUnadj
    ,RASPDCRateUnadj
    ,RASNumeratorflag
    ,DaysInIPStatin
    ,DaysInSNFStatin
    ,StatinPDCDenominator
    ,StatinPDCNumerator
    ,StatinPDCRate
    ,StatinPDCDenominatorUnadj
    ,StatinPDCNumeratorUnadj
    ,StatinPDCRateUnadj
    ,StatinNumeratorflag
    ,SUPDNumeratorFlag
    ,RunID
    ,YearMonth
) 
VALUES (
     s.ClientID
    ,s.FileID
    ,s.LoadDateTime
    ,s.FileLayoutID
    ,s.FileLayoutDescription
    ,s.MBI
    ,s.MemberID
    ,s.DOB
    ,s.Gender
    ,s.LIS
    ,s.EnrollmentStart
    ,s.EnrollmentEnd
    ,s.DualEligible
    ,s.Disability
    ,s.DaysInIPDiab
    ,s.DaysInSNFDiab
    ,s.DiabPDCDenominator
    ,s.DiabPDCNumerator
    ,s.DiabPDCRate
    ,s.DiabPDCDenominatorUnadj
    ,s.DiabPDCNumeratorUnadj
    ,s.DiabPDCRateUnadj
    ,s.DiabNumeratorflag
    ,s.DaysInIPRAS
    ,s.DaysInSNFRAS
    ,s.RASPDCDenominator
    ,s.RASPDCNumerator
    ,s.RASPDCRate
    ,s.RASPDCDenominatorUnadj
    ,s.RASPDCNumeratorUnadj
    ,s.RASPDCRateUnadj
    ,s.RASNumeratorflag
    ,s.DaysInIPStatin
    ,s.DaysInSNFStatin
    ,s.StatinPDCDenominator
    ,s.StatinPDCNumerator
    ,s.StatinPDCRate
    ,s.StatinPDCDenominatorUnadj
    ,s.StatinPDCNumeratorUnadj
    ,s.StatinPDCRateUnadj
    ,s.StatinNumeratorflag
    ,s.SUPDNumeratorFlag
    ,s.RunID
    ,s.YearMonth
)
"""

  spark.sql(mergeSQL)
  return "SUCCESS"

# COMMAND ----------

def RunStarsClinicalPharmacy(ClientCode):
  #Execute query against ConfigurationDB --creates a tempView called ConfigDB
  RunConfigFileQuery()
  #mount destination -- creates a tempView called StarsClinicalPharmacy
  mountDestination()
  #mount destination -- creates a tempView called ConsolidatedStarsClinicalPharmacy
  mountSource()
  #Execute tempSQLScript -- creates a tempView called tempSQLScript
  RunTempSQLScript()
  #Run duplicate processing check
  RunDupCheck()
  #run merge
  Merge()
  return "SUCCESS"

# COMMAND ----------

returnStr = ""
try:
  RunStarsClinicalPharmacy(ClientCode) 
  returnStr = "SUCCESS"
except Exception as e:
  returnStr += repr(e)
  returnStr = "FAILURE"
finally:
  dbutils.notebook.exit(returnStr)
