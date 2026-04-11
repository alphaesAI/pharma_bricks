# Databricks notebook source
# DBTITLE 1,Setup variables and mount point
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","") #this is needed but not used in this notebook.  The need comes from the parent notebook

clientCode = dbutils.widgets.get("ClientContainer")
#bcbsks / devidap1Alert

#datalake mount point
mntPnt = '/mnt/'

# COMMAND ----------

# DBTITLE 1,Setup table configs
tableConfig = """
{
  "DestinationTableName": "MemberRevenueGap",
  "DestinationTablePath": "#clientCode/Gold/MA/PEC/MemberRevenueGap",
  "SourceTables": [
    {
      "TableName": "RevenueGapParameters",
      "TablePath": "global/consolidated/MA/Data/RevenueGapParameters",
      "TableFormat": "delta"
    },
    {
      "TableName": "PotentialHCC",
      "TablePath": "#clientCode/OperationalData/RAQ/AlertDB/dbo/PotentialHCC",
      "TableFormat": "parquet"
    },
    {
      "TableName": "CDIAlertEntity",
      "TablePath": "#clientCode/OperationalData/RAQ/TepAlert/dbo/CDIAlertEntity",
      "TableFormat": "parquet"
    },
    {
      "TableName": "CDIAlertEntityDetail",
      "TablePath": "#clientCode/OperationalData/RAQ/TepAlert/dbo/CDIAlertEntityDetail",
      "TableFormat": "parquet"
    },
    {
      "TableName": "CDIAlertWorkflowResponse",
      "TablePath": "#clientCode/OperationalData/RAQ/TepAlert/dbo/CDIAlertWorkflowResponse",
      "TableFormat": "parquet"
    },
    {
      "TableName": "Alert",
      "TablePath": "#clientCode/OperationalData/RAQ/AlertDB/dbo/Alert",
      "TableFormat": "parquet"
    },
    {
      "TableName": "MemberMaster",
      "TablePath": "#clientCode/OperationalData/RAQ/MerlinRA7/dbo/tblMemberMaster",
      "TableFormat": "parquet"
    },
    {
      "TableName": "tblCMSAdjustmentsV7",
      "TablePath": "#clientCode/OperationalData/RAQ/MerlinRA7/dbo/tblCMSAdjustmentsV7",
      "TableFormat": "parquet"
    },
    {
      "TableName": "tblProviderSpecialtyDetail",
      "TablePath": "#clientCode/OperationalData/RAQ/MerlinRA7/dbo/tblProviderSpecialtyDetail",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ProviderSpecialtyDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ProviderSpecialtyDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "tblProviderMaster",
      "TablePath": "#clientCode/OperationalData/RAQ/MerlinRA7/dbo/tblProviderMaster",
      "TableFormat": "parquet"
    },
    {
      "TableName": "DetailGroup",
      "TablePath": "#clientCode/OperationalData/RAQ/TepAlert/cdi/DetailGroup",
      "TableFormat": "parquet"
    },
    {
      "TableName": "HCCDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/HCCDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "AlertResponseOption",
      "TablePath": "global/OperationalData/RAQ/AlertReference/dbo/AlertResponseOption",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ICDDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ICDDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "ICDEffectiveYear",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/ICDEffectiveYear",
      "TableFormat": "parquet"
    },
    {
      "TableName": "HCCICDDatasetXref",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/HCCICDDatasetXref",
      "TableFormat": "parquet"
    },
    {
      "TableName": "HCCDataset",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/HCCDataset",
      "TableFormat": "parquet"
    },
    {
      "TableName": "HCCEffectiveYear",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/HCCEffectiveYear",
      "TableFormat": "parquet"
    },
    {
      "TableName": "HCCHierarchy",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/HCCHierarchy",
      "TableFormat": "parquet"
    },
    {
      "TableName": "CMSModelEffectiveDate",
      "TablePath": "global/OperationalData/RAQ/TepReference/dbo/CMSModelEffectiveDate",
      "TableFormat": "parquet"
    },    
    {
      "TableName": "RollUpParameters",
      "TablePath": "global/consolidated/MA/Data/RollUpParameters",
      "TableFormat": "delta"
    },
    {
      "TableName": "MAO004",
      "TablePath": "#clientCode/consolidated/MA/Data/MAO004",
      "TableFormat": "delta"
    },
    {
      "TableName": "Raps",
      "TablePath": "#clientCode/consolidated/MA/Data/RAPSReturn",
      "TableFormat": "delta"
    },
    {
      "TableName": "MemberPersonBridge",
      "TablePath": "#clientCode/Gold/MA/Client/MemberPersonBridge",
      "TableFormat": "delta"
    },
    {
      "TableName": "ReportBase",
      "TablePath": "#clientCode/Gold/MA/PEC/pecReportBase",
      "TableFormat": "delta"
    },
    {
      "TableName": "MemberRoster",
      "TablePath": "#clientCode/Gold/MA/Client/memberroster",
      "TableFormat": "delta"
    },
    {
      "TableName": "GoldenClaim",
      "TablePath": "#clientCode/Gold/MA/Client/GoldenClaim",
      "TableFormat": "delta"
    },
      {
      "TableName": "MedicalGoldenClaimDiagnosis",
      "TablePath": "#clientCode/Gold/MA/Client/MedicalGoldenClaimDiagnosis",
      "TableFormat": "delta"
    },
    {
      "TableName": "MedicalClaimHeader",
      "TablePath": "#clientCode/consolidated/MA/Data/MedicalClaimHeader",
      "TableFormat": "delta"
    },
    {
      "TableName": "MedicalClaimLine",
      "TablePath": "#clientCode/consolidated/MA/Data/MedicalClaimLine",
      "TableFormat": "delta"
    }
  ]
}
"""

# COMMAND ----------

# DBTITLE 1,Method: pathExists
def pathExists(pathToCheck): 
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists 

# COMMAND ----------

# DBTITLE 1,Create TempView if exists
def LoadAndCreateTempView(path, format, tablename, clientCode, mntPnt):
  UpdatedPath = mntPnt + path.replace("#clientCode",clientCode)
   
  if(pathExists(UpdatedPath)):
    dfFile = spark.read.format(format).option("header","true").load(UpdatedPath)
    dfFile.createOrReplaceTempView(tablename)
    print("TempViewCreated: " + tablename)
    return 0
  else:
    print("TempViewNotCreated because path does not exist: "  + f"{UpdatedPath}/{tablename}")
    return 1

# COMMAND ----------

# DBTITLE 1,Loop tables and create views
from pyspark.sql.functions import explode, col

jsonList = []
jsonList.append(tableConfig)
df = spark.read.json(sc.parallelize(jsonList))
df.createOrReplaceTempView("tables")

numIssues = 0
for destTable in df.collect():
  DestinationTableName = destTable["DestinationTableName"]
  DestinationTablePath = destTable["DestinationTablePath"]
  numIssues += LoadAndCreateTempView(DestinationTablePath, 'delta', DestinationTableName, clientCode, mntPnt)

dfSourceTables = df.select(explode("SourceTables").alias("SourceTables")) \
                   .select("SourceTables.TableFormat", "SourceTables.TableName", "SourceTables.TablePath")

for sourceTable in dfSourceTables.collect():
  TableFormat = sourceTable["TableFormat"]
  TableName = sourceTable["TableName"]
  TablePath = sourceTable["TablePath"]
  LoadAndCreateTempView(TablePath, TableFormat, TableName, clientCode, mntPnt)

dfSourceTables.createOrReplaceTempView("sourcetables")

if(numIssues >= 1):
  raise Exception("All tables are not available");

# COMMAND ----------

# %sql
# SELECT * 
# FROM sourcetables

# COMMAND ----------

