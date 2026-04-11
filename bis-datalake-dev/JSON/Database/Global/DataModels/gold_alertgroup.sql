CREATE TABLE #clientCode.gold_alertgroup (
 alertGroupID  int
,alertGroupCode  string
,alertGroupDescription  string
,displayText  string
,sortOrder  int
,isActive  boolean
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/alertGroup'