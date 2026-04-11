CREATE TABLE #clientCode.gold_ma_goldenclaim (
 GeneratedGoldenClaimsUniqueKey string
,GeneratedMedicalClaimsUniqueKey string
,ClientID string
,FileLayoutID int
,FileLayoutDescription string
,SourceName string
,ClaimNumber string
,OriginalClaimNumber string
,BeneficiaryID string
,PlanMemberID string
,UniquePersonKey string
,CMSContractNumber string
,BillTypeCode string
,ClaimTypeInd string
,ClaimStatus string
,ClaimProcessDate string
,IsRiskAdjustable int
,IsRiskAdjustableSource string
,IsTeleHealth int
,LoadTimestamp timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Client/GoldenClaim'