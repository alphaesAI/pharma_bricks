/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm
PROD - bcbsks, bcbsm
*/
CREATE TABLE [devidap1].[LISHIST]	
(
	[LoadDateTime] datetime2(7) NOT NULL, 
	[FileID]       bigint  NOT NULL,
	[ClientID]  varchar(20)  NOT NULL,
	[FileLayoutID]       integer  NOT NULL,
	[FileLayoutDescription]  varchar(255)  NOT NULL,
	[RecordType] varchar(1) NOT NULL,
	[MCOContractNumber] varchar(5) NOT NULL ,
	[PBPNumber]       varchar(3)  NOT NULL,
	[BeneficiaryID]  varchar(12)  NOT NULL,
	[Surname] varchar(12)  NOT NULL,
	[FirstName]        varchar(7)  NOT NULL,
	[MiddleInitial] varchar(1)  NULL,
	[Sex]                varchar(1)  NULL,
	[DateOfBirth]          integer  NULL,
	[LowIncomePeriodStartDate]  integer  NULL,
	[LowIncomePeriodEndDate]  integer  NULL,
	[LIPSPercentage]       varchar(3)  NULL,
	[PremiumLISAmount] decimal(7,2)  NULL,
	[LowIncomeCoPayLevelID]  integer  NOT NULL ,
	[BeneficiarySourceofSubsidyCode] varchar(1)  NULL,
	[LISActivityFlag]	varchar(1) NULL,
	[PBPStartDate]   integer  NULL,
	[NetPartDPremiumAmount]  decimal(7,2)  NULL,
	[ContractYear]       integer  NULL,
	[InstitutionalStatusIndicator]       integer  NULL,
	[PBPEnrollmentTerminationDate]         integer  NULL,
	[Filler]             varchar(56)  NULL
)