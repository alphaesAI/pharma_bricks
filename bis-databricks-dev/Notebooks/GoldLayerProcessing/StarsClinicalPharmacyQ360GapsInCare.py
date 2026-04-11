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
  SourcePath = MountPoint + f"{ClientCodeLower}/Gold/MA/Quality/StarsClinicalPharmacy"
  SourcePathdf = spark.read.format("delta").option("header","true").load(SourcePath)
  SourcePathdf.createOrReplaceTempView("StarsClinicalPharmacy")
  print(SourcePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Loading Destination Path
def mountDestination():
  DestinationPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Quality/Q360GapsInCare"
  Destinationdf = spark.read.format("delta").option("header","true").load(DestinationPath)
  Destinationdf.createOrReplaceTempView("Q360GapsInCare")
  print(DestinationPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Loading Crosswalk Data
def mountLookUp():
  LookUpPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Client/MemberPersonBridge"
  LookUpPathdf = spark.read.format("delta").option("header","true").load(LookUpPath)
  LookUpPathdf.createOrReplaceTempView("MemberPersonBridge")
  print(LookUpPath)
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
	,FileLayoutID
FROM (
	SELECT 
		 FileId
		,FileName
		,RegistrationDatetime
		,FileLayoutID
	FROM LatestFileWorkflowState 
	where 
	Workflowstatedescription = 'ConsolidationCompleted'
	and FileLayoutID IN(
		SELECT FileLayoutID 
		FROM refFileLayout 
		WHERE 
		FileEntity = 'StarsClinicalPharmacy'
	)
) t
WHERE 
FileName LIKE '%_Adherence_Denominator_%'
UNION ALL
SELECT 
	 FileId
	,FileName
	,RegistrationDatetime
	,FileLayoutID
FROM (
	SELECT 
		 FileId
		,FileName
		,RegistrationDatetime
		,FileLayoutID
	FROM LatestFileWorkflowState 
	where 
	Workflowstatedescription = 'ConsolidationCompleted'
	and FileLayoutID IN(
		SELECT FileLayoutID 
		FROM refFileLayout 
		WHERE 
		FileEntity = 'StarsClinicalPharmacy'
	)
) t
WHERE 
FileName LIKE '%_SUPD_Denominator_%'
"""

  pushdown_query = "(" + ConfigSQLQuery + ") a"
  ConfigDBFileDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  ConfigDBFileDF.createOrReplaceTempView("ConfigDBFiles")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Run StarsClinicalPharmacy-Q360GapsinCare Querry
def RunTempSQLScript():
  tempSQLScript="""
with 
Members AS (
SELECT DISTINCT
   COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
  ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
  ,COALESCE(nullif(lmpb.UniquePersonKey,'None'),nullif(lmpb.PlanMemberID,'None')) AS LatestMemberID
FROM MemberPersonBridge mpb --current member
  LEFT JOIN MemberPersonBridge ompb --Original Member
      ON ompb.BISInternalPersonId = mpb.BISInternalPersonId
      AND ompb.IsOriginalMemberId = 1
  LEFT JOIN MemberPersonBridge lmpb --latest member
      ON lmpb.BISInternalPersonId = mpb.BISInternalPersonId
      AND lmpb.IsCurrent = 1
)
,SRCYM as ( 
Select 
Max(YearMonth) Max_YearMonth_Key,
FileLayoutID 
from StarsClinicalPharmacy
group by FileLayoutID
)
,LatestYM as (
select
FileLayoutID,
Max_YearMonth_Key
from SRCYM
)
,SRCData as (
select 
 distinct
 cf.FileName
,coalesce(M.OriginalMemberID,srcp.MemberID) as MemberID
,srcp.YearMonth
,srcp.DiabNumeratorFlag
,srcp.DIABPDCRate
,srcp.RASNumeratorFlag
,srcp.RASPDCRate
,srcp.StatinNumeratorFlag
,srcp.StatinPDCRate
,srcp.SUPDNumeratorFlag
,srcp.FileLayoutDescription
,srcp.FileLayoutID
,srcp.FileID
,srcp.RunID
from StarsClinicalPharmacy srcp
inner join LatestYM lym on srcp.YearMonth=lym.Max_YearMonth_Key 
                          and lym.FileLayoutID=srcp.FileLayoutID
inner join ConfigDBFiles cf on cf.fileid=srcp.fileid
left join Members M on M.MemberID=srcp.MemberID
)
,DiabetesMedicationAdherence as (
select
 YearMonth
,null as ClaimsThroughDate
,MemberID
,Case when DiabNumeratorFlag in (0,1) then 'MA-D' end as MeasureCode
,Case when DiabNumeratorFlag in (0,1) then 'Diabetes Medication Adherence' end as MeasureName
,Case
  when DiabNumeratorFlag  = 1 then 1
  when DiabNumeratorFlag  = 0 then 0
  end as numercnt
,Case when DiabNumeratorFlag  in (0,1) then 1 end as DenomCnt
,null as SubmeasureCode
,null as SubmeasureName
,null as EventName
,null as DateofService
,null as Claimnumber
,null as ProviderID
,null as ProviderName
,null as ExpectedRate
,null as ServiceNeededByDate
,case when DiabNumeratorFlag in (0,1) then DIABPDCRate end as PDC
,null as HBTest
,null as LastHBVal
,null as LastHBDate
,null as LastBPDia
,null as LastBPSys
,null as LastBPDate
,null as Category
,FileLayoutDescription as Source
,FileName as DataLoadName
,'Acumen' as DataFileName
,FileID
,RunID
,getdate() as LoadDateTime
from SRCData
where FileLayoutDescription like '%Adherence%' and DiabNumeratorFlag in (0,1)
)
, HypertensionMedicationAdherence as (
select
 YearMonth
,null as ClaimsThroughDate
,MemberID
,Case when RASNumeratorFlag in (0,1) then 'MA-H' end as MeasureCode
,Case when RASNumeratorFlag in (0,1) then 'Hypertension Medication Adherence' end as MeasureName
,Case
  when RASNumeratorFlag  = 1 then 1
  when RASNumeratorFlag  = 0 then 0
  end as numercnt
,Case when RASNumeratorFlag  in (0,1) then 1 end as DenomCnt
,null as SubmeasureCode
,null as SubmeasureName
,null as EventName
,null as DateofService
,null as Claimnumber
,null as ProviderID
,null as ProviderName
,null as ExpectedRate
,null as ServiceNeededByDate
,case when RASNumeratorFlag in (0,1) then RASPDCRate end as PDC
,null as HBTest
,null as LastHBVal
,null as LastHBDate
,null as LastBPDia
,null as LastBPSys
,null as LastBPDate
,null as Category
,FileLayoutDescription as Source
,FileName as DataLoadName
,'Acumen' as DataFileName
,FileID
,RunID
,getdate() as LoadDateTime
from SRCData
where FileLayoutDescription like '%Adherence%' and RASNumeratorFlag in (0,1)
)
,CholesterolMedicationAdherence as (
select
 YearMonth
,null as ClaimsThroughDate
,MemberID
,Case when StatinNumeratorFlag in (0,1) then 'MA-C' end as MeasureCode
,Case when StatinNumeratorFlag in (0,1) then 'Cholesterol Medication Adherence' end as MeasureName
,Case
  when StatinNumeratorFlag  = 1 then 1
  when StatinNumeratorFlag  = 0 then 0
  end as numercnt
,Case when StatinNumeratorFlag  in (0,1) then 1 end as DenomCnt
,null as SubmeasureCode
,null as SubmeasureName
,null as EventName
,null as DateofService
,null as Claimnumber
,null as ProviderID
,null as ProviderName
,null as ExpectedRate
,null as ServiceNeededByDate
,case when StatinNumeratorFlag in (0,1) then StatinPDCRate end as PDC
,null as HBTest
,null as LastHBVal
,null as LastHBDate
,null as LastBPDia
,null as LastBPSys
,null as LastBPDate
,null as Category
,FileLayoutDescription as Source
,FileName as DataLoadName
,'Acumen' as DataFileName
,FileID
,RunID
,getdate() as LoadDateTime
from SRCData
where FileLayoutDescription like '%Adherence%' and StatinNumeratorFlag in (0,1)
)
,SUPD as (
select
 YearMonth
,null as ClaimsThroughDate
,MemberID
,Case when SUPDNumeratorFlag in (0,1) then 'SUPD' end as MeasureCode
,Case when SUPDNumeratorFlag in (0,1) then 'Statin Use in Persons with Diabetes' end as MeasureName
,Case
  when SUPDNumeratorFlag  = 1 then 1
  when SUPDNumeratorFlag  = 0 then 0
  end as numercnt
,Case when SUPDNumeratorFlag  in (0,1) then 1 end as DenomCnt
,null as SubmeasureCode
,null as SubmeasureName
,null as EventName
,null as DateofService
,null as Claimnumber
,null as ProviderID
,null as ProviderName
,null as ExpectedRate
,null as ServiceNeededByDate
,case when SUPDNumeratorFlag in (0,1) then '' end as PDC
,null as HBTest
,null as LastHBVal
,null as LastHBDate
,null as LastBPDia
,null as LastBPSys
,null as LastBPDate
,null as Category
,FileLayoutDescription as Source
,FileName as DataLoadName
,'AcumenSUPD' as DataFileName
,FileID
,RunID
,getdate() as LoadDateTime
from SRCData
where FileLayoutDescription like '%SUPD%' and SUPDNumeratorFlag in (0,1)
)
,final as (
select
YearMonth
,ClaimsThroughDate
,MemberID
,MeasureCode
,MeasureName
,Numercnt
,DenomCnt
,SubmeasureCode
,SubmeasureName
,EventName
,DateofService
,Claimnumber
,ProviderID
,ProviderName
,ExpectedRate
,ServiceNeededByDate
,PDC
,HBTest
,LastHBVal
,LastHBDate
,LastBPDia
,LastBPSys
,LastBPDate
,Category
,Source
,DataLoadName
,DataFileName
,FileID
,RunID
,LoadDateTime
from DiabetesMedicationAdherence
union all
select
YearMonth
,ClaimsThroughDate
,MemberID
,MeasureCode
,MeasureName
,Numercnt
,DenomCnt
,SubmeasureCode
,SubmeasureName
,EventName
,DateofService
,Claimnumber
,ProviderID
,ProviderName
,ExpectedRate
,ServiceNeededByDate
,PDC
,HBTest
,LastHBVal
,LastHBDate
,LastBPDia
,LastBPSys
,LastBPDate
,Category
,Source
,DataLoadName
,DataFileName
,FileID
,RunID
,LoadDateTime
from HypertensionMedicationAdherence
union all
select
YearMonth
,ClaimsThroughDate
,MemberID
,MeasureCode
,MeasureName
,Numercnt
,DenomCnt
,SubmeasureCode
,SubmeasureName
,EventName
,DateofService
,Claimnumber
,ProviderID
,ProviderName
,ExpectedRate
,ServiceNeededByDate
,PDC
,HBTest
,LastHBVal
,LastHBDate
,LastBPDia
,LastBPSys
,LastBPDate
,Category
,Source
,DataLoadName
,DataFileName
,FileID
,RunID
,LoadDateTime
from CholesterolMedicationAdherence
union all
select
YearMonth
,ClaimsThroughDate
,MemberID
,MeasureCode
,MeasureName
,Numercnt
,DenomCnt
,SubmeasureCode
,SubmeasureName
,EventName
,DateofService
,Claimnumber
,ProviderID
,ProviderName
,ExpectedRate
,ServiceNeededByDate
,PDC
,HBTest
,LastHBVal
,LastHBDate
,LastBPDia
,LastBPSys
,LastBPDate
,Category
,Source
,DataLoadName
,DataFileName
,FileID
,RunID
,LoadDateTime
from SUPD
)
select
YearMonth
,ClaimsThroughDate
,MemberID
,MeasureCode
,MeasureName
,Numercnt
,DenomCnt
,SubmeasureCode
,SubmeasureName
,EventName
,DateofService
,Claimnumber
,ProviderID
,ProviderName
,ExpectedRate
,ServiceNeededByDate
,PDC
,HBTest
,LastHBVal
,LastHBDate
,LastBPDia
,LastBPSys
,LastBPDate
,Category
,Source
,DataLoadName
,DataFileName
,FileID
,RunID
,LoadDateTime
from final
order by MemberID,MeasureCode
"""
  print("Running main sql query")
  dfData = spark.sql(tempSQLScript)
  dfData.createOrReplaceTempView("tempSQLScript")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Deletes data based on YearMonth check
def RunDeleteSQLQuery():
  DeleteSQLQuery="""
DELETE FROM Q360GapsInCare
WHERE
Source in ('StarsClinicalPharmacyAdherence','StarsClinicalPharmacySUPD')
AND
YearMonth in (select
Max_YearMonth_Key
from (
  Select 
Max(YearMonth) Max_YearMonth_Key
from StarsClinicalPharmacy
      )
    )
"""
  print("Running delete sql query")
  dfData = spark.sql(DeleteSQLQuery)
  dfData.createOrReplaceTempView("DeleteSQLQuery")
  
  return "SUCCESS"

# COMMAND ----------

def Merge(): 
  print("Running merge script")
  mergeSQL = """
MERGE INTO Q360GapsInCare t 
USING (
	SELECT 
	 YearMonth
	,ClaimsThroughDate
	,MemberID
	,MeasureCode
	,MeasureName
	,NumerCnt
	,DenomCnt
	,SubmeasureCode
	,SubmeasureName
	,EventName
	,DateofService
	,Claimnumber
	,ProviderID
	,ProviderName
	,ExpectedRate
	,ServiceNeededByDate
	,PDC
	,HBTest
	,LastHBVal
	,LastHBDate
	,LastBPDia
	,LastBPSys
	,LastBPDate
	,Category
	,Source
	,DataLoadName
	,DataFileName
	,FileID
	,RunID
	,LoadDateTime
	FROM tempSQLScript
) s 
    ON  t.YearMonth = s.YearMonth
    AND t.RunID = s.RunID
WHEN NOT MATCHED THEN 
INSERT (
	 YearMonth
	,ClaimsThroughDate
	,MemberID
	,MeasureCode
	,MeasureName
	,NumerCnt
	,DenomCnt
	,SubmeasureCode
	,SubmeasureName
	,EventName
	,DateofService
	,Claimnumber
	,ProviderID
	,ProviderName
	,ExpectedRate
	,ServiceNeededByDate
	,PDC
	,HBTest
	,LastHBVal
	,LastHBDate
	,LastBPDia
	,LastBPSys
	,LastBPDate
	,Category
	,Source
	,DataLoadName
	,DataFileName
	,FileID
	,RunID
	,LoadDateTime
) 
VALUES (
	 s.YearMonth
	,s.ClaimsThroughDate
	,s.MemberID
	,s.MeasureCode
	,s.MeasureName
	,s.NumerCnt
	,s.DenomCnt
	,s.SubmeasureCode
	,s.SubmeasureName
	,s.EventName
	,s.DateofService
	,s.Claimnumber
	,s.ProviderID
	,s.ProviderName
	,s.ExpectedRate
	,s.ServiceNeededByDate
	,s.PDC
	,s.HBTest
	,s.LastHBVal
	,s.LastHBDate
	,s.LastBPDia
	,s.LastBPSys
	,s.LastBPDate
	,s.Category
	,s.Source
	,s.DataLoadName
	,s.DataFileName
	,s.FileID
	,s.RunID
	,s.LoadDateTime
)
"""

  spark.sql(mergeSQL)
  return "SUCCESS"

# COMMAND ----------

def RunStarsClinicalPharmacyQ360GIC(ClientCode):
  #Execute query against ConfigurationDB --creates a tempView called ConfigDB
  RunConfigFileQuery()
  #mount destination -- creates a tempView called Q360GapsInCare
  mountDestination()
  #mount source -- creates a tempView called StarsClinicalPharmacy
  mountSource()
  #mount lookup -- creates a tempView called MemberPersonBridge
  mountLookUp()
  #Execute tempSQLScript -- creates a tempView called tempSQLScript
  RunTempSQLScript()
  #run delete script -- deletes the existing yearmonth based on condition
  RunDeleteSQLQuery()
  #run merge
  Merge()
  return "SUCCESS"

# COMMAND ----------

returnStr = ""
try:
  RunStarsClinicalPharmacyQ360GIC(ClientCode) 
  returnStr = "SUCCESS"
except Exception as e:
  returnStr += repr(e)
  returnStr = "FAILURE"
finally:
  dbutils.notebook.exit(returnStr)
