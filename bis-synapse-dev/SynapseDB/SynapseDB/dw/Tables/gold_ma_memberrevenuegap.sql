CREATE TABLE [devidap1].[gold_ma_memberrevenuegap]
(  
	 [planMemberID] NVARCHAR(50) NULL
	,[hccNumber] NVARCHAR(10) NULL
	,[reportMonth] NVARCHAR(6) NULL
	,[clientCode] NVARCHAR(10) NULL
	,[memberFirstName] NVARCHAR(300) NULL
	,[memberLastName] NVARCHAR(300) NULL
	,[memberDOB] date NULL 
	,[hccVersion] NVARCHAR(10) NULL
	,[hccDescription] NVARCHAR(255) NULL
	,[providerID] NVARCHAR(50) NULL
	,[providerNPI] NVARCHAR(25) NULL
	,[providerLastName] NVARCHAR(300) NULL
	,[providerFirstName] NVARCHAR(300) NULL
	,[practiceCode] NVARCHAR(50) NULL
	,[practiceName] NVARCHAR(255) NULL
	,[market] NVARCHAR(25) NULL
	,[alertCategory] NVARCHAR(100) NULL
	,[closureReason] NVARCHAR(100) NULL
	,[lastDCConfirmedDate] date NULL 
	,[lastPCPVisitDate] date NULL 
	,[lastAWVDate] date NULL 
	,[snapshotDate] date NULL
	,[planID] nvarchar(100) NULL
	,[hashKey] NVARCHAR(255) NULL
) 