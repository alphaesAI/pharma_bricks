CREATE TABLE #clientCode.export_aca_chcproviderhierarchyerrors (
 FileId  long
,BatchId long
,ColumnName string
,ErrorCode string
,ErrorDescription string
,HashOfRow  string
,SourceFileName string
) USING delta LOCATION '/mnt/export#clientCode/BatchAuditErrors/ACA/CHCProviderHierarchyErrors'