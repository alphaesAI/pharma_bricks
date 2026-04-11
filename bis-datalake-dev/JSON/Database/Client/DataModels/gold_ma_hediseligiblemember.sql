CREATE TABLE #clientCode.gold_ma_hediseligiblemember (
 BISInternalPersonID  string
,PlanMemberID  string
,UniquePersonKey  string
) USING delta LOCATION '/mnt/#clientCode/Gold/MA/Q360/HedisEligibleMember'