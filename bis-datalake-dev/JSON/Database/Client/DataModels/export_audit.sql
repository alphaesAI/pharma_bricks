CREATE TABLE #clientCode.export_audit (
 ExportAuditTrackingId string --Need to add this hash of the Entity / SourceFileId and BatchId
,Entity string
,SourceFileId string
,SourceFileName string
,BatchId integer
,Layer string
,LOB string
,ClientCode string
,SubClientCode string
,TotalNumberOfBatches integer
,LoadDateTime timestamp
) USING delta LOCATION '/mnt/export#clientCode/BatchAudit/export_audit'