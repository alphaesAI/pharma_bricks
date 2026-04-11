CREATE TABLE #clientCode.consolidated_aca_medicalclaimline (
 FileID  string
,GeneratedMedicalClaimsUniqueKey  string
,ClaimLineNumber  int
,PayStatus  string
,AuthorizationNum  int
,COBPaidAmt  string
,AllowedAmt  string
,TotalChargeAmt  string
,CoinsuranceAmt  string
,DeductibleAmt  string
,PaidAmount  string
,DetailServiceDate date
,ServiceFromDate date
,ServiceToDate date
,ProcCode  string
,ProcMod1  string
,ProcMod2  string
,ProcMod3  string
,ProcMod4  string
,PlaceOfService  string
,MSDRG  string
,RevenueCode  string
,RenderingProviderID  string
,RenderingProviderNPI  string
,RenderingProviderTIN  string
,RenderingProviderSpecialtyCode  string
) USING delta LOCATION '/mnt/#clientCode/consolidated/ACA/Data/MedicalClaimLine'