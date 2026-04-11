CREATE TABLE [devidap1].[gold_icdhccxref]
( 
	 [icd] nvarchar(20) NOT NULL PRIMARY KEY NONCLUSTERED ([icd] ASC,[icdCodeType] ASC,[icdEffectiveYear] ASC,[hccNumber] ASC,[hccVersion] ASC,[hccType] ASC,[hccEffectiveYear] ASC,[effectiveStartDate] ASC,[effectiveEndDate] ASC) NOT ENFORCED
	,[icdCodeType] nvarchar(4) NOT NULL
	,[icdEffectiveYear] int NOT NULL
	,[hccNumber] nvarchar(20) NOT NULL
	,[hccVersion] nvarchar(20) NOT NULL
	,[hccType] nvarchar(20) NOT NULL
	,[hccEffectiveYear] int NOT NULL
	,[isPrimary] bit
	,[effectiveStartDate] date NOT NULL
	,[effectiveEndDate] date NOT NULL
	,[icdHCCKey] bigint
) 

 