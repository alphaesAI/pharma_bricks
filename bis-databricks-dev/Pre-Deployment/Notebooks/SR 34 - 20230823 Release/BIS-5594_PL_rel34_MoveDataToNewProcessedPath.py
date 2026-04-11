# Databricks notebook source
# DBTITLE 1,Parameters
fullConfigPath = "/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json"


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

envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

# DBTITLE 1,Get all Clients
from pyspark.sql.functions import explode, col

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(fullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))


# COMMAND ----------

# DBTITLE 1,Defined Processed Paths
needToMoveJSON = """{
  "Paths": [
    {      
      "ProcessedPath": [
        {
          "Entity": "Age-in_AbbrevClaim",
          "currentPath": "/processed/MA/Data/Age-in_AbbrevClaim/7.12/Age-in_AbbrevClaim",
          "newPath": "/processed/MA/Data/MedicalClaims/7.12/Age-in_AbbrevClaim"
        },
        {
          "Entity": "PremeraAge-in_AbbrevClaim",
          "currentPath": "/processed/MA/Data/Age-in_AbbrevClaim/7.9/PremeraAge-in_AbbrevClaim",
          "newPath": "/processed/MA/Data/MedicalClaims/7.9/PremeraAge-in_AbbrevClaim"
        }
      ]   
    }  
  ]
}"""

# COMMAND ----------

# DBTITLE 1,Get All Processed Paths

rddJSON = sc.parallelize([needToMoveJSON]) 
dfRaw = sqlContext.read.json(rddJSON)

paths = dfRaw.select(explode("Paths").alias("Column"))
dfPaths = paths.select(explode("Column.ProcessedPath").alias("Path")).select("Path.Entity", "Path.currentPath", "Path.newPath")
display(dfPaths)

# COMMAND ----------

# DBTITLE 1,Method: Delete Files in Old Processed Folder
def deleteFiles(folderPath):
  files = dbutils.fs.ls(folderPath)
  
  for f in files:
    if f.isDir():
      deleteFiles(f.path)
    else:
      dbutils.fs.rm(f.path, recurse=True)

  #Remove root level folder path
  dbutils.fs.rm(folderPath, recurse=True)

# COMMAND ----------

# DBTITLE 1,Method: Move Data into New Processed
def moveDf(oldPath, newPath):
  oldDf = spark.read.format("parquet").load(oldPath)
  print(f"INFO: Moving Data from {oldPath} to {newPath}!")

  oldDf.write.format("parquet").mode("overwrite").save(newPath)
  print(f" INFO: Moved to {newPath}")

  #delete the actual files in datalake
  deleteFiles(oldPath)
  print(f" INFO: Deleted the files in {oldPath}")

# COMMAND ----------

# DBTITLE 1,Method: Check File Path
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Main
dfClientsCollect = dfClientsForEnvironment.collect()
dfPathsCollect = dfPaths.collect()

mountPoint = "/mnt/"

for ent in dfClientsCollect:
  clientCode = ent["Clients"]
  for path in dfPathsCollect:
    entity = path["Entity"]
    oldP = path["currentPath"]
    newP = path["newPath"]
    #get full processed paths
    fullCurrentPath = f"{mountPoint}{clientCode}{oldP}"
    fullDestPath = f"{mountPoint}{clientCode}{newP}"

    try:
      if(clientCode != "global" and path_exists(fullCurrentPath) == True):
        moveDf(fullCurrentPath, fullDestPath)
        print(f"INFO: Moved data in {clientCode} for {entity} !")
    except Exception as e:
      print(f"Error: {str(e)}")
