/***************************************************************************************
BIS-6185 Droping CMS tables
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO DROP CMS TABLES'
DECLARE @servername_48 VARCHAR(30), @i_48 int, @cnt_48 int, @var_client_48 VARCHAR(30)

SELECT @servername_48 = SERVERPROPERTY('ServerName')

CREATE TABLE #allclients48(id int, client VARCHAR(30))

IF  substring(@servername_48,7,1) = 'd'
    BEGIN
     PRINT substring(@servername_48,7,1)
     insert into #allclients48(id,client) select 1,'devidap1' union select 2,'devidap2' union select 3,'global' union select 4,'dbo'
    END
ELSE IF  substring(@servername_48,7,1) = 'q'
    BEGIN
     PRINT substring(@servername_48,7,1)
     insert into #allclients48(id,client) select 1,'qaidap1' union select 2,'qaidap2' union select 3,'global' union select 4,'dbo'
    END
ELSE IF  substring(@servername_48,7,1) in ('s','p')
    BEGIN
     PRINT substring(@servername_48,7,1)
     insert into #allclients48(id,client) 
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

SET @i_48=1
SELECT @cnt_48=count(*) from #allclients48
WHILE @i_48 <= @cnt_48
BEGIN
 select @var_client_48=client from #allclients48 where id=@i_48
 print 'execute for client ' + @var_client_48

 IF OBJECT_ID(@var_client_48+'.CMS_HICN_MBI_CrossWalk','U') is not null
 BEGIN
    EXEC ('drop table '+ @var_client_48 + '.CMS_HICN_MBI_CrossWalk')
 END

 IF OBJECT_ID(@var_client_48+'.CMS_LISHIST','U') is not null
 BEGIN
    EXEC ('drop table '+ @var_client_48 + '.CMS_LISHIST')
 END

 IF OBJECT_ID(@var_client_48+'.CMS_MMR','U') is not null
 BEGIN
    EXEC ('drop table '+ @var_client_48 + '.CMS_MMR')
 END

 set @i_48 = @i_48+1
END
drop table #allclients48
