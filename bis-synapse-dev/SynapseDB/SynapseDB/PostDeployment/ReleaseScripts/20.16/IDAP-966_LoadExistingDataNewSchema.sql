/*************************
IDAP-966 
This script is to copy values from the original schema.table to the new client.table 
IDAP-1096
This script will remove the Kansas data from BCBSM tables
*************************/
PRINT 'EXECUTING POSTDEPLOYMENT SCRIPT TO POPULATE NEW SCHEMAS'
PRINT 'REMOVING KANSAS DATA FROM BCBSM'

GO
DECLARE @dbName VARCHAR(1) = SUBSTRING(db_name(),7,1)
DECLARE @clientSchema VARCHAR(20)

SET @clientSchema = CASE @dbName
	WHEN 'd' THEN 'devidap1'
	WHEN 'q' THEN 'qaidap1'
	else 'bcbsm'
	END

PRINT @dbName 
PRINT @clientSchema

IF @dbName <>'p' AND getDate() <= '12/16/2020'
BEGIN
--ClaimHeader Data Move
DECLARE @ClaimHeaderSQL VARCHAR(300)
SET @ClaimHeaderSQL = 
--('DECLARE @ClaimHeaderCount INT = 0;
--SELECT @ClaimHeaderCount = COUNT(1) FROM dw.ClaimHeader
--IF @ClaimHeaderCount > 0
--INSERT INTO '+@clientSchema+'.ClaimHeader SELECT * FROM dw.ClaimHeader;'
--);
'DELETE FROM '+@clientSchema+'.ClaimHeader'
PRINT @ClaimHeaderSQL
PRINT 'ReMoving records from ClaimHeader'
EXEC(@ClaimHeaderSQL)

--ClaimLine Data Move
DECLARE @ClaimLineSQL VARCHAR(300)
SET @ClaimLineSQL = 
--('DECLARE @ClaimLineCount INT = 0
--SELECT @ClaimLineCount = COUNT(1) FROM dw.ClaimLine
--IF @ClaimLineCount  > 0
--INSERT INTO '+@clientSchema+'.ClaimLine SELECT * FROM dw.ClaimLine')
'DELETE FROM '+@clientSchema+'.ClaimLine'
PRINT @ClaimLineSQL
PRINT 'Removing records for ClaimLine'
EXEC(@ClaimLineSQL)

--CMS_LISHIST Data Move
DECLARE @CMS_LISHISTSQL VARCHAR(300)
SET @CMS_LISHISTSQL = 
--('DECLARE @CMS_LISHISTCount INT = 0
--SELECT @CMS_LISHISTCount = COUNT(1) FROM dw.CMS_LISHIST
--IF @CMS_LISHISTCount  > 0
--INSERT INTO '+@clientSchema+'.CMS_LISHIST SELECT * FROM dw.CMS_LISHIST')
'DELETE FROM '+@clientSchema+'.CMS_LISHIST'
PRINT @CMS_LISHISTSQL
PRINT 'ReMoving records for CMS_LISHIST'
EXEC(@CMS_LISHISTSQL)

--GoldenClaim Data Move
DECLARE @GoldenClaimSQL VARCHAR(300)
SET @GoldenClaimSQL = 
--('DECLARE @GoldenClaimCount INT = 0
--SELECT @GoldenClaimCount = COUNT(1) FROM dw.GoldenClaim
--IF @GoldenClaimCount  > 0
--INSERT INTO '+@clientSchema+'.GoldenClaim SELECT * FROM dw.GoldenClaim')
'DELETE FROM '+@clientSchema+'.GoldenClaim'
PRINT @GoldenClaimSQL
PRINT 'Moving records for GoldenClaim'
EXEC(@GoldenClaimSQL)

--GoldenClaimHistory Data Move
DECLARE @GoldenClaimHistorySQL VARCHAR(300)
SET @GoldenClaimHistorySQL = 
--('DECLARE @GoldenClaimHistoryCount INT = 0
--SELECT @GoldenClaimHistoryCount = COUNT(1) FROM dw.GoldenClaimHistory
--IF @GoldenClaimHistoryCount  > 0
--INSERT INTO '+@clientSchema+'.GoldenClaimHistory SELECT * FROM dw.GoldenClaimHistory')
'DELETE FROM '+@clientSchema+'.GoldenClaimHistory'
PRINT @GoldenClaimHistorySQL
PRINT 'Moving records for GoldenClaimHistory'
EXEC(@GoldenClaimHistorySQL)


--CMS MMR Data Remove
DECLARE @CMSMMRSQL VARCHAR(300)
SET @CMSMMRSQL = 
'DELETE FROM '+@clientSchema+'.CMS_MMR'
PRINT @CMSMMRSQL
PRINT 'Removing records for CMS MMR Data'
EXEC(@CMSMMRSQL)

END

ELSE
PRINT 'No records moved either due to environment or date'