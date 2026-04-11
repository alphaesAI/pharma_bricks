# Databricks notebook source
# DBTITLE 1,Declare variables
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

clientCode = dbutils.widgets.get("ClientContainer") 
mntPnt = '/mnt/'
consolidateMemFolderPath = mntPnt + clientCode + "/consolidated/MA/Data/Member"
goldMemPerBrdgFolderPath = mntPnt + clientCode + "/Gold/MA/Client/MemberPersonBridge"
goldMemFolderPath = mntPnt + clientCode + "/Gold/MA/Client/Member"

print("Client: " + clientCode)
print("consolidateMemFolderPath: " + consolidateMemFolderPath)
print("goldMemPerBrdgFolderPath: " + goldMemPerBrdgFolderPath)
print("goldMemFolderPath: " + goldMemFolderPath)

# COMMAND ----------

# DBTITLE 1,SQL Config DB connection
dbEnv = spark.conf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
envLetter = "" 
envUser="_ETLUSER_SQL"
blobKey = ""

if(dbEnv == "934226345849410"):
  envLetter = "d"
  envUser = "DEV"+envUser
elif(dbEnv == "5826678703751685"):
  envLetter = "q"
  envUser = "QA"+envUser
elif(dbEnv == "7093677384385470"):
  envLetter = "s"
  envUser = "STG"+envUser
else:
  envLetter = "p"
  envUser = "PRD"+envUser

jdbcPort = "1433"
jdbcUsername = envUser
jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")

jdbcHostname = "sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net"
jdbcDatabase = "Configuration_DB_"+ clientCode.upper()
jdbcPort = "1433"

jdbcUrl = "jdbc:sqlserver://" + jdbcHostname+":"+jdbcPort +";database="+jdbcDatabase  

jdbcProperties = {
              "user" : jdbcUsername,
              "password" : jdbcPassword,
              "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
            }

# COMMAND ----------

def path_exists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Temp view for refFileLayout
pushdown_query = "(SELECT FileLayoutID FROM refFileLayout where FilterEntity='GoldMember') a"
df = spark.read.jdbc(url=jdbcUrl, table=pushdown_query, properties=jdbcProperties)
df.createOrReplaceTempView("refFileLayout")

# COMMAND ----------

# DBTITLE 1,Source SQL
srcsql= """
WITH consolidateMem1 as
(
  SELECT
    brdg.BISInternalPersonID
   ,brdg.UniqueRecord 
   ,mem.ClientID
   ,mem.FileID
   ,mem.LoadDateTime
   ,mem.FileLayoutID
   ,mem.FileLayoutDescription
   ,mem.UniquePersonKey
   ,mem.PlanMemberID
   ,mem.SubscriberID
   ,mem.BeneficiaryID
   ,mem.LastName
   ,mem.FirstName
   ,mem.MiddleInitial
   ,mem.EnrolleeUniqueID
   ,mem.DateofBirth
   ,mem.DeceasedDate
   ,mem.Gender
   ,mem.PermanentAddressLine1
   ,mem.PermanentAddressLine2
   ,mem.PermanentCity
   ,mem.PermanentCounty
   ,mem.PermanentState
   ,mem.PermanentZipCode
   ,mem.MailingAddressLine1
   ,mem.MailingAddressLine2
   ,mem.MailingCity
   ,mem.MailingState
   ,mem.MailingZipCode
   ,mem.MailingCounty
   ,mem.PhoneNumber
   ,mem.Email
   ,mem.MedicaidID
   ,mem.Fax
   ,mem.RaceCode
   ,mem.RaceDataSource
   ,mem.CaretakerFirstName
   ,mem.CaretakerLastName
   ,mem.CaretakerMiddleInitial
   ,mem.EthnicityCode
   ,mem.EthnicityDatasource
   ,mem.SpokenLanguage
   ,mem.SpokenLanguagesourcecode
   ,mem.WrittenLanguageCode
   ,mem.WrittenLanguageSourcecode
   ,mem.OtherLanguage
   ,mem.OtherLanguageSourcecode
   ,mem.USCitizen
   ,mem.AlternateKey1
   ,mem.AlternateKey2
   ,mem.AlternateKey3
   ,mem.AlternateKey4
   ,mem.AlternateKey5
   ,mem.AlternateKey6
   ,mem.AlternateKey7
   ,mem.AlternateKey8
   ,mem.AlternateKey9
   ,mem.AlternateKey10
   ,mem.MaskedMemberID
   ,mem.EnrolleeEducation
   ,mem.EnrolleeEmployment
   ,brdg.PMUP
   ,brdg.IsCurrentPMUP
   ,mem.ProductID
  FROM consolidateMem mem
  INNER JOIN refFileLayout ref
   ON ref.FileLayoutID = mem.FileLayoutID
  INNER JOIN goldMemPerBrdg brdg
   ON mem.UniqueRecord = brdg.UniqueRecord
   AND ref.FileLayoutID = brdg.FileLayoutID
   AND brdg.IsCurrentPMUP = 1
 )

SELECT 
  BISInternalPersonID
 ,UniqueRecord 
 ,ClientID
 ,FileID
 ,LoadDateTime
 ,FileLayoutID
 ,FileLayoutDescription
 ,UniquePersonKey
 ,PlanMemberID
 ,SubscriberID
 ,BeneficiaryID
 ,LastName
 ,FirstName
 ,MiddleInitial
 ,EnrolleeUniqueID
 ,DateofBirth
 ,DeceasedDate
 ,Gender
 ,PermanentAddressLine1
 ,PermanentAddressLine2
 ,PermanentCity
 ,PermanentCounty
 ,PermanentState
 ,PermanentZipCode
 ,MailingAddressLine1
 ,MailingAddressLine2
 ,MailingCity
 ,MailingState
 ,MailingZipCode
 ,MailingCounty
 ,PhoneNumber
 ,Email
 ,MedicaidID
 ,Fax
 ,RaceCode
 ,RaceDataSource
 ,CaretakerFirstName
 ,CaretakerLastName
 ,CaretakerMiddleInitial
 ,EthnicityCode
 ,EthnicityDatasource
 ,SpokenLanguage
 ,SpokenLanguagesourcecode
 ,WrittenLanguageCode
 ,WrittenLanguageSourcecode
 ,OtherLanguage
 ,OtherLanguageSourcecode
 ,USCitizen
 ,AlternateKey1
 ,AlternateKey2
 ,AlternateKey3
 ,AlternateKey4
 ,AlternateKey5
 ,AlternateKey6
 ,AlternateKey7
 ,AlternateKey8
 ,AlternateKey9
 ,AlternateKey10
 ,MaskedMemberID
 ,EnrolleeEducation
 ,EnrolleeEmployment
 ,PMUP
 ,IsCurrentPMUP
 ,ProductID
 ,sha2(
     concat(IfNull(BISInternalPersonID,"")
     ,"|",IfNull(UniqueRecord,"")
	 ,"|",IfNull(ClientID,"")
     ,"|",IfNull(FileID,"")
     ,"|",IfNull(LoadDateTime,"")
     ,"|",IfNull(FileLayoutID,"")
     ,"|",IfNull(FileLayoutDescription,"")
     ,"|",IfNull(UniquePersonKey,"")
     ,"|",IfNull(PlanMemberID,"")
     ,"|",IfNull(SubscriberID,"")
     ,"|",IfNull(BeneficiaryID,"")
     ,"|",IfNull(LastName,"")
     ,"|",IfNull(FirstName,"")
     ,"|",IfNull(MiddleInitial,"")
     ,"|",IfNull(EnrolleeUniqueID,"")
     ,"|",IfNull(DateofBirth,"")
     ,"|",IfNull(DeceasedDate,"")
     ,"|",IfNull(Gender,"")
     ,"|",IfNull(PermanentAddressLine1,"")
     ,"|",IfNull(PermanentAddressLine2,"")
     ,"|",IfNull(PermanentCity,"")
     ,"|",IfNull(PermanentCounty,"")
     ,"|",IfNull(PermanentState,"")
     ,"|",IfNull(PermanentZipCode,"")
     ,"|",IfNull(MailingAddressLine1,"")
     ,"|",IfNull(MailingAddressLine2,"")
     ,"|",IfNull(MailingCity,"")
     ,"|",IfNull(MailingState,"")
     ,"|",IfNull(MailingZipCode,"")
     ,"|",IfNull(MailingCounty,"")
     ,"|",IfNull(PhoneNumber,"")
     ,"|",IfNull(Email,"")
     ,"|",IfNull(MedicaidID,"")
     ,"|",IfNull(Fax,"")
     ,"|",IfNull(RaceCode,"")
     ,"|",IfNull(RaceDataSource,"")
     ,"|",IfNull(CaretakerFirstName,"")
     ,"|",IfNull(CaretakerLastName,"")
     ,"|",IfNull(CaretakerMiddleInitial,"")
     ,"|",IfNull(EthnicityCode,"")
     ,"|",IfNull(EthnicityDatasource,"")
     ,"|",IfNull(SpokenLanguage,"")
     ,"|",IfNull(SpokenLanguagesourcecode,"")
     ,"|",IfNull(WrittenLanguageCode,"")
     ,"|",IfNull(WrittenLanguageSourcecode,"")
     ,"|",IfNull(OtherLanguage,"")
     ,"|",IfNull(OtherLanguageSourcecode,"")
     ,"|",IfNull(USCitizen,"")
     ,"|",IfNull(AlternateKey1,"")
     ,"|",IfNull(AlternateKey2,"")
     ,"|",IfNull(AlternateKey3,"")
     ,"|",IfNull(AlternateKey4,"")
     ,"|",IfNull(AlternateKey5,"")
     ,"|",IfNull(AlternateKey6,"")
     ,"|",IfNull(AlternateKey7,"")
     ,"|",IfNull(AlternateKey8,"")
     ,"|",IfNull(AlternateKey9,"")
     ,"|",IfNull(AlternateKey10,"")
     ,"|",IfNull(MaskedMemberID,"")
     ,"|",IfNull(EnrolleeEducation,"")
     ,"|",IfNull(EnrolleeEmployment,"")
     ,"|",IfNull(PMUP,"")
     ,"|",IfNull(IsCurrentPMUP,"")
     ,"|",IfNull(ProductID,"")
     ),256
   ) AS HashKey 
  FROM consolidateMem1
  """

# COMMAND ----------

# DBTITLE 1,Merge SQL
mrgsql= """
MERGE INTO DestinationTable t
USING (SELECT * FROM tempSQLScript)s ON s.PMUP = t.PMUP
WHEN MATCHED AND t.HashKey <> s.HashKey THEN 
UPDATE SET
 BISInternalPersonID = s.BISInternalPersonID
,UniqueRecord = s.UniqueRecord 
,ClientID = s.ClientID
,FileID = s.FileID
,LoadDateTime = s.LoadDateTime
,FileLayoutID = s.FileLayoutID
,FileLayoutDescription = s.FileLayoutDescription
,UniquePersonKey = s.UniquePersonKey
,PlanMemberID = s.PlanMemberID
,SubscriberID = s.SubscriberID
,BeneficiaryID = s.BeneficiaryID
,LastName = s.LastName
,FirstName = s.FirstName
,MiddleInitial = s.MiddleInitial
,EnrolleeUniqueID = s.EnrolleeUniqueID
,DateofBirth = s.DateofBirth
,DeceasedDate = s.DeceasedDate
,Gender = s.Gender
,PermanentAddressLine1 = s.PermanentAddressLine1
,PermanentAddressLine2 = s.PermanentAddressLine2
,PermanentCity = s.PermanentCity
,PermanentCounty = s.PermanentCounty
,PermanentState = s.PermanentState
,PermanentZipCode = s.PermanentZipCode
,MailingAddressLine1 = s.MailingAddressLine1
,MailingAddressLine2 = s.MailingAddressLine2
,MailingCity = s.MailingCity
,MailingState = s.MailingState
,MailingZipCode = s.MailingZipCode
,MailingCounty = s.MailingCounty
,PhoneNumber = s.PhoneNumber
,Email = s.Email
,MedicaidID = s.MedicaidID
,Fax = s.Fax
,RaceCode = s.RaceCode
,RaceDataSource = s.RaceDataSource
,CaretakerFirstName = s.CaretakerFirstName
,CaretakerLastName = s.CaretakerLastName
,CaretakerMiddleInitial = s.CaretakerMiddleInitial
,EthnicityCode = s.EthnicityCode
,EthnicityDatasource = s.EthnicityDatasource
,SpokenLanguage = s.SpokenLanguage
,SpokenLanguagesourcecode = s.SpokenLanguagesourcecode
,WrittenLanguageCode = s.WrittenLanguageCode
,WrittenLanguageSourcecode = s.WrittenLanguageSourcecode
,OtherLanguage = s.OtherLanguage
,OtherLanguageSourcecode = s.OtherLanguageSourcecode
,USCitizen = s.USCitizen
,AlternateKey1 = s.AlternateKey1
,AlternateKey2 = s.AlternateKey2
,AlternateKey3 = s.AlternateKey3
,AlternateKey4 = s.AlternateKey4
,AlternateKey5 = s.AlternateKey5
,AlternateKey6 = s.AlternateKey6
,AlternateKey7 = s.AlternateKey7
,AlternateKey8 = s.AlternateKey8
,AlternateKey9 = s.AlternateKey9
,AlternateKey10 = s.AlternateKey10
,MaskedMemberID = s.MaskedMemberID
,EnrolleeEducation = s.EnrolleeEducation
,EnrolleeEmployment = s.EnrolleeEmployment
,PMUP = s.PMUP
,IsCurrentPMUP = s.IsCurrentPMUP
,HashKey  = s.HashKey 
,ProductID = s.ProductID
WHEN NOT MATCHED THEN 
INSERT (BISInternalPersonID
 ,UniqueRecord
 ,ClientID
 ,FileID
 ,LoadDateTime
 ,FileLayoutID
 ,FileLayoutDescription
 ,UniquePersonKey
 ,PlanMemberID
 ,SubscriberID
 ,BeneficiaryID
 ,LastName
 ,FirstName
 ,MiddleInitial
 ,EnrolleeUniqueID
 ,DateofBirth
 ,DeceasedDate
 ,Gender
 ,PermanentAddressLine1
 ,PermanentAddressLine2
 ,PermanentCity
 ,PermanentCounty
 ,PermanentState
 ,PermanentZipCode
 ,MailingAddressLine1
 ,MailingAddressLine2
 ,MailingCity
 ,MailingState
 ,MailingZipCode
 ,MailingCounty
 ,PhoneNumber
 ,Email
 ,MedicaidID
 ,Fax
 ,RaceCode
 ,RaceDataSource
 ,CaretakerFirstName
 ,CaretakerLastName
 ,CaretakerMiddleInitial
 ,EthnicityCode
 ,EthnicityDatasource
 ,SpokenLanguage
 ,SpokenLanguagesourcecode
 ,WrittenLanguageCode
 ,WrittenLanguageSourcecode
 ,OtherLanguage
 ,OtherLanguageSourcecode
 ,USCitizen
 ,AlternateKey1
 ,AlternateKey2
 ,AlternateKey3
 ,AlternateKey4
 ,AlternateKey5
 ,AlternateKey6
 ,AlternateKey7
 ,AlternateKey8
 ,AlternateKey9
 ,AlternateKey10
 ,MaskedMemberID
 ,EnrolleeEducation
 ,EnrolleeEmployment
 ,PMUP
 ,IsCurrentPMUP
 ,HashKey 
 ,ProductID
)
VALUES (s.BISInternalPersonID
 ,s.UniqueRecord
 ,s.ClientID
 ,s.FileID
 ,s.LoadDateTime
 ,s.FileLayoutID
 ,s.FileLayoutDescription
 ,s.UniquePersonKey
 ,s.PlanMemberID
 ,s.SubscriberID
 ,s.BeneficiaryID
 ,s.LastName
 ,s.FirstName
 ,s.MiddleInitial
 ,s.EnrolleeUniqueID
 ,s.DateofBirth
 ,s.DeceasedDate
 ,s.Gender
 ,s.PermanentAddressLine1
 ,s.PermanentAddressLine2
 ,s.PermanentCity
 ,s.PermanentCounty
 ,s.PermanentState
 ,s.PermanentZipCode
 ,s.MailingAddressLine1
 ,s.MailingAddressLine2
 ,s.MailingCity
 ,s.MailingState
 ,s.MailingZipCode
 ,s.MailingCounty
 ,s.PhoneNumber
 ,s.Email
 ,s.MedicaidID
 ,s.Fax
 ,s.RaceCode
 ,s.RaceDataSource
 ,s.CaretakerFirstName
 ,s.CaretakerLastName
 ,s.CaretakerMiddleInitial
 ,s.EthnicityCode
 ,s.EthnicityDatasource
 ,s.SpokenLanguage
 ,s.SpokenLanguagesourcecode
 ,s.WrittenLanguageCode
 ,s.WrittenLanguageSourcecode
 ,s.OtherLanguage
 ,s.OtherLanguageSourcecode
 ,s.USCitizen
 ,s.AlternateKey1
 ,s.AlternateKey2
 ,s.AlternateKey3
 ,s.AlternateKey4
 ,s.AlternateKey5
 ,s.AlternateKey6
 ,s.AlternateKey7
 ,s.AlternateKey8
 ,s.AlternateKey9
 ,s.AlternateKey10
 ,s.MaskedMemberID
 ,s.EnrolleeEducation
 ,s.EnrolleeEmployment
 ,s.PMUP
 ,s.IsCurrentPMUP
 ,s.HashKey 
 ,s.ProductID
)
"""

# COMMAND ----------

# DBTITLE 1,Build Gold Member
from pyspark.sql.functions import date_format, monotonically_increasing_id, sha2, concat_ws, col, row_number
from pyspark.sql.window import Window

if(path_exists(consolidateMemFolderPath) and path_exists(goldMemPerBrdgFolderPath)):
  dfconsolidateMemSrc = spark.read.format("delta").load(consolidateMemFolderPath)
  dfgoldMemPerBrdg = spark.read.format("delta").load(goldMemPerBrdgFolderPath)
  windowPartition = Window.partitionBy(col("FileId")).orderBy(col("RecordHash").desc())
  dfconsolidateMem = dfconsolidateMemSrc.distinct() \
              .withColumn("RecordHash", sha2(concat_ws("||", *dfconsolidateMemSrc.columns),256)) \
              .withColumn("RowNumber", row_number().over(windowPartition)) \
              .withColumn("UniqueRecord", concat_ws("-",col("FileID"),col("RowNumber")))
  dfconsolidateMem.createOrReplaceTempView("consolidateMem")
  dfgoldMemPerBrdg.createOrReplaceTempView("goldMemPerBrdg")

  dfsrc = spark.sql(srcsql).cache()
  dfsrc.createOrReplaceTempView("tempSQLScript")

  dfgoldMemFolderPath = spark.read.format("delta").load(goldMemFolderPath)
  dfgoldMemFolderPath.createOrReplaceTempView("DestinationTable")

  spark.sql(mrgsql)
