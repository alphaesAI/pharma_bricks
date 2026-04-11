CREATE TABLE #clientCode.consolidated_ma_afealertresponseinbound (
 ClientID  string
,LoadDateTime date
,FileID  int
,FileLayoutID  int
,FileLayoutDescription  string
,PlanMemberID  string
,MemberLastName  string
,MemberFirstName  string
,MRN  string
,ProviderFirstName  string
,ProviderLastName  string
,PlanProviderID  string
,ProviderNPI  string
,PracticeID  string
,PracticeName  string
,VisitDate date
,CDIAlertEntityID  int
,CDIAlertEntityDetailID  int
,SelectedAlertResponseOptionID  int
,Client  string
,LOB  string
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/AFEAlertResponseInbound'