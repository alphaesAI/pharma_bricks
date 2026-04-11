WITH ExportAudit AS (
SELECT MAX(CAST(SourceFileId AS LONG)) AS FileId
FROM ExportAudit ea
WHERE
SubClientCode = '#subClientCode'
AND
Entity = 'CHCMember'
),
CHCErrors AS (
SELECT 
     FileId
    ,HashOfRow
    ,ColumnName AS ErrorColumnName
    ,ErrorCode
    ,ErrorDescription
    ,SourceFileName
FROM CHCMemberErrors
),
CHCMember AS (
SELECT 
   FileId
  ,sha2(concat_ws("|", *), 256) AS HashOfRow
  ,PlanMemberID
  ,BeneficiaryID
  ,FirstName
  ,LastName
  ,DateofBirth
FROM CHCMemberConsolidated
)
SELECT DISTINCT
   me.FileID
  ,me.SourceFileName AS FileName
  ,cm.PlanMemberID
  ,cm.BeneficiaryID
  ,cm.FirstName
  ,cm.LastName
  ,cm.DateOfBirth
  ,me.ErrorColumnName
  ,me.ErrorCode
  ,me.ErrorDescription
  ,current_timestamp() AS Loaddatetime
FROM CHCMember cm
  INNER JOIN CHCErrors me
    ON cm.FileId = me.FileId 
    AND cm.HashOfRow = me.HashOfRow
  INNER JOIN ExportAudit ea
    ON me.FileId = ea.FileId 