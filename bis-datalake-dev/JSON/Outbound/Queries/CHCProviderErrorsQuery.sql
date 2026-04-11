WITH ExportAudit AS (
SELECT MAX(CAST(SourceFileId AS LONG)) AS FileId
FROM ExportAudit
WHERE
SubClientCode = '#subClientCode'
AND
Entity = 'CHCProvider'
),
CHCPErrors AS (
SELECT 
     FileId
    ,HashOfRow
    ,CASE 
      WHEN ColumnName = "LastName" THEN "ProviderLastName" 
      WHEN ColumnName = "NPI" THEN "ProviderNPI" 
      ELSE ColumnName
     END AS ErrorColumnName
    ,ErrorCode
    ,ErrorDescription
    ,SourceFileName
FROM CHCProviderErrors
),
CHCProvider AS (
SELECT 
   FileId
  ,sha2(concat_ws("|", *), 256) AS HashOfRow
  ,ProviderID
  ,NPI AS ProviderNPI
  ,LastName AS ProviderLastName
FROM CHCProviderConsolidated
),
PFinal AS(
SELECT DISTINCT
   me.FileID
  ,me.SourceFileName AS FileName
  ,cp.ProviderID
  ,cp.ProviderNPI
  ,cp.ProviderLastName
  ,me.ErrorColumnName
  ,me.ErrorCode
  ,me.ErrorDescription
  ,current_timestamp() AS Loaddatetime
FROM CHCProvider cp
  INNER JOIN CHCPErrors me
    ON cp.FileId = me.FileId 
    AND cp.HashOfRow = me.HashOfRow
  INNER JOIN ExportAudit ea
    ON me.FileId = ea.FileId
),
CHCPHErrors AS (
SELECT 
     FileId
    ,HashOfRow
    ,ColumnName AS ErrorColumnName
    ,ErrorCode
    ,ErrorDescription
    ,SourceFileName
FROM CHCProviderHierarchyErrors
),
CHCProviderHierarchy AS (
SELECT 
   FileId
  ,sha2(concat_ws("|", *), 256) AS HashOfRow
  ,ProviderID
  ,ProviderNPI
  ,ProviderLastName
  ,LocationAddress1
FROM CHCProviderHierarchyConsolidated
),
PHFinal AS(
SELECT DISTINCT
   me.FileID
  ,me.SourceFileName AS FileName
  ,ph.ProviderID
  ,ph.ProviderNPI
  ,ph.ProviderLastName
  ,ph.LocationAddress1
  ,me.ErrorColumnName
  ,me.ErrorCode
  ,me.ErrorDescription
  ,current_timestamp() AS Loaddatetime
FROM CHCProviderHierarchy ph
  INNER JOIN CHCPHErrors me
    ON ph.FileId = me.FileId 
    AND ph.HashOfRow = me.HashOfRow
  INNER JOIN ExportAudit ea
    ON me.FileId = ea.FileId
),
Final AS(
SELECT 
   coalesce(pf.FileID, phf.FileID) AS FileID
  ,coalesce(pf.FileName, phf.FileName) AS FileName
  ,coalesce(pf.ProviderID, phf.ProviderID) AS ProviderID
  ,coalesce(pf.ProviderNPI, phf.ProviderNPI) AS ProviderNPI
  ,coalesce(pf.ProviderLastName, phf.ProviderLastName) AS ProviderLastName
  ,phf.LocationAddress1 AS LocationAddress1
  ,coalesce(pf.ErrorColumnName, phf.ErrorColumnName) AS ErrorColumnName
  ,coalesce(pf.ErrorCode, phf.ErrorCode) AS ErrorCode
  ,coalesce(pf.ErrorDescription, phf.ErrorDescription) AS ErrorDescription
  ,coalesce(pf.Loaddatetime, phf.Loaddatetime) AS Loaddatetime
FROM PFinal pf
  FULL OUTER JOIN PHFinal phf
    ON pf.ProviderId = phf.ProviderId
),
EndResult AS(
SELECT DISTINCT 
   FileID
  ,FileName
  ,ProviderID
  ,ProviderNPI
  ,ProviderLastName
  ,LocationAddress1
  ,ErrorColumnName
  ,ErrorCode
  ,ErrorDescription
  ,Loaddatetime
FROM Final
)
SELECT  
   FileID
  ,FileName
  ,ProviderID
  ,ProviderNPI
  ,ProviderLastName
  ,LocationAddress1
  ,ErrorColumnName
  ,ErrorCode
  ,ErrorDescription
  ,Loaddatetime
FROM EndResult