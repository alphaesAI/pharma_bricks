# Databricks notebook source
# DBTITLE 1,Parameters
clientCode = 'global'
deleteRootPath = """
{"Path":"global/OperationalData/RAQ/TepAlert"}
"""

# COMMAND ----------

# DBTITLE 1,Get Root Folder Path
rddJSON = sc.parallelize([deleteRootPath]) 
dfRaw = sqlContext.read.json(rddJSON)

display(dfRaw)

# COMMAND ----------

# DBTITLE 1,Method: Delete Files in current Folder
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

# DBTITLE 1,Method: Check File Path
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Main
dfPathsCollect = dfRaw.collect()

mountPoint = "/mnt/"

for path in dfPathsCollect:
  Path = path["Path"]
  fullCurrentPath = f"{mountPoint}{Path}"
    
  try:
    if(path_exists(fullCurrentPath)):  
      deleteFiles(fullCurrentPath)
      print(f"INFO: Delete files and folder in {clientCode} in {Path} !")
  except Exception as e:
    print(f"Error: {str(e)}")
