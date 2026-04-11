CREATE TABLE [devidap1].[ConsolidatedMMR] ( 
	 [PlanID]	VARCHAR(5)	NULL	
	,[BeneficiaryID]	VARCHAR(12)	NULL	
	,[BeneficiaryIDOriginal]	VARCHAR(12)	NULL	
	,[MBIIndicator]	VARCHAR(1)	NULL	
	,[EnrollmentMonth]	VARCHAR(8)	NULL	
	,[EnrollmentYear]	VARCHAR(8)	NULL
	,[EnrollmentYearMonth]	VARCHAR(8)	NULL
	,[Rundate]	DATE	NULL	
	,[Lastname]	VARCHAR(25)	NULL	
	,[FirstInitial]	VARCHAR(1)	NULL	
	,[EnrollmentSource]	VARCHAR(1)	NULL	
	,[PersonTotal]	VARCHAR (255)	NULL	
	,[PlanBenefitPackage]	VARCHAR(3)	NULL	
	,[NewPlanBenefitPackage]	VARCHAR(3)	NULL	
	,[SegmentID]	VARCHAR(3)	NULL	
	,[EghpFlag]	VARCHAR(1)	NULL	
	,[RiskAdjusterFactorA]	VARCHAR (20)	NULL	
	,[PartDRAFactor]	VARCHAR(7)	NULL	
	,[Gendercode]	VARCHAR(1)	NULL	
	,[DOB]	DATE	NULL	
	,[Agegroup]	VARCHAR(4)	NULL	
	,[AgedDisabledIdentifier]	VARCHAR(4)	NULL	
	,[StateandCountyCode]	VARCHAR(5)	NULL	
	,[OutOfAreaIndicator]	VARCHAR(1)	NULL	
	,[Hospice]	VARCHAR(1)	NULL	
	,[ESRD]	VARCHAR(1)	NULL	
	,[AgedMsp]	VARCHAR(1)	NULL	
	,[InstitutionalFlag]	VARCHAR(1)	NULL	
	,[NHC]	VARCHAR(1)	NULL	
	,[MedicaidBeneficiaryStatusFlag]	VARCHAR(1)	NULL	
	,[MedicaidIndicator]	VARCHAR(1)	NULL	
	,[CurrentMedicaidStatus]	VARCHAR(1)	NULL	
	,[PartCDualStatusFlag]	VARCHAR(16)	NULL	
	,[PartDDualStatusFlag]	VARCHAR(16)	NULL	
	,[LTIFlag]	VARCHAR(1)	NULL	
	,[PartDLowIncomeIndicator]	VARCHAR(1)	NULL	
	,[PartDLongTermInstitutionalIndicator]	VARCHAR(1)	NULL	
	,[PartCDefaultRiskFactorCode]	VARCHAR(2)	NULL	
	,[ESRDMspFlag]	VARCHAR(1)	NULL	
	,[RiskAdjusterAgeGroup]	VARCHAR(4)	NULL	
	,[PreviousDisableRatio]	VARCHAR(8)	NULL	
	,[DeMinimis]	VARCHAR(1)	NULL	
	,[RaceCode]	VARCHAR(1)	NULL	
	,[PartCRAFactorTypeCode]	VARCHAR(2)	NULL	
	,[FrailtyIndicator]	VARCHAR(1)	NULL	
	,[OriginalReasonforEntitlement]	VARCHAR(1)	NULL	
	,[LagIndicator]	VARCHAR(1)	NULL	
	,[EnrolledInPartAIndicator]	VARCHAR(1)	NULL	
	,[EnrolledInPartBIndicator]	VARCHAR(1)	NULL	
	,[EnrolledInPartCIndicator]	VARCHAR(1)	NULL	
	,[EnrolledInPartDIndicator]	VARCHAR(1)	NULL	
	,[FinalPartCStatus]	VARCHAR(50)	NULL	
	,[FinalPartDStatus]	VARCHAR(50)	NULL	
	,[DemographicPaymentAdjustmentRatePartA]	VARCHAR(20)	NULL	
	,[DemographicPaymentAdjustmentRatePartB]	VARCHAR(20)	NULL	
	,[RiskAdjusterPaymtAdjustmentRateA]	VARCHAR(20)	NULL	
	,[RiskAdjusterPaymtAdjustmentRateB]	VARCHAR(20)	NULL	
	,[RiskAdjusterPaymtAdjustmentRateAPlusRateB]	VARCHAR(20)	NULL	
	,[RiskAdjusterPaymtAdjustmentRateAPlusRateBSeq]	VARCHAR(20)	NULL	
	,[LISPremiumSubsidy]	VARCHAR (20)	NULL	
	,[PartCBasicPremiumPartAAmount]	VARCHAR (20)	NULL	
	,[PartCBasicPremiumPartBAmount]	VARCHAR (20)	NULL	
	,[PartCBasicPremiumPartAAmountPlusPartBAmout]	VARCHAR (20)	NULL	
	,[RebateCostshareA]	VARCHAR (20)	NULL	
	,[RebateCostshareB]	VARCHAR (20)	NULL	
	,[RebateforPartAPlusPartBCostSharingReduction]	VARCHAR (20)	NULL	
	,[RebateforPartAPlusPartBCostSharingReductionSeq]	VARCHAR (20)	NULL	
	,[RebateforOtherPartAMandatorySupplementalBenefits]	VARCHAR (20)	NULL	
	,[RebateforOtherPartBMandatorySupplementalBenefits]	VARCHAR (20)	NULL	
	,[RebateforOtherPartAPlusPartBMandatorySupplementalBenefits]	VARCHAR (20)	NULL	
	,[RebateforOtherPartAPlusPartBMandatorySupplementalBenefitsSeq]	VARCHAR (20)	NULL	
	,[RebateforPartBPremiumReductionPartAAmount]	VARCHAR (20)	NULL	
	,[RebateforPartBPremiumReductionPartBAmount]	VARCHAR (20)	NULL	
	,[RebateforPartBPremiumReductionPartAPlusPartBAmount]	VARCHAR (20)	NULL	
	,[RebateforPartBPremiumReductionPartAPlusPartBAmountSeq]	VARCHAR (20)	NULL	
	,[RebateforPartDSupplementalBenefitsPartAAmount]	VARCHAR (20)	NULL	
	,[RebateforPartDSupplementalBenefitsPartBAmount]	VARCHAR (20)	NULL	
	,[RebateforPartDSupplementalBenefitsPartAPlusPartBAmount]	VARCHAR (20)	NULL	
	,[RebateforPartDSupplementalBenefitsPartAPlusPartBAmountSeq]	VARCHAR (20)	NULL	
	,[TotalPartAPayment]	VARCHAR (20)	NULL	
	,[TotalPartBPayment]	VARCHAR (20)	NULL	
	,[TotalPartCPayment]	VARCHAR (20)	NULL	
	,[RebateForPartDBasicPremiumReduction]	VARCHAR (20)	NULL	
	,[RebateForPartDBasicPremiumReductionSeq]	VARCHAR (20)	NULL	
	,[PartDBasicPremiumAmount]	VARCHAR (20)	NULL	
	,[PartDDirectSubsidyPaymentAmount]	VARCHAR (20)	NULL	
	,[PartDDirectSubsidyPaymentAmountSeq]	VARCHAR (20)	NULL	
	,[ReinsuranceSubsidyAmount]	VARCHAR (20)	NULL	
	,[LowIncomeSubsidyCostSharingAmount]	VARCHAR (20)	NULL	
	,[TotalPartDPayment]	VARCHAR (20)	NULL	
	,[PacePremiumAddOn]	VARCHAR (20)	NULL	
	,[PaceCostSharingAddOn]	VARCHAR (20)	NULL	
	,[BeneficiaryDualandPartDEnrollmentStatusFlag]	VARCHAR(1)	NULL	
	,[PartCFrailtyScoreFactor]	VARCHAR(1)	NULL	
	,[MspFactor]	VARCHAR(7)	NULL	
	,[MspMemberMonths]	VARCHAR(8)	NULL	
	,[MspReductionAdjustmentAmountPartA]	VARCHAR(20)	NULL	
	,[MspReductionAdjustmentAmountPartB]	VARCHAR(20)	NULL	
	,[MspReductionAdjustmentPartAPlusPartBAmount]	VARCHAR(20)	NULL	
	,[MspReductionAdjustmentPartAPlusPartBAmountSeq]	VARCHAR(20)	NULL	
	,[MedicaidDualStatusCode]	VARCHAR(2)	NULL	
	,[GapDiscount]	VARCHAR (20)	NULL	
	,[GapDiscountSeq]	VARCHAR (20)	NULL	
	,[PdRafactype]	VARCHAR(2)	NULL	
	,[DefaultPdRa]	VARCHAR(1)	NULL	
	,[Finalmedicaidstatus]	VARCHAR(2)	NULL	
	,[Plantype]	VARCHAR(10)	NULL	
	,[PlanTypeSeparator]	VARCHAR(20)	NULL	
	,[BidNoRisk]	VARCHAR(20)	NULL	
	,[BidNoRiskSeq]	VARCHAR(20)	NULL	
	,[PartCCountyLevelPaymentRate]	VARCHAR(20)	NULL	
	,[PartCCountyLevelPaymentRateSeq]	VARCHAR(20)	NULL	
	,[RSPTCBIDMedicaidStatus]	VARCHAR(2)	NULL	
	,[BeneficiaryPartCDEGroup]	VARCHAR(40)	NULL	
	,[BeneficiaryPartCEsrdGroup]	VARCHAR(40)	NULL	
	,[BeneficiaryPartCMedicaidStatus]	VARCHAR(40)	NULL	
	,[BeneficiaryPartCDualStatus]	VARCHAR(50)	NULL	
	,[BeneficiaryPartCRiskScoreBaseUnnormalizedEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreProjUnnormalizedEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreBaseNormalizedForEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreProjNormalizedForEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreBaseUnNormalizedForEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreProjUnNormalizedForEDS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreBaseUnNormalizedRAPS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreBaseNormalizedForRAPS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskScoreBaseUnNormalizedForRAPS]	VARCHAR(30)	NULL	
	,[BeneficiaryPartCRiskcohort]	VARCHAR(40)	NULL	
	,[BeneficiaryPartCFlag]	VARCHAR(3)	NULL	
	,[BeneficiaryPartCFrailtyMemberMonths]	VARCHAR(10)	NULL	
	,[PartDBeneficiaryFileBeneficiaryStatus]	VARCHAR(100)	NULL	
	,[PartDBeneficiaryFileEDSRiskScore]	VARCHAR(20)	NULL	
	,[PartDBeneficiaryFileRAPSRiskScore]	VARCHAR(20)	NULL	
	,[PartDBeneficiaryFileProjEdsRiskScore]	VARCHAR(20)	NULL	
	,[BeneficiaryFilePartDStatus]	VARCHAR(33)	NULL	
	,[BeneficiaryFilePartDFlag]	VARCHAR(3)	NULL	
	,[Groupnumber]	VARCHAR(10)	NULL	
	,[GroupSuffix]	VARCHAR(10)	NULL
	,[CMMRFileCreateDate] DATE NULL
	,[LoadDateTime]	DATETIME2(7)	NOT NULL DEFAULT	'0001-01-01 00:00:00'
	,[FileID]	BIGINT	NOT NULL	
	,[ClientID]	VARCHAR(20)	NOT NULL	
	,[FileLayoutID]	INTEGER	NOT NULL	
	,[FileLayoutDescription]	VARCHAR(255)	NOT NULL	
)