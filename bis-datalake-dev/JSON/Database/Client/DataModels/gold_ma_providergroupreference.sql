CREATE TABLE #clientCode.gold_ma_providergroupreference (
 reportMonth  string
,providerID  string
,clientCode  string
,pecProgramYear  int
,providerNPI  string
,providerTIN  string
,providerLastName  string
,providerFirstName  string
,providerMiddleInitial  string
,providerAddress1  string
,providerAddress2  string
,providerCity  string
,providerState  string
,providerZipCode  string
,providerSpecialtyDescription string
,practiceCode  string
,practiceName  string
,practiceProgramType  string
,practiceEngagedDate date
,practiceDisengagedDate date
,practiceTargetedStatus  string
,practiceParticipationDecision  string
,poCode  string
,poName  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/PEC/providerGroupReference'