/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[Product] 
(
 ClientID varchar(20) NOT NULL
,LoadDateTime datetime2(7) NOT NULL
,FileID bigint  NOT NULL
,FileLayoutID int  NOT NULL
,FileLayoutDescription varchar(255) NOT NULL
,ProductID varchar(50) NULL
,PlanID varchar(50) NULL
,ProductLine varchar(50) NULL
,PlanGroupID varchar(50) NULL
,PlanGroupName varchar(100) NULL
,PlanSubGroup varchar(20) NULL
,PlanType varchar(30) NULL
,PlanSubType varchar(30) NULL
,StartDate date NULL
,EndDate date NULL
,PBP varchar(30) NULL
,ECDSIndicator varchar(1) NULL
,AlphaPrefix varchar(10) NULL
,ProductType varchar(30) NULL
,PlanMarketingName varchar(100) NULL
,MarketCoverage varchar(2) NULL
,NCQASubmissionID varchar(5) NULL
,MetalLevel varchar(1) NULL
,IssuerID varchar(5) NULL
)