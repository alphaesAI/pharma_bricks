CREATE TABLE #clientCode.consolidated_ma_revenueGapParameters (
 ClientID string
,LoadDateTime date
,FileID bigint
,FileLayoutID int
,FileLayoutDescription string
,Client string
,Market string
,ClientMarket string
,ConfigID string
,LockDownMonthStart string
,LockDownDayStart string
,LockDownMonthEnd string
,LockDownDayEnd string
,NotOnCurrentAlert string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/RevenueGapParameters'