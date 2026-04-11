# Databricks notebook source
# DBTITLE 1,Parameters For Config File Path
dbutils.widgets.text("FileConfigMount","","")
dbutils.widgets.text("ConfigurationFile","","")

fileConfigMount = dbutils.widgets.get("FileConfigMount")  #"/mnt/fileconfig/"
configurationFile = dbutils.widgets.get("ConfigurationFile")  #"JSON/Clients/ClientsByEnvironment.json"
FullConfigPath = fileConfigMount + configurationFile

print(FullConfigPath)

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
dfConfigFile = spark.read.format("json").option("multiline",True).load(FullConfigPath)
#Split out environments into column
dfEnvironmentsConfigFile = dfConfigFile.select(explode("Environments").alias("Column"))
#split out all of the individual environments and filter by the current environment
dfEnvironmentConfigFile = dfEnvironmentsConfigFile.select("Column.EnvironmentLetter", "Column.Clients").filter(col("Column.EnvironmentLetter") == envLetter)
#split out all of the individual environments and filter by the current environment
dfClientsForEnvironment = dfEnvironmentConfigFile.select(explode("Clients").alias("Clients"))

dfClientsForEnvironment.createOrReplaceTempView("DeltaTable")

# COMMAND ----------

# DBTITLE 1,Configuration JSON for the dbs
from pyspark.sql.functions import explode, col,lit
import json

json = """[
  {
    "Type": "DataModels",
    "Client": true, 
    "FileConfigPath": "/mnt/fileconfig/JSON/Database/Client/DataModels"
  },
  {
    "Type": "DataModels",
    "Client": false, 
    "FileConfigPath": "/mnt/fileconfig/JSON/Database/Global/DataModels"
  },
  {
    "Type": "Views",
    "Client": true, 
    "FileConfigPath": "/mnt/fileconfig/JSON/Database/Client/Views"
  },
  {
    "Type": "Views",
    "Client": false, 
    "FileConfigPath": "/mnt/fileconfig/JSON/Database/Global/Views"
  }
]"""

# COMMAND ----------

# DBTITLE 1,Load JSON config from variable/file (etc...) into Dataframe
jsonList = []
jsonList.append(json)
df = spark.read.json(sc.parallelize(jsonList))
dfexplodedGroup = df.select("Type","Client","FileConfigPath")

#create local table from JSON
dfexplodedGroup.createOrReplaceTempView("Layers")

# COMMAND ----------

# DBTITLE 1,Method: createDatabase - Creates database if not exists by ClientContainer (aka ClientCode)
def createDatabase(clientCode):
  sqlQuery = "CREATE SCHEMA IF NOT EXISTS " + clientCode
  #print(sqlQuery)
  spark.sql(sqlQuery)

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

# DBTITLE 1,Check if database exists
def databaseExists(databaseToCheck):
  databases = spark.catalog.listDatabases()
  return next((t for t in databases if t.name == databaseToCheck), None)

# COMMAND ----------

# DBTITLE 1,Loop through all clients in this environment and get all tables by clientid
databases = dfClientsForEnvironment.collect()

for database in databases:
  clientCode = database["Clients"]
  clientContainer = clientCode.lower()
  createDatabase(clientContainer)

  print(database["Clients"])
  databaseTables = spark.catalog.listTables(database["Clients"])
  dfDatabaseTables = spark.createDataFrame(databaseTables, schema).cache()     
  dfDatabaseTables.createOrReplaceTempView(database["Clients"])

  tableQuery = f"""
            SELECT 
               name
              ,replace(replace(namespace,'[',''),']','') AS database
              ,description
              ,tableType
              ,isTemporary
            FROM {database["Clients"]}
            WHERE
            tableType = 'EXTERNAL'
    """

  dfTables = spark.sql(tableQuery).cache()
  dfTables.createOrReplaceTempView(database["Clients"] + 'tables')

  viewQuery = f"""
            SELECT
               name
              ,replace(replace(namespace,'[',''),']','') AS database
              ,description
              ,tableType
              ,isTemporary
            FROM {database["Clients"]}
            WHERE
            tableType = 'VIEW'
    """

  dfViews = spark.sql(viewQuery).cache()
  dfViews.createOrReplaceTempView(database["Clients"] + 'views')

# COMMAND ----------

# DBTITLE 1,Loop through all clients in this environment and combine into one dataframe
sqlQuery = ""
iterator = 0
clientCount = 0

for database in databases:
  if(databaseExists(database["Clients"])):
    clientCount = 1
    if(iterator != 0):
      sqlQuery +=  " UNION ALL SELECT * FROM " + database["Clients"]
    else:
      sqlQuery +=  "SELECT * FROM " + database["Clients"]
  else: 
      print('database does not exist - ' + database["Clients"])
  iterator += 1

if(clientCount > 0):
  dfDataBase = spark.sql(sqlQuery)
  dfDataBase.createOrReplaceTempView("DatabaseContents")
else:
  dfDataBase.createOrReplaceTempView("DatabaseContents")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM DatabaseContents

# COMMAND ----------

def tableExists(databases,fullTableName): 
  tempBoolean = False
  dataCollect = databases.collect()

  for table in dataCollect:
    fulltable = table["database"] + '.' + table["name"]
    if fulltable == fullTableName:
      tempBoolean = True
      break  

  return tempBoolean

# COMMAND ----------

def checkTableExists(tableName):
  tempBoolean = True
  try:
    sqlStatement = "DESCRIBE " + tableName
    tableSchema = spark.sql(sqlStatement)
    tempBoolean = True
  except:
    tempBoolean = False
  finally:
    return tempBoolean

# COMMAND ----------

def getTableMetadata(tableName):
  sqlStatement = "DESCRIBE " + tableName
  colsqlStatement = "SHOW COLUMNS IN " + tableName
  tableSchema = spark.sql(sqlStatement)
  tableColumns = spark.sql(colsqlStatement)
  
  tableColumns.createOrReplaceTempView("tableCols")
  tableSchema.createOrReplaceTempView("tableSchema")
  
  finalsqlQuery = """
  SELECT sc.col_name, sc.data_type, sc.comment
  FROM tableSchema sc
    INNER JOIN tableCols tc
      ON sc.col_name = tc.col_name"""
  
  dataframe = spark.sql(finalsqlQuery)
  dfCollect = dataframe.collect()
  
  colList = []
  for col in dfCollect:
    tempColList = [col["col_name"], col["data_type"]]
    colList.append(tempColList)
    
  return colList

# COMMAND ----------

# DBTITLE 1,Method: dropView- Drops view if exists
def dropView(viewName):
  dropViewSqlQuery = "DROP VIEW IF EXISTS " + viewName
  #print(dropTableSqlQuery)
  spark.sql(dropViewSqlQuery)

# COMMAND ----------

# DBTITLE 1,Method: dropUnmanagedTable - Drops Unmanaged table if exists
def dropUnmanagedTable(tableName):
  dropTableSqlQuery = "DROP TABLE IF EXISTS " + tableName
  #print(dropTableSqlQuery)
  spark.sql(dropTableSqlQuery)

# COMMAND ----------

# DBTITLE 1,Method: getStruct - Creates Schema From List
def getStruct(colList):
  arrayStructureSchema = []
  
  for col in colList:
    dataType = col[1].lower()
    value = dataType.find('decimal')
    if(value == 0):
      dataType = 'decimal'
    
    arrayStructureSchema.append(StructField(str(col[0]),getDataType(dataType), nullable = True))
    
  return StructType(arrayStructureSchema)

# COMMAND ----------

# DBTITLE 1,Method: getPath
def getPath(pathArray):
  path = ""
  maxPathArray = len(pathArray)
  pathIterator = 1

  for col in pathArray:
    if pathIterator == maxPathArray:
      path = str(col[4])
    pathIterator += 1
  #remove single quotes around the path
  path = path.strip("'")
  
  #print(path)

  return path

# COMMAND ----------

# DBTITLE 1,Method: getDataType - Get datatypes for sparkSql
from pyspark.sql.types import StructType,StructField,StringType,ByteType,ShortType,IntegerType,LongType,FloatType,BinaryType,BooleanType,TimestampType,DateType,DecimalType,DoubleType

def getDataType(argument):
    switcher = {
        "string": StringType(),
        "byte": ByteType(),
        "smallint": ShortType(),
        "int": IntegerType(),
        "integer": IntegerType(),
        "bigint": LongType(),
        "float": FloatType(), 
        "decimal": DecimalType(),  #broken - per Doug's request to add the note lol
        "binary": BinaryType(),
        "bit": BinaryType(),
        "boolean": BooleanType(),
        "timestamp": TimestampType(),
        "date": DateType(),
        "double": DoubleType()
    }
    
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, StringType())

# COMMAND ----------

from pyspark.sql.types import StructType,StructField,StringType,ByteType,ShortType,IntegerType,LongType,FloatType,BinaryType,BooleanType,TimestampType,DateType,DecimalType,DoubleType

def getSQLDataType(argument):  
    switcher = {
        "StringType()": "string",
        "ByteType()": "byte",
        "ShortType()": "smallint",
        "IntegerType()": "int",
        "LongType()": "bigint",
        "FloatType()": "float", 
        "DecimalType()": "decimal",  #broken - per Doug's request to add the note lol
        "BinaryType()": "binary",
        "BooleanType()": "boolean",
        "TimestampType()": "timestamp",
        "DateType()": "date",
        "DoubleType()": "double"
    }
    
    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "string")

# COMMAND ----------

# DBTITLE 1,Method: getFormat
def getFormat(formatArray):
  doubleQuote = """ " """.strip()
  tempFormat = ""
  maxFormatArray = len(formatArray)
  formatIterator = 1

  for col in formatArray:
    if formatIterator == maxFormatArray:
      tempFormat = str(col[2])
    formatIterator += 1
  format = doubleQuote + tempFormat + doubleQuote
  #print(format)

  return format

# COMMAND ----------

# DBTITLE 1,Method: getTableName - Get tableName
def getTableName(tableArray):
  tableName = "" 
  tableIterator = 1

  for col in tableArray:
    if tableIterator == 1:
      tableName = str(col[2])
    tableIterator += 1

  #print(tableName)

  return tableName

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

def getSelectExpr(availableCols, requiredCols):
  SQLCommand = ""
  iterator = 0

  #Loop through required columns
  for rColumn in requiredCols:
    if(iterator != 0):
      SQLCommand = SQLCommand + "!" #split command for SQL select expr
			
    matchingColumn = ""
    columnsToMatch = ""
    
    #For each column in required columns loop through to find a match in columns available
    for aColumn in availableCols:
      columnsToMatch = aColumn.name
      if rColumn.name == columnsToMatch:
        matchingColumn = columnsToMatch
        break

    if matchingColumn == "":
      SQLCommand = SQLCommand + "CAST(null AS " + getSQLDataType(str(rColumn.dataType)) + ") " + " AS " + rColumn.name
    else:
      SQLCommand = SQLCommand + "CAST(" + columnsToMatch + " AS " + getSQLDataType(str(rColumn.dataType)) + ") "  + " AS " + rColumn.name

    iterator = iterator + 1
			
  #print(SQLCommand)
  return SQLCommand.split("!") 

# COMMAND ----------

# DBTITLE 1,Method: createUnmanagedTable - Creates UnManaged Tables
def createUnmanagedTable(filterDF, clientCode, configFile):
  clientContainer = clientCode
  dataModelPath = configFile
  
  #load entire file into a dataframe
  rdd = spark.sparkContext.wholeTextFiles(dataModelPath)
  dataModelString = rdd.collect()[0][1]
  #replace #clientCode across the entire file
  sqlDatamodelString = dataModelString.replace("#clientCode", clientContainer)

  #print(sqlDatamodelString)
  listString = sqlDatamodelString.split('\r\n')

  #iterator for rowNumbers from the file
  iterator = 1

  #New list to add columns to
  colList = []
  #New list to add tablename
  tableNameList = []
  #New list to add tablePath to
  tablePathList = [] #will include the format also
  #get the last row in the file << should contain the path
  maxListStr = len(listString)

  #Pull out all data from the string: Columns, TableName, Path and format
  for line in listString:
    if iterator != 1 and iterator != maxListStr:
      colList.append(line.replace(",", "").strip().split())
    elif iterator == 1:
      tableNameList.append(line.replace(",", "").strip().split())
    elif iterator == maxListStr:
      tablePathList.append(line.replace(",", "").strip().split())
    iterator += 1
	  
  #get path 
  tablePath = getPath(tablePathList)
  #get format
  tableFormat = getFormat(tablePathList)
  #get tableName
  tableName = getTableName(tableNameList).lower()

  print("Start " + tableName)
  ##create the destination schema from the datamodel from the columns and datatypes in the file
  destSchema = getStruct(colList)
  ##Create an empty DataFrame with the new updated datamodel
  emptyRDD = spark.sparkContext.emptyRDD()
  dfDataModel = spark.createDataFrame(emptyRDD, destSchema)

  #table exists already
  tableAlreadyThere = tableExists(filterDF,tableName)
  
  checkMetadataExists = True
  #if table exists make sure its readable, if its not reset it to not there
  if(tableAlreadyThere):
    checkMetadataExists = checkTableExists(tableName)
  
  pathAlreadyThere = pathExists(tablePath) #path exists but may not be the same as the unmanaged table path which may cause a problem  
    
  if(tableAlreadyThere):
    if(pathAlreadyThere is False): #table exists and path does not -- means there is a table with no data
      #drop unmanaged - external table -- table will not exist at this point
      dropUnmanagedTable(tableName)
      #create table with using datamodel
      dfDataModel.write.format("delta").option("path", tablePath).saveAsTable(tableName)
      print("Route taken: Table exist and Path does not - " + tableName + "   created at path: " + tablePath)
    if(pathAlreadyThere and checkMetadataExists is False):
      dropUnmanagedTable(tableName)
      dfFile = spark.read.format("delta").option("header","true").load(tablePath)  
      #Conform to new table structure
      newDFDatamodel = dfFile.selectExpr(
							getSelectExpr(    
																dfFile.schema, #Available columns
																dfDataModel.schema #Required Columns 
							)
				  )
      
      #create table with using datamodel
      newDFDatamodel.write \
		  .format("delta") \
		  .mode("overwrite") \
		  .option("overwriteSchema", "true") \
		  .option("path", tablePath) \
		  .saveAsTable(tableName)
      print("Route taken: Table and Path does exist (but path has changed and needs to be updated) - " + tableName + "   created at path: " + tablePath)
    if(checkMetadataExists):
      needsUpdate = 0
      numMatches = []
      
      tableColList = getTableMetadata(tableName) #if table points at another path this will fail
      tableSchema = getStruct(tableColList)
      
      for tableRow in tableSchema:
        for destRow in destSchema:
          if(tableRow == destRow): 
            numMatches.append(destRow.name)
            break
      
      destStructLength = len(destSchema)
      tableStructLength = len(tableSchema)
      numberOfMatches = len(numMatches)
	  
      if(numberOfMatches != destStructLength):
        needsUpdate = 1
      if(numberOfMatches != tableStructLength):
        needsUpdate = 1
      
      #table needs to be updated
      if(needsUpdate == 1): 
        #drop unmanaged - external table -- table will not exist at this point
        dropUnmanagedTable(tableName)
        #Load existing data
        dfFile = spark.read.format("delta").option("header","true").load(tablePath)
        #Conform to new table structure
        newDFDatamodel = dfFile.selectExpr(
							getSelectExpr(    
																dfFile.schema, #Available columns
																dfDataModel.schema #Required Columns 
							)
				  )
        #Recreate table with new datamodel
        newDFDatamodel.write \
		  .format("delta") \
		  .mode("overwrite") \
		  .option("overwriteSchema", "true") \
		  .option("path", tablePath) \
		  .saveAsTable(tableName)
        print("Route taken: Table and Path does exist (but datamodel needs to be updated) - " + tableName + "   created at path: " + tablePath)
  else: #table does not exist
    if(pathAlreadyThere): #path exists but table does not -- means there is data there with no table
      #Load Data
      dfFile = spark.read.format("delta").option("header","true").load(tablePath)
      #Conform to new table structure
      newDFDatamodel = dfFile.selectExpr(
							getSelectExpr(    
																dfFile.schema, #Available columns
																dfDataModel.schema #Required Columns 
							)
				  )
      
      #create table with using datamodel
      newDFDatamodel.write \
		  .format("delta") \
		  .mode("overwrite") \
		  .option("overwriteSchema", "true") \
		  .option("path", tablePath) \
		  .saveAsTable(tableName)
      print("Route taken: Table does not exist and Path does exist - " + tableName + "   created at path: " + tablePath)
    else:
      #Table does not exist - Create datamodel fresh
      dfDataModel.write.format("delta").option("path", tablePath).saveAsTable(tableName)
      print("Route taken: Table and Path do not exist (completely new table with no data) - " + tableName + "   created at path: " + tablePath)

# COMMAND ----------

def createView(clientCode, configFile):
  clientContainer = clientCode
  dataModelPath = configFile
  
  #load entire file into a dataframe
  rdd = spark.sparkContext.wholeTextFiles(dataModelPath)
  dataModelString = rdd.collect()[0][1]
  #replace #clientCode across the entire file
  sqlDatamodelString = dataModelString.replace("#clientCode", clientContainer)
  spark.sql(sqlDatamodelString)

# COMMAND ----------

