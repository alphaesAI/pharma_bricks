/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*//*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/

CREATE TABLE [devidap1].[Pharmacy] 
(
	LoadDateTime 				datetime2(7) NOT NULL DEFAULT '0001-01-01 00:00:00',
	FileID       				bigint  NOT NULL,
	ClientID     				varchar(20)  NOT NULL,
	FileLayoutID       			integer  NOT NULL,
	FileLayoutDescription  		varchar(255)  NOT NULL,
	UniquePersonKey 			varchar(50)  NULL,
	PlanMemberID 				varchar(50)  NULL,
	BeneficiaryID 				varchar(30)  NULL,
	ProviderID  				varchar(50)  NULL,
	ProviderNPI 				varchar(20)  NULL,
	ClaimNumber 				varchar(100)  NULL,
	ProductID 					varchar(50)  NULL,
	AmountCharged				varchar(30)  NULL,
	AmtEligible 				varchar(30)  NULL,
	AmountPaid 					varchar(30)  NULL,
	NDCCodeSTD 					varchar(100)  NULL,
	RxFillDate 					date         NULL,
	RxDaysSupply 				integer     NULL,
	RXNorm						varchar(20) NULL,
	CVX							varchar(20) NULL,
	RxCodeType					varchar(20) NULL,
	USCCode						varchar(30) NULL,
	GPI							varchar(20) NULL,
	GPIName						varchar(255) NULL,
	Quantity	 				decimal(15,3) NULL,
	UnitsOfMeasure				varchar(50) NULL,
	PrescriberNumber 			varchar(50) NULL,
	PrescriberID				varchar(50) NULL,
	DEANumber					varchar(50) NULL,
	ClaimStatus					varchar(5)  NULL,
	AdjudicationDate			varchar(15)  NULL,
	DispensingFee				varchar(30)  NULL,
	CoPay						varchar(30)  NULL,
	CoInsurance					varchar(30)  NULL,
	Deductible					varchar(30)  NULL,
	DispenseAsWritten			varchar(25) NULL,
	MailOrder					varchar(10) NULL,
	SalesTax					varchar(30)  NULL,
	PharmacyNPI					varchar(20) NULL,
	PrescriptionReferenceNumber varchar(50) NULL,
	PlaceOfService 				varchar(5) NULL,
	SuppliesClaim				varchar(5) NULL,
	ClaimSourceIndicator        varchar(5) NULL,
	AlternateKey1				varchar(255) NULL,
	AlternateKey2				varchar(255) NULL,
	ProviderSpecialty			varchar(20) NULL,
	SourceName					varchar(255) NULL,
	BackoutIndicator			varchar(255) NULL
)