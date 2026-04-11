CREATE TABLE [devidap1].[platinum_dimProviderNPI]
(
 [providerNPIKey] nvarchar(100) NOT NULL PRIMARY KEY NONCLUSTERED ([providerNPIKey] ASC) NOT ENFORCED
,[NPI] nvarchar(50)
,[lastName] nvarchar(100)
,[firstName] nvarchar(100)
,[middleName] nvarchar(100)
,[orgName] nvarchar(255)
,[entityTypeDescription] nvarchar(100)
,[fullRowHash] nvarchar(100)
)