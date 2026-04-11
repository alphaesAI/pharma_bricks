CREATE TABLE [devidap1].[gold_appointmenttype]
( 
	 [appointmentTypeID] int  NOT NULL PRIMARY KEY NONCLUSTERED ([appointmentTypeID] ASC) NOT ENFORCED
	,[appointmentTypeDescription] nvarchar(100)
	,[isDeleted] bit
	,[createdDateTime] datetime2(7)
	,[updatedDateTime] datetime2(7)
	,[hashKey] int
)