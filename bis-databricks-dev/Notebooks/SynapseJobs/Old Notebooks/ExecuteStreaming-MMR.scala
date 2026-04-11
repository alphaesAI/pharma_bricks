// Databricks notebook source
// DBTITLE 1,Setup parameters
dbutils.widgets.text("ClientContainer","","")
dbutils.widgets.text("ConsolidatedPath","","")
dbutils.widgets.text("DestTable","","")
dbutils.widgets.text("CheckPoint","","")

val clientContainer = dbutils.widgets.get("ClientContainer")
val consolidatedPath = dbutils.widgets.get("ConsolidatedPath")
val destTable = dbutils.widgets.get("DestTable")
val checkPoint = dbutils.widgets.get("CheckPoint")

// COMMAND ----------

// DBTITLE 1,Import libraries
import org.apache.spark.sql.streaming.Trigger
import org.apache.spark.sql.DataFrame
import scala.util.{Try, Success, Failure}
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._

// COMMAND ----------

// DBTITLE 1,Defined variables for JDBC connection
//Create environment variable to handle the database connection
val dbEnv = spark.sparkContext.getConf.get("spark.databricks.clusterUsageTags.clusterOwnerOrgId")
var envLetter =""
var envUser="_ETLUSER_SQL"
var blobKey = ""

if (dbEnv == "934226345849410") {envLetter = "d"; envUser = "DEV"+envUser; blobKey = "zbeO33jn/dsLe/dzJiWbpRhsEdS7OR4+kwi/OuEiZkq6qxNYsiHmvCQejOYYhSSwhTJAYBqVTY9Kwe0yyXRmMQ=="}
else if (dbEnv == "5826678703751685") {envLetter = "q"; envUser = "QA"+envUser; blobKey = "tjmO3z7qpHlUNRnZ4cYtRTbIWlypTEX/D+6HFtLHXNs5wSDpAXHaVa4/G/8IYxaavqXw53vj3uaolw1SEYB82Q=="}
else if (dbEnv == "7093677384385470") {envLetter = "s"; envUser = "STG"+envUser; blobKey = "5a3ho8IS2Xvfp458gqh42DL021Tq0WyuDy8BgLjvUiZFZWXZPBEpwudAhD0yPsocNsWAsLJv7MziyRYGYPOKPA=="}
else {envLetter = "p"; envUser = "PRD"+envUser; blobKey = "wzOEDvQP/12TggUpV8diII/T1q/3mUj2l+C5E/GSD964A7k/N2TDVF6MvHCD7PpwU4FPtx5pMslYEzWJlh2Lew=="} 

val jdbcUsername = envUser
val jdbcPassword = dbutils.secrets.get(scope = "idapkeyvault", key = "ETLUSER-SQL")
val sprakPath = "fs.azure.account.key.svtss"+envLetter+"idap01s.blob.core.windows.net"
val jdbcString = "jdbc:sqlserver://sql-c-"+envLetter+"-shrd-idap0000-01.database.windows.net:1433;database=syn-c-"+envLetter+"-shrd-idap0000-01"
val tempDir = "wasbs://"+clientContainer+"@svtss"+envLetter+"idap01s.blob.core.windows.net/stream-temp"

// COMMAND ----------

// DBTITLE 1,Create streaming method
def startStreaming(df: DataFrame): Try[org.apache.spark.sql.streaming.StreamingQuery] = {
  try{
    spark.conf.set(sprakPath, blobKey)
    
    val stream = df.writeStream
                  .format("com.databricks.spark.sqldw")  
                  .option("url", jdbcString)
                  .option("user", jdbcUsername)
                  .option("password", jdbcPassword)
                  .option("tempDir", tempDir)
                  .option("forwardSparkAzureStorageCredentials", "true")
                  .option("dbTable", destTable) 
                  .option("checkpointLocation", checkPoint) 
                  .trigger(Trigger.Once) // make sure iterate just one time
                  .outputMode("append")
                  .start()
    
    stream.awaitTermination()
    
    Success(stream)
    
    } 
  catch {
      case unknown: Exception => {
        Failure(unknown)
      }
    }
}

// COMMAND ----------

// DBTITLE 1,Execute streaming and return notebook output
var rJSON = ""

//Read the table as a stream source 
var consolidated = spark.readStream.format("delta").load(consolidatedPath) 

//Renamed columns to match model in synapse
consolidated = consolidated
    .withColumnRenamed("LOAD_DATETIME", "LoadDateTime")
    .withColumnRenamed("FILE_ID", "FileID")
    .withColumnRenamed("CLIENT_ID", "ClientID")
    .withColumnRenamed("FILE_LAYOUT_ID", "FileLayoutID")
    .withColumnRenamed("FILE_LAYOUT_DESCRIPTION", "FileLayoutDescription")
    // data format
    // can be removed once we update to define the datatypes in delta lake
    .withColumn("RunDate", col("RunDate").cast(IntegerType))
    .withColumn("PaymentDate", col("PaymentDate").cast(IntegerType))
    .withColumn("DateOfBirth", col("DateOfBirth").cast(IntegerType))
    .withColumn("NumberOfPaymentAdjustmentMonthsPartA", col("NumberOfPaymentAdjustmentMonthsPartA").cast(IntegerType))
    .withColumn("NumberOfPaymentAdjustmentMonthsPartB", col("NumberOfPaymentAdjustmentMonthsPartB").cast(IntegerType))
    .withColumn("PaymentAdjustmentStartDate", col("PaymentAdjustmentStartDate").cast(IntegerType))
    .withColumn("PaymentAdjustmentEndDate", col("PaymentAdjustmentEndDate").cast(IntegerType))
    .withColumn("NumberOfPaymentAdjustmentMonthsPartD", col("NumberOfPaymentAdjustmentMonthsPartD").cast(IntegerType))
    .withColumn("RiskAdjusterFactorA", col("RiskAdjusterFactorA").cast(DecimalType(6,4)))
    .withColumn("RiskAdjusterFactorB", col("RiskAdjusterFactorB").cast(DecimalType(6,4)))
    .withColumn("DemographicPaymentAdjustmentRatePartA", col("DemographicPaymentAdjustmentRatePartA").cast(DecimalType(8,2)))
    .withColumn("DemographicPaymentAdjustmentRatePartB", col("DemographicPaymentAdjustmentRatePartB").cast(DecimalType(8,2)))
    .withColumn("MonthlyPaymentAdjustmentAmountRateA", col("MonthlyPaymentAdjustmentAmountRateA").cast(DecimalType(8,2)))
    .withColumn("MonthlyPaymentAdjustmentAmountRateB", col("MonthlyPaymentAdjustmentAmountRateB").cast(DecimalType(8,2)))
    .withColumn("LisPremiumSubsidy", col("LisPremiumSubsidy").cast(DecimalType(7,2)))
    .withColumn("MtmAddOn", col("MtmAddOn").cast(DecimalType(9,2)))
    .withColumn("PreviousDisableRatio", col("PreviousDisableRatio").cast(DecimalType(7,4)))
    .withColumn("PartCBasicPremiumPartAAmount", col("PartCBasicPremiumPartAAmount").cast(DecimalType(7,2)))
    .withColumn("PartCBasicPremiumPartBAmount", col("PartCBasicPremiumPartBAmount").cast(DecimalType(7,2)))
    .withColumn("RebateForPartACostSharingReduction", col("RebateForPartACostSharingReduction").cast(DecimalType(7,2)))
    .withColumn("RebateForPartBCostSharingReduction", col("RebateForPartBCostSharingReduction").cast(DecimalType(7,2)))
    .withColumn("RebateForOtherPartAMandatorySupplementalBenefits", col("RebateForOtherPartAMandatorySupplementalBenefits").cast(DecimalType(7,2)))
    .withColumn("RebateForOtherPartBMandatorySupplementalBenefits", col("RebateForOtherPartBMandatorySupplementalBenefits").cast(DecimalType(7,2)))
    .withColumn("RebateForPartBPremiumReductionPartAAmount", col("RebateForPartBPremiumReductionPartAAmount").cast(DecimalType(7,2)))
    .withColumn("RebateForPartBPremiumReductionPartBAmount", col("RebateForPartBPremiumReductionPartBAmount").cast(DecimalType(7,2)))
    .withColumn("RebateForPartDSupplementalBenefitsPartAAmount", col("RebateForPartDSupplementalBenefitsPartAAmount").cast(DecimalType(7,2)))
    .withColumn("RebateForPartDSupplementalBenefitsPartBAmount", col("RebateForPartDSupplementalBenefitsPartBAmount").cast(DecimalType(7,2)))
    .withColumn("TotalPartAMAPayment", col("TotalPartAMAPayment").cast(DecimalType(9,2)))
    .withColumn("TotalPartBMAPayment", col("TotalPartBMAPayment").cast(DecimalType(9,2)))
    .withColumn("TotalMAPaymentAmount", col("TotalMAPaymentAmount").cast(DecimalType(10,2)))
    .withColumn("PartDRAFactor", col("PartDRAFactor").cast(DecimalType(6,4)))
    .withColumn("PartDLowIncomeMultiplier", col("PartDLowIncomeMultiplier").cast(DecimalType(6,4)))
    .withColumn("PartDLongTermInstitutionalMultiplier", col("PartDLongTermInstitutionalMultiplier").cast(DecimalType(6,4)))
    .withColumn("RebateForPartDBasicPremiumReduction", col("RebateForPartDBasicPremiumReduction").cast(DecimalType(7,2)))
    .withColumn("PartDBasicPremiumAmount", col("PartDBasicPremiumAmount").cast(DecimalType(7,2)))
    .withColumn("PartDDirectSubsidyMonthlyPaymentAmount", col("PartDDirectSubsidyMonthlyPaymentAmount").cast(DecimalType(9,2)))
    .withColumn("ReinsuranceSubsidyAmount", col("ReinsuranceSubsidyAmount").cast(DecimalType(9,2)))
    .withColumn("LowIncomeSubsidyCostSharingAmount", col("LowIncomeSubsidyCostSharingAmount").cast(DecimalType(9,2)))
    .withColumn("TotalPartDPayment", col("TotalPartDPayment").cast(DecimalType(10,2)))
    .withColumn("PACEPremiumAddOn", col("PACEPremiumAddOn").cast(DecimalType(9,2)))
    .withColumn("PACECostSharingAddOn", col("PACECostSharingAddOn").cast(DecimalType(9,2)))
    .withColumn("PartCFrailtyScoreFactor", col("PartCFrailtyScoreFactor").cast(DecimalType(6,4)))
    .withColumn("MSPFactor", col("MSPFactor").cast(DecimalType(6,4)))
    .withColumn("MSPReductionReductionAdjustmentAmountPartA", col("MSPReductionReductionAdjustmentAmountPartA").cast(DecimalType(9,2)))
    .withColumn("MSPReductionReductionAdjustmentAmountPartB", col("MSPReductionReductionAdjustmentAmountPartB").cast(DecimalType(9,2)))
    .withColumn("PartDCoverageGapDiscountAmount",col("PartDCoverageGapDiscountAmount").cast(DecimalType(7,2)))
    .withColumn("PartARiskAdjustedMonthlyRateAmountForPaymentAdjustment", col("PartARiskAdjustedMonthlyRateAmountForPaymentAdjustment").cast(DecimalType(8,2)))
    .withColumn("PartBRiskAdjustedMonthlyRateAmountForPaymentAdjustment", col("PartBRiskAdjustedMonthlyRateAmountForPaymentAdjustment").cast(DecimalType(8,2)))
    .withColumn("PartDDirectSubsidyMonthlyRateAmountForPaymentAdjustment", col("PartDDirectSubsidyMonthlyRateAmountForPaymentAdjustment").cast(DecimalType(8,2)))

startStreaming(consolidated) match {
                    case Success(df) => {
                           rJSON = "SUCCESS"
                    }
                    case Failure(ex) => { //handle exception
                        rJSON = "FAILURE: " + ex.getMessage.toString
                    }
            }

dbutils.notebook.exit(rJSON)
