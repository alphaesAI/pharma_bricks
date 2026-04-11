/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[Provider] 
(
	LoadDateTime datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       bigint  NOT NULL,
	ClientID     varchar(20)  NOT NULL,
	FileLayoutID       integer  NOT NULL,
	FileLayoutDescription  varchar(255)  NOT NULL,
	ProviderID varchar(50)  NULL,
	LastName varchar(150)  NULL,
	MiddleInitial  varchar(25)  NULL,
	FirstName  varchar(150)  NULL,
	TaxonomyCode1 varchar(10)  NULL,
	HpSpecialtyCode1 varchar(2)  NULL,
	ADVProviderSpecialtyCode1 varchar(10)  NULL,
	TaxonomyCode2 varchar(10)  NULL,
	HpSpecialtyCode2 varchar(2)  NULL,
	ADVProviderSpecialtyCode2 varchar(10)  NULL,
	TaxonomyCode3 varchar(10)  NULL,
	HpSpecialtyCode3 varchar(2)  NULL,
	ADVProviderSpecialtyCode3 varchar(10)  NULL,
	TaxonomyCode4 varchar(10)  NULL,
	HpSpecialtyCode4 varchar(2)  NULL,
	ADVProviderSpecialtyCode4 varchar(10)  NULL,
	TaxonomyCode5 varchar(10)  NULL,
	HpSpecialtyCode5 varchar(2)  NULL,
	ADVProviderSpecialtyCode5 varchar(10)  NULL,
	NPI varchar(10)  NULL,
	PrescribePrivilege varchar(1)  NULL,
	DEA varchar(25)  NULL,
	PayorID varchar(25)  NULL,
	Contracted varchar(1)  NULL,
	ProviderHAI varchar(1)  NULL,
	HospitalID varchar(25)  NULL,
	ExcludeFromProviderReporting varchar(1)  NULL,
	AltProvReporting1 varchar(100)  NULL,
	AltProvReporting2 varchar(100)  NULL,
	AltProvReporting3 varchar(100)  NULL,
	AltProvReporting4 varchar(100)  NULL,
	AltProvReporting5 varchar(100)  NULL,
	AltProvReporting6 varchar(100)  NULL,
	AltProvReporting7 varchar(100)  NULL,
	AltProvReporting8 varchar(100)  NULL,
	AltProvReporting9 varchar(100)  NULL,
	AltProvReporting10 varchar(100)  NULL,
	ProductID varchar(100)  NULL,
	ProviderType varchar(100)  NULL
)