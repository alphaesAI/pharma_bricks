CREATE TABLE #clientCode.gold_ma_demographicriskscore  (
ClientID string
,FileID integer
,LoadDateTime date
,FileLayoutID integer
,FileLayoutDescription string
,PlanMemberID string
,GenderCode string
,MemberAge integer
,RiskAdjustmentFactorTypeCode string
,MedicaidIndicator string
,OREC boolean
,MedicaidDualStatusCode string
,Hospice string
,ESRD string
,IsLatest boolean
,DemographicRiskAdjustmentFactor string
,ProgramYear string
,ProgramYearMonth string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Risk/DemographicRiskScore'