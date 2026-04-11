CREATE TABLE #clientCode.gold_ma_memberpersonbridge (
 BISInternalPersonID string
,IsCurrent int
,UniqueRecord string
,FileLayoutID string
,FileId bigint
,LastName string
,FirstName string
,DateOfBirth string
,Gender string  
,PermanentAddressLine1 string 
,PhoneNumber string 
,PlanMemberID string
,BeneficiaryID string
,UniquePersonKey string
,hashKey string
,IsCurrentPlanMemberID int
,IsCurrentUniquePersonKey int
,IsOriginalMemberID int
,PMUP string
,IsCurrentPMUP int
)  USING delta LOCATION '/mnt/#clientCode/Gold/MA/Client/MemberPersonBridge'