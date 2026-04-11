CREATE TABLE #clientCode.consolidated_aca_product (
 ClientID string
,FileID int
,LoadDateTime date
,FileLayoutID int
,FileLayoutDescription string
,ProductID string
,PlanID string
,ProductLine string
,PlanGroupID string
,PlanGroupName string
,PlanSubGroup string
,PlanType string
,PlanSubType string
,StartDate date
,EndDate date
,ECDSIndicator string
,AlphaPrefix string
,ProductType string
,PlanMarketingName string
,MarketCoverage string
,NCQASubmissionID string
,MetalLevel string
,IssuerID string
)  USING delta LOCATION '/mnt/#clientCode/consolidated/ACA/Data/Product'