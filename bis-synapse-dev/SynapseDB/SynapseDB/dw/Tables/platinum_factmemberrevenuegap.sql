CREATE TABLE [devidap1].[platinum_factmemberrevenuegap]
( 
	 pecYearMonthKey int NOT NULL PRIMARY KEY NONCLUSTERED (pecYearMonthKey ASC,clientKey ASC,memberKey ASC,hccKey ASC) NOT ENFORCED
	,clientKey int NOT NULL
	,memberKey bigint NOT NULL
	,planID nvarchar(40) NOT NULL
	,hccKey int NOT NULL
	,snapshotDateKey int NOT NULL
	,planProviderKey int NOT NULL
	,alertGroupKey int NOT NULL
	,isHCCClosed  nvarchar(2) NOT NULL
	,lastDCConfirmedDateKey int NOT NULL
	,lastPCPVisitDateKey int NOT NULL
	,lastAWVDateKey int NOT NULL
	,factMemberRevenueGapHashKey nvarchar(255) NOT NULL
	,fullRowHash nvarchar(255) NOT NULL
	,loadDateKey int NOT NULL
) 