CREATE TABLE #clientCode.gold_cdialertquerycode (
 cdiAlertQueryCodeID  int
,cdiAlertQueryCodeDescription  string
,isSelectable  boolean
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/cdiAlertQueryCode'