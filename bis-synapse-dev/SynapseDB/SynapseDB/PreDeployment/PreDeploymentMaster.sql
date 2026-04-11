/*
Pre-Deployment Script Template							
--------------------------------------------------------------------------------------
 This file contains SQL statements that will be appended to the build script.		
 Use SQLCMD syntax to include a file in the pre-deployment script.			
 Example:      :r .\myfile.sql								
 Use SQLCMD syntax to reference a variable in the pre-deployment script.		
 Example:      :setvar TableName MyTable							
               SELECT * FROM [$(TableName)]					
--------------------------------------------------------------------------------------
*/

--This is treated as one script combined
:r .\R2DropStatisticsforClaimWeight.sql

----This section is for release specific scripts.  Remove after the release.
--:r .\ReleaseScripts\21.06\IDAP-1849_SW_GCModel_Changes.sql
--:r .\ReleaseScripts\21.06\IDAP-1849_SW_GCHModel_Changes.sql
--:r .\IDAP-2296_DropTables.sql
--:r .\IDAP-1925_AlterAndTruncPharmacyTbl.sql
--:r .\BIS-47_TruncMedicalVision712Tbls.sql
--:r .\ReleaseScripts\SR_32_20230628_Release\BIS-4718_TruncCDIAlertline.sql
--:r .\ReleaseScripts\SR_32_20230628_Release\BIS-5355_TruncMemberPersonBridge.sql
--:r .\ReleaseScripts\SR_35_Release\BIS-4632_SW_DropACAMedicalClaims.sql
--:r .\ReleaseScripts\SR_35_Release\BIS-6185_DS_DropCMSTables.sql
--:r .\ReleaseScripts\SR_36_Release\BIS-6351_PL_TruncateDimQualityYearMonth.sql