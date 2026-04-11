// Databricks notebook source
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("SubGroupConfigPath","","")

val Container = dbutils.widgets.get("ClientContainer")

// COMMAND ----------

import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import scala.util.Try
import io.delta.tables._
import spark.implicits._

// COMMAND ----------

import  org.apache.hadoop.fs.{FileSystem,Path}

def path_exists(pathToCheck: String): Boolean =
{ 
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val IsExists = fs.exists(new org.apache.hadoop.fs.Path(pathToCheck)) 
  return IsExists 
}

// COMMAND ----------

val CMMRLocation = "/mnt/" + Container + "/Gold/MA/Client/ConsolidatedMMR"
val dfCMMRLocationFile = spark.read.format("delta").option("header","true").load(CMMRLocation)

dfCMMRLocationFile.createOrReplaceTempView("ConsolidatedMMR")
dfCMMRLocationFile.printSchema

val MemberLocation = "/mnt/" + Container + "/Gold/MA/Client/Member"
val dfMemberLocationFile = spark.read.format("delta").option("header","true").load(MemberLocation)

dfMemberLocationFile.createOrReplaceTempView("Member")
dfMemberLocationFile.printSchema

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW SEGMENTINI AS 
// MAGIC WITH THIS AS(
// MAGIC SELECT 
// MAGIC    SubscriberId 
// MAGIC   ,TotalPartCPayment
// MAGIC   ,PartCRAFactorTypeCode
// MAGIC   ,PartCDefaultRiskFactorCode
// MAGIC   ,Hospice
// MAGIC   ,ESRD
// MAGIC   ,MedicaidDualStatusCode
// MAGIC   ,OriginalReasonforEntitlement --?
// MAGIC   ,PlanID
// MAGIC   ,MedicaidIndicator
// MAGIC   ,DOB
// MAGIC   ,PlanBenefitPackage
// MAGIC   ,StateandCountyCode
// MAGIC   ,RiskAdjusterFactorA
// MAGIC   ,EnrollmentYear
// MAGIC   ,EnrollmentMonth
// MAGIC   ,OriginalReasonforEntitlement as OREC
// MAGIC   ,DATEDIFF(current_date(),DOB) div 365 as AGE
// MAGIC   ,CASE 
// MAGIC     WHEN PartCRAFactorTypeCode IN ('CP','CN','CF') AND MedicaidDualStatusCode <> ' '   
// MAGIC 		THEN   
// MAGIC 			CASE WHEN MedicaidDualStatusCode IN ('01','03','05','06') THEN 'CP' 
// MAGIC 				 WHEN MedicaidDualStatusCode IN ('02','04','08','10') THEN 'CF' ELSE 'CN' 
// MAGIC 			END
// MAGIC     ELSE    
// MAGIC        CASE 
// MAGIC          WHEN PartCRAFactorTypeCode = ' ' AND PartCDefaultRiskFactorCode in ('1','Y') THEN 'E' 
// MAGIC 		 ELSE PartCRAFactorTypeCode 
// MAGIC        END
// MAGIC     END AS RAF 
// MAGIC FROM ConsolidatedMMR
// MAGIC )
// MAGIC SELECT DISTINCT
// MAGIC    SubscriberId 
// MAGIC   ,TotalPartCPayment
// MAGIC   ,PartCRAFactorTypeCode
// MAGIC   ,PartCDefaultRiskFactorCode
// MAGIC   ,Hospice
// MAGIC   ,ESRD
// MAGIC   ,MedicaidDualStatusCode
// MAGIC   ,OriginalReasonforEntitlement
// MAGIC   ,PlanID
// MAGIC   ,MedicaidIndicator
// MAGIC   ,DOB
// MAGIC   ,PlanBenefitPackage
// MAGIC   ,StateandCountyCode
// MAGIC   ,RiskAdjusterFactorA
// MAGIC   ,Age
// MAGIC   ,RAF
// MAGIC   ,CASE 
// MAGIC     WHEN RAF = 'CP' and (OREC=0  or AGE>=65 ) THEN 'CPA' 
// MAGIC     WHEN RAF = 'CP' and (OREC!=0 or AGE<65  ) then 'CPD'
// MAGIC     WHEN RAF  ='CF' and (OREC=0  or AGE>=65 ) THEN 'CFA' 
// MAGIC     WHEN RAF = 'CF' and (OREC!=0 or AGE<65  ) then 'CFD' 
// MAGIC     WHEN RAF  ='CN' and (OREC=0  or AGE>=65 ) THEN 'CNA' 
// MAGIC     WHEN RAF = 'CN' and (OREC!=0 or AGE<65  ) then 'CND'
// MAGIC     WHEN RAF  ='E' THEN 'NE'
// MAGIC     WHEN RAF  ='I' THEN 'INS'
// MAGIC     WHEN PartCRAFactorTypeCode=' ' and ESRD=' ' and Hospice=' ' and PartCDefaultRiskFactorCode in (' ','N') THEN 'NULL'
// MAGIC     WHEN ESRD='' and Hospice='Y' then 'Hospice' -- added Hospice as Segment on 6/23
// MAGIC     WHEN PartCRAFactorTypeCode in ('C1','C2') then 'GC'
// MAGIC     WHEN PartCRAFactorTypeCode in ('G1','G2','I1','I2') then 'GI'
// MAGIC     WHEN PartCRAFactorTypeCode in ('D') then 'DI'
// MAGIC     WHEN PartCRAFactorTypeCode in ('ED') then 'DNE'
// MAGIC     WHEN PartCRAFactorTypeCode in ('E1','E2') then 'GNE'
// MAGIC     WHEN PartCRAFactorTypeCode='SE' then 'SNP'
// MAGIC     WHEN PartCRAFactorTypeCode='' and PartCDefaultRiskFactorCode in ('','N') and HOSPICE='Y' and ESRD='Y' then 'Hospice, ESRD'
// MAGIC     WHEN PartCRAFactorTypeCode not in ('CP','CN','CF','C','I','E','C1','C2','E2') and ESRD='Y' then 'ESRD'
// MAGIC     WHEN PartCRAFactorTypeCode = ' ' and PartCDefaultRiskFactorCode = 3 then 'ESRD'
// MAGIC    END AS SEGMENT
// MAGIC   ,CASE 
// MAGIC     WHEN last_day(to_date(concat_ws("-",CAST(EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(EnrollmentMonth,3), "MMM"),to_timestamp(right(EnrollmentMonth,3), "MMM"))) AS STRING),'20'), "yyyy-MM-dd")) > last_day(add_months(current_date(), -1)) THEN 0       ELSE 1 
// MAGIC    END AS MemberMonth
// MAGIC   ,to_date(concat_ws("-",CAST(EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(EnrollmentMonth,3), "MMM"),to_timestamp(right(EnrollmentMonth,3), "MMM"))) AS STRING),'01'), "yyyy-MM-dd") AS StartDate
// MAGIC   ,last_day(to_date(concat_ws("-",CAST(EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(EnrollmentMonth,3), "MMM"),to_timestamp(right(EnrollmentMonth,3), "MMM"))) AS STRING),'20'), "yyyy-MM-dd")) AS Enddate
// MAGIC FROM THIS;
// MAGIC     
// MAGIC SELECT * FROM SEGMENTINI

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW SegmentWithMember AS 
// MAGIC WITH THIS AS(
// MAGIC SELECT DISTINCT  
// MAGIC    SubscriberId
// MAGIC   ,StartDate 
// MAGIC   ,Enddate
// MAGIC   ,TotalPartCPayment
// MAGIC   ,PartCRAFactorTypeCode
// MAGIC   ,PartCDefaultRiskFactorCode
// MAGIC   ,Hospice
// MAGIC   ,ESRD
// MAGIC   ,MedicaidDualStatusCode
// MAGIC   ,OriginalReasonforEntitlement
// MAGIC   ,PlanID
// MAGIC   ,MedicaidIndicator
// MAGIC   ,DOB
// MAGIC   ,PlanBenefitPackage
// MAGIC   ,StateandCountyCode
// MAGIC   ,RiskAdjusterFactorA
// MAGIC   ,Age
// MAGIC   ,RAF
// MAGIC   ,Segment 
// MAGIC   ,MemberMonth     
// MAGIC   ,CASE 
// MAGIC       WHEN A.SEGMENT='INS' THEN 'INSTITUTIONAL'
// MAGIC       WHEN A.SEGMENT IN ('GC','GNE','DI','GI','DNE') THEN 'ESRD'
// MAGIC       WHEN A.SEGMENT='HOSPICE, ESRD' THEN A.SEGMENT
// MAGIC       WHEN A.SEGMENT='NE' THEN 'NEW ENROLLEE'
// MAGIC       WHEN A.SEGMENT='HOSPICE' THEN 'HOSPICE'
// MAGIC       WHEN A.SEGMENT='ESRD' THEN 'ESRD'--@@
// MAGIC       WHEN A.SEGMENT LIKE 'CN%' THEN 'FULL RISK COMMUNITY'
// MAGIC       WHEN A.SEGMENT LIKE 'CP%' THEN 'PARTIAL DUAL'
// MAGIC       WHEN A.SEGMENT LIKE 'CF%' THEN 'FULL DUAL'
// MAGIC       WHEN A.SEGMENT='SNP' THEN 'NEW ENROLLEE CHRONIC CARE SNP'
// MAGIC    END AS MEMBERSTATUS
// MAGIC   ,ROW_NUMBER() OVER(PARTITION BY A.SubscriberID ORDER BY A.StartDate DESC) AS Islatest 
// MAGIC   ,SUM(MemberMonth) OVER(PARTITION BY A.SubscriberID) AS TotalMemberMonths 
// MAGIC FROM SEGMENTINI A
// MAGIC         --INNER JOIN Member B  -- Goldlayer/Member
// MAGIC         --  ON A.SubscriberID=B.SubscriberId
// MAGIC )
// MAGIC SELECT 
// MAGIC    SubscriberId
// MAGIC   ,StartDate 
// MAGIC   ,Enddate
// MAGIC   ,TotalPartCPayment
// MAGIC   ,PartCRAFactorTypeCode
// MAGIC   ,PartCDefaultRiskFactorCode
// MAGIC   ,Hospice
// MAGIC   ,ESRD
// MAGIC   ,MedicaidDualStatusCode
// MAGIC   ,OriginalReasonforEntitlement
// MAGIC   ,PlanID
// MAGIC   ,MedicaidIndicator
// MAGIC   ,DOB
// MAGIC   ,PlanBenefitPackage
// MAGIC   ,StateandCountyCode
// MAGIC   ,RiskAdjusterFactorA
// MAGIC   ,Age
// MAGIC   ,RAF
// MAGIC   ,Segment 
// MAGIC   ,MemberMonth     
// MAGIC   ,MEMBERSTATUS
// MAGIC   ,CASE WHEN IsLatest = 1 THEN 1 ELSE 0 END AS Islatest 
// MAGIC   ,TotalMemberMonths 
// MAGIC FROM THIS;
// MAGIC 
// MAGIC SELECT * FROM SegmentWithMember;

// COMMAND ----------

// MAGIC %sql
// MAGIC CREATE OR REPLACE TEMP VIEW Segment AS SELECT 
// MAGIC SubscriberId
// MAGIC ,StartDate 
// MAGIC ,Enddate
// MAGIC ,TotalPartCPayment
// MAGIC ,PartCRAFactorTypeCode
// MAGIC ,PartCDefaultRiskFactorCode
// MAGIC ,Hospice
// MAGIC ,ESRD
// MAGIC ,MedicaidDualStatusCode
// MAGIC ,OriginalReasonforEntitlement
// MAGIC ,PlanID
// MAGIC ,MedicaidIndicator
// MAGIC ,DOB
// MAGIC ,PlanBenefitPackage
// MAGIC ,StateandCountyCode
// MAGIC ,RiskAdjusterFactorA
// MAGIC ,Age
// MAGIC ,RAF AS RiskAdjustmentFactor
// MAGIC ,Segment
// MAGIC ,IsLatest
// MAGIC ,MemberMonth
// MAGIC ,MemberStatus
// MAGIC ,TotalMemberMonths
// MAGIC FROM SegmentWithMember;
// MAGIC 
// MAGIC SELECT * FROM Segment;

// COMMAND ----------

val GoldPath = "/mnt/"+ Container + "/Gold/MA/Risk/Segment"
val PathToDelete = "/mnt/" + Container + "/Gold/MA/Risk/ToDelete"

val df_Segment = spark.sql(""" SELECT * FROM Segment """)

if(path_exists(GoldPath) == true)
{
dbutils.fs.mv(GoldPath, PathToDelete,true)
}

df_Segment.write.format("delta").save(GoldPath)
