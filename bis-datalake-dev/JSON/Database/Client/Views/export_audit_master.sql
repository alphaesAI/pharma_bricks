CREATE OR REPLACE VIEW #clientCode.export_audit_master AS
WITH eat AS(
SELECT 
   ExportAuditTrackingId
  ,Entity
  ,SourceFileId
  ,BatchId
  ,JSONFileName
  ,ExtractionDate
  ,SentToTopic
  ,LoadDateTime
  ,NDJSONCount
  ,ROW_NUMBER() OVER(PARTITION BY ExportAuditTrackingId ORDER BY LoadDateTime DESC) AS RowNumber
FROM #clientCode.export_audit_tracking
)
SELECT 
	 ea.ExportAuditTrackingId
	,ea.Entity
	,ea.SourceFileId
    ,ea.SourceFileName
	,ea.BatchId
    ,ea.TotalNumberOfBatches
	,ea.Layer
	,ea.LOB
	,ea.ClientCode
	,ea.SubClientCode 
    ,eat.JSONFileName
    ,eat.ExtractionDate
    ,eat.SentToTopic
    ,eat.NDJSONCount
FROM #clientCode.export_audit ea
  LEFT JOIN eat
    ON ea.ExportAuditTrackingId = eat.ExportAuditTrackingId
    AND eat.RowNumber = 1