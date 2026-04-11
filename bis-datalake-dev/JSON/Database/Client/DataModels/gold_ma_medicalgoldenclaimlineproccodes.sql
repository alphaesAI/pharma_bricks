CREATE TABLE #clientCode.gold_ma_medicalgoldenclaimlineproccodes (
 GeneratedGoldenClaimsUniqueKey  string
,GeneratedMedicalClaimsUniqueKey  string
,ClientID  string
,FileLayoutID  int
,FileLayoutDescription  string
,ClaimNumber  string
,OriginalClaimNumber  string
,BeneficiaryID  string
,PlanMemberID  string
,LineNumber  string
,ProcCode  string
,ProcCodeType  string
,ProcMod1  string
,ProcMod2  string
,ProcMod3  string
,ProcMod4  string
,PrimaryPaidAmt  string
,RevenueCode  string
,PlaceOfService  string
,ServiceFromDate date
,ServiceToDate date
,IsRiskAdjustable int
,hashKey  int
,UniquePersonKey  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Client/MedicalGoldenClaimLineProcCodes'