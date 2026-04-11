CREATE TABLE [devidap1].[gold_cdialertqueryresponse]
( 
	 [cdiAlertQueryResponseID] int NOT NULL PRIMARY KEY NONCLUSTERED ([cdiAlertQueryResponseID] ASC) NOT ENFORCED
	,[cdiAlertQueryResponseDescription] nvarchar(200)
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
) 
