CREATE TABLE #clientCode.platinum_dimProviderNPI (
 providerNPIKey string
,NPI string
,lastName string
,firstName string
,middleName string
,orgName string
,entityTypeDescription string
,fullRowHash string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimProviderNPI'