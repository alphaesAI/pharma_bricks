CREATE TABLE #clientCode.gold_icdhccxref (
 icd  string
,icdCodeType  string
,icdEffectiveYear  int
,hccNumber  string
,hccVersion  string
,hccType  string
,hccEffectiveYear  int
,isPrimary  boolean
,effectiveStartDate date
,effectiveEndDate date
,icdHCCKey  int
) USING delta LOCATION '/mnt/#clientCode/Gold/icdHCCXref'