CREATE TABLE [devidap1].[gold_cdialertworkflowexceptionoption]
( 
	 [cdiAlertWorkflowExceptionOptionID] int NOT NULL PRIMARY KEY NONCLUSTERED ([cdiAlertWorkflowExceptionOptionID] ASC) NOT ENFORCED
	,[exceptionOptionText] nvarchar(1000)
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
) 
