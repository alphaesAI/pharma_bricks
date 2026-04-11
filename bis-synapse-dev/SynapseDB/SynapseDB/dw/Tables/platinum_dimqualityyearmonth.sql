CREATE TABLE [devidap1].[platinum_dimqualityyearmonth] 
(
	 qualityYearMonthKey  int NOT NULL PRIMARY KEY NONCLUSTERED (qualityYearMonthKey ASC) NOT ENFORCED
	,monthNumber int NOT NULL
	,monthName nvarchar(50) NOT NULL
	,yearNumber int NOT NULL
	,isRunout bit NOT NULL
)