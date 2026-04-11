CREATE TABLE [devidap1].[platinum_dimdate]
(  
	 [dateKey] int NOT NULL PRIMARY KEY NONCLUSTERED ([dateKey] ASC) NOT ENFORCED
	,[date] date
	,[shortDateName] nvarchar(30)
	,[longDateName] nvarchar(50)
	,[yearNumber] int
	,[yearName] nvarchar(8)
	,[quarterKey] int
	,[quarterNumber] int
	,[quarterName] nvarchar(50)
	,[quarterOfYearNumber] int
	,[quarterOfYearName] nvarchar(50)
	,[monthKey] int
	,[monthNumber] int
	,[monthName] nvarchar(30)
	,[monthOfQuarterNumber] int
	,[monthOfQuarterName] nvarchar(30)
	,[monthOfYearShortName] nvarchar(20)
	,[weekKey] int
	,[weekNumber] int
	,[weekName] nvarchar(20)
	,[dayOfWeekNumber] int
	,[dayOfWeekName] nvarchar(30)
	,[dayOfYear] int
	,[isWorkDay] bit 
) 