# Databricks notebook source
from pyspark.sql.functions import concat_ws, sha2, col, lit, concat

dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigFile","","")

ConfigFile = dbutils.widgets.get("ConfigFile")
ClientContainer =  dbutils.widgets.get("ClientContainer")
#just changing the name
clientCode = ClientContainer

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Create TempView if exists
def LoadAndCreateTempView(path, format, tablename, clientCode,IsSource):
  UpdatedPath = path.replace("#clientCode",clientCode)
   
  if(pathExists(UpdatedPath)):
    if(IsSource == '1'):
      dfFile = spark.read.format(format).option("header","true").load(UpdatedPath)
      dfNewSourceFile = dfFile.withColumn("HashOfRow", sha2(concat_ws("|", *dfFile.columns), 256))
      dfNewSourceFile.createOrReplaceTempView(tablename)
    else:
      dfFile = spark.read.format(format).option("header","true").load(UpdatedPath)
      dfFile.createOrReplaceTempView(tablename)
    print("TempViewCreated: " + tablename)
  else:
    print("TempViewNotCreated because path does not exist: "  + tablename)

# COMMAND ----------

from pyspark.sql.functions import explode, col

df = spark.read.format("json").option("multiline", "true").load(ConfigFile)
df.createOrReplaceTempView("tables")

#get destination table and create view
for destTable in df.collect():
  DestinationTableName = destTable["DestinationTableName"]
  DestinationTablePath = destTable["DestinationTablePath"]
  LoadAndCreateTempView(DestinationTablePath, 'delta', DestinationTableName, clientCode, '0')

#get source tables
dfSourceTables = df.select(explode("SourceTables").alias("SourceTables")) \
                   .select("SourceTables.IsSource","SourceTables.TableFormat", "SourceTables.TableName", "SourceTables.TablePath")
#get validations
dfValidations = df.select(explode("Validations").alias("Validations")) \
                   .select("Validations.Field","Validations.Validator", "Validations.SQLQuery")
# dfValidations.createOrReplaceTempView("CheckValidation")

for sourceTable in dfSourceTables.collect():
  IsSource = sourceTable["IsSource"]
  TableFormat = sourceTable["TableFormat"]
  TableName = sourceTable["TableName"]
  TablePath = sourceTable["TablePath"]
  LoadAndCreateTempView(TablePath, TableFormat, TableName, clientCode, IsSource)

dfSourceTables.createOrReplaceTempView("sourcetables")

# COMMAND ----------

# DBTITLE 1,Method: IsRequired
def IsRequired(filterColName, validator):
  sqlQuery = f"""
    SELECT
       FileId
      ,BatchId
      ,'{filterColName}' AS ColumnName
      ,'{validator}' AS ErrorCode
      ,'{filterColName} is null or empty' AS ErrorDescription
      ,HashOfRow
      ,SourceFileName
    FROM QueryResult
    WHERE
    coalesce({filterColName},'') = ''
  """

  dfErrors = spark.sql(sqlQuery)
  return dfErrors

# COMMAND ----------

# DBTITLE 1,Method: IsCustom
def IsCustom(sqlQuery):
  dfErrors = spark.sql(sqlQuery)
  return dfErrors

# COMMAND ----------

def DynamicUnionOfDataframes(dfList: list):
  sqlQuery = ""
  iterator = 0
  
  for view in dfList:
    iterator = iterator + 1
    if(iterator == len(dfList)):
      sqlQuery += "SELECT * FROM " + view
    else:
      sqlQuery += "SELECT * FROM " + view + " UNION ALL "

  
#   print(sqlQuery)
  combinedDF = spark.sql(sqlQuery)
  combinedDF.createOrReplaceTempView("UnionDetail")

# COMMAND ----------

###Load and create QueryResult table
QueryResultSQL = """
SELECT 
   bt.BatchId
  ,at.SourceFileName
  ,st.*
FROM BatchTable bt
  INNER JOIN SourceTable st
    ON bt.FileId = st.FileId
    AND bt.HashOfRow = st.HashOfRow
  INNER JOIN AuditTable at
    ON bt.FileId = at.SourceFileId
    AND bt.BatchId = at.BatchId
"""

dfQueryResult = spark.sql(QueryResultSQL)
dfQueryResult.createOrReplaceTempView("QueryResult")

combineList = []

for row in dfValidations.collect():
  Field = row["Field"]
  Validator = row["Validator"]
  SQLQuery = row["SQLQuery"]
  print(f"Processing: {Field}")
  viewName = "QueryResult" + "_" + Field + "_" + Validator

  if(SQLQuery == ""):
    dfErrors = IsRequired(Field, Validator)
  else:
    dfErrors = IsCustom(SQLQuery)
  
  #create view after validation is complete
  dfErrors.createOrReplaceTempView(viewName)
  #add to list of dataframes to combine
  combineList.append(viewName)

#Union the dataframes in the list created above
DynamicUnionOfDataframes(combineList)

# COMMAND ----------

# DBTITLE 1,Insert data into destination table
InsertSQLQuerry = f"""
  INSERT INTO {DestinationTableName} (
  FileId
  ,BatchId
  ,ColumnName
  ,ErrorCode
  ,ErrorDescription
  ,HashOfRow
  ,SourceFileName
  )
  SELECT 
     ud.FileId
    ,ud.BatchId
    ,ud.ColumnName
    ,ud.ErrorCode
    ,ud.ErrorDescription
    ,ud.HashOfRow
    ,ud.SourceFileName
  FROM UnionDetail ud
    LEFT JOIN {DestinationTableName} dt
      ON dt.FileId = ud.FileId
      AND dt.BatchId = ud.BatchId
      AND dt.HashOfRow = ud.HashOfRow
  WHERE
  dt.HashOfRow IS NULL
  """

spark.sql(InsertSQLQuerry) 
