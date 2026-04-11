/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[MemberEnrollment] 
(
	 [ClientID]	varchar(20) NULL
	,[FileID]	bigint NULL
	,[LoadDateTime]	datetime2(7) NULL
	,[FileLayoutID]	int NULL
	,[FileLayoutDescription]	varchar(255) NULL
	,[UniquePersonKey]	varchar(50) NULL
	,[PlanMemberID]	varchar(50) NULL
	,[BeneficiaryID]	varchar(30) NULL
	,[MedicaidID]	varchar(30) NULL
	,[StartDate]	date NULL
	,[EndDate]	date NULL
	,[CMSContractNumber]	varchar(50) NULL
	,[ProductLine]	varchar(50) NULL
	,[ProductID]	varchar(50) NULL
	,[SubscriberID]	varchar(50) NULL
	,[SecondProductID]	varchar(50) NULL
	,[AdditionalSpanValue]	varchar(30) NULL
	,[PBP]	varchar(30) NULL
	,[ECDSFlag]	varchar(1) NULL
	,[AlphaPrefix]	varchar(30) NULL
	,[Pharmacy]	varchar(1) NULL
	,[Dental]	varchar(1) NULL
	,[Vision]	varchar(1) NULL
	,[MH]	varchar(1) NULL
	,[MHIP]	varchar(1) NULL
	,[MHDN]	varchar(1) NULL
	,[MHAMB]	varchar(1) NULL
	,[CD]	varchar(1) NULL
	,[CDIP]	varchar(1) NULL
	,[CDDN]	varchar(1) NULL
	,[CDAMB]	varchar(1) NULL
	,[Hospice]	varchar(1) NULL
	,[SNP]	varchar(1) NULL
	,[SNPEnrolleeType]	int NULL
	,[IssuerID]	varchar(50) NULL
	,[MetalLevel]	varchar(15) NULL
	,[CostSharingVariant]	varchar(5) NULL
	,[MarketCoverage]	varchar(5) NULL
	,[CSREligibility]	varchar(1) NULL
	,[MemberEnrollmentQHPState]	varchar(2) NULL
	,[LongTermInstitution]	varchar(1) NULL
	,[PlanEmployee]	varchar(1) NULL
	,[MedicaidExpansionQHPEnrollee]	int NULL
	,[MemberGroupCode]	varchar(50) NULL
	,[AltSpanReporting1]	varchar(255) NULL
	,[AltSpanReporting2]	varchar(255) NULL
	,[AltSpanReporting3]	varchar(255) NULL
	,[AltSpanReporting4]	varchar(255) NULL
	,[AltSpanReporting5]	varchar(255) NULL
	,[AltSpanReporting6]	varchar(255) NULL
	,[AltSpanReporting7]	varchar(255) NULL
	,[AltSpanReporting8]	varchar(255) NULL
	,[AltSpanReporting9]	varchar(255) NULL
	,[AltSpanReporting10]	varchar(255) NULL
	,[Segment]	varchar(5) NULL
	,[HealthPlanClassID]	varchar(30) NULL
	,[HealthPlanCode]	varchar(15) NULL
	,[DisenrollmentReasonCode]	varchar(5) NULL
	,[SignatureDate]	varchar(8) NULL
	,[CSNPDisenrollmentEffDate]	varchar(8) NULL
	,[ElectionType]	varchar(500) NULL
	,[TermReasonCode] 	varchar(50) NULL
	,[SourcefileID] 	varchar(255) NULL
)