CREATE TABLE #clientCode.gold_ma_q360lishist (
 RecordType  string
,MCOContractNumber  string
,PBPNumber  string
,BeneficiaryID  string
,Surname  string
,FirstName  string
,MiddleInitial  string
,Sex  string
,DateofBirth  int
,LowIncomePeriodStartDate  int
,LowIncomePeriodEndDate  int
,LIPSpercentage  string
,PremiumLISAmount  string
,LowIncomeCoPayLevelID  int
,BeneficiarySourceofSubsidyCode  string
,LISActivityFlag  string
,PBPStartDate  int
,NetPartDPremiumAmount  string
,ContractYear  int
,InstitutionalStatusIndicator  int
,PBPEnrollmentTerminationDate  int
,Filler  string
,LoadDateTime timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Q360/Q360LISHIST'