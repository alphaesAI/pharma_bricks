CREATE TABLE [devidap1].[gold_ma_supplementaldiagnosis]
( 
	 [planMemberID] nvarchar(100) NULL
	,[dosYear] int NULL
	,[hccNumber] nvarchar(20) NULL
	,[hccVersion] nvarchar(20) NULL
	,[evidenceSource] nvarchar(510) NULL
	,[serviceFromDate] date NULL
	,[serviceToDate] date NULL
	,[isChronic] bit NULL
	,[providerID] nvarchar(100) NULL
	,[hashKey] int NULL
	,[ICD] nvarchar(20) NULL
) 