/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[Lab] 
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,
	UniquePersonKey varchar(50)  NULL,
	MemberNumber varchar(50)  NULL,
	ProviderID  varchar(50)  NULL,
	ClaimNumber  varchar(100)  NULL,
	ClaimLineNumber varchar(25)  NULL,
	ProviderNPI varchar(10)  NULL,
	LocationID varchar(50)  NULL,
	DOS date  NULL,
	ProductID varchar(50)  NULL,
	ProviderSpecialty varchar(255)  NULL,
	ClaimStatus varchar(5)  NULL,
	LabCode varchar(50)  NULL,
	BillingIden varchar(50)  NULL,
	ClientNumber varchar(50)  NULL,
	RefPCP varchar(10)  NULL,
	UPIN varchar(100)  NULL,
	DiagCode varchar(10)  NULL,
	OrderCode varchar(50)  NULL,
	OrderName varchar(100)  NULL,
	CPTCode varchar(10)  NULL,
	HCPCSCode varchar(10)  NULL,
	HCPCSModifier varchar(5)  NULL,
	SNOMEDCode varchar(25)  NULL,
	LOINCode varchar(15)  NULL,
	ResultCode varchar(50)  NULL,
	ResultName varchar(100)  NULL,
	ResultValue varchar(25)  NULL,
	ResultUnit varchar(25)  NULL,
	RefRangeLow varchar(25)  NULL,
	RefRangeHigh varchar(25)  NULL,
	RefRangeAlpha varchar(250)  NULL,
	Comments varchar(255)  NULL,
	ClaimSourceIndicator varchar(5)  NULL,
	DateEnd varchar(25)  NULL,
	SourceName varchar(100)  NULL		
)