CREATE TABLE [devidap1].[gold_ma_stars_clinical_pharmacy]	
(
	 [ClientID]  NVARCHAR(20)  NOT NULL
	,[FileID]  BIGINT  NOT NULL
	,[LoadDateTime]  DATETIME2  NOT NULL
	,[FileLayoutID]  INT  NOT NULL
	,[FileLayoutDescription]  NVARCHAR(255)  NOT NULL
	,[MBI]  NVARCHAR(50)  NOT NULL
	,[MemberID]  NVARCHAR(50)  NOT NULL
	,[DOB]  DATE  NOT NULL
	,[Gender]  NVARCHAR(30)  NOT NULL
	,[LIS]  NVARCHAR(10)  
	,[EnrollmentStart]  DATE  
	,[EnrollmentEnd]  DATE  
	,[DualEligible]  NVARCHAR(10)  
	,[Disability]  NVARCHAR(10)  
	,[DaysInIPDiab]  NVARCHAR(50)  
	,[DaysInSNFDiab]  NVARCHAR(50)  
	,[DiabPDCDenominator]  NVARCHAR(50)  
	,[DiabPDCNumerator]  NVARCHAR(50)  
	,[DiabPDCRate]  NVARCHAR(50)  
	,[DiabPDCDenominatorUnadj]  NVARCHAR(50)  
	,[DiabPDCNumeratorUnadj]  NVARCHAR(50)  
	,[DiabPDCRateUnadj]  NVARCHAR(50)  
	,[DiabNumeratorflag]  NVARCHAR(50)  
	,[DaysInIPRAS]  NVARCHAR(50)  
	,[DaysInSNFRAS]  NVARCHAR(50)  
	,[RASPDCDenominator]  NVARCHAR(50)  
	,[RASPDCNumerator]  NVARCHAR(50)  
	,[RASPDCRate]  NVARCHAR(50)  
	,[RASPDCDenominatorUnadj]  NVARCHAR(50)  
	,[RASPDCNumeratorUnadj]  NVARCHAR(50)  
	,[RASPDCRateUnadj]  NVARCHAR(50)  
	,[RASNumeratorflag]  NVARCHAR(50)  
	,[DaysInIPStatin]  NVARCHAR(50)  
	,[DaysInSNFStatin]  NVARCHAR(50)  
	,[StatinPDCDenominator]  NVARCHAR(50)  
	,[StatinPDCNumerator]  NVARCHAR(50)  
	,[StatinPDCRate]  NVARCHAR(50)  
	,[StatinPDCDenominatorUnadj]  NVARCHAR(50)  
	,[StatinPDCNumeratorUnadj]  NVARCHAR(50)  
	,[StatinPDCRateUnadj]  NVARCHAR(50)  
	,[StatinNumeratorflag]  NVARCHAR(50)  
	,[SUPDNumeratorFlag]  NVARCHAR(50)  
	,[RunID]  NVARCHAR(255)  NOT NULL
	,[YearMonth]  INT  NOT NULL
)