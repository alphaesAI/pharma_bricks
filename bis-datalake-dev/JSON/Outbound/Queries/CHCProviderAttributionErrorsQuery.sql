WITH ExportAudit AS (
SELECT MAX(CAST(SourceFileId AS LONG)) AS FileId
FROM ExportAudit ea
WHERE
SubClientCode = '#subClientCode'
AND
Entity = 'CHCProviderAttribution'
),
CHCErrors AS (
SELECT 
     FileId
    ,HashOfRow
    ,ColumnName AS ErrorColumnName
    ,ErrorCode
    ,ErrorDescription
    ,SourceFileName
FROM CHCProviderAttributionErrors
),
CHCProviderAttribution AS (
SELECT 
   FileId
  ,sha2(concat_ws("|", *), 256) AS HashOfRow
  --,PlanMemberID
  ,UniquePersonKey
  ,ProviderID
  ,StartDate
  ,EndDate
FROM CHCProviderAttributionConsolidated
)
SELECT DISTINCT
   me.FileID
  ,me.SourceFileName AS FileName
  --,pa.PlanMemberID
  ,pa.UniquePersonKey
  ,pa.ProviderID
  ,pa.StartDate
  ,pa.EndDate
  ,me.ErrorColumnName
  ,me.ErrorCode
  ,me.ErrorDescription
  ,current_timestamp() AS Loaddatetime
FROM CHCProviderAttribution pa
  INNER JOIN CHCErrors me
    ON pa.FileId = me.FileId 
    AND pa.HashOfRow = me.HashOfRow
  INNER JOIN ExportAudit ea
    ON me.FileId = ea.FileId 