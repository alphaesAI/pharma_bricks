CREATE TABLE #clientCode.gold_cdialertqueryresponse (
 cdiAlertQueryResponseID  int
,cdiAlertQueryResponseDescription  string
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/cdiAlertQueryResponse'