CREATE TABLE #clientCode.consolidated_ma_planxref (
 ClientID string
,LoadDateTime date
,FileID int
,FileLayoutID int
,FileLayoutDescription string
,PlanID string
,PlanDescription string
,IsActive string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/MA/Data/PlanXref'