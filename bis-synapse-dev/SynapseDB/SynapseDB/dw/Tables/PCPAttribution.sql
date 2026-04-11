/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[PCPAttribution] 
(
	 [FileId]	bigint NULL
	,[ClientId]	varchar(20) NULL
	,[FileLayoutID]	int NULL
	,[FileLayoutDescription]	varchar(255) NULL
	,[LoadDateTime]	datetime2(7) NULL
	,[UniquePersonKey]	varchar(50) NULL
	,[PlanMemberID]	varchar(50) NULL
	,[BeneficiaryID]	varchar(30) NULL
	,[MedicaidID]	varchar(30) NULL
	,[StartDate]	date NULL
	,[EndDate]	date NULL
	,[AdditionalSpanValue] varchar(20) NULL
	,[ProviderID]  varchar(50) NULL
	,[AltPCPReporting1]	varchar(255) NULL
	,[AltPCPReporting2]	varchar(255) NULL
	,[AltPCPReporting3]	varchar(255) NULL
	,[AltPCPReporting4]	varchar(255) NULL
	,[AltPCPReporting5]	varchar(255) NULL
	,[AltPCPReporting6]	varchar(255) NULL
	,[AltPCPReporting7]	varchar(255) NULL
	,[AltPCPReporting8]	varchar(255) NULL
	,[AltPCPReporting9]	varchar(255) NULL
	,[AltPCPReporting10] varchar(255) NULL
	,[SubscriberID]	varchar(50) NULL
	,[ProviderAddressSuffix] varchar(25) NULL
	,[ProviderEffDate] date NULL
	,[ProviderFirstName] varchar(100) NULL
	,[ProviderLastName] varchar(100) NULL
	,[ProviderMiddleInitial] varchar(100) NULL
	,[MemberFirstName] varchar(100) NULL
	,[MemberLastName] varchar(100) NULL
	,[MemberMiddleInitial] varchar(100) NULL
	,[MemberDOB] date NULL
	,[CMSContractNumber] varchar(20) NULL
	,[ProviderNPI] varchar(20) NULL
	,[ProviderTaxonomy] varchar(20) NULL
	,[ProviderTIN] varchar(20) NULL
	,[ProviderAddress1] varchar(100) NULL
	,[ProviderAddress2] varchar(100) NULL
	,[ProviderCity] varchar(100) NULL
	,[ProviderState] varchar(2) NULL
	,[ProviderZip] varchar(15) NULL
	,[ProviderCounty] varchar(50) NULL
	,[ProviderPhone] varchar(50) NULL
	,[ProviderFax] varchar(50) NULL
	,[ProviderEmail] varchar(100) NULL
	,[BillingProviderID] varchar(50) NULL
	,[BillingProviderLastName] varchar(100) NULL
	,[BillingProviderMiddleInitial] varchar(100) NULL
	,[BillingProviderFirstName] varchar(100) NULL
	,[BillingProviderNPI] varchar(20) NULL
	,[BillingProviderTIN] varchar(20) NULL
	,[Source] varchar(20) NULL
	,[BillingProviderAddressLine1] varchar(100) NULL
	,[BillingProviderAddressLine2] varchar(100) NULL
	,[BillingProviderCity] varchar(100) NULL
	,[BillingProviderState] varchar(2) NULL
	,[BillingProviderZip] varchar(15) NULL
	,[BillingProviderCountyCode] varchar(50) NULL
	,[BillingProviderPhoneNumber] varchar(50) NULL
	,[BillingProviderFaxNumber] varchar(50) NULL
	,[BillingProviderEmail] varchar(100) NULL
	,[FileGenerationDateTime] datetime2 NULL
)