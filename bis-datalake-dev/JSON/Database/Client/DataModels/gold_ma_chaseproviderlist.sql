CREATE TABLE #clientCode.gold_ma_chaseproviderlist (
 ProviderID  string
,NPI  string
,PracticeNPI  string
,ProviderFirstName  string
,ProviderLastName  string
,AddressLine1  string
,AddressLine2  string
,City  string
,State  string
,ZipCode  string
,PhoneNumber  string
,FaxNumber  string
,ContactPerson  string
,ProviderTIN  string
,TaxonomyCode  string
,Specialty  string
,CMSApproved  string
,RAApproved  string
,ProviderSourceID  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Client/ChaseProviderList'