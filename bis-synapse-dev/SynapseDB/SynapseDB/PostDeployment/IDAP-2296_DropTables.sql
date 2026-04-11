/*************************
IDAP-2296
This script is to drop ClaimHeader, ClaimLine, Vision837, DataMovementTracking from synapse db in all envs 
*************************/
IF OBJECT_ID('TEMPDB..#TablesList') IS NOT NULL DROP TABLE #TablesList

-- Gives list of tables from information schema

SELECT  ROW_NUMBER() OVER (ORDER BY Table_name) AS RowNumber,
Table_Schema + '.' + Table_name AS TableName
INTO #TablesList 
FROM INFORMATION_SCHEMA.TABLES WHERE Table_name IN ('DataMovementTracking','ClaimHeader','ClaimLine','Vision837')

DECLARE @Id INT
DECLARE @MaxCount INT
DECLARE @SQL  varchar(50)
DECLARE @TableName varchar(50)

SET @Id = 1

SELECT @MaxCount = COUNT(*) FROM #TablesList

WHILE @Id <= @MaxCount
BEGIN
SELECT @TableName = TableName FROM #TablesList
WHERE RowNumber = @Id

SET @SQL = 'DROP TABLE ' + @TableName
--drop tables ClaimHeader, ClaimLine, Vision837, DataMovementTracking
PRINT @SQL
EXEC (@SQL)

SET @Id = @Id + 1

END