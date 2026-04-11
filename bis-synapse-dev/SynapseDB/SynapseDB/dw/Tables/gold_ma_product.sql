CREATE TABLE [devidap1].[gold_ma_product] (
	 [ClientID] nvarchar(20) NULL
	,[FileID] int NULL
	,[LoadDateTime] date NULL
	,[FileLayoutID] int NULL
	,[FileLayoutDescription] nvarchar(255) NULL
	,[ProductID] nvarchar(255) NULL
	,[PlanID] nvarchar(255) NULL
	,[ProductLine] nvarchar(255) NULL
	,[PlanGroupID] nvarchar(255) NULL
	,[PlanGroupName] nvarchar(255) NULL
	,[PlanSubGroup] nvarchar(255) NULL
	,[PlanType] nvarchar(255) NULL
	,[PlanSubType] nvarchar(255) NULL
	,[StartDate] date NULL
	,[EndDate] date NULL
	,[PBP] nvarchar(255) NULL
	,[ECDSIndicator] nvarchar(255) NULL
	,[AlphaPrefix] nvarchar(255) NULL
	,[ProductType] nvarchar(255) NULL
	,[PlanMarketingName] nvarchar(255) NULL
	,[MarketCoverage] nvarchar(255) NULL
	,[NCQASubmissionID] nvarchar(255) NULL
	,[MetalLevel] nvarchar(255) NULL
	,[IssuerID] nvarchar(255) NULL
)