/*replace the "devidap1" schema with client names for each environment:
DEV - devidap1, devidap2
QA - qaidap1,qaidap2
STAGE - bcbsks, bcbsm, vba, nbnd
PROD - bcbsks, bcbsm, vba, nbnd
*/
CREATE TABLE [devidap1].[ProviderHierarchy] 
(
ClientID varchar(20) NOT NULL
,LoadDateTime datetime2(7) NOT NULL
,FileID bigint  NOT NULL
,FileLayoutID int  NOT NULL
,FileLayoutDescription varchar(255) NOT NULL
,ProviderID varchar(50) NOT NULL
,ProviderLastName varchar(150) NULL
,ProviderNPI varchar(10) NULL
,LocationGroupID varchar(50) NULL
,LocationRanking int  NULL
,LocationIDType varchar(25) NULL
,LocationID varchar(50) NULL
,LocationDesc varchar(100) NULL
,LocationTIN varchar(25) NULL
,LocationAddress1 varchar(100) NULL
,LocationAddress2 varchar(100) NULL
,LocationCity varchar(100) NULL
,LocationState varchar(2) NULL
,LocationZip varchar(10) NULL
,CountyCode  varchar(10) NULL
,PhoneNumber varchar(20) NULL
,FaxNumber  varchar(20) NULL
,ContactPerson varchar(100) NULL
,DoNotChase varchar(1) NULL
,Tier2IDType varchar(50) NULL
,Tier2ID varchar(50) NULL
,Tier2Desc varchar(100) NULL
,Tier2Address1 varchar(100) NULL
,Tier2Address2 varchar(100) NULL
,Tier2City varchar(100) NULL
,Tier2State varchar(2) NULL
,Tier2Zip varchar(9) NULL
,Tier3IDType varchar(50) NULL
,Tier3ID varchar(50) NULL
,Tier3Desc varchar(100) NULL
,Tier3Address1 varchar(100) NULL
,Tier3Address2 varchar(100) NULL
,Tier3City varchar(100) NULL
,Tier3State varchar(2) NULL
,Tier3Zip varchar(9) NULL
,Tier4IDType varchar(50) NULL
,Tier4ID varchar(50) NULL
,Tier4Desc varchar(100) NULL
,Tier4Address1 varchar(100) NULL
,Tier4Address2 varchar(100) NULL
,Tier4City varchar(100) NULL
,Tier4State varchar(2) NULL
,Tier4Zip varchar(9) NULL
,StartDate date NULL
,EndDate date NULL
)