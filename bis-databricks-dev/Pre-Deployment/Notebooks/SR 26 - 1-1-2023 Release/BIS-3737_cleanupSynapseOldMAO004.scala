// Databricks notebook source
// DBTITLE 1,get environment and connection configuration ready
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter ="" 
var envUser="_ETLUSER_SQL"

if (dbEnv == "934226345849410") {envLetter = "d";envUser = "DEV"+envUser}
else if (dbEnv == "5826678703751685") {envLetter = "q";envUser = "QA"+envUser}
else if (dbEnv == "7093677384385470") {envLetter = "s";envUser = "STG"+envUser}
else {envLetter = "p";envUser = "PRD"+envUser} 

Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
val jdbcHostname = "sql-c-" + envLetter + "-shrd-idap0000-01.database.windows.net"
val jdbcPort = 1433
val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

// Create a Properties() object to hold the parameters.
import java.util.Properties
val connectionProperties = new Properties()

connectionProperties.put("user", s"$jdbcUsername")       
connectionProperties.put("password", s"$jdbcPassword") 

val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
connectionProperties.setProperty("Driver", driverClass)

val jdbcDataBase = "syn-c-"+envLetter+"-shrd-idap0000-01"
val jdbcURL = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDataBase

// COMMAND ----------

// DBTITLE 1,connect to synapse db and drop tables
import java.sql.DriverManager
val connectionProperties = new Properties()
connectionProperties.put("user", s"$jdbcUsername")       
connectionProperties.put("password", s"$jdbcPassword") 

val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
connectionProperties.setProperty("Driver", driverClass)

val sqlStatment = """
IF OBJECT_ID(N'tempdb..#tempdelete') IS NOT NULL
DROP TABLE #tempdelete
select schema_name(t.schema_id)+ '.' + t.name as tableName        
	   into #tempdelete
from sys.tables t
where t.name = 'gold_ma_mao004diagnosis'

--loop through table list and drop these tables in list
declare @cnt int = 0, @tablename varchar(max), @sql varchar(max) = '', @error varchar(1000)
select @cnt =count(*) from #tempdelete

while @cnt> 0
	begin
		select top 1  @tablename = tableName from  #tempdelete 
		set @sql =  'drop table ' + @tablename + ';'
		begin try
          exec (@sql)
          delete from #tempdelete where tableName = @tablename
          set @cnt = @cnt -1
		end try
        
		begin catch
          delete from #tempdelete where tableName = @tablename
          set @cnt = @cnt -1
		end catch
	end
    
IF OBJECT_ID(N'tempdb..#tempdelete') IS NOT NULL
DROP TABLE #tempdelete
"""

val con = DriverManager.getConnection(jdbcURL, connectionProperties)
val stmt = con.createStatement()

  
stmt.execute(sqlStatment)
stmt.close()


// COMMAND ----------

// DBTITLE 1,table name list query
val sqlquery1 = """
select schema_name(t.schema_id)+ '.' + t.name as tableName      
from sys.tables t
where t.name = 'gold_ma_mao004diagnosis'
"""

// COMMAND ----------

// DBTITLE 1,report cleanup execution result
val jdbcDF = spark.read.jdbc(s"$jdbcURL", s"($sqlquery1) as table1", connectionProperties)

val tblCount = jdbcDF.count()

if (tblCount == 0) {
  println ("Table cleanup completed successfully!")
}
else {
  println("Tables couldn't be dropped:")
  jdbcDF.collect.foreach(println)
}
