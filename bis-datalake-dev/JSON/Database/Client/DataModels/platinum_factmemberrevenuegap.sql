CREATE TABLE #clientCode.platinum_factmemberrevenuegap (
 pecYearMonthKey  int
,clientKey  int
,memberKey BIGINT
,planID  string
,hccKey  int
,snapshotDateKey  int
,planProviderKey  int
,alertGroupKey  int
,isHCCClosed  string
,lastDCConfirmedDateKey  int
,lastPCPVisitDateKey  int
,lastAWVDateKey  int
,factMemberRevenueGapHashKey string
,fullRowHash string
,loadDateKey int
) USING delta LOCATION '/mnt/#clientCode/Platinum/factMemberRevenueGap'