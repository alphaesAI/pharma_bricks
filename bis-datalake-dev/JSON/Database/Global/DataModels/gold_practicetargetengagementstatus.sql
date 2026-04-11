CREATE TABLE #clientCode.gold_practicetargetengagementstatus (
 clientCode  string
,pecProgramYear  int
,poCode  string
,poName  string
,practiceCode  string
,practiceName  string
,engagedDate  string
,disengagedDate  string
,targetedStatus  string
,participationDecision  string
,product  string
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/practiceTargetEngagementStatus'