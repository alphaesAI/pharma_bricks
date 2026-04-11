CREATE TABLE #clientCode.platinum_dimclosurereason (
 closureReasonKey  int
,closureReasonDescription  string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimClosureReason'