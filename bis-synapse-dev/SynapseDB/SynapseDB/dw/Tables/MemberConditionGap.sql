CREATE TABLE [devidap1].[MemberConditionGap] ( 
	 [MemberID]	NVARCHAR(20)	NULL	
	,[MedicareBeneficiaryID]	NVARCHAR(15)	NULL	
	,[MedicaidID]	NVARCHAR(15)	NULL	
	,[PlanID]	NVARCHAR(20)	NULL	
	,[LastName]	NVARCHAR(50)	NULL	
	,[FirstName]	NVARCHAR(50)	NULL
	,[MiddleInitial]	NVARCHAR(10)	NULL
	,[DateOfBirth]	DATE	NULL	
	,[Gender]	NVARCHAR(1)	NULL	
	,[SuspectedHCC]	NVARCHAR(10)	NULL	
	,[HCCType]	NVARCHAR(10)	NULL	
	,[HCCVersion]	NVARCHAR (10)	NULL	
	,[EvidenceCodeValue]	NVARCHAR(20)	NULL	
	,[EvidenceCodeType]	NVARCHAR(50)	NULL	
	,[EvidenceCodeDescription]	NVARCHAR(256)	NULL	
	,[EvidenceDateOfService]	DATE	NULL	
	,[EvidenceCodeResult]	DECIMAL(10,4)	NULL	
	,[EvidenceIdentifier]	NVARCHAR(25)	NULL	
	,[ProbabilityScore]	DECIMAL(5,4)	NULL	
	,[SourceName]	NVARCHAR(20)	NULL	
	,[GapYear]	INT	NULL	
	,[GapType]	NVARCHAR (20)	NULL	
	,[LoadDateTime]	DATETIME2(7)	NOT NULL DEFAULT	'0001-01-01 00:00:00'
	,[FileID]	BIGINT	NOT NULL	
	,[ClientID]	NVARCHAR(20)	NOT NULL	
	,[FileLayoutID]	INTEGER	NOT NULL	
	,[FileLayoutDescription]	NVARCHAR(255)	NOT NULL	
)