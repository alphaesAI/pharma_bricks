/*
 Pre-Deployment Script Template							
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be executed before the build script.	
 Use SQLCMD syntax to include a file in the pre-deployment script.			
 Example:      :r .\myfile.sql								
 Use SQLCMD syntax to reference a variable in the pre-deployment script.		
 Example:      :setvar TableName MyTable							
               SELECT * FROM [$(TableName)]					
--------------------------------------------------------------------------------------
*/
DECLARE @DB_NAME VARCHAR(255) = DB_NAME()

DECLARE @Flag INT = 0


SELECT @Flag =  is_auto_create_stats_on
FROM sys.databases
WHERE name = @DB_NAME   

IF @Flag = 1
BEGIN

EXEC('ALTER DATABASE ['+@DB_NAME+'] SET AUTO_CREATE_STATISTICS OFF')

Declare @val Varchar(MAX); 
Select @val = STRING_AGG(ISNULL(statistics_name, ''), '; ')
FROM (SELECT 'DROP STATISTICS ' + sch.name + '.' + t.name + '.' + s.name AS statistics_name
		FROM sys.stats AS s  
		INNER JOIN sys.stats_columns AS sc   
			ON s.object_id = sc.object_id AND s.stats_id = sc.stats_id  
		INNER JOIN sys.columns AS c   
			ON sc.object_id = c.object_id AND c.column_id = sc.column_id  
		INNER JOIN sys.tables AS t
			ON t.OBJECT_ID = c.OBJECT_ID
		INNER JOIN sys.schemas AS sch
			ON t.schema_id = sch.schema_id
		WHERE c.name = 'ClaimWeight'
		AND s.name like '%_WA_Sys_%') q 		

Select @val;

EXEC(@val)

END