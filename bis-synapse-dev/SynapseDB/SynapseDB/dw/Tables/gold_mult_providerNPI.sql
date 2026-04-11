CREATE TABLE [devidap1].[gold_mult_providerNPI]
( 
	 [NPI] nvarchar(50) NOT NULL PRIMARY KEY NONCLUSTERED ([NPI] ASC) NOT ENFORCED
	,[lastName] nvarchar(100)
	,[firstName] nvarchar(100) 
	,[middleName] nvarchar(100) 
	,[orgName] nvarchar(255)
	,[entityTypeDescription] nvarchar(100) 
	,[hashKey] int
)