def CurrentPrintedDiagsFinalAfterSeptember(HCCVersionRAPS, HCCVersionEDPS, programyear):
  #MaxAlertDate should already exists in 2022 because its run prior to this
  maxAlertDateQuery = """SELECT MAX(AlertDate) AS MaxAlertDate
  FROM Alert
  WHERE  
  YEAR(AlertDate) = '{program_year}'
  AND 
  MONTH(AlertDate) <= 9
  """
  
  maxAlertDateQuery = maxAlertDateQuery.format(program_year = programyear)
  MaxAlertDate = spark.sql(maxAlertDateQuery).first()[0]
  

  CurrentPrintedDiagsFinalQuery = """
  WITH CurrentPrintedDiags AS(
	SELECT 
       cae.AlertID
      ,adb.AlertDate
      ,tmm.MemberID
      ,caed.RecordType
      ,caed.StarOrDiagnosisCode AS DiagnosisCode
      ,ph.HCC
      ,hcc.HCCversion
      ,MAX(aro.AlertResponseType) AS AlertResponseType
      ,MIN(dg.DetailGroupCode) AS AlertCategory
	FROM CDIAlertEntity cae
	INNER JOIN Alert adb
	  ON cae.AlertID = adb.AlertID
	  AND adb.AlertDate = '{Max_Alert_Date}'
	LEFT JOIN CDIAlertEntityDetail caed
	  ON caed.CDIAlertEntityID = cae.CDIAlertEntityID
	LEFT JOIN MemberMaster tmm
	  ON cae.MemberMasterID = tmm.MemberMaster_WK
	LEFT JOIN PotentialHCC ph
	  ON ph.RecordID = caed.RecordID
	LEFT JOIN HCCDataset hcc
	  ON ph.HCC = hcc.HCCNumber
	  AND caed.AlertLineText = hcc.HCCDescription
	  AND hcc.HCCVersion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
	LEFT JOIN CDIAlertWorkflowResponse wfr
	  ON wfr.CDIAlertEntityDetailID = caed.CDIAlertEntityDetailID
	LEFT JOIN AlertResponseOption aro
	  ON aro.AlertResponseOptionID = wfr.AlertResponseOptionID
	LEFT JOIN DetailGroup dg
	  ON dg.DetailGroupID = caed.AlertGroupID
	WHERE
      caed.AlertGroupID <> 3
	GROUP BY 
       cae.AlertID
      ,adb.AlertDate
      ,tmm.MemberID
      ,caed.RecordType
      ,caed.StarOrDiagnosisCode
      ,ph.HCC
      ,hcc.HCCversion
   ),
   CurrentPrintedDiagsTwo AS(
	SELECT DISTINCT
		    pd.AlertID
		   ,pd.AlertDate
		   ,pd.MemberID
		   ,pd.RecordType
		   ,pd.DiagnosisCode
		   ,CASE WHEN pd.HCC IS NULL
					  AND hcc.HCCNumber IS NULL
					  AND (pd.DiagnosisCode LIKE 'E112%'
						   OR pd.DiagnosisCode LIKE 'E113%'
						   OR pd.DiagnosisCode LIKE 'E114%'
						   OR pd.DiagnosisCode LIKE 'E115%'
						   OR pd.DiagnosisCode LIKE 'E116%'
						   )
				 THEN 18
			 ELSE COALESCE(hcc.HCCNumber, pd.HCC)
			 END AS HCC
		   ,COALESCE(hcc.HCCVersion, pd.HCCVersion) AS HCCVersion
		   ,pd.AlertResponseType
		   ,pd.AlertCategory 
	FROM CurrentPrintedDiags pd
          LEFT JOIN ICDHCCTepRef hcc 
            ON pd.DiagnosisCode = hcc.ICD
            AND pd.RecordType = 'Diag'
            AND hcc.HCCVersion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
            AND pd.AlertDate >= hcc.EffectiveDateStart
            AND pd.AlertDate < hcc.EffectiveDateEnd
   ),
   CurrentPrintedDiagsThree AS(
   SELECT 
   		    AlertID
		   ,AlertDate
		   ,MemberID
		   ,RecordType
		   ,DiagnosisCode
		   ,HCC
		   ,HCCVersion
		   ,AlertResponseType
		   ,AlertCategory 
   FROM CurrentPrintedDiagsTwo
   WHERE 
   HCC IS NOT NULL
   )
   SELECT 
		    AlertID
		   ,AlertDate
		   ,MemberID
		   ,RecordType
		   ,DiagnosisCode
		   ,HCC
		   ,HCCVersion
		   ,AlertResponseType
		   ,AlertCategory 
   FROM CurrentPrintedDiags
  """
  
  CurrentPrintedDiagsFinalQuery = CurrentPrintedDiagsFinalQuery.format( \
        Max_Alert_Date = MaxAlertDate,\
        HCC_VersionRAPS = HCCVersionRAPS,\
        HCC_VersionEDPS = HCCVersionEDPS,\
        )

  return CurrentPrintedDiagsFinalQuery

# COMMAND ----------

def BasePrintedDiags(startingGapBegin, startingGapEnd, programyear, HCCVersionRAPS, HCCVersionEDPS):
  printedDiagsQuery = """
  WITH PrintedDiagsZero AS(
      SELECT 
            cae.AlertID
           ,adb0.AlertDate
           ,tmm.MemberID
           ,caed.RecordType
           ,caed.StarOrDiagnosisCode AS DiagnosisCode
           ,ph.HCC
           ,hcc.HCCversion
           ,MAX(aro.AlertResponseType) AS AlertResponseType
           ,MIN(dg.DetailGroupCode) AS AlertCategory
           ,CASE WHEN adb.AlertID IS NULL THEN 0 ELSE 1 END AS LockDownFlag
    FROM CDIAlertEntity cae
          INNER JOIN Alert adb0
            ON cae.AlertID = adb0.AlertID
            AND YEAR(adb0.AlertDate) = '{program_year}' --commenting this out for a minute :)
          LEFT JOIN Alert adb
            ON cae.AlertID = adb.AlertID
            AND adb.AlertDate >= '{starting_gap_begin}'
            AND adb.AlertDate <= '{starting_gap_end}'
          LEFT JOIN CDIAlertEntityDetail caed
            ON caed.CDIAlertEntityID = cae.CDIAlertEntityID
          LEFT JOIN MemberMaster tmm
            ON cae.MemberMasterID = tmm.MemberMaster_WK
          LEFT JOIN PotentialHCC ph
            ON ph.RecordID = caed.RecordID
          LEFT JOIN HCCDataset hcc
            ON ph.HCC = hcc.HCCNumber
            AND caed.AlertLineText = hcc.HCCDescription
            AND hcc.HCCVersion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
          LEFT JOIN CDIAlertWorkflowResponse wfr
            ON wfr.CDIAlertEntityDetailID = caed.CDIAlertEntityDetailID
          LEFT JOIN AlertResponseOption aro
            ON aro.AlertResponseOptionID = wfr.AlertResponseOptionID
          LEFT JOIN DetailGroup dg
            ON dg.DetailGroupID = caed.AlertGroupID
    WHERE
      caed.AlertGroupID <> 3
    GROUP BY 
       cae.AlertID
      ,adb0.AlertDate
      ,tmm.MemberID
      ,caed.RecordType
      ,caed.StarOrDiagnosisCode
      ,ph.HCC
      ,hcc.HCCversion
      ,CASE WHEN adb.AlertID IS NULL THEN 0 ELSE 1 END 
    ),
    FinalResponsesDiag AS(
      SELECT 
         MemberID
        ,RecordType
        ,DiagnosisCode
        ,MAX(AlertResponseType) AS AlertResponseType
        ,MIN(AlertCategory) AS AlertCategory
      FROM PrintedDiagsZero 
      WHERE 
        RecordType = 'Diag'
      GROUP BY 
         MemberID
        ,RecordType
        ,DiagnosisCode
    ),
    PrintedDiagsOne AS(
    SELECT 
            pd.AlertID
           ,pd.AlertDate
           ,pd.MemberID
           ,pd.RecordType
           ,pd.DiagnosisCode
           ,pd.HCC
           ,pd.HCCversion
           ,COALESCE(frd.AlertResponseType,pd.AlertResponseType) AS AlertResponseType
           ,COALESCE(frd.AlertCategory,pd.AlertCategory) AS AlertCategory
           ,pd.LockDownFlag
    FROM PrintedDiagsZero pd
        LEFT JOIN FinalResponsesDiag frd
          ON pd.MemberID = frd.MemberID
            AND pd.RecordType = frd.RecordType
            AND pd.DiagnosisCode = frd.DiagnosisCode
    ),
    FinalResponsesHCC AS(
    SELECT 
       MemberID
      ,RecordType
      ,HCC
      ,MAX(AlertResponseType) AS AlertResponseType
      ,MIN(AlertCategory) AS AlertCategory
    FROM PrintedDiagsOne
    WHERE 
      RecordType = 'HCC'
    GROUP BY 
       MemberID
      ,RecordType
      ,HCC
    ),
    PrintedDiagTwo AS(
    SELECT 
            pdo.AlertID
           ,pdo.AlertDate
           ,pdo.MemberID
           ,pdo.RecordType
           ,pdo.DiagnosisCode
           ,pdo.HCC
           ,pdo.HCCversion
           ,COALESCE(frc.AlertResponseType,pdo.AlertResponseType) AS AlertResponseType
           ,COALESCE(frc.AlertCategory,pdo.AlertCategory) AS AlertCategory
           ,pdo.LockDownFlag
    FROM PrintedDiagsOne pdo
      LEFT JOIN FinalResponsesHCC frc
        ON pdo.MemberID = frc.MemberID
        AND pdo.RecordType = frc.RecordType
        AND pdo.HCC = frc.HCC
    )
    SELECT 
            AlertID
           ,AlertDate
           ,MemberID
           ,RecordType
           ,DiagnosisCode
           ,HCC
           ,HCCversion
           ,AlertResponseType
           ,AlertCategory
           ,LockDownFlag
    FROM PrintedDiagTwo
    WHERE
    LockDownFlag = 1
    """

  printedDiagsQuery = printedDiagsQuery.format( \
        program_year = programyear,\
        starting_gap_begin  = startingGapBegin,\
        starting_gap_end = startingGapEnd,\
        HCC_VersionRAPS = HCCVersionRAPS,\
        HCC_VersionEDPS = HCCVersionEDPS,\
        )
  
  PrintedDiagsDF = spark.sql(printedDiagsQuery)
  
  PrintedDiagsDF.createOrReplaceTempView("PrintedDiags")
  
  #create final printed diag query before doing curent printed diag logic
  BasePrintedDiagsQuery = """
        WITH PrintedDiagsTwo AS(
        SELECT DISTINCT
                pd.AlertID
               ,pd.AlertDate
               ,pd.MemberID
               ,pd.RecordType
               ,pd.DiagnosisCode
               ,CASE WHEN pd.HCC IS NULL
                          AND hcc.HCCNumber IS NULL
                          AND (pd.DiagnosisCode LIKE 'E112%'
                               OR pd.DiagnosisCode LIKE 'E113%'
                               OR pd.DiagnosisCode LIKE 'E114%'
                               OR pd.DiagnosisCode LIKE 'E115%'
                               OR pd.DiagnosisCode LIKE 'E116%'
                               )
                     THEN 18
                 ELSE COALESCE(hcc.HCCNumber, pd.HCC)
                 END AS HCC
               ,COALESCE(hcc.HCCVersion, pd.HCCVersion) AS HCCVersion
               ,pd.AlertResponseType
               ,pd.AlertCategory
        FROM PrintedDiags pd 
          LEFT JOIN ICDHCCTepRef hcc 
            ON pd.DiagnosisCode = hcc.ICD
            AND pd.RecordType = 'Diag'
            AND hcc.HCCVersion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
            AND pd.AlertDate >= hcc.EffectiveDateStart
            AND pd.AlertDate < hcc.EffectiveDateEnd
        )
        SELECT
                AlertID
               ,AlertDate
               ,MemberID
               ,RecordType
               ,DiagnosisCode
               ,HCC
               ,CASE WHEN HCCVersion IS NULL THEN '{HCC_VersionEDPS}' ELSE HCCVersion END AS HCCVersion
               ,AlertResponseType
               ,AlertCategory
        FROM PrintedDiagsTwo
        WHERE 
        HCC IS NOT NULL
  """
  
  BasePrintedDiagsQuery = BasePrintedDiagsQuery.format( \
        HCC_VersionRAPS = HCCVersionRAPS,\
        HCC_VersionEDPS = HCCVersionEDPS,\
        )
  
  BasePrintedDiagsDF = spark.sql(BasePrintedDiagsQuery)
  BasePrintedDiagsDF.createOrReplaceTempView("BasePrintedDiags")
  
  return ""

# COMMAND ----------

def HCCClosuresHierarchy(startingGapBegin, startingGapEnd, programyear, HCCVersionRAPS, HCCVersionEDPS):
  StartingGapsAndCDIResponsesQuery = """
  SELECT 
     MemberID
    ,MAX(RecordType) AS RecordType
    ,DiagnosisCode
    ,HCC
    ,HCCVersion
    ,MAX(AlertResponseType) AS AlertResponseType
    ,CASE 
        WHEN MAX(AlertResponseType) = 'Pos' THEN 1 
        ELSE 0 
     END AS YesResponse
    ,CASE 
        WHEN max(AlertResponseType) = 'Neg' THEN 1
        ELSE 0
     END AS NoResponse
    ,MIN(AlertCategory) AS AlertCategory
  FROM BasePrintedDiags
  WHERE
  HCCVersion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
  GROUP BY 
     MemberID
    ,DiagnosisCode
    ,HCC
    ,HCCVersion
    """

  StartingGapsAndCDIResponsesQuery = StartingGapsAndCDIResponsesQuery.format( \
        HCC_VersionRAPS = HCCVersionRAPS,\
        HCC_VersionEDPS = HCCVersionEDPS,\
        )
  
  StartingGapsAndCDIResponsesDF = spark.sql(StartingGapsAndCDIResponsesQuery)
  
  StartingGapsAndCDIResponsesDF.createOrReplaceTempView("StartingGapsAndCDIResponses") 
  
  
  #Get Raps
  HCCRapsQuery = """
      WITH HCCRAPS AS(
      SELECT DISTINCT 
         tmm.PlanMemberId
        ,a.ICD9 AS DiagnosisCode
        ,to_date(a.ThruDate) AS DOS
        ,h.HCCNumber AS HCC
        ,h.HCCVersion AS HCCVersion
      FROM RapsDiagnosis a 
        LEFT JOIN BenMemberId tmm 
          on a.BeneficiaryID = tmm.BeneficiaryId
        LEFT JOIN ICDHCCTepRef h 
          ON a.ICD9 = h.ICD 
          AND a.ThruDate >= h.EffectiveDateStart
          AND a.ThruDate < h.EffectiveDateEnd
          AND h.HCCVersion IN ('{HCC_VersionRAPS}')
      WHERE 
      year(a.ThruDate) = '{program_year}'
      AND 
      h.HCCNumber IS NOT NULL
      )
      SELECT 
         PlanMemberId AS MemberID
        ,DiagnosisCode
        ,MIN(DOS) AS DOS
        ,HCC
        ,HCCVersion
      FROM HCCRAPS
      GROUP BY 
         PlanMemberId
        ,DiagnosisCode
        ,HCC
        ,HCCVersion
    """

  HCCRapsQuery = HCCRapsQuery.format( \
        HCC_VersionRAPS = HCCVersionRAPS,\
        program_year = programyear,\
        )
  
  HCCRapsDF = spark.sql(HCCRapsQuery)
  
  HCCRapsDF.createOrReplaceTempView("HCCRaps") 
  
  #Get MAO004
  MAO004Query = """
      SELECT DISTINCT 
         tmm.PlanMemberID AS MemberID
        ,a.DiagnosisCode
        ,MIN(a.ThroughDateOfService) AS DOS
        ,c.HCCNumber AS HCC
        ,c.HCCVersion 
      FROM MAO004Diagnosis a
        INNER JOIN ICDHCCTepRef c
          ON a.DiagnosisCode = c.ICD
          AND CAST(a.ThroughDateOfService AS date) >= c.EffectiveDateStart
          AND CAST(a.ThroughDateOfService AS date) < c.EffectiveDateEnd
          AND c.HCCVersion IN ('{HCC_VersionEDPS}')
        LEFT JOIN BenMemberId tmm 
          ON a.BeneficiaryID = tmm.BeneficiaryId 
      WHERE 
      YEAR(a.ThroughDateOfService) = '{program_year}'
      GROUP BY 
         tmm.PlanMemberID
        ,a.DiagnosisCode
        ,c.HCCNumber
        ,c.HCCVersion
    """

  MAO004Query = MAO004Query.format( \
        HCC_VersionEDPS = HCCVersionEDPS,\
        program_year = programyear,\
        )
  
  MAO004DF = spark.sql(MAO004Query)
  
  MAO004DF.createOrReplaceTempView("MAO004DetailDiagnosis")
    

  #Get HCCClosuresHierarchy
  HCCClosuresHierarchyQuery = """
      WITH StartingGapsResponsesAndReturns AS(
      SELECT DISTINCT
         a.MemberID
        ,a.RecordType
        ,a.DiagnosisCode
        ,a.HCC
        ,a.HCCVersion
        ,a.AlertResponseType
        ,a.YesResponse
        ,a.NoResponse
        ,a.AlertCategory        
        ,CASE 
          WHEN b.DiagnosisCode IS NOT NULL THEN 1
          WHEN d.HCC IS NOT NULL THEN 1 
          ELSE 0
         END AS InRAPS
        ,CASE 
          WHEN c.DiagnosisCode IS NOT NULL THEN 1
          WHEN e.HCC IS NOT NULL THEN 1 
          ELSE 0
         END AS InMAO004
      FROM StartingGapsAndCDIResponses a
        LEFT JOIN HCCRAPS b
          ON a.MemberID = b.MemberID
          AND a.DiagnosisCode = b.DiagnosisCode
        LEFT JOIN MAO004DetailDiagnosis c
          ON a.MemberID = c.MemberID
          AND a.DiagnosisCode = c.DiagnosisCode
        LEFT JOIN HCCRAPS d
          ON a.MemberID = d.MemberID
          AND a.HCC = d.HCC
          AND a.HCCVersion = '{HCC_VersionRAPS}'
        LEFT JOIN MAO004DetailDiagnosis e
          ON a.MemberID = e.MemberID
          AND a.HCC = e.HCC
          AND a.HCCVersion = '{HCC_VersionEDPS}'
      ), 
      HCCStartingGapsResponsesAndReturns AS(
      SELECT 
         MemberID
        ,'HCC' AS RecordType
        ,HCC
        ,concat_ws('; ',collect_set(HCCVersion)) AS HCCVersions		
        ,MAX(YesResponse) AS YesResponse
        ,MIN(NoResponse) AS NoResponse
        ,MAX(InRAPS) AS InRAPS
        ,MAX(InMAO004) AS InMAO004
        ,MIN(AlertCategory) AS AlertCategory
        ,concat_ws('; ',collect_set(DiagnosisCode)) AS Diags 
      FROM StartingGapsResponsesAndReturns s
      GROUP BY 
         MemberID
        ,HCC
      ),
      HCCClosures AS(
      SELECT 
         MemberID
        ,RecordType
        ,HCC
        ,HCCVersions
        ,AlertCategory
        ,CASE 
          WHEN (YesResponse + NoResponse + InRAPS + InMAO004) > 0	THEN 1
          ELSE 0
         END AS HCCClosed
        ,CASE 
          WHEN (YesResponse + InRAPS + InMAO004) > 0 THEN 1
          ELSE 0
         END AS HCCClosedPositive
        ,CASE 
          WHEN YesResponse = 1 THEN 'Yes on Alert'
          WHEN YesResponse = 0 AND InMAO004 = 1 THEN 'In MAO-004'
          WHEN YesResponse = 0 AND InMAO004 = 0 AND InRAPS = 1 THEN 'In RAPS'
          WHEN YesResponse = 0 AND InMAO004 = 0 AND InRAPS = 0 AND NoResponse = 1 THEN 'No on Alert'
          ELSE 'Open'
         END AS ClosureReason
        ,Diags
      FROM HCCStartingGapsResponsesAndReturns
      ),
      hierarchy AS(
      SELECT DISTINCT 
         s.hccnumber AS Keep_HCC
        ,s1.hccnumber AS Drop_HCC
        ,s.hccversion AS HCCVersion
      FROM HCCDataset s
        INNER JOIN HCCHierarchy h 
        on s.hccdatasetid = h.keephccdatasetid
        INNER JOIN HCCDataset s1 
          on h.drophccdatasetid = s1.hccdatasetid
      WHERE 
      s.hccversion IN ('{HCC_VersionRAPS}', '{HCC_VersionEDPS}')
      ),
      HCCClosuresHierarchy AS(
      SELECT DISTINCT
         a.MemberID
        ,a.RecordType
        ,a.HCC
        ,a.HCCVersions
        ,a.AlertCategory
        ,CASE 
          WHEN a.HCCClosedPositive = 0 AND c.MemberID IS NOT NULL THEN 1
          ELSE a.HCCClosed
         END AS HCCClosed
        ,CASE 
          WHEN a.HCCClosedPositive = 0 AND c.MemberID IS NOT NULL THEN 1
          ELSE a.HCCClosedPositive
         END AS HCCClosedPositive
        ,CASE 
          WHEN a.HCCClosedPositive = 0 AND c.MemberID IS NOT NULL THEN 'Hierarchy'
          ELSE a.ClosureReason
         END AS ClosureReason
        ,a.Diags
      FROM HCCClosures a
        LEFT JOIN hierarchy b
          ON a.HCC = b.Drop_HCC
        LEFT JOIN HCCClosures c
          ON c.HCC = b.Keep_HCC
          AND c.MemberID = a.MemberID
          AND c.HCCClosedPositive = 1
      )
      SELECT 
         MemberID
        ,RecordType
        ,HCC
        ,HCCVersions
        ,AlertCategory
        ,MAX(HCCClosed) AS HCCClosed
        ,MAX(HCCClosedPositive) AS HCCClosedPositive
        ,MIN(ClosureReason) AS ClosureReason
        ,Diags
      FROM HCCClosuresHierarchy s
      GROUP BY MemberID
             ,RecordType
             ,HCC
             ,HCCVersions
             ,AlertCategory
             ,Diags
    """

  HCCClosuresHierarchyQuery = HCCClosuresHierarchyQuery.format( \
        HCC_VersionEDPS = HCCVersionEDPS,\
        HCC_VersionRAPS = HCCVersionRAPS,\
        )
  
  HCCClosuresHierarchyDF = spark.sql(HCCClosuresHierarchyQuery)
  
  HCCClosuresHierarchyDF.createOrReplaceTempView("HCCClosuresHierarchy")

  return ""

# COMMAND ----------

def MemberPersonBridge():
  benMemIdSQLQuery = """
      WITH THIS AS(
      SELECT 
         BeneficiaryId
        ,PlanMemberId
        ,FirstName
        ,LastName
        ,DateOfBirth
        ,ROW_NUMBER() OVER(PARTITION BY BeneficiaryId ORDER BY FileID DESC, split(UniqueRecord, '-')[1] DESC ) AS IsCurrentBeneficiary
      FROM MemberPersonBridge
      WHERE
      COALESCE(PlanMemberId,'None') <> 'None' --ensure we get 7.x --7.12 will need to update
      )
      SELECT 
         BeneficiaryId
        ,PlanMemberId
        ,FirstName
        ,LastName
        ,DateOfBirth
      FROM THIS 
      WHERE
      IsCurrentBeneficiary = 1
      """
  
  BenMemberIdDF = spark.sql(benMemIdSQLQuery)
  
  BenMemberIdDF.createOrReplaceTempView("BenMemberId")

# COMMAND ----------

def RapsDiagnosis():
  RapsDiagnosisSQLQuery = """
      WITH RapsPivoted AS(
      SELECT 
        BeneficiaryID
       ,stack(10, 
               array(ThruDate1,DiagnosisCode1), 
               array(ThruDate2,DiagnosisCode2), 
               array(ThruDate3,DiagnosisCode3), 
               array(ThruDate4,DiagnosisCode4), 
               array(ThruDate5,DiagnosisCode5), 
               array(ThruDate6,DiagnosisCode6), 
               array(ThruDate7,DiagnosisCode7), 
               array(ThruDate8,DiagnosisCode8), 
               array(ThruDate9,DiagnosisCode9), 
               array(ThruDate10,DiagnosisCode10)
               ) AS Unpivotcolumns
      FROM Raps
      ),
      RapsDiagnosis AS(
      SELECT 
           BeneficiaryID
          ,Unpivotcolumns[0] AS ThruDate
          ,Unpivotcolumns[1] AS ICD9
      FROM RapsPivoted
      )
      SELECT * 
      FROM RapsDiagnosis
      WHERE
      ThruDate IS NOT NULL 
      AND
      ICD9 IS NOT NULL
      """
  RapsDiagnosisDF = spark.sql(RapsDiagnosisSQLQuery)
  
  RapsDiagnosisDF.createOrReplaceTempView("RapsDiagnosis")

# COMMAND ----------

def MAO004Diagnosis():
  MAO004DiagnosisSQLQuery = """
        WITH MAO004Pivoted AS(
        SELECT 
           ThroughDateofService
          ,BeneficiaryID 
          ,stack(38, 
                       DiagnosisCode1,DiagnosisCode2,DiagnosisCode3,DiagnosisCode4,DiagnosisCode5,DiagnosisCode6,DiagnosisCode7,DiagnosisCode8,DiagnosisCode9,DiagnosisCode10,
                       DiagnosisCode11,DiagnosisCode12,DiagnosisCode13,DiagnosisCode14,DiagnosisCode15,DiagnosisCode16,DiagnosisCode17,DiagnosisCode18,DiagnosisCode19,DiagnosisCode20,
                       DiagnosisCode21,DiagnosisCode22,DiagnosisCode23,DiagnosisCode24,DiagnosisCode25,DiagnosisCode26,DiagnosisCode27,DiagnosisCode28,DiagnosisCode29,DiagnosisCode30,
                       DiagnosisCode31,DiagnosisCode32,DiagnosisCode33,DiagnosisCode34,DiagnosisCode35,DiagnosisCode36,DiagnosisCode37,DiagnosisCode38
            ) AS DiagnosisCode
        FROM MAO004
        ),
        MAO004Diagnosis AS(
        SELECT 
           ThroughDateofService
          ,BeneficiaryID
          ,DiagnosisCode
        FROM MAO004Pivoted
        )
        SELECT * 
        FROM MAO004Diagnosis
        WHERE
        DiagnosisCode IS NOT NULL
      """
  
  MAO004DiagnosisDF = spark.sql(MAO004DiagnosisSQLQuery)
  
  MAO004DiagnosisDF.createOrReplaceTempView("MAO004Diagnosis")

# COMMAND ----------

def GoldRevenueGapsParameters():
  GoldRevenueGapsParametersSQLQuery = """ 
      WITH GoldRevenueGapParameters AS(
      SELECT 
         ClientID
        ,LoadDateTime
        ,FileID
        ,FileLayoutID
        ,FileLayoutDescription
        ,Client
        ,Market
        ,ClientMarket
        ,ConfigID
        ,LockDownMonthStart
        ,LockDownDayStart
        ,LockDownMonthEnd
        ,LockDownDayEnd
        ,NotOnCurrentAlert 
        ,DENSE_RANK() OVER(ORDER BY FileId DESC) AS LatestFileId
      FROM RevenueGapParameters 
      )
      SELECT 
         ClientID
        ,LoadDateTime
        ,FileID
        ,FileLayoutID
        ,FileLayoutDescription
        ,Client
        ,Market
        ,ClientMarket
        ,ConfigID
        ,LockDownMonthStart
        ,LockDownDayStart
        ,LockDownMonthEnd
        ,LockDownDayEnd
        ,NotOnCurrentAlert 
      FROM GoldRevenueGapParameters 
      WHERE
      LatestFileId = 1
      """
  
  GoldRevenueGapsParametersDF = spark.sql(GoldRevenueGapsParametersSQLQuery)
  
  GoldRevenueGapsParametersDF.createOrReplaceTempView("GoldRevenueGapParameters")

# COMMAND ----------

def GoldRollupParameters():
  GoldRollupParametersSQLQuery = """
    WITH GoldRollUpParameters AS(
    SELECT 
       ClientID
      ,FileID
      ,LoadDateTime
      ,FileLayoutID
      ,FileLayoutDescription
      ,Client
      ,RollUp
      ,RollUpDesc
      ,CountNAs
      ,GapAddressedOnly
      ,IsActive
      ,MonthRunDay
      ,SubClients
      ,ApptLookback
      ,LatestStatus
      ,RunStatus 
      ,DENSE_RANK() OVER(ORDER BY FileId DESC) AS LatestFileId
    FROM RollUpParameters
    )
    SELECT 
       ClientID
      ,FileID
      ,LoadDateTime
      ,FileLayoutID
      ,FileLayoutDescription
      ,Client
      ,RollUp
      ,RollUpDesc
      ,CountNAs
      ,GapAddressedOnly
      ,IsActive
      ,MonthRunDay
      ,SubClients
      ,ApptLookback
      ,LatestStatus
      ,RunStatus 
    FROM GoldRollUpParameters 
    WHERE 
    LatestFileId = 1
      """
  
  GoldRollupParametersDF = spark.sql(GoldRollupParametersSQLQuery)
  
  GoldRollupParametersDF.createOrReplaceTempView("GoldRollupParameters")

# COMMAND ----------

# DBTITLE 1,RevenueGapsDetail method
def RevenueGapsDetail(client,startingGapBegin,startingGapEnd,programyear,NotOnCurrentAlert, Market, ClientMarket):
  if(NotOnCurrentAlert is None):
    NotOnCurrentAlert = 9

  HCCVersionRAPS = 'V22'
  HCCVersionEDPS = 'V24'

  #####this is where it was ICDHCC

  ###############################################################################################################
  ##     EVERYTHING BEYOND THIS POINT IS FOR GENERATING THE CurrentPrintedDiags to make the final output
  ###############################################################################################################

  #Run Base set of data #PrintedDiags3
  BasePrintedDiags(startingGapBegin, startingGapEnd, programyear, HCCVersionRAPS, HCCVersionEDPS)

  #run HCC Closures
  HCCClosuresHierarchy(startingGapBegin, startingGapEnd, programyear, HCCVersionRAPS, HCCVersionEDPS)

  maxAlertDateQuery = f"""SELECT  MONTH(MAX(AlertDate)) AS MonthOfMaxAlertDate FROM Alert WHERE YEAR(AlertDate) = '{programyear}'"""

  if(spark.sql(maxAlertDateQuery).first()[0] is None):
    MaxAlertDate = 0
  else:
    MaxAlertDate = spark.sql(maxAlertDateQuery).first()[0]

  #If this fails its because the program year does not exist yet for the alert.
  if(MaxAlertDate > NotOnCurrentAlert):
    print("Running CurrentPrintedDiagsFinal for after Septempber")
    CurrentPrintedDiagsFinalQuery = CurrentPrintedDiagsFinalAfterSeptember(HCCVersionRAPS, HCCVersionEDPS, programyear)
  else:
    CurrentPrintedDiagsFinalQuery = """
                SELECT 
                     AlertID
                    ,AlertDate
                    ,MemberID
                    ,RecordType
                    ,DiagnosisCode
                    ,HCC
                    ,HCCVersion
                    ,AlertResponseType
                    ,AlertCategory
                FROM BasePrintedDiags
                """

  CurrentPrintedDiagsFinalDF = spark.sql(CurrentPrintedDiagsFinalQuery)
  CurrentPrintedDiagsFinalDF.createOrReplaceTempView("CurrentPrintedDiagsFinal")

  #Final Detail by Market query
  FinalDetailMarketQuery = f"""
        WITH UniqueMembersAndHCC AS(
        SELECT DISTINCT 
           MemberID
          ,HCC
        FROM CurrentPrintedDiagsFinal 
        ),
        FinalDetail AS(
        SELECT DISTINCT 
           a.MemberID
          ,a.RecordType
          ,a.HCC
          ,a.HCCVersions
          ,a.AlertCategory
          ,CASE 
            WHEN a.HCCClosed = 0 AND b.MemberID IS NULL THEN 1
            ELSE a.HCCClosed
           END AS HCCClosed
          ,a.HCCClosedPositive
          ,CASE 
            WHEN a.HCCClosed = 0 AND b.MemberID IS NULL THEN 'Not on Current Alert'
            ELSE a.ClosureReason
           END AS ClosureReason
          ,Diags
        FROM HCCClosuresHierarchy a
          LEFT JOIN UniqueMembersAndHCC b
            ON a.MemberID = b.MemberID
            AND a.HCC = b.HCC
        )
        SELECT DISTINCT
           MemberID
          ,RecordType
          ,HCC
          ,HCCVersions
          ,AlertCategory
          ,HCCClosed
          ,HCCClosedPositive
          ,ClosureReason
          ,Diags
          ,'{Market}' as Market
          ,'{ClientMarket}' as ClientMarket
        FROM FinalDetail
  """

  FinalDetailMarketDF = spark.sql(FinalDetailMarketQuery)
  FinalDetailMarketViewName = f"FinalDetail_{Market}"
  FinalDetailMarketDF.createOrReplaceTempView(FinalDetailMarketViewName)
  
  return FinalDetailMarketViewName

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

def FinalWithRankedMarkets():
  finalDetailQuery = """
          SELECT DISTINCT 
              MemberID
              ,RecordType
              ,HCC
              ,HCCVersions
              ,AlertCategory
              ,HCCClosed
              ,HCCClosedPositive
              ,ClosureReason
              ,Diags
              ,Market
              ,ClientMarket
          FROM (
                SELECT ud.*
                      ,ROW_NUMBER() OVER (PARTITION BY MemberID, HCC ORDER BY ClientMarket) AS MarketRank
                FROM UnionDetail ud
                 ) q
         WHERE MarketRank = 1
            """
  
  finalDetailQuery = spark.sql(finalDetailQuery)
  finalDetailQuery.createOrReplaceTempView("FinalDetail")

# COMMAND ----------

def ZeroOneA(clientCode, ReportPeriod, ProgramYear):
  ClientCode = clientCode.upper()

  MarketsQuery = """SELECT COUNT(DISTINCT ClientMarket)
                    FROM GoldRevenueGapParameters
                    WHERE Client = '{Client}'
                 """

  markets = spark.sql(MarketsQuery.format(Client = ClientCode)).first()[0]
  numberCounter = 1
  OriginalConfigID = 0

  marketViewList = []

  while(numberCounter <= markets):
    FinalDetailViewName = ""
    marketParametersQuery = """
            SELECT
              to_date(concat(LockDownDayStart, '-', LockDownMonthStart, '-',LEFT(concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')),4)), 'd-MMM-yyyy' ) AS starting_gap_begin	
            ,to_date(concat(LockDownDayEnd, '-', LockDownMonthEnd, '-',LEFT(concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')),4)), 'd-MMM-yyyy') AS starting_gap_end              
             ,NotOnCurrentAlert
             ,Market
             ,ClientMarket
             ,ConfigID
            FROM GoldRevenueGapParameters
            WHERE 
            Client = '{Client}'
            AND
            ClientMarket = {Counter}
                 """

    startingGapBegin = spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[0]
    startingGapEnd = spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[1]
    NotOnCurrentAlert = int(spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[2])
    Market = spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[3].replace(" ","_")
    ClientMarket = spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[4]
    ConfigId = spark.sql(marketParametersQuery.format(Client = ClientCode, Counter = numberCounter)).first()[5]

    print("Running the following market: " + Market)
    #only one where the ConfigId = 0 is the default for every client
    if(OriginalConfigID != ConfigId):
      FinalDetailViewName = RevenueGapsDetail(ClientCode,startingGapBegin,startingGapEnd,ProgramYear,NotOnCurrentAlert, Market, ClientMarket)
      print(FinalDetailViewName)
      marketViewList.append(FinalDetailViewName)

    #increment numberCounter
    numberCounter = numberCounter + 1

  #reset veiw variable to empty string
  FinalDetailViewName = ""
  #After loop run the default config for the client
  defaultMarketParametersQuery = """
            SELECT
              to_date(concat(LockDownDayStart, '-', LockDownMonthStart, '-',LEFT(concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')),4)), 'd-MMM-yyyy')  AS starting_gap_begin	
              ,to_date(concat(LockDownDayEnd, '-', LockDownMonthEnd, '-',LEFT(concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')),4)), 'd-MMM-yyyy') AS starting_gap_end            
             ,NotOnCurrentAlert
             ,Market
             ,99 as ClientMarket
             ,ConfigID
            FROM GoldRevenueGapParameters
            WHERE 
            Client = '{Client}'
            AND
            ConfigId = {ConfigId}
                 """

  if(spark.sql(defaultMarketParametersQuery.format(Client = ClientCode, ConfigId = '0')).first() is None):
    print("Not running the default market as the Query returned nothing")
  else:
    #going to hardCode the value to zero here -- note could just put OriginalConfigId also
    defaultStartingGapBegin = spark.sql(defaultMarketParametersQuery.format(Client = ClientCode, ConfigId = '0')).first()[0]
    defaultStartingGapEnd = spark.sql(defaultMarketParametersQuery.format(Client = ClientCode, ConfigId = '0')).first()[1]
    defaultNotOnCurrentAlert = int(spark.sql(defaultMarketParametersQuery.format(Client = ClientCode,  ConfigId = '0')).first()[2])
    defaultMarket = spark.sql(defaultMarketParametersQuery.format(Client = ClientCode,  ConfigId = '0')).first()[3].replace(" ","_")
    defaultClientMarket = spark.sql(defaultMarketParametersQuery.format(Client = ClientCode,  ConfigId = '0')).first()[4]
    defaultConfigId = spark.sql(defaultMarketParametersQuery.format(Client = ClientCode,  ConfigId = '0')).first()[5]

    print("Running the following market: " + defaultMarket)
    FinalDetailViewName = RevenueGapsDetail(ClientCode, defaultStartingGapBegin, defaultStartingGapEnd, ProgramYear, defaultNotOnCurrentAlert, defaultMarket, defaultClientMarket)
    print(FinalDetailViewName)
    marketViewList.append(FinalDetailViewName)

  #Union the dataframes in the list
  DynamicUnionOfDataframes(marketViewList)

  #Rank by Market to produce a member by market
  print("Running member ranking by market")
  FinalWithRankedMarkets()
  return ""

# COMMAND ----------

def PCPAWVisits(clientCode, ReportPeriod, ProgramYear):
  YOS = ProgramYear
  
  #Get Number of Years to Look Back
  ClientRollupQuery = """
    SELECT ApptLookback
    FROM GoldRollUpParameters
    WHERE
    Client = '{ClientCode}'
  """ 
  
  ClientRollupQuery = ClientRollupQuery.format(ClientCode = clientCode)
  if(spark.sql(ClientRollupQuery).first() is None):
    Lookback = 0
  else:
    Lookback = spark.sql(ClientRollupQuery).first()[0]

  
  #Get Last PCP Visit
  LastPCPVisitQuery = """
          WITH ProviderSpecialityDetail AS(
          SELECT 
             pm.ProviderId 
            ,m.CMSSpecialtyCode
          FROM tblProviderSpecialtyDetail psd
            LEFT JOIN tblProviderMaster pm
              ON psd.ProviderMaster_WK = pm.ProviderMaster_WK
            LEFT JOIN ProviderSpecialtyDataset m
              ON psd.TaxonomyCode = m.TaxonomyCode
          ),
          GoldenClaimDiagnosis AS(
          SELECT 
             GeneratedMedicalClaimsUniqueKey
            ,StatementFromDate
            ,StatementToDate
            ,ROW_NUMBER() OVER(PARTITION BY GeneratedMedicalClaimsUniqueKey ORDER BY GeneratedMedicalClaimsUniqueKey) AS RowNumber
          FROM MedicalGoldenClaimDiagnosis
          ),
          Claims AS(
          SELECT 
             mch.PlanMemberId
            ,mch.RenderingProviderId AS ProviderId
            ,mch.RenderingProviderSpecialtyCode AS SpecialtyCode
            ,mch.PlaceOfService AS POS
            ,gcd.StatementToDate AS ThruDate
          FROM MedicalClaimHeader mch
            INNER JOIN GoldenClaim gc
              ON mch.GeneratedMedicalClaimsUniqueKey = gc.GeneratedMedicalClaimsUniqueKey
            LEFT JOIN GoldenClaimDiagnosis gcd 
              ON mch.GeneratedMedicalClaimsUniqueKey = gcd.GeneratedMedicalClaimsUniqueKey
              AND gcd.RowNumber = 1
          --WHERE 
          --gc.IsRiskAdjustable = 1
           )
          SELECT 
               PlanMemberID
              ,MAX(date_format(z.Last_DOS,"MM/dd/yyyy")) AS last_pcp_visit
          FROM (
              SELECT  c.PlanMemberID
                      ,c.ProviderId
                      ,COALESCE(c.SpecialtyCode, '') AS Specialty_On_Claim
                      ,COALESCE(d.CMSSpecialtyCode, '') AS CMSSpecialtyCode
                      ,COALESCE(c.POS, '') AS POS
                      ,MAX(c.ThruDate) AS Last_DOS
              FROM (
                  SELECT 
                          PlanMemberID
                          ,ProviderId
                          ,SpecialtyCode
                          ,POS
                          ,ThruDate 
                  FROM Claims
                  WHERE
                  to_date(ThruDate, 'yyyy-MM-dd') >= to_date(CONCAT('01-jan-', {yos} - {lookback}), 'd-MMM-yyyy')                 
                  ) c
              LEFT JOIN ProviderSpecialityDetail d
              ON c.ProviderId = d.ProviderId
              GROUP BY 
                      c.PlanMemberID
                      ,c.ProviderId
                      ,COALESCE(c.SpecialtyCode, '')
                      ,COALESCE(d.CMSSpecialtyCode, '')
                      ,COALESCE(c.POS, '')
              ) z
          WHERE  
          CASE
              WHEN POS = '11' AND Specialty_On_Claim IN ('01', '08', '11', '38', '50', '97') THEN 1
              WHEN POS = '11' AND CMSSpecialtyCode IN ('01', '08', '11', '38', '50', '97') THEN 1
              ELSE 0 
          END = 1
          GROUP BY 
          PlanMemberID
  """
  
  LastPCPVisitDF = spark.sql(LastPCPVisitQuery.format(yos = YOS, lookback = Lookback))
  LastPCPVisitDF.createOrReplaceTempView("LastPCPVisit")
   
    #Get Last AW Visit
  LastAWVisitQuery = """   
       WITH GoldenClaimDiagnosis AS(
      SELECT 
         GeneratedMedicalClaimsUniqueKey
        ,StatementFromDate
        ,StatementToDate
        ,ROW_NUMBER() OVER(PARTITION BY GeneratedMedicalClaimsUniqueKey ORDER BY GeneratedMedicalClaimsUniqueKey) AS RowNumber
      FROM MedicalGoldenClaimDiagnosis
      ),
      Claims AS(
      SELECT 
          mch.PlanMemberId
          ,gcd.StatementToDate AS ThruDate
          ,mcl.ProcCode AS HCPCSCode
          ,mch.GeneratedMedicalClaimsUniqueKey
      FROM MedicalClaimHeader mch
          INNER JOIN MedicalClaimLine mcl
            ON mch.GeneratedMedicalClaimsUniqueKey = mcl.GeneratedMedicalClaimsUniqueKey
          INNER JOIN GoldenClaim gc
            ON mch.GeneratedMedicalClaimsUniqueKey = gc.GeneratedMedicalClaimsUniqueKey
          LEFT JOIN GoldenClaimDiagnosis gcd 
            ON mch.GeneratedMedicalClaimsUniqueKey = gcd.GeneratedMedicalClaimsUniqueKey
            AND gcd.RowNumber = 1
      WHERE
      mcl.ProcCodeType = 'HCPCSCode'
      --AND
      --gc.IsRiskAdjustable = 1
      )
      SELECT DISTINCT 
           awv.PlanMemberId
          ,awv.last_awv
          --,awv.days_since_last_awv 
      FROM  (
              SELECT PlanMemberId
                  ,MAX(date_format(ThruDate,"MM/dd/yyyy")) AS last_awv
                 -- ,datediff(current_timestamp(), MAX(date_format(ThruDate,"MM/dd/yyyy"))) AS days_since_last_awv
              FROM (	
                  SELECT DISTINCT c.ThruDate
                                  ,c.PlanMemberId
                                  ,c.HCPCSCode AS HCPCSCode
                                  FROM Claims c
                                  WHERE 
                                  to_date(c.ThruDate, 'yyyy-MM-dd') >= to_date(CONCAT('01-jan-', {yos} - {lookback}), 'd-MMM-yyyy')   
                                  AND 
                                  c.HCPCSCode IN ('G0438','G0439', 'G0402', 'G0403', 'G0404', 'G0405')
                  ) a
                  GROUP BY PlanMemberId
              ) awv
      WHERE
      last_awv is not null
  """
  
  LastAWVisitDF = spark.sql(LastAWVisitQuery.format(yos = YOS, lookback = Lookback))
  LastAWVisitDF.createOrReplaceTempView("LastAWVisit")
  
  
     #Get Last PCP Visit
  LastPCPAWVisitQuery = """
      SELECT 
              COALESCE(a.PlanMemberId, b.PlanMemberId) AS PlanMemberId
             ,a.Last_AWV
             --,a.Days_Since_Last_AWV
             ,b.Last_PCP_Visit
             ,'{Client}' AS Client
             ,current_timestamp() AS SnapshotDate
      FROM LastAWVisit a
        FULL OUTER JOIN LastPCPVisit b
          ON a.PlanMemberId = b.PlanMemberId
  """
  
  LastPCPAWVisitDF = spark.sql(LastPCPAWVisitQuery.format(Client = clientCode))
  LastPCPAWVisitDF.createOrReplaceTempView("LastPCPAWVisit") 
  
  return ""  

# COMMAND ----------

def RevenueGapHCC(clientCode):
  datesQuery = """SELECT  
                     concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')) AS ReportPeriod
                    ,LEFT(concat(lpad(year(current_date()),4,'0'),lpad(month(current_date()),2,'0')),4) AS ProgramYear
  """

  ReportPeriod = spark.sql(datesQuery).first()[0]
  ProgramYear = spark.sql(datesQuery).first()[1]
  
  hccQuery = """
     SELECT 
       ids.CodeType 
      ,ids.ICD
      ,COALESCE(hds.HCCNumber, '') AS HCCNumber
      ,COALESCE(ids.LongDescription, '') AS LongDescription
      ,COALESCE(ids.ShortDescription, '') AS ShortDescription
      ,COALESCE(hds.HCCDescription, '') AS HCCDescription
      ,COALESCE(hds.HCCVersion, '') AS HCCVersion
      ,COALESCE(UPPER(hds.HCCType), '') AS HCCType
      ,CASE 
        WHEN COALESCE(hx.EffectiveDateStart, '1900-01-01') < iyr.EffectiveDateStart THEN iyr.EffectiveDateStart 
        ELSE hx.EffectiveDateStart 
       END AS EffectiveDateStart
      ,CASE
        WHEN COALESCE(hx.EffectiveDateEnd, '9999-12-31') < iyr.EffectiveDateEnd THEN hx.EffectiveDateEnd 
        ELSE iyr.EffectiveDateEnd 
       END AS EffectiveDateEnd
      ,hds.ischronic 
    FROM ICDDataset ids
      INNER JOIN ICDEffectiveYear iyr
        ON iyr.ICDEffectiveYearID = ids.ICDEffectiveYearID
      LEFT JOIN HCCICDDatasetXref hx
        ON hx.ICDDatasetID = ids.ICDDatasetID
      LEFT JOIN HCCDataset hds
        ON hds.HCCDatasetID = hx.HCCDatasetID
      LEFT JOIN HCCEffectiveYear hyr
        ON hyr.HCCEffectiveYearID = hds.HCCEffectiveYearID
    WHERE 
      ids.IsComplete = 1
  """
  
  #get icd to hcc reference data
  ICDHCCTepRefDF = spark.sql(hccQuery)
  ICDHCCTepRefDF.createOrReplaceTempView("ICDHCCTepRef")
  
  #Setup data
  MemberPersonBridge() ##need this for BeneficiaryId to PlanMemberId mapping
  RapsDiagnosis()
  MAO004Diagnosis()
  GoldRevenueGapsParameters() #to get current RevenueGapsParams
  GoldRollupParameters() #to get current RollupParams
  
  #create PECDWClientRevenueGaps
  ZeroOneA(clientCode, ReportPeriod, ProgramYear)

  ######################################################################################################################################################
  ##########################      Everything below here is used for RevenueGapsHCC portion  ############################################################
  ######################################################################################################################################################
  YOS = ProgramYear

  ModelsAndWeightsQuery = """
                          SELECT 
                             MIN(concat('V', b.Model)) AS RAPSModel
                            ,MAX(concat('V', b.Model)) AS EDPSModel
                            ,b.RateYear
                            ,b.Ratio AS RAPS_Weight
                            ,b.EDPSRatio AS EDPS_Weight
                          FROM CMSModelEffectiveDate a
                            INNER JOIN tblCMSAdjustmentsV7 b
                              ON a.Model = b.Model
                              AND b.RateYear = '{YearOfService}' + 1
                          WHERE 
                          YEAR(a.StartDate) <= '{YearOfService}' 
                          AND 
                          YEAR(a.EndDate) >= '{YearOfService}' 
                          AND 
                          a.Model >= 22
                          GROUP BY 
                             b.RateYear
                            ,b.Ratio
                            ,b.EDPSRatio
                 """

  HCCVersionRAPSNew = spark.sql(ModelsAndWeightsQuery.format(YearOfService = YOS)).first()[0]
  HCCVersionEDPSNew = spark.sql(ModelsAndWeightsQuery.format(YearOfService = YOS)).first()[1]
  
  
  #Get LastConfirmed
  LastConfirmedQuery = """
        WITH RAPSNew AS(
        SELECT DISTINCT 
             tmm.PlanMemberId
            ,a.ICD9 AS DiagnosisCode
            ,to_date(a.ThruDate) AS DOS
            ,h.HCCNumber AS HCC
            ,h.HCCVersion AS HCCVersion
            ,h.HCCDescription
        FROM RapsDiagnosis a 
            LEFT JOIN BenMemberId tmm 
                ON a.BeneficiaryID = tmm.BeneficiaryId
            LEFT JOIN ICDHCCTepRef h 
                ON a.ICD9 = h.ICD 
                AND a.ThruDate >= h.EffectiveDateStart
                AND a.ThruDate < h.EffectiveDateEnd
                AND h.HCCVersion IN ('{HCC_VersionRAPS}') 
        ),
        MAO004DetailDiagnosisNew AS(
        SELECT DISTINCT 
             tmm.PlanMemberID
            ,a.DiagnosisCode
            ,cast(a.ThroughDateOfService as date) AS DOS
            ,c.HCCNumber AS HCC
            ,c.HCCVersion
            ,c.HCCDescription
        FROM MAO004Diagnosis a
            INNER JOIN ICDHCCTepRef c
                ON a.DiagnosisCode = c.ICD
                AND CAST(a.ThroughDateOfService AS date) >= c.EffectiveDateStart
                AND CAST(a.ThroughDateOfService AS date) < c.EffectiveDateEnd
                AND c.HCCVersion IN ('{HCC_VersionEDPS}')
            LEFT JOIN BenMemberId tmm 
                ON a.BeneficiaryID = tmm.BeneficiaryId
        ),
        CMSCombined AS(
        SELECT DISTINCT 
           PlanMemberId
          ,HCC
          ,HCCVersion
          ,DOS
          ,HCCDescription 
        FROM RAPSNew
        UNION
        SELECT DISTINCT 
           PlanMemberId
          ,HCC
          ,HCCVersion
          ,DOS
          ,HCCDescription
        FROM MAO004DetailDiagnosisNew
        )
        SELECT 
           a.PlanMemberId
          ,a.HCC
          ,a.HCCVersion
          ,MAX(a.DOS) AS LastDOS
          ,a.HCCDescription
        FROM CMSCombined a
        INNER JOIN (SELECT PlanMemberId, HCC, MAX(HCCVersion) AS HCCVersion
                    FROM CMSCombined
                    GROUP BY PlanMemberId, HCC
                    ) b
          ON a.PlanMemberId = b.PlanMemberId
          AND a.HCC = b.HCC
          AND a.HCCVersion = b.HCCVersion
        GROUP BY 
           a.PlanMemberId
          ,a.HCC
          ,a.HCCVersion
          ,a.HCCDescription
  """

  LastConfirmedQuery = LastConfirmedQuery.format( \
        HCC_VersionEDPS = HCCVersionEDPSNew,\
        HCC_VersionRAPS = HCCVersionRAPSNew,\
        )
  
  LastConfirmedDF = spark.sql(LastConfirmedQuery)
  
  LastConfirmedDF.createOrReplaceTempView("LastConfirmed")
  
  #Run PCPAWVisits
  PCPAWVisits(clientCode, ReportPeriod, ProgramYear)
  
  #Create FinalDetail
  RevenueGapsCompleteQuery = """   
        WITH RosterInfo AS(
        SELECT 
                 mr.PlanMemberId
                ,mr.providerID
                ,mr.memberFirstName AS MemberFirstName
                ,mr.memberLastName AS MemberLastName
                ,mr.memberDOB AS MemberDOB
                ,mr.POCode
                ,mr.POName
                ,mr.PracticeCode
                ,mr.PracticeName
                ,mr.providerNPI AS NPI
                ,mr.ProviderFirstName
                ,mr.ProviderLastName
        FROM MemberRoster mr 
        WHERE
        mr.reportMonth = '{Report_Period}'
        ),
        ReportBaseInfo AS(
        SELECT 
                 rb.PlanMemberId
                ,rb.market AS Market
                ,rb.reportMonth AS RosterMonth
                ,rb.planID
        FROM ReportBase rb 
        WHERE 
        rb.reportMonth = '{Report_Period}'
        ),
        RevenueGapsFinal AS(
            SELECT DISTINCT
            '{Client_Code}' AS clientCode
            ,rg.HCC
            ,rg.HCCVersions
            ,rg.AlertCategory
            ,rg.ClosureReason
            ,lc.HCCDescription
            ,lc.LastDOS AS Last_DCConfirmed
            ,rb.RosterMonth
            ,lp.Last_PCP_Visit
            ,lp.Last_AWV
            ,'{Report_Period}' AS ReportPeriod 
            ,current_timestamp() AS SnapshotDate --generated at runtime
            ,mr.providerID
            ,rg.MemberId
            ,mr.MemberFirstName
            ,mr.MemberLastName
            ,mr.MemberDOB
            ,mr.POCode
            ,mr.POName
            ,mr.PracticeCode
            ,mr.PracticeName
            ,rg.Market
            ,mr.NPI
            ,mr.ProviderFirstName
            ,mr.ProviderLastName
            ,rg.Diags
            ,rb.PlanID
            FROM FinalDetail rg 
            JOIN ReportBaseInfo rb 
                ON rg.MemberId = rb.PlanMemberId 
            LEFT JOIN RosterInfo mr 
                ON rg.MemberId = mr.PlanMemberId
            LEFT JOIN LastConfirmed lc 
                ON rg.MemberId = lc.PlanMemberId
                AND rg.HCC = lc.HCC 
            LEFT JOIN LastPCPAWVisit lp 
                ON rg.MemberId = lp.PlanMemberId
          )
          SELECT 
             clientCode
            ,HCC AS hccNumber
            ,HCCVersions AS hccVersion
            ,AlertCategory AS alertCategory
            ,ClosureReason AS closureReason
            ,HCCDescription AS hccDescription
            ,to_date(Last_DCConfirmed,"MM/dd/yyyy") AS lastDCConfirmedDate
            ,to_date(Last_PCP_Visit,"MM/dd/yyyy") AS lastPCPVisitDate
            ,to_date(Last_AWV,"MM/dd/yyyy") AS lastAWVDate
            ,ReportPeriod AS reportMonth
            ,to_date(SnapshotDate,"MM-dd-yyyy") AS snapshotDate
            ,providerID AS providerID
            ,MemberId AS planMemberID
            ,MemberFirstName AS memberFirstName
            ,MemberLastName AS memberLastName
            ,MemberDOB AS memberDOB
            ,PracticeCode AS practiceCode
            ,PracticeName AS practiceName
            ,Market AS market
            ,NPI AS providerNPI
            ,ProviderFirstName AS providerFirstName
            ,ProviderLastName AS providerLastName
            ,PlanID as planID
            ,sha2(concat_ws("|",
                        IfNull(clientCode,"") 
                       ,IfNull(HCC,"") 
                       ,IfNull(HCCVersions,"")
                       ,IfNull(AlertCategory,"")
                       ,IfNull(ClosureReason,"") 
                       ,IfNull(HCCDescription,"") 
                       ,IfNull(Last_DCConfirmed,"") 
                       ,IfNull(Last_PCP_Visit,"") 
                       ,IfNull(Last_AWV,"") 
                       ,IfNull(ReportPeriod,"") 
                       ,IfNull(SnapshotDate,"")
                       ,IfNull(providerID,"")
                       ,IfNull(MemberId,"")
                       ,IfNull(MemberFirstName,"") 
                       ,IfNull(MemberLastName,"")
                       ,IfNull(MemberDOB,"") 
                       ,IfNull(PracticeCode,"") 
                       ,IfNull(PracticeName,"")
                       ,IfNull(Market,"") 
                       ,IfNull(NPI,"") 
                       ,IfNull(ProviderFirstName,"")
                       ,IfNull(ProviderLastName,"")
                       ,IfNull(PlanID,"")
                ), 256) AS hashKey
          FROM RevenueGapsFinal
  """

  RevenueGapsCompleteQuery = RevenueGapsCompleteQuery.format( \
        Report_Period = ReportPeriod,\
        Client_Code = clientCode
        )
  
  print(f"ReportPeriod:{ReportPeriod}")
  
  RevenueGapsCompleteDF = spark.sql(RevenueGapsCompleteQuery)
  
  RevenueGapsCompleteDF.createOrReplaceTempView("RevenueGapsComplete")
  
  return ""

# COMMAND ----------

def WriteOutput(clientCode):
  print("Writing out to MemberRevenueGap")
  
  #Merge if there are no issues
  mergeSQL = """
MERGE INTO MemberRevenueGap t 
USING (
	SELECT 
       planMemberID
      ,hccNumber
      ,reportMonth
      ,clientCode
      ,memberFirstName
      ,memberLastName
      ,memberDOB
      ,hccVersion
      ,hccDescription
      ,providerID
      ,providerNPI
      ,providerLastName
      ,providerFirstName
      ,practiceCode
      ,practiceName
      ,market
      ,alertCategory
      ,closureReason
      ,lastDCConfirmedDate
      ,lastPCPVisitDate
      ,lastAWVDate
      ,snapshotDate
      ,planID
      ,hashKey
	FROM RevenueGapsComplete 
) s 
    ON t.planMemberID = s.planMemberID
    AND t.hccNumber = s.hccNumber
    AND t.reportMonth = s.reportMonth
WHEN MATCHED AND s.hashKey <> t.hashKey THEN
UPDATE SET 
       clientCode = s.clientCode
      ,memberFirstName = s.memberFirstName
      ,memberLastName = s.memberLastName
      ,memberDOB = s.memberDOB
      ,hccVersion = s.hccVersion
      ,hccDescription = s.hccDescription
      ,providerID = s.providerID
      ,providerNPI = s.providerNPI
      ,providerLastName = s.providerLastName
      ,providerFirstName = s.providerFirstName
      ,practiceCode = s.practiceCode
      ,practiceName = s.practiceName
      ,market = s.market
      ,alertCategory  = s.alertCategory
      ,lastDCConfirmedDate = s.lastDCConfirmedDate
      ,lastPCPVisitDate = s.lastPCPVisitDate
      ,lastAWVDate = s.lastAWVDate
      ,snapshotDate = s.snapshotDate
      ,planID = s.planID
      ,hashKey = s.hashKey 
WHEN NOT MATCHED THEN 
INSERT (
       planMemberID
      ,hccNumber
      ,reportMonth
      ,clientCode
      ,memberFirstName
      ,memberLastName
      ,memberDOB
      ,hccVersion
      ,hccDescription
      ,providerID
      ,providerNPI
      ,providerLastName
      ,providerFirstName
      ,practiceCode
      ,practiceName
      ,market
      ,alertCategory
      ,closureReason
      ,lastDCConfirmedDate
      ,lastPCPVisitDate
      ,lastAWVDate
      ,snapshotDate
      ,planID
      ,hashKey
) 
VALUES (
     s.planMemberID
    ,s.hccNumber
    ,s.reportMonth
    ,s.clientCode
    ,s.memberFirstName
    ,s.memberLastName
    ,s.memberDOB
    ,s.hccVersion
    ,s.hccDescription
    ,s.providerID
    ,s.providerNPI
    ,s.providerLastName
    ,s.providerFirstName
    ,s.practiceCode
    ,s.practiceName
    ,s.market
    ,s.alertCategory
    ,s.closureReason
    ,s.lastDCConfirmedDate
    ,s.lastPCPVisitDate
    ,s.lastAWVDate
    ,s.snapshotDate
    ,s.planID
    ,s.hashKey
)
"""
  spark.sql(mergeSQL)

# COMMAND ----------

# DBTITLE 1,Final Output
try:
  #Run all the other stuff above
  RevenueGapHCC(clientCode)

  #Check for Duplicates based on business keys
  DuplicateQuery = """
    SELECT COUNT(1) AS NumDups
    FROM (
        SELECT 
           planMemberID
          ,hccNumber
          ,reportMonth
        FROM RevenueGapsComplete
        GROUP BY 
           planMemberID
          ,hccNumber
          ,reportMonth
        HAVING COUNT(1) > 1
        ) a
    """
  
  if(spark.sql(DuplicateQuery).first()[0] == 0): #no dups yay move along
    WriteOutput(clientCode)
  else:
    raise Exception("Duplicates Found!!!!!! :O")
except Exception as e:
      print(str(e))
