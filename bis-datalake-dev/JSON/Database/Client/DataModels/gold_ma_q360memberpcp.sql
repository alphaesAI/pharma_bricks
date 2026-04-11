CREATE TABLE #clientCode.gold_ma_q360memberpcp (
 MemberID  string
,ProviderID string
,StartDate string
,EndDate string
,AdditionalColumn1 string
,AdditionalColumn2 string
,AdditionalColumn3 string
,AdditionalColumn4 string
,AdditionalColumn5 string
,Filler string
,LoadDateTime  timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Q360/Q360MemberPCP'