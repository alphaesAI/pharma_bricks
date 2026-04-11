# Databricks notebook source
# DBTITLE 1,read client from ADF
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("delayTimer","","")

clientContainer =  dbutils.widgets.get("ClientContainer")
delayTimer =  dbutils.widgets.get("delayTimer")
ExportAuditTablePath = "/mnt/export" + clientContainer +"/BatchAudit/export_audit"
ExportAuditTrackingTablePath = "/mnt/export" + clientContainer +"/BatchAudit/export_audit_tracking"

# COMMAND ----------

# DBTITLE 1,Import libaries
from pyspark.sql.types import (
    StringType,
    StructField,
    StructType,
    IntegerType,
    MapType
)
from pyspark.sql.functions import udf
import pyspark.sql.functions as F
from pyspark.sql.functions import lit, col, row_number, monotonically_increasing_id
from pyspark.sql import Window
w = Window.orderBy(monotonically_increasing_id())

# COMMAND ----------

import time

def delay(delayTimer):
  timeToWait = 0
  if(delayTimer == ""):
    timeToWait = 0
  else:
    timeToWait = int(delayTimer)

  time.sleep(timeToWait)

# COMMAND ----------

def GenerateMessage(currentMessage):
  message = [("V2",1)]

  msgSchema = StructType([ \
    StructField("MessageVersion",StringType(),True), \
    StructField("columnindex",IntegerType(),True)
  ])
  
  #Create a dataframe
  msgdf = spark.createDataFrame(data=message,schema=msgSchema)
  
  #parralelize a single message
  sentdf = spark.read.json(sc.parallelize([currentMessage]))
  
  #set JSONFileName to a rdd map
  filenames = sentdf.select('JSONFileName').rdd.flatMap(lambda x: x).collect()
  
  #Create UDF for Entity structure
  build_Entities_udf = udf(lambda Entity, FileNames: {
    'Entity': Entity,
    'Files': FileNames
}, MapType(StringType(), StringType()))

  Sent_df1 = (
    sentdf
    .withColumn("columnindex", row_number().over(w)) #monotonically increasing id
    .withColumn('filenamearray',F.array([F.lit(string) for string in filenames])) #Create an array of filenames from filename rdd map
)

  Sent_df2 = (
    Sent_df1
    .withColumn('Entities', build_Entities_udf(Sent_df1['Entity'], Sent_df1['filenamearray'])) #UDF to create entities << only works if a single entity is in one message  
)

  Sent_df3 = (
    Sent_df2    
    .drop('filenamearray')
    .drop('JSONFileName')
    .drop('BatchId')
    .drop('SourceFileId')
    .drop('Entity')
    .drop('SourceFileId') #dropping some columns
    .drop('SourceFileName') #dropping some columns
    .drop('TotalNumberOfBatches') #dropping some columns
    .drop('NDJSONCount') #dropping some columns
    .drop('ExportAuditTrackingId')
    .drop('ExtractionDate')
)

  topicdf = msgdf.join(Sent_df3, msgdf.columnindex == Sent_df3.columnindex, 'inner').drop('columnindex') #join message to topic message to create json with version

  JSONObj = topicdf.toJSON().collect() #convert to json and collect object << does not garuntee order of json << most likely alphabetical order ascending
  JSONStr = str(JSONObj) #make json a string
  message = JSONStr.replace("['","").replace("']","").replace(':"[',':["').replace(']"','"]').replace('"Entities":','"Entities":[').replace('}}','}]}') #do all kinds of cool magic to replace json
  return message

# COMMAND ----------

def GenerateMessageVersionThree(currentMessage):  
  message = [("V3",1)]

  msgSchema = StructType([ \
    StructField("MessageVersion",StringType(),True), \
    StructField("columnindex",IntegerType(),True)
  ])
  
  #Create a dataframe
  msgdf = spark.createDataFrame(data=message,schema=msgSchema)
  
  #parralelize a single message
  sentdf = spark.read.json(sc.parallelize([currentMessage]))
  
  #set JSONFileName to a rdd map
  filenames = sentdf.select('JSONFileName').rdd.flatMap(lambda x: x).collect()
  
  #Create UDF for Entity structure
  build_Entities_udf = udf(lambda Entity, FileNames: {
    'Entity': Entity,
    'Files': FileNames
}, MapType(StringType(), StringType()))

  Sent_df1 = (
    sentdf
    .withColumn("columnindex", row_number().over(w)) #monotonically increasing id
    .withColumn('filenamearray',F.array([F.lit(string) for string in filenames])) #Create an array of filenames from filename rdd map
)

  Sent_df2 = (
    Sent_df1
    .withColumn('Entities', build_Entities_udf(Sent_df1['Entity'], Sent_df1['filenamearray'])) #UDF to create entities << only works if a single entity is in one message  
)

  Sent_df3 = (
    Sent_df2      #dropping some columns
    .drop('filenamearray')
    .drop('JSONFileName')
    .drop('BatchId')
    .drop('SourceFileId')
    .drop('Entity')
    .drop('SourceFileId')
    .drop('ExportAuditTrackingId')
    .drop('ExtractionDate')
)

  topicdf = msgdf.join(Sent_df3, msgdf.columnindex == Sent_df3.columnindex, 'inner').drop('columnindex') #join message to topic message to create json with version

  JSONObj = topicdf.toJSON().collect() #convert to json and collect object << does not garuntee order of json << most likely alphabetical order ascending
  JSONStr = str(JSONObj) #make json a string
  message = JSONStr.replace("['","").replace("']","").replace(':"[',':["').replace(']"','"]').replace('"Entities":','"Entities":[').replace('}}','}]}') #do all kinds of cool magic to replace json
  return message

# COMMAND ----------

def GetFunctionAppURL():
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
  functionAppURL = "" 

  ######## THIS IS THE MASTER FUNCTION KEY -- MAY RESET
  if(dbEnv == "934226345849410"): #dev
    functionAppURL = "https://func-c-d-shrd-idap0000-01.azurewebsites.net/api/SendMessageToExportTopic?code=bkn8LNSVlUb_XOSSx9H3_jBridOg5xqvk8ULRpltFJAJAzFuJN6NFA=="
  elif(dbEnv == "5826678703751685"): #qa
    functionAppURL = "https://func-c-q-shrd-idap0000-01.azurewebsites.net/api/SendMessageToExportTopic?code=8yJU4fVE9VKXUUBqjxby9W3j_VA8SOPdcWNPBgefIUTLAzFu_waM8A=="
  elif(dbEnv == "7093677384385470"): #stg
    functionAppURL = "https://func-c-s-shrd-idap0000-01.azurewebsites.net/api/SendMessageToExportTopic?code=zJfaaDMRaYehHnzyiMZRPKkVaEnLIfwX5CdoxncPhQzaPpaorzStfQ=="
  else: #prod
    functionAppURL = "https://func-c-p-shrd-idap0000-01.azurewebsites.net/api/SendMessageToExportTopic?code=vN60a8vXJcXsO9l01zaEWZ6dDSluf8qHfAtofMS5UbZMV9FDt8qWvw=="
    
  return functionAppURL

# COMMAND ----------

import requests
import json
from requests.auth import HTTPBasicAuth

def putMessageOnServiceBus(client,message):
  returnString = ""
  
  #connect to function SendMessageToExportTopic
  url = GetFunctionAppURL()
  
  #create header variable
  headers =  {"clientId":client, "jsonMessage":message}
  
  try:
    #make request and return response
    rsp = requests.get(url, headers=headers)
    tempString = str(rsp.status_code)
    
    if (tempString == "200"):
      returnString = "SUCCESS"
    else:
      returnString = "Failure-ResponseCode: " + tempString
  except Exception as e:
    returnString = "Error: " + e
  finally:
    return returnString

# COMMAND ----------

def InsertExportAuditTracking(message):
  updatedf = spark.read.json(sc.parallelize([message]))
  updatedf.createOrReplaceTempView("sentRecord")

  InsertExportAuditTrackingBatch = f"""
    INSERT INTO ExportAuditTracking    
    SELECT 
             ExportAuditTrackingId
            ,Entity
            ,FileId
            ,BatchId
            ,JSONFileName
            ,ExtractionDate
            ,True
            ,NDJSONCount
            ,current_timestamp()
    FROM sentRecord
  """

  #Execute query 
  spark.sql(InsertExportAuditTrackingBatch)

  return "Success"

# COMMAND ----------

# DBTITLE 1,select batch created files for 3rd notebook
sentJson = ""

try:
  spark.read.format("delta").load(ExportAuditTablePath).createOrReplaceTempView("ExportAudit")
  spark.read.format("delta").load(ExportAuditTrackingTablePath).createOrReplaceTempView("ExportAuditTracking")
  
  sqlQuery = """
      WITH CurrentExportTracking AS( 
      SELECT 
         ExportAuditTrackingId
        ,JSONFileName 
        ,SentToTopic
        ,ExtractionDate
        ,NDJSONCount
        ,ROW_NUMBER() OVER(PARTITION BY ExportAuditTrackingId ORDER BY LoadDateTime DESC) AS RowNumber
      FROM ExportAuditTracking 
      )
      SELECT DISTINCT
             a.ExportAuditTrackingId
            ,a.Entity 
            ,a.LOB
            ,a.ClientCode
            ,a.SubClientCode
            ,a.SourceFileId  AS FileId
            ,cet.JSONFileName
            ,a.BatchId
            ,a.SourceFileName
            ,a.TotalNumberOfBatches
            ,cet.NDJSONCount
            ,cet.ExtractionDate
      FROM ExportAudit a
        LEFT JOIN CurrentExportTracking cet
          ON a.ExportAuditTrackingId = cet.ExportAuditTrackingId
          AND cet.RowNumber = 1
      WHERE
      cet.JSONFileName IS NOT NULL 
      AND 
      COALESCE(cet.SentToTopic,False) = 0
        """

  result = spark.sql(sqlQuery)
  messages = result.toJSON().collect()
  
  for message in messages:
    delay(delayTimer) #comment this out as soon as possible :(
#    newMessage = GenerateMessage(message)
    newMessage = GenerateMessageVersionThree(message)
    print(newMessage)
    messageResponse = putMessageOnServiceBus(clientContainer, newMessage)
    InsertExportAuditTracking(message)

  sentJson = "SUCCESS"
except:
  sentJson = "FAILURE"

# COMMAND ----------

dbutils.notebook.exit(sentJson)
