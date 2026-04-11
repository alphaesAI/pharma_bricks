CREATE TABLE #clientCode.consolidated_ma_demographicsriskscore (
 ClientID string
,LoadDateTime date
,FileID int
,FileLayoutID int
,FileLayoutDescription string
,PlanMemberID string
,GenderCode string
,MemberAge int
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
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/DemographicsRiskScore'