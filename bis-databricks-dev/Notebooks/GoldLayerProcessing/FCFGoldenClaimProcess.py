# Databricks notebook source
# DBTITLE 1,Setup variables and mount point
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("DataSourceName","","")

clientCode = dbutils.widgets.get("ClientContainer")
DataSourceName = dbutils.widgets.get("DataSourceName")

mntPnt = '/mnt/'
mntPntClientCode = mntPnt + clientCode

# COMMAND ----------

# DBTITLE 1,Setup table configs
tableConfig = """
{
  "DestinationTableName": "GoldenClaim",
  "DestinationTablePath": "#clientCode/Gold/MA/Client/GoldenClaim",
  "SourceTables": [
    {
      "TableName": "GoldenClaimHistory",
      "TablePath": "#clientCode/Gold/MA/Client/GoldenClaimHistory",
      "TableFormat": "delta"
    },
    {
      "TableName": "MedicalClaimHeader",
      "TablePath": "#clientCode/consolidated/MA/Data/MedicalClaimHeader",
      "TableFormat": "delta"
    },
    {
      "TableName": "MedicalClaimLine",
      "TablePath": "#clientCode/consolidated/MA/Data/MedicalClaimLine",
      "TableFormat": "delta"
    },
    {
      "TableName": "ProviderSpecialtyDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ProviderSpecialtyDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ProcedureDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ProcedureDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "PlaceOfServiceDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/PlaceOfServiceDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ResponseMAO002",
      "TablePath": "#clientCode/consolidated/MA/Data/MAO002",
      "TableFormat": "delta"
    },
    {
      "TableName": "ResponseMAO004",
      "TablePath": "#clientCode/consolidated/MA/Data/MAO004",
      "TableFormat": "delta"
    },
    {
      "TableName": "Submitted837OutboundClaimHeader",
      "TablePath": "#clientCode/consolidated/MA/Data/Submitted837OutboundClaimHeader",
      "TableFormat": "delta"
    }
  ]
}
"""

# COMMAND ----------

# DBTITLE 1,Ingest Golden Claim Helper notebook
# MAGIC %run ./GoldenClaimHelper

# COMMAND ----------

# DBTITLE 1,Query for before claims
beforeClaims = """
WITH rawCH AS (
   SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
          ,ch.ClaimTypeInd
          ,ch.BillTypeCode
          ,ch.DetailServiceDate
          ,ch.PlaceOfService
          ,ch.RenderingProviderSpecialtyCode
          ,ch.BillingProviderTaxonomy
     FROM MedicalClaimHeader ch    
     WHERE to_date(ch.DetailServiceDate, 'yyyy-MM-dd' ) < to_date('2021-01-01', 'yyyy-MM-dd')  
)
,rawCL AS (
     SELECT DISTINCT cl.GeneratedMedicalClaimsUniqueKey
          ,cl.ServiceFromDate
          ,cl.ProcCode
          ,cl.ProcCodeType          
     FROM MedicalClaimLine  cl     
)
,rawPSD AS (
    SELECT DISTINCT TaxonomyCode        
     FROM ProviderSpecialtyDataset
     WHERE CMSApproved = 1 
          AND RAApproved = 1 
)
,rawPD AS (
     SELECT DISTINCT pd.Code
               ,pd.CodeType
               ,pd.EffectiveStartDate
               ,pd.EffectiveEndDate
     FROM ProcedureDataset pd
     WHERE pd.IsRiskAdjustable  = '1'
)
,rawPlaceOfServiceDataset AS (
     SELECT DISTINCT psd.Code
     FROM PlaceOfServiceDataset psd
     WHERE psd.IsRiskAdjustable  = '1'
)
,dfRawClaims AS (
     SELECT ch.*
          ,cl.ServiceFromDate
          ,cl.ProcCode
          ,cl.ProcCodeType          
     FROM rawCH ch
     JOIN rawCL cl
          ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey              
)
,dfBeforeRawData AS (
     SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
                    ,ch.ClaimTypeInd
                    ,ch.BillTypeCode
                    ,ch.DetailServiceDate
                    ,ch.PlaceOfService        
                    ,ch.ServiceFromDate
                    ,pd.EffectiveStartDate
                    ,pd.EffectiveEndDate 
     FROM dfRawClaims ch
     JOIN rawPSD psd
     ON ch.RenderingProviderSpecialtyCode = psd.TaxonomyCode
          OR ch.BillingProviderTaxonomy = psd.TaxonomyCode
     JOIN rawPD pd
     ON ch.ProcCode = pd.Code
          AND pd.CodeType = Replace(ch.ProcCodeType,'Code', '') 
) 
SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
    ,NULL AS IsRiskAdjustableSource -- add IsRiskAdjustableSource
FROM dfBeforeRawData ch   
WHERE ((ch.ClaimTypeInd in (1, 'I') 
      AND SUBSTRING(ch.BillTypeCode,1,2) IN ('11','41'))
      OR (ch.ClaimTypeInd in (2, 'O') 
      AND SUBSTRING(ch.BillTypeCode,1,2) IN ('12','13','43','71','73','76','77','85')))
    AND YEAR(to_date(ch.DetailServiceDate, 'yyyy-MM-dd' )) 
        BETWEEN YEAR(to_date(ch.EffectiveStartDate, 'yyyy-MM-dd' )) 
            AND YEAR(to_date(IfNull(ch.EffectiveEndDate, '9999-12-31'), 'yyyy-MM-dd' ))
UNION
SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
    ,NULL AS IsRiskAdjustableSource -- add IsRiskAdjustableSource
FROM dfBeforeRawData ch  
JOIN rawPlaceOfServiceDataset psd
    ON ch.PlaceOfService = psd.Code
WHERE ch.ClaimTypeInd IN (3, 'P')    
    AND YEAR(to_date(ch.ServiceFromDate, 'yyyy-MM-dd' )) 
        BETWEEN YEAR(to_date(ch.EffectiveStartDate, 'yyyy-MM-dd' )) 
            AND YEAR(to_date(IfNull(ch.EffectiveEndDate, '9999-12-31'), 'yyyy-MM-dd' ))
"""

# COMMAND ----------

# DBTITLE 1,Query for between claims
betweenClaims = """
WITH dfMedChRaw AS (
     SELECT ch.GeneratedMedicalClaimsUniqueKey
          ,ch.ClaimTypeInd
          ,ch.BillTypeCode
          ,ch.DetailServiceDate
          ,ch.PlaceOfService
     FROM MedicalClaimHeader ch
     WHERE to_date(ch.DetailServiceDate, 'yyyy-MM-dd' ) 
     BETWEEN to_date('2021-01-01', 'yyyy-MM-dd') 
          AND to_date('2022-05-31', 'yyyy-MM-dd')
)
,dfMedCLRaw AS (
     SELECT DISTINCT cl.GeneratedMedicalClaimsUniqueKey
          ,cl.ServiceFromDate
          ,cl.ProcCode
          ,cl.ProcCodeType          
     FROM MedicalClaimLine cl     
)
,dfPDRaw AS (
     SELECT DISTINCT pd.Code
          ,pd.CodeType
          ,pd.EffectiveStartDate
          ,pd.EffectiveEndDate 
     FROM ProcedureDataset pd
     WHERE pd.IsRiskAdjustable  = '1'
)
,rawPlaceOfServiceDataset AS (
     SELECT DISTINCT psd.Code
     FROM PlaceOfServiceDataset psd
     WHERE psd.IsRiskAdjustable  = '1'
)
,dfRawData AS (
     SELECT DISTINCT ch.*
          ,cl.ServiceFromDate
          ,pd.EffectiveStartDate
          ,pd.EffectiveEndDate 
     FROM dfMedChRaw ch
     JOIN dfMedCLRaw cl
     ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey
     JOIN dfPDRaw pd
     ON cl.ProcCode = pd.Code
     AND pd.CodeType = Replace(cl.ProcCodeType,'Code', '')
)  
SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
    ,NULL AS IsRiskAdjustableSource -- add IsRiskAdjustableSource
FROM dfRawData ch 
WHERE ((ch.ClaimTypeInd in (1, 'I') 
AND SUBSTRING(ch.BillTypeCode,1,2) IN ('11','41'))
OR (ch.ClaimTypeInd in (2, 'O') 
     AND SUBSTRING(ch.BillTypeCode,1,2) IN ('12','13','43','71','73','76','77','85')))
     AND YEAR(to_date(ch.DetailServiceDate, 'yyyy-MM-dd' )) 
          BETWEEN YEAR(to_date(ch.EffectiveStartDate, 'yyyy-MM-dd' )) 
          AND YEAR(to_date(IfNull(ch.EffectiveEndDate, '9999-12-31'), 'yyyy-MM-dd' ))
UNION
SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
     ,NULL AS IsRiskAdjustableSource -- add IsRiskAdjustableSource 
FROM dfRawData ch  
JOIN rawPlaceOfServiceDataset psd
ON ch.PlaceOfService = psd.Code
WHERE ch.ClaimTypeInd in (3, 'P')
AND YEAR(to_date(ch.ServiceFromDate, 'yyyy-MM-dd' )) 
     BETWEEN YEAR(to_date(ch.EffectiveStartDate, 'yyyy-MM-dd' )) 
     AND YEAR(to_date(IfNull(ch.EffectiveEndDate, '9999-12-31'), 'yyyy-MM-dd'))
"""

# COMMAND ----------

# DBTITLE 1,Query for AfterClaims
afterClaims = """
WITH AfterClaims AS (
  SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
    ,ch.ClaimNumber
  FROM MedicalClaimHeader ch
  WHERE to_date(ch.DetailServiceDate, 'yyyy-MM-dd' ) >= to_date('2022-06-01', 'yyyy-MM-dd')
)
,RawMAO002 as (
  SELECT DISTINCT m2.PrelimRAFlag
    ,m2.EncounterLineNumber
    ,m2.EncounterICN
    ,m2.PlanEncounterID
  FROM ResponseMAO002 m2
  WHERE m2.PrelimRAFlag = 'PA'
      AND m2.EncounterLineNumber = '000'
)
,RawSubmt837Ch AS (
     SELECT DISTINCT s.TraceNumber
          ,s.EncounterICN
     FROM Submitted837OutboundClaimHeader s
)
,RawMAO004 AS (
     SELECT DISTINCT EncounterICN
     FROM ResponseMAO004
     WHERE AllowedDisallowedflag='A'
)
,MAO002 as (
  SELECT DISTINCT s.TraceNumber
    ,m2.PrelimRAFlag
    ,m2.EncounterLineNumber
    ,m2.EncounterICN
    ,m2.PlanEncounterID
  FROM RawMAO002 m2 
  INNER JOIN RawSubmt837Ch s
  ON m2.PlanEncounterID = s.EncounterICN
)
,MAO004 as (
  SELECT DISTINCT m2.TraceNumber
    ,m2.PrelimRAFlag
    ,m2.EncounterLineNumber
    ,m2.EncounterICN
    ,m2.PlanEncounterID
  FROM MAO002 m2
  INNER JOIN RawMAO004 m4
    ON m2.EncounterICN = m4.EncounterICN  
)
,MAO004Accepted as (
  SELECT DISTINCT mh.GeneratedMedicalClaimsUniqueKey,
    'MAO004Accepted' AS IsRiskAdjustableSource
  FROM AfterClaims mh
  INNER JOIN MAO004 s
    ON mh.ClaimNumber = s.TraceNumber
)
,NotMatchedStep1 as (
  SELECT DISTINCT *
  FROM AfterClaims mh
  WHERE mh.GeneratedMedicalClaimsUniqueKey NOT IN (
    SELECT DISTINCT GeneratedMedicalClaimsUniqueKey
    FROM MAO004Accepted
  )
)
,MAO002Accepted as (
  SELECT DISTINCT mh.GeneratedMedicalClaimsUniqueKey,
    'MAO002Accepted' AS IsRiskAdjustableSource
  FROM NotMatchedStep1 mh
  INNER JOIN MAO002 s
    ON mh.ClaimNumber = s.TraceNumber
)
SELECT * FROM MAO002Accepted
UNION 
SELECT * FROM MAO004Accepted
"""

# COMMAND ----------

# DBTITLE 1,Query for IsAdjustableSource
  adjSqlQuery = """
    SELECT DISTINCT 
      GeneratedMedicalClaimsUniqueKey
      ,IsRiskAdjustableSource
    FROM dfBeforeClaims 
    UNION 
    SELECT DISTINCT  
      GeneratedMedicalClaimsUniqueKey
      ,IsRiskAdjustableSource
    FROM dfBetweenClaims
    UNION 
    SELECT DISTINCT
      GeneratedMedicalClaimsUniqueKey
      ,IsRiskAdjustableSource
    FROM dfAfterClaims
  """

# COMMAND ----------

# DBTITLE 1,Query for TeleHealthClaims
rawTeleHealthClaims = """
WITH dfChRaw AS (
     SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
               ,ch.PlaceOfService 
     FROM MedicalClaimHeader ch 
     WHERE ch.ClaimTypeInd IN (3, 'P')
)
,dfClRaw AS (
     SELECT DISTINCT cl.GeneratedMedicalClaimsUniqueKey
               ,cl.ProcCode
               ,cl.ProcCodeType
               ,cl.ServiceFromDate
     FROM MedicalClaimLine cl 
     WHERE cl.PlaceOfService = '02'
     OR cl.ProcMod1Orig IN ('GT', '95')
)
,dfPSDRaw AS (
     SELECT DISTINCT psd.Code
     FROM PlaceOfServiceDataset psd
     WHERE psd.IsRiskAdjustable  = '1'
)
,dfPDRaw AS (
     SELECT DISTINCT pd.Code
               ,pd.CodeType
               ,pd.EffectiveStartDate
               ,pd.EffectiveEndDate
     FROM ProcedureDataset pd
     WHERE pd.IsRiskAdjustable  = '1'
)
,dfClaimsRaw AS (
     SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
               ,ch.PlaceOfService 
               ,cl.ProcCode
               ,cl.ProcCodeType
               ,cl.ServiceFromDate
     FROM dfChRaw ch        
     JOIN dfClRaw cl
     ON ch.GeneratedMedicalClaimsUniqueKey = cl.GeneratedMedicalClaimsUniqueKey
)
SELECT DISTINCT ch.GeneratedMedicalClaimsUniqueKey
FROM dfClaimsRaw ch  
     JOIN dfPSDRaw psd ON ch.PlaceOfService = psd.Code   
     JOIN dfPDRaw pd ON ch.ProcCode = pd.Code
     AND pd.CodeType = Replace(ch.ProcCodeType,'Code', '') 
     AND YEAR(to_date(ch.ServiceFromDate, 'yyyy-MM-dd' )) 
       BETWEEN YEAR(to_date(pd.EffectiveStartDate, 'yyyy-MM-dd' )) 
     AND YEAR(to_date(IfNull(pd.EffectiveEndDate, '9999-12-31'), 'yyyy-MM-dd' ))
"""

# COMMAND ----------

# DBTITLE 1,Query for GCPool
goldenClaimPoolSQLQuery = f"""
    WITH StrippedMedicalClaimHeader AS(
    SELECT 
       GeneratedMedicalClaimsUniqueKey
      ,ClientID
      ,FileLayoutID
      ,FileLayoutDescription
      ,ClaimNumber
      ,OriginalClaimNumber
      ,BeneficiaryID
      ,PlanMemberID
      ,UniquePersonKey
      ,CMSContractNumber
      ,BillTypeCode
      ,ClaimTypeInd
      ,ClaimWeight
      ,ClaimStatus
      ,ClaimProcessDate
      ,ClaimSource 
    FROM MedicalClaimHeader
    WHERE
    COALESCE(IsDeniedDuplicate,0) = 0
    AND
    FileLayoutId IN(SELECT DISTINCT FileLayoutID FROM GoldenClaimFileLayouts WHERE DataSourceName = 'FCF')
    AND
    FileId NOT IN(SELECT DISTINCT FileId FROM ErrorFileIds)
    ),
    GoldenClaimSource AS(
    SELECT
       CONCAT(COALESCE(OriginalClaimNumber,''),'-',COALESCE(FileLayoutID,''),'-',COALESCE(ClientID,'')) AS GeneratedGoldenClaimsUniqueKey
      ,GeneratedMedicalClaimsUniqueKey
      ,ClientID
      ,FileLayoutID
      ,FileLayoutDescription
      ,ClaimNumber
      ,OriginalClaimNumber
      ,BeneficiaryID
      ,PlanMemberID
      ,UniquePersonKey
      ,CMSContractNumber
      ,BillTypeCode
      ,CASE
          WHEN ClaimTypeInd = '1' THEN 'I'
          WHEN ClaimTypeInd = '2' THEN 'O'
          WHEN ClaimTypeInd = '3' THEN 'P'
          ELSE ClaimTypeInd
      END AS ClaimTypeInd
      ,ClaimWeight
      ,ClaimStatus
      ,ClaimProcessDate
      ,ClaimSource
      ,to_timestamp(current_timestamp(), "MM/dd/yyyy HH:mm:ss") AS LoadTimestamp
      ,row_number() OVER (PARTITION BY OriginalClaimNumber ORDER BY ClaimNumber DESC, ClaimWeight DESC) AS RowNumber
    FROM StrippedMedicalClaimHeader 
    )
    SELECT 
       gcs.GeneratedGoldenClaimsUniqueKey
      ,gcs.GeneratedMedicalClaimsUniqueKey
      ,gcs.ClientID
      ,gcs.FileLayoutID
      ,gcs.FileLayoutDescription
      ,'{DataSourceName}' AS SourceName
      ,gcs.ClaimNumber
      ,gcs.OriginalClaimNumber
      ,gcs.BeneficiaryID
      ,gcs.PlanMemberID
      ,gcs.UniquePersonKey
      ,gcs.CMSContractNumber
      ,gcs.BillTypeCode
      ,gcs.ClaimTypeInd
      ,gcs.ClaimWeight
      ,gcs.ClaimStatus
      ,gcs.ClaimProcessDate
      ,gcs.ClaimSource
      ,gcs.LoadTimestamp
      ,CASE WHEN ra.GeneratedMedicalClaimsUniqueKey IS NOT NULL THEN 1 ELSE 0 END AS IsRiskAdjustable
      ,CASE WHEN th.GeneratedMedicalClaimsUniqueKey IS NOT NULL THEN 1 ELSE 0 END AS IsTeleHealth
      ,ra.IsRiskAdjustableSource
    FROM GoldenClaimSource gcs
      LEFT JOIN RiskAdjustable ra
        ON gcs.GeneratedMedicalClaimsUniqueKey = ra.GeneratedMedicalClaimsUniqueKey
      LEFT JOIN TeleHealth th
        ON gcs.GeneratedMedicalClaimsUniqueKey = th.GeneratedMedicalClaimsUniqueKey
    WHERE gcs.RowNumber = 1
  """

# COMMAND ----------

# DBTITLE 1,Method to Get Claims IsRiskAdjusted 
def isRiskAdjustedClaims():

  dfBeforeClaims = sqlContext.sql(beforeClaims)
  dfBeforeClaims.createOrReplaceTempView("dfBeforeClaims")
  
  dfBetweenClaims = sqlContext.sql(betweenClaims)
  dfBetweenClaims.createOrReplaceTempView("dfBetweenClaims")
  
  dfAfterClaims = sqlContext.sql(afterClaims)
  dfAfterClaims.createOrReplaceTempView("dfAfterClaims")

  #Union the GeneratedMedicalClaimsUniqueKey
  dfAdjusted = sqlContext.sql(adjSqlQuery)
  dfAdjusted.createOrReplaceTempView("RiskAdjustable")

# COMMAND ----------

# DBTITLE 1,Method to Get Claims IsTeleHealth
def isTeleHealthClaims():
  dfTeleHealth = sqlContext.sql(rawTeleHealthClaims)
  dfTeleHealth.createOrReplaceTempView("TeleHealth")

# COMMAND ----------

# DBTITLE 1,Run Golden Claims Logic
if (len(failedTablesList) == 0):
  #get the dataframe of GeneratedMedicalClaimsUniqueKey for IsRiskAdjusted
  isRiskAdjustedClaims() #dfAdjustedClaimsIDs
  #get the dataframe of GeneratedMedicalClaimsUniqueKey for IsTeleHealth
  isTeleHealthClaims() #dfTeleHealthClaimsIDs

  goldenClaimPool = sqlContext.sql(goldenClaimPoolSQLQuery)
  goldenClaimPool.createOrReplaceTempView("FinalGoldenClaim")

  ##insert into GC
  InsertGC()

  returnStr = "GoldenClaim tables refreshed!"
else:
  #add more info to see why gc not run
  returnStr = "GoldenClaim tables did not refresh because: \r\nNew claim files count: " + len(clmDF.collect()) +  "\r\n" + "OR the following tables did not exist" + ' '.join(failedTablesList) +"\r\n"

# COMMAND ----------

# DBTITLE 0,Exit notebook -- return back to caller
dbutils.notebook.exit(returnStr)
