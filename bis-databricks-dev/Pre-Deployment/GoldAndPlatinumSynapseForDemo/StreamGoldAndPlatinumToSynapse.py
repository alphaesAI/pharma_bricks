# Databricks notebook source
dbutils.widgets.text("client","","")

client = dbutils.widgets.get("client")
clientContainer = client.lower()
mountPoint = "/mnt/"

# COMMAND ----------

from pyspark.sql.functions import explode, col,lit
import json

# COMMAND ----------

json = """{
  "Synapse": [
    {
      "Type": "RefData",
      "Group": [
        {
          "Layer": "Gold",
          "TableName": "goldICD",
          "SourcePath": "/Gold/icd",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldHCC",
          "SourcePath": "/Gold/hcc",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldICDHCCXRef",
          "SourcePath": "/Gold/icdHCCXref",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldTrumpingHCC",
          "SourcePath": "/Gold/TrumpingHCC",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldAppointmentType",
          "SourcePath": "/Gold/appointmentType",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCDIAlertQueryResponse",
          "SourcePath": "/Gold/cdiAlertQueryResponse",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCDIAlertWorkflowExceptionOption",
          "SourcePath": "/Gold/cdiAlertWorkflowExceptionOption",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCDIAlertWorkflowStatus",
          "SourcePath": "/Gold/cdiAlertWorkflowStatus",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldAlertResponseOption",
          "SourcePath": "/Gold/alertResponseOption",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCDIAlertQueryCode",
          "SourcePath": "/Gold/cdiAlertQueryCode",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldAlertGroup",
          "SourcePath": "/Gold/alertGroup",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimDate",
          "SourcePath": "/Platinum/dimDate",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimMonth",
          "SourcePath": "/Platinum/dimMonth",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimICD",
          "SourcePath": "/Platinum/dimICD",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimHCC",
          "SourcePath": "/Platinum/dimHCC",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimAlertGroup",
          "SourcePath": "/Platinum/dimAlertGroup",
          "Notebook": "ExecuteStreaming"
        }
      ]
    },
    {
      "Type": "Client",
      "Group": [
        {
          "Layer": "Platinum",
          "TableName": "dimProvider",
          "SourcePath": "/Platinum/dimProvider",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "dimMember",
          "SourcePath": "/Platinum/dimMember",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMember",
          "SourcePath": "/Gold/MA/Client/Member",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldProvider",
          "SourcePath": "/Gold/MA/Client/Provider",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldProviderGroupReference",
          "SourcePath": "/Gold/MA/PEC/providerGroupReference",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMemberRoster",
          "SourcePath": "/Gold/MA/PEC/memberRoster",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldPecReportBase",
          "SourcePath": "/Gold/MA/PEC/pecReportBase",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldConsolidatedMMR",
          "SourcePath": "/Gold/MA/Client/ConsolidatedMMR",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldChaseProviderList",
          "SourcePath": "/Gold/MA/Risk/ChaseProviderList",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldSupplementalDiagnosis",
          "SourcePath": "/Gold/MA/Risk/SupplementalDiagnosis",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMedicalGoldenClaimDiagnosis",
          "SourcePath": "/Gold/MA/Risk/MedicalGoldenClaimDiagnosis",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMedicalGoldenClaimProcedure",
          "SourcePath": "/Gold/MA/Risk/MedicalGoldenClaimLineProcCodes",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCDIAlertLine",
          "SourcePath": "/Gold/MA/PEC/cdiAlertLine",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCacheSuspectAnalysis",
          "SourcePath": "/Gold/MA/Risk/CacheSuspectAnalysis",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldCacheSuspectAnalysisHistory",
          "SourcePath": "/Gold/MA/Risk/CacheSuspectAnalysisHistory",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMembership",
          "SourcePath": "/Gold/MA/Risk/Membership",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldMAO004Diagnosis",
          "SourcePath": "/Gold/MA/Risk/MAO004Diagnosis",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Gold",
          "TableName": "goldProviderHierarchy",
          "SourcePath": "/Gold/MA/Client/ProviderHierarchy",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "factMemberCDIAlert",
          "SourcePath": "/Platinum/factMemberCDIAlert",
          "Notebook": "ExecuteStreaming"
        },
        {
          "Layer": "Platinum",
          "TableName": "factMemberRevenueGap",
          "SourcePath": "/Platinum/factMemberRevenueGap",
          "Notebook": "ExecuteStreaming"
        }
      ]
    }
  ]
}"""

