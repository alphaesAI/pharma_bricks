/***************************************************************************************
BIS-4632 Droping ACA Medical Claim tables
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO DROP ACAMedicalClaim TABLES'
DECLARE @servername_47 VARCHAR(30), @i_47 int, @cnt_47 int, @var_client_47 VARCHAR(30)

SELECT @servername_47 = SERVERPROPERTY('ServerName')

CREATE TABLE #allclients47(id int, client VARCHAR(30))

IF  substring(@servername_47,7,1) = 'd'
    BEGIN
     PRINT substring(@servername_47,7,1)
     insert into #allclients47(id,client) select 1,'devidap1' union select 2,'devidap2' union select 3,'global' union select 4,'dbo'
    END
ELSE IF  substring(@servername_47,7,1) = 'q'
    BEGIN
     PRINT substring(@servername_47,7,1)
     insert into #allclients47(id,client) select 1,'qaidap1' union select 2,'qaidap2' union select 3,'global' union select 4,'dbo'
    END
ELSE IF  substring(@servername_47,7,1) in ('s','p')
    BEGIN
     PRINT substring(@servername_47,7,1)
     insert into #allclients47(id,client) 
     select 1,'bcbsks' 
     union 
     select 2,'bcbsm' 
     union 
     select 3,'bcbsne'
     union 
     select 4,'dbo'
     union 
     select 5,'fallon'
     union 
     select 6,'global' 
     union 
     select 7,'nbnd'
     union 
     select 8,'premera'
     union 
     select 9,'vba'
     union 
     select 10,'wahp'
    END
ELSE
PRINT 'DID NO OPERATIONS'

SET @i_47=1
SELECT @cnt_47=count(*) from #allclients47
WHILE @i_47 <= @cnt_47
BEGIN
 select @var_client_47=client from #allclients47 where id=@i_47
 print 'execute for client ' + @var_client_47

 IF OBJECT_ID(@var_client_47+'.ACAMedicalClaimHeader','U') is not null
 BEGIN
    EXEC ('drop table '+ @var_client_47 + '.ACAMedicalClaimHeader')
 END

 IF OBJECT_ID(@var_client_47+'.ACAMedicalClaimLine','U') is not null
 BEGIN
    EXEC ('drop table '+ @var_client_47 + '.ACAMedicalClaimLine')
 END

 set @i_47 = @i_47+1
END
drop table #allclients47
