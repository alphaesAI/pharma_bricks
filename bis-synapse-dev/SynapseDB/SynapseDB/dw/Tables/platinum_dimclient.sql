CREATE TABLE [devidap1].[platinum_dimclient]
( 
 [clientKey] int NOT NULL PRIMARY KEY NONCLUSTERED (clientKey ASC) NOT ENFORCED
,[clientCode] nvarchar(20)
,[clientName] nvarchar(200)
,[subClientCode] nvarchar(20)
,[subClientName] nvarchar(200)
) 