CREATE TABLE [devidap1].[gold_ma_q360GapsInCare]
( 
	 [YearMonth] int NOT NULL
	,[ClaimsThroughDate] nvarchar(30) NULL
	,[MemberID] nvarchar(30) NOT NULL
	,[MeasureCode] nvarchar(30) NULL
	,[MeasureName] nvarchar(255) NULL
	,[NumerCnt] int NOT NULL
	,[DenomCnt] int NOT NULL
	,[SubmeasureCode] nvarchar(30) NULL
	,[SubmeasureName] nvarchar(255) NULL
	,[EventName] nvarchar(255) NULL
	,[DateofService] date NULL
	,[Claimnumber] nvarchar(50) NULL
	,[ProviderID] nvarchar(50) NULL
	,[ProviderName] nvarchar(100) NULL
	,[ExpectedRate] nvarchar(50) NULL
	,[ServiceNeededByDate] date NULL
	,[PDC] nvarchar(50) NULL
	,[HBTest] int NULL
	,[LastHBVal] nvarchar(50) NULL
	,[LastHBDate] date NULL
	,[LastBPDia] int NULL
	,[LastBPSys] int NULL
	,[LastBPDate] date NULL
	,[Category] nvarchar(255) NULL
	,[Source] nvarchar(255) NULL
	,[DataLoadName] nvarchar(255) NULL
	,[DataFileName] nvarchar(255) NULL
	,[FileID] bigint NOT NULL
	,[RunID] nvarchar(255) NOT NULL
	,[LoadDateTime] datetime2(7) NOT NULL
)