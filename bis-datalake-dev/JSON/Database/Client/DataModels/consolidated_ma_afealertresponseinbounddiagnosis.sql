CREATE TABLE #clientCode.consolidated_ma_afealertresponseinbounddiagnosis (
 ClientID string
,LoadDateTime timestamp
,FileID bigint
,FileLayoutID int
,FileLayoutDescription string
,PlanMemberID string
,MemberLastName string
,MemberFirstName string
,MemberDOB string
,MRN string
,ProviderFirstName string
,ProviderLastName string
,PlanProviderID string
,ProviderNPI string
,PracticeID string
,PracticeName string
,VisitDate string
,Status string
,CodeSystem string
,DiagnosisCode string
,DiagnosisOrCondition string
,HCC string
,HccTypeVersion string
,Client string
,LOB string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/AFEAlertResponseInboundDiagnosis'