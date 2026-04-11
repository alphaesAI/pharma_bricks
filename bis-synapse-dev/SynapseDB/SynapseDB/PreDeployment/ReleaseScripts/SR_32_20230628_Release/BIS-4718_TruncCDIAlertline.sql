/***************************************************************************************
BIS-4718_Truncgold_ma_cdialertline
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO TRUNC gold_ma_cdialertline'
DECLARE @servername_47 VARCHAR(30), @i_47 int, @cnt_47 int, @var_client_47 VARCHAR(30)
select @servername_47 = SERVERPROPERTY('ServerName')
CREATE TABLE #allclients47(id int, client VARCHAR(30))
IF  substring(@servername_47,7,1) = 'd'
BEGIN
 PRINT substring(@servername_47,7,1)
 insert into #allclients47(id,client) select 1,'devidap1' union select 2,'devidap2'
END
ELSE IF  substring(@servername_47,7,1) = 'q'
BEGIN
 PRINT substring(@servername_47,7,1)
 insert into #allclients47(id,client) select 1,'qaidap1' union select 2,'qaidap2'
END
ELSE IF  substring(@servername_47,7,1) in ('s','p')
BEGIN
 PRINT substring(@servername_47,7,1)
 insert into #allclients47(id,client) select 1,'bcbsks' union select 2,'bcbsm' union select 3,'nbnd' union select 4,'vba'
END
ELSE
PRINT 'DID NO OPERATIONS'

SET @i_47=1
SELECT @cnt_47=count(*) from #allclients47
WHILE @i_47 <= @cnt_47
BEGIN
 select @var_client_47=client from #allclients47 where id=@i_47
 print 'execute for client ' + @var_client_47

 IF OBJECT_ID(@var_client_47+'.gold_ma_cdialertline','U') is not null
 BEGIN
  IF(SELECT count(*) FROM INFORMATION_SCHEMA.columns where table_schema=@var_client_47 and table_name='gold_ma_cdialertline')=0
   BEGIN
    EXEC ('truncate table '+ @var_client_47 + '.gold_ma_cdialertline')
   END
 END

 set @i_47 = @i_47+1
END
drop table #allclients47
