CREATE TABLE #clientCode.platinum_dimcdialertworkflowstatus (
 cdiAlertWorkflowStatusKey  int
,cdiAlertWorkflowStatusDescription  string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimCDIAlertWorkflowStatus'