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

--This is treated as one script combined
:r .\R2ReEnableAutoStatistics.sql

----This section is for release specific scripts.  Remove after the release.
--:r .\ReleaseScripts\20.16\IDAP-966_LoadExistingDataNewSchema.sql
--:r .\ReleaseScripts\20.16\IDAP-1409_RemovingFileIDFromSynapseTable.sql
--:r .\ReleaseScripts\21.06\IDAP-1849_SW_GCModel_Changes.sql
--:r .\ReleaseScripts\21.06\IDAP-1849_SW_GCHModel_Changes.sql
--:r .\ReleaseScripts\21.07\IDAP-2123_DeleteDataInMember.sql
--:r .\IDAP-2296_DropTables.sql