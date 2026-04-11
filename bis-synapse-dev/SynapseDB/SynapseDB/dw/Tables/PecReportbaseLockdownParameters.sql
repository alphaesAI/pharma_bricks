CREATE TABLE [devidap1].PecReportbaseLockdownParameters (
	 ClientID NVARCHAR(20) NULL
	,FileID BIGINT NULL
	,LoadDateTime DATETIME2(7) NULL
	,FileLayoutID INT NULL
	,FileLayoutDescription NVARCHAR(255) NULL
	,Client NVARCHAR(20) NULL
	,ID INT NULL
	,Type NVARCHAR(50) NULL
	,LockDownReportBase INT NULL
	,LastDynamicRosterMonth NVARCHAR(6) NULL	
)