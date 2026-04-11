CREATE TABLE #clientCode.gold_icd (
 icdKey  int
,icd  string
,icdCodeType  string
,icdFormatted  string
,icdShortDescription  string
,icdLongDescription  string
,icdDisplayDescripton  string
,icdEffectiveYear  int
,icdEffectiveStartDate date
,icdEffectiveEndDate date
,isChronic  boolean
,isComplete  boolean
) USING delta LOCATION '/mnt/#clientCode/Gold/icd'