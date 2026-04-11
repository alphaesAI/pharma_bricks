CREATE TABLE #clientCode.gold_cdistatus (
 clientCode  string
,market  string
,metric  string
,cdiStatus  string
,cdiStatusUse  string
,countFlag  string
,hashkey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/cdiStatus'