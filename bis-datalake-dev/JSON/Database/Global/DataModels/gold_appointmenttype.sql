CREATE TABLE #clientCode.gold_appointmenttype (
 appointmentTypeID  int
,appointmentTypeDescription  string
,isDeleted  boolean
,createdDateTime timestamp
,updatedDateTime timestamp
,hashKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/appointmentType'