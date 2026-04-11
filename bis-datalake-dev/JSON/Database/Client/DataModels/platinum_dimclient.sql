CREATE TABLE #clientCode.platinum_dimclient (
 clientKey  int
,clientCode  string
,clientName  string
,subClientCode  string
,subClientName  string
) USING delta LOCATION '/mnt/#clientCode/Platinum/dimClient'