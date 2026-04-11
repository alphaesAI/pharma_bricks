CREATE TABLE #clientCode.gold_cdialertworkflowexceptionoption (
 cdiAlertWorkflowExceptionOptionID  int
,exceptionOptionText  string
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/cdiAlertWorkflowExceptionOption'