# Databricks notebook source
# DBTITLE 1,Parameters For Config File Path
dbutils.widgets.text("FileConfigMount","","")
dbutils.widgets.text("ConfigurationFile","","")

fileConfigMount = dbutils.widgets.get("FileConfigMount")  #"/mnt/fileconfig/"
configurationFile = dbutils.widgets.get("ConfigurationFile")  #"JSON/Clients/ClientsByEnvironment.json"
FullConfigPath = fileConfigMount + configurationFile

print(FullConfigPath)

# COMMAND ----------

# DBTITLE 1,Method: getEnvLetter
def getEnvLetter():
  dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
  envLetter = ""  

  if(dbEnv == "934226345849410"):
    envLetter = "d" 
  elif(dbEnv == "5826678703751685"):
    envLetter = "q" 
  elif(dbEnv == "7093677384385470"):
    envLetter = "s" 
  else:
    envLetter = "p" 
    
  return envLetter

# COMMAND ----------

# DBTITLE 1,Get Environment Letter
envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

# DBTITLE 1,Read Clients From Clients.json File (For Environment)
from pyspark.sql.functions import explode, col

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

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

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Loop through all clients in this environment and get all tables by clientid
databases = dfClientsForEnvironment.collect()
#remove Risk related paths
fileList = ['/mnt/#clientCode/Gold/MA/Risk/MedicalGoldenClaimDiagnosis','/mnt/#clientCode/Gold/MA/Risk/MedicalGoldenClaimLineProcCodes']

for database in databases:
  ClientCode = database["Clients"]
  print("Running: " + ClientCode)
  
  for file in fileList:
    FullPath = file.replace("#clientCode", ClientCode)
    if(pathExists(FullPath)):
      print("Deleting: " + FullPath)
      delete_mounted_dir(FullPath)
    else:
      print("Path does not exist for client: " + ClientCode)
