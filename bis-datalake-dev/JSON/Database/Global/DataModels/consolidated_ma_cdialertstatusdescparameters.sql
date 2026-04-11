CREATE TABLE #clientCode.consolidated_ma_cdialertstatusdescparameters (
 ClientID string
,LoadDateTime date
,FileID bigint
,FileLayoutID int
,FileLayoutDescription string
,Client string
,Market string
,Metric string
,CDIAlertStatusDesc string
,CDIAlertStatusDesc_USE string
,CountFlag string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/CDIAlertStatusDescParameters'