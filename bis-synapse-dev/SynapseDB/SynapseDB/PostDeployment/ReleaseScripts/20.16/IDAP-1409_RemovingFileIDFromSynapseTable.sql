/*************************
This script is to remove fileid's from Config tables 
IDAP-1409
This script will remove the Kansas Config tables
*************************/


PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO REMOVE UNWANTED FILEID'
PRINT 'REMOVING FILEID FROM KANSAS'

GO
DECLARE @servername VARCHAR(30)
DECLARE @clientSchema VARCHAR(40)

SELECT @servername = SERVERPROPERTY('ServerName')

SET @clientSchema = CASE substring(@servername,7,1)
	WHEN 'd' THEN 'devidap1'
	WHEN 'q' THEN 'qaidap1'
	ELSE 'bcbsks'
	END

PRINT @servername
PRINT @clientSchema


IF substring(@servername,7,1) not in ('d','q','s') AND cast(getDate() as date) <= '2021-03-16'
BEGIN
--Delete the FIleID's data from synapse database table

DECLARE @DeleteClaimLineFileIDSQL VARCHAR(max)
SET @DeleteClaimLineFileIDSQL = 'DELETE cl FROM '+@clientSchema+'.ClaimLine cl join '+@clientSchema+'.ClaimHeader ch on ch.GeneratedClaimsUniqueKey = cl.GeneratedClaimsUniqueKey where ch.FileID = 167'

PRINT @DeleteClaimLineFileIDSQL
EXEC(@DeleteClaimLineFileIDSQL)

DECLARE @DeleteClaimHeaderFileIDSQL VARCHAR(max)
SET @DeleteClaimHeaderFileIDSQL = 'DELETE FROM '+@clientSchema+'.ClaimHeader where FILEID = 167'

PRINT @DeleteClaimHeaderFileIDSQL
EXEC(@DeleteClaimHeaderFileIDSQL)

END

ELSE
PRINT 'No records moved either due to environment or date'