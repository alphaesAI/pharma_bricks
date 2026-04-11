CREATE TABLE #clientCode.gold_mult_providerNPI (
 NPI string
,lastName string
,firstName string
,middleName string
,orgName string
,entityTypeDescription string
,hashkey int
) USING delta LOCATION '/mnt/#clientCode/Gold/MULT/providerNPI'