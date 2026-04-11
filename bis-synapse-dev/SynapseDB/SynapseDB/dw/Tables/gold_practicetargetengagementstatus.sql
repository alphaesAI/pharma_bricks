CREATE TABLE [devidap1].[gold_practicetargetengagementstatus]
( 
	 [clientCode] nvarchar(20) NOT NULL PRIMARY KEY NONCLUSTERED ([clientCode] ASC,[pecProgramYear] ASC,[practiceCode] ASC) NOT ENFORCED
	,[pecProgramYear] int NOT NULL
	,[poCode] nvarchar(200)
	,[poName] nvarchar(510)
	,[practiceCode] nvarchar(200) NOT NULL
	,[practiceName] nvarchar(510)
	,[engagedDate] nvarchar(16)
	,[disengagedDate] nvarchar(16)
	,[targetedStatus] nvarchar(510)
	,[participationDecision] nvarchar(510)
	,[product] nvarchar(100)
	,[hashKey] int
) 