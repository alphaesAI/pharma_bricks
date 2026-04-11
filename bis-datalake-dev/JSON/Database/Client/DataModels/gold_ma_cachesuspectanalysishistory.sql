CREATE TABLE #clientCode.gold_ma_cachesuspectanalysishistory  (
 StatisticsID  int
,ReviewTypeID  int
,ReviewTypeDescription  string
,PlanMemberID  string
,ProviderID  string
,SuspectFor  string
,HCC  string
,HCCGroup  int
,RuleUsed  int
,SuspectType  int
,InsertedDate timestamp
,Weight  int
,RAF double
,IsSuspect  boolean
,WeightDesc  string
,RAGain double
,TrumpingHCC  string
,BaseRate double
,DiseaseSuspectPriority  string
,RecordType  string
,DOSYear  int
,EvidenceType  string
,EvidenceValue  string
,EvidenceResult  string
,EvidenceDate date
,HashKey  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Risk/CacheSuspectAnalysisHistory'