/*

Post-Deployment Script Template							

--------------------------------------------------------------------------------------

 This file contains SQL statements that will be appended to the build script.		

 Use SQLCMD syntax to include a file in the post-deployment script.			

 Example:      :r .\myfile.sql								

 Use SQLCMD syntax to reference a variable in the post-deployment script.		

 Example:      :setvar TableName MyTable							

               SELECT * FROM [$(TableName)]					

--------------------------------------------------------------------------------------

*/

DECLARE @DB_NAME VARCHAR(255) = DB_NAME()

DECLARE @Flag INT = 0



SELECT @Flag =  is_auto_create_stats_on

FROM sys.databases

WHERE name = @DB_NAME



IF @Flag = 0

BEGIN

EXEC('ALTER DATABASE ['+@DB_NAME+'] SET AUTO_CREATE_STATISTICS ON')

END