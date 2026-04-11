/***************************************************************************************
BIS-6351 Truncate tables platinum_dimqualityyearmonth in clients
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO TRUNCATE platinum_dimqualityyearmonth TABLES (NOT GLOBAL!)'
DECLARE @servername_49 VARCHAR(30), @i_49 int, @cnt_49 int, @var_client_49 VARCHAR(30)

SELECT @servername_49 = SERVERPROPERTY('ServerName')

CREATE TABLE #allclients49(id int, client VARCHAR(30))

IF  substring(@servername_49,7,1) = 'd'
    BEGIN
     PRINT substring(@servername_49,7,1)
     insert into #allclients49(id,client) select 1,'devidap1' union select 2,'devidap2' union select 3,'dbo'
    END
ELSE IF  substring(@servername_49,7,1) = 'q'
    BEGIN
     PRINT substring(@servername_49,7,1)
     insert into #allclients49(id,client) select 1,'qaidap1' union select 2,'qaidap2' union select 3,'dbo'
    END
ELSE IF  substring(@servername_49,7,1) in ('s','p')
    BEGIN
     PRINT substring(@servername_49,7,1)
     insert into #allclients49(id,client) 
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
     select 6,'nbnd'
     union 
     select 7,'premera'
     union 
     select 8,'vba'
     union 
     select 9,'wahp'
    END
ELSE
PRINT 'DID NO OPERATIONS'

SET @i_49=1
SELECT @cnt_49=count(*) from #allclients49
WHILE @i_49 <= @cnt_49
BEGIN
 select @var_client_49=client from #allclients49 where id=@i_49
 print 'execute for client ' + @var_client_49

 IF OBJECT_ID(@var_client_49+'.platinum_dimqualityyearmonth','U') is not null
 BEGIN
    EXEC ('truncate table '+ @var_client_49 + '.platinum_dimqualityyearmonth')
 END

 set @i_49 = @i_49+1
END
drop table #allclients49
