CREATE TABLE #clientCode.consolidated_aca_provider (
 ClientID  string
,LoadDateTime  date
,FileID  bigint
,FileLayoutID  int
,FileLayoutDescription  string
,ProviderID  string
,NPI  string
,FirstName  string
,LastName  string
,MiddleInitial  string
,TaxonomyCode1  string
,DEA  string
,HpSpecialtyCode1  string
,PrescribePrivilege  string
,Contracted  string
,ProviderClass string
) USING delta LOCATION '/mnt/#clientCode/consolidated/ACA/Data/Provider'