# Databricks notebook source
# DBTITLE 1,setup config
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConfigPath","","")

ClientCode = dbutils.widgets.get("ClientContainer")
SourceConfigPath = dbutils.widgets.get("ConfigPath")

MountPoint = "/mnt/"
FullConfigPath = MountPoint + SourceConfigPath

ClientCodeLower = ClientCode.lower()
ClientCodeUpper = ClientCode.upper()

print(ClientCode)
print(ClientCodeLower)
print(ClientCodeUpper)
print(SourceConfigPath)
print(FullConfigPath)

# COMMAND ----------

# DBTITLE 1,def source data
def mountSource():
  SourcePath = MountPoint + f"{ClientCodeLower}/Gold/MA/Q360/Q360ProviderLookup"
  Sourcedf = spark.read.format("delta").option("header","true").load(SourcePath)
  Sourcedf.createOrReplaceTempView("Q360ProviderLookup")
  print(SourcePath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def destination data
def mountDestination():
  DestinationPath = MountPoint + f"{ClientCodeLower}/Gold/MA/Q360/Q360Provider"
  Destinationdf = spark.read.format("delta").option("header","true").load(DestinationPath)
  Destinationdf.createOrReplaceTempView("Q360Provider")
  print(DestinationPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,def lookup data
def mountLookUp():
  LookUpPath = MountPoint + f"{ClientCodeLower}/consolidated/MA/Data/Provider"
  LookUpPathdf = spark.read.format("delta").option("header","true").load(LookUpPath)
  LookUpPathdf.createOrReplaceTempView("cProvider")
  print(LookUpPath)
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Run Source Query
def RunTempSQLScript():
  tempSQLScript=f"""
 with ProvIDDEA as (
select trim(ProviderID) as ProviderID,DEA
,row_number()over(partition by ProviderID order by FileID desc) rownum
 from cProvider)
 ,ProvIDDEAData as (
 select ProviderID,DEA from ProvIDDEA
 where rownum=1 and coalesce(DEA,'')<>''
 )
 ,ProvNPIDEA as (
 select NPI as ProviderNPI,DEA
,row_number()over(partition by NPI order by providerid asc,FileID desc) rownumb
 from cProvider)
 ,ProvNPIDEAData as (
 select ProviderNPI, DEA from ProvNPIDEA
 where rownumb=1 and coalesce(DEA,'')<>''
 )
,Final as (
SELECT
	 distinct
   src.ProviderID
	,CASE WHEN SpecialtyCode IN ('08','11','27','37','38','50','99','D8') THEN 'Y' ELSE 'N' END AS PCPFlag
	,CASE WHEN SpecialtyCode IN ('16','98') THEN 'Y' ELSE 'N' END AS OBGYNFlag
	,CASE 
    WHEN SpecialtyCode IN ('26','62','68','80','86') THEN 'Y' 
    WHEN Taxonomy IN (
      '101Y00000X',
      '101YA0400X',
      '101YM0800X',
      '101YP2500X',
      '101YS0200X',
      '102L00000X',
      '103G00000X',
      '103K00000X',
      '104100000X',
      '1041S0200X',
      '106H00000X' 
      ) THEN 'Y'
        ELSE 'N' 
   END AS MHProviderFlag
	,CASE WHEN SpecialtyCode IN ('18','41') THEN 'Y' ELSE 'N' END AS EyeCareProviderFlag
	,CASE 
    WHEN SpecialtyCode IN ('19','C5') THEN 'Y' 
    WHEN Taxonomy IN (
      '1223E0200X',
      '1223P0106X',
      '1223P0300X',
      '1223P0700X',
      '1223X0400X',
      '1223D0001X',
      '1223X0008X',
      '1223X2210X',
      '125K00000X',
      '126800000X'
    ) THEN 'Y'
      ELSE 'N' 
   END AS DentistFlag
	,CASE WHEN SpecialtyCode = '39' THEN 'Y' ELSE 'N' END AS NephrologistFlag
	,CASE WHEN SpecialtyCode IN ('05','32') THEN 'Y' ELSE 'N' END AS AnesthesiologistFlag
	,CASE WHEN SpecialtyCode = '50' THEN 'Y' ELSE 'N' END AS NPRProviderFlag
	,CASE WHEN SpecialtyCode = '97' THEN 'Y' ELSE 'N' END AS PASProviderFlag
	,Case WHEN '{ClientCodeLower}' IN ('bcbsne','qaidap1','devidap1') and coalesce(LKPID.DEA,LKPNPI.DEA)<>'' then 'Y'
        WHEN coalesce(Prescriber,'') <> '' THEN 'Y'
	      WHEN SpecialtyCode IN ('08','11','27','37','38','50','99','D8','26','86','A0') then 'Y'
	      ELSE 'N'
        end AS ProviderPrescribingPrivilegesFlag
	,CASE 
    WHEN Taxonomy IN (
    '1835P0018X',
    '183500000X',
    '1835P1200X',
    '1835P1300X',
    '1835P2201X',
    '1835X0200X'
    ) THEN 'Y'
    ELSE 'N' 
   END AS ClinicalPharmacistFlag
	,CASE 
    WHEN SpecialtyCode = 'A0' THEN 'Y'
    WHEN Taxonomy IN (
    '273100000X',
    '276400000X',
    '282NR1301X',
    '282NW0100X',
    '286500000X'
    ) THEN 'Y'
    ELSE 'N' 
   END AS HospitalFlag
	,CASE 
    WHEN SpecialtyCode = 'A1' THEN 'Y' 
    WHEN Taxonomy = '315P00000X'  THEN 'Y'
    ELSE 'N' 
   END AS SNFFlag
	,CASE WHEN SpecialtyCode IN ('02','14','19','20','24','28','33','40','76','77','78','85','91','D7') THEN 'Y' ELSE 'N' END AS SurgeonFlag
	,CASE 
    WHEN SpecialtyCode IN ('31','43') THEN 'Y'
    WHEN Taxonomy IN ( 
      '163W00000X',
      '163WC0200X',
      '163WC0400X',
      '163WC1500X',
      '163WD0400X',
      '163WG0000X',
      '163WL0100X',
      '163WM0705X',
      '163WP0200X',
      '163WP0808X',
      '163WP0809X',
      '163WS0200X',
      '163WW0101X' 
      ) THEN 'Y'
    ELSE 'N' 
   END AS RegisteredNurseFlag
	,CASE WHEN SpecialtyCode = '37' THEN 'Y' ELSE 'N' END AS PediatricianFlag
	,CASE WHEN SpecialtyCode = '46' THEN 'Y' ELSE 'N' END AS DiabetologistFlag
	,CASE WHEN SpecialtyCode = '71' THEN 'Y' ELSE 'N' END AS DieticianFlag
	,CASE 
    WHEN SpecialtyCode IN ('25','65') THEN 'Y'
    WHEN Taxonomy IN (
    '224Z00000X',
    '225200000X',
    '225400000X',
    '225500000X',
    '2255A2300X'
    ) THEN 'Y'
    ELSE 'N' 
   END AS PhysiotherapistFlag
	,CASE 
    WHEN SpecialtyCode = '71' THEN 'Y'
    WHEN Taxonomy IN (
      '133N00000X',
      '133NN1002X',
      '136A00000X'
    ) THEN 'Y' 
    ELSE 'N' 
   END AS NutritionistFlag
	,CASE WHEN SpecialtyCode = '46' THEN 'Y' ELSE 'N' END AS Endocrinologist
	,CASE WHEN SpecialtyCode = '34' THEN 'Y' ELSE 'N' END AS Urologist
	,CASE WHEN SpecialtyCode IN ('06','21','C3','C4') THEN 'Y' ELSE 'N' END AS Cardiologist
	,CASE 
    WHEN SpecialtyCode IN ('45','74','92','94','95') THEN 'Y'
    WHEN Taxonomy IN (
    '2085B0100X',
    '2085R0203X'
    ) THEN 'Y'
    ELSE 'N' 
   END AS Radiologist
	,CASE WHEN SpecialtyCode IN ('83','89','90','91') THEN 'Y' ELSE 'N' END AS Oncologist
	,CASE WHEN SpecialtyCode IN ('09','72') THEN 'Y' ELSE 'N' END AS PainSpecialist
	,CASE WHEN SpecialtyCode = '47' THEN 'Y' ELSE 'N' END AS MedicalLabTechnician
	,CASE WHEN SpecialtyCode = '69' THEN 'Y' ELSE 'N' END AS ClinicalLabTechnician
	,src.ProviderNPI
	,Taxonomy AS AdditionalColumn1
	,SpecialtyCode AS AdditionalColumn2
	,'' AS AdditionalColumn3
	,'' AS AdditionalColumn4
	,'' AS AdditionalColumn5
	,'' AS Filler
	,current_timestamp() AS LoadDateTime
	,InNetworkFlag
  ,FirstName
  ,LastName
  ,LocationID
  ,LocationName
  ,LocationType
  ,ServiceLocation
  ,Address1
  ,Address2
  ,City
  ,State
  ,Zip
  ,Country
  ,AddressType
  ,Phone1
  ,Phone2
  ,Fax
  ,Email
  ,TIN
  ,ProviderGroupName
  ,ProviderType
  ,Case WHEN '{ClientCodeLower}' IN ('bcbsne','qaidap1','devidap1') then coalesce(LKPID.DEA,LKPNPI.DEA) ELSE NULL END as DEA
 FROM Q360ProviderLookup SRC
 LEFT JOIN ProvIDDEAData LKPID ON REPLACE(SRC.PROVIDERID,'NPI-','')=LKPID.PROVIDERID
 LEFT JOIN ProvNPIDEAData LKPNPI ON REPLACE(SRC.PROVIDERID,'NPI-','')=LKPNPI.ProviderNPI
 )
 SELECT
   ProviderID
	,PCPFlag
	,OBGYNFlag
	,MHProviderFlag
	,EyeCareProviderFlag
	,DentistFlag
	,NephrologistFlag
	,AnesthesiologistFlag
	,NPRProviderFlag
	,PASProviderFlag
	,ProviderPrescribingPrivilegesFlag
	,ClinicalPharmacistFlag
	,HospitalFlag
	,SNFFlag
	,SurgeonFlag
	,RegisteredNurseFlag
	,PediatricianFlag
	,DiabetologistFlag
	,DieticianFlag
	,PhysiotherapistFlag
	,NutritionistFlag
	,Endocrinologist
	,Urologist
	,Cardiologist
	,Radiologist
	,Oncologist
	,PainSpecialist
	,MedicalLabTechnician
	,ClinicalLabTechnician
	,ProviderNPI
	,AdditionalColumn1
	,AdditionalColumn2
	,AdditionalColumn3
	,AdditionalColumn4
	,AdditionalColumn5
	,Filler
	,LoadDateTime
	,InNetworkFlag
  ,FirstName
  ,LastName
  ,LocationID
  ,LocationName
  ,LocationType
  ,ServiceLocation
  ,Address1
  ,Address2
  ,City
  ,State
  ,Zip
  ,Country
  ,AddressType
  ,Phone1
  ,Phone2
  ,Fax
  ,Email
  ,TIN
  ,ProviderGroupName
  ,ProviderType
  ,DEA
 FROM FINAL
"""
  print("Running main sql query")
  dfData = spark.sql(tempSQLScript)
  dfData.createOrReplaceTempView("tempSQLScript")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Delete Statement
def RunDeleteSQLQuery():
  DeleteSQLQuery="""
DELETE FROM Q360Provider
"""
  print("Running delete sql query")
  dfData = spark.sql(DeleteSQLQuery)
  dfData.createOrReplaceTempView("DeleteSQLQuery")
  
  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Dupes Check
def RunDupCheck():
  print("Checking duplicates")
  checkVar = 0
  dupSQLScript="""
SELECT COUNT(1)
FROM (
  SELECT 
    ProviderID
  FROM tempSQLScript
  GROUP BY
    ProviderID
  HAVING COUNT(1) > 1
  ) a
"""

  checkVar = spark.sql(dupSQLScript).first()[0]
  
  print(f"Duplicates found: {str(checkVar)}")
  if(checkVar > 1):
    raise Exception('Duplicates Detected from BusinessKey')

  return "SUCCESS"

# COMMAND ----------

# DBTITLE 1,Merge Statement
def Merge(): 
  print("Running merge script")
  mergeSQL = """
MERGE INTO Q360Provider t 
USING (
	SELECT
	 ProviderID
	,PCPFlag
	,OBGYNFlag
	,MHProviderFlag
	,EyeCareProviderFlag
	,DentistFlag
	,NephrologistFlag
	,AnesthesiologistFlag
	,NPRProviderFlag
	,PASProviderFlag
	,ProviderPrescribingPrivilegesFlag
	,ClinicalPharmacistFlag
	,HospitalFlag
	,SNFFlag
	,SurgeonFlag
	,RegisteredNurseFlag
	,PediatricianFlag
	,DiabetologistFlag
	,DieticianFlag
	,PhysiotherapistFlag
	,NutritionistFlag
	,Endocrinologist
	,Urologist
	,Cardiologist
	,Radiologist
	,Oncologist
	,PainSpecialist
	,MedicalLabTechnician
	,ClinicalLabTechnician
	,ProviderNPI
	,AdditionalColumn1
	,AdditionalColumn2
	,AdditionalColumn3
	,AdditionalColumn4
	,AdditionalColumn5
	,Filler
	,LoadDateTime
	,InNetworkFlag
  ,FirstName
  ,LastName
  ,LocationID
  ,LocationName
  ,LocationType
  ,ServiceLocation
  ,Address1
  ,Address2
  ,City
  ,State
  ,Zip
  ,Country
  ,AddressType
  ,Phone1
  ,Phone2
  ,Fax
  ,Email
  ,TIN
  ,ProviderGroupName
  ,ProviderType
  ,DEA
 FROM tempSQLScript
) s
on t.ProviderID=s.ProviderID
WHEN NOT MATCHED THEN 
INSERT (
	 ProviderID
	,PCPFlag
	,OBGYNFlag
	,MHProviderFlag
	,EyeCareProviderFlag
	,DentistFlag
	,NephrologistFlag
	,AnesthesiologistFlag
	,NPRProviderFlag
	,PASProviderFlag
	,ProviderPrescribingPrivilegesFlag
	,ClinicalPharmacistFlag
	,HospitalFlag
	,SNFFlag
	,SurgeonFlag
	,RegisteredNurseFlag
	,PediatricianFlag
	,DiabetologistFlag
	,DieticianFlag
	,PhysiotherapistFlag
	,NutritionistFlag
	,Endocrinologist
	,Urologist
	,Cardiologist
	,Radiologist
	,Oncologist
	,PainSpecialist
	,MedicalLabTechnician
	,ClinicalLabTechnician
	,ProviderNPI
	,AdditionalColumn1
	,AdditionalColumn2
	,AdditionalColumn3
	,AdditionalColumn4
	,AdditionalColumn5
	,Filler
	,LoadDateTime
	,InNetworkFlag
  ,FirstName
  ,LastName
  ,LocationID
  ,LocationName
  ,LocationType
  ,ServiceLocation
  ,Address1
  ,Address2
  ,City
  ,State
  ,Zip
  ,Country
  ,AddressType
  ,Phone1
  ,Phone2
  ,Fax
  ,Email
  ,TIN
  ,ProviderGroupName
  ,ProviderType
  ,DEA
) 
VALUES (
	 s.ProviderID
	,s.PCPFlag
	,s.OBGYNFlag
	,s.MHProviderFlag
	,s.EyeCareProviderFlag
	,s.DentistFlag
	,s.NephrologistFlag
	,s.AnesthesiologistFlag
	,s.NPRProviderFlag
	,s.PASProviderFlag
	,s.ProviderPrescribingPrivilegesFlag
	,s.ClinicalPharmacistFlag
	,s.HospitalFlag
	,s.SNFFlag
	,s.SurgeonFlag
	,s.RegisteredNurseFlag
	,s.PediatricianFlag
	,s.DiabetologistFlag
	,s.DieticianFlag
	,s.PhysiotherapistFlag
	,s.NutritionistFlag
	,s.Endocrinologist
	,s.Urologist
	,s.Cardiologist
	,s.Radiologist
	,s.Oncologist
	,s.PainSpecialist
	,s.MedicalLabTechnician
	,s.ClinicalLabTechnician
	,s.ProviderNPI
	,s.AdditionalColumn1
	,s.AdditionalColumn2
	,s.AdditionalColumn3
	,s.AdditionalColumn4
	,s.AdditionalColumn5
	,s.Filler
	,s.LoadDateTime
	,s.InNetworkFlag
  ,s.FirstName
  ,s.LastName
  ,s.LocationID
  ,s.LocationName
  ,s.LocationType
  ,s.ServiceLocation
  ,s.Address1
  ,s.Address2
  ,s.City
  ,s.State
  ,s.Zip
  ,s.Country
  ,s.AddressType
  ,s.Phone1
  ,s.Phone2
  ,s.Fax
  ,s.Email
  ,s.TIN
  ,s.ProviderGroupName
  ,s.ProviderType
  ,s.DEA
)
"""

  spark.sql(mergeSQL)
  return "SUCCESS"

# COMMAND ----------

def RunQ360Provider(ClientCode):
  #mount destination
  mountDestination()
  #mount source
  mountSource()
  #mount lookup
  mountLookUp()
  #Execute tempSQLScript -- creates a tempView called tempSQLScript
  RunTempSQLScript()
  #run delete script -- deletes the existing yearmonth based on condition
  RunDeleteSQLQuery()
  #dupes check
  RunDupCheck()
  #run merge
  Merge()
  return "SUCCESS"


# COMMAND ----------

returnStr = ""
try:
  RunQ360Provider(ClientCode) 
  returnStr = "SUCCESS"
except Exception as e:
  returnStr += repr(e)
  returnStr = "FAILURE"
finally:
  dbutils.notebook.exit(returnStr)
