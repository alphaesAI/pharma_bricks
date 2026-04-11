CREATE TABLE #clientCode.platinum_dimQualityMeasure (
 qualityMeasureKey  int
,measureYear  int
,qualityMeasureCode string
,qualityMeasureName string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimQualityMeasure'