/***************************************************************************************
IDAP-1925
This script is to truncate and update DispenseAsWritten column length of Pharmacy table 
****************************************************************************************/
PRINT 'EXECUTING PREDEPLOYMENT SCRIPT TO TRUNC AND UPDATE COLUMN FOR PHARMACY TBL'
DECLARE @servername VARCHAR(30), @i int, @cnt int, @var_client VARCHAR(30), @chr_len int
select @servername = SERVERPROPERTY('ServerName')
CREATE TABLE #tblclients(id int, client VARCHAR(30))
IF  substring(@servername,7,1) = 'd'
BEGIN
 PRINT substring(@servername,7,1)
 insert into #tblclients(id,client) select 1,'devidap1' union select 2,'devidap2'
END
ELSE IF  substring(@servername,7,1) = 'q'
BEGIN
 PRINT substring(@servername,7,1)
 insert into #tblclients(id,client) select 1,'qaidap1' union select 2,'qaidap2'
END
ELSE IF  substring(@servername,7,1) in ('s','p')
BEGIN
 PRINT substring(@servername,7,1)
 insert into #tblclients(id,client) select 1,'bcbsks' union select 2,'bcbsm' union select 3,'nbnd' union select 4,'vba'
END
ELSE
PRINT 'DID NO OPERATIONS'

SET @i=1
SELECT @cnt=count(*) from #tblclients
WHILE @i <= @cnt
BEGIN
 select @var_client=client from #tblclients where id=@i
 IF OBJECT_ID(@var_client+'.Pharmacy','U') is not null
 BEGIN
  SELECT @chr_len=character_maximum_length
  FROM INFORMATION_SCHEMA.columns where table_schema=@var_client and table_name='Pharmacy' and column_name='DispenseAsWritten'
  IF @chr_len < 25
  BEGIN
  print 'execute for client ' + @var_client
  EXEC ('truncate table '+ @var_client + '.Pharmacy')
  EXEC ('alter table '+ @var_client +'.Pharmacy alter column DispenseAsWritten varchar(25)')
  END
 END
 set @i = @i+1
END
drop table #tblclients