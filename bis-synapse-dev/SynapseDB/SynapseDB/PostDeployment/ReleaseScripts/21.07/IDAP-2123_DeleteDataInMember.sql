/*************************
IDAP-2123
This script is to delete data from Member synapse table for all envs 
*************************/
PRINT 'REMOVING DATA FROM MEMBER TABLE'

GO
DECLARE @dbName VARCHAR(1) = SUBSTRING(db_name(),7,1)
DECLARE @clientSchema VARCHAR(20)
DECLARE @clientBcbsksSchema VARCHAR(20)
DECLARE @clientVbaSchema VARCHAR(20)
DECLARE @clientNbndSchema VARCHAR(20)

-- setup  default clientSchema
SET @clientSchema = CASE @dbName
	WHEN 'd' THEN 'devidap1'
	WHEN 'q' THEN 'qaidap1'
	else 'bcbsm'
	END

PRINT @dbName 
PRINT @clientSchema

-- setup other clientSchema
SET @clientBcbsksSchema = 'bcbsks'	
SET @clientVbaSchema = 'vba'
SET @clientNbndSchema = 'nbnd'	


DECLARE @DeleteMemberSQL VARCHAR(300)
SET @DeleteMemberSQL = 
'DELETE FROM '+@clientSchema+'.Member'

DECLARE @DeleteMemberBcbsksSQL VARCHAR(300)
SET @DeleteMemberBcbsksSQL = 
'DELETE FROM '+@clientBcbsksSchema+'.Member'

DECLARE @DeleteMemberVbaSQL VARCHAR(300)
SET @DeleteMemberVbaSQL = 
'DELETE FROM '+@clientVbaSchema+'.Member'

DECLARE @DeleteMemberNbndSQL VARCHAR(300)
SET @DeleteMemberNbndSQL = 
'DELETE FROM '+@clientNbndSchema+'.Member'

-- for dev and qa
IF @dbName <>'p' AND  @dbName <>'s' AND getDate() <= '06/23/2021'
BEGIN
--delete the member data
PRINT @DeleteMemberSQL
PRINT 'Delete records from Member'
EXEC(@DeleteMemberSQL)

END
-- for stage
IF @dbName = 's' AND getDate() <= '07/10/2021'
BEGIN
--delete the member data
PRINT @DeleteMemberSQL
EXEC(@DeleteMemberSQL)

PRINT @DeleteMemberBcbsksSQL
EXEC(@DeleteMemberBcbsksSQL)

PRINT @DeleteMemberVbaSQL
EXEC(@DeleteMemberVbaSQL)

PRINT @DeleteMemberNbndSQL
EXEC(@DeleteMemberNbndSQL)

END

-- for prod
-- Note: we need to define when to delete the member data in prod???
IF @dbName = 'p' AND getDate() <= '07/30/2021'
BEGIN
--delete the member data
PRINT @DeleteMemberSQL
EXEC(@DeleteMemberSQL)

PRINT @DeleteMemberBcbsksSQL
EXEC(@DeleteMemberBcbsksSQL)

PRINT @DeleteMemberVbaSQL
EXEC(@DeleteMemberVbaSQL)

PRINT @DeleteMemberNbndSQL
EXEC(@DeleteMemberNbndSQL)

END

ELSE
PRINT 'No records moved either due to environment or date'