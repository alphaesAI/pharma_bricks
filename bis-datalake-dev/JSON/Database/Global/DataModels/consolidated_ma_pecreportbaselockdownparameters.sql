CREATE TABLE #clientCode.consolidated_ma_pecreportbaselockdownparameters (
 ClientID string
,LoadDateTime date
,FileID bigint
,FileLayoutID int
,FileLayoutDescription string
,Client string
,ID  int
,Type  string
,LockDownReportBase  int
,LastDynamicRosterMonth string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/PecReportbaseLockdownParameters'