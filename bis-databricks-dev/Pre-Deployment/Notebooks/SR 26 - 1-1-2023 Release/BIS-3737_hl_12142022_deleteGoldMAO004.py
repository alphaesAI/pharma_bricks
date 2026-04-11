# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
from pyspark.sql.functions import explode
from pyspark.sql.types import StructType, LongType, StructField, StringType, IntegerType, TimestampType

# COMMAND ----------

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


jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
jdbcURL = f"jdbc:sqlserver://sql-c-{EnvironmentLetter}-shrd-idap0000-01.database.windows.net:1433;database=syn-c-{EnvironmentLetter}-shrd-idap0000-01"
jdbcConnectionProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }


# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

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

# DBTITLE 1,drop Old gold Membership and Segement
#delete old table if schema isn't updated for each client
for client in clientlist:
  if client != "global":
    mao004GoldPath = f'/mnt/{client}/Gold/MA/Risk/MAO004Diagnosis'
    
    
    if path_exists(mao004GoldPath):     
      drop_deltaDir(mao004GoldPath)
      print(f"old gold risk table mao004Diagnosis dropped successfully for client: {client}!")        
       
