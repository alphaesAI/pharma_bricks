CREATE TABLE #clientCode.platinum_dimalertgroup (
 alertGroupKey  int
,alertGroupCode  string
,alertGroupDescription  string
,displayText  string
,sortOrder  int
,isActive  boolean
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimAlertGroup'