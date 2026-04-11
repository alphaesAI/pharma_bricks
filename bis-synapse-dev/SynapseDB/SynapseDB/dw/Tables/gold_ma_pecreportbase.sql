CREATE TABLE [devidap1].[gold_ma_pecreportbase]
( 
	 [reportMonth] nvarchar(12)  NOT NULL PRIMARY KEY NONCLUSTERED ([reportMonth] ASC, [planMemberID] ASC, [clientCode] ASC) NOT ENFORCED
	,[planMemberID] nvarchar(100) NOT NULL
	,[clientCode] nvarchar(20) NOT NULL
	,[reportPeriod] nvarchar(12) NULL
	,[providerID] nvarchar(255) NULL
	,[providerNPI] nvarchar(255) NULL
	,[providerName] nvarchar(255) NULL
	,[poCode] nvarchar(255) NULL
	,[poName] nvarchar(255) NULL
	,[practiceCode] nvarchar(255) NULL
	,[practiceName] nvarchar(255) NULL
	,[engagement] nvarchar(255) NULL
	,[market] nvarchar(255) NULL
	,[groupName] nvarchar(255) NULL
	,[groupNumber] nvarchar(255) NULL
	,[isActive] nvarchar(25) NULL
	,[isMidYearNewMember] nvarchar(25) NULL
	,[loadDate] date NULL
	,[ageModel] nvarchar(10) NULL
	,[metalLevel] nvarchar(20) NULL
	,[lineOfBusiness] nvarchar(20) NULL
	,[businessEntity] nvarchar(20) NULL
	,[isMemberTargeted] nvarchar(2) NULL
	,[relationship] nvarchar(20) NULL
	,[planID] nvarchar(50) NULL
	,[hashKey] nvarchar(510) NULL
) 

