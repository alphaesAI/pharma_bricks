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


gchSchema = StructType([
  StructField('GeneratedGoldenClaimsUniqueKey', StringType(), False),
  StructField('GeneratedMedicalClaimsUniqueKey', StringType(), False),
  StructField('ClientID', StringType(), False),
  StructField('FileLayoutID', IntegerType(), False),
  StructField('FileLayoutDescription', StringType(), False),
  StructField('ClaimNumber', StringType(), False),
  StructField('OriginalClaimNumber', StringType(), True),
  StructField('BeneficiaryID', StringType(), True),
  StructField('PlanMemberID', StringType(), True),
  StructField('CMSContractNumber', StringType(), True),
  StructField('BillTypeCode', StringType(), True),
  StructField('ClaimTypeInd', StringType(), True),
  StructField('ClaimWeight', LongType(), False),
  StructField('ClaimStatus', StringType(), True),
  StructField('ClaimProcessDate', TimestampType(), True),
  StructField('ClaimSource', StringType(), True),
  StructField('LoadTimestamp', TimestampType(), False)  
  ])

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

def path_exists(path):
  stat = False
  try:
    dbutils.fs.ls(path)
    stat = True
  except Exception as e:
    stat = False 
  return stat

# COMMAND ----------

#note this code drop existing GoldenClaimHistory delta table and recreate it from copying synapse. So it should be only run before the new goldenclaim start in production
for client in clientlist:
  if client != "global":    
    pushDownQuery = f'select * from {client}.GoldenClaimHistory'
    gchFolderPath = f"/mnt/{client}/consolidated/MA/Data/GoldenClaimHistory"
    
    dfgch = spark.read.format("jdbc"). \
      options(url=jdbcURL,
              driver='com.microsoft.sqlserver.jdbc.SQLServerDriver',            
              query=pushDownQuery,
              user=jdbcUsername,
              password=jdbcPassword).load()

    if path_exists(gchFolderPath):
      drop_deltaDir(gchFolderPath)
      
    #copy synapse GoldenClaimHistory to consolidate
    dfgch.write.format("delta").option("forceSchema", gchSchema).mode("append").save(gchFolderPath)  

