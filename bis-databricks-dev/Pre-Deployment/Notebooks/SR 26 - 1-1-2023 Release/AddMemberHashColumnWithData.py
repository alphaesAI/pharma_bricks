# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, ArrayType
from pyspark.sql.functions import explode
from pyspark.sql.functions import concat,concat_ws
from pyspark.sql.functions import sha2

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
  
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
jdbcURL = f"jdbc:sqlserver://sql-c-{EnvironmentLetter}-shrd-idap0000-01.database.windows.net:1433;database=syn-c-{EnvironmentLetter}-shrd-idap0000-01"
jdbcConnectionProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

def addHashColumn (MemberPath):
  if path_exists(MemberPath):
    Mbrdf = spark.read.format("delta").load(MemberPath)

    #add new hash column with value
    Mbrdf.withColumn("FullRowHash", sha2(concat_ws("|", *Mbrdf.columns), 256))\
    .write\
    .format("delta")\
    .mode("overwrite")\
    .option("overwriteSchema", "true")\
    .save(MemberPath)

  return True    

# COMMAND ----------

def get_dir_content(ls_path):
  dir_paths = dbutils.fs.ls(ls_path)
  subdir_paths = [get_dir_content(p.path) for p in dir_paths if p.isDir()]
  flat_subdir_paths = [p for subdir in subdir_paths for p in subdir]
  return list(map(lambda p: p.path, dir_paths)) + flat_subdir_paths
    

# COMMAND ----------

def cleanUpCheckpt (items): 
  removed= False
  for item in items:
    if item[-1] !="/":
      dbutils.fs.rm(item)
  for item in items:
    if item[-1] =="/":
      dbutils.fs.rm(item)
  removed= True
  return removed

# COMMAND ----------

def cleanupSynapseMember (tableName,connectionProperties):
  truncated = False
  emptydf = spark.createDataFrame([], StructType([]))
  #truncate the table
  emptydf.write.mode("overwrite").option("truncate", True).jdbc(url=jdbcURL, table=tableName, properties=connectionProperties)
  truncated = True
  return truncated 

# COMMAND ----------

def delete_mounted_dir(FolderPath):
  files = dbutils.fs.ls(FolderPath)
  
  for f in files:
    if f.isDir():
      delete_mounted_dir(f.path)
    else:
      dbutils.fs.rm(f.path, recurse=True)

  #Remove root level folder path
  dbutils.fs.rm(FolderPath, recurse=True)

# COMMAND ----------

#main execution
try:
  returnStr = ""
  LOB = ['MA', 'ACA']
  for client in clientlist:  
    if client != "global": 
      for lob in LOB:
        print(client, lob)
        MemberPath = f'/mnt/{client}/consolidated/{lob}/Data/Member'
         #add hash comumn in member
        addHashColumn (MemberPath)
        #clean up checkpoint MA
        checkPointPath = f'{MemberPath}/Checkpoint-Member/'        
        if path_exists(checkPointPath): 
          delete_mounted_dir(checkPointPath)
          print(checkPointPath + ' removed!')
          #remove check point
          #dirContent = get_dir_content(checkPointPath)
          
          #if cleanUpCheckpt (dirContent):
          #  dbutils.fs.rm(checkPointPath)
          #  print(checkPointPath + ' removed!')
            
          #truncate synapse member table
          memberTable = f'{client}.Member'                   
          cleanupSynapseMember(memberTable, jdbcConnectionProperties)
          print(memberTable + ' truncated')
          
  returnStr = "Script completed successful!"
  
except Exception as e:
  returnStr += str(e)
  

dbutils.notebook.exit(returnStr)
