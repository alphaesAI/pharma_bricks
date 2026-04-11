CREATE TABLE #clientCode.consolidated_ma_mao002 (
 ClientID  string
,FileID  int
,LoadDateTime date
,FileLayoutID  int
,FileLayoutDescription  string
,RecordType  string
,ReportID  string
,MedicareAdvantageContractID  string
,PlanEncounterID  string
,EncounterICN  string
,EncounterLineNumber  string
,EncounterStatus  string
,ErrorCode  int
,ErrorDescription  string
,ReportDate date
,TransactionDate date
,PrelimRAFlag  string
,PrelimReasonCode  string
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/MAO002'