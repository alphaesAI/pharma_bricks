# Databricks notebook source
# DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConsolidatedPath","","")
dbutils.widgets.text("DestTable","","")
dbutils.widgets.text("CheckPoint","","")

clientContainer = dbutils.widgets.get("ClientContainer")
consolidatedPath = dbutils.widgets.get("ConsolidatedPath")
destTable = dbutils.widgets.get("DestTable")
checkPoint = dbutils.widgets.get("CheckPoint")

print("clientContainer: " + clientContainer)
print("consolidatedPath: " + consolidatedPath)
print("destTable: " + destTable)
print("checkPoint: " + checkPoint)

# COMMAND ----------

# DBTITLE 1,Import libraries
from pyspark.sql.functions import explode, col,lit
import json

# COMMAND ----------

# DBTITLE 1,Run SQL ConnectionNotebook
# MAGIC %run "../GoldAndPlatinumSynapseForDemo/SetupSQLConnectionJDBC"

# COMMAND ----------

# DBTITLE 1,Get Parameters (Scala)
# MAGIC %scala 
# MAGIC val destTable = dbutils.widgets.get("DestTable")

# COMMAND ----------

# DBTITLE 1,Truncate table (Scala)
# MAGIC %scala 
# MAGIC val sqlStatment = """TRUNCATE TABLE """ + destTable
# MAGIC         
# MAGIC import java.sql.DriverManager
# MAGIC import java.sql.Connection
# MAGIC import java.util.Properties
# MAGIC 
# MAGIC val conection = DriverManager.getConnection(jdbcURL, connectionProperties)
# MAGIC val statement = conection.createStatement()
# MAGIC 
# MAGIC statement.execute(sqlStatment)
# MAGIC statement.close()

# COMMAND ----------

# DBTITLE 1,Setup Polybase connections
sparkPath = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"
spark.conf.set(sparkPath, blobKey)
tempDir = "wasbs://"+clientContainer+"@svtss"+envLetter+"idap01s.blob.core.windows.net/stream-temp"

# COMMAND ----------

# DBTITLE 1,Write to Synapse
def write(df):
  (df.write.mode("append")
                    .format("com.databricks.spark.sqldw")
                    .option("url", jdbcUrl)
                    .option("user", jdbcUsername)
                    .option("password", jdbcPassword)
                    .option("tempDir", tempDir)
                    .option("forwardSparkAzureStorageCredentials", "true")
                    .option("dbTable", destTable)
                    .save()
  )

# COMMAND ----------

# DBTITLE 1,Select the fields from one dataframe that match the other dataframe (lowering the column names)
def customSelect(availableCols, requiredCols):
  newColumns = []
  for column in requiredCols:
    for columnsToMatch in availableCols:
      if column.lower() == columnsToMatch.lower():
        newColumns.append(column)
        break
      #else:
      #  newColumns.append(lit(None))
  return newColumns

# COMMAND ----------

# DBTITLE 1,getSelectExpr
def getSelectExpr(availableCols, requiredCols):
	SQLCommand = ""
	iterator = 0
	#Loop through required columns
	for column in requiredCols:
		if(iterator != 0):
			SQLCommand = SQLCommand + "!" #split command for SQL select expr
			
		matchingColumn = ""
		#For each column in required columns loop through to find a match in columns available
		for columnsToMatch in availableCols:
			if column.lower() == columnsToMatch.lower():
				matchingColumn = columnsToMatch
				break
			
		if matchingColumn == "":
			SQLCommand = SQLCommand + "CAST(null AS STRING) " + " AS " + column
		else:
			SQLCommand = SQLCommand + columnsToMatch + " AS " + column
		iterator = iterator + 1
			
	
	print(SQLCommand)
	return SQLCommand.split("!") 

# COMMAND ----------

# DBTITLE 1,Read Dataframes (from Gold and from Synapse - using a pushdown query)
gold = spark.read.format("delta").load(consolidatedPath)
pushdown_query = "(SELECT TOP 1 * FROM " + destTable + ") a" 
synapse = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)

# COMMAND ----------

# DBTITLE 1,Create Union Of Two Dataframes With columns combined and matching destination format
dfgold = gold.selectExpr(
                      getSelectExpr(                            
                                                                        gold.columns, #Available columns
                                                                        synapse.columns #Required Columns 
                                                                         )
)

#dfgold.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Execute streaming and return notebook output
rJSON = ""
rJSON = write(dfgold)
dbutils.notebook.exit(rJSON)
