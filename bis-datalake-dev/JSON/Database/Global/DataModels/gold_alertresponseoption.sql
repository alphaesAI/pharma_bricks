CREATE TABLE #clientCode.gold_alertresponseoption (
 alertResponseOptionID  int
,alertPromptID  int
,alertResponseType  string
,alertResponseOptionText  string
,displayCol  int
,sortOrder  int
,isActive  boolean
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/alertResponseOption'