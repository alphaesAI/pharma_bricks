CREATE TABLE [devidap1].[platinum_factgapsincare]
( 
	 gapsInCareID bigint NOT NULL PRIMARY KEY NONCLUSTERED (gapsInCareID ASC) NOT ENFORCED
	,qualityYearMonthKey bigint NULL
	,memberKey bigint NULL
	,qualityMeasureKey int NULL
	,qualityEventKey int NULL
	,numerCnt int NULL
	,denomCnt int NULL
	,dateOfServiceDateKey int NULL
	,gapsEventProviderKey  nvarchar(25) NULL
	,planProviderKey int NULL
	,providerNPIKey nvarchar(100) NULL
	,expectedRate decimal(28,10) NULL
	,serviceNeededByDateKey int NULL
	,pdc decimal(28,10) NULL
	,lastHBVal decimal(28,10) NULL
	,lastHBDateKey int NULL
	,lastBPDia int NULL
	,lastBPSys int NULL
	,claimNumber nvarchar(255) NULL
	,hbTest int NULL
	,fullRowHash nvarchar(256) NOT NULL
) 