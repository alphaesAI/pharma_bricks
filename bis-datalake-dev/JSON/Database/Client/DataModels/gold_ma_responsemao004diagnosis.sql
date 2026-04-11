CREATE TABLE #clientCode.gold_ma_responsemao004diagnosis (
 PlanID  string
,BeneficiaryID  string
,EncounterICN  string
,OrigEncounterICN  string
,ClaimTypeInd  string
,ServiceFromdate date
,ServiceTodate date
,PlanSubmissionDate date
,TransactionDate date
,ICDCodeType  string
,icd  string
,AddDeleteFlag  string
,ClaimNumber  string
,OriginalClaimNumber  string
,ProgramID string
,ProjectID string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Risk/ResponseMAO004Diagnosis'