CREATE TABLE #clientCode.consolidated_ma_duplicateprioritylookup (
 ClientID  string
,LoadDateTime date
,FileID  int
,FileLayoutID  int
,FileLayoutDescription  string
,CDIAlertStatusDesc  string
,AppointmentTypeDesc  string
,CDIStatus  string
,FinalRankStandard  string
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/DuplicatePriorityLookup'