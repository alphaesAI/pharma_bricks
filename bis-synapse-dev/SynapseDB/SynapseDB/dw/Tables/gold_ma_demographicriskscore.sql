CREATE TABLE [devidap1].[gold_ma_demographicriskscore] 
( 
	ClientID nvarchar(20) NULL	
	,FileID  bigint  NULL
	,LoadDateTime  datetime2(7) NULL
	,FileLayoutID int  NULL
	,FileLayoutDescription  nvarchar(255) NULL
	,PlanMemberID nvarchar(50) NULL
	,GenderCode nvarchar(1) NULL
	,MemberAge int NULL
	,RiskAdjustmentFactorTypeCode nvarchar(5) NULL
	,MedicaidIndicator nvarchar(2) NULL
	,OREC bit NULL
	,MedicaidDualStatusCode nvarchar(2) NULL
	,Hospice nvarchar(2) NULL
	,ESRD nvarchar(2) NULL
	,IsLatest bit NULL
	,DemographicRiskAdjustmentFactor decimal(6,3) NULL
	,ProgramYear int NULL
	,ProgramYearMonth int NULL
)