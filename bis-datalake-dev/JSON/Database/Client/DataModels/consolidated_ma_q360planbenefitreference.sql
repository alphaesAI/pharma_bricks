CREATE TABLE #clientCode.consolidated_ma_q360planbenefitreference (
 ClientID  string
,FileID  int
,LoadDateTime date
,FileLayoutID  int
,FileLayoutDescription  string
,Client  string
,PlanGroupName  string
,PlanID  string
,PlanGroupID  string
,PlanSubGroup  string
,PBP  string
,PlanType  string
,PlanSubType  string
,Medical  string
,Pharmacy  string
,Dental  string
,Vision  string
,MH  string
,MHIP  string
,MHDN  string
,MHAMB  string
,CD  string
,CDIP  string
,CDDN  string
,CDAMB  string
) USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/Q360PlanBenefitReference'