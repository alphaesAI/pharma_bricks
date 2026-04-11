CREATE TABLE [devidap1].[platinum_dimmonth]
(
	 [monthKey] int  NOT NULL PRIMARY KEY NONCLUSTERED ([monthKey] ASC) NOT ENFORCED
	,[monthNumber] int
	,[monthName] nvarchar(30)
	,[yearNumber] int
	,[yearName] nvarchar(8)
	,[quarterNumber] int
	,[quarterName] nvarchar(50)
) 