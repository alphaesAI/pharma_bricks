# Databricks notebook source
# DBTITLE 1,Setup variables and mount point
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("DataSourceName","","")

clientCode = dbutils.widgets.get("ClientContainer")
DataSourceName = dbutils.widgets.get("DataSourceName")

mntPnt = '/mnt/'

# COMMAND ----------

# DBTITLE 1,Setup table configs
tableConfig = """
{
  "DestinationTableName": "GoldenClaim",
  "DestinationTablePath": "#clientCode/Gold/MA/Client/GoldenClaim",
  "SourceTables": [
    {
      "TableName": "MedicalClaimHeader",
      "TablePath": "#clientCode/consolidated/MA/Data/MedicalClaimHeader",
      "TableFormat": "delta"
    }
  ]
}
"""

# COMMAND ----------

# DBTITLE 1,Ingest Golden Claim Helper notebook
# MAGIC %run ./GoldenClaimHelper

# COMMAND ----------

# DBTITLE 1,Run Golden Claims Logic
returnStr = ""

if (len(failedTablesList) == 0):
  GoldenClaimQuery = f"""
---Find a claim #'s original claim number group and their associated suffix sequence ---
WITH OriginalClaimGroupGeneration AS(
SELECT  
      ClaimNumber
     ,GeneratedMedicalClaimsUniqueKey
     ,ClientId
     ,FileLayoutID
     ,FileLayoutDescription
     ,SourceName
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
     ,CASE 
        WHEN REPLACE(ClaimNumber, SUBSTRING(ClaimNumber, PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') = REPLACE(REVERSE(ClaimNumber),SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') THEN ClaimNumber --Handles cases where the same number exists on bothh sides of the claim example = 23171E23171
        WHEN REPLACE(ClaimNumber, SUBSTRING(ClaimNumber, PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') = REVERSE(SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',ClaimNumber), LEN(ClaimNumber)))THEN ClaimNumber --Handles cases where the numbers differ between sides of the claim
        ELSE REVERSE(SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',REVERSE(ClaimNumber)) + 1, LEN(ClaimNumber)))
      END AS OriginalClaimGroup
     ,CASE 
        WHEN REPLACE(ClaimNumber, SUBSTRING(ClaimNumber, PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') = REPLACE(REVERSE(ClaimNumber),SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') THEN NULL --Handles cases where the same number exists on bothh sides of the claim example = 23171E23171
        WHEN REPLACE(ClaimNumber, SUBSTRING(ClaimNumber, PATERNINDEX('[a-zA-Z]',ClaimNumber) + 1, LEN(ClaimNumber)),'') = REVERSE(SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',ClaimNumber), LEN(ClaimNumber)))THEN NULL --Handles cases where the numbers differ between sides of the claim
        ELSE REPLACE(ClaimNumber,REVERSE(SUBSTRING(REVERSE(ClaimNumber), PATERNINDEX('[a-zA-Z]',REVERSE(ClaimNumber)) + 1, LEN(ClaimNumber))),'')
      END AS OriginalClaimGroupSequence
      
     ,null AS IsRiskAdjustable
     ,null AS IsTeleHealth
     ,null AS IsRiskAdjustableSource
     ,current_timestamp() AS LoadTimestamp
FROM MedicalClaimHeader
WHERE 
SourceName = '{DataSourceName}'
AND
FileId NOT IN(SELECT DISTINCT FileId FROM ErrorFileIds)
),
ClaimGroupingLevel AS(
SELECT 
     ClaimNumber
    ,GeneratedMedicalClaimsUniqueKey
    ,SourceName
    ,IsRiskAdjustable
    ,IsTeleHealth
    ,IsRiskAdjustableSource
    ,LoadTimestamp
    ,FileLayoutID
    ,FileLayoutDescription
    ,ClientId
    ,OriginalClaimGroup
    ,OriginalClaimGroupSequence
    ,CASE 
        WHEN OriginalClaimGroupSequence IS NULL THEN '?'
        ELSE LEFT(OriginalClaimGroupSequence,1) 
     END AS AorR
    ,CASE 
        WHEN OriginalClaimGroupSequence IS NULL THEN -1
        WHEN LEFT(OriginalClaimGroupSequence,1)  = 'R' THEN 0
        WHEN LEFT(OriginalClaimGroupSequence,1)  = 'A' THEN 1
     END AS AorRWeight
    ,CAST(
     CASE 
        WHEN OriginalClaimGroupSequence IS NULL THEN '0'
        ELSE REPLACE(OriginalClaimGroupSequence, LEFT(OriginalClaimGroupSequence,1),'')
     END AS INT) AS SequenceNumber
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
FROM OriginalClaimGroupGeneration
),
FinalGoldenClaim AS(
--- RowNumber 1 is the golden claim  for the OriginalClaimGroup ---
SELECT 
     ClaimNumber
    ,CONCAT(COALESCE(OriginalClaimGroup,''),'-',COALESCE(FileLayoutID,''),'-',COALESCE(ClientID,'')) AS GeneratedGoldenClaimsUniqueKey
    ,GeneratedMedicalClaimsUniqueKey
    ,SourceName
    ,IsRiskAdjustable
    ,IsTeleHealth
    ,IsRiskAdjustableSource
    ,LoadTimestamp
    ,FileLayoutID
    ,FileLayoutDescription
    ,ClientId
    ,OriginalClaimGroup AS OriginalClaimNumber
    ,OriginalClaimGroupSequence
    ,AorR
    ,AorRWeight
    ,SequenceNumber
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
    ,ROW_NUMBER() OVER(PARTITION BY OriginalClaimGroup ORDER BY SequenceNumber DESC, AorRWeight DESC) AS RowNumber -- Your golden claim basically (where RowNumber = 1 is the golden claim)
FROM ClaimGroupingLevel
)
SELECT *
FROM FinalGoldenClaim
WHERE
RowNumber = 1
"""

  GoldenClaimDF = spark.sql(GoldenClaimQuery)
  GoldenClaimDF.createOrReplaceTempView("FinalGoldenClaim")
  #Insert into GoldenClaim
  InsertGC()

  returnStr = "GoldenClaim tables refreshed!"
else:
  #add more info to see why gc not run
  returnStr = "GoldenClaim tables did not refresh because: \r\nNew claim files count: " + len(clmDF.collect()) +  "\r\n" + "OR the following tables did not exist" + ' '.join(failedTablesList) +"\r\n"

# COMMAND ----------

# DBTITLE 1,Exit notebook -- return back to caller
dbutils.notebook.exit(returnStr)

# COMMAND ----------

# DBTITLE 1,Keep this cell here for an example -- OriginalClaimNumber not recieved but A1 and R1 have been recieved
# MAGIC %sql
# MAGIC --Note OriginalClaimNumber we may have not recieved -- here is an example -- this will show the same in the golden claim as it does in MedicalClaimHeader
# MAGIC SELECT * 
# MAGIC FROM MedicalClaimHeader
# MAGIC WHERE
# MAGIC -- ClaimNumber = '20207E06022'
# MAGIC OriginalClaimNumber = '20207E06022'
