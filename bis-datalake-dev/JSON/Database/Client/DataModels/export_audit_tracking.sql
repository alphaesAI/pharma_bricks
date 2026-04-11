CREATE TABLE #clientCode.export_audit_tracking (
 ExportAuditTrackingId string --Hash of Entity / SourceFileId and BatchId -- used to join 
,Entity string
,SourceFileId string
,BatchId integer
,JSONFileName string
,ExtractionDate timestamp
,SentToTopic boolean
,NDJSONCount integer
,LoadDateTime timestamp
) USING delta LOCATION '/mnt/export#clientCode/BatchAudit/export_audit_tracking'