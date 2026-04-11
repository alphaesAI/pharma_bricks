# Databricks notebook source
def getJDBCUrl(dbType, clientCode):
  
  envLetter = "" 
  envUser="_ETLUSER_SQL"
  blobKey = ""
  
  #gets the databricks environment tag so we can get the sdlc environment information
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")

  #set variables depending on the environment
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

  #define the jdbc connection and it's properties
  jdbcUsername = envUser
  jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

  jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
  jdbcPort = "1433"
  
  #determines which database to use
  if(dbType == 'config'):
    jdbcDatabase = "Configuration_DB_" + clientCode.upper()
  elif(dbType == 'synapse'):
    jdbcDatabase = "syn-c-"+envLetter+"-shrd-idap0000-01"
    
  jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

  jdbcProperties = {
                "user" : jdbcUsername,
                "password" : jdbcPassword,
                "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
              }
  
  return jdbcUrl, jdbcProperties;
