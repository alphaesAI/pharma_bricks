/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm
PROD - bcbsks, bcbsm
*/
CREATE TABLE [devidap1].[MAO002] 
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,	
	RecordType           varchar(1),
	ReportID           varchar(7),
	MedicareAdvantageContractID           varchar(5),
	PlanEncounterID           varchar(50),
	EncounterICN           varchar(50),
	PrelimRAFlag		varchar(5),
	PrelimReasonCode		varchar(5),
	EncounterLineNumber           varchar(3),
	EncounterStatus           varchar(8),
	ErrorCode           varchar(5),
	ErrorDescription           varchar(50),
	ReportDate           date,
	TransactionDate           date
)