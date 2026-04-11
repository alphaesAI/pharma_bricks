CREATE TABLE [devidap1].[gold_ma_provider]
(  
	 [ClientID] nvarchar(20) NOT NULL
	,[FileID] int NOT NULL
	,[LoadDateTime] date NOT NULL
	,[FileLayoutID] int NOT NULL
	,[FileLayoutDescription] nvarchar(255) NOT NULL
	,[ProviderID] nvarchar(100) NOT NULL PRIMARY KEY NONCLUSTERED ([ProviderID] ASC) NOT ENFORCED
	,[LastName] nvarchar(300) NULL
	,[MiddleInitial] nvarchar(20) NULL
	,[FirstName] nvarchar(300) NULL
	,[TaxonomyCode1] nvarchar(20) NULL
	,[HpSpecialtyCode1] nvarchar(20) NULL
	,[ADVProviderSpecialtyCode1] nvarchar(20) NULL
	,[TaxonomyCode2] nvarchar(20) NULL
	,[HpSpecialtyCode2] nvarchar(20) NULL
	,[ADVProviderSpecialtyCode2] nvarchar(20) NULL
	,[TaxonomyCode3] nvarchar(20) NULL
	,[HpSpecialtyCode3] nvarchar(20) NULL
	,[ADVProviderSpecialtyCode3] nvarchar(20) NULL
	,[TaxonomyCode4] nvarchar(20) NULL
	,[HpSpecialtyCode4] nvarchar(20) NULL
	,[ADVProviderSpecialtyCode4] nvarchar(20) NULL
	,[TaxonomyCode5] nvarchar(20) NULL
	,[HpSpecialtyCode5] nvarchar(20) NULL
	,[ADVProviderSpecialtyCode5] nvarchar(20) NULL
	,[NPI] nvarchar(20) NULL
	,[PrescribePrivilege] nvarchar(20) NULL
	,[DEA] nvarchar(20) NULL
	,[PayorID] nvarchar(20) NULL
	,[Contracted] nvarchar(20) NULL
	,[ProviderHAI] nvarchar(20) NULL
	,[HospitalID] nvarchar(20) NULL
	,[ExcludeFromProviderReporting] nvarchar(20) NULL
	,[AltProvReporting1] nvarchar(200) NULL
	,[AltProvReporting2] nvarchar(200) NULL
	,[AltProvReporting3] nvarchar(200) NULL
	,[AltProvReporting4] nvarchar(200) NULL
	,[AltProvReporting5] nvarchar(200) NULL
	,[AltProvReporting6] nvarchar(200) NULL
	,[AltProvReporting7] nvarchar(200) NULL
	,[AltProvReporting8] nvarchar(200) NULL
	,[AltProvReporting9] nvarchar(200) NULL
	,[AltProvReporting10] nvarchar(200) NULL
	,[ProductID] nvarchar(100) NULL
	,[ProviderType] nvarchar(100) NULL
	,[HashKey] int NULL
) 