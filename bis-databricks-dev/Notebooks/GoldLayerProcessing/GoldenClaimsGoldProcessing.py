# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","") ####No value needed

clientCode = dbutils.widgets.get("ClientContainer")

mntPnt = '/mnt/'

# COMMAND ----------

# DBTITLE 1,Setup table configs
tableConfig = """
{
  "DestinationTableName": "GoldenClaimHistory", 
  "DestinationTablePath": "#clientCode/Gold/MA/Client/GoldenClaimHistory",
  "SourceTables": [
    {
      "TableName": "GoldenClaim",
      "TablePath": "#clientCode/Gold/MA/Client/GoldenClaim",
      "TableFormat": "delta"
    }
  ]
}
"""

# COMMAND ----------

# DBTITLE 1,Ingest Golden Claim Helper notebook
# MAGIC %run ./GoldenClaimHelper

# COMMAND ----------

# DBTITLE 1,Available DataSources
dataSources = """
{
  "DataSources": [
    {
      "DataSourceName":"FCF", 
      "DataSourceNotebook":"./FCFGoldenClaimProcess"
    },
    {
      "DataSourceName":"QNXT", 
      "DataSourceNotebook":"./QNXTGoldenClaimProcess"
    }
  ]  
}
"""

# COMMAND ----------

# DBTITLE 1,Load DataSources
from pyspark.sql.functions import explode

dataSourceList = []
dataSourceList.append(dataSources)
dsDF = spark.read.json(sc.parallelize(dataSourceList)).select(explode("DataSources")).select("col.DataSourceName","col.DataSourceNotebook")
dsDF.createOrReplaceTempView("DataSources")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM DataSources

# COMMAND ----------

# DBTITLE 1,Loop DataSources
returnStr = ""

clmCnt = clmDF.head()[0]

try:
  if (clmCnt > 0):
    #delete all golden claims for the client table mounted
    DeleteGC()

    #iterate through each entity records 
    for row in dsDF.collect():
      DataSourceName = row['DataSourceName']
      DataSourceNotebook = row['DataSourceNotebook']
      print(f"Running {DataSourceNotebook}")

      try:
        dbutils.notebook.run(DataSourceNotebook, 0, {
                                      "ClientContainer": clientCode
                                    ,"DataSourceName": DataSourceName
                                  })
        returnStr += f"{DataSourceName} completed with success\r\n"
      except Exception as e:
        returnStr += f"{DataSourceName} completed with failure. More information: " + str(e)

      #insert all sources from golden claims into golden claims history -- after they have run
      InsertGCHistory()
      returnStr += ""
except Exception as e:
      returnStr += str(e)
finally:
      dbutils.notebook.exit(returnStr)
