CREATE TABLE #clientCode.gold_ma_pecreportbase (
 reportMonth  string
,planMemberID  string
,clientCode  string
,reportPeriod  string
,providerID  string
,providerNPI  string
,providerName  string
,poCode  string
,poName  string
,practiceCode  string
,practiceName  string
,engagement  string
,market  string
,groupName  string
,groupNumber  string
,isActive  string
,isMidYearNewMember  string
,loadDate date
,ageModel  string
,metalLevel  string
,lineOfBusiness  string
,businessEntity  string
,isMemberTargeted  string
,relationship  string
,planID  string
,hashKey  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/PEC/pecReportBase'