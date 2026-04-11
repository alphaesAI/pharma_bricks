CREATE TABLE [devidap1].[StarsClinicalPharmacy] 
(
	[ClientID] varchar(20) NOT NULL
	,[FileID] bigint NOT NULL
	,[LoadDateTime] datetime2(7) NOT NULL
	,[FileLayoutID] int NOT NULL
	,[FileLayoutDescription] varchar(255) NOT NULL
	,[MBI] nvarchar(50) NOT NULL
	,[MemberID] nvarchar(50) NOT NULL
	,[DOB] Date NOT NULL
	,[Gender] nvarchar(30) NOT NULL
	,[LIS] nvarchar(10) NOT NULL
	,[EnrollmentStart] Date NOT NULL
	,[EnrollmentEnd] Date NOT NULL
	,[DualEligible] nvarchar(10) NULL
	,[Disability] nvarchar(10) NULL
	,[DaysInIPDiab] nvarchar(50) NULL
	,[DaysInSNFDiab] nvarchar(50) NULL
	,[DiabPDCDenominator] nvarchar(50) NULL
	,[DiabPDCNumerator] nvarchar(50) NULL
	,[DiabPDCRate] nvarchar(50) NULL
	,[DiabPDCDenominatorUnadj] nvarchar(50) NULL
	,[DiabPDCNumeratorUnadj] nvarchar(50) NULL
	,[DiabPDCRateUnadj] nvarchar(50) NULL
	,[DiabNumeratorflag] nvarchar(50) NULL
	,[DaysInIPRAS] nvarchar(50) NULL
	,[DaysInSNFRAS] nvarchar(50) NULL
	,[RASPDCDenominator] nvarchar(50) NULL
	,[RASPDCNumerator] nvarchar(50) NULL
	,[RASPDCRate] nvarchar(50) NULL
	,[RASPDCDenominatorUnadj] nvarchar(50) NULL
	,[RASPDCNumeratorUnadj] nvarchar(50) NULL
	,[RASPDCRateUnadj] nvarchar(50) NULL
	,[RASNumeratorflag] nvarchar(50) NULL
	,[DaysInIPStatin] nvarchar(50) NULL
	,[DaysInSNFStatin] nvarchar(50) NULL
	,[StatinPDCDenominator] nvarchar(50) NULL
	,[StatinPDCNumerator] nvarchar(50) NULL
	,[StatinPDCRate] nvarchar(50) NULL
	,[StatinPDCDenominatorUnadj] nvarchar(50) NULL
	,[StatinPDCNumeratorUnadj] nvarchar(50) NULL
	,[StatinPDCRateUnadj] nvarchar(50) NULL
	,[StatinNumeratorflag] nvarchar(50) NULL
	,[SUPDNumeratorFlag] nvarchar(50) NULL
	,[RunID] nvarchar(255) NOT NULL
)