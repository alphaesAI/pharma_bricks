/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[DemographicsRiskScore] 
( 
	 ClientID varchar(20) NOT NULL
	,LoadDateTime  datetime2(7) NOT NULL
	,FileID  bigint  NOT NULL
	,FileLayoutID int  NOT NULL
	,FileLayoutDescription  varchar(255) NOT NULL
	,PlanMemberID varchar(50) NULL
	,GenderCode varchar(1) NULL
	,MemberAge int NULL
	,RiskAdjustmentFactorTypeCode varchar(5) NULL
	,MedicaidIndicator varchar(2) NULL
	,OREC bit NULL
	,MedicaidDualStatusCode varchar(2) NULL
	,Hospice varchar(2) NULL
	,ESRD varchar(2) NULL
	,IsLatest bit NULL
	,DemographicRiskAdjustmentFactor decimal(6,3) NULL
	,ProgramYear int NULL
	,ProgramYearMonth int NULL
)