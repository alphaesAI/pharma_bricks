CREATE TABLE #clientCode.consolidated_ma_pecpracticetargetengagementstatus (
 ClientID  string
,LoadDateTime date
,FileID  int
,FileLayoutID  int
,FileLayoutDescription  string
,Client  string
,PECProgramYear  string
,POCode  string
,POName  string
,PracticeCode  string
,PracticeName  string
,EngagedDate  string
,DisengagedDate  string
,TargetStatus  string
,ParticipationDecision  string
,Product  string
,FileLoadDate date
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/PECPracticeTargetEngagementStatus'