# Databricks notebook source
# DBTITLE 1,Release instructions
# MAGIC %md
# MAGIC ####This needs to be executed anytime before the create databricks database job

# COMMAND ----------

# DBTITLE 1,Variable to hold the list of tables to be moved
tableJSON = """
{
    "Tables": [
        {
            "Name": "MemberConditionGap - Processed",
            "CurrentPath": "/mnt/#clientCode/processed/ACA/Data/ACAMemberConditionGap/V1.1/ACAMemberConditionGap",
            "NewPath": "/mnt/#clientCode/processed/ACA/Data/MemberConditionGap/V1.1/ACAMemberConditionGap",
            "Format": "parquet"
        },
        {
            "Name": "ChaseList - Processed",
            "CurrentPath": "/mnt/#clientCode/processed/COMM/Data/COMMChaseList/V1.0/COMMChaseList",
            "NewPath": "/mnt/#clientCode/processed/COMM/Data/ChaseList/V1.0/COMMChaseList",
            "Format": "parquet"
        },
        {
            "Name": "RADVChaseList - Processed",
            "CurrentPath": "/mnt/#clientCode/processed/COMM/Data/COMMRADVChaseList/V1.0/COMMRADVChaseList",
            "NewPath": "/mnt/#clientCode/processed/COMM/Data/ChaseList/V1.0/COMMRADVChaseList",
            "Format": "parquet"
        },
        {
            "Name": "RMChaseList - Processed",
            "CurrentPath": "/mnt/#clientCode/processed/COMM/Data/COMMRMChaseList/V1.0/COMMRMChaseList",
            "NewPath": "/mnt/#clientCode/processed/COMM/Data/ChaseList/V1.0/COMMRMChaseList",
            "Format": "parquet"
        },
        {
            "Name": "MemberConditionGap - Consolidation",
            "CurrentPath": "/mnt/#clientCode/consolidated/ACA/Data/ACAMemberConditionGap",
            "NewPath": "/mnt/#clientCode/consolidated/ACA/Data/MemberConditionGap",
            "Format": "delta"
        },
        {
            "Name": "Product - Consolidation",
            "CurrentPath": "/mnt/#clientCode/consolidated/ACA/Data/ACAProduct",
            "NewPath": "/mnt/#clientCode/consolidated/ACA/Data/Product",
            "Format": "delta"
        },
        {
            "Name": "Provider - Consolidation",
            "CurrentPath": "/mnt/#clientCode/consolidated/ACA/Data/ACAProvider",
            "NewPath": "/mnt/#clientCode/consolidated/ACA/Data/Provider",
            "Format": "delta"
        },
        {
            "Name": "MemberEnrollment - Consolidation",
            "CurrentPath": "/mnt/#clientCode/consolidated/ACA/Data/Enrollment",
            "NewPath": "/mnt/#clientCode/consolidated/ACA/Data/MemberEnrollment",
            "Format": "delta"
        },
        {
            "Name": "ChaseList - Consolidation",
            "CurrentPath": "/mnt/#clientCode/consolidated/COMM/Data/COMMChaseList",
            "NewPath": "/mnt/#clientCode/consolidated/COMM/Data/ChaseList",
            "Format": "delta"
        }
    ]
}
"""
# print(clientJSON)

# COMMAND ----------

# DBTITLE 1,Variable to hold the client by env json
FullConfigPath = "/mnt/fileconfig/JSON/Clients/ClientsByEnvironment.json"
# print(FullConfigPath)

# COMMAND ----------

# DBTITLE 1,Method: getEnvLetter()
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

envLetter = getEnvLetter()
print (envLetter)

# COMMAND ----------

# DBTITLE 1,Get a dataframe to hold the clients by environment
from pyspark.sql.functions import explode, col, sha2, concat_ws, coalesce, lit

#Read the config file
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

display(dfClientsForEnvironment)

# COMMAND ----------

# DBTITLE 1,Get a dataframe to hold the tables to be moved
#Read the tableJSON
rddJSON = sc.parallelize([tableJSON]) 
dfTableJson = spark.read.json(rddJSON)
#Split out tables into separate records
dfTables = dfTableJson.select(explode("Tables").alias("Tables"))
#split out all of the columns
dfTableInfo = dfTables.select("Tables.Name", "Tables.CurrentPath", "Tables.NewPath", "Tables.Format")

display(dfTableInfo)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Tables to move
# MAGIC - MemberConditionGap
# MAGIC - Product
# MAGIC - Provider
# MAGIC - MemberEnrollment
# MAGIC - Chaselist

# COMMAND ----------

# DBTITLE 1,Method: path_exists()
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Method: delete_data
def delete_data(p):
  print(f"    INFO: Deleting Original Path Data")
  files = dbutils.fs.ls(p)
  
  for f in files:
    if f.isDir():
      delete_data(f.path)
    else:
      dbutils.fs.rm(f.path, recurse=True)

  #Remove root level folder path
  dbutils.fs.rm(p, recurse=True)

# COMMAND ----------

# DBTITLE 1,Method: MigrateData
def migrate_data(currentPath,newPath,frmt):
  print(f"    INFO: Moving to New Path: {newPath}")
  
  try:
    #load records into dataframe
    dfCurrent = spark.read.format(frmt).option("header","true").load(currentPath)
    
    #write records to new location
    dfCurrent.write.format(frmt).mode("overwrite").option("mergeSchema","true").save(newPath)
    # print(dfCurrent.count())
    
    #delete original path
    delete_data(currentPath)
  except Exception as e:
    print(f"    ERROR: {str(e)}")

# COMMAND ----------

# DBTITLE 1,Method: MoveTables
def move_tables(clientCode,tableCollection):
  for table in tableCollection:
    tName = table["Name"]
    cPath = table["CurrentPath"].replace("#clientCode",clientCode)
    nPath = table["NewPath"].replace("#clientCode",clientCode)
    fmt = table["Format"]

    print(f"  INFO: Begin Table: {tName}")
    print(f"    INFO: Checking Current Path For Existence: {cPath}")
    
    if(path_exists(cPath)):
      migrate_data(cPath,nPath,fmt)
    else:
      print(f"    INFO: Current Path Does Not Exist")

# COMMAND ----------

# DBTITLE 1,Main
clientsCollect = dfClientsForEnvironment.collect()
tablesCollect = dfTableInfo.collect()

for client in clientsCollect:
  clientCode = client["Clients"]
  print(f"INFO: Begin: {clientCode}")

  move_tables(clientCode, tablesCollect)
  print("\n")