# DBTITLE 1,Create a local table from all configs that have a FileConfigPath
def buildOutDatabase(dataCollect, clientContainer):
  newDataCollect = dataCollect.filter(col("FileConfigPath") != "").collect()
  
  for row in newDataCollect:
    FileConfigPath = row["FileConfigPath"]
    Type = row["Type"]
    
    if(Type == "DataModels"):
      dataModels = dbutils.fs.ls(FileConfigPath)
      dataCollect = len(dataModels)
      print(f"Deploying {str(dataCollect)} DataModels for - {clientContainer}")
      
      if(dataCollect > 0):
        dfDatamodels = spark.createDataFrame(dataModels)
        dataModelCollect = dfDatamodels.collect()
        #filterSQL for drop later
        filterSQL = f"""SELECT * FROM {clientContainer}tables WHERE database = '{clientContainer}'""" 
        filterDF = spark.sql(filterSQL)
        filterDF.createOrReplaceTempView("ClientDatabaseContent")
        dfDatamodels.withColumn("database", lit(clientContainer)).createOrReplaceTempView("TableList")
      
    
        #query to drop unmanaged tables that should not be there
        dropSqlQuery = """
          WITH ConfigFolderList AS(
          SELECT  
              trim(database) as database
             ,lower(trim(concat(database,'.',LEFT(name, INSTR(name, '.')-1)))) as FullTableName
          FROM TableList
          WHERE
          trim(LEFT(name, INSTR(name, '.')-1)) <> ""
          ),
          DatabricksDatabase AS(
          SELECT 
             trim(database) as database
            ,lower(trim(concat(database,'.',name))) as FullTableName
          FROM ClientDatabaseContent
          )
          SELECT ddb.FullTableName
          FROM DatabricksDatabase ddb
            LEFT JOIN ConfigFolderList cfl
              ON ddb.FullTableName = cfl.FullTableName --has database in the name
          WHERE 
          COALESCE(cfl.FullTableName, "") = "" 
         """
    
        dropDF = spark.sql(dropSqlQuery)
        dropDataModelCollect = dropDF.distinct().collect()
    
        for dropModel in dropDataModelCollect:
          FullTableName = dropModel["FullTableName"]
          print("Route taken: Droping table as it no longer exist - " + FullTableName)
          dropUnmanagedTable(FullTableName)

        #create unmananged tables that should be there
        for model in dataModelCollect:
          dataModelPath = model["path"]
          createUnmanagedTable(filterDF, clientContainer, dataModelPath)

    if(Type == "Views"):
      dataView = dbutils.fs.ls(FileConfigPath)
      dataCollect = len(dataView)

      print(f"Deploying {str(dataCollect)} Views for - {clientContainer}")
      if(dataCollect > 0):
        dfViews = spark.createDataFrame(dataView)
        dataViewsCollect = dfViews.collect()
        dfViews.withColumn("database", lit(clientContainer)).createOrReplaceTempView("ViewList")

        #query to drop views --always recreate
        dropViewSqlQuery = f"""
          WITH ConfigFolderList AS(
          SELECT  
              trim(database) as database
             ,lower(trim(concat(database,'.',LEFT(name, INSTR(name, '.')-1)))) as FullViewName
             ,path
          FROM ViewList
          WHERE
          trim(LEFT(name, INSTR(name, '.')-1)) <> ""
          )
          SELECT 
               cfl.FullViewName
              ,path
          FROM ConfigFolderList cfl --recreate all views
       """

        dropDF = spark.sql(dropViewSqlQuery)
        dropAndRecreatePath = dropDF.distinct().collect()
    
        for dropModel in dropAndRecreatePath:
          FullViewName = dropModel["FullViewName"]
          dataModelPath = dropModel["path"]
          print("Route taken: Droping view and recreating it - " + FullViewName)
          dropView(FullViewName)
          createView(clientContainer, dataModelPath)

# COMMAND ----------

# DBTITLE 1,Filter config by client / global
dfClientsForEnvironmentCollect = dfClientsForEnvironment.collect()

for client in dfClientsForEnvironmentCollect:
    clientCode = client["Clients"]
    clientContainer = clientCode.lower()
    
    print("Begin "+clientCode)

    #filter by client from config as they have different source paths
    if clientContainer == "global":
      dataCollect = dfexplodedGroup.filter(col("Client") == "false")
    elif clientContainer != "global":
      dataCollect = dfexplodedGroup.filter(col("Client") == "true")

    buildOutDatabase(dataCollect, clientContainer)
