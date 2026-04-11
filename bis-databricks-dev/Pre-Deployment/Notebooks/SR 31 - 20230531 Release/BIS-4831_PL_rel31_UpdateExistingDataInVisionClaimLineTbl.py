# Databricks notebook source
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

from pyspark.sql.functions import explode, col, substring, when, expr

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

def updateColumns(path):
  oldDf = spark.read.format("delta").load(path)
  rawDf = oldDf.withColumn("ProcCodeType_new", expr("CASE WHEN ProcCodeType IS NULL AND ProcCode BETWEEN 00000 AND 99999 AND LENGTH(ProcCode) = 5 THEN 'CPTCode'" +
 "WHEN ProcCodeType IS NULL AND SUBSTRING(ProcCode,1,1) BETWEEN 'A' AND 'Z' AND SUBSTRING(ProcCode,2,5) BETWEEN 0000 AND 9999 AND LENGTH(ProcCode)= 5 THEN 'HCPCSCode'" +
 "WHEN ProcCodeType IS NULL THEN 'Unknown'" +
 "WHEN ProcCodeType IS NOT NULL THEN ProcCodeType END"))               
  
  finalDf = rawDf.drop("ProcCodeType")\
                 .withColumnRenamed("ProcCodeType_new", "ProcCodeType")
    
  finalDf.write.format("delta").mode("overwrite").option("mergeSchema","true").save(path)

# COMMAND ----------

clients = dfClientsForEnvironment.collect()

for c in clients:
  print(c["Clients"])
  try:
    clientCode = c["Clients"]

    TablePath = fr"/mnt/{clientCode}/consolidated/MA/Data/VisionClaimLine"
    
    if(path_exists(TablePath)):
      updateColumns(TablePath)
  except Exception as e:
    print(str(e))
