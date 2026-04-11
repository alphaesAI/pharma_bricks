CREATE TABLE #clientCode.platinum_dimhcc (
 HCCNumber  string
,HCCDescription  string
,HCCVersion  string
,HCCType  string
,IsChronic  boolean
,EffectiveYear  int
,EffectiveDateStart date
,EffectiveDateEnd date
,hashKey  int
,hccKey  int
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimHCC'