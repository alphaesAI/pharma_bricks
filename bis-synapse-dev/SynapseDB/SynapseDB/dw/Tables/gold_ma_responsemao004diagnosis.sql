CREATE TABLE [devidap1].[gold_ma_responsemao004diagnosis]
( 
	 [PlanID] nvarchar(100) NULL
	,[BeneficiaryID] nvarchar(60) NULL
	,[EncounterICN] nvarchar(40) NULL
	,[OrigEncounterICN] nvarchar(40) NULL
	,[ClaimTypeInd] nvarchar(2) NULL
	,[ServiceFromdate] date NULL
	,[ServiceTodate] date NULL
	,[PlanSubmissionDate] date NULL
	,[TransactionDate] date NULL
	,[ICDCodeType] nvarchar(4) NULL
	,[icd] nvarchar(20) NULL
	,[AddDeleteFlag] nvarchar(2) NULL
	,[ClaimNumber] nvarchar(200) NULL
	,[OriginalClaimNumber] nvarchar(200) NULL
	,[ProgramID] nvarchar(20) NULL
	,[ProjectID] nvarchar(20) NULL
) 