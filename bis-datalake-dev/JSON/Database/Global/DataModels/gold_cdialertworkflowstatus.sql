CREATE TABLE #clientCode.gold_cdialertworkflowstatus (
 cdiAlertWorkflowStatusID  int
,cdiAlertWorkflowStatusDescription  string
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/cdiAlertWorkflowStatus'