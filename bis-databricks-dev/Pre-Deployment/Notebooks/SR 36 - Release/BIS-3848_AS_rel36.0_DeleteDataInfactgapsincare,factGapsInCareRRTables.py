# Databricks notebook source
# DBTITLE 1,Release instructions
# MAGIC %md
# MAGIC This needs to be run before the create databricks job due to a datamodel change
# MAGIC

# COMMAND ----------

# DBTITLE 1,ClientConfig JSON
FullConfigPath = "/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json"

# COMMAND ----------

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

envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

# DBTITLE 1,Clients
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

def deleteData(client, table):
  deleteSQL = f"TRUNCATE TABLE {client}.{table};"
  print(f"  INFO: {deleteSQL}")
  spark.sql(deleteSQL)

# COMMAND ----------

# DBTITLE 1,Main delete data
EntityDelCollect = dfClientsForEnvironment.collect()

for ent in EntityDelCollect:
  clientCode = ent["Clients"]
  if(clientCode != "global"):
    print(f"INFO: Begin deleting for Client: {clientCode}")

    try:
      deleteData(clientCode, "platinum_factgapsincare")
      deleteData(clientCode, "platinum_factgapsincarerr")

    except Exception as e:
      print(str(e))
