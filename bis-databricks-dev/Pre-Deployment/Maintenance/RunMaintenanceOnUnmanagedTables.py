# Databricks notebook source
# DBTITLE 1,RELEASE INSTRUCTIONS
# MAGIC %md
# MAGIC ###This notebook requires a job to be created in each environment 

# COMMAND ----------

dbutils.widgets.text("ClientContainer","","") #should be empty since this needed for the dataprocessing framework but isn't needed for this processing
dbutils.widgets.text("ConfigPath","","") 

clientContainer = dbutils.widgets.get("ClientContainer")
configPath = dbutils.widgets.get("ConfigPath")

mountPoint = "/mnt/"
fileConfig = "fileconfig"
fullConfigPath = mountPoint + fileConfig + configPath

print(fullConfigPath)

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
dfConfigFile = spark.read.format("json").option("multiline",True).load(fullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Check if database exists
def databaseExists(databaseToCheck):
  databases = spark.catalog.listDatabases()
  return next((t for t in databases if t.name == databaseToCheck), None)

# COMMAND ----------

# DBTITLE 1,Create Schema for table list
from pyspark.sql.types import StructType,StructField, StringType, IntegerType

schema = StructType([ \
    StructField("name",StringType(),True), \
    StructField("catalog",StringType(),True), \
    StructField("namespace",StringType(),True), \
    StructField("description", StringType(), True), \
    StructField("tableType", StringType(), True), \
    StructField("isTemporary", StringType(), True) \
  ])

emptyRDD = spark.sparkContext.emptyRDD()
dfDataBase = spark.createDataFrame(emptyRDD,schema)

# COMMAND ----------

# DBTITLE 1,Method: maintenanceMode (using this to loop through a dataframe and perform maintenance for each table record)
def maintenanceMode(df):
  for t in df.collect():
    tn = t["tableName"]

    print(f"  INFO: Begin maintenance: {tn}")

    if (checkTableDelta(tn)==True):
      vacuumTable(tn)
      optimizeTable(tn)
    else:
      print(f"\t WARNING: ******* {tn} cannot be optimized. This table is not in delta format")

# COMMAND ----------

# DBTITLE 1,Method: checkTableDelta - Checks if table is based on the delta format  
def checkTableDelta(t):
  tempBoolean = True

  sqlStatement = f"DESCRIBE TABLE EXTENDED {t}" 
  dfTableSchema = spark.sql(sqlStatement)

  if (dfTableSchema.filter("col_name = 'Provider' and data_type = 'delta'").count() > 0):
    tempBoolean = True
  else:
    tempBoolean = False

  return tempBoolean

# COMMAND ----------

# DBTITLE 1,Method: optimizeTable
def optimizeTable(t):
  print(f"\t --Optimizing {t}")

  optimizeSQL = f"OPTIMIZE {t}"
  # print(optimizeSQL)

  spark.sql(optimizeSQL)

# COMMAND ----------

# DBTITLE 1,Method: vacuumTable
def vacuumTable(t):
  print(f"\t --Vacuuming {t}")

  vacuumSQL = f"VACUUM {t}"
  # print(vacuumSQL)

  spark.sql(vacuumSQL)

# COMMAND ----------

# DBTITLE 1,Loop through all clients in this environment and get all tables by clientid
databases = dfClientsForEnvironment.collect()

for database in databases:
  client = database["Clients"]

  if(databaseExists(client)):
    print(f"INFO: Start maintenance: {client}")
    databaseTables = spark.catalog.listTables(database["Clients"])
    dfTables = spark.createDataFrame(databaseTables, schema).cache()     
    dfTables.createOrReplaceTempView(client)

    tableQuery = f"""
            SELECT 
               concat(replace(replace(namespace,'[',''),']',''),'.',name) as tableName
            FROM {client}
            WHERE
            tableType = 'EXTERNAL'
    """

    dfTables = spark.sql(tableQuery).cache()

    maintenanceMode(dfTables)

  else:
    print('EXCEPTION: database does not exist - ' + client)
