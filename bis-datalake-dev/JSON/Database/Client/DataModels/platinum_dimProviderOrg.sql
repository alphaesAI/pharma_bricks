CREATE TABLE #clientCode.platinum_dimProviderOrg (
 providerOrgKey  string
,providerOrgID  string
,providerOrgName string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimProviderOrg'