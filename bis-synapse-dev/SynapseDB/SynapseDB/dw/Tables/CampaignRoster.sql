/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[CampaignRoster] 
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,	
	ClientName varchar(100)  NULL,
	POCode  varchar(100)  NULL,
	POName  varchar(255)  NULL,
	PracticeCode varchar(100)  NULL,
	PracticeName varchar(255)  NULL,
	ProviderFirstName varchar(100)  NULL,	
	ProviderMiddleName varchar(50)  NULL,
	ProviderLastName varchar(100)  NULL,
	ClientProviderID varchar(100)  NULL,
	ProviderNPI varchar(10)  NULL,
	ClientMemberID varchar(100)  NULL,
	SPClientMemberLookup varchar(100)  NULL,
	BeneficiaryID varchar(30)  NULL,
	MemberFirstName varchar(100)  NULL,
	MemberMiddleName varchar(50)  NULL,
	MemberLastName varchar(100)  NULL,
	MemberDOB varchar(15)  NULL,
	EligibleForReview varchar(25)  NULL,
	MRRScannedFileName varchar(8000)  NULL,
	MRRScannedStatus varchar(100)  NULL,
	PracticeRetrievalType varchar(100)  NULL,
	PracticeImplementationYear varchar(15)  NULL,
	PracticeAssignedPEC varchar(255)  NULL,
	ScanningCampaign varchar(100)  NULL,
	PriorYearDOSScannedPDFName varchar(8000)  NULL,
	PriorYearDOSScannedPDFCount varchar(15)  NULL,
	GroupingID varchar(100)  NULL,
	ScanningComments varchar(8000)  NULL,
	EngagedPractice  varchar(5)  NULL		
)