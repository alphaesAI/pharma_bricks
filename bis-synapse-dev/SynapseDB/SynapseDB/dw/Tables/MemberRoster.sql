CREATE TABLE [devidap1].[MemberRoster]
(
	 ClientID VARCHAR(20) NULL
	,LoadDateTime DATETIME2(7) NULL
	,FileID BIGINT NULL
	,FileLayoutID INT NULL
	,FileLayoutDescription VARCHAR(255) NULL
	,ClientName VARCHAR(10) NOT NULL
	,POCode VARCHAR(50) NOT NULL
	,POName VARCHAR(255) NOT NULL
	,PracticeCode VARCHAR(50) NOT NULL
	,PracticeName VARCHAR(255) NOT NULL
	,ProviderAddress1 VARCHAR(255) NOT NULL
	,ProviderAddress2 VARCHAR(255) NULL
	,ProviderCity VARCHAR(100) NULL
	,ProviderState VARCHAR(2) NULL
	,ProviderZipCode VARCHAR(10) NULL
	,ProviderFirstName VARCHAR(100) NULL
	,ProviderMiddleName VARCHAR(50) NULL
	,ProviderLastName VARCHAR(100) NULL
	,ProviderID VARCHAR(50) NULL
	,ProviderNPI VARCHAR(25) NOT NULL
	,ProviderPhoneNumber VARCHAR(30) NULL
	,ReportingLevel VARCHAR(50) NULL
	,PlanMemberID VARCHAR(50) NOT NULL
	,MemberMBI VARCHAR(30) NULL
	,MemberFirstName VARCHAR(100) NULL
	,MemberMiddleName VARCHAR(50) NULL
	,MemberLastName VARCHAR(100) NULL
	,MemberDOB date NULL
	,MemberPhoneNumber VARCHAR(30) NULL
	,PlanType VARCHAR(10) NULL
	,MemberPlanEligibilityStart date NULL
	,NewPECMember bit null
	,ProgramType VARCHAR(30) NULL
	,RosterMonth VARCHAR(6) NOT NULL
	,FileLoadDate DATETIME2 NOT NULL
)
