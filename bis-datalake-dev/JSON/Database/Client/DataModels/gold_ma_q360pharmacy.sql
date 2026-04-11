CREATE TABLE #clientCode.gold_ma_q360pharmacy (
 MemberID  string
,DaysSupply  int
,ServiceDate  string
,NDCDrugCode  string
,ClaimStatus  string
,QuantityDispensed  string
,SupplementalData  string
,DataSourceName  string
,ProviderID  string
,ProviderNPI  string
,PharmacyNPI  string
,ClaimID  string
,ClaimLineID  string
,AdditionalColumn1  string
,AdditionalColumn2  string
,AdditionalColumn3  string
,AdditionalColumn4  string
,AdditionalColumn5  string
,Filler  string
,LoadDateTime  timestamp
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Q360/Q360Pharmacy'