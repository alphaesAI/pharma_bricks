CREATE TABLE #clientCode.platinum_dimqualityevent (
 qualityEventKey  int
,qualityEventDescription  string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimQualityEvent'