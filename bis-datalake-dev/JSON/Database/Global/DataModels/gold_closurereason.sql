CREATE TABLE #clientCode.gold_closurereason (
 closureReasonID  int
,closureReasonDescription  string
) USING delta LOCATION '/mnt/#clientCode/Gold/closureReason'