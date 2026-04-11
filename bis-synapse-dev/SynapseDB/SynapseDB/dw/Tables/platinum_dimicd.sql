CREATE TABLE [devidap1].[platinum_dimicd]
(  
	 [icdKey] int NOT NULL PRIMARY KEY NONCLUSTERED ([icdKey] ASC) NOT ENFORCED
	,[icd] nvarchar(20)
	,[icdCodeType] nvarchar(4)
	,[icdFormatted] nvarchar(20)
	,[icdShortDescription] nvarchar(200)
	,[icdLongDescription] nvarchar(512)
	,[icdDisplayDescripton] nvarchar(512)
	,[icdEffectiveYear] int
	,[icdEffectiveStartDate] date
	,[icdEffectiveEndDate] date
	,[isChronic] bit
	,[isComplete] bit 
) 