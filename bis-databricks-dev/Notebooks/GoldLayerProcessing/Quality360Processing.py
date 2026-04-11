# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigPath","","")

ClientCode = dbutils.widgets.get("ClientContainer")
SourceConfigPath = dbutils.widgets.get("ConfigPath")

MountPoint = "/mnt/"
FullConfigPath = MountPoint + SourceConfigPath
print(ClientCode)
print(SourceConfigPath)
print(FullConfigPath)

# COMMAND ----------

from pyspark.sql.functions import explode, col

Quality360JsonExtracted =  spark.read.format("json").option("multiline", "true").load(FullConfigPath)

explodedDF = Quality360JsonExtracted.select(explode("Quality360Files")).select(
              "col.Entity" 
             ,"col.ConfigPath"
             ,"col.SubNotebook"
)

# COMMAND ----------

from dateutil.relativedelta import relativedelta
import pyspark.sql.functions as psf
from pyspark.sql.types import *

def month_range(startDate, endDate):
  return [startDate + relativedelta(months=+x) for x in range((endDate.year - startDate.year)*12 + endDate.month - startDate.month + 1)]

month_range_udf = psf.udf(month_range, ArrayType(DateType()))
spark.udf.register("month_range", month_range_udf) #registers as a spark sql function

# COMMAND ----------

# DBTITLE 1,Create the entity in the gold layer
def CreateEntity(Entity, ConfigPath):
  returnValue = ""
  SingleQuote = "'"
  
  ConfigJSONExtracted = spark.read.format("json").option("multiline", "true").load(ConfigPath)
  ConfigDF = ConfigJSONExtracted.select("Entity", "DestinationTable", explode("SourceTables"), "SQLScript","TruncateScript").select(
                 col("Entity").alias("DestinationEntity")
                ,"DestinationTable"
                ,"col.Entity"
                ,"col.SourceTable" 
                ,"col.SourceFormat" 
                ,"SQLScript"
                ,"TruncateScript"
              )
  
  ViewName = "Config" + Entity
  ConfigDF.createOrReplaceTempView(ViewName)
  
  #Create variables
  QueryVariables = f"""SELECT
                           DestinationEntity
                          ,DestinationTable
                          ,SQLScript
                          ,TruncateScript
                    FROM {ViewName}
                 """
  
  DestinationEntity = spark.sql(QueryVariables).first()[0]
  DestinationTable = spark.sql(QueryVariables).first()[1]
  SQLScript = spark.sql(QueryVariables).first()[2]
  TruncateScript = spark.sql(QueryVariables).first()[3]
  
  #Load destination path entity
  DestinationPath = MountPoint + DestinationTable.replace("#clientCode",ClientCode)
  destdf = spark.read.format('delta').option("header", "true").load(DestinationPath) 
  destdf.createOrReplaceTempView(DestinationEntity)
  print(DestinationEntity + " temp view created")
  
  #Load all sources
  for row in ConfigDF.collect():
    EntityToCreate = row["Entity"]
    SourcePath = row["SourceTable"]
    SourceFormat = row["SourceFormat"]
    
    UpdatedSourcePath = MountPoint + SourcePath.replace("#clientCode",ClientCode)
    #Create a tempview
    dfFile = spark.read.format(SourceFormat).option("header", "true").load(UpdatedSourcePath) 
    dfFile.createOrReplaceTempView(EntityToCreate)
    print(EntityToCreate + " temp view created")

  #Run truncate script
  TruncateSQLQuery = TruncateScript.replace("#clientCode",ClientCode) 
  spark.sql(TruncateSQLQuery)
  print("Truncate SQL was executed")
  
  #Run main query and save into dataframe
  mainSQLQuery = SQLScript.replace("#clientCode",ClientCode) 
  mDF = spark.sql(mainSQLQuery).cache()
  #   mDF.createOrReplaceTempView("tempSQLScript")
  print("Main SQL Query was executed")
  
  #insert into destination table
  mDF.write.format("delta").option("mergeSchema", "true").mode("append").save(DestinationPath) 
  print("Data was written to destination")
    
  returnValue = "Success"
      
  return returnValue

# COMMAND ----------

