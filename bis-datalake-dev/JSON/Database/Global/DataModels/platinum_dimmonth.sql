CREATE TABLE #clientCode.platinum_dimmonth (
 monthKey  int
,monthNumber  int
,monthName  string
,yearNumber  int
,yearName  string
,quarterNumber  int
,quarterName  string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimMonth'