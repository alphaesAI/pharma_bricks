# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("WizardOrchestratorJSON","","")

WizardOrchestrator = dbutils.widgets.get("WizardOrchestratorJSON")
WizardOrchestratorpath = "/mnt/fileconfig/" + WizardOrchestrator
clientContainer =  dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,import
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, ArrayType, LongType, TimestampType, BooleanType
from pyspark.sql.functions import explode
from pyspark.sql.functions import lit
from pyspark.sql.functions import sha2
from pyspark.sql.functions import concat_ws

# COMMAND ----------

# DBTITLE 1,function to validate path
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Flatten configuration
Entity_schema = StructType(fields=[
    StructField('ExportAuditTable', StringType(), False),
    StructField('ExportAuditTableMountPoint', StringType(), True),
    StructField('ExportAuditTrackingTable', StringType(), False),
    StructField('ExportAuditTrackingTableMountPoint', StringType(), True),
    StructField(
        'Entities', ArrayType(
            StructType([
                StructField('Entity', StringType(), True),
                StructField('ConfigFile', StringType(), True),
                StructField('ErrorConfigFile', StringType(), True),
                StructField('ConfigMountPoint', StringType(), True), 
                StructField('LOB', StringType(), True),
                StructField('SourceLayer', StringType(), True),
                StructField('BatchSize', IntegerType(), True)
            ])
        )
    )
])

df = spark.read.format("json").option("multiline", "true").json(WizardOrchestratorpath, schema=Entity_schema)

entity_df = df.select("ExportAuditTable","ExportAuditTableMountPoint","ExportAuditTrackingTable","ExportAuditTrackingTableMountPoint",
    explode("Entities").alias("EntitiesExplode")
).select("ExportAuditTable","ExportAuditTableMountPoint","ExportAuditTrackingTable","ExportAuditTrackingTableMountPoint", "EntitiesExplode.*")

entity_df.createOrReplaceTempView("TempEntity")  

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM TempEntity

# COMMAND ----------

# DBTITLE 1,Determine Mount Point
def getMountPoint(Path, MountName):
  mountPath = ""
  DataLakeMountPoint = "/mnt/"
  ExportMountPoint = "/mnt/export"
  FileConfigMountPoint = "/mnt/fileconfig/"

  if (MountName == "DataLake"):
    mountPath = DataLakeMountPoint + Path
  elif(MountName == "Export"):
    mountPath = ExportMountPoint + Path
  elif(MountName == "FileConfig"):
    mountPath = FileConfigMountPoint + Path
  
  return mountPath

# COMMAND ----------

# DBTITLE 1,Main Execution
returnStr = ""
entity_psdf = entity_df.select("*").collect()

Entity = ""
SourceTable = ""
SourceTableMountPoint = ""
BatchTable = ""
BatchTableMountPoint = ""
LOB = ""
Layer = ""
BatchSize = -1

try:
  #iterate through each entity records 
  for row in entity_psdf:
      Entity = row['Entity']
      ConfigMountPoint = row['ConfigMountPoint']
      ErrorConfigFile = row['ErrorConfigFile']
      ErrorConfigFilePath = getMountPoint(ErrorConfigFile,ConfigMountPoint)

      #run export portion via another notebook
      try:
        if(ErrorConfigFile != ""):
          dbutils.notebook.run("WizardErrorValidation", 0, {
                                      "ClientContainer": clientContainer
                                     ,"ConfigFile": ErrorConfigFilePath
                                   })
        
          returnStr += "SUCCESS"
      except Exception as e:
        returnStr += "FAILURE: " + str(e)

  returnStr += ""
except Exception as e:
      returnStr += str(e)
finally:
      dbutils.notebook.exit(returnStr)
