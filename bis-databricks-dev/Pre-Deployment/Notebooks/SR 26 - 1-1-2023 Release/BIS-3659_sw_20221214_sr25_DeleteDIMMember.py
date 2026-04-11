# Databricks notebook source
from pyspark.sql.types import *
from pyspark.sql.functions import explode

# COMMAND ----------

# DBTITLE 1,Get list of clients per environment
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

configdf.createOrReplaceTempView("configClient")

# COMMAND ----------

# DBTITLE 1,Get environment information
clustername = spark.conf.get("spark.databricks.clusterUsageTags.clusterName")
clientlist = []
returnStr = ""
envUser="_ETLUSER_SQL"

c_df = configdf.select(explode("Environments").alias("Env")).select("Env.*")
EnvironmentLetter = ""
jdbcUsername =""

#determine client folders for current environment dynamically
if "-d-" in clustername: 
  EnvironmentLetter = "d"  
  jdbcUsername =f"DEV{envUser}"  
if "-q-" in clustername:
  EnvironmentLetter = "q" 
  jdbcUsername =f"QA{envUser}" 
if "-s-" in clustername:
  EnvironmentLetter = "s" 
  jdbcUsername =f"STG{envUser}"  
if "-p-" in clustername:
  EnvironmentLetter = "p"  
  jdbcUsername =f"PRD{envUser}"
if "p162802" in clustername:
  EnvironmentLetter = "p"  
  jdbcUsername =f"PRD{envUser}"

jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
jdbcURL = f"jdbc:sqlserver://sql-c-{EnvironmentLetter}-shrd-idap0000-01.database.windows.net:1433;database=syn-c-{EnvironmentLetter}-shrd-idap0000-01"
jdbcConnectionProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

# DBTITLE 1,Method: drop delta directories
def drop_deltaDir(FolderPath):
  files = dbutils.fs.ls(FolderPath)
  
  for f in files:
    if f.isDir():
      drop_deltaDir(f.path)
    else:
      dbutils.fs.rm(f.path, recurse=True)

  #Remove root level folder path
  dbutils.fs.rm(FolderPath, recurse=True)

# COMMAND ----------

# DBTITLE 1,Method: check if path exists
def path_exists(path):
  stat = False
  try:
    dbutils.fs.ls(path)
    stat = True
  except Exception as e:
    stat = False 
  return stat

# COMMAND ----------

# DBTITLE 1,Get list of clients to be checked against
clients = c_df.select("Clients").filter(c_df.EnvironmentLetter == EnvironmentLetter).collect()

for row in clients:  
  clientlistOri = row["Clients"].replace("[","").replace("]","").replace('"','').split(",")
  print(f"Clients to check: {clientlistOri}")

# COMMAND ----------

# DBTITLE 1,Check for dimMember and delete if found
#note this code drop existing GoldenClaimHistory delta table and recreate it from copying synapse. So it should be only run before the new goldenclaim start in production
for row in clients:  
  clientlist = row["Clients"].replace("[","").replace("]","").replace('"','').split(",")

for client in clientlist:
  if client != "global":
    dmFolderPath = f"/mnt/{client}/Platinum/dimMember"
    
    print(f"Checking for dimMember for: {client}")
        
    if path_exists(dmFolderPath):
      print(f"\t dimMember found")
      drop_deltaDir(dmFolderPath)
      print(f"\t Deleted dimMember")
