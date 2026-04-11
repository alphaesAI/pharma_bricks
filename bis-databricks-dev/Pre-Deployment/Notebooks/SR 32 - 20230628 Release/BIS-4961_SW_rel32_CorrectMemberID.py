# Databricks notebook source
# DBTITLE 1,Release instructions
# MAGIC %md
# MAGIC This can be run either before or after the create databricks job

# COMMAND ----------

# DBTITLE 1,ClientConfig JSON
clientAppendJSON = """{
    "Environments": [
        {
            "EnvironmentLetter": "d",
            "Clients": [
                {
                    "ClientCode": "devidap1",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "Pharmacy",
                    "FileLayoutID": "11010",
                    "DatalakePath": "/consolidated/MA/Data/Pharmacy"
                },
                {
                    "ClientCode": "devidap2",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "devidap2",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "52000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "devidap2",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                }
            ]
        },
        {
            "EnvironmentLetter": "q",
            "Clients": [
                {
                    "ClientCode": "qaidap2",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "qaidap2",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                },
                {
                    "ClientCode": "qaidap2",
                    "Entity": "Pharmacy",
                    "FileLayoutID": "11010",
                    "DatalakePath": "/consolidated/MA/Data/Pharmacy"
                },
                {
                    "ClientCode": "qaidap1",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "52000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                }
            ]
        },
        {
            "EnvironmentLetter": "s",
            "Clients": [
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "Pharmacy",
                    "FileLayoutID": "11010",
                    "DatalakePath": "/consolidated/MA/Data/Pharmacy"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "52000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                }
            ]
        },
        {
            "EnvironmentLetter": "p",
            "Clients": [
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "Pharmacy",
                    "FileLayoutID": "11010",
                    "DatalakePath": "/consolidated/MA/Data/Pharmacy"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "MedicalClaimHeader",
                    "FileLayoutID": "52000",
                    "DatalakePath": "/consolidated/MA/Data/MedicalClaimHeader"
                },
                {
                    "ClientCode": "premera",
                    "Entity": "GoldenClaimHistory",
                    "FileLayoutID": "1000",
                    "DatalakePath": "/Gold/MA/Client/GoldenClaimHistory"
                }
            ]
        }
    ]
}
"""
# print(clientJSON)

# COMMAND ----------

# DBTITLE 1,Deletion config
clientDeleteJSON = """{
    "Environments": [
        {
            "EnvironmentLetter": "d",
            "Clients": [
                {
                    "ClientCode": "devidap1",
                    "Entity": "MedicalGoldenClaimDiagnosis",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimDiagnosis"
                },
                {
                    "ClientCode": "devidap1",
                    "Entity": "MedicalGoldenClaimLineProcCodes",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimLineProcCodes"
                }
            ]
        },
        {
            "EnvironmentLetter": "q",
            "Clients": [
                {
                    "ClientCode": "qaidap2",
                    "Entity": "MedicalGoldenClaimDiagnosis",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimDiagnosis"
                },
                {
                    "ClientCode": "qaidap2",
                    "Entity": "MedicalGoldenClaimLineProcCodes",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimLineProcCodes"
                }
            ]
        },
        {
            "EnvironmentLetter": "s",
            "Clients": [
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalGoldenClaimDiagnosis",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimDiagnosis"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalGoldenClaimLineProcCodes",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimLineProcCodes"
                }
            ]
        },
        {
            "EnvironmentLetter": "p",
            "Clients": [
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalGoldenClaimDiagnosis",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimDiagnosis"
                },
                {
                    "ClientCode": "bcbsks",
                    "Entity": "MedicalGoldenClaimLineProcCodes",
                    "DatalakePath": "/Gold/MA/Client/MedicalGoldenClaimLineProcCodes"
                }
            ]
        }
    ]
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

# DBTITLE 1,Clients and entities for Appending
from pyspark.sql.functions import explode, col

#Read the config file
# dfConfigFile = spark.read.format("json").option("multiline",True).load(clientJSON)
rddAppendJSON = sc.parallelize([clientAppendJSON]) 
dfAppendConfigFile = sqlContext.read.json(rddAppendJSON)
#Split out environments into column
dfAppendEnvironmentsConfigFile = dfAppendConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfAppendEnvironmentConfigFile = dfAppendEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfAppendClientsForEnvironment = dfAppendEnvironmentConfigFile.select(explode("Clients").alias("Clients")).select("Clients.ClientCode","Clients.Entity","Clients.FileLayoutID","Clients.DatalakePath")

display(dfAppendClientsForEnvironment)
#dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Clients and entities for deleting
from pyspark.sql.functions import explode, col

#Read the config file
# dfConfigFile = spark.read.format("json").option("multiline",True).load(clientJSON)
rddDeleteJSON = sc.parallelize([clientDeleteJSON]) 
dfDeleteConfigFile = sqlContext.read.json(rddDeleteJSON)
#Split out environments into column
dfDeleteEnvironmentsConfigFile = dfDeleteConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfDeleteEnvironmentConfigFile = dfDeleteEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfDeleteClientsForEnvironment = dfDeleteEnvironmentConfigFile.select(explode("Clients").alias("Clients")).select("Clients.ClientCode","Clients.Entity","Clients.DatalakePath")

display(dfDeleteClientsForEnvironment)
#dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

def updatePMID(entity, flid, path):

  print(f"\tCreating dataframe for {entity}")
  dfFile = spark.read.format("delta").option("header", "true").load(path)
  dfFile.createOrReplaceTempView(entity)

  print(f"\tUpdating records")
  
  updateSQL = f"""
    UPDATE {entity}
    SET PlanMemberID = concat(PlanMemberID,'00')
    WHERE LEN(PlanMemberID) = 9
    AND FileLayoutID = {flid}
  """

  # print(updateSQL)
  spark.sql(updateSQL)

# COMMAND ----------

def deleteData(entity,path):
  print(f"\tCreating dataframe for {entity}")
  dfFile = spark.read.format("delta").option("header", "true").load(path)
  dfFile.createOrReplaceTempView(entity)

  print("\tBegin deteling records")

  deleteSQL = f"""
  DELETE FROM {entity}
  """
  
  spark.sql(deleteSQL)

# COMMAND ----------

# DBTITLE 1,Main PlanMemberID appending
MountPoint = "/mnt/"

EntityAppCollect = dfAppendClientsForEnvironment.collect()

for ent in EntityAppCollect:
  clientCode = ent["ClientCode"]
  entity = ent["Entity"]
  flid = ent["FileLayoutID"]
  dlPath = ent["DatalakePath"]
  fullPath = f"{MountPoint}{clientCode}{dlPath}"
  
  print(f"Begin appending for Client: {clientCode}, Entity: {entity}, FileLayoutID: {flid}")

  try:
    if(path_exists(fullPath)):
      updatePMID(entity, flid, fullPath)
  
  except Exception as e:
    print(str(e))
  

# COMMAND ----------

# DBTITLE 1,Main delete data
MountPoint = "/mnt/"

EntityDelCollect = dfDeleteClientsForEnvironment.collect()

for ent in EntityDelCollect:
  clientCode = ent["ClientCode"]
  entity = ent["Entity"]
  dlPath = ent["DatalakePath"]
  fullPath = f"{MountPoint}{clientCode}{dlPath}"
  
  print(f"Begin deleting for Client: {clientCode}, Entity: {entity}")

  try:
    if(path_exists(fullPath)):
      deleteData(entity, fullPath)
  
  except Exception as e:
    print(str(e))
  
