CREATE TABLE #clientCode.gold_ma_q360lab (
 MemberID  string
,CPTCode  string
,LOINCCode  string
,TestResultValue  string
,DateOfService  string
,ProviderID  string
,DataSourceName  string
,AdditionalColumn1  string
,AdditionalColumn2  string
,AdditionalColumn3  string
,AdditionalColumn4  string
,AdditionalColumn5  string
,Filler  string
,LoadDateTime  timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Q360/Q360Lab'