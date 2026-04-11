CREATE TABLE [devidap1].[gold_trumpinghcc]
( 
	 [trumpedHcc] nvarchar(20) NOT NULL PRIMARY KEY NONCLUSTERED ([trumpedHcc] ASC) NOT ENFORCED
	,[trumpingHcc] nvarchar(20)
	,[hccVersion] nvarchar(20) NULL
	,[hashKey] int
) 