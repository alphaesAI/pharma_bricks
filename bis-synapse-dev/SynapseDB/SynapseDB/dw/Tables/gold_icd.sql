CREATE TABLE [devidap1].[gold_icd]
( 
	 [icdKey] int 
	,[icd] nvarchar(20) NOT NULL PRIMARY KEY NONCLUSTERED ([icd] ASC, [icdCodeType] ASC, [icdEffectiveYear] ASC) NOT ENFORCED
	,[icdCodeType] nvarchar(4) NOT NULL
	,[icdFormatted] nvarchar(20)
	,[icdShortDescription] nvarchar(200)
	,[icdLongDescription] nvarchar(512)
	,[icdDisplayDescripton] nvarchar(512)
	,[icdEffectiveYear] int  NOT NULL
	,[icdEffectiveStartDate] date
	,[icdEffectiveEndDate] date
	,[isChronic] bit
	,[isComplete] bit
) 
