CREATE TABLE [devidap1].[gold_ma_memberroster]
( 
	 [reportMonth] nvarchar(12) NOT NULL PRIMARY KEY NONCLUSTERED ([reportMonth] ASC, [planMemberID] ASC, [clientCode] ASC) NOT ENFORCED
	,[planMemberID] nvarchar(100) NOT NULL
	,[clientCode] nvarchar(20) NOT NULL
	,[providerID] nvarchar(100) NULL
	,[reportingLevel] nvarchar(100) NULL
	,[memberBeneficiaryID] nvarchar(60) NULL
	,[memberLastName] nvarchar(200) NULL
	,[memberFirstName] nvarchar(200) NULL
	,[memberMiddleName] nvarchar(100) NULL
	,[memberDOB] date NULL
	,[memberPhone] nvarchar(60) NULL
	,[providerNPI] nvarchar(50) NULL
	,[providerLastName] nvarchar(200) NULL
	,[providerFirstName] nvarchar(200) NULL
	,[providerMiddleName] nvarchar(100) NULL
	,[providerAddress1] nvarchar(510) NULL
	,[providerAddress2] nvarchar(510) NULL
	,[providerCity] nvarchar(200) NULL
	,[providerState] nvarchar(50) NULL
	,[providerZip] nvarchar(20) NULL
	,[providerPhone] nvarchar(60) NULL
	,[practiceCode] nvarchar(100) NULL
	,[practiceName] nvarchar(510) NULL
	,[poCode] nvarchar(100) NULL
	,[poName] nvarchar(510) NULL
	,[planID] nvarchar(100) NULL
	,[memberPlanEligibilityStartDate] date NULL
	,[isNewPECMember] bit NULL
	,[programType] nvarchar(60) NULL
	,[FileID] BIGINT NULL
	,[HashKey] nvarchar(510) NULL
) 