CREATE TABLE #clientCode.consolidated_ma_peccdistatus (
 ClientID string
,LoadDateTime date
,FileID int
,FileLayoutID int
,FileLayoutDescription string
,Client string
,Market string
,Metric string
,CDIStatus string
,CDIStatus_USE string
,CountFlag string
,FileLoadDate date
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/PECCDIStatus'