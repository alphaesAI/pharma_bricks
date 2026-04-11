CREATE TABLE [devidap1].[gold_ma_providergroupreference]
( 
	 [reportMonth] nvarchar(12) NOT NULL PRIMARY KEY NONCLUSTERED ([reportMonth] ASC, [providerID] ASC, [clientCode] ASC) NOT ENFORCED
	,[providerID] nvarchar(100) NOT NULL
	,[clientCode] nvarchar(20) NOT NULL
	,[pecProgramYear] int NULL
	,[providerNPI] nvarchar(50) NULL
	,[providerTIN] nvarchar(50) NULL
	,[providerLastName] nvarchar(200) NULL
	,[providerFirstName] nvarchar(200) NULL
	,[providerMiddleInitial] nvarchar(100) NULL
	,[providerAddress1] nvarchar(510) NULL
	,[providerAddress2] nvarchar(510) NULL
	,[providerCity] nvarchar(200) NULL
	,[providerState] nvarchar(50) NULL
	,[providerZipCode] nvarchar(20) NULL
	,[providerSpecialtyDescription] nvarchar(200) NULL
	,[practiceCode] nvarchar(100) NULL
	,[practiceName] nvarchar(510) NULL
	,[practiceProgramType] nvarchar(200) NULL
	,[practiceEngagedDate] date NULL
	,[practiceDisengagedDate] date NULL
	,[practiceTargetedStatus] nvarchar(200) NULL
	,[practiceParticipationDecision] nvarchar(200) NULL
	,[poCode] nvarchar(100) NULL
	,[poName] nvarchar(510) NULL
) 