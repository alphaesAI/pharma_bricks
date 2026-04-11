CREATE TABLE [devidap1].[gold_alertresponseoption]
( 
	 [alertResponseOptionID] int NOT NULL PRIMARY KEY NONCLUSTERED ([alertResponseOptionID] ASC) NOT ENFORCED
	,[alertPromptID] int
	,[alertResponseType] nvarchar(30)
	,[alertResponseOptionText] nvarchar(1000)
	,[displayCol] int
	,[sortOrder] int
	,[isActive] bit
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
) 