# COMMAND ----------

jsonList = []
jsonList.append(json)
df = spark.read.json(sc.parallelize(jsonList))

dfexplodedGroup = df.select(explode("Synapse")).select(
                  "col.Type" 
                 ,"col.Group"
                  )

dfexplodedSubGroup = dfexplodedGroup.select("Type", explode("Group")).select(
                  "Type" 
                 ,"col.Layer"
                 ,"col.TableName"
                 ,"col.SourcePath"
                 ,"col.Notebook"
                  )

dfexplodedSubGroup.createOrReplaceTempView("SynapseTables")

# COMMAND ----------

if clientContainer == "global":
  dataCollect = dfexplodedSubGroup.filter(col("Type") == "RefData").collect()
elif clientContainer != "global":
  dataCollect = dfexplodedSubGroup.filter(col("Type") == "Client").collect()

for row in dataCollect:
  print("Processing " + row["TableName"])
  sourcePath = mountPoint + clientContainer + row["SourcePath"]
  checkPoint = sourcePath + "/Checkpoint-" + row["TableName"]
  destinationTable = clientContainer + "." + row["TableName"]

  try:
    result = dbutils.notebook.run(row["Notebook"], 0, {"ClientContainer": clientContainer, "ConsolidatedPath": sourcePath,"DestTable": destinationTable,"CheckPoint": checkPoint} )
    result = "SUCCESS"
  except:
    result = "FAILURE"

  print("Processing "  + row["TableName"] + ": " + result)

# COMMAND ----------

# DBTITLE 1,Run SQL ConnectionNotebook
# MAGIC %run "../GoldAndPlatinumSynapseForDemo/SetupSQLConnectionJDBC"

# COMMAND ----------

# DBTITLE 1,Create SQL Variable (scala context)
# MAGIC %scala
# MAGIC val sqlStatment = """
# MAGIC --- processing log table used for restart from failure or audit
# MAGIC 	if object_id('dbo.processtable_Log') is null
# MAGIC 	create  table dbo.processtable_Log
# MAGIC 	(
# MAGIC 	TableName varchar(50), 
# MAGIC 	ErrorMessage varchar(2000),
# MAGIC 	[Start] datetime,
# MAGIC 	[End] datetime
# MAGIC 	)			
# MAGIC --- determin running envrioment
# MAGIC declare @dbname varchar(50), @Source_schema varchar(15) = NULL, @demo_schema  varchar(15) = null
# MAGIC select @dbname = db_name()
# MAGIC --print @dbname
# MAGIC 
# MAGIC if (@dbname like '%-d-%')
# MAGIC begin 
# MAGIC 	set @Source_schema = 'devidap1'
# MAGIC 	set @demo_schema = 'devidap2'	
# MAGIC end
# MAGIC 
# MAGIC if (@dbname like '%-s-%')
# MAGIC begin 
# MAGIC 	set @Source_schema = 'bcbsks'
# MAGIC 	set @demo_schema = 'demo'
# MAGIC end
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC ----- all table list-- total table list from BIS-1429
# MAGIC if object_id('tempdb..#alltablename') is not null drop table #alltablename
# MAGIC select distinct tab.name as tablename
# MAGIC into  #alltablename
# MAGIC from sys.tables as tab   
# MAGIC where schema_name(tab.schema_id) = @Source_schema
# MAGIC and tab.name in ('goldCDIAlertLine',
# MAGIC 'goldCDIStatus',
# MAGIC 'goldCacheSuspectAnalysis',
# MAGIC 'goldCacheSuspectAnalysisHistory',
# MAGIC 'goldChaseProviderList',
# MAGIC 'goldConsolidatedMMR',
# MAGIC 'goldGapsInCare',
# MAGIC 'goldGapsInCareRR',
# MAGIC 'goldMAMembershipStars',
# MAGIC 'goldMAO004Diagnosis',
# MAGIC 'goldMedicalGoldenClaimDiagnosis',
# MAGIC 'goldMedicalGoldenClaimProcedure',
# MAGIC 'goldMember',
# MAGIC 'goldMemberRevenueGap',
# MAGIC 'goldMemberRoster',
# MAGIC 'goldMembership',
# MAGIC 'goldPCPAttribution',
# MAGIC 'goldPecReportBase',
# MAGIC 'goldPracticeTargetEngagementStatus',
# MAGIC 'goldProvider',
# MAGIC 'goldProviderGroupReference',
# MAGIC 'goldProviderHierarchy',
# MAGIC 'goldRiskByHCC',
# MAGIC 'goldRiskByMember',
# MAGIC 'goldSupplementalDiagnosis',
# MAGIC --'goldTrumpingHCC',
# MAGIC --'goldAlertGroup',
# MAGIC --'goldAlertResponseOption',
# MAGIC --'goldAppointmentType',
# MAGIC --'goldCDIAlertQueryCode',
# MAGIC --'goldCDIAlertQueryResponse',
# MAGIC --'goldCDIAlertWorkflowExceptionOption',
# MAGIC --'goldCDIAlertWorkflowStatus',
# MAGIC --'goldHCC',
# MAGIC --'goldICD',
# MAGIC --'goldICDHCCXRef',
# MAGIC --pltm
# MAGIC 'dimClient',
# MAGIC 'dimClosureReason',
# MAGIC 'dimMember',
# MAGIC 'dimProvider',
# MAGIC 'factMemberCDIAlert',
# MAGIC 'factMemberRevenueGap'
# MAGIC --'dimDate',
# MAGIC --'dimHCC',
# MAGIC --'dimICD',
# MAGIC --'dimAlertGroup',
# MAGIC --'dimMonth',
# MAGIC )
# MAGIC 
# MAGIC 
# MAGIC -----PHI tables with columns and column length that need to be de-identified
# MAGIC if object_id('tempdb..#processtable') is not null drop table #processtable
# MAGIC select * ,
# MAGIC case when column_name like '%client%code%' then --column_name + ' = ''' + 'Demo' + ''''   else -- 
# MAGIC 												column_name + ' = ''' + @demo_schema  + ''''  else
# MAGIC case when isnull(col_len,'') <> '' and col_len >= 16 then column_name + ' = case when isnull(' + column_name + ','''') = '''' then null else ' + 'cast(HASHBYTES(''MD5'', ' + column_name + ') as varchar('+ cast(col_len as varchar) + ')) end'
# MAGIC 		when isnull(col_len,'') <> ''  and col_len < 16 then  column_name + ' = case when isnull(' + column_name + ','''') = '''' then null else ' + 'left(cast(CHECKSUM(' + column_name + ') as varchar),' + cast(col_len as varchar) + ')  end'
# MAGIC 		when isnull(col_len,'') = ''  and (column_name like '%DOB%' or column_name like '%date%')  then  column_name + ' = ' + 'case when isdate(cast(' + column_name + ' as varchar))= 1 then DATEADD(day, 1000, ' + column_name + ') else null end'
# MAGIC 		when isnull(col_len,'') = ''  and isdate(col_len) = 0 then  column_name + ' = cast(' + column_name + ' as int) - 3'
# MAGIC end end as update_string
# MAGIC into  #processtable
# MAGIC from (
# MAGIC 		select distinct tab.name as table_name,  col.name as column_name, CHARACTER_MAXIMUM_LENGTH as col_len 
# MAGIC 		from sys.tables as tab
# MAGIC 			inner join sys.columns as col
# MAGIC 				on tab.object_id = col.object_id
# MAGIC 			left join sys.types as t
# MAGIC 			on col.user_type_id = t.user_type_id
# MAGIC 			left join INFORMATION_SCHEMA.COLUMNS infocol
# MAGIC 			on schema_name(tab.schema_id) = infocol.Table_schema
# MAGIC 			and tab.name = infocol.table_name and col.name = infocol.column_name
# MAGIC 		where schema_name(tab.schema_id) = @Source_schema
# MAGIC 		and col.name in (
# MAGIC 		---PEC
# MAGIC 		'uniquePersonKey',
# MAGIC 		'planMemberID',
# MAGIC 		'beneficiaryID',
# MAGIC 		'subscriberID',
# MAGIC 		'fullName',
# MAGIC 		'LastName',
# MAGIC 		'firstname',
# MAGIC 		'middleInitial',
# MAGIC 		'alternateMemberID',
# MAGIC 		'maskedMemberID',
# MAGIC 		'enrolleeUniqueID',
# MAGIC 		'dateofBirth',
# MAGIC 		'deceasedDate',
# MAGIC 		'gender',
# MAGIC 		'permanentAddressLine1',
# MAGIC 		'permanentAddressLine2',
# MAGIC 		'permanentAddressLine3',
# MAGIC 		'permanentCity',
# MAGIC 		'permanentCounty',
# MAGIC 		'permanentZIPCode',
# MAGIC 		'permanentSCC',
# MAGIC 		'mailingAddressLine1',
# MAGIC 		'mailingAddressLine2',
# MAGIC 		'mailingAddressLine3',
# MAGIC 		'mailingCity',
# MAGIC 		'mailingCounty',
# MAGIC 		'mailingZIPCode',
# MAGIC 		'mailingCounty',
# MAGIC 		'billingAddressLine1',
# MAGIC 		'billingAddressLine2',
# MAGIC 		'billingAddressLine3',
# MAGIC 		'billingCity',
# MAGIC 		'billingCounty',
# MAGIC 		'billingZIPCode',
# MAGIC 		'phoneNumber',
# MAGIC 		'alternatePhoneNumber',
# MAGIC 		'email',
# MAGIC 		'emergencyContactName',
# MAGIC 		'emergencyContactRelationship',
# MAGIC 		'emergencyContactPhoneNumber',
# MAGIC 		'medicaidID',
# MAGIC 		'fax',
# MAGIC 		'poaName',
# MAGIC 		'poaAddress1',
# MAGIC 		'poaAddress2',
# MAGIC 		'poaAddress3',
# MAGIC 		'poaCity',
# MAGIC 		'poaZipCode',
# MAGIC 		'poaPhoneNumber',
# MAGIC 		'caretakerFirstName',
# MAGIC 		'caretakerLastName',
# MAGIC 		'caretakerMiddleInitial',
# MAGIC 		'lastName',
# MAGIC 		'firstName',
# MAGIC 		'middleName',
# MAGIC 		'practiceName',
# MAGIC 		'providerOrgName',
# MAGIC 		--QA
# MAGIC 		'beneficiaryID',
# MAGIC 		'planMemberID',
# MAGIC 		'memberLastName',
# MAGIC 		'memberFirstName',
# MAGIC 		'memberDOB',
# MAGIC 		'memberDOD',
# MAGIC 		'memberAddress1',
# MAGIC 		'memberAddress2',
# MAGIC 		'memberCity',
# MAGIC 		'memberState',
# MAGIC 		'memberZip',
# MAGIC 		'memberCounty',
# MAGIC 		'memberPhone',
# MAGIC 		'memberEmail',
# MAGIC 		'poName',
# MAGIC 		'practiceName',
# MAGIC 		'providerLastName',
# MAGIC 		'providerFirstName',
# MAGIC 		'AltMemberId9',
# MAGIC 		'altMemberIdCurr',
# MAGIC 		'pbp',
# MAGIC 		'memberGroupNumber',
# MAGIC 		'memberGroupName',
# MAGIC 		'planMemberID',
# MAGIC 		'providerName',
# MAGIC 		--risk
# MAGIC 		'ClientCode',
# MAGIC 		'planMemberID',
# MAGIC 		'memberFirstName',
# MAGIC 		'memberLastName',
# MAGIC 		'memberDOB',
# MAGIC 		'memberGender',
# MAGIC 		'BeneficiaryID',
# MAGIC 		'memberAge',
# MAGIC 		'permanentAddressLine1',
# MAGIC 		'permanentAddressLine2',
# MAGIC 		'permanentAddressLine3',
# MAGIC 		'permanentCity',
# MAGIC 		'permanentCounty',
# MAGIC 		'permanentState',
# MAGIC 		'permanentZIPCode',
# MAGIC 		'memberZIPCode',
# MAGIC 		'memberState',
# MAGIC 		'memberCounty',
# MAGIC 		'memberDOB'
# MAGIC 		)
# MAGIC 		and tab.name in (select tablename from #alltablename)
# MAGIC ) c
# MAGIC 
# MAGIC 
# MAGIC ---------perform pull data from source and de-identify PHI columns and load to demo
# MAGIC 
# MAGIC 
# MAGIC 	declare @tablename varchar(60), @i int = 0 
# MAGIC 	declare @sql varchar(max), @updatesql varchar(max), @errorsql varchar(max)
# MAGIC 	--- for restart from last failure purpose, remove process completed tables from list 
# MAGIC 	delete from #alltablename where tablename in ( select tablename from dbo.processtable_Log where [end] is not null)
# MAGIC 	select @i = count(*) from #alltablename
# MAGIC 	
# MAGIC 
# MAGIC 	WHILE @i > 0 
# MAGIC 	BEGIN
# MAGIC       BEGIN TRY
# MAGIC 		set @sql = null 
# MAGIC 		set @updatesql = null 
# MAGIC 		set @errorsql  = null
# MAGIC 		select top 1 @tablename = tablename from #alltablename 	
# MAGIC 		---insert log start
# MAGIC 		insert into dbo.processtable_Log  (TableName, [start])
# MAGIC 		select @tablename as tablename, getdate() as [start]
# MAGIC 				
# MAGIC 		IF EXISTS (SELECT 1 FROM  #processtable WHERE table_name = @tablename)
# MAGIC 		begin
# MAGIC 			--get update statement dynamically
# MAGIC 			select @updatesql = STRING_AGG(cast(update_string as varchar(Max)), ',') from #processtable
# MAGIC 			where table_name = @tablename							
# MAGIC 		end	
# MAGIC 		
# MAGIC 		IF (@updatesql IS NOT NULL)  ---- table contains PHI data, need to process masking
# MAGIC 		begin
# MAGIC 			---copy data from source to temp table
# MAGIC 			set @sql = 'if object_id(''tempdb..#temp'') is not null drop table #temp
# MAGIC 					select * into #temp from ' + @Source_schema + '.' + @tablename
# MAGIC 			--- mask PHI in temp table
# MAGIC 			set @sql = @sql + cast('  Update #temp set ' + @updatesql as varchar(max))
# MAGIC 			--insert into destination from #temp table
# MAGIC 			set @sql = @sql + '  insert into ' + @demo_schema + '.' + @tablename + ' select * from #temp '	
# MAGIC 		end
# MAGIC 
# MAGIC 		ELSE --- if no PHI data, table copied from source to destination without transform
# MAGIC 		begin 
# MAGIC 			set @sql = '  insert into ' + @demo_schema + '.' + @tablename + ' select * from ' + @Source_schema + '.' + @tablename
# MAGIC 		end 
# MAGIC 
# MAGIC 		EXEC(@sql)
# MAGIC 
# MAGIC 		delete from	#alltablename where tablename = @tablename 
# MAGIC 		update dbo.processtable_Log  set [END] = getdate()  where tablename = @tablename
# MAGIC 		set @i = @i -1
# MAGIC       END TRY
# MAGIC       BEGIN CATCH
# MAGIC         --- if any failure, you need to check table processtable_Log to fix the issue and re-run this script, it will start from unprocessed tables
# MAGIC         set @errorsql = ' truncate table  ' + @demo_schema + '.' + @tablename 
# MAGIC         EXEC(@errorsql)
# MAGIC         update dbo.processtable_Log  set ErrorMessage = ERROR_MESSAGE(), tablename = tablename +'_failed'  where tablename = @tablename	
# MAGIC 		delete from	#alltablename where tablename = @tablename 
# MAGIC 		set @i = @i -1
# MAGIC 	END CATCH;
# MAGIC 	END
# MAGIC  
# MAGIC 
# MAGIC --------------------validate running results------------------------
# MAGIC select * from dbo.processtable_Log
# MAGIC 
# MAGIC --   drop table dbo.processtable_Log 
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC """

# COMMAND ----------

# DBTITLE 1,Execute SQL Command
# MAGIC %scala
# MAGIC import java.sql.DriverManager
# MAGIC import java.sql.Connection
# MAGIC import java.util.Properties
# MAGIC 
# MAGIC val conection = DriverManager.getConnection(jdbcURL, connectionProperties)
# MAGIC val statement = conection.createStatement()
# MAGIC 
# MAGIC statement.execute(sqlStatment)
# MAGIC statement.close()
