# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
from pyspark.sql.functions import explode

# COMMAND ----------

def path_exists(path):
  stat = False
  try:
    dbutils.fs.ls(path)
    stat = True
  except Exception as e:
    stat = False 
  return stat

# COMMAND ----------

#get Environment variables from config file
config_schema = StructType(fields=[
    StructField(
        'Environments', ArrayType(
            StructType([
                StructField('EnvironmentLetter', StringType(), True),               
                StructField('Clients',StringType(), True)               
            ])
        )
    )
])

configPath = '/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json'
configdf = spark.read.format("json").option("multiline", "true").json(configPath,schema=config_schema)

clustername = spark.conf.get("spark.databricks.clusterUsageTags.clusterName")
clientlist = []
returnStr = ""
envUser="_ETLUSER_SQL"

c_df = configdf.select(explode("Environments").alias("Env")).select("Env.*")
EnvironmentLetter = ""

#determine client folders for current environment dynamically
if "-d-" in clustername:
  clients = c_df.select("Clients").filter(c_df.EnvironmentLetter == "d").collect()  
  EnvironmentLetter = "d"  
  jdbcUsername =f"DEV{envUser}"
if "-q-" in clustername:
  clients = c_df.select("Clients").filter(c_df.EnvironmentLetter == "q").collect()
  EnvironmentLetter = "q" 
  jdbcUsername =f"QA{envUser}"
if "-s-" in clustername:
  clients = c_df.select("Clients").filter(c_df.EnvironmentLetter == "s").collect()
  EnvironmentLetter = "s" 
  jdbcUsername =f"STG{envUser}"
if "-p-" in clustername:
  clients = c_df.select("Clients").filter(c_df.EnvironmentLetter == "p").collect()
  EnvironmentLetter = "p"  
  jdbcUsername =f"PRD{envUser}"
  
for row in clients:  
  clientlist = row["Clients"].replace("[","").replace("]","").replace('"','').split(",")
  
print(clientlist)

# COMMAND ----------

strmsg = "clients: "
for client in clientlist:  
  if client != "global":
    try:      
      processedPath = f'/mnt/{client}/processed/MA/Data/FCF/V1.0/FCF'
      consolidatedPath = f'/mnt/{client}/consolidated/MA/Data/MedicalClaimLine'
      if path_exists(processedPath) and path_exists(consolidatedPath):
        spark.read.format("parquet").load(processedPath).createOrReplaceTempView("processedClmLine")
        spark.read.format("delta").load(consolidatedPath).createOrReplaceTempView("clmLine")
        updateSQL = """
          UPDATE clmLine AS c
          SET c.ProcCodeType = CASE WHEN c.ProcCode BETWEEN 00000 AND 99999 AND LENGTH(c.ProcCode) = 5 THEN 'CPTCode' 
                                    WHEN SUBSTRING(c.ProcCode,1,1) BETWEEN 'A' AND 'Z' AND SUBSTRING(c.ProcCode,2,5) BETWEEN 0000 AND 9999 AND LENGTH(c.ProcCode)= 5 THEN 'HCPCSCode' 
                                    WHEN c.ProcCode IS NOT NULL THEN 'Unknown' END          
          WHERE c.fileID in (SELECT distinct file_ID FROM processedClmLine WHERE cast(FILE_LAYOUT_ID as int)=1000)
          and c.ProcCodeType is null
          and c.ProcCode is not null
          """
        spark.sql(updateSQL)
        strmsg += client + " consolidated claimLine is updated! "
    except Exception as e:
      strmsg += client + " error message: " + str(e)

print(strmsg)
