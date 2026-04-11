# Databricks notebook source
# DBTITLE 1,import client parameter
dbutils.widgets.text("ClientContainer","","")

clientContainer = dbutils.widgets.get("ClientContainer")

print("clientContainer: " + clientContainer)

# COMMAND ----------

# DBTITLE 1,Setup Database connections (python)
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
  blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
  blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
  blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="
else:
  envLetter = "p"
  envUser = "PRD"+envUser
  blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
#jdbcDatabase = "Configuration_DB_" + ClientContainerUpper
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Setup Database connections (scala)
# MAGIC %scala 
# MAGIC val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
# MAGIC var envLetter ="" 
# MAGIC var envUser="_ETLUSER_SQL"
# MAGIC 
# MAGIC if (dbEnv == "934226345849410") {envLetter = "d";envUser = "DEV"+envUser}
# MAGIC else if (dbEnv == "5826678703751685") {envLetter = "q";envUser = "QA"+envUser}
# MAGIC else if (dbEnv == "7093677384385470") {envLetter = "s";envUser = "STG"+envUser}
# MAGIC else {envLetter = "p";envUser = "PRD"+envUser} 
# MAGIC 
# MAGIC Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver")
# MAGIC val jdbcHostname = "sql-c-" + envLetter + "-shrd-idap0000-01.database.windows.net"
# MAGIC val jdbcPort = 1433
# MAGIC val jdbcUsername = envUser
# MAGIC val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
# MAGIC 
# MAGIC // Create a Properties() object to hold the parameters.
# MAGIC import java.util.Properties
# MAGIC val connectionProperties = new Properties()
# MAGIC 
# MAGIC connectionProperties.put("user", s"$jdbcUsername")       
# MAGIC connectionProperties.put("password", s"$jdbcPassword") 
# MAGIC 
# MAGIC val driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# MAGIC connectionProperties.setProperty("Driver", driverClass)
# MAGIC 
# MAGIC val jdbcDataBase = "syn-c-"+envLetter+"-shrd-idap0000-01"
# MAGIC val jdbcURL = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDataBase
