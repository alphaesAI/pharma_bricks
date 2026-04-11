CREATE TABLE #clientCode.consolidated_ma_rollupparameters (
 ClientID string
,FileID int
,LoadDateTime date
,FileLayoutID int
,FileLayoutDescription string
,Client string
,RollUp string
,RollUpDesc string
,CountNAs string
,GapAddressedOnly string
,IsActive string
,MonthRunDay string
,SubClients string
,ApptLookback string
,LatestStatus string
,RunStatus string
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/RollUpParameters'