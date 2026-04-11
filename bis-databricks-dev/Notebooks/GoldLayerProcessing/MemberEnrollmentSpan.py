# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
clientContainer = dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,Source Table (Consolidation Member Enrollment)
SourceFileLocation = "/mnt/" + clientContainer + "/consolidated/MA/Data/MemberEnrollment" 
dfSourceFile = spark.read.format("delta").option("header","true").load(SourceFileLocation)

# COMMAND ----------

# MAGIC %run "./SpanProcessingRules"

# COMMAND ----------

df = SpanProcessingRules(dfSourceFile)
df.show()
