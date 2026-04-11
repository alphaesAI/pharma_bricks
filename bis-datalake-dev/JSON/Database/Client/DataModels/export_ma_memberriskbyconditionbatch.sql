CREATE TABLE #clientCode.export_ma_memberriskbyconditionbatch (
 HashOfRow  string
,BatchId  long
,FileID long
,FileLayoutID  integer
,RowNumber  integer
,TotalNumberOfBatches integer
) USING delta LOCATION '/mnt/export#clientCode/BatchAudit/MA/MemberRiskByConditionBatch'