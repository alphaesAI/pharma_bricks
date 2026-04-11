CREATE TABLE #clientCode.platinum_dimqualityyearmonth (
 qualityYearMonthKey  int
,monthNumber  int
,monthName string
,yearNumber int
,isRunout boolean
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimQualityYearMonth'