CREATE TABLE [devidap1].[gold_ma_memberpersonbridge]
(
	 [BISInternalPersonID] nvarchar(255) NULL 
	,[IsCurrent] int NULL
	,[UniqueRecord] nvarchar(40) NULL 
	,[FileLayoutID] nvarchar(20) NULL 
	,[FileId] bigint NULL 
	,[LastName] nvarchar(300) NULL
	,[FirstName] nvarchar(300) NULL
	,[DateOfBirth] nvarchar(40) NULL 
	,[Gender] nvarchar(10) NULL 
	,[PermanentAddressLine1] nvarchar(250) NULL
	,[PhoneNumber] nvarchar(250) NULL
	,[PlanMemberID] nvarchar(20) NULL 
	,[BeneficiaryID] nvarchar(20) NULL 
	,[UniquePersonKey] nvarchar(40) NULL 
	,[hashKey] nvarchar(510) NULL 
	,[IsCurrentPlanMemberID] int NULL
	,[IsCurrentUniquePersonKey] int NULL
	,[IsOriginalMemberID] int NULL
	,[PMUP] nvarchar(65) NULL
	,[IsCurrentPMUP] int NULL
) 