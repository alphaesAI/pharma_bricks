CREATE TABLE [devidap1].[gold_cdialertworkflowstatus]
( 
	 [cdiAlertWorkflowStatusID] int NOT NULL PRIMARY KEY NONCLUSTERED ([cdiAlertWorkflowStatusID] ASC) NOT ENFORCED
	,[cdiAlertWorkflowStatusDescription] nvarchar(100)
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
) 
