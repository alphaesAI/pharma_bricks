# Databricks notebook source
dbutils.widgets.text("SubNotebookName","","")
dbutils.widgets.text("SubNotebookPath","","")
dbutils.widgets.text("SubNotebookParameterValue","","")
dbutils.widgets.text("ClientContainer","","")

SubNotebookName = dbutils.widgets.get("SubNotebookName")
SubNotebookPath = dbutils.widgets.get("SubNotebookPath")
SubNotebookParameterValue = dbutils.widgets.get("SubNotebookParameterValue")
ClientContainer = dbutils.widgets.get("ClientContainer")
DynamicNotebookArgPath = "/mnt/fileconfig/JSON/NotebookConfig/NotebookArgNames.json"

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.functions import col
from pyspark.sql.functions import explode



# COMMAND ----------

# DBTITLE 1,run subnotebook with 2 parameters or no parameter
df = spark.read.format("json").option("multiLine", True).load(DynamicNotebookArgPath)
filterDF = df.filter(df.notebookname == SubNotebookName)
args = [ClientContainer, SubNotebookParameterValue]
argument_dict = {}

if filterDF.count() == 0:  
  argument_dict = {}
else:
  explodeDF = filterDF.select(explode("parameterNames").alias("p"))
  flattenDF = explodeDF.selectExpr("p.p1", "p.p2")
  p1 = flattenDF.select("*")
  l = p1.toPandas().values.tolist()
  lst = l[0]  
  for i in range(len(lst)):
    argument_dict[lst[i]] = args[i]

results = dbutils.notebook.run(SubNotebookPath, 0, argument_dict)
dbutils.notebook.exit(results)

