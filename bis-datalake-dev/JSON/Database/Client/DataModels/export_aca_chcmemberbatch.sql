CREATE TABLE #clientCode.export_aca_chcmemberbatch (
 HashOfRow  string
,BatchId  long
,FileID long
,FileLayoutID  integer
,RowNumber  integer
,TotalNumberOfBatches integer
) USING delta LOCATION '/mnt/export#clientCode/BatchAudit/ACA/CHCMemberBatch'