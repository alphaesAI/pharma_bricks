# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")

ClientCode = dbutils.widgets.get("ClientContainer")
Entity = 'Q360Pharmacy'

MountPoint = "/mnt/"
print(ClientCode)
print(Entity)

# COMMAND ----------

from pyspark.sql.functions import explode, col,lit
import json

clientConfiguration = """
{
  "Entity": "Q360Pharmacy",
  "Clients": [
    {
      "ClientCode": "DEVIDAP1",
      "ConfigurationType": "1",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "ESI"
        },
        {
          "FileLayoutId": "11000",
          "DataSourceName": "OPT"
        }
      ]
    },
    {
      "ClientCode": "DEVIDAP2",
      "ConfigurationType": "3",
      "Filters": [
        {
          "FileLayoutId": "11010",
          "DataSourceName": ""
        }
      ]
    },
    {
      "ClientCode": "QAIDAP1",
      "ConfigurationType": "1",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "ESI"
        },
        {
          "FileLayoutId": "11000",
          "DataSourceName": "OPT"
        }
      ]
    },
    {
      "ClientCode": "QAIDAP2",
      "ConfigurationType": "3",
      "Filters": [
        {
          "FileLayoutId": "11010",
          "DataSourceName": ""
        }
      ]
    },
    {
      "ClientCode": "NBND",
      "ConfigurationType": "1",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "ESI"
        },
        {
          "FileLayoutId": "11000",
          "DataSourceName": "OPT"
        }
      ]
    },
    {
      "ClientCode": "VBA",
      "ConfigurationType": "1",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "ESI"
        },
        {
          "FileLayoutId": "11000",
          "DataSourceName": "OPT"
        }
      ]
    },
    {
      "ClientCode": "WAHP",
      "ConfigurationType": "2",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "CVS RX"
        }
      ]
    },
    {
      "ClientCode": "BCBSKS",
      "ConfigurationType": "3",
      "Filters": [
        {
          "FileLayoutId": "11010",
          "DataSourceName": ""
        }
      ]
    },
    {
      "ClientCode": "BCBSNE",
      "ConfigurationType": "3",
      "Filters": [
        {
          "FileLayoutId": "11000",
          "DataSourceName": "PRIME"
        }
      ]
    },
    {
      "ClientCode": "Premera",
      "ConfigurationType": "4",
      "Filters": [
        {
          "FileLayoutId": "",
          "DataSourceName": "CVS Rx"
        }
      ]
    }
  ]
}
"""

clientConfigJSONList = []
clientConfigJSONList.append(clientConfiguration)
clientConfigJSONExtracted = spark.read.json(sc.parallelize(clientConfigJSONList))

clientConfigDF = clientConfigJSONExtracted.select("Entity",explode("Clients")).select(
                 "Entity"
                ,col("col.ClientCode").alias("ClientCode")
                ,col("col.ConfigurationType").alias("ConfigurationType")
                ,explode(col("col.Filters")).alias("Filters")
              ).select(
               "Entity"
              ,"ClientCode"
              ,"ConfigurationType"
              ,"Filters.FileLayoutId"
              ,"Filters.DataSourceName"
              )
 
ViewName = "ClientConfig"
clientConfigDF.createOrReplaceTempView(ViewName)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM ClientConfig

# COMMAND ----------

def ConfigurationOne(ClientCode):
  ##### Run ConfigurationOne
  StagePharmacySQLQuerry = """
        WITH SourceData AS(
        SELECT 
           p.MemberID
          ,p.RxDaysSupply
          ,p.RxFillDate
          ,p.NDCCodeSTD
          ,p.ClaimStatus
          ,p.Quantity
          ,p.SourceName
          ,p.ProviderID
          ,p.ProviderNPI
          ,p.PharmacyNPI
          ,p.ClaimNumber
          ,p.AdjudicationDate
          ,p.AlternateKey1
          ,p.AlternateKey2
          ,p.FileLayoutId
          ,p.FileId
        FROM PharmacyData p
          INNER JOIN ClientConfiguration cc
            ON p.FileLayoutId = cc.FileLayoutId
            AND p.SourceName = cc.DataSourceName
        ),
        ESIPharmacy AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
          ,ROW_NUMBER() OVER(PARTITION BY MemberId,RxFillDate,NDCCodeSTD ORDER BY AdjudicationDate DESC,AlternateKey1 DESC,ClaimStatus) AS RowNumber
        FROM SourceData
        WHERE
        SourceName = 'ESI'
        ),
        OPTPharmacy AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
          ,ROW_NUMBER() OVER(PARTITION BY MemberId,RxFillDate,NDCCodeSTD ORDER BY AdjudicationDate DESC,AlternateKey1 DESC,AlternateKey2 DESC ,  
                      CASE     
                        WHEN ClaimStatus = 'I' THEN 1
                        WHEN ClaimStatus = 'A' THEN 2
                        WHEN ClaimStatus = 'D' THEN 3
                        WHEN ClaimStatus = 'R' THEN 4
                        WHEN ClaimStatus = 'P' THEN 5
                      END DESC 
          ) AS RowNumber
        FROM SourceData
        WHERE
        SourceName = 'OPT'
        ),
        Combined AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM ESIPharmacy
        WHERE
        RowNumber = 1
        UNION ALL
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM OPTPharmacy
        WHERE
        RowNumber = 1
        )
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM Combined
        WHERE
        CASE 
          WHEN ClaimStatus = 'R' THEN 0
          ELSE 1 
        END = 1
  """
  
  dfStagePharmacy = spark.sql(StagePharmacySQLQuerry).cache()
  dfStagePharmacy.createOrReplaceTempView("StageQ360Pharmacy")
  
  return "ConfigurationOne Success!"

# COMMAND ----------

def ConfigurationTwo(ClientCode):
  ##### Run ConfigurationTwo
  StagePharmacySQLQuerry = """
        WITH SourceData AS(
        SELECT 
           p.MemberID
          ,p.RxDaysSupply
          ,p.RxFillDate
          ,p.NDCCodeSTD
          ,p.ClaimStatus
          ,p.Quantity
          ,p.SourceName
          ,p.ProviderID
          ,p.ProviderNPI
          ,p.PharmacyNPI
          ,p.ClaimNumber
          ,p.AdjudicationDate
          ,p.AlternateKey1
          ,p.AlternateKey2
          ,p.FileLayoutId
          ,p.FileId
          ,ROW_NUMBER() OVER(PARTITION BY p.MemberID, p.RxFillDate, p.NDCCodeSTD ORDER BY p.AdjudicationDate DESC, p.AlternateKey2 DESC,p.AlternateKey1 DESC, p.ClaimStatus) AS RowNumber
        FROM PharmacyData p
          INNER JOIN ClientConfiguration cc
            ON p.FileLayoutId = cc.FileLayoutId
            AND p.SourceName = cc.DataSourceName
        ),
        Combined AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM SourceData
        WHERE
        RowNumber = 1
        )
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM Combined
        WHERE
        CASE 
          WHEN ClaimStatus = 'R' THEN 0
          ELSE 1 
        END = 1
  """
  
  dfStagePharmacy = spark.sql(StagePharmacySQLQuerry).cache()
  dfStagePharmacy.createOrReplaceTempView("StageQ360Pharmacy")
  
  return "ConfigurationTwo Success!"

# COMMAND ----------

def ConfigurationThree(ClientCode):
  ##### Run ConfigurationThree
  StagePharmacySQLQuerry = """
        WITH SourceData AS(
        SELECT 
           p.MemberID
          ,p.RxDaysSupply
          ,p.RxFillDate
          ,p.NDCCodeSTD
          ,p.ClaimStatus
          ,p.Quantity
          ,p.SourceName
          ,p.ProviderID
          ,p.ProviderNPI
          ,p.PharmacyNPI
          ,p.ClaimNumber
          ,p.AdjudicationDate
          ,p.AlternateKey1
          ,p.AlternateKey2
          ,p.FileLayoutId
          ,p.FileId
        FROM PharmacyData p
          INNER JOIN ClientConfiguration cc
            ON p.FileLayoutId = cc.FileLayoutId
            AND p.SourceName = cc.DataSourceName
        ),
        Adjudication AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
          ,ROW_NUMBER() over (partition by MemberID,RxFillDate,NDCCodeSTD ORDER BY AlternateKey1, AdjudicationDate DESC, CASE
                      WHEN ClaimStatus = 'R' THEN 1
                      WHEN ClaimStatus = 'A' THEN 2
                      WHEN ClaimStatus = 'I' THEN 3
                      WHEN ClaimStatus = 'D' THEN 4
                      ELSE 0
                      END) AS RowNumber
        FROM SourceData
        ),
        Q360Pharmacy  AS(
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM Adjudication
        WHERE
        RowNumber = 1
        )
        SELECT 
           MemberID
          ,RxDaysSupply
          ,RxFillDate
          ,NDCCodeSTD
          ,ClaimStatus
          ,Quantity
          ,SourceName
          ,ProviderID
          ,ProviderNPI
          ,PharmacyNPI
          ,ClaimNumber
          ,AdjudicationDate
          ,AlternateKey1
          ,AlternateKey2
          ,FileLayoutId
          ,FileId
        FROM Q360Pharmacy
        WHERE
        CASE 
          WHEN ClaimStatus = 'R' THEN 0
          ELSE 1 
        END = 1
  """
  
  dfStagePharmacy = spark.sql(StagePharmacySQLQuerry).cache()
  dfStagePharmacy.createOrReplaceTempView("StageQ360Pharmacy")
  
  return "ConfigurationThree Success!"

# COMMAND ----------

def runProcess(ClientCode,TruncateScript,DestinationTable,DestinationEntity):
  #Load destination path entity
  DestinationPath = MountPoint + DestinationTable.replace("#clientCode",ClientCode)
  destdf = spark.read.format('delta').option("header", "true").load(DestinationPath) 
  destdf.createOrReplaceTempView(DestinationEntity)
  print(DestinationEntity + " temp view created")
  
  ##### Run ClientConfig
  FilteredConfigurationSQLQuerry = f"""
    SELECT
       ConfigurationType
      ,ClientCode
      ,FileLayoutId
      ,DataSourceName
    FROM ClientConfig
    WHERE
    LOWER(ClientCode) = LOWER('{ClientCode}')
  """

  ConfigurationType = spark.sql(FilteredConfigurationSQLQuerry).first()[0]
  dfConfig = spark.sql(FilteredConfigurationSQLQuerry).cache()
  dfConfig.createOrReplaceTempView("ClientConfiguration")

  ##### Run EligibleMembers 
  MemberSQLQuerry = """
      SELECT DISTINCT
         COALESCE(nullif(mpb.UniquePersonKey,'None'),nullif(mpb.PlanMemberID,'None')) AS MemberID
        ,COALESCE(nullif(ompb.UniquePersonKey,'None'),nullif(ompb.PlanMemberID,'None')) AS OriginalMemberID
      FROM MemberPersonBridge mpb
        INNER JOIN HedisEligibleMember hem
          ON mpb.BISInternalPersonId = hem.BISInternalPersonId
        LEFT JOIN MemberPersonBridge ompb
          ON ompb.BISInternalPersonId = hem.BISInternalPersonId
          AND ompb.IsOriginalMemberId = 1
  """

  dfMember = spark.sql(MemberSQLQuerry).cache()
  dfMember.createOrReplaceTempView("EligibleMemberData")
  
  ##### Run Pharmacy 
  PharmacySQLQuerry = """
    WITH PharmacyTemp AS(
        SELECT 
           COALESCE(nullif(p.UniquePersonKey,'None'),nullif(p.PlanMemberID,'None')) AS MemberID
          ,p.RxDaysSupply
          ,p.RxFillDate
          ,p.NDCCodeSTD
          ,p.ClaimStatus
          ,p.Quantity
          ,trim(COALESCE(p.SourceName,'')) AS SourceName 
          ,p.ProviderID 
          ,p.ProviderNPI
          ,p.PharmacyNPI
          ,p.ClaimNumber
          ,p.AdjudicationDate
          ,p.AlternateKey1
          ,p.AlternateKey2
          ,p.FileLayoutId
          ,p.FileId
        FROM Pharmacy p
    )
    SELECT 
           em.OriginalMemberId AS MemberID
          ,p.RxDaysSupply
          ,p.RxFillDate
          ,p.NDCCodeSTD
          ,p.ClaimStatus
          ,p.Quantity
          ,p.SourceName
          ,p.ProviderID 
          ,p.ProviderNPI
          ,p.PharmacyNPI
          ,p.ClaimNumber
          ,p.AdjudicationDate
          ,p.AlternateKey1
          ,p.AlternateKey2
          ,p.FileLayoutId
          ,p.FileId
    FROM PharmacyTemp p
          INNER JOIN EligibleMemberData em
            ON p.MemberId = em.MemberId
  """

  dfPharmacy = spark.sql(PharmacySQLQuerry).cache()
  dfPharmacy.createOrReplaceTempView("PharmacyData") 
  
  if(ConfigurationType == "1"):
      ConfigurationOne(ClientCode)
  elif(ConfigurationType == "2"):
      ConfigurationTwo(ClientCode)
  elif(ConfigurationType == "3"):
      ConfigurationThree(ClientCode)
  
  # Run truncate script
  TruncateSQLQuery = TruncateScript.replace("#clientCode",ClientCode) 
  spark.sql(TruncateSQLQuery)
  print("Truncate SQL was executed")

  finalSQLQuery = """
      SELECT
         s.MemberID
        ,RxDaysSupply AS DaysSupply
        ,date_format(to_date(RxFillDate), 'yyyyMMdd') AS ServiceDate
        ,NDCCodeSTD AS NDCDrugCode
        ,CASE
            WHEN ClaimStatus = 'I' THEN '1'
            WHEN ClaimStatus = 'D' THEN '2'
            WHEN ClaimStatus IN('A','P') THEN '1'
            WHEN ClaimStatus = 'R' THEN '4' --should not be any
            ELSE NULL
         END AS ClaimStatus
        ,CAST(Quantity AS STRING) AS QuantityDispensed
        ,'N' AS SupplementalData
        ,SourceName AS DataSourceName
        ,ProviderID 
        ,ProviderNPI
        ,PharmacyNPI
        ,ClaimNumber AS ClaimID
        ,'1' AS ClaimLineID
        ,AdjudicationDate AS AdditionalColumn1
        ,AlternateKey1 AS AdditionalColumn2
        ,AlternateKey2 AS AdditionalColumn3
        ,'' AS AdditionalColumn4
        ,'' AS AdditionalColumn5
        ,'' AS Filler
        ,current_timestamp() AS LoadDateTime
      FROM StageQ360Pharmacy s
  """
  
  mDF = spark.sql(finalSQLQuery).cache()
  #insert into destination table
  mDF.write.format("delta").option("mergeSchema", "true").mode("append").save(DestinationPath) 
  print("Data was written to destination")

  ########unpersisting dataframes -------DO NOT REMOVE ---- MUST BE LAST THING
  dfConfig.unpersist()
  dfMember.unpersist()
  dfPharmacy.unpersist()
  mDF.unpersist()
  
  return "SUCCESS!"

# COMMAND ----------

def CreateEntity(Entity):
  entitySQL = """SELECT Entity FROM ClientConfig LIMIT(1)"""
  Entity = spark.sql(entitySQL).first()[0]

  ConfigJSON = """
  {
    "Entity": "Q360Pharmacy",
    "DestinationTable": "#clientCode/Gold/MA/Q360/Q360Pharmacy",
    "SourceTables": [
      {
        "Entity": "Pharmacy",
        "SourceTable": "#clientCode/consolidated/MA/Data/Pharmacy",
        "SourceFormat": "delta"
      },
      {
        "Entity": "Provider",
        "SourceTable": "#clientCode/consolidated/MA/Data/Provider",
        "SourceFormat": "delta"
      },
      {
        "Entity": "HedisEligibleMember",
        "SourceTable": "#clientCode/Gold/MA/Q360/HedisEligibleMember",
        "SourceFormat": "delta"
      },
      {
        "Entity": "MemberPersonBridge",
        "SourceTable": "#clientCode/Gold/MA/Client/MemberPersonBridge",
        "SourceFormat": "delta"
      }
    ],
    "SQLScript": "",
    "TruncateScript": "DELETE FROM Q360Pharmacy"
  }
  """

  configJSONList = []
  configJSONList.append(ConfigJSON)
  ConfigJSONExtracted = spark.read.json(sc.parallelize(configJSONList))

  ConfigDF = ConfigJSONExtracted.select("Entity", "DestinationTable", explode("SourceTables"), "SQLScript","TruncateScript").select(
                   col("Entity").alias("DestinationEntity")
                  ,"DestinationTable"
                  ,"col.Entity"
                  ,"col.SourceTable" 
                  ,"col.SourceFormat" 
                  ,"SQLScript"
                  ,"TruncateScript"
                )

  ViewName = "Config" + Entity
  ConfigDF.createOrReplaceTempView(ViewName)

  #Create variables
  QueryVariables = f"""SELECT DISTINCT
                             DestinationEntity
                            ,DestinationTable
                            ,TruncateScript
                      FROM {ViewName}
                   """

  DestinationEntity = spark.sql(QueryVariables).first()[0]
  DestinationTable = spark.sql(QueryVariables).first()[1]
  TruncateScript = spark.sql(QueryVariables).first()[2]

  #Load all sources
  for row in ConfigDF.collect():
    EntityToCreate = row["Entity"]
    SourcePath = row["SourceTable"]
    SourceFormat = row["SourceFormat"]

    UpdatedSourcePath = MountPoint + SourcePath.replace("#clientCode",ClientCode)

    #Create a tempview
    dfFile = spark.read.format(SourceFormat).option("header", "true").load(UpdatedSourcePath)
    dfFile.createOrReplaceTempView(EntityToCreate)
    print(EntityToCreate + " temp view created")

  runProcess(ClientCode,TruncateScript,DestinationTable,DestinationEntity)

# COMMAND ----------

returnStr = ""
try:
  CreateEntity(Entity)
  returnStr = "SUCCESS"
except:
  returnStr = "FAILURE"
finally:
  dbutils.notebook.exit(returnStr) 
