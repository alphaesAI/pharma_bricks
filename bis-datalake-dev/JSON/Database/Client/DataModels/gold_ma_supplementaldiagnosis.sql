CREATE TABLE #clientCode.gold_ma_supplementaldiagnosis (
 planMemberID  string
,dosYear  int
,hccNumber  string
,hccVersion  string
,evidenceSource  string
,serviceFromDate date
,serviceToDate date
,isChronic  boolean
,providerID  string
,hashKey  int
,ICD  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Risk/SupplementalDiagnosis'