CREATE TABLE #clientCode.consolidated_ma_hicnmbicrosswlk (
 ClientID  string
,FileID  int
,LoadDateTime date
,FileLayoutID  int
,FileLayoutDescription  string
,Contract  string
,PBP  string
,HICN  string
,MBI  string
,Surname  string
,FirstName  string
,DateOfBirth  int
,DateOfDeath  int
,Gender  string
,RecentEnrollmentDate  int
,RecentDisenrollmentDate  int
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/HICNMBICrossWlk'