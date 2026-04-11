CREATE TABLE [devidap1].[gold_ma_medicalgoldenclaimlineproccodes]
( 
	 [GeneratedGoldenClaimsUniqueKey] nvarchar(510) NULL
	,[GeneratedMedicalClaimsUniqueKey] nvarchar(510) NULL
	,[ClientID] nvarchar(20) NULL
	,[FileLayoutID] int NULL
	,[FileLayoutDescription] nvarchar(510) NULL
	,[ClaimNumber] nvarchar(200) NULL
	,[OriginalClaimNumber] nvarchar(200) NULL
	,[BeneficiaryID] nvarchar(60) NULL
	,[PlanMemberID] nvarchar(100) NULL
	,[LineNumber] nvarchar(20) NULL
	,[ProcCode] nvarchar(20) NULL
	,[ProcCodeType] nvarchar(10) NULL
	,[ProcMod1] nvarchar(10) NULL
	,[ProcMod2] nvarchar(10) NULL
	,[ProcMod3] nvarchar(10) NULL
	,[ProcMod4] nvarchar(10) NULL
	,[PrimaryPaidAmt] nvarchar(40) NULL
	,[RevenueCode] nvarchar(10) NULL
	,[PlaceOfService] nvarchar(10) NULL
	,[ServiceFromDate] date NULL
	,[ServiceToDate] date NULL
	,[IsRiskAdjustable] int NULL
	,[hashKey] int NULL
	,[UniquePersonKey] nvarchar(100) NULL
) 