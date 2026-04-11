# Databricks notebook source
dbutils.widgets.text("ClientContainer","","")

container = dbutils.widgets.get("ClientContainer")

# COMMAND ----------

# DBTITLE 1,Defined File Paths
cmmrConsolidatedPath =  "/mnt/"+ container + "/consolidated/MA/Data/ConsolidatedMMR"
memberGroupPath = "/mnt/"+ container + "/Gold/MA/Client/MemberGroup"
cmmrGoldPath = "/mnt/"+ container + "/Gold/MA/Client/ConsolidatedMMR"

# COMMAND ----------

# DBTITLE 1,Method: check file path
def path_exists(pathToCheck):
  fs = sc._jvm.org.apache.hadoop.fs.FileSystem.get(sc._jsc.hadoopConfiguration())
  IsExists = fs.exists(sc._jvm.org.apache.hadoop.fs.Path(pathToCheck))
  return IsExists

# COMMAND ----------

# DBTITLE 1,SQL for Joining MemberGroup Gold Table and Latest Consolidated CMMR to Find Same Year
sqlStmt = """
With gcmmr AS
(SELECT DISTINCT
		 cmmr.PlanID
		,cmmr.BeneficiaryID
		,cmmr.BeneficiaryIDOriginal
		,cmmr.MBIIndicator
		,cmmr.EnrollmentMonth
		,cmmr.EnrollmentYear
        ,cmmr.EnrollmentYearMonth
		,cmmr.Rundate
		,cmmr.Lastname
		,cmmr.FirstInitial
		,cmmr.EnrollmentSource
		,cmmr.PersonTotal
		,cmmr.PlanBenefitPackage
		,cmmr.NewPlanBenefitPackage
		,cmmr.SegmentID
		,cmmr.EghpFlag
		,cmmr.RiskAdjusterFactorA
		,cmmr.PartDRAFactor
		,cmmr.Gendercode
		,cmmr.DOB
		,cmmr.Agegroup
		,cmmr.AgedDisabledIdentifier
		,cmmr.StateandCountyCode
		,cmmr.OutOfAreaIndicator
		,cmmr.Hospice
		,cmmr.ESRD
		,cmmr.AgedMsp
		,cmmr.InstitutionalFlag
		,cmmr.NHC
		,cmmr.MedicaidBeneficiaryStatusFlag
		,cmmr.MedicaidIndicator
		,cmmr.CurrentMedicaidStatus
		,cmmr.PartCDualStatusFlag
		,cmmr.PartDDualStatusFlag
		,cmmr.LTIFlag
		,cmmr.PartDLowIncomeIndicator
		,cmmr.PartDLongTermInstitutionalIndicator
		,cmmr.PartCDefaultRiskFactorCode
		,cmmr.ESRDMspFlag
		,cmmr.RiskAdjusterAgeGroup
		,cmmr.PreviousDisableRatio
		,cmmr.DeMinimis
		,cmmr.RaceCode
		,cmmr.PartCRAFactorTypeCode
		,cmmr.FrailtyIndicator
		,cmmr.OriginalReasonforEntitlement
		,cmmr.LagIndicator
		,cmmr.EnrolledInPartAIndicator
		,cmmr.EnrolledInPartBIndicator
		,cmmr.EnrolledInPartCIndicator
		,cmmr.EnrolledInPartDIndicator
		,cmmr.FinalPartCStatus
		,cmmr.FinalPartDStatus
		,cmmr.DemographicPaymentAdjustmentRatePartA
		,cmmr.DemographicPaymentAdjustmentRatePartB
		,cmmr.RiskAdjusterPaymtAdjustmentRateA
		,cmmr.RiskAdjusterPaymtAdjustmentRateB
		,cmmr.RiskAdjusterPaymtAdjustmentRateAPlusRateB
		,cmmr.RiskAdjusterPaymtAdjustmentRateAPlusRateBSeq
		,cmmr.LISPremiumSubsidy
		,cmmr.PartCBasicPremiumPartAAmount
		,cmmr.PartCBasicPremiumPartBAmount
		,cmmr.PartCBasicPremiumPartAAmountPlusPartBAmout
		,cmmr.RebateCostshareA
		,cmmr.RebateCostshareB
		,cmmr.RebateforPartAPlusPartBCostSharingReduction
		,cmmr.RebateforPartAPlusPartBCostSharingReductionSeq
		,cmmr.RebateforOtherPartAMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartBMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartAPlusPartBMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartAPlusPartBMandatorySupplementalBenefitsSeq
		,cmmr.RebateforPartBPremiumReductionPartAAmount
		,cmmr.RebateforPartBPremiumReductionPartBAmount
		,cmmr.RebateforPartBPremiumReductionPartAPlusPartBAmount
		,cmmr.RebateforPartBPremiumReductionPartAPlusPartBAmountSeq
		,cmmr.RebateforPartDSupplementalBenefitsPartAAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartBAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartAPlusPartBAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartAPlusPartBAmountSeq
		,cmmr.TotalPartAPayment
		,cmmr.TotalPartBPayment
		,cmmr.TotalPartCPayment
		,cmmr.RebateForPartDBasicPremiumReduction
		,cmmr.RebateForPartDBasicPremiumReductionSeq
		,cmmr.PartDBasicPremiumAmount
		,cmmr.PartDDirectSubsidyPaymentAmount
		,cmmr.PartDDirectSubsidyPaymentAmountSeq
		,cmmr.ReinsuranceSubsidyAmount
		,cmmr.LowIncomeSubsidyCostSharingAmount
		,cmmr.TotalPartDPayment
		,cmmr.PacePremiumAddOn
		,cmmr.PaceCostSharingAddOn
		,cmmr.BeneficiaryDualandPartDEnrollmentStatusFlag
		,cmmr.PartCFrailtyScoreFactor
		,cmmr.MspFactor
		,cmmr.MspMemberMonths
		,cmmr.MspReductionAdjustmentAmountPartA
		,cmmr.MspReductionAdjustmentAmountPartB
		,cmmr.MspReductionAdjustmentPartAPlusPartBAmount
		,cmmr.MspReductionAdjustmentPartAPlusPartBAmountSeq
		,cmmr.MedicaidDualStatusCode
		,cmmr.GapDiscount
		,cmmr.GapDiscountSeq
		,cmmr.PdRafactype
		,cmmr.DefaultPdRa
		,cmmr.Finalmedicaidstatus
		,cmmr.Plantype
		,cmmr.PlanTypeSeparator
		,cmmr.BidNoRisk
		,cmmr.BidNoRiskSeq
		,cmmr.PartCCountyLevelPaymentRate
		,cmmr.PartCCountyLevelPaymentRateSeq
		,cmmr.RSPTCBIDMedicaidStatus
		,cmmr.BeneficiaryPartCDEGroup
		,cmmr.BeneficiaryPartCEsrdGroup
		,cmmr.BeneficiaryPartCMedicaidStatus
		,cmmr.BeneficiaryPartCDualStatus
		,cmmr.BeneficiaryPartCRiskScoreBaseUnnormalizedEDS
		,cmmr.BeneficiaryPartCRiskScoreProjUnnormalizedEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreProjNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreProjUnNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedRAPS
		,cmmr.BeneficiaryPartCRiskScoreBaseNormalizedForRAPS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedForRAPS
		,cmmr.BeneficiaryPartCRiskcohort
		,cmmr.BeneficiaryPartCFlag
		,cmmr.BeneficiaryPartCFrailtyMemberMonths
		,cmmr.PartDBeneficiaryFileBeneficiaryStatus
		,cmmr.PartDBeneficiaryFileEDSRiskScore
		,cmmr.PartDBeneficiaryFileRAPSRiskScore
		,cmmr.PartDBeneficiaryFileProjEdsRiskScore
		,cmmr.BeneficiaryFilePartDStatus
		,cmmr.BeneficiaryFilePartDFlag
		,cmmr.CMMRFileCreateDate
		,cmmr.ClientID
		,cmmr.LoadDateTime
		,cmmr.FileID
		,cmmr.FileLayoutID
		,cmmr.FileLayoutDescription
		,mg.SubscriberID
		,mg.GroupNumber
		,mg.GroupSuffix
        ,to_date(concat_ws("-",CAST(cmmr.EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(cmmr.EnrollmentMonth,3), "MMM"),to_timestamp(right(cmmr.EnrollmentMonth,3), "MMM"))) AS STRING),'01'), "yyyy-MM-dd") AS StartDate
        , mg.StartDate as MGSD
		,DENSE_RANK() OVER(ORDER BY cmmr.CMMRFileCreateDate DESC) AS RowNumber
FROM ConsolidatedCMMR cmmr 
LEFT JOIN MemberGroup mg 
 ON cmmr.BeneficiaryID = mg.BeneficiaryID 
 AND cmmr.PlanID = mg.CMSContractNumber
 AND to_date(concat_ws("-",CAST(cmmr.EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(cmmr.EnrollmentMonth,3), "MMM"),to_timestamp(right(cmmr.EnrollmentMonth,3), "MMM"))) AS STRING),'01'), "yyyy-MM-dd") = mg.StartDate 
 )
SELECT DISTINCT
	 PlanID
	,BeneficiaryID
	,BeneficiaryIDOriginal
	,MBIIndicator
	,EnrollmentMonth
    ,StartDate
    ,MGSD
	,EnrollmentYear
    ,EnrollmentYearMonth
	,Rundate
	,Lastname
	,FirstInitial
	,EnrollmentSource
	,PersonTotal
	,PlanBenefitPackage
	,NewPlanBenefitPackage
	,SegmentID
	,EghpFlag
	,RiskAdjusterFactorA
	,PartDRAFactor
	,Gendercode
	,DOB
	,Agegroup
	,AgedDisabledIdentifier
	,StateandCountyCode
	,OutOfAreaIndicator
	,Hospice
	,ESRD
	,AgedMsp
	,InstitutionalFlag
	,NHC
	,MedicaidBeneficiaryStatusFlag
	,MedicaidIndicator
	,CurrentMedicaidStatus
	,PartCDualStatusFlag
	,PartDDualStatusFlag
	,LTIFlag
	,PartDLowIncomeIndicator
	,PartDLongTermInstitutionalIndicator
	,PartCDefaultRiskFactorCode
	,ESRDMspFlag
	,RiskAdjusterAgeGroup
	,PreviousDisableRatio
	,DeMinimis
	,RaceCode
	,PartCRAFactorTypeCode
	,FrailtyIndicator
	,OriginalReasonforEntitlement
	,LagIndicator
	,EnrolledInPartAIndicator
	,EnrolledInPartBIndicator
	,EnrolledInPartCIndicator
	,EnrolledInPartDIndicator
	,FinalPartCStatus
	,FinalPartDStatus
	,DemographicPaymentAdjustmentRatePartA
	,DemographicPaymentAdjustmentRatePartB
	,RiskAdjusterPaymtAdjustmentRateA
	,RiskAdjusterPaymtAdjustmentRateB
	,RiskAdjusterPaymtAdjustmentRateAPlusRateB
	,RiskAdjusterPaymtAdjustmentRateAPlusRateBSeq
	,LISPremiumSubsidy
	,PartCBasicPremiumPartAAmount
	,PartCBasicPremiumPartBAmount
	,PartCBasicPremiumPartAAmountPlusPartBAmout
	,RebateCostshareA
	,RebateCostshareB
	,RebateforPartAPlusPartBCostSharingReduction
	,RebateforPartAPlusPartBCostSharingReductionSeq
	,RebateforOtherPartAMandatorySupplementalBenefits
	,RebateforOtherPartBMandatorySupplementalBenefits
	,RebateforOtherPartAPlusPartBMandatorySupplementalBenefits
	,RebateforOtherPartAPlusPartBMandatorySupplementalBenefitsSeq
	,RebateforPartBPremiumReductionPartAAmount
	,RebateforPartBPremiumReductionPartBAmount
	,RebateforPartBPremiumReductionPartAPlusPartBAmount
	,RebateforPartBPremiumReductionPartAPlusPartBAmountSeq
	,RebateforPartDSupplementalBenefitsPartAAmount
	,RebateforPartDSupplementalBenefitsPartBAmount
	,RebateforPartDSupplementalBenefitsPartAPlusPartBAmount
	,RebateforPartDSupplementalBenefitsPartAPlusPartBAmountSeq
	,TotalPartAPayment
	,TotalPartBPayment
	,TotalPartCPayment
	,RebateForPartDBasicPremiumReduction
	,RebateForPartDBasicPremiumReductionSeq
	,PartDBasicPremiumAmount
	,PartDDirectSubsidyPaymentAmount
	,PartDDirectSubsidyPaymentAmountSeq
	,ReinsuranceSubsidyAmount
	,LowIncomeSubsidyCostSharingAmount
	,TotalPartDPayment
	,PacePremiumAddOn
	,PaceCostSharingAddOn
	,BeneficiaryDualandPartDEnrollmentStatusFlag
	,PartCFrailtyScoreFactor
	,MspFactor
	,MspMemberMonths
	,MspReductionAdjustmentAmountPartA
	,MspReductionAdjustmentAmountPartB
	,MspReductionAdjustmentPartAPlusPartBAmount
	,MspReductionAdjustmentPartAPlusPartBAmountSeq
	,MedicaidDualStatusCode
	,GapDiscount
	,GapDiscountSeq
	,PdRafactype
	,DefaultPdRa
	,Finalmedicaidstatus
	,Plantype
	,PlanTypeSeparator
	,BidNoRisk
	,BidNoRiskSeq
	,PartCCountyLevelPaymentRate
	,PartCCountyLevelPaymentRateSeq
	,RSPTCBIDMedicaidStatus
	,BeneficiaryPartCDEGroup
	,BeneficiaryPartCEsrdGroup
	,BeneficiaryPartCMedicaidStatus
	,BeneficiaryPartCDualStatus
	,BeneficiaryPartCRiskScoreBaseUnnormalizedEDS
	,BeneficiaryPartCRiskScoreProjUnnormalizedEDS
	,BeneficiaryPartCRiskScoreBaseNormalizedForEDS
	,BeneficiaryPartCRiskScoreProjNormalizedForEDS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedForEDS
	,BeneficiaryPartCRiskScoreProjUnNormalizedForEDS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedRAPS
	,BeneficiaryPartCRiskScoreBaseNormalizedForRAPS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedForRAPS
	,BeneficiaryPartCRiskcohort
	,BeneficiaryPartCFlag
	,BeneficiaryPartCFrailtyMemberMonths
	,PartDBeneficiaryFileBeneficiaryStatus
	,PartDBeneficiaryFileEDSRiskScore
	,PartDBeneficiaryFileRAPSRiskScore
	,PartDBeneficiaryFileProjEdsRiskScore
	,BeneficiaryFilePartDStatus
	,BeneficiaryFilePartDFlag
	,CMMRFileCreateDate
	,ClientID
	,LoadDateTime
	,FileID
	,FileLayoutID
	,FileLayoutDescription
	,SubscriberID
	,GroupNumber
	,GroupSuffix
 FROM gcmmr 
 WHERE RowNumber = 1
 """

# COMMAND ----------

findLastYear = """
select  cmmr.PlanID
		,cmmr.BeneficiaryID
		,cmmr.BeneficiaryIDOriginal
		,cmmr.MBIIndicator      
		,cmmr.EnrollmentMonth
		,cmmr.EnrollmentYear
        ,cmmr.EnrollmentYearMonth
		,cmmr.Rundate
		,cmmr.Lastname
		,cmmr.FirstInitial
		,cmmr.EnrollmentSource
		,cmmr.PersonTotal
		,cmmr.PlanBenefitPackage
		,cmmr.NewPlanBenefitPackage
		,cmmr.SegmentID
		,cmmr.EghpFlag
		,cmmr.RiskAdjusterFactorA
		,cmmr.PartDRAFactor
		,cmmr.Gendercode
		,cmmr.DOB
		,cmmr.Agegroup
		,cmmr.AgedDisabledIdentifier
		,cmmr.StateandCountyCode
		,cmmr.OutOfAreaIndicator
		,cmmr.Hospice
		,cmmr.ESRD
		,cmmr.AgedMsp
		,cmmr.InstitutionalFlag
		,cmmr.NHC
		,cmmr.MedicaidBeneficiaryStatusFlag
		,cmmr.MedicaidIndicator
		,cmmr.CurrentMedicaidStatus
		,cmmr.PartCDualStatusFlag
		,cmmr.PartDDualStatusFlag
		,cmmr.LTIFlag
		,cmmr.PartDLowIncomeIndicator
		,cmmr.PartDLongTermInstitutionalIndicator
		,cmmr.PartCDefaultRiskFactorCode
		,cmmr.ESRDMspFlag
		,cmmr.RiskAdjusterAgeGroup
		,cmmr.PreviousDisableRatio
		,cmmr.DeMinimis
		,cmmr.RaceCode
		,cmmr.PartCRAFactorTypeCode
		,cmmr.FrailtyIndicator
		,cmmr.OriginalReasonforEntitlement
		,cmmr.LagIndicator
		,cmmr.EnrolledInPartAIndicator
		,cmmr.EnrolledInPartBIndicator
		,cmmr.EnrolledInPartCIndicator
		,cmmr.EnrolledInPartDIndicator
		,cmmr.FinalPartCStatus
		,cmmr.FinalPartDStatus
		,cmmr.DemographicPaymentAdjustmentRatePartA
		,cmmr.DemographicPaymentAdjustmentRatePartB
		,cmmr.RiskAdjusterPaymtAdjustmentRateA
		,cmmr.RiskAdjusterPaymtAdjustmentRateB
		,cmmr.RiskAdjusterPaymtAdjustmentRateAPlusRateB
		,cmmr.RiskAdjusterPaymtAdjustmentRateAPlusRateBSeq
		,cmmr.LISPremiumSubsidy
		,cmmr.PartCBasicPremiumPartAAmount
		,cmmr.PartCBasicPremiumPartBAmount
		,cmmr.PartCBasicPremiumPartAAmountPlusPartBAmout
		,cmmr.RebateCostshareA
		,cmmr.RebateCostshareB
		,cmmr.RebateforPartAPlusPartBCostSharingReduction
		,cmmr.RebateforPartAPlusPartBCostSharingReductionSeq
		,cmmr.RebateforOtherPartAMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartBMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartAPlusPartBMandatorySupplementalBenefits
		,cmmr.RebateforOtherPartAPlusPartBMandatorySupplementalBenefitsSeq
		,cmmr.RebateforPartBPremiumReductionPartAAmount
		,cmmr.RebateforPartBPremiumReductionPartBAmount
		,cmmr.RebateforPartBPremiumReductionPartAPlusPartBAmount
		,cmmr.RebateforPartBPremiumReductionPartAPlusPartBAmountSeq
		,cmmr.RebateforPartDSupplementalBenefitsPartAAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartBAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartAPlusPartBAmount
		,cmmr.RebateforPartDSupplementalBenefitsPartAPlusPartBAmountSeq
		,cmmr.TotalPartAPayment
		,cmmr.TotalPartBPayment
		,cmmr.TotalPartCPayment
		,cmmr.RebateForPartDBasicPremiumReduction
		,cmmr.RebateForPartDBasicPremiumReductionSeq
		,cmmr.PartDBasicPremiumAmount
		,cmmr.PartDDirectSubsidyPaymentAmount
		,cmmr.PartDDirectSubsidyPaymentAmountSeq
		,cmmr.ReinsuranceSubsidyAmount
		,cmmr.LowIncomeSubsidyCostSharingAmount
		,cmmr.TotalPartDPayment
		,cmmr.PacePremiumAddOn
		,cmmr.PaceCostSharingAddOn
		,cmmr.BeneficiaryDualandPartDEnrollmentStatusFlag
		,cmmr.PartCFrailtyScoreFactor
		,cmmr.MspFactor
		,cmmr.MspMemberMonths
		,cmmr.MspReductionAdjustmentAmountPartA
		,cmmr.MspReductionAdjustmentAmountPartB
		,cmmr.MspReductionAdjustmentPartAPlusPartBAmount
		,cmmr.MspReductionAdjustmentPartAPlusPartBAmountSeq
		,cmmr.MedicaidDualStatusCode
		,cmmr.GapDiscount
		,cmmr.GapDiscountSeq
		,cmmr.PdRafactype
		,cmmr.DefaultPdRa
		,cmmr.Finalmedicaidstatus
		,cmmr.Plantype
		,cmmr.PlanTypeSeparator
		,cmmr.BidNoRisk
		,cmmr.BidNoRiskSeq
		,cmmr.PartCCountyLevelPaymentRate
		,cmmr.PartCCountyLevelPaymentRateSeq
		,cmmr.RSPTCBIDMedicaidStatus
		,cmmr.BeneficiaryPartCDEGroup
		,cmmr.BeneficiaryPartCEsrdGroup
		,cmmr.BeneficiaryPartCMedicaidStatus
		,cmmr.BeneficiaryPartCDualStatus
		,cmmr.BeneficiaryPartCRiskScoreBaseUnnormalizedEDS
		,cmmr.BeneficiaryPartCRiskScoreProjUnnormalizedEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreProjNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreProjUnNormalizedForEDS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedRAPS
		,cmmr.BeneficiaryPartCRiskScoreBaseNormalizedForRAPS
		,cmmr.BeneficiaryPartCRiskScoreBaseUnNormalizedForRAPS
		,cmmr.BeneficiaryPartCRiskcohort
		,cmmr.BeneficiaryPartCFlag
		,cmmr.BeneficiaryPartCFrailtyMemberMonths
		,cmmr.PartDBeneficiaryFileBeneficiaryStatus
		,cmmr.PartDBeneficiaryFileEDSRiskScore
		,cmmr.PartDBeneficiaryFileRAPSRiskScore
		,cmmr.PartDBeneficiaryFileProjEdsRiskScore
		,cmmr.BeneficiaryFilePartDStatus
		,cmmr.BeneficiaryFilePartDFlag
		,cmmr.CMMRFileCreateDate
		,cmmr.ClientID
		,cmmr.LoadDateTime
		,cmmr.FileID
		,cmmr.FileLayoutID
		,cmmr.FileLayoutDescription
        ,cmmr.StartDate
        ,cmmr.MGSD
        ,cmmr.SidPrev
        ,cmmr.GnPrev
        ,cmmr.GsPrev
		,mg.SubscriberID
		,mg.GroupNumber
		,mg.GroupSuffix 
        ,mg.StartDate as LastYearDate from dfCmmrGoldRaw cmmr
left join MemberGroup mg
ON cmmr.BeneficiaryID = mg.BeneficiaryID 
 AND cmmr.PlanID = mg.CMSContractNumber
 AND (cmmr.SidPrev is null and GnPrev is null and GsPrev is null)
 and (cmmr.EnrollmentYear >= YEAR(mg.StartDate) and to_date(concat_ws("-",CAST(cmmr.EnrollmentYear AS STRING),CAST(MONTH(ifnull(to_timestamp(left(cmmr.EnrollmentMonth,3), "MMM"),to_timestamp(right(cmmr.EnrollmentMonth,3), "MMM"))) AS STRING),'01'), "yyyy-MM-dd") > mg.StartDate)

"""

# COMMAND ----------

finalData = """
-- cannot find in the same year, will look for last years
select * from 
(select cmmr.*, rank() OVER(partition by cmmr.PlanID, cmmr.BeneficiaryID ORDER BY cmmr.LastYearDate DESC) AS RowNumber
from dfCmmrGold as cmmr
where LastYearDate is not null) 
where RowNumber = 1
union 
-- same year already find member group info  
select *, 1 As RowNumber from dfCmmrGold
where LastYearDate is null
and (SidPrev is not null or GnPrev is not null or GsPrev is not null) 
union
-- not matched
select *, 1 As RowNumber from dfCmmrGold
where LastYearDate is null
and (SidPrev is null and GnPrev is null and GsPrev is null and SubscriberID is null and GroupNumber is null and GroupSuffix is null)
"""

# COMMAND ----------

populateAll = """
SELECT DISTINCT
	 PlanID
	,BeneficiaryID
	,BeneficiaryIDOriginal
	,MBIIndicator
	,EnrollmentMonth
	,EnrollmentYear
    ,EnrollmentYearMonth
	,Rundate
	,Lastname
	,FirstInitial
	,EnrollmentSource
	,PersonTotal
	,PlanBenefitPackage
	,NewPlanBenefitPackage
	,SegmentID
	,EghpFlag
	,RiskAdjusterFactorA
	,PartDRAFactor
	,Gendercode
	,DOB
	,Agegroup
	,AgedDisabledIdentifier
	,StateandCountyCode
	,OutOfAreaIndicator
	,Hospice
	,ESRD
	,AgedMsp
	,InstitutionalFlag
	,NHC
	,MedicaidBeneficiaryStatusFlag
	,MedicaidIndicator
	,CurrentMedicaidStatus
	,PartCDualStatusFlag
	,PartDDualStatusFlag
	,LTIFlag
	,PartDLowIncomeIndicator
	,PartDLongTermInstitutionalIndicator
	,PartCDefaultRiskFactorCode
	,ESRDMspFlag
	,RiskAdjusterAgeGroup
	,PreviousDisableRatio
	,DeMinimis
	,RaceCode
	,PartCRAFactorTypeCode
	,FrailtyIndicator
	,OriginalReasonforEntitlement
	,LagIndicator
	,EnrolledInPartAIndicator
	,EnrolledInPartBIndicator
	,EnrolledInPartCIndicator
	,EnrolledInPartDIndicator
	,FinalPartCStatus
	,FinalPartDStatus
	,DemographicPaymentAdjustmentRatePartA
	,DemographicPaymentAdjustmentRatePartB
	,RiskAdjusterPaymtAdjustmentRateA
	,RiskAdjusterPaymtAdjustmentRateB
	,RiskAdjusterPaymtAdjustmentRateAPlusRateB
	,RiskAdjusterPaymtAdjustmentRateAPlusRateBSeq
	,LISPremiumSubsidy
	,PartCBasicPremiumPartAAmount
	,PartCBasicPremiumPartBAmount
	,PartCBasicPremiumPartAAmountPlusPartBAmout
	,RebateCostshareA
	,RebateCostshareB
	,RebateforPartAPlusPartBCostSharingReduction
	,RebateforPartAPlusPartBCostSharingReductionSeq
	,RebateforOtherPartAMandatorySupplementalBenefits
	,RebateforOtherPartBMandatorySupplementalBenefits
	,RebateforOtherPartAPlusPartBMandatorySupplementalBenefits
	,RebateforOtherPartAPlusPartBMandatorySupplementalBenefitsSeq
	,RebateforPartBPremiumReductionPartAAmount
	,RebateforPartBPremiumReductionPartBAmount
	,RebateforPartBPremiumReductionPartAPlusPartBAmount
	,RebateforPartBPremiumReductionPartAPlusPartBAmountSeq
	,RebateforPartDSupplementalBenefitsPartAAmount
	,RebateforPartDSupplementalBenefitsPartBAmount
	,RebateforPartDSupplementalBenefitsPartAPlusPartBAmount
	,RebateforPartDSupplementalBenefitsPartAPlusPartBAmountSeq
	,TotalPartAPayment
	,TotalPartBPayment
	,TotalPartCPayment
	,RebateForPartDBasicPremiumReduction
	,RebateForPartDBasicPremiumReductionSeq
	,PartDBasicPremiumAmount
	,PartDDirectSubsidyPaymentAmount
	,PartDDirectSubsidyPaymentAmountSeq
	,ReinsuranceSubsidyAmount
	,LowIncomeSubsidyCostSharingAmount
	,TotalPartDPayment
	,PacePremiumAddOn
	,PaceCostSharingAddOn
	,BeneficiaryDualandPartDEnrollmentStatusFlag
	,PartCFrailtyScoreFactor
	,MspFactor
	,MspMemberMonths
	,MspReductionAdjustmentAmountPartA
	,MspReductionAdjustmentAmountPartB
	,MspReductionAdjustmentPartAPlusPartBAmount
	,MspReductionAdjustmentPartAPlusPartBAmountSeq
	,MedicaidDualStatusCode
	,GapDiscount
	,GapDiscountSeq
	,PdRafactype
	,DefaultPdRa
	,Finalmedicaidstatus
	,Plantype
	,PlanTypeSeparator
	,BidNoRisk
	,BidNoRiskSeq
	,PartCCountyLevelPaymentRate
	,PartCCountyLevelPaymentRateSeq
	,RSPTCBIDMedicaidStatus
	,BeneficiaryPartCDEGroup
	,BeneficiaryPartCEsrdGroup
	,BeneficiaryPartCMedicaidStatus
	,BeneficiaryPartCDualStatus
	,BeneficiaryPartCRiskScoreBaseUnnormalizedEDS
	,BeneficiaryPartCRiskScoreProjUnnormalizedEDS
	,BeneficiaryPartCRiskScoreBaseNormalizedForEDS
	,BeneficiaryPartCRiskScoreProjNormalizedForEDS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedForEDS
	,BeneficiaryPartCRiskScoreProjUnNormalizedForEDS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedRAPS
	,BeneficiaryPartCRiskScoreBaseNormalizedForRAPS
	,BeneficiaryPartCRiskScoreBaseUnNormalizedForRAPS
	,BeneficiaryPartCRiskcohort
	,BeneficiaryPartCFlag
	,BeneficiaryPartCFrailtyMemberMonths
	,PartDBeneficiaryFileBeneficiaryStatus
	,PartDBeneficiaryFileEDSRiskScore
	,PartDBeneficiaryFileRAPSRiskScore
	,PartDBeneficiaryFileProjEdsRiskScore
	,BeneficiaryFilePartDStatus
	,BeneficiaryFilePartDFlag
	,CMMRFileCreateDate
	,ClientID
	,LoadDateTime
	,FileID
	,FileLayoutID
	,FileLayoutDescription
	,coalesce(SubscriberID, SidPrev) as SubscriberID
    ,coalesce(GroupNumber, GnPrev) as GroupNumber
	,coalesce(GroupSuffix, GsPrev) as GroupSuffix
From dfCmmrGoldFinal
"""

# COMMAND ----------

# DBTITLE 1,Get Source Data
from delta.tables import *
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# check if source file path exists
if path_exists(cmmrConsolidatedPath) and path_exists(memberGroupPath):
#   read source data
  dfMemberGroup = spark.read.format("delta").load(memberGroupPath)
  dfCmmr = spark.read.format("delta").load(cmmrConsolidatedPath)
  
  dfMemberGroup.createOrReplaceTempView("MemberGroup")
  dfCmmr.createOrReplaceTempView("ConsolidatedCMMR")
  
#   get the source joined data   
  dfCmmrGoldRaw = spark.sql(sqlStmt)
  
#   find the latest SubscriberId, GroupNumber and GroupSuffix if no month span found in MemberGroup gold table in  the same year 
  overCols = Window.partitionBy(col("BeneficiaryID"), col("PlanID")).orderBy(col("StartDate"))
  
#  If find any member in the same year, then SidPrev, GnPRev or GsPRev will be populated
  dfCmmrGoldRaw = dfCmmrGoldRaw.withColumn("SidPrev", when(col("SubscriberID").isNotNull(), col("SubscriberID")).otherwise(last("SubscriberID", True).over(overCols))) \
        .withColumn("GnPrev", when(col("GroupNumber").isNotNull(), col("GroupNumber")).otherwise(last("GroupNumber", True).over(overCols))) \
        .withColumn("GsPrev", when(col("GroupSuffix").isNotNull(), col("GroupSuffix")).otherwise(last("GroupSuffix", True).over(overCols)))
  dfCmmrGoldRaw.createOrReplaceTempView("dfCmmrGoldRaw")
  
#   find group info from latest years if cannot populate SidPrev, GnPRev or GsPRev
  dfCmmrGold = spark.sql(findLastYear)
  dfCmmrGold.createOrReplaceTempView("dfCmmrGold")
  
#   find the final data to comebine same year and latest in last years
  dfCmmrGoldFinal = spark.sql(finalData)
  dfCmmrGoldFinal.createOrReplaceTempView("dfCmmrGoldFinal")
  
#   populate all the SubscriberID, GroupNumber, GroupSuffix 
  dfCmmrGoldSource = spark.sql(populateAll)
  
  if path_exists(cmmrGoldPath):
    # wipe the delta data and then write the final df into gold table
    files = dbutils.fs.ls(cmmrGoldPath)
    for f in files:
      dbutils.fs.rm(f.path, recurse=True)
    dbutils.fs.rm(cmmrGoldPath)
    
    dfCmmrGoldSource.write.format("delta").save(cmmrGoldPath)
  else:
  #   just write into gold delta table
    dfCmmrGoldSource.write.format("delta").save(cmmrGoldPath)

