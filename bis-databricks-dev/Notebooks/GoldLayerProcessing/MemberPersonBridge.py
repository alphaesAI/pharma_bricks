# Databricks notebook source
# DBTITLE 1,Install PYPI libraries --scoped to this notebook
# MAGIC %pip install recordlinkage==0.15

# COMMAND ----------

# MAGIC %pip install pandas==1.3.5

# COMMAND ----------

# MAGIC %pip install numpy==1.21.6

# COMMAND ----------

# DBTITLE 1,Declare variables
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

clientCode = dbutils.widgets.get("ClientContainer") 
mntPnt = '/mnt/'
memFolderPath = mntPnt + clientCode + "/consolidated/MA/Data/Member"
goldMemFolderPath = mntPnt + clientCode + "/Gold/MA/Client/MemberPersonBridge"

print("Client: " + clientCode)
print("SourceFolderPath: " + memFolderPath)
print("GoldLayerFolderPath: " + goldMemFolderPath)

# COMMAND ----------

# DBTITLE 1,Setup Database connections
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
  blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
  blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
  blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="
else:
  envLetter = "p"
  envUser = "PRD"+envUser
  blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
jdbcDatabase = "Configuration_DB_" + clientCode.upper()
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }


# COMMAND ----------

# DBTITLE 1,Import libraries
from pyspark.sql.functions import date_format, monotonically_increasing_id
import pandas as pd
import recordlinkage
from pyspark.sql.functions import sha2, concat_ws, col, row_number, substring, lower, coalesce, upper, trim, regexp_replace
from pyspark.sql.window import Window

# COMMAND ----------

# DBTITLE 1,Rules
#Setup as followed... last number is the threshold and the columns before are evaulated for match... the first column is used as the index
RuleMBIColumns = ["BeneficiaryID","FirstInitial","LastInitial","DateofBirthFormatted","PhoneNumberFormatted","PermanentAddressLine1",11]
RulePMIDColumns = ["PlanMemberID","FirstInitial","LastInitial","DateofBirthFormatted","PhoneNumberFormatted","PermanentAddressLine1",11]
RuleUPKColumns = ["UniquePersonKey","FirstInitial","LastInitial","DateofBirthFormatted","PhoneNumberFormatted","PermanentAddressLine1",11]
RuleOtherColumns = ["DateofBirthFormatted","FirstName", "LastName","PhoneNumberFormatted","PermanentAddressLine1",14]

#All of the rule lists from above needed for evaulation
RulesAll =[RuleMBIColumns, RulePMIDColumns, RuleUPKColumns, RuleOtherColumns]

#List of all potential columns needed for comparison
CompareColumns = ["LastInitial", "FirstInitial", "LastName", "FirstName", "BeneficiaryID", "PlanMemberID", "UniquePersonKey", "DateofBirthFormatted", "PhoneNumberFormatted", "PermanentAddressLine1"]

# COMMAND ----------

# DBTITLE 1,Get needed FileLayoutIDs
getNonMemOutFileLayoutsSql = """SELECT DISTINCT FileLayoutID FROM dbo.refFileLayout WHERE FilterEntity = 'GoldMember'"""

getNonMemOutFileLayouts = (spark.read.format("jdbc") 
        .options(url=jdbcUrl,
                driver='com.microsoft.sqlserver.jdbc.SQLServerDriver',            
                query=getNonMemOutFileLayoutsSql,
                user=jdbcUsername,
                password=jdbcPassword).load())

getNonMemOutFileLayouts.createOrReplaceTempView("FileLayouts")

# COMMAND ----------

# DBTITLE 1,Load Source Dataframe
def LoadSource(memFolderPath):        
  #load delta into spark dataframe
  dfMBPGold = spark.read.format("delta").load(memFolderPath)

  #create windowed partition to generate unique row numbers based on the data
  windowPartition = Window.partitionBy(col("FileId")).orderBy(col("RecordHash").desc())

  sparkMem_df = dfMBPGold.distinct() \
            .withColumn("RecordHash", sha2(concat_ws("||", *dfMBPGold.columns),256)) \
            .withColumn("RowNumber", row_number().over(windowPartition)) \
            .withColumn("UniqueRecord", concat_ws("-",col("FileID"),col("RowNumber"))) \
            .withColumn("BeneficiaryID", upper(trim(col("BeneficiaryID")))) \
            .withColumn("PlanMemberID", upper(trim(col("PlanMemberID")))) \
            .withColumn("UniquePersonkey", upper(trim(col("UniquePersonkey")))) \
            .withColumn("LastName", upper(trim(col("LastName")))) \
            .withColumn("FirstName", upper(trim(col("FirstName")))) \
            .withColumn("LastInitial", upper(substring(trim(col("LastName")),1,1))) \
            .withColumn("FirstInitial", upper(substring(trim(col("FirstName")),1,1))) \
            .withColumn("DateofBirthFormatted",date_format(trim(col("DateofBirth")),"yyyyMMdd")) \
            .withColumn("PhoneNumber", trim(col("PhoneNumber"))) \
            .withColumn("PhoneNumberFormatted", regexp_replace(trim(col("PhoneNumber")),"[^0-9]","")) \
            .withColumn("PermanentAddressLine1", upper(trim(col("PermanentAddressLine1")))) \
            .select( 
                  col("UniqueRecord") #Will be BISInternalPersonId
                 ,col("FileLayoutID")
                 ,col("FileID")
                 ,col("RowNumber")
                 ,col("LastName")
                 ,col("FirstName")
                 ,col("Gender")
                 ,col("PhoneNumber")
                 ,col("PermanentAddressLine1")
                 ,col("DateofBirthFormatted")
                 ,col("PlanMemberID")
                 ,col("BeneficiaryID")
                 ,col("UniquePersonKey")
                 ,col("LastInitial")
                 ,col("FirstInitial")
                 ,col("PhoneNumberFormatted")
             ) \
            .filter("FileLayoutID IN (SELECT fl.FileLayoutID FROM FileLayouts fl)")
  #.where(upper(col("FileLayoutID")).isin(getNonMemOutFileLayouts["FileLayoutID"]))
  
  return sparkMem_df

# COMMAND ----------

# DBTITLE 1,Rules all currently are exact matches
def RulesToCompare(rules, pandasMem_df):
  matchesAllRules_df = pd.DataFrame()

  for lst in rules:
    #Indexing step for block
    indexer = recordlinkage.Index()
    indexer.block(lst[0])

    #capture and print number of candidates
    candidatesBlock = indexer.index(pandasMem_df)
    print(f"Number of candidates: {len(candidatesBlock)}")

    #Compare and link like records with Exact matches
    # Comparison step
    compareBlock = recordlinkage.Compare()
    threshold = lst[-1]

    for col in CompareColumns:
      compareBlock.exact(col, col, label=str(col))

    features = compareBlock.compute(candidatesBlock, pandasMem_df)

    features[lst[0]] = features[lst[0]].apply(lambda x: x*10)

    matchesRule = features[features[lst[:-1]].sum(axis=1) >= threshold]
    matchesRule_df = matchesRule.index.to_frame()
    matchesAllRules_df = matchesAllRules_df.append(matchesRule_df)
  
  return matchesAllRules_df

# COMMAND ----------

# DBTITLE 1,Indexing step for block
def RunLinking(sparkMem_df):
  #convert spark dataframe to pandas for recordlinkage to work
  pandasMem_df = sparkMem_df.toPandas()
  pandasMem_df.set_index("UniqueRecord")

  #combine the dataframes for exact matches by Rule
  dfCombined = RulesToCompare(RulesAll, pandasMem_df)

  #Rename columns and reset index for columnA as A
  dfMatchedColumnA = dfCombined.rename(columns={0:"A",1:"B"})

  #Rename columns and reset index for columnB as A 
  dfMatchedColumnB = dfCombined.rename(columns={0:"B",1:"A"})

  #merge two dataframes together 
  dfMatched = pd.concat([dfMatchedColumnA,dfMatchedColumnB], ignore_index=True)

  #remove the duplicates from the merged dataframes
  dfMatched.drop_duplicates(inplace=True)

  #########Combine all matches to generate a grouping column named Match#############
  #Reverse A and B to get a list of all records per id. Reindex and remove unneeded columns, basically combining all A and B into column A and all column A and B into B -- complete set
  matchesAll_df = pd.concat([dfMatched[["A","B"]].rename(columns={"A": "Record", "B": "Match"}) \
                          ,dfMatched[["B","A"]].rename(columns={"B": "Record", "A": "Match"}) \
                          ]).reset_index()

  ##Get the Record and store it in the Match column... this is so when we group we will have that record in the list
  matchesSame_df = matchesAll_df[["Record","Record"]]
  matchesSame_df.columns=['Record', 'Match'] 

  #Merge matches with the record dataframe to get a comprehensive list of ids
  matchesAll_df = pd.concat([matchesAll_df,matchesSame_df])

  #dropping duplicates
  matchesAll_df.drop_duplicates(inplace=True)

  #Create distinct record per group based on columnA
  distinctRow = dfMatched.groupby('A').head(1).drop('B', axis=1)

  #Join all matches with the distinct rules
  matchesAll_df = pd.merge(matchesAll_df, distinctRow, how="left",left_on="Record", right_on="A").drop('A', axis=1)

  ######Combine all ColumnA and all ColumnB that match. Ensure this only runs once will append multiple times if not########
  ##Get Record and MatchID from parents tables
  matchesAll_df = pd.merge(matchesAll_df,pandasMem_df["UniqueRecord"],left_on="Record", right_index=True).rename(columns={"UniqueRecord":"RecordID"})
  matchesAll_df = pd.merge(matchesAll_df,pandasMem_df["UniqueRecord"],left_on="Match", right_index=True).rename(columns={"UniqueRecord":"MatchID"})

  ######Combine all ColumnA and all ColumnB that match#####
  #Create a list of each recordid by using groupby()
  matched_df = matchesAll_df.groupby("RecordID") \
        .agg({"MatchID": lambda x: list(pd.unique(x))}) \
        .reset_index()
  matched_df["MatchID"] = matched_df["MatchID"].apply(lambda x: sorted(x))

  ########Rejoin to all matches to maintain Rule and Threshold column#######
  matchesAllModified = matchesAll_df.groupby("RecordID").head(1).drop('MatchID', axis=1).drop('Match', axis=1).drop('index', axis=1).drop('Record', axis=1)
  newDFToMatch = pd.merge(matched_df, matchesAllModified, how="left",left_on="RecordID", right_on="RecordID")

  ########Create full list dataframe; including matches and non matches#######
  finalPandas_df = pandasMem_df.merge(newDFToMatch,left_on="UniqueRecord", right_on="RecordID", how="left")
  finalPandas_df['MatchID'] = finalPandas_df['MatchID'].fillna(finalPandas_df['UniqueRecord'])

  return spark.createDataFrame(finalPandas_df.astype(str))

# COMMAND ----------

# DBTITLE 1,Query for Final Dataframe output
finalSQL = """WITH BISPersonWithIdentifiers AS(
SELECT 
   UniqueRecord
  ,FileLayoutID
  ,FileId
  ,RowNumber
  ,LastName
  ,FirstName
  ,DateofBirthFormatted AS DateOfBirth
  ,Gender
  ,PermanentAddressLine1
  ,PhoneNumber
  ,PlanMemberID
  ,BeneficiaryID
  ,UniquePersonKey
  ,case when instr(MatchID,",")=0 then MatchID else substr(MatchID,2,instr(MatchID,",")) end as MatchID
  ,ROW_NUMBER() OVER(PARTITION BY  (case when instr(MatchID,",")=0 then MatchID else substr(MatchID,2,instr(MatchID,",")) end)  
                      ORDER BY FileId ASC, RowNumber ASC) AS FirstPersonIdentifier
  ,ROW_NUMBER() OVER(PARTITION BY  (case when instr(MatchID,",")=0 then MatchID else substr(MatchID,2,instr(MatchID,",")) end)  
                      ORDER BY FileId DESC, RowNumber DESC) AS CurrentPersonIdentifier
FROM BISCompletePersonTable
)
,MemberPersonBridge AS(
SELECT 
   fp.UniqueRecord AS BISInternalPersonID
  ,CASE WHEN cp.CurrentPersonIdentifier = 1 THEN 1 ELSE 0 END AS IsCurrent
  ,cp.UniqueRecord
  ,cp.FileLayoutID
  ,cp.FileId
  ,cp.RowNumber
  ,cp.LastName
  ,cp.FirstName
  ,cp.DateofBirth AS DateOfBirth
  ,cp.Gender
  ,cp.PermanentAddressLine1
  ,cp.PhoneNumber
  ,cp.PlanMemberID
  ,cp.BeneficiaryID
  ,cp.UniquePersonKey
  ,cp.MatchID
FROM BISPersonWithIdentifiers cp
  LEFT JOIN BISPersonWithIdentifiers fp -- to get BISInternalPerson -- FirstPersonIdentifier should be the BISInternalPersonID
    ON cp.MatchId = fp.MatchId
      AND fp.FirstPersonIdentifier = 1
)
,MemberPersonBridge_CurrPlanMbr AS(
SELECT 
   BISInternalPersonID
  ,IsCurrent
  ,UniqueRecord
  ,FileLayoutID
  ,FileId
  ,RowNumber
  ,LastName
  ,FirstName
  ,DateOfBirth
  ,Gender
  ,PermanentAddressLine1
  ,PhoneNumber
  ,PlanMemberID
  ,BeneficiaryID
  ,ifnull(nullif(PlanMemberID,'None'),'') AS PlanMemberIdModified
  ,ifnull(nullif(UniquePersonKey,'None'),'') AS UniquePersonKeyModified
  ,UniquePersonKey
  ,MatchID
  ,case when ifnull(PlanMemberID,'None')='None' then null 
       when row_number() over(partition by PlanMemberID order by FileId desc, RowNumber desc) = 1 then 1
   else 0 end as IsCurrentPlanMemberID
  ,case when ifnull(UniquePersonKey,'None')='None' then null 
       when row_number() over(partition by UniquePersonKey order by FileId desc, RowNumber desc) = 1 then 1
   else 0 end as IsCurrentUniquePersonKey
  ,case when BISInternalPersonID = UniqueRecord then 1 else 0 end AS IsOriginalMemberID 
FROM MemberPersonBridge
)
,PUModPop AS(
SELECT
    *
    ,CASE WHEN PlanMemberIdModified <> '' THEN 1 ELSE 0 END AS IsPlanMemberIdPopulated
    ,CASE WHEN UniquePersonKeyModified <> '' THEN 1 ELSE 0 END AS IsUniquePersonKeyModifiedPopulated
    ,concat(PlanMemberIdModified,'-',UniquePersonKeyModified) AS PMUP
FROM MemberPersonBridge_CurrPlanMbr
)
,Final AS (
SELECT
    *
    ,CASE WHEN IsPlanMemberIdPopulated = 1 AND IsUniquePersonKeyModifiedPopulated = 1 THEN 'Fail' --this will fail the processing intentionally
        ELSE COALESCE(IsCurrentPlanMemberID,IsCurrentUniquePersonKey)
     END AS IsCurrentPMUP
FROM PUModPop
)
SELECT 
   BISInternalPersonID
  ,IsCurrent
  ,UniqueRecord
  ,FileLayoutID
  ,FileId
  ,LastName
  ,FirstName
  ,DateOfBirth
  ,Gender
  ,PermanentAddressLine1
  ,PhoneNumber
  ,PlanMemberID
  ,BeneficiaryID
  ,UniquePersonKey
  ,sha2(concat_ws("|",
              IfNull(BISInternalPersonID,"") 
             ,IfNull(IsCurrent,"")
             ,IfNull(UniqueRecord,"")
             ,IfNull(FileLayoutID,"") 
             ,IfNull(FileId,"") 
             ,IfNull(LastName,"") 
             ,IfNull(FirstName,"") 
             ,IfNull(DateOfBirth,"")
             ,IfNull(Gender,"") 
             ,IfNull(PermanentAddressLine1,"") 
             ,IfNull(PhoneNumber,"")              
             ,IfNull(PlanMemberID,"") 
             ,IfNull(BeneficiaryID,"")
             ,IfNull(UniquePersonKey,"")
             ,IfNull(IsCurrentPlanMemberID,"")
             ,IfNull(IsCurrentUniquePersonKey,"")
             ,IfNull(IsOriginalMemberID,"")
             ,IfNull(PMUP,"")
             ,IfNull(IsCurrentPMUP,"")
      ), 256) AS hashKey
  ,IsCurrentPlanMemberID 
  ,IsCurrentUniquePersonKey
  ,IsOriginalMemberID
  ,PMUP
  ,CAST(IsCurrentPMUP AS INT)AS IsCurrentPMUP
FROM Final"""

# COMMAND ----------

# DBTITLE 1,MergeQuery
mergeSQL = """
MERGE INTO DestinationTable t 
USING (
	SELECT 
		 BISInternalPersonID
        ,IsCurrent
        ,UniqueRecord
        ,FileLayoutID
        ,FileId
        ,LastName
        ,FirstName
        ,DateOfBirth
        ,Gender
        ,PermanentAddressLine1
        ,PhoneNumber
        ,PlanMemberID
        ,BeneficiaryID
        ,UniquePersonKey
        ,hashKey
        ,IsCurrentPlanMemberID
        ,IsCurrentUniquePersonKey
        ,IsOriginalMemberID
        ,PMUP
        ,IsCurrentPMUP
	FROM tempSQLScript 
) s 
    ON t.UniqueRecord = s.UniqueRecord
WHEN MATCHED AND s.hashKey <> t.hashKey THEN
UPDATE SET 
       BISInternalPersonID = s.BISInternalPersonID
      ,IsCurrent = s.IsCurrent
      ,UniqueRecord = s.UniqueRecord
      ,FileLayoutID = s.FileLayoutID
      ,FileId = s.FileId
      ,LastName = s.LastName
      ,FirstName = s.FirstName
      ,DateOfBirth = s.DateOfBirth
      ,Gender = s.Gender
      ,PermanentAddressLine1 = s.PermanentAddressLine1
      ,PhoneNumber = s.PhoneNumber
      ,PlanMemberID = s.PlanMemberID
      ,BeneficiaryID = s.BeneficiaryID
      ,UniquePersonKey = s.UniquePersonKey
      ,hashKey = s.hashKey
      ,IsCurrentPlanMemberID = s.IsCurrentPlanMemberID
      ,IsCurrentUniquePersonKey = s.IsCurrentUniquePersonKey
      ,IsOriginalMemberID = s.IsOriginalMemberID
      ,PMUP = s.PMUP
      ,IsCurrentPMUP = s.IsCurrentPMUP
WHEN NOT MATCHED THEN 
INSERT (
		 BISInternalPersonID
        ,IsCurrent
        ,UniqueRecord
        ,FileLayoutID
        ,FileId
        ,LastName
        ,FirstName
        ,DateOfBirth
        ,Gender
        ,PermanentAddressLine1
        ,PhoneNumber
        ,PlanMemberID
        ,BeneficiaryID
        ,UniquePersonKey
        ,hashKey
        ,IsCurrentPlanMemberID
        ,IsCurrentUniquePersonKey
        ,IsOriginalMemberID
        ,PMUP
        ,IsCurrentPMUP
) 
VALUES (
        s.BISInternalPersonID
        ,s.IsCurrent
        ,s.UniqueRecord
        ,s.FileLayoutID
        ,s.FileId
        ,s.LastName
        ,s.FirstName
        ,s.DateOfBirth
        ,s.Gender
        ,s.PermanentAddressLine1
        ,s.PhoneNumber
        ,s.PlanMemberID
        ,s.BeneficiaryID
        ,s.UniquePersonKey
        ,s.hashKey
        ,s.IsCurrentPlanMemberID
        ,s.IsCurrentUniquePersonKey
        ,s.IsOriginalMemberID
        ,s.PMUP
        ,s.IsCurrentPMUP
        )
"""

# COMMAND ----------

# DBTITLE 1,path_exists
def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, StringType, IntegerType, LongType

def CreateEmptyDataframe():
  schema = StructType([ \
    StructField("UniqueRecord",StringType(),True), \
    StructField("FileLayoutID",StringType(),True), \
    StructField("FileId",StringType(),True), \
    StructField("RowNumber", StringType(), True), \
    StructField("LastName", StringType(), True), \
    StructField("FirstName", StringType(), True), \
    StructField("DateofBirth", StringType(), True), \
    StructField("Gender", StringType(), True), \
    StructField("PermanentAddressLine1", StringType(), True), \
    StructField("PhoneNumber", StringType(), True), \
    StructField("PlanMemberID", StringType(), True), \
    StructField("BeneficiaryID", StringType(), True), \
    StructField("UniquePersonKey", StringType(), True), \
    StructField("hashKey", StringType(), True) \
  ]) 
  
  emptyRDD = spark.sparkContext.emptyRDD()
  
  return spark.createDataFrame(emptyRDD,schema)

# COMMAND ----------

# DBTITLE 1,Merged Spark dataframes to get to final dataframe
Exists = path_exists(memFolderPath)

if(Exists):
  sparkMem_df = LoadSource(memFolderPath)
  numRows = sparkMem_df.count()
  
  if(numRows == 0):
    convertedSpark_df = CreateEmptyDataframe()
  else: 
    convertedSpark_df = RunLinking(sparkMem_df) #executes the matching
    convertedSpark_df = convertedSpark_df.withColumn("FileID", col("FileID").cast(LongType())) \
                                        .withColumn("RowNumber", col("RowNumber").cast(LongType()))

# convertedSpark_df.printSchema()
convertedSpark_df.createOrReplaceTempView("BISCompletePersonTable")

# spark.sql("SELECT * FROM BISCompletePersonTable").show()

#load final sql script
temp_df = spark.sql(finalSQL)
temp_df.createOrReplaceTempView("tempSQLScript")

if (temp_df.filter("IsCurrentPMUP IS NULL").count() > 0):
  raise Exception("Failed as records contain both a PlanMemberID and UniquePersonKey")
else:
  #if path doesnt exist write temp_df to it
  if(path_exists(goldMemFolderPath) is False):
    print("Creating table new at: " + goldMemFolderPath)
    temp_df.write.format("delta").mode("append").save(goldMemFolderPath) 
  else:
    print("Updating table at: " + goldMemFolderPath)
    #Merge schema
    destinationDataModel = spark.createDataFrame(spark.sparkContext.emptyRDD(), temp_df.schema)
    destinationDataModel.write.format("delta").option("mergeSchema", "true").mode("append").save(goldMemFolderPath)
    
    #load destination table
    dfGoldMemberPersonBridge = spark.read.format("delta").load(goldMemFolderPath)
    dfGoldMemberPersonBridge.createOrReplaceTempView("DestinationTable")
  
    #run merge script
    spark.sql(mergeSQL)
