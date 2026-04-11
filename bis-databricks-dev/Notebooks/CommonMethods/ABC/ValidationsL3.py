# Databricks notebook source
# DBTITLE 1,Call ErrorHandling Methods
# MAGIC %run "./ErrorHandling"

# COMMAND ----------

# DBTITLE 1,Method: addRowID - Adds a column named RowID
def addRowID(df):
    df = df.withColumn("Id", monotonically_increasing_id()+1)
    windowSpec = Window.orderBy("id")
    df = df.withColumn("RowId", row_number().over(windowSpec))\
                                      .drop("Id")
    return df

# COMMAND ----------

# DBTITLE 1,Method: rowEquals - Fails if the row does not equal.
def rowEquals(dfData, query, cValue, vName, errorPath):
  df = spark.sql(query) \
          .filter(f"CheckVal <> {cValue}") \
          .drop("CheckVal") \
          .select("*") \
          .withColumn("Validation",lit(vName))
   
#    if errors write to file 
  if (df.count() > 0):
    consolidateError(df, errorPath) 

  return df.count()

# COMMAND ----------

# DBTITLE 1,Method: rowGreaterEquals - Fails if the row is less than the value
def rowGreaterEqual(dfData, query, cValue, vName, errorPath):
  df = spark.sql(query) \
          .filter(f"CheckVal < {cValue}") \
          .drop("CheckVal") \
          .select("*") \
          .withColumn("Validation",lit(vName))
            
#    if errors write to file 
  if (df.count() > 0):
    consolidateError(df, errorPath) 

  return df.count()

# COMMAND ----------

# DBTITLE 1,Method: rowCheckValidator - Used to check the row level validations
def rowCheckValidator(dfData, dfRowCheck, errorFilePath):
  validationOutcome = 0

  #files validation section
  rowCheckCollect = dfRowCheck.collect()
  for rc in rowCheckCollect:
    #get the comparision value from t.value
    cValue = str(rc.Value)
    vName = str(rc.Name)
    fileQuery = str(rc.DataFileQuery)
    opr = str(rc.Operator)

    if opr == "Equals":
      validationOutcome+=rowEquals(dfData, fileQuery, cValue, vName, errorFilePath)
    elif opr == "GreaterEqual":
      validationOutcome+=rowGreaterEqual(dfData, fileQuery, cValue, vName, errorFilePath)
    else:
      println("Unimplemented Function")

  return validationOutcome


# COMMAND ----------

# DBTITLE 1,Method: fileRulesValidator - Runs the File Rules Validations Against a File.
def fileRulesValidator(dfData, dfRulesCheck, dfControl, errorFilePath): 
  result="true"
    
  dataOutcome = []
  controlOutcome =  []
  validationOutcome = []

  dfControl.createOrReplaceTempView("controlDF")
  dfData.createOrReplaceTempView("dataDF")

  try:
    rulesCheckCollect = dfRulesCheck.collect()
    for rc in rulesCheckCollect:
      #control file query 
      x=rc.control_file_query
      controlFileQuery=x.replace("control_file","controlDF")
      dfValControlQueryOutput=spark.sql(controlFileQuery).collect()
      b=str(dfValControlQueryOutput[0][0])
      controlOutcome.append(b)

      #data file query
      y=rc.data_file_query
      dataFileQuery=y.replace("data_file","dataDF")
      dfValDataQueryOutput=spark.sql(dataFileQuery).collect()
      a=str(dfValDataQueryOutput[0][0])
      dataOutcome.append(a)

      if(a==b):
        validationOutcome.append("Validation SUCCESS!!")
      else:
        validationOutcome.append("Validation FAILED!!")
        result="false"

  except Exception as e:
    result = "false"

  controlOutputDF = spark.createDataFrame(controlOutcome,StringType())
  controlOutputDF = controlOutputDF.withColumnRenamed("value","controlFileOutput")
  controlOutputDF = addRowID(controlOutputDF)

  #create data output df and order columns for join
  dataOutputDF = spark.createDataFrame(dataOutcome,StringType())
  dataOutputDF = dataOutputDF.withColumnRenamed("value","dataFileOutput")
  dataOutputDF = addRowID(dataOutputDF)

  validationOutputDF = spark.createDataFrame(validationOutcome,StringType())
  validationOutputDF = validationOutputDF.withColumnRenamed("value","validationOutput")
  validationOutputDF = addRowID(validationOutputDF)

  dfRulesCheck = addRowID(dfRulesCheck)

  intermediateDF = dfRulesCheck.join(dataOutputDF, "RowId")\
                              .drop("RowId")
  intermediateDF = addRowID(intermediateDF)

  finalDF = intermediateDF.join(controlOutputDF,"RowId")\
                              .drop("RowId")
  finalDF = addRowID(finalDF)

  errorFile = finalDF.join(validationOutputDF,"RowId")\
                    .withColumn("RecordType",lit(""))

  if(result=="false"):
    errorFile.write.mode("overwrite").option("header", "true").format("csv").save(errorFilePath)

  return result