# DBTITLE 1,Run SQL ConnectionNotebook
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
jdbcDatabase = "Configuration_DB_"+ ClientCode.upper()
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Method: GetFunctionAppURL
def GetFunctionAppURL():
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
  functionAppURL = ""
  
  #master host key
  if(dbEnv == "934226345849410"): #dev
    functionAppURL = "https://func-c-d-shrd-idap0000-01.azurewebsites.net/api/SendMessageToOutboundTopic?code=bkn8LNSVlUb_XOSSx9H3_jBridOg5xqvk8ULRpltFJAJAzFuJN6NFA=="
  elif(dbEnv == "5826678703751685"): #qa
    functionAppURL = "https://func-c-q-shrd-idap0000-01.azurewebsites.net/api/SendMessageToOutboundTopic?code=8yJU4fVE9VKXUUBqjxby9W3j_VA8SOPdcWNPBgefIUTLAzFu_waM8A=="
  elif(dbEnv == "7093677384385470"): #stg
    functionAppURL = "https://func-c-s-shrd-idap0000-01.azurewebsites.net/api/SendMessageToOutboundTopic?code=zJfaaDMRaYehHnzyiMZRPKkVaEnLIfwX5CdoxncPhQzaPpaorzStfQ=="
  else: #prod
    functionAppURL = "https://func-c-p-shrd-idap0000-01.azurewebsites.net/api/SendMessageToOutboundTopic?code=vN60a8vXJcXsO9l01zaEWZ6dDSluf8qHfAtofMS5UbZMV9FDt8qWvw=="

  return functionAppURL

# COMMAND ----------

# DBTITLE 1,Method: putMessageOnServiceBus
import requests
import json
from requests.auth import HTTPBasicAuth

def putMessageOnServiceBus(message):
  returnString = ""
  
  messageFormatted = "".join(message.splitlines()).replace(' ','')
  
  #connect to function SendMessageToExportTopic
  url = GetFunctionAppURL()
  
  #create header variable
  headers =  {"jsonMessage":messageFormatted}
  
  #make request and return response
  rsp = requests.get(url, headers=headers)
  tempString = str(rsp.status_code)
    
  if (tempString == "200"):
    returnString = "SUCCESS"
  else:
    returnString = "Failure-ResponseCode: " + tempString  
  return returnString

# COMMAND ----------

# DBTITLE 1,Method: SendMessageToOutboundServiceBus
def SendMessageToOutboundServiceBus(Entity, ConfigPath):
  returnStr = ""
  
  #generate Query to get OutboundFileLayoutDecription -- should match the entity from the gold layer
    #should only generate a single output -- if there are more than one this will only pickup the first
  SQLConfigQuery = f"""
      SELECT TOP 1
         outfr.OutboundFileReferenceID
        ,outfl.ConfigContainer + '/' + outfl.ConfigPath + outfl.ConfigFileName AS FullFilePath 
      FROM out.refOutboundFileLayout outfl
          LEFT JOIN out.refOutboundFileReference outfr
              ON outfl.OutboundFileLayoutID = outfr.OutboundFileLayoutID
      WHERE
      outfl.OutboundFileLayoutDescription = '{Entity}'
      AND
      outfr.IsActive = 1
    """
  
  pushdown_query = "(" + SQLConfigQuery + ") a" 
  #Gets the outbound file layout description
  OutboundFileDF = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
  
  if(OutboundFileDF.count() > 0):
      OutboundFileReferenceID = ""
      FullFilePath = ""
      for row in OutboundFileDF.collect():
        OutboundFileReferenceID = str(row["OutboundFileReferenceID"])
        FullFilePath = row["FullFilePath"]
        
      FilePath = MountPoint + FullFilePath 
      rdd = spark.sparkContext.wholeTextFiles(FilePath)
      jsonMessage = rdd.collect()[0][1]
  
      #reformat message to be put onto service bus
      newJsonMessage = jsonMessage.replace("#clientCode", ClientCode).replace("#ClientCode", ClientCode).replace("#outboundFileReferenceId", OutboundFileReferenceID).replace("#OutboundFileReferenceId", OutboundFileReferenceID)
      #Put the message on the service bus
      putMessageOnServiceBus(newJsonMessage)
      returnStr = "Success" 
  return returnStr

# COMMAND ----------

# DBTITLE 1,Process Sequentially and Call Sub Notebooks
EntityCollect = explodedDF.collect()

returnStr = ""

for tempEntity in EntityCollect:
  Entity = tempEntity["Entity"]
  TempConfigPath = tempEntity["ConfigPath"]
  ConfigPath = MountPoint + TempConfigPath
  notebookName = tempEntity["SubNotebook"]
  if notebookName == '':       
    print(Entity + " is being truncated and loaded")
    print("ConfigPath: " + ConfigPath)
    CreateEntity(Entity, ConfigPath)
#     print(Entity + " is being sent to outbound -- note will not be maintained in this thread")
    SendMessageToOutboundServiceBus(Entity, ConfigPath)
    returnStr += Entity + " success!"
  else: 
    #run the subnotebook if it's needed         
    print(Entity + " is being truncated and loaded")
    print(notebookName + " is being called")
    
    res = dbutils.notebook.run(notebookName, 0, {"ClientContainer": ClientCode})
    SendMessageToOutboundServiceBus(Entity, ConfigPath)
#     print(Entity + " is being sent to outbound -- note will not be maintained in this thread")
    returnStr += Entity + " finished!" + res
   

# COMMAND ----------

dbutils.notebook.exit(returnStr)
