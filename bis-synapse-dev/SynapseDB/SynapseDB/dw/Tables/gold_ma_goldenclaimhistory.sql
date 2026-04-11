CREATE TABLE [devidap1].[gold_ma_goldenclaimhistory]	
(
	[GeneratedGoldenClaimsUniqueKey] nvarchar(255) NOT NULL PRIMARY KEY NONCLUSTERED([GeneratedGoldenClaimsUniqueKey] ASC) NOT ENFORCED,
	[GeneratedMedicalClaimsUniqueKey] nvarchar(255) NOT NULL,
	[ClientID] nvarchar(40) NOT NULL,
	[FileLayoutID] int NOT NULL,
	[FileLayoutDescription] nvarchar(255) NOT NULL,
	[SourceName] nvarchar(50) NULL,
	[ClaimNumber] nvarchar(40) NOT NULL,
	[OriginalClaimNumber] nvarchar(40) NULL,
	[BeneficiaryID] nvarchar(25) NULL,
	[PlanMemberID] nvarchar(60) NULL,
	[UniquePersonKey] nvarchar(60) NULL,
	[CMSContractNumber] nvarchar(15) NULL,
	[BillTypeCode] nvarchar(10) NULL,
	[ClaimTypeInd] nvarchar(2) NULL,
	[ClaimStatus] nvarchar(2) NULL,
	[ClaimProcessDate] datetime2(7) NULL,
	[IsRiskAdjustable] int NULL,
	[IsRiskAdjustableSource] nvarchar(20) NULL,
	[IsTeleHealth] int NULL,
	[LoadTimestamp] datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00'
)