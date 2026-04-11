WITH ExportAudit AS (
SELECT MAX(CAST(SourceFileId AS LONG)) AS FileId
FROM ExportAudit ea
WHERE
SubClientCode = '#subClientCode'
AND
Entity = 'ACAMemberConditionGap'
),
CHCErrors AS (
SELECT 
     FileId
    ,HashOfRow
    ,ColumnName AS ErrorColumnName
    ,ErrorCode
    ,ErrorDescription
    ,SourceFileName
FROM CHCMemberConditionGapErrors
),
CHCMemberConditionGap AS (
SELECT 
   FileId
  ,sha2(concat_ws("|", *), 256) AS HashOfRow
  ,MemberID
  ,SuspectedHCC AS HCC
  ,HCCVersion
  ,HCCType
  ,GapYear
  ,GapType
  ,EvidenceDateOfService
  ,EvidenceCodeType
  ,EvidenceCodeValue
FROM CHCMemberConditionGapConsolidated
)
SELECT DISTINCT
	 cm.MemberID
	,cm.HCC
	,cm.HCCVersion
	,cm.HCCType
	,cm.GapYear
	,cm.GapType
	,cm.EvidenceDateOfService
	,cm.EvidenceCodeType
	,cm.EvidenceCodeValue
	,me.FileID
	,me.SourceFileName AS FileName
	,me.ErrorCode
	,me.ErrorDescription
FROM CHCMemberConditionGap cm
  INNER JOIN CHCErrors me
    ON cm.FileId = me.FileId 
    AND cm.HashOfRow = me.HashOfRow
  INNER JOIN ExportAudit ea
    ON me.FileId = ea.FileId 