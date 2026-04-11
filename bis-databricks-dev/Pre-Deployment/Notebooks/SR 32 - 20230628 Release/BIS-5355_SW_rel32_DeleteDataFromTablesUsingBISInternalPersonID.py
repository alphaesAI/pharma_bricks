# Databricks notebook source
# DBTITLE 1,Release instructions
# MAGIC %md
# MAGIC This needs to be run before the create databricks job due to a datamodel change
# MAGIC

# COMMAND ----------

# DBTITLE 1,ClientConfig JSON
clientJSON = """
{
    "Environments": [
        {
            "EnvironmentLetter": "d",
            "Clients": ["devidap1", "devidap2"]
        },
        {
            "EnvironmentLetter": "q",
            "Clients": ["qaidap1", "qaidap2"]
        },
        {
            "EnvironmentLetter": "s",
            "Clients": ["bcbsks", "vba", "wahp", "nbnd"]
        },
        {
            "EnvironmentLetter": "p",
            "Clients": ["bcbsks","vba"]
        }
    ],
    "Tables": ["gold_ma_member", "gold_ma_memberpersonbridge", "gold_ma_pcpattribution", "platinum_dimmember", "platinum_factgapsincare", "platinum_factgapsincarerr", "platinum_factmemberrevenuegap", "platinum_factmonthlymembercdialert"]
}
"""
# print(clientJSON)

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
# dfConfigFile = spark.read.format("json").option("multiline",True).load(clientJSON)
rddJSON = sc.parallelize([clientJSON]) 
dfConfigFile = sqlContext.read.json(rddJSON)

#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Env"),"Tables")

#Split out all of the individual environments and filter by the current environment
dfEnvBreakoutConfigFile = dfEnvironmentsConfigFile.select("Env.EnvironmentLetter", "Env.Clients", "Tables").filter(col("Env.EnvironmentLetter") == envLetter)

#Split out clients
dfClientsForEnvironment = dfEnvBreakoutConfigFile.select(explode("Clients").alias("ClientCode"),"Tables")

display(dfClientsForEnvironment)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Tables to delete data from
# MAGIC - gold_ma_member
# MAGIC - gold_ma_memberpersonbridge
# MAGIC - gold_ma_pcpattribution
# MAGIC - platinum_dimmember
# MAGIC - platinum_factgapsincare
# MAGIC - platinum_platinum_factgapsincarerr
# MAGIC - platinum_factmemberrevenuegap
# MAGIC - platinum_platinum_factmonthlymembercdialert

# COMMAND ----------

def deleteData(client, tables):

  for tab in tables: 
    deleteSQL = f"DELETE FROM {client}.{tab};"
    print(f"  INFO: {deleteSQL}")

    spark.sql(deleteSQL)

# COMMAND ----------

# DBTITLE 1,Main delete data
EntityDelCollect = dfClientsForEnvironment.collect()

for ent in EntityDelCollect:
  clientCode = ent["ClientCode"]
  tables = ent["Tables"]
  print(f"INFO: Begin deleting for Client: {clientCode}")

  try:
    deleteData(clientCode, tables)

  except Exception as e:
    print(str(e))
