CREATE TABLE #clientCode.export_aca_chcmembererrors (
 FileId  long
,BatchId long
,ColumnName string
,ErrorCode string
,ErrorDescription string
,HashOfRow  string
,SourceFileName string
) USING delta LOCATION '/mnt/export#clientCode/BatchAuditErrors/ACA/CHCMemberErrors'