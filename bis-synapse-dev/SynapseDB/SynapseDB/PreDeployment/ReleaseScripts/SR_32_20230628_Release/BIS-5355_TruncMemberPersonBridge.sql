/***************************************************************************************
BIS-5355_Truncgold_ma_memberpersonbridge
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO TRUNC gold_ma_memberpersonbridge'
DECLARE @servername_99 VARCHAR(30), @i_99 int, @cnt_99 int, @var_client_99 VARCHAR(30)
select @servername_99 = SERVERPROPERTY('ServerName')
CREATE TABLE #allclients99(id int, client VARCHAR(30))
IF  substring(@servername_99,7,1) = 'd'
BEGIN
 PRINT substring(@servername_99,7,1)
 insert into #allclients99(id,client) select 1,'devidap1' union select 2,'devidap2'
END
ELSE IF  substring(@servername_99,7,1) = 'q'
BEGIN
 PRINT substring(@servername_99,7,1)
 insert into #allclients99(id,client) select 1,'qaidap1' union select 2,'qaidap2'
END
ELSE IF  substring(@servername_99,7,1) in ('s','p')
BEGIN
 PRINT substring(@servername_99,7,1)
 insert into #allclients99(id,client) select 1,'bcbsks' union select 2,'vba'
END
ELSE
PRINT 'DID NO OPERATIONS'

SET @i_99=1
SELECT @cnt_99=count(*) from #allclients99
WHILE @i_99 <= @cnt_99
BEGIN
 select @var_client_99=client from #allclients99 where id=@i_99
 print 'execute for client ' + @var_client_99

 IF OBJECT_ID(@var_client_99+'.gold_ma_memberpersonbridge','U') is not null
 BEGIN
  IF(SELECT count(*) FROM INFORMATION_SCHEMA.columns where table_schema=@var_client_99 and table_name='gold_ma_memberpersonbridge')=0
   BEGIN
    EXEC ('truncate table '+ @var_client_99 + '.gold_ma_memberpersonbridge')
   END
 END

 set @i_99 = @i_99+1
END
drop table #allclients99
