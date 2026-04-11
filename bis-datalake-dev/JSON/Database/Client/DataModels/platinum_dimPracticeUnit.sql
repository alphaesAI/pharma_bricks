CREATE TABLE #clientCode.platinum_dimPracticeUnit (
 practiceUnitKey  string
,practiceUnitID  string
,practiceUnitName string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimPracticeUnit'