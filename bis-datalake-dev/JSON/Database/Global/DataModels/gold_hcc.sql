CREATE TABLE #clientCode.gold_hcc (
 HCCNumber  string
,HCCDescription  string
,HCCVersion  string
,HCCType  string
,IsChronic  boolean
,EffectiveYear  int
,EffectiveDateStart date
,EffectiveDateEnd date
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/hcc'