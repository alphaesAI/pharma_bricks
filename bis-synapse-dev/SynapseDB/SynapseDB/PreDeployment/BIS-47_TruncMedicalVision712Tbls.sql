/***************************************************************************************
BIS-47_TruncMedicalVision712Tbls
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO TRUNC Medical and Visoin 7.12 TBLs'
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

 IF OBJECT_ID(@var_client_47+'.MedicalClaimLine','U') is not null
 BEGIN
  IF(SELECT count(*) FROM INFORMATION_SCHEMA.columns where table_schema=@var_client_47 and table_name='MedicalClaimLine' and column_name='ProcCode1')=0
   BEGIN
    EXEC ('truncate table '+ @var_client_47 + '.MedicalClaimHeader')
    EXEC ('truncate table '+ @var_client_47 + '.MedicalClaimLine')
   END
 END

 IF OBJECT_ID(@var_client_47+'.VisionClaimLine','U') is not null
 BEGIN
  IF(SELECT count(*) FROM INFORMATION_SCHEMA.columns where table_schema=@var_client_47 and table_name='VisionClaimLine' and column_name='ProcCode1')=0
   BEGIN
      EXEC ('truncate table '+ @var_client_47 + '.VisionClaimHeader')
      EXEC ('truncate table '+ @var_client_47 + '.VisionClaimLine')
   END
 END

 set @i_47 = @i_47+1
END
drop table #allclients47
