CREATE TABLE [devidap1].[gold_cdialertquerycode]
( 
	 [cdiAlertQueryCodeID] int  NOT NULL PRIMARY KEY NONCLUSTERED ([cdiAlertQueryCodeID] ASC) NOT ENFORCED
	,[cdiAlertQueryCodeDescription] nvarchar(200)
	,[isSelectable] bit
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
) 