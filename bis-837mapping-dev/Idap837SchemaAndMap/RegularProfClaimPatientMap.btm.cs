namespace Idap837SchemaAndMap {
    
    
    [Microsoft.XLANGs.BaseTypes.SchemaReference(@"Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P", typeof(global::Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P))]
    [Microsoft.XLANGs.BaseTypes.SchemaReference(@"Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema", typeof(global::Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema))]
    public sealed class RegularProfClaimPatientMap : global::Microsoft.XLANGs.BaseTypes.TransformBase {
        
        private const string _strMap = @"<?xml version=""1.0"" encoding=""UTF-16""?>
<xsl:stylesheet xmlns:xsl=""http://www.w3.org/1999/XSL/Transform"" xmlns:msxsl=""urn:schemas-microsoft-com:xslt"" xmlns:var=""http://schemas.microsoft.com/BizTalk/2003/var"" exclude-result-prefixes=""msxsl var s0 s1 s2 userCSharp"" version=""1.0"" xmlns:s0=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent"" xmlns:s2=""http://schemas.microsoft.com/BizTalk/2003/aggschema"" xmlns:s1=""http://schemas.microsoft.com/BizTalk/EDI/X12/2006"" xmlns:ns0=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfessionalClaim"" xmlns:userCSharp=""http://schemas.microsoft.com/BizTalk/2003/userCSharp"">
  <xsl:output omit-xml-declaration=""yes"" method=""xml"" version=""1.0"" />
  <xsl:template match=""/"">
    <xsl:apply-templates select=""/s2:Root"" />
  </xsl:template>
  <xsl:template match=""/s2:Root"">
    <xsl:variable name=""var:v1"" select=""count(/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2400_Loop1/s1:LX_ServiceLineNumber_2/LX01_AssignedNumber)"" />
    <xsl:variable name=""var:v9"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_MedicalRecordNumber_2))"" />
    <xsl:variable name=""var:v11"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text()) , &quot;EI&quot;)"" />
    <xsl:variable name=""var:v12"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text())"" />
    <xsl:variable name=""var:v14"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3/REF01_ReferenceIdentificationQualifier/text()) , &quot;G2&quot;)"" />
    <xsl:variable name=""var:v16"" select=""userCSharp:StringUpperCase(&quot;        &quot;)"" />
    <xsl:variable name=""var:v17"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM108_IdentificationCodeQualifier/text()) , &quot;XV&quot;)"" />
    <xsl:variable name=""var:v19"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber))"" />
    <xsl:variable name=""var:v21"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_RepricerReceivedDate_2))"" />
    <xsl:variable name=""var:v23"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3))"" />
    <xsl:variable name=""var:v25"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text())"" />
    <xsl:variable name=""var:v28"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2))"" />
    <xsl:variable name=""var:v34"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress))"" />
    <xsl:variable name=""var:v35"" select=""userCSharp:StringSize(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N301_PatientAddressLine/text()))"" />
    <xsl:variable name=""var:v37"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N301_PatientAddressLine/text())"" />
    <xsl:variable name=""var:v39"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress)"" />
    <xsl:variable name=""var:v40"" select=""userCSharp:LogicalExistence($var:v39)"" />
    <xsl:variable name=""var:v41"" select=""userCSharp:StringSize($var:v37)"" />
    <xsl:variable name=""var:v44"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode))"" />
    <xsl:variable name=""var:v45"" select=""userCSharp:StringSize(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N401_PatientCityName/text()))"" />
    <xsl:variable name=""var:v47"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N401_PatientCityName/text())"" />
    <xsl:variable name=""var:v49"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode)"" />
    <xsl:variable name=""var:v50"" select=""userCSharp:LogicalExistence($var:v49)"" />
    <xsl:variable name=""var:v51"" select=""userCSharp:StringSize($var:v47)"" />
    <xsl:variable name=""var:v56"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2))"" />
    <xsl:variable name=""var:v58"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2)"" />
    <xsl:variable name=""var:v59"" select=""userCSharp:LogicalExistence($var:v58)"" />
    <xsl:variable name=""var:v60"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02401_RelatedCausesCode/text())"" />
    <xsl:variable name=""var:v61"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02402_RelatedCausesCode/text())"" />
    <xsl:variable name=""var:v62"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02403_Related_CausesCode/text())"" />
    <xsl:variable name=""var:v65"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_OnsetofCurrentIllnessorSymptom_2))"" />
    <xsl:variable name=""var:v66"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastMenstrualPeriod_2))"" />
    <xsl:variable name=""var:v68"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2))"" />
    <xsl:variable name=""var:v70"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2)"" />
    <xsl:variable name=""var:v71"" select=""userCSharp:LogicalExistence($var:v70)"" />
    <xsl:variable name=""var:v72"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP01_DateTimeQualifier/text())"" />
    <xsl:variable name=""var:v73"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP02_DateTimePeriodFormatQualifier/text())"" />
    <xsl:variable name=""var:v74"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP03_DisabilityFromDate/text())"" />
    <xsl:variable name=""var:v76"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Admission_2))"" />
    <xsl:variable name=""var:v78"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Discharge_2))"" />
    <xsl:variable name=""var:v80"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM10_PatientSignatureSourceCode))"" />
    <xsl:variable name=""var:v82"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_37/C02201_DiagnosisTypeCode/text())"" />
    <xsl:variable name=""var:v85"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_InitialTreatmentDate_3))"" />
    <xsl:variable name=""var:v86"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastSeenDate_3))"" />
    <xsl:variable name=""var:v87"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AcuteManifestation_2))"" />
    <xsl:variable name=""var:v88"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2))"" />
    <xsl:variable name=""var:v89"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3))"" />
    <xsl:variable name=""var:v90"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_HearingandVisionPrescriptionDate_2))"" />
    <xsl:variable name=""var:v91"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AssumedandRelinquishedCareDates_2_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates_2))"" />
    <xsl:variable name=""var:v92"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_PropertyandCasualtyDateofFirstContact_2))"" />
    <xsl:variable name=""var:v94"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_InitialTreatmentDate_3)"" />
    <xsl:variable name=""var:v95"" select=""userCSharp:LogicalExistence($var:v94)"" />
    <xsl:variable name=""var:v96"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastSeenDate_3)"" />
    <xsl:variable name=""var:v97"" select=""userCSharp:LogicalExistence($var:v96)"" />
    <xsl:variable name=""var:v98"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AcuteManifestation_2)"" />
    <xsl:variable name=""var:v99"" select=""userCSharp:LogicalExistence($var:v98)"" />
    <xsl:variable name=""var:v100"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2)"" />
    <xsl:variable name=""var:v101"" select=""userCSharp:LogicalExistence($var:v100)"" />
    <xsl:variable name=""var:v102"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3)"" />
    <xsl:variable name=""var:v103"" select=""userCSharp:LogicalExistence($var:v102)"" />
    <xsl:variable name=""var:v104"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_HearingandVisionPrescriptionDate_2)"" />
    <xsl:variable name=""var:v105"" select=""userCSharp:LogicalExistence($var:v104)"" />
    <xsl:variable name=""var:v106"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AssumedandRelinquishedCareDates_2_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates_2)"" />
    <xsl:variable name=""var:v107"" select=""userCSharp:LogicalExistence($var:v106)"" />
    <xsl:variable name=""var:v108"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_PropertyandCasualtyDateofFirstContact_2)"" />
    <xsl:variable name=""var:v109"" select=""userCSharp:LogicalExistence($var:v108)"" />
    <xsl:variable name=""var:v111"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_OnsetofCurrentIllnessorSymptom_2)"" />
    <xsl:variable name=""var:v112"" select=""userCSharp:LogicalExistence($var:v111)"" />
    <xsl:variable name=""var:v113"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastMenstrualPeriod_2)"" />
    <xsl:variable name=""var:v114"" select=""userCSharp:LogicalExistence($var:v113)"" />
    <xsl:variable name=""var:v116"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_DemonstrationProjectIdentifier_2))"" />
    <xsl:variable name=""var:v118"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_DemonstrationProjectIdentifier_2)"" />
    <xsl:variable name=""var:v119"" select=""userCSharp:LogicalExistence($var:v118)"" />
    <xsl:variable name=""var:v139"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation))"" />
    <xsl:variable name=""var:v141"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation)"" />
    <xsl:variable name=""var:v142"" select=""userCSharp:LogicalExistence($var:v141)"" />
    <xsl:variable name=""var:v144"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification))"" />
    <xsl:variable name=""var:v156"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:PRV_RenderingProviderSpecialtyInformation_3))"" />
    <xsl:variable name=""var:v158"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3))"" />
    <xsl:variable name=""var:v160"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3)"" />
    <xsl:variable name=""var:v161"" select=""userCSharp:LogicalExistence($var:v160)"" />
    <xsl:variable name=""var:v163"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v164"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
    <xsl:variable name=""var:v165"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[1]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v166"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
    <xsl:variable name=""var:v167"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v168"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[2]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v169"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v170"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[3]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v171"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[4]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v172"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3[4]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v173"" select=""userCSharp:StringConcat(string($var:v163) , string($var:v164) , string($var:v165) , string($var:v166) , string($var:v167) , string($var:v164) , string($var:v168) , string($var:v166) , string($var:v169) , string($var:v164) , string($var:v170) , string($var:v166) , string($var:v171) , string($var:v164) , string($var:v172) , string($var:v166))"" />
    <xsl:variable name=""var:v203"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v204"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[1]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v205"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v206"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[2]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v207"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v208"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[3]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v209"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[4]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v210"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_3[4]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v211"" select=""userCSharp:StringConcat(string($var:v203) , string($var:v164) , string($var:v204) , string($var:v166) , string($var:v205) , string($var:v164) , string($var:v206) , string($var:v166) , string($var:v207) , string($var:v164) , string($var:v208) , string($var:v166) , string($var:v209) , string($var:v164) , string($var:v210) , string($var:v166))"" />
    <xsl:variable name=""var:v212"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v213"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[1]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v214"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v215"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[2]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v216"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v217"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_3[3]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v218"" select=""userCSharp:StringConcat(string($var:v212) , string($var:v164) , string($var:v213) , string($var:v166) , string($var:v214) , string($var:v164) , string($var:v215) , string($var:v166) , string($var:v216) , string($var:v164) , string($var:v217) , string($var:v166))"" />
    <xsl:variable name=""var:v219"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v220"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v221"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[1]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v222"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[2]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v223"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v224"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[3]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v225"" select=""userCSharp:StringConcat(string($var:v219) , &quot;:&quot; , string($var:v220) , &quot;,&quot; , string($var:v221) , &quot;:&quot; , string($var:v222) , &quot;,&quot; , string($var:v223) , &quot;:&quot; , string($var:v224) , &quot;,&quot;)"" />
    <xsl:variable name=""var:v226"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v227"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[1]/REF02_BillingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v228"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v229"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[2]/REF02_BillingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v230"" select=""userCSharp:StringConcat(string($var:v226) , &quot;:&quot; , string($var:v227) , &quot;,&quot; , string($var:v228) , &quot;:&quot; , string($var:v229) , &quot;,&quot;)"" />
    <xsl:variable name=""var:v231"" select=""userCSharp:StringConcat(string($var:v225) , string($var:v230))"" />
    <xsl:variable name=""var:v232"" select=""userCSharp:StringConcat(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanSecondaryIdentification/REF01_ReferenceIdentificationQualifier/text()) , string($var:v164) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanSecondaryIdentification/REF02_Pay_toPlanSecondaryIdentifier/text()) , string($var:v166) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF01_ReferenceIdentificationQualifier/text()) , string($var:v164) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF02_Pay_ToPlanTaxIdentificationNumber/text()) , string($var:v166))"" />
    <xsl:variable name=""var:v704"" select=""userCSharp:StringConcat(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_AnesthesiaRelatedProcedure_2/s1:C022_HealthCareCodeInformation_49/C02201_CodeListQualifierCode/text()) , &quot;:&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_AnesthesiaRelatedProcedure_2/s1:C022_HealthCareCodeInformation_49/C02202_AnesthesiaRelatedSurgicalProcedure/text()) , &quot;,&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_AnesthesiaRelatedProcedure_2/s1:C022_HealthCareCodeInformation_50/C02201_CodeListQualifierCode/text()) , &quot;:&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_AnesthesiaRelatedProcedure_2/s1:C022_HealthCareCodeInformation_50/C02202_IndustryCode/text()))"" />
    <xsl:variable name=""var:v705"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_61/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v706"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_62/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v707"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_63/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v708"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_64/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v709"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_65/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v710"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_66/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v711"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_67/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v712"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_68/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v713"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_69/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v714"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_70/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v715"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_71/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v716"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_72/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v737"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode/text()) , &quot;P&quot;)"" />
    <xsl:variable name=""var:v738"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount))"" />
    <xsl:variable name=""var:v739"" select=""userCSharp:LogicalEq(string($var:v737) , string($var:v738))"" />
    <xsl:variable name=""var:v741"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode/text())"" />
    <xsl:variable name=""var:v742"" select=""userCSharp:LogicalEq($var:v741 , &quot;P&quot;)"" />
    <xsl:variable name=""var:v743"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount))"" />
    <xsl:variable name=""var:v744"" select=""userCSharp:LogicalEq(string($var:v742) , string($var:v743))"" />
    <xsl:variable name=""var:v746"" select=""userCSharp:LogicalEq($var:v741 , &quot;S&quot;)"" />
    <xsl:variable name=""var:v747"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount)"" />
    <xsl:variable name=""var:v748"" select=""userCSharp:LogicalExistence($var:v747)"" />
    <xsl:variable name=""var:v749"" select=""userCSharp:LogicalEq(string($var:v746) , string($var:v748))"" />
    <xsl:variable name=""var:v751"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount)"" />
    <xsl:variable name=""var:v752"" select=""userCSharp:LogicalExistence($var:v751)"" />
    <xsl:variable name=""var:v753"" select=""userCSharp:LogicalEq(string($var:v746) , string($var:v752))"" />
    <xsl:variable name=""var:v755"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_3))"" />
    <xsl:variable name=""var:v757"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_EPSDTReferral_2))"" />
    <xsl:variable name=""var:v759"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_EPSDTReferral_2)"" />
    <xsl:variable name=""var:v760"" select=""userCSharp:LogicalExistence($var:v759)"" />
    <xsl:variable name=""var:v763"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_MammographyCertificationNumber_3))"" />
    <xsl:variable name=""var:v765"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:NM1_AmbulanceDrop_offLocation_3))"" />
    <xsl:variable name=""var:v767"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP01_DateTimeQualifier))"" />
    <xsl:variable name=""var:v769"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP03_LastX_RayDate))"" />
    <ns0:Integration_Professional_Claims>
      <ns0:CLAIM>
        <ns0:DETAIL_COUNT>
          <xsl:value-of select=""$var:v1"" />
        </ns0:DETAIL_COUNT>
        <xsl:variable name=""var:v2"" select=""userCSharp:strAuthNumber(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_PriorAuthorization_3/REF02_PriorAuthorizationNumber/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_ReferralNumber_3/REF02_ReferralNumber/text()))"" />
        <ns0:AUTHORIZATION_NUMBER>
          <xsl:value-of select=""$var:v2"" />
        </ns0:AUTHORIZATION_NUMBER>
        <xsl:variable name=""var:v3"" select=""userCSharp:cobstatusprof(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()))"" />
        <ns0:COB_STATUS>
          <xsl:value-of select=""$var:v3"" />
        </ns0:COB_STATUS>
        <ns0:PAID_BY_PRIMARY_PAYER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()"" />
        </ns0:PAID_BY_PRIMARY_PAYER>
        <xsl:variable name=""var:v4"" select=""userCSharp:InitCumulativeMin(0)"" />
        <xsl:for-each select=""/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2400_Loop1/s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2"">
          <xsl:variable name=""var:v5"" select=""userCSharp:StringLeft(string(DTP03_ServiceDate/text()) , &quot;8&quot;)"" />
          <xsl:variable name=""var:v6"" select=""userCSharp:AddToCumulativeMin(0,string($var:v5),&quot;1000&quot;)"" />
        </xsl:for-each>
        <xsl:variable name=""var:v7"" select=""userCSharp:GetCumulativeMin(0)"" />
        <ns0:FIRST_SERVICE_DATE>
          <xsl:value-of select=""$var:v7"" />
        </ns0:FIRST_SERVICE_DATE>
        <xsl:variable name=""var:v8"" select=""userCSharp:ExternalClmID(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_RepricedClaimNumber_2/REF02_RepricedClaimReferenceNumber/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_ClaimIdentifierForTransmissionIntermediaries_2/REF02_ValueAddedNetworkTraceNumber/text()))"" />
        <ns0:EXTERNAL_CLAIM_ID>
          <xsl:value-of select=""$var:v8"" />
        </ns0:EXTERNAL_CLAIM_ID>
        <ns0:PATIENT_CONTROL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM01_PatientControlNumber/text()"" />
        </ns0:PATIENT_CONTROL_NUMBER>
        <xsl:if test=""string($var:v9)='true'"">
          <xsl:variable name=""var:v10"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_MedicalRecordNumber_2/REF02_MedicalRecordNumber/text()"" />
          <ns0:MEDICAL_RECORD_NUMBER>
            <xsl:value-of select=""$var:v10"" />
          </ns0:MEDICAL_RECORD_NUMBER>
        </xsl:if>
        <xsl:variable name=""var:v13"" select=""userCSharp:PayToProviderIDQual(string($var:v11) , $var:v12)"" />
        <ns0:PAY_TO_PROVIDER_ID_QUAL>
          <xsl:value-of select=""$var:v13"" />
        </ns0:PAY_TO_PROVIDER_ID_QUAL>
        <xsl:if test=""string($var:v14)='true'"">
          <xsl:variable name=""var:v15"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:REF_RenderingProviderSecondaryIdentification_3/REF01_ReferenceIdentificationQualifier/text()"" />
          <ns0:PROVIDER_ID_QUAL>
            <xsl:value-of select=""$var:v15"" />
          </ns0:PROVIDER_ID_QUAL>
        </xsl:if>
        <ns0:PAID_BY_MEMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:AMT_PatientAmountPaid_2/AMT02_PatientAmountPaid/text()"" />
        </ns0:PAID_BY_MEMBER>
        <ns0:EOB_NOTE>
          <xsl:text />
        </ns0:EOB_NOTE>
        <ns0:EDI_SUBMITTER_ID>
          <xsl:value-of select=""$var:v16"" />
        </ns0:EDI_SUBMITTER_ID>
        <ns0:EDI_RECEIVER_ID>
          <xsl:value-of select=""$var:v16"" />
        </ns0:EDI_RECEIVER_ID>
        <ns0:EDI_CORRECTION_LIST>
          <xsl:value-of select=""$var:v16"" />
        </ns0:EDI_CORRECTION_LIST>
        <ns0:PAY_TO_PLAN_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM103_Pay_toPlanOrganizationalName/text()"" />
        </ns0:PAY_TO_PLAN_NAME>
        <xsl:if test=""string($var:v17)='true'"">
          <xsl:variable name=""var:v18"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM109_Pay_toPlanPrimaryIdentifier/text()"" />
          <ns0:PAY_TO_PLAN_NPI>
            <xsl:value-of select=""$var:v18"" />
          </ns0:PAY_TO_PLAN_NPI>
        </xsl:if>
        <xsl:if test=""string($var:v19)='true'"">
          <xsl:variable name=""var:v20"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF02_Pay_ToPlanTaxIdentificationNumber/text()"" />
          <ns0:PAY_TO_PLAN_TAXID>
            <xsl:value-of select=""$var:v20"" />
          </ns0:PAY_TO_PLAN_TAXID>
        </xsl:if>
        <ns0:PAY_TO_PLAN_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N301_Pay_toPlanAddressLine/text()"" />
        </ns0:PAY_TO_PLAN_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N302_Pay_toPlanAddressLine"">
          <ns0:PAY_TO_PLAN_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N302_Pay_toPlanAddressLine/text()"" />
          </ns0:PAY_TO_PLAN_ADD2>
        </xsl:if>
        <ns0:PAY_TO_PLAN_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N401_Pay_toPlanCityName/text()"" />
        </ns0:PAY_TO_PLAN_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N402_Pay_toPlanStateorProvinceCode"">
          <ns0:PAY_TO_PLAN_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N402_Pay_toPlanStateorProvinceCode/text()"" />
          </ns0:PAY_TO_PLAN_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N403_Pay_toPlanPostalZoneorZIPCode"">
          <ns0:PAY_TO_PLAN_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N403_Pay_toPlanPostalZoneorZIPCode/text()"" />
          </ns0:PAY_TO_PLAN_ZIP>
        </xsl:if>
        <xsl:if test=""string($var:v21)='true'"">
          <xsl:variable name=""var:v22"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_RepricerReceivedDate_2/DTP03_RepricerReceivedDate/text()"" />
          <ns0:REPRICER_RECVD_DATE>
            <xsl:value-of select=""$var:v22"" />
          </ns0:REPRICER_RECVD_DATE>
        </xsl:if>
        <xsl:if test=""string($var:v23)='true'"">
          <xsl:variable name=""var:v24"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3/AMT02_RemainingPatientLiability/text()"" />
          <ns0:PATIENT_LIABILTY_AMT>
            <xsl:value-of select=""$var:v24"" />
          </ns0:PATIENT_LIABILTY_AMT>
        </xsl:if>
        <ns0:PAY_TO_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N301_Pay_toAddressLine/text()"" />
        </ns0:PAY_TO_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N302_Pay_toAddressLine"">
          <ns0:PAY_TO_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N302_Pay_toAddressLine/text()"" />
          </ns0:PAY_TO_ADD2>
        </xsl:if>
        <ns0:PAY_TO_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N401_Pay_toAddressCityName/text()"" />
        </ns0:PAY_TO_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N402_Pay_toAddressStateCode"">
          <ns0:PAY_TO_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N402_Pay_toAddressStateCode/text()"" />
          </ns0:PAY_TO_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N403_Pay_toAddressPostalZoneorZIPCode"">
          <ns0:PAY_TO_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N403_Pay_toAddressPostalZoneorZIPCode/text()"" />
          </ns0:PAY_TO_ZIP>
        </xsl:if>
        <ns0:PROVIDER_SIGNATURE_FILE_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM06_ProviderorSupplierSignatureIndicator/text()"" />
        </ns0:PROVIDER_SIGNATURE_FILE_IND>
        <ns0:MEDICARE_ASSIGNMENT_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM07_AssignmentorPlanParticipationCode/text()"" />
        </ns0:MEDICARE_ASSIGNMENT_CODE>
        <ns0:ASSIGNMENT_BENEFIT_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM08_BenefitsAssignmentCertificationIndicator/text()"" />
        </ns0:ASSIGNMENT_BENEFIT_IND>
        <ns0:RELEASE_INFO_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM09_ReleaseofInformationCode/text()"" />
        </ns0:RELEASE_INFO_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM10_PatientSignatureSourceCode"">
          <ns0:PATIENT_SIGNATURE_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM10_PatientSignatureSourceCode/text()"" />
          </ns0:PATIENT_SIGNATURE_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02404_AutoAccidentStateorProvinceCode"">
          <ns0:AUTO_ACCIDENT_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02404_AutoAccidentStateorProvinceCode/text()"" />
          </ns0:AUTO_ACCIDENT_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM12_SpecialProgramIndicator"">
          <ns0:SPECIAL_PROGRAM_IND>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM12_SpecialProgramIndicator/text()"" />
          </ns0:SPECIAL_PROGRAM_IND>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM16_ProviderAgreementCode"">
          <ns0:PARTICIPATION_AGREEMENT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM16_ProviderAgreementCode/text()"" />
          </ns0:PARTICIPATION_AGREEMENT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM20_DelayReasonCode"">
          <ns0:DELAY_REASON_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM20_DelayReasonCode/text()"" />
          </ns0:DELAY_REASON_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM109_SubscriberPrimaryIdentifier"">
          <ns0:INSURED_EXTID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM109_SubscriberPrimaryIdentifier/text()"" />
          </ns0:INSURED_EXTID>
        </xsl:if>
        <ns0:PATIENT_EXTID>
          <xsl:text />
        </ns0:PATIENT_EXTID>
        <xsl:variable name=""var:v26"" select=""userCSharp:cobindicator($var:v25 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2400_Loop1/s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD02_ServiceLinePaidAmount/text()))"" />
        <ns0:COB_INDICATOR>
          <xsl:value-of select=""$var:v26"" />
        </ns0:COB_INDICATOR>
        <ns0:ITS_PPSPA_REQUEST_ID>
          <xsl:text />
        </ns0:ITS_PPSPA_REQUEST_ID>
        <ns0:ITS_CLAIM_TYPE>
          <xsl:text />
        </ns0:ITS_CLAIM_TYPE>
        <ns0:TOTAL_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM02_TotalClaimChargeAmount/text()"" />
        </ns0:TOTAL_CHARGES>
        <xsl:variable name=""var:v27"" select=""userCSharp:PrincipalDiagQual(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_37/C02201_DiagnosisTypeCode/text()))"" />
        <ns0:ICD_VERSION_IND>
          <xsl:value-of select=""$var:v27"" />
        </ns0:ICD_VERSION_IND>
        <xsl:variable name=""var:v29"" select=""userCSharp:InitCumulativeMin(1)"" />
        <xsl:for-each select=""/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2400_Loop1/s1:TS837_2430_Loop1/s1:DTP_LineCheckorRemittanceDate_2"">
          <xsl:variable name=""var:v30"" select=""userCSharp:StringLeft(string(DTP03_AdjudicationorPaymentDate/text()) , &quot;8&quot;)"" />
          <xsl:variable name=""var:v31"" select=""userCSharp:AddToCumulativeMin(1,string($var:v30),&quot;1000&quot;)"" />
        </xsl:for-each>
        <xsl:variable name=""var:v32"" select=""userCSharp:GetCumulativeMin(1)"" />
        <xsl:variable name=""var:v33"" select=""userCSharp:ADJREMITDATE(string($var:v28) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate/text()) , string($var:v32))"" />
        <ns0:PRIMARY_PAID_DATE>
          <xsl:value-of select=""$var:v33"" />
        </ns0:PRIMARY_PAID_DATE>
        <xsl:variable name=""var:v36"" select=""userCSharp:nHaveData(string($var:v34) , string($var:v35))"" />
        <xsl:variable name=""var:v38"" select=""userCSharp:PATADDRESS($var:v37 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N301_SubscriberAddressLine/text()) , string($var:v36))"" />
        <ns0:PATIENT_ADD1>
          <xsl:value-of select=""$var:v38"" />
        </ns0:PATIENT_ADD1>
        <xsl:variable name=""var:v42"" select=""userCSharp:nHaveData(string($var:v40) , string($var:v41))"" />
        <xsl:variable name=""var:v43"" select=""userCSharp:PATADDRESSST(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N302_PatientAddressLine/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N302_SubscriberAddressLine/text()) , string($var:v42))"" />
        <ns0:PATIENT_ADD2>
          <xsl:value-of select=""$var:v43"" />
        </ns0:PATIENT_ADD2>
        <xsl:variable name=""var:v46"" select=""userCSharp:nHaveData(string($var:v44) , string($var:v45))"" />
        <xsl:variable name=""var:v48"" select=""userCSharp:PATCITY($var:v47 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N401_SubscriberCityName/text()) , string($var:v46))"" />
        <ns0:PATIENT_CITY>
          <xsl:value-of select=""$var:v48"" />
        </ns0:PATIENT_CITY>
        <xsl:variable name=""var:v52"" select=""userCSharp:nHaveData(string($var:v50) , string($var:v51))"" />
        <xsl:variable name=""var:v53"" select=""userCSharp:PATSTATE(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N402_PatientStateCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N402_SubscriberStateCode/text()) , string($var:v52))"" />
        <ns0:PATIENT_STATE>
          <xsl:value-of select=""$var:v53"" />
        </ns0:PATIENT_STATE>
        <xsl:variable name=""var:v54"" select=""userCSharp:nHaveData(string($var:v50) , string($var:v51))"" />
        <xsl:variable name=""var:v55"" select=""userCSharp:PATZIP(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N403_PatientPostalZoneorZIPCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N403_SubscriberPostalZoneorZIPCode/text()) , string($var:v54))"" />
        <ns0:PATIENT_ZIP>
          <xsl:value-of select=""$var:v55"" />
        </ns0:PATIENT_ZIP>
      </ns0:CLAIM>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2000C_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop1"">
              <xsl:for-each select=""s1:TS837_2400_Loop1"">
                <ns0:CLAIM_DETAIL>
                  <ns0:LINE_NUMBER>
                    <xsl:value-of select=""s1:LX_ServiceLineNumber_2/LX01_AssignedNumber/text()"" />
                  </ns0:LINE_NUMBER>
                </ns0:CLAIM_DETAIL>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
      <ns0:PROF_CLAIM>
        <xsl:variable name=""var:v57"" select=""userCSharp:conditionEmp(string($var:v56) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02401_RelatedCausesCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02402_RelatedCausesCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02403_Related_CausesCode/text()))"" />
        <ns0:CONDITION_EMPLOYMENT>
          <xsl:value-of select=""$var:v57"" />
        </ns0:CONDITION_EMPLOYMENT>
        <xsl:variable name=""var:v63"" select=""userCSharp:conditionAuto(string($var:v59) , $var:v60 , $var:v61 , $var:v62)"" />
        <ns0:CONDITION_AUTO_ACCIDENT>
          <xsl:value-of select=""$var:v63"" />
        </ns0:CONDITION_AUTO_ACCIDENT>
        <xsl:variable name=""var:v64"" select=""userCSharp:conditionOth(string($var:v59) , $var:v60 , $var:v61 , $var:v62)"" />
        <ns0:CONDITION_OTHER_ACCIDENT>
          <xsl:value-of select=""$var:v64"" />
        </ns0:CONDITION_OTHER_ACCIDENT>
        <ns0:OTHER_INSURANCE_FLAG>
          <xsl:text>N</xsl:text>
        </ns0:OTHER_INSURANCE_FLAG>
        <xsl:variable name=""var:v67"" select=""userCSharp:DTPIllnessseg(string($var:v65) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_OnsetofCurrentIllnessorSymptom_2/DTP03_OnsetofCurrentIllnessorInjuryDate/text()) , string($var:v66) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastMenstrualPeriod_2/DTP03_LastMenstrualPeriodDate/text()))"" />
        <ns0:FIRST_SYMPTOM_DATE>
          <xsl:value-of select=""$var:v67"" />
        </ns0:FIRST_SYMPTOM_DATE>
        <ns0:FIRST_SIMILAR_SYMPTOM_DATE>
          <xsl:text />
        </ns0:FIRST_SIMILAR_SYMPTOM_DATE>
        <xsl:variable name=""var:v69"" select=""userCSharp:DisabilityBeginDate(string($var:v68) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP01_DateTimeQualifier/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP02_DateTimePeriodFormatQualifier/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_DisabilityDates_2/DTP03_DisabilityFromDate/text()))"" />
        <ns0:LOSS_OF_WORK_BEGIN>
          <xsl:value-of select=""$var:v69"" />
        </ns0:LOSS_OF_WORK_BEGIN>
        <xsl:variable name=""var:v75"" select=""userCSharp:DisabilityEndDate(string($var:v71) , $var:v72 , $var:v73 , $var:v74)"" />
        <ns0:LOSS_OF_WORK_END>
          <xsl:value-of select=""$var:v75"" />
        </ns0:LOSS_OF_WORK_END>
        <xsl:if test=""string($var:v76)='true'"">
          <xsl:variable name=""var:v77"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Admission_2/DTP03_RelatedHospitalizationAdmissionDate/text()"" />
          <ns0:HOSPITALIZATION_BEGIN>
            <xsl:value-of select=""$var:v77"" />
          </ns0:HOSPITALIZATION_BEGIN>
        </xsl:if>
        <xsl:if test=""string($var:v78)='true'"">
          <xsl:variable name=""var:v79"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Discharge_2/DTP03_RelatedHospitalizationDischargeDate/text()"" />
          <ns0:HOSPITALIZATION_END>
            <xsl:value-of select=""$var:v79"" />
          </ns0:HOSPITALIZATION_END>
        </xsl:if>
        <ns0:RELEASE_INFO_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM09_ReleaseofInformationCode/text()"" />
        </ns0:RELEASE_INFO_CODE>
        <xsl:if test=""string($var:v80)='true'"">
          <xsl:variable name=""var:v81"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM10_PatientSignatureSourceCode/text()"" />
          <ns0:PATIENT_SIGNATURE_CODE>
            <xsl:value-of select=""$var:v81"" />
          </ns0:PATIENT_SIGNATURE_CODE>
        </xsl:if>
        <ns0:PROVIDER_SIGNATURE_FILE_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM06_ProviderorSupplierSignatureIndicator/text()"" />
        </ns0:PROVIDER_SIGNATURE_FILE_IND>
        <ns0:AMBULATORY_PATIENT_GROUP>
          <xsl:text />
        </ns0:AMBULATORY_PATIENT_GROUP>
        <ns0:TOTAL_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/CLM02_TotalClaimChargeAmount/text()"" />
        </ns0:TOTAL_CHARGES>
        <xsl:variable name=""var:v83"" select=""userCSharp:InstDiagCodesList($var:v82 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_37/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_38/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_38/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_39/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_39/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_40/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_40/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_41/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_41/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_42/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_42/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_43/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_43/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_44/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_44/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_45/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_45/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_46/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_46/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_47/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_47/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_48/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_48/C02202_DiagnosisCode/text()))"" />
        <ns0:DIAGNOSIS_CODES_LIST>
          <xsl:value-of select=""$var:v83"" />
        </ns0:DIAGNOSIS_CODES_LIST>
        <ns0:REPRICE_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HCP_ClaimPricing_RepricingInformation_2/HCP02_RepricedAllowedAmount/text()"" />
        </ns0:REPRICE_CHARGES>
        <xsl:variable name=""var:v84"" select=""userCSharp:ConditionCodes(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_61/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_62/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_63/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_64/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_65/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_66/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_67/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_68/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_69/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_70/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_71/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:HI_SubLoop_2/s1:HI_ConditionInformation_2_Loop/s1:HI_ConditionInformation_2/s1:C022_HealthCareCodeInformation_72/C02202_ConditionCode/text()))"" />
        <ns0:CONDITION_CODES_LIST>
          <xsl:value-of select=""$var:v84"" />
        </ns0:CONDITION_CODES_LIST>
        <ns0:CLAIM_FREQUENCY_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C023_HealthCareServiceLocationInformation_2/C02303_ClaimFrequencyCode/text()"" />
        </ns0:CLAIM_FREQUENCY_CODE>
        <xsl:variable name=""var:v93"" select=""userCSharp:DTPsegQual(string($var:v85) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_InitialTreatmentDate_3/DTP01_DateTimeQualifier/text()) , string($var:v86) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastSeenDate_3/DTP01_DateTimeQualifier/text()) , string($var:v87) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AcuteManifestation_2/DTP01_DateTimeQualifier/text()) , string($var:v88) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2/DTP01_DateTimeQualifier/text()) , string($var:v89) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP01_DateTimeQualifier/text()) , string($var:v90) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_HearingandVisionPrescriptionDate_2/DTP01_DateTimeQualifier/text()) , string($var:v91) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AssumedandRelinquishedCareDates_2_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates_2/DTP01_DateTimeQualifier/text()) , string($var:v92) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_PropertyandCasualtyDateofFirstContact_2/DTP01_DateTimeQualifier/text()))"" />
        <ns0:OTHER_DATE_QUAL>
          <xsl:value-of select=""$var:v93"" />
        </ns0:OTHER_DATE_QUAL>
        <xsl:variable name=""var:v110"" select=""userCSharp:DTPseg(string($var:v95) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_InitialTreatmentDate_3/DTP03_InitialTreatmentDate/text()) , string($var:v97) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastSeenDate_3/DTP03_LastSeenDate/text()) , string($var:v99) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AcuteManifestation_2/DTP03_AcuteManifestationDate/text()) , string($var:v101) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2/DTP03_AccidentDate/text()) , string($var:v103) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP03_LastX_RayDate/text()) , string($var:v105) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_HearingandVisionPrescriptionDate_2/DTP03_PrescriptionDate/text()) , string($var:v107) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_AssumedandRelinquishedCareDates_2_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates_2/DTP03_AssumedorRelinquishedCareDate/text()) , string($var:v109) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_PropertyandCasualtyDateofFirstContact_2/DTP03_DateTimePeriod/text()))"" />
        <ns0:OTHER_DATE>
          <xsl:value-of select=""$var:v110"" />
        </ns0:OTHER_DATE>
        <xsl:variable name=""var:v115"" select=""userCSharp:DTPIllnesssegQual(string($var:v112) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_OnsetofCurrentIllnessorSymptom_2/DTP01_DateTimeQualifier/text()) , string($var:v114) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastMenstrualPeriod_2/DTP01_DateTimeQualifier/text()))"" />
        <ns0:FIRST_SYMPTOM_DATE_QUAL>
          <xsl:value-of select=""$var:v115"" />
        </ns0:FIRST_SYMPTOM_DATE_QUAL>
        <ns0:LOCATION_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C023_HealthCareServiceLocationInformation_2/C02301_PlaceofServiceCode/text()"" />
        </ns0:LOCATION_CODE>
        <xsl:if test=""string($var:v116)='true'"">
          <xsl:variable name=""var:v117"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_DemonstrationProjectIdentifier_2/REF01_ReferenceIdentificationQualifier/text()"" />
          <ns0:ADDTNL_CLAIM_INFO_QUAL>
            <xsl:value-of select=""$var:v117"" />
          </ns0:ADDTNL_CLAIM_INFO_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v119)='true'"">
          <xsl:variable name=""var:v120"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_DemonstrationProjectIdentifier_2/REF02_DemonstrationProjectIdentifier/text()"" />
          <ns0:ADDTNL_CLAIM_INFO>
            <xsl:value-of select=""$var:v120"" />
          </ns0:ADDTNL_CLAIM_INFO>
        </xsl:if>
      </ns0:PROF_CLAIM>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2000C_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop1"">
              <xsl:for-each select=""s1:TS837_2400_Loop1"">
                <xsl:variable name=""var:v123"" select=""string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP02_DateTimePeriodFormatQualifier/text())"" />
                <xsl:variable name=""var:v124"" select=""string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP03_ServiceDate/text())"" />
                <xsl:variable name=""var:v126"" select=""userCSharp:LogicalExistence(boolean(s1:SV1_ProfessionalService_2/SV105_PlaceofServiceCode))"" />
                <xsl:variable name=""var:v127"" select=""userCSharp:StringSize(string(s1:SV1_ProfessionalService_2/SV105_PlaceofServiceCode/text()))"" />
                <xsl:variable name=""var:v129"" select=""string(s1:SV1_ProfessionalService_2/SV105_PlaceofServiceCode/text())"" />
                <xsl:variable name=""var:v133"" select=""s1:TS837_2410_Loop1/s1:LIN_DrugIdentification_2[1]/LIN03_NationalDrugCodeorUniversalProductNumber/text()"" />
                <xsl:variable name=""var:v134"" select=""string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00401_DiagnosisCodePointer/text())"" />
                <xsl:variable name=""var:v135"" select=""string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00402_DiagnosisCodePointer/text())"" />
                <xsl:variable name=""var:v136"" select=""string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00403_DiagnosisCodePointer/text())"" />
                <xsl:variable name=""var:v137"" select=""string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00404_DiagnosisCodePointer/text())"" />
                <ns0:PROF_CLAIM_DETAIL>
                  <ns0:LINE_NUMBER>
                    <xsl:value-of select=""s1:LX_ServiceLineNumber_2/LX01_AssignedNumber/text()"" />
                  </ns0:LINE_NUMBER>
                  <ns0:SERVICE_CODE_QUALIFIER>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00301_ProductorServiceIDQualifier/text()"" />
                  </ns0:SERVICE_CODE_QUALIFIER>
                  <ns0:SERVICE_CODE>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00302_ProcedureCode/text()"" />
                  </ns0:SERVICE_CODE>
                  <xsl:variable name=""var:v121"" select=""userCSharp:SubServiceModifierList(string(s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00303_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00304_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00305_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00306_ProcedureModifier/text()))"" />
                  <ns0:SERVICE_MODIFIER_LIST>
                    <xsl:value-of select=""$var:v121"" />
                  </ns0:SERVICE_MODIFIER_LIST>
                  <xsl:variable name=""var:v122"" select=""userCSharp:SubServiceFromDate(string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP02_DateTimePeriodFormatQualifier/text()) , string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP03_ServiceDate/text()))"" />
                  <ns0:SERVICE_FROM_DATE>
                    <xsl:value-of select=""$var:v122"" />
                  </ns0:SERVICE_FROM_DATE>
                  <xsl:variable name=""var:v125"" select=""userCSharp:SubServiceToDate($var:v123 , $var:v124)"" />
                  <ns0:SERVICE_TO_DATE>
                    <xsl:value-of select=""$var:v125"" />
                  </ns0:SERVICE_TO_DATE>
                  <xsl:variable name=""var:v128"" select=""userCSharp:bHaveData(string($var:v126) , string($var:v127))"" />
                  <xsl:variable name=""var:v130"" select=""userCSharp:LocationCode($var:v129 , string(../s1:CLM_ClaimInformation_2/s1:C023_HealthCareServiceLocationInformation_2/C02301_PlaceofServiceCode/text()) , string($var:v128))"" />
                  <ns0:LOCATION_CODE>
                    <xsl:value-of select=""$var:v130"" />
                  </ns0:LOCATION_CODE>
                  <xsl:variable name=""var:v131"" select=""userCSharp:DiagnosisPointers(string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00401_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00402_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00403_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService_2/s1:C004_CompositeDiagnosisCodePointer_2/C00404_DiagnosisCodePointer/text()))"" />
                  <xsl:variable name=""var:v132"" select=""userCSharp:DiagPatCodesList(string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_37/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_37/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_38/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_38/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_39/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_39/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_40/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_40/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_41/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_41/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_42/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_42/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_43/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_43/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_44/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_44/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_45/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_45/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_46/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_46/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_47/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_47/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_48/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop_2/s1:HI_HealthCareDiagnosisCode_2/s1:C022_HealthCareCodeInformation_48/C02202_DiagnosisCode/text()) , string($var:v131))"" />
                  <ns0:DIAGNOSIS_CODE_LIST>
                    <xsl:value-of select=""$var:v132"" />
                  </ns0:DIAGNOSIS_CODE_LIST>
                  <ns0:NDC_CODE_LIST>
                    <xsl:value-of select=""$var:v133"" />
                  </ns0:NDC_CODE_LIST>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/SV106_ServiceTypeCode"">
                    <ns0:TYPE_OF_SERVICE>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV106_ServiceTypeCode/text()"" />
                    </ns0:TYPE_OF_SERVICE>
                  </xsl:if>
                  <ns0:TOTAL_CHARGES>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV102_LineItemChargeAmount/text()"" />
                  </ns0:TOTAL_CHARGES>
                  <ns0:UNIT_MEASUREMENT>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV103_UnitorBasisforMeasurementCode/text()"" />
                  </ns0:UNIT_MEASUREMENT>
                  <ns0:QUANTITY>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV104_ServiceUnitCount/text()"" />
                  </ns0:QUANTITY>
                  <ns0:COB_PAID>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD02_ServiceLinePaidAmount/text()"" />
                  </ns0:COB_PAID>
                  <ns0:REPRICE_CHARGES>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP02_RepricedAllowedAmount/text()"" />
                  </ns0:REPRICE_CHARGES>
                  <xsl:variable name=""var:v138"" select=""userCSharp:DiagnosisPointers($var:v134 , $var:v135 , $var:v136 , $var:v137)"" />
                  <ns0:DIAGNOSIS_IDX>
                    <xsl:value-of select=""$var:v138"" />
                  </ns0:DIAGNOSIS_IDX>
                  <ns0:TP_ORG_NOTES>
                    <xsl:value-of select=""s1:NTE_SubLoop_2/s1:NTE_ThirdPartyOrganizationNotes_2/NTE02_LineNoteText/text()"" />
                  </ns0:TP_ORG_NOTES>
                  <ns0:LINEITEM_CONTROL_NUMBER>
                    <xsl:value-of select=""s1:REF_SubLoop_11/s1:REF_LineItemControlNumber_2/REF02_LineItemControlNumber/text()"" />
                  </ns0:LINEITEM_CONTROL_NUMBER>
                  <ns0:OBS_ANESTHSIA_ADDTNL_UNITS>
                    <xsl:value-of select=""s1:QTY_SubLoop_2/s1:QTY_ObstetricAnesthesiaAdditionalUnits_2/QTY02_ObstetricAdditionalUnits/text()"" />
                  </ns0:OBS_ANESTHSIA_ADDTNL_UNITS>
                  <ns0:PATIENT_LIABILTY_AMT>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:AMT_RemainingPatientLiability_4/AMT02_RemainingPatientLiability/text()"" />
                  </ns0:PATIENT_LIABILTY_AMT>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/SV109_EmergencyIndicator"">
                    <ns0:EMERGENCY_IND>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV109_EmergencyIndicator/text()"" />
                    </ns0:EMERGENCY_IND>
                  </xsl:if>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/SV111_EPSDTIndicator"">
                    <ns0:EPSDT_IND>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV111_EPSDTIndicator/text()"" />
                    </ns0:EPSDT_IND>
                  </xsl:if>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/SV112_FamilyPlanningIndicator"">
                    <ns0:FAMILY_PLAN_IND>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV112_FamilyPlanningIndicator/text()"" />
                    </ns0:FAMILY_PLAN_IND>
                  </xsl:if>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/SV115_Co_PayStatusCode"">
                    <ns0:COPAY_WAVIER>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/SV115_Co_PayStatusCode/text()"" />
                    </ns0:COPAY_WAVIER>
                  </xsl:if>
                  <ns0:PROV_LINEITEM_NUM>
                    <xsl:text />
                  </ns0:PROV_LINEITEM_NUM>
                  <ns0:NATIONAL_DRUG_COUNT>
                    <xsl:value-of select=""s1:TS837_2410_Loop1/s1:CTP_DrugQuantity_2/CTP04_NationalDrugUnitCount/text()"" />
                  </ns0:NATIONAL_DRUG_COUNT>
                </ns0:PROF_CLAIM_DETAIL>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
      <ns0:CLAIM_ADDTNL>
        <xsl:if test=""string($var:v139)='true'"">
          <xsl:variable name=""var:v140"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV01_ProviderCode/text()"" />
          <ns0:BILL_PAYTO_TAX_QUAL>
            <xsl:value-of select=""$var:v140"" />
          </ns0:BILL_PAYTO_TAX_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v142)='true'"">
          <xsl:variable name=""var:v143"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV03_ProviderTaxonomyCode/text()"" />
          <ns0:BILL_PAYTO_TAXONOMY>
            <xsl:value-of select=""$var:v143"" />
          </ns0:BILL_PAYTO_TAXONOMY>
        </xsl:if>
        <ns0:BILL_PROVIDER_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM102_EntityTypeQualifier/text()"" />
        </ns0:BILL_PROVIDER_QUAL>
        <ns0:BILL_PROVIDER_LNAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM103_BillingProviderLastorOrganizationalName/text()"" />
        </ns0:BILL_PROVIDER_LNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM105_BillingProviderMiddleNameorInitial"">
          <ns0:BILL_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM105_BillingProviderMiddleNameorInitial/text()"" />
          </ns0:BILL_PROVIDER_MNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM104_BillingProviderFirstName"">
          <ns0:BILL_PROVIDER_FNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM104_BillingProviderFirstName/text()"" />
          </ns0:BILL_PROVIDER_FNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM107_BillingProviderNameSuffix"">
          <ns0:BILL_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM107_BillingProviderNameSuffix/text()"" />
          </ns0:BILL_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM108_IdentificationCodeQualifier"">
          <ns0:BILL_PROVIDER_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:BILL_PROVIDER_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM109_BillingProviderIdentifier"">
          <ns0:BILL_PROVIDER_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM109_BillingProviderIdentifier/text()"" />
          </ns0:BILL_PROVIDER_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM109_BillingProviderIdentifier"">
          <ns0:BILL_PROVIDER_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:NM1_BillingProviderName/NM109_BillingProviderIdentifier/text()"" />
          </ns0:BILL_PROVIDER_NPI_ID>
        </xsl:if>
        <ns0:BILL_PROVIDER_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N3_BillingProviderAddress/N301_BillingProviderAddressLine/text()"" />
        </ns0:BILL_PROVIDER_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N3_BillingProviderAddress/N302_BillingProviderAddressLine"">
          <ns0:BILL_PROVIDER_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N3_BillingProviderAddress/N302_BillingProviderAddressLine/text()"" />
          </ns0:BILL_PROVIDER_ADD2>
        </xsl:if>
        <ns0:BILL_PROVIDER_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N401_BillingProviderCityName/text()"" />
        </ns0:BILL_PROVIDER_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N402_BillingProviderStateorProvinceCode"">
          <ns0:BILL_PROVIDER_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N402_BillingProviderStateorProvinceCode/text()"" />
          </ns0:BILL_PROVIDER_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N403_BillingProviderPostalZoneorZIPCode"">
          <ns0:BILL_PROVIDER_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N403_BillingProviderPostalZoneorZIPCode/text()"" />
          </ns0:BILL_PROVIDER_ZIP>
        </xsl:if>
        <xsl:if test=""string($var:v144)='true'"">
          <xsl:variable name=""var:v145"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text()"" />
          <xsl:variable name=""var:v146"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
          <xsl:variable name=""var:v147"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification)"" />
          <xsl:variable name=""var:v148"" select=""userCSharp:LogicalExistence($var:v147)"" />
          <xsl:if test=""string($var:v148)='true'"">
            <xsl:variable name=""var:v149"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF02_BillingProviderTaxIdentificationNumber/text()"" />
            <xsl:variable name=""var:v150"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
            <xsl:variable name=""var:v151"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[1]/REF01_ReferenceIdentificationQualifier/text()"" />
            <xsl:variable name=""var:v152"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[1]/REF02_BillingProviderLicenseand_orUPINInformation/text()"" />
            <xsl:variable name=""var:v153"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[2]/REF01_ReferenceIdentificationQualifier/text()"" />
            <xsl:variable name=""var:v154"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[2]/REF02_BillingProviderLicenseand_orUPINInformation/text()"" />
            <xsl:variable name=""var:v155"" select=""userCSharp:StringConcat(string($var:v145) , string($var:v146) , string($var:v149) , string($var:v150) , string($var:v151) , string($var:v146) , string($var:v152) , string($var:v150) , string($var:v153) , string($var:v146) , string($var:v154) , string($var:v150))"" />
            <ns0:BILL_PROVIDER_REF>
              <xsl:value-of select=""$var:v155"" />
            </ns0:BILL_PROVIDER_REF>
          </xsl:if>
        </xsl:if>
        <ns0:BILL_PROVIDER_PER01>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER01_ContactFunctionCode/text()"" />
        </ns0:BILL_PROVIDER_PER01>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER02_BillingProviderContactName"">
          <ns0:BILL_PROVIDER_PER02>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER02_BillingProviderContactName/text()"" />
          </ns0:BILL_PROVIDER_PER02>
        </xsl:if>
        <ns0:BILL_PROVIDER_PER03>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER03_CommunicationNumberQualifier/text()"" />
        </ns0:BILL_PROVIDER_PER03>
        <ns0:BILL_PROVIDER_PER04>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER04_CommunicationNumber/text()"" />
        </ns0:BILL_PROVIDER_PER04>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER05_CommunicationNumberQualifier"">
          <ns0:BILL_PROVIDER_PER05>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER05_CommunicationNumberQualifier/text()"" />
          </ns0:BILL_PROVIDER_PER05>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER06_CommunicationNumber"">
          <ns0:BILL_PROVIDER_PER06>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER06_CommunicationNumber/text()"" />
          </ns0:BILL_PROVIDER_PER06>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER07_CommunicationNumberQualifier"">
          <ns0:BILL_PROVIDER_PER07>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER07_CommunicationNumberQualifier/text()"" />
          </ns0:BILL_PROVIDER_PER07>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER08_CommunicationNumber"">
          <ns0:BILL_PROVIDER_PER08>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:PER_BillingProviderContactInformation/PER08_CommunicationNumber/text()"" />
          </ns0:BILL_PROVIDER_PER08>
        </xsl:if>
        <ns0:PAY_TO_PROVIDER_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM102_EntityTypeQualifier/text()"" />
        </ns0:PAY_TO_PROVIDER_QUAL>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM103_Pay_toLastorOrganizationalName"">
          <ns0:PAY_TO_PROVIDER_LNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM103_Pay_toLastorOrganizationalName/text()"" />
          </ns0:PAY_TO_PROVIDER_LNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM105_NameMiddle"">
          <ns0:PAY_TO_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM105_NameMiddle/text()"" />
          </ns0:PAY_TO_PROVIDER_MNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM104_NameFirst"">
          <ns0:PAY_TO_PROVIDER_FNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM104_NameFirst/text()"" />
          </ns0:PAY_TO_PROVIDER_FNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM107_NameSuffix"">
          <ns0:PAY_TO_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM107_NameSuffix/text()"" />
          </ns0:PAY_TO_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM108_IdentificationCodeQualifier"">
          <ns0:PAY_TO_PROVIDER_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:PAY_TO_PROVIDER_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode"">
          <ns0:PAY_TO_PROVIDER_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode/text()"" />
          </ns0:PAY_TO_PROVIDER_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode"">
          <ns0:PAY_TO_PROVIDER_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode/text()"" />
          </ns0:PAY_TO_PROVIDER_NPI_ID>
        </xsl:if>
        <ns0:PAY_TO_PROVIDER_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N301_Pay_toAddressLine/text()"" />
        </ns0:PAY_TO_PROVIDER_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N302_Pay_toAddressLine"">
          <ns0:PAY_TO_PROVIDER_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N3_Pay_ToAddress_ADDRESS/N302_Pay_toAddressLine/text()"" />
          </ns0:PAY_TO_PROVIDER_ADD2>
        </xsl:if>
        <ns0:PAY_TO_PROVIDER_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N401_Pay_toAddressCityName/text()"" />
        </ns0:PAY_TO_PROVIDER_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N402_Pay_toAddressStateCode"">
          <ns0:PAY_TO_PROVIDER_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N402_Pay_toAddressStateCode/text()"" />
          </ns0:PAY_TO_PROVIDER_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N403_Pay_toAddressPostalZoneorZIPCode"">
          <ns0:PAY_TO_PROVIDER_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:N4_Pay_toAddressCity_State_ZIPCode/N403_Pay_toAddressPostalZoneorZIPCode/text()"" />
          </ns0:PAY_TO_PROVIDER_ZIP>
        </xsl:if>
        <ns0:PAY_TO_PROVIDER_REF>
          <xsl:text />
        </ns0:PAY_TO_PROVIDER_REF>
        <xsl:if test=""string($var:v156)='true'"">
          <xsl:variable name=""var:v157"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:PRV_RenderingProviderSpecialtyInformation_3/PRV03_ProviderTaxonomyCode/text()"" />
          <ns0:REN_PROVIDER_TAXONOMY>
            <xsl:value-of select=""$var:v157"" />
          </ns0:REN_PROVIDER_TAXONOMY>
        </xsl:if>
        <xsl:if test=""string($var:v158)='true'"">
          <xsl:variable name=""var:v159"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM102_EntityTypeQualifier/text()"" />
          <ns0:REN_PROVIDER_QUAL>
            <xsl:value-of select=""$var:v159"" />
          </ns0:REN_PROVIDER_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v161)='true'"">
          <xsl:variable name=""var:v162"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM103_RenderingProviderLastorOrganizationName/text()"" />
          <ns0:REN_PROVIDER_LNAME>
            <xsl:value-of select=""$var:v162"" />
          </ns0:REN_PROVIDER_LNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM105_RenderingProviderMiddleNameorInitial"">
          <ns0:REN_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM105_RenderingProviderMiddleNameorInitial/text()"" />
          </ns0:REN_PROVIDER_MNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM104_RenderingProviderFirstName"">
          <ns0:REN_REN_PROVIDER_FNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM104_RenderingProviderFirstName/text()"" />
          </ns0:REN_REN_PROVIDER_FNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM107_RenderingProviderNameSuffix"">
          <ns0:REN_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM107_RenderingProviderNameSuffix/text()"" />
          </ns0:REN_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM108_IdentificationCodeQualifier"">
          <ns0:REN_PROVIDER_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:REN_PROVIDER_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM109_RenderingProviderIdentifier"">
          <ns0:REN_PROVIDER_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM109_RenderingProviderIdentifier/text()"" />
          </ns0:REN_PROVIDER_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM109_RenderingProviderIdentifier"">
          <ns0:REN_PROVIDER_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310B_Loop1/s1:NM1_RenderingProviderName_3/NM109_RenderingProviderIdentifier/text()"" />
          </ns0:REN_PROVIDER_NPI_ID>
        </xsl:if>
        <ns0:REN_PROVIDER_REF>
          <xsl:value-of select=""$var:v173"" />
        </ns0:REN_PROVIDER_REF>
        <ns0:AREF_PROVIDER_TAXONOMY>
          <xsl:text />
        </ns0:AREF_PROVIDER_TAXONOMY>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v174"" select=""position()"" />
                      <xsl:variable name=""var:v175"" select=""userCSharp:LogicalEq(string($var:v174) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v175"">
                        <xsl:variable name=""var:v176"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_ReferringProviderName_3))"" />
                        <xsl:if test=""string($var:v176)='true'"">
                          <xsl:variable name=""var:v177"" select=""s1:NM1_ReferringProviderName_3/NM102_EntityTypeQualifier/text()"" />
                          <ns0:AREF_PROVIDER_QUAL>
                            <xsl:value-of select=""$var:v177"" />
                          </ns0:AREF_PROVIDER_QUAL>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v178"" select=""position()"" />
                      <xsl:variable name=""var:v179"" select=""userCSharp:LogicalEq(string($var:v178) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v179"">
                        <ns0:AREF_PROVIDER_LNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM103_ReferringProviderLastName/text()"" />
                        </ns0:AREF_PROVIDER_LNAME>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v180"" select=""position()"" />
                      <xsl:variable name=""var:v181"" select=""userCSharp:LogicalEq(string($var:v180) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v181"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM105_ReferringProviderMiddleNameorInitial"">
                          <ns0:AREF_PROVIDER_MNAME>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                          </ns0:AREF_PROVIDER_MNAME>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v182"" select=""position()"" />
                      <xsl:variable name=""var:v183"" select=""userCSharp:LogicalEq(string($var:v182) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v183"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM104_ReferringProviderFirstName"">
                          <ns0:AREF_PROVIDER_FNAME>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM104_ReferringProviderFirstName/text()"" />
                          </ns0:AREF_PROVIDER_FNAME>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v184"" select=""position()"" />
                      <xsl:variable name=""var:v185"" select=""userCSharp:LogicalEq(string($var:v184) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v185"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM107_ReferringProviderNameSuffix"">
                          <ns0:AREF_PROVIDER_SUFFIX>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM107_ReferringProviderNameSuffix/text()"" />
                          </ns0:AREF_PROVIDER_SUFFIX>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v186"" select=""position()"" />
                      <xsl:variable name=""var:v187"" select=""userCSharp:LogicalEq(string($var:v186) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v187"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM108_IdentificationCodeQualifier"">
                          <ns0:AREF_PROVIDER_ID_QUAL>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM108_IdentificationCodeQualifier/text()"" />
                          </ns0:AREF_PROVIDER_ID_QUAL>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v188"" select=""position()"" />
                      <xsl:variable name=""var:v189"" select=""userCSharp:LogicalEq(string($var:v188) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v189"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier"">
                          <ns0:AREF_PROVIDER_ID>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier/text()"" />
                          </ns0:AREF_PROVIDER_ID>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v190"" select=""position()"" />
                      <xsl:variable name=""var:v191"" select=""userCSharp:LogicalEq(string($var:v190) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v191"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier"">
                          <ns0:AREF_PROVIDER_NPI_ID>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier/text()"" />
                          </ns0:AREF_PROVIDER_NPI_ID>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v192"" select=""position()"" />
                      <xsl:variable name=""var:v193"" select=""userCSharp:LogicalEq(string($var:v192) , &quot;1&quot;)"" />
                      <xsl:if test=""$var:v193"">
                        <xsl:variable name=""var:v194"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v195"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
                        <xsl:variable name=""var:v196"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v197"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
                        <xsl:variable name=""var:v198"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v199"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v200"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v201"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v202"" select=""userCSharp:StringConcat(string($var:v194) , string($var:v195) , string($var:v196) , string($var:v197) , string($var:v198) , string($var:v195) , string($var:v199) , string($var:v197) , string($var:v200) , string($var:v195) , string($var:v201) , string($var:v197))"" />
                        <ns0:AREF_PROVIDER_REF>
                          <xsl:value-of select=""$var:v202"" />
                        </ns0:AREF_PROVIDER_REF>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:SUPER_PROVIDER_TAXONOMY>
          <xsl:text />
        </ns0:SUPER_PROVIDER_TAXONOMY>
        <ns0:SUPER_PROVIDER_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM102_EntityTypeQualifier/text()"" />
        </ns0:SUPER_PROVIDER_QUAL>
        <ns0:SUPER_PROVIDER_LNAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM103_SupervisingProviderLastName/text()"" />
        </ns0:SUPER_PROVIDER_LNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM105_SupervisingProviderMiddleNameorInitial"">
          <ns0:SUPER_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM105_SupervisingProviderMiddleNameorInitial/text()"" />
          </ns0:SUPER_PROVIDER_MNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM104_SupervisingProviderFirstName"">
          <ns0:SUPER_PROVIDER_FNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM104_SupervisingProviderFirstName/text()"" />
          </ns0:SUPER_PROVIDER_FNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM107_SupervisingProviderNameSuffix"">
          <ns0:SUPER_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM107_SupervisingProviderNameSuffix/text()"" />
          </ns0:SUPER_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM108_IdentificationCodeQualifier"">
          <ns0:SUPER_PROVIDER_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:SUPER_PROVIDER_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM109_SupervisingProviderIdentifier"">
          <ns0:SUPER_PROVIDER_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM109_SupervisingProviderIdentifier/text()"" />
          </ns0:SUPER_PROVIDER_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM109_SupervisingProviderIdentifier"">
          <ns0:SUPER_PROVIDER_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310D_Loop1/s1:NM1_SupervisingProviderName_3/NM109_SupervisingProviderIdentifier/text()"" />
          </ns0:SUPER_PROVIDER_NPI_ID>
        </xsl:if>
        <ns0:SUPER_PROVIDER_REF>
          <xsl:value-of select=""$var:v211"" />
        </ns0:SUPER_PROVIDER_REF>
        <ns0:SERVICE_PROV_ENTITY_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM101_EntityIdentifierCode/text()"" />
        </ns0:SERVICE_PROV_ENTITY_QUAL>
        <ns0:SERVICE_PROV_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM102_EntityTypeQualifier/text()"" />
        </ns0:SERVICE_PROV_QUAL>
        <ns0:SERVICE_PROV_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM103_LaboratoryorFacilityName/text()"" />
        </ns0:SERVICE_PROV_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM108_IdentificationCodeQualifier"">
          <ns0:SERVICE_PROV_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:SERVICE_PROV_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM109_LaboratoryorFacilityPrimaryIdentifier"">
          <ns0:SERVICE_PROV_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM109_LaboratoryorFacilityPrimaryIdentifier/text()"" />
          </ns0:SERVICE_PROV_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM109_LaboratoryorFacilityPrimaryIdentifier"">
          <ns0:SERVICE_PROV_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:NM1_ServiceFacilityLocationName_2/NM109_LaboratoryorFacilityPrimaryIdentifier/text()"" />
          </ns0:SERVICE_PROV_NPI_ID>
        </xsl:if>
        <ns0:SERVICE_PROV_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N3_ServiceFacilityLocationAddress_3/N301_LaboratoryorFacilityAddressLine/text()"" />
        </ns0:SERVICE_PROV_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N3_ServiceFacilityLocationAddress_3/N302_LaboratoryorFacilityAddressLine"">
          <ns0:SERVICE_PROV_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N3_ServiceFacilityLocationAddress_3/N302_LaboratoryorFacilityAddressLine/text()"" />
          </ns0:SERVICE_PROV_ADD2>
        </xsl:if>
        <ns0:SERVICE_PROV_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_3/N401_LaboratoryorFacilityCityName/text()"" />
        </ns0:SERVICE_PROV_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_3/N402_LaboratoryorFacilityStateorProvinceCode"">
          <ns0:SERVICE_PROV_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_3/N402_LaboratoryorFacilityStateorProvinceCode/text()"" />
          </ns0:SERVICE_PROV_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_3/N403_LaboratoryorFacilityPostalZoneorZIPCode"">
          <ns0:SERVICE_PROV_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_3/N403_LaboratoryorFacilityPostalZoneorZIPCode/text()"" />
          </ns0:SERVICE_PROV_ZIP>
        </xsl:if>
        <ns0:SERVICE_PROV_REF>
          <xsl:value-of select=""$var:v218"" />
        </ns0:SERVICE_PROV_REF>
        <ns0:SERVICE_PROV_PER01>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER01_ContactFunctionCode/text()"" />
        </ns0:SERVICE_PROV_PER01>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER02_Name"">
          <ns0:SERVICE_PROV_PER02>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER02_Name/text()"" />
          </ns0:SERVICE_PROV_PER02>
        </xsl:if>
        <ns0:SERVICE_PROV_PER03>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER03_CommunicationNumberQualifier/text()"" />
        </ns0:SERVICE_PROV_PER03>
        <ns0:SERVICE_PROV_PER04>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER04_CommunicationNumber/text()"" />
        </ns0:SERVICE_PROV_PER04>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER05_CommunicationNumberQualifier"">
          <ns0:SERVICE_PROV_PER05>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER05_CommunicationNumberQualifier/text()"" />
          </ns0:SERVICE_PROV_PER05>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER06_CommunicationNumber"">
          <ns0:SERVICE_PROV_PER06>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310C_Loop1/s1:PER_ServiceFacilityContactInformation_2/PER06_CommunicationNumber/text()"" />
          </ns0:SERVICE_PROV_PER06>
        </xsl:if>
        <ns0:PRIMARY_SEQ_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode/text()"" />
        </ns0:PRIMARY_SEQ_NUMBER>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR02_IndividualRelationshipCode"">
          <ns0:PRIMARY_RELATION_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR02_IndividualRelationshipCode/text()"" />
          </ns0:PRIMARY_RELATION_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR04_SubscriberGroupName"">
          <ns0:PRIMARY_GROUP_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR04_SubscriberGroupName/text()"" />
          </ns0:PRIMARY_GROUP_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR05_InsuranceTypeCode"">
          <ns0:PRIMARY_INS_TYPE_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR05_InsuranceTypeCode/text()"" />
          </ns0:PRIMARY_INS_TYPE_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR09_ClaimFilingIndicatorCode"">
          <ns0:PRIMARY_CLAIM_IND>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR09_ClaimFilingIndicatorCode/text()"" />
          </ns0:PRIMARY_CLAIM_IND>
        </xsl:if>
        <ns0:PRIMARY_PAYER_REF>
          <xsl:value-of select=""$var:v231"" />
        </ns0:PRIMARY_PAYER_REF>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR03_SubscriberGrouporPolicyNumber"">
          <ns0:INSURED_GROUP_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:SBR_SubscriberInformation/SBR03_SubscriberGrouporPolicyNumber/text()"" />
          </ns0:INSURED_GROUP_ID>
        </xsl:if>
        <ns0:INSURED_PAYER_ID>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:NM1_PayerName/NM109_PayerIdentifier/text()"" />
        </ns0:INSURED_PAYER_ID>
        <ns0:INSURED_PAYER_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:NM1_PayerName/NM103_PayerName/text()"" />
        </ns0:INSURED_PAYER_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM108_IdentificationCodeQualifier"">
          <ns0:INSURED_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:INSURED_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM109_SubscriberPrimaryIdentifier"">
          <ns0:INSURED_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM109_SubscriberPrimaryIdentifier/text()"" />
          </ns0:INSURED_ID>
        </xsl:if>
        <ns0:INSURED_LAST_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM103_SubscriberLastName/text()"" />
        </ns0:INSURED_LAST_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM104_SubscriberFirstName"">
          <ns0:INSURED_FIRST_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM104_SubscriberFirstName/text()"" />
          </ns0:INSURED_FIRST_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM105_SubscriberMiddleNameorInitial"">
          <ns0:INSURED_MIDDLE_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM105_SubscriberMiddleNameorInitial/text()"" />
          </ns0:INSURED_MIDDLE_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM107_SubscriberNameSuffix"">
          <ns0:INSURED_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:NM1_SubscriberName/NM107_SubscriberNameSuffix/text()"" />
          </ns0:INSURED_SUFFIX>
        </xsl:if>
        <ns0:INSURED_GENDER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:DMG_SubscriberDemographicInformation/DMG03_SubscriberGenderCode/text()"" />
        </ns0:INSURED_GENDER>
        <ns0:INSURED_BIRTH_DATE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:DMG_SubscriberDemographicInformation/DMG02_SubscriberBirthDate/text()"" />
        </ns0:INSURED_BIRTH_DATE>
        <ns0:INSURED_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N301_SubscriberAddressLine/text()"" />
        </ns0:INSURED_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N302_SubscriberAddressLine"">
          <ns0:INSURED_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N302_SubscriberAddressLine/text()"" />
          </ns0:INSURED_ADD2>
        </xsl:if>
        <ns0:INSURED_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N401_SubscriberCityName/text()"" />
        </ns0:INSURED_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N402_SubscriberStateCode"">
          <ns0:INSURED_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N402_SubscriberStateCode/text()"" />
          </ns0:INSURED_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N403_SubscriberPostalZoneorZIPCode"">
          <ns0:INSURED_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N403_SubscriberPostalZoneorZIPCode/text()"" />
          </ns0:INSURED_ZIP>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT06_PatientDeathDate"">
          <ns0:INSURED_DEATH>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT06_PatientDeathDate/text()"" />
          </ns0:INSURED_DEATH>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT07_UnitorBasisforMeasurementCode"">
          <ns0:INSURED_UOM>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT07_UnitorBasisforMeasurementCode/text()"" />
          </ns0:INSURED_UOM>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT08_PatientWeight"">
          <ns0:INSURED_WEIGHT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT08_PatientWeight/text()"" />
          </ns0:INSURED_WEIGHT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT09_PregnancyIndicator"">
          <ns0:INSURED_PRG_IND>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:PAT_PatientInformation/PAT09_PregnancyIndicator/text()"" />
          </ns0:INSURED_PRG_IND>
        </xsl:if>
        <ns0:PATIENT_RELATION_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT01_IndividualRelationshipCode/text()"" />
        </ns0:PATIENT_RELATION_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM108_IdentificationCodeQualifier"">
          <ns0:PATIENT_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:PATIENT_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM109_IdentificationCode"">
          <ns0:PATIENT_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM109_IdentificationCode/text()"" />
          </ns0:PATIENT_ID>
        </xsl:if>
        <ns0:PATIENT_LAST_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM103_PatientLastName/text()"" />
        </ns0:PATIENT_LAST_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM104_PatientFirstName"">
          <ns0:PATIENT_FIRST_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM104_PatientFirstName/text()"" />
          </ns0:PATIENT_FIRST_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM105_PatientMiddleNameorInitial"">
          <ns0:PATIENT_MIDDLE_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:NM1_PatientName/NM105_PatientMiddleNameorInitial/text()"" />
          </ns0:PATIENT_MIDDLE_NAME>
        </xsl:if>
        <ns0:PATIENT_GENDER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:DMG_PatientDemographicInformation/DMG03_PatientGenderCode/text()"" />
        </ns0:PATIENT_GENDER>
        <ns0:PATIENT_BIRTH_DATE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:DMG_PatientDemographicInformation/DMG02_PatientBirthDate/text()"" />
        </ns0:PATIENT_BIRTH_DATE>
        <ns0:PATIENT_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N301_PatientAddressLine/text()"" />
        </ns0:PATIENT_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N302_PatientAddressLine"">
          <ns0:PATIENT_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N302_PatientAddressLine/text()"" />
          </ns0:PATIENT_ADD2>
        </xsl:if>
        <ns0:PATIENT_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N401_PatientCityName/text()"" />
        </ns0:PATIENT_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N402_PatientStateCode"">
          <ns0:PATIENT_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N402_PatientStateCode/text()"" />
          </ns0:PATIENT_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N403_PatientPostalZoneorZIPCode"">
          <ns0:PATIENT_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N403_PatientPostalZoneorZIPCode/text()"" />
          </ns0:PATIENT_ZIP>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT06_PatientDeathDate"">
          <ns0:PATIENT_DEATH>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT06_PatientDeathDate/text()"" />
          </ns0:PATIENT_DEATH>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT07_UnitorBasisforMeasurementCode"">
          <ns0:PATIENT_UOM>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT07_UnitorBasisforMeasurementCode/text()"" />
          </ns0:PATIENT_UOM>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT08_PatientWeight"">
          <ns0:PATIENT_WEIGHT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT08_PatientWeight/text()"" />
          </ns0:PATIENT_WEIGHT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT09_PregnancyIndicator"">
          <ns0:PATIENT_PRG_IND>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:PAT_PatientInformation_2/PAT09_PregnancyIndicator/text()"" />
          </ns0:PATIENT_PRG_IND>
        </xsl:if>
        <ns0:REPORT_TYPE_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK01_AttachmentReportTypeCode/text()"" />
        </ns0:REPORT_TYPE_CODE>
        <ns0:TRANSMISSION_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK02_AttachmentTransmissionCode/text()"" />
        </ns0:TRANSMISSION_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK05_IdentificationCodeQualifier"">
          <ns0:ID_CODER_QUALIFIER>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK05_IdentificationCodeQualifier/text()"" />
          </ns0:ID_CODER_QUALIFIER>
        </xsl:if>
        <ns0:CONTROL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_PayerClaimControlNumber_2/REF02_PayerClaimControlNumber/text()"" />
        </ns0:CONTROL_NUMBER>
        <ns0:FIXED_FORMAT_INFO>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:K3_FileInformation_3/K301_FixedFormatInformation/text()"" />
        </ns0:FIXED_FORMAT_INFO>
        <ns0:DRUG_PROD_QUAL>
          <xsl:text />
        </ns0:DRUG_PROD_QUAL>
        <ns0:NATIONAL_DRUG_CODE>
          <xsl:text />
        </ns0:NATIONAL_DRUG_CODE>
        <ns0:DRUG_UNIT_PRICE>
          <xsl:text />
        </ns0:DRUG_UNIT_PRICE>
        <ns0:DRUG_UNIT_COUNT>
          <xsl:text />
        </ns0:DRUG_UNIT_COUNT>
        <ns0:DRUG_CODE_QUAL>
          <xsl:text />
        </ns0:DRUG_CODE_QUAL>
        <ns0:PRE_CODE_QUAL>
          <xsl:text />
        </ns0:PRE_CODE_QUAL>
        <ns0:PRE_NUMBER>
          <xsl:text />
        </ns0:PRE_NUMBER>
        <ns0:PAY_TO_PLAN_ID>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM109_Pay_toPlanPrimaryIdentifier/text()"" />
        </ns0:PAY_TO_PLAN_ID>
        <ns0:PAY_TO_PLAN_ENTITYQUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM108_IdentificationCodeQualifier/text()"" />
        </ns0:PAY_TO_PLAN_ENTITYQUAL>
        <ns0:PAY_TO_PLAN_LASTNAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM103_Pay_toPlanOrganizationalName/text()"" />
        </ns0:PAY_TO_PLAN_LASTNAME>
        <ns0:PAY_TO_PLAN_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N301_Pay_toPlanAddressLine/text()"" />
        </ns0:PAY_TO_PLAN_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N302_Pay_toPlanAddressLine"">
          <ns0:PAY_TO_PLAN_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N3_Pay_ToPlanAddress/N302_Pay_toPlanAddressLine/text()"" />
          </ns0:PAY_TO_PLAN_ADD2>
        </xsl:if>
        <ns0:PAY_TO_PLAN_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N401_Pay_toPlanCityName/text()"" />
        </ns0:PAY_TO_PLAN_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N402_Pay_toPlanStateorProvinceCode"">
          <ns0:PAY_TO_PLAN_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N402_Pay_toPlanStateorProvinceCode/text()"" />
          </ns0:PAY_TO_PLAN_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N403_Pay_toPlanPostalZoneorZIPCode"">
          <ns0:PAY_TO_PLAN_ZIPCODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:N4_Pay_ToPlanCity_State_ZIPCode/N403_Pay_toPlanPostalZoneorZIPCode/text()"" />
          </ns0:PAY_TO_PLAN_ZIPCODE>
        </xsl:if>
        <ns0:PAY_TO_PLAN_REF>
          <xsl:value-of select=""$var:v232"" />
        </ns0:PAY_TO_PLAN_REF>
        <ns0:AMBULANCE_PICKUP_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N3_AmbulancePick_upLocationAddress_3/N301_AmbulancePick_upAddressLine/text()"" />
        </ns0:AMBULANCE_PICKUP_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N3_AmbulancePick_upLocationAddress_3/N302_AmbulancePick_upAddressLine"">
          <ns0:AMBULANCE_PICKUP_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N3_AmbulancePick_upLocationAddress_3/N302_AmbulancePick_upAddressLine/text()"" />
          </ns0:AMBULANCE_PICKUP_ADD2>
        </xsl:if>
        <ns0:AMBULANCE_PICKUP_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_3/N401_AmbulancePick_upCityName/text()"" />
        </ns0:AMBULANCE_PICKUP_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_3/N402_AmbulancePick_upStateorProvinceCode"">
          <ns0:AMBULANCE_PICKUP_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_3/N402_AmbulancePick_upStateorProvinceCode/text()"" />
          </ns0:AMBULANCE_PICKUP_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_3/N403_AmbulancePick_upPostalZoneorZIPCode"">
          <ns0:AMBULANCE_PICKUP_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310E_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_3/N403_AmbulancePick_upPostalZoneorZIPCode/text()"" />
          </ns0:AMBULANCE_PICKUP_ZIP>
        </xsl:if>
        <ns0:AMBULANCE_DROPOFF_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_3/N301_AmbulanceDrop_offAddressLine/text()"" />
        </ns0:AMBULANCE_DROPOFF_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_3/N302_AmbulanceDrop_offAddressLine"">
          <ns0:AMBULANCE_DROPOFF_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_3/N302_AmbulanceDrop_offAddressLine/text()"" />
          </ns0:AMBULANCE_DROPOFF_ADD2>
        </xsl:if>
        <ns0:AMBULANCE_DROPOFF_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_3/N401_AmbulanceDrop_offCityName/text()"" />
        </ns0:AMBULANCE_DROPOFF_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_3/N402_AmbulanceDrop_offStateorProvinceCode"">
          <ns0:AMBULANCE_DROPOFF_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_3/N402_AmbulanceDrop_offStateorProvinceCode/text()"" />
          </ns0:AMBULANCE_DROPOFF_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_3/N403_AmbulanceDrop_offPostalZoneorZIPCode"">
          <ns0:AMBULANCE_DROPOFF_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_3/N403_AmbulanceDrop_offPostalZoneorZIPCode/text()"" />
          </ns0:AMBULANCE_DROPOFF_ZIP>
        </xsl:if>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v233"" select=""position()"" />
                  <xsl:variable name=""var:v234"" select=""userCSharp:LogicalEq(string($var:v233) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v234"">
                    <xsl:variable name=""var:v235"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode))"" />
                    <xsl:if test=""string($var:v235)='true'"">
                      <xsl:variable name=""var:v236"" select=""s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode/text()"" />
                      <ns0:SEC_SEQ_NUMBER>
                        <xsl:value-of select=""$var:v236"" />
                      </ns0:SEC_SEQ_NUMBER>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v237"" select=""position()"" />
                  <xsl:variable name=""var:v238"" select=""userCSharp:LogicalEq(string($var:v237) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v238"">
                    <xsl:variable name=""var:v239"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR02_IndividualRelationshipCode))"" />
                    <xsl:if test=""string($var:v239)='true'"">
                      <xsl:variable name=""var:v240"" select=""s1:SBR_OtherSubscriberInformation_2/SBR02_IndividualRelationshipCode/text()"" />
                      <ns0:SEC_RELATION_CODE>
                        <xsl:value-of select=""$var:v240"" />
                      </ns0:SEC_RELATION_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v241"" select=""position()"" />
                  <xsl:variable name=""var:v242"" select=""userCSharp:LogicalEq(string($var:v241) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v242"">
                    <xsl:variable name=""var:v243"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR03_InsuredGrouporPolicyNumber))"" />
                    <xsl:if test=""string($var:v243)='true'"">
                      <xsl:variable name=""var:v244"" select=""s1:SBR_OtherSubscriberInformation_2/SBR03_InsuredGrouporPolicyNumber/text()"" />
                      <ns0:SEC_GROUP_ID>
                        <xsl:value-of select=""$var:v244"" />
                      </ns0:SEC_GROUP_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v245"" select=""position()"" />
                  <xsl:variable name=""var:v246"" select=""userCSharp:LogicalEq(string($var:v245) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v246"">
                    <xsl:variable name=""var:v247"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR04_OtherInsuredGroupName))"" />
                    <xsl:if test=""string($var:v247)='true'"">
                      <xsl:variable name=""var:v248"" select=""s1:SBR_OtherSubscriberInformation_2/SBR04_OtherInsuredGroupName/text()"" />
                      <ns0:SEC_GROUP_NAME>
                        <xsl:value-of select=""$var:v248"" />
                      </ns0:SEC_GROUP_NAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v249"" select=""position()"" />
                  <xsl:variable name=""var:v250"" select=""userCSharp:LogicalEq(string($var:v249) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v250"">
                    <xsl:variable name=""var:v251"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR09_ClaimFilingIndicatorCode))"" />
                    <xsl:if test=""string($var:v251)='true'"">
                      <xsl:variable name=""var:v252"" select=""s1:SBR_OtherSubscriberInformation_2/SBR09_ClaimFilingIndicatorCode/text()"" />
                      <ns0:SEC_CLAIM_IND>
                        <xsl:value-of select=""$var:v252"" />
                      </ns0:SEC_CLAIM_IND>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v253"" select=""position()"" />
                  <xsl:variable name=""var:v254"" select=""userCSharp:LogicalEq(string($var:v253) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v254"">
                    <xsl:variable name=""var:v255"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation_2/SBR05_InsuranceTypeCode))"" />
                    <xsl:if test=""string($var:v255)='true'"">
                      <xsl:variable name=""var:v256"" select=""s1:SBR_OtherSubscriberInformation_2/SBR05_InsuranceTypeCode/text()"" />
                      <ns0:SEC_INS_TYPE_CODE>
                        <xsl:value-of select=""$var:v256"" />
                      </ns0:SEC_INS_TYPE_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v257"" select=""position()"" />
                  <xsl:variable name=""var:v258"" select=""userCSharp:LogicalEq(string($var:v257) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v258"">
                    <xsl:variable name=""var:v259"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI03_BenefitsAssignmentCertificationIndicator))"" />
                    <xsl:if test=""string($var:v259)='true'"">
                      <xsl:variable name=""var:v260"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI03_BenefitsAssignmentCertificationIndicator/text()"" />
                      <ns0:SEC_ASSIGN_BENRFIT_IND>
                        <xsl:value-of select=""$var:v260"" />
                      </ns0:SEC_ASSIGN_BENRFIT_IND>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v261"" select=""position()"" />
                  <xsl:variable name=""var:v262"" select=""userCSharp:LogicalEq(string($var:v261) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v262"">
                    <xsl:variable name=""var:v263"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI04_PatientSignatureSourceCode))"" />
                    <xsl:if test=""string($var:v263)='true'"">
                      <xsl:variable name=""var:v264"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI04_PatientSignatureSourceCode/text()"" />
                      <ns0:SEC_PAT_SIGN_SRC_CODE>
                        <xsl:value-of select=""$var:v264"" />
                      </ns0:SEC_PAT_SIGN_SRC_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v265"" select=""position()"" />
                  <xsl:variable name=""var:v266"" select=""userCSharp:LogicalEq(string($var:v265) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v266"">
                    <xsl:variable name=""var:v267"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI06_ReleaseofInformationCode))"" />
                    <xsl:if test=""string($var:v267)='true'"">
                      <xsl:variable name=""var:v268"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI06_ReleaseofInformationCode/text()"" />
                      <ns0:SEC_RELEASE_INFO_CODE>
                        <xsl:value-of select=""$var:v268"" />
                      </ns0:SEC_RELEASE_INFO_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v269"" select=""position()"" />
                  <xsl:variable name=""var:v270"" select=""userCSharp:LogicalEq(string($var:v269) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v270"">
                    <xsl:variable name=""var:v271"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM103_OtherInsuredLastName))"" />
                    <xsl:if test=""string($var:v271)='true'"">
                      <xsl:variable name=""var:v272"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM103_OtherInsuredLastName/text()"" />
                      <ns0:SEC_INSURED_LNAME>
                        <xsl:value-of select=""$var:v272"" />
                      </ns0:SEC_INSURED_LNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v273"" select=""position()"" />
                  <xsl:variable name=""var:v274"" select=""userCSharp:LogicalEq(string($var:v273) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v274"">
                    <xsl:variable name=""var:v275"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM104_OtherInsuredFirstName))"" />
                    <xsl:if test=""string($var:v275)='true'"">
                      <xsl:variable name=""var:v276"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM104_OtherInsuredFirstName/text()"" />
                      <ns0:SEC_INSURED_FNAME>
                        <xsl:value-of select=""$var:v276"" />
                      </ns0:SEC_INSURED_FNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v277"" select=""position()"" />
                  <xsl:variable name=""var:v278"" select=""userCSharp:LogicalEq(string($var:v277) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v278"">
                    <xsl:variable name=""var:v279"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM105_OtherInsuredMiddleName))"" />
                    <xsl:if test=""string($var:v279)='true'"">
                      <xsl:variable name=""var:v280"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM105_OtherInsuredMiddleName/text()"" />
                      <ns0:SEC_INSURED_MNAME>
                        <xsl:value-of select=""$var:v280"" />
                      </ns0:SEC_INSURED_MNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v281"" select=""position()"" />
                  <xsl:variable name=""var:v282"" select=""userCSharp:LogicalEq(string($var:v281) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v282"">
                    <xsl:variable name=""var:v283"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM107_OtherInsuredNameSuffix))"" />
                    <xsl:if test=""string($var:v283)='true'"">
                      <xsl:variable name=""var:v284"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM107_OtherInsuredNameSuffix/text()"" />
                      <ns0:SEC_INSURED_SUFFIX>
                        <xsl:value-of select=""$var:v284"" />
                      </ns0:SEC_INSURED_SUFFIX>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v285"" select=""position()"" />
                  <xsl:variable name=""var:v286"" select=""userCSharp:LogicalEq(string($var:v285) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v286"">
                    <xsl:variable name=""var:v287"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM108_IdentificationCodeQualifier))"" />
                    <xsl:if test=""string($var:v287)='true'"">
                      <xsl:variable name=""var:v288"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM108_IdentificationCodeQualifier/text()"" />
                      <ns0:SEC_INSURED_ID_QUAL>
                        <xsl:value-of select=""$var:v288"" />
                      </ns0:SEC_INSURED_ID_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v289"" select=""position()"" />
                  <xsl:variable name=""var:v290"" select=""userCSharp:LogicalEq(string($var:v289) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v290"">
                    <xsl:variable name=""var:v291"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM109_OtherInsuredIdentifier))"" />
                    <xsl:if test=""string($var:v291)='true'"">
                      <xsl:variable name=""var:v292"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM109_OtherInsuredIdentifier/text()"" />
                      <ns0:SEC_INSURED_ID>
                        <xsl:value-of select=""$var:v292"" />
                      </ns0:SEC_INSURED_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v293"" select=""position()"" />
                  <xsl:variable name=""var:v294"" select=""userCSharp:LogicalEq(string($var:v293) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v294"">
                    <xsl:variable name=""var:v295"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM103_OtherPayerOrganizationName))"" />
                    <xsl:if test=""string($var:v295)='true'"">
                      <xsl:variable name=""var:v296"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM103_OtherPayerOrganizationName/text()"" />
                      <ns0:SEC_PAYER_NAME>
                        <xsl:value-of select=""$var:v296"" />
                      </ns0:SEC_PAYER_NAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v297"" select=""position()"" />
                  <xsl:variable name=""var:v298"" select=""userCSharp:LogicalEq(string($var:v297) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v298"">
                    <xsl:variable name=""var:v299"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM109_OtherPayerPrimaryIdentifier))"" />
                    <xsl:if test=""string($var:v299)='true'"">
                      <xsl:variable name=""var:v300"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM109_OtherPayerPrimaryIdentifier/text()"" />
                      <ns0:SEC_PAYER_ID>
                        <xsl:value-of select=""$var:v300"" />
                      </ns0:SEC_PAYER_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:SEC_INSURED_GENDER>
          <xsl:text />
        </ns0:SEC_INSURED_GENDER>
        <ns0:SEC_INSURED_DOB>
          <xsl:text />
        </ns0:SEC_INSURED_DOB>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v301"" select=""position()"" />
                  <xsl:variable name=""var:v302"" select=""userCSharp:LogicalEq(string($var:v301) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v302"">
                    <xsl:variable name=""var:v303"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N301_OtherInsuredAddressLine))"" />
                    <xsl:if test=""string($var:v303)='true'"">
                      <xsl:variable name=""var:v304"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N301_OtherInsuredAddressLine/text()"" />
                      <ns0:SEC_INSURED_ADD1>
                        <xsl:value-of select=""$var:v304"" />
                      </ns0:SEC_INSURED_ADD1>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v305"" select=""position()"" />
                  <xsl:variable name=""var:v306"" select=""userCSharp:LogicalEq(string($var:v305) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v306"">
                    <xsl:variable name=""var:v307"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N302_OtherInsuredAddressLine))"" />
                    <xsl:if test=""string($var:v307)='true'"">
                      <xsl:variable name=""var:v308"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N302_OtherInsuredAddressLine/text()"" />
                      <ns0:SEC_INSURED_ADD2>
                        <xsl:value-of select=""$var:v308"" />
                      </ns0:SEC_INSURED_ADD2>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v309"" select=""position()"" />
                  <xsl:variable name=""var:v310"" select=""userCSharp:LogicalEq(string($var:v309) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v310"">
                    <xsl:variable name=""var:v311"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N401_OtherSubscriberCityName))"" />
                    <xsl:if test=""string($var:v311)='true'"">
                      <xsl:variable name=""var:v312"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N401_OtherSubscriberCityName/text()"" />
                      <ns0:SEC_INSURED_CITY>
                        <xsl:value-of select=""$var:v312"" />
                      </ns0:SEC_INSURED_CITY>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v313"" select=""position()"" />
                  <xsl:variable name=""var:v314"" select=""userCSharp:LogicalEq(string($var:v313) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v314"">
                    <xsl:variable name=""var:v315"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N402_OtherSubscriberStateorProvinceCode))"" />
                    <xsl:if test=""string($var:v315)='true'"">
                      <xsl:variable name=""var:v316"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N402_OtherSubscriberStateorProvinceCode/text()"" />
                      <ns0:SEC_INSURED_STATE>
                        <xsl:value-of select=""$var:v316"" />
                      </ns0:SEC_INSURED_STATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v317"" select=""position()"" />
                  <xsl:variable name=""var:v318"" select=""userCSharp:LogicalEq(string($var:v317) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v318"">
                    <xsl:variable name=""var:v319"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N403_OtherSubscriberPostalZoneorZIPCode))"" />
                    <xsl:if test=""string($var:v319)='true'"">
                      <xsl:variable name=""var:v320"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N403_OtherSubscriberPostalZoneorZIPCode/text()"" />
                      <ns0:SEC_INSURED_ZIP>
                        <xsl:value-of select=""$var:v320"" />
                      </ns0:SEC_INSURED_ZIP>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v321"" select=""position()"" />
                  <xsl:variable name=""var:v322"" select=""userCSharp:LogicalEq(string($var:v321) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v322"">
                    <xsl:variable name=""var:v323"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments_2/CAS01_ClaimAdjustmentGroupCode))"" />
                    <xsl:if test=""string($var:v323)='true'"">
                      <xsl:variable name=""var:v324"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS01_ClaimAdjustmentGroupCode/text()"" />
                      <ns0:SEC_CAS01_CODE>
                        <xsl:value-of select=""$var:v324"" />
                      </ns0:SEC_CAS01_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v325"" select=""position()"" />
                  <xsl:variable name=""var:v326"" select=""userCSharp:LogicalEq(string($var:v325) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v326"">
                    <xsl:variable name=""var:v327"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments_2/CAS02_AdjustmentReasonCode))"" />
                    <xsl:if test=""string($var:v327)='true'"">
                      <xsl:variable name=""var:v328"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS02_AdjustmentReasonCode/text()"" />
                      <ns0:SEC_CAS02_REASON>
                        <xsl:value-of select=""$var:v328"" />
                      </ns0:SEC_CAS02_REASON>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v329"" select=""position()"" />
                  <xsl:variable name=""var:v330"" select=""userCSharp:LogicalEq(string($var:v329) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v330"">
                    <xsl:variable name=""var:v331"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments_2/CAS03_AdjustmentAmount))"" />
                    <xsl:if test=""string($var:v331)='true'"">
                      <xsl:variable name=""var:v332"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS03_AdjustmentAmount/text()"" />
                      <ns0:SEC_CAS03_AMT>
                        <xsl:value-of select=""$var:v332"" />
                      </ns0:SEC_CAS03_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v333"" select=""position()"" />
                  <xsl:variable name=""var:v334"" select=""userCSharp:LogicalEq(string($var:v333) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v334"">
                    <xsl:variable name=""var:v335"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount))"" />
                    <xsl:if test=""string($var:v335)='true'"">
                      <xsl:variable name=""var:v336"" select=""s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()"" />
                      <ns0:SEC_PAYERPAID_AMT>
                        <xsl:value-of select=""$var:v336"" />
                      </ns0:SEC_PAYERPAID_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v337"" select=""position()"" />
                  <xsl:variable name=""var:v338"" select=""userCSharp:LogicalEq(string($var:v337) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v338"">
                    <xsl:variable name=""var:v339"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount))"" />
                    <xsl:if test=""string($var:v339)='true'"">
                      <xsl:variable name=""var:v340"" select=""s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount/text()"" />
                      <ns0:SEC_NONCOVERED_AMT>
                        <xsl:value-of select=""$var:v340"" />
                      </ns0:SEC_NONCOVERED_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v341"" select=""position()"" />
                  <xsl:variable name=""var:v342"" select=""userCSharp:LogicalEq(string($var:v341) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v342"">
                    <xsl:variable name=""var:v343"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3/AMT02_RemainingPatientLiability))"" />
                    <xsl:if test=""string($var:v343)='true'"">
                      <xsl:variable name=""var:v344"" select=""s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3/AMT02_RemainingPatientLiability/text()"" />
                      <ns0:SEC_LIABILITY_AMT>
                        <xsl:value-of select=""$var:v344"" />
                      </ns0:SEC_LIABILITY_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v345"" select=""position()"" />
                  <xsl:variable name=""var:v346"" select=""userCSharp:LogicalEq(string($var:v345) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v346"">
                    <xsl:variable name=""var:v347"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:REF_OtherSubscriberSecondaryIdentification_2/REF02_OtherInsuredAdditionalIdentifier))"" />
                    <xsl:if test=""string($var:v347)='true'"">
                      <xsl:variable name=""var:v348"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:REF_OtherSubscriberSecondaryIdentification_2/REF02_OtherInsuredAdditionalIdentifier/text()"" />
                      <ns0:SEC_INSURED_SSN_REF>
                        <xsl:value-of select=""$var:v348"" />
                      </ns0:SEC_INSURED_SSN_REF>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v349"" select=""position()"" />
                  <xsl:variable name=""var:v350"" select=""userCSharp:LogicalEq(string($var:v349) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v350"">
                    <xsl:variable name=""var:v351"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N301_OtherPayerAddressLine))"" />
                    <xsl:if test=""string($var:v351)='true'"">
                      <xsl:variable name=""var:v352"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N301_OtherPayerAddressLine/text()"" />
                      <ns0:SEC_PAYER_ADD1>
                        <xsl:value-of select=""$var:v352"" />
                      </ns0:SEC_PAYER_ADD1>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v353"" select=""position()"" />
                  <xsl:variable name=""var:v354"" select=""userCSharp:LogicalEq(string($var:v353) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v354"">
                    <xsl:variable name=""var:v355"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N302_OtherPayerAddressLine))"" />
                    <xsl:if test=""string($var:v355)='true'"">
                      <xsl:variable name=""var:v356"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N302_OtherPayerAddressLine/text()"" />
                      <ns0:SEC_PAYER_ADD2>
                        <xsl:value-of select=""$var:v356"" />
                      </ns0:SEC_PAYER_ADD2>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v357"" select=""position()"" />
                  <xsl:variable name=""var:v358"" select=""userCSharp:LogicalEq(string($var:v357) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v358"">
                    <xsl:variable name=""var:v359"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N401_OtherPayerCityName))"" />
                    <xsl:if test=""string($var:v359)='true'"">
                      <xsl:variable name=""var:v360"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N401_OtherPayerCityName/text()"" />
                      <ns0:SEC_PAYER_CITY>
                        <xsl:value-of select=""$var:v360"" />
                      </ns0:SEC_PAYER_CITY>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v361"" select=""position()"" />
                  <xsl:variable name=""var:v362"" select=""userCSharp:LogicalEq(string($var:v361) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v362"">
                    <xsl:variable name=""var:v363"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N402_OtherPayerStateorProvinceCode))"" />
                    <xsl:if test=""string($var:v363)='true'"">
                      <xsl:variable name=""var:v364"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N402_OtherPayerStateorProvinceCode/text()"" />
                      <ns0:SEC_PAYER_STATE>
                        <xsl:value-of select=""$var:v364"" />
                      </ns0:SEC_PAYER_STATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v365"" select=""position()"" />
                  <xsl:variable name=""var:v366"" select=""userCSharp:LogicalEq(string($var:v365) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v366"">
                    <xsl:variable name=""var:v367"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N403_OtherPayerPostalZoneorZIPCode))"" />
                    <xsl:if test=""string($var:v367)='true'"">
                      <xsl:variable name=""var:v368"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N403_OtherPayerPostalZoneorZIPCode/text()"" />
                      <ns0:SEC_PAYER_ZIPCODE>
                        <xsl:value-of select=""$var:v368"" />
                      </ns0:SEC_PAYER_ZIPCODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v369"" select=""position()"" />
                  <xsl:variable name=""var:v370"" select=""userCSharp:LogicalEq(string($var:v369) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v370"">
                    <xsl:variable name=""var:v371"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate))"" />
                    <xsl:if test=""string($var:v371)='true'"">
                      <xsl:variable name=""var:v372"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate/text()"" />
                      <ns0:SEC_PAYER_REMITTANCE_DATE>
                        <xsl:value-of select=""$var:v372"" />
                      </ns0:SEC_PAYER_REMITTANCE_DATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v373"" select=""position()"" />
                  <xsl:variable name=""var:v374"" select=""userCSharp:LogicalEq(string($var:v373) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v374"">
                    <xsl:variable name=""var:v375"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v376"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[1]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v377"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v378"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[2]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v379"" select=""userCSharp:StringConcat(string($var:v375) , &quot;:&quot; , string($var:v376) , &quot;,&quot; , string($var:v377) , &quot;:&quot; , string($var:v378) , &quot;,&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerPriorAuthorizationNumber_2/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerPriorAuthorizationNumber_2/REF02_OtherPayerPriorAuthorizationNumber/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerReferralNumber_2/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerReferralNumber_2/REF02_OtherPayerPriorAuthorizationorReferralNumber/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimAdjustmentIndicator_2/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimAdjustmentIndicator_2/REF02_OtherPayerClaimAdjustmentIndicator/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimControlNumber_2/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimControlNumber_2/REF02_OtherPayer_sClaimControlNumber/text()))"" />
                    <ns0:SEC_PAYER_REF>
                      <xsl:value-of select=""$var:v379"" />
                    </ns0:SEC_PAYER_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v380"" select=""position()"" />
                  <xsl:variable name=""var:v381"" select=""userCSharp:LogicalEq(string($var:v380) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v381"">
                    <xsl:variable name=""var:v382"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:NM1_OtherPayerReferringProvider_2/NM102_EntityTypeQualifier))"" />
                    <xsl:if test=""string($var:v382)='true'"">
                      <xsl:variable name=""var:v383"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:NM1_OtherPayerReferringProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:SEC_INSURED_REFERING_QUAL>
                        <xsl:value-of select=""$var:v383"" />
                      </ns0:SEC_INSURED_REFERING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v384"" select=""position()"" />
                  <xsl:variable name=""var:v385"" select=""userCSharp:LogicalEq(string($var:v384) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v385"">
                    <xsl:variable name=""var:v386"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v387"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[1]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v388"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v389"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[2]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v390"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v391"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[3]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v392"" select=""userCSharp:StringConcat(string($var:v386) , &quot;:&quot; , string($var:v387) , &quot;,&quot; , string($var:v388) , &quot;:&quot; , string($var:v389) , &quot;,&quot; , string($var:v390) , &quot;:&quot; , string($var:v391) , &quot;,&quot;)"" />
                    <ns0:SEC_INSURED_REFERING_REF>
                      <xsl:value-of select=""$var:v392"" />
                    </ns0:SEC_INSURED_REFERING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v393"" select=""position()"" />
                  <xsl:variable name=""var:v394"" select=""userCSharp:LogicalEq(string($var:v393) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v394"">
                    <xsl:variable name=""var:v395"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:NM1_OtherPayerRenderingProvider_2/NM102_EntityTypeQualifier))"" />
                    <xsl:if test=""string($var:v395)='true'"">
                      <xsl:variable name=""var:v396"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:NM1_OtherPayerRenderingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:SEC_INSURED_RENDERING_QUAL>
                        <xsl:value-of select=""$var:v396"" />
                      </ns0:SEC_INSURED_RENDERING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v397"" select=""position()"" />
                  <xsl:variable name=""var:v398"" select=""userCSharp:LogicalEq(string($var:v397) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v398"">
                    <xsl:variable name=""var:v399"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v400"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[1]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v401"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v402"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[2]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v403"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v404"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[3]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v405"" select=""userCSharp:StringConcat(string($var:v399) , &quot;:&quot; , string($var:v400) , &quot;,&quot; , string($var:v401) , &quot;:&quot; , string($var:v402) , &quot;,&quot; , string($var:v403) , &quot;:&quot; , string($var:v404) , &quot;,&quot;)"" />
                    <ns0:SEC_INSURED_RENDERING_REF>
                      <xsl:value-of select=""$var:v405"" />
                    </ns0:SEC_INSURED_RENDERING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v406"" select=""position()"" />
                  <xsl:variable name=""var:v407"" select=""userCSharp:LogicalEq(string($var:v406) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v407"">
                    <xsl:variable name=""var:v408"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:NM1_OtherPayerServiceFacilityLocation_2/NM102_EntityTypeQualifier))"" />
                    <xsl:if test=""string($var:v408)='true'"">
                      <xsl:variable name=""var:v409"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:NM1_OtherPayerServiceFacilityLocation_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:SEC_INSURED_SERVICEFACILITY_QUAL>
                        <xsl:value-of select=""$var:v409"" />
                      </ns0:SEC_INSURED_SERVICEFACILITY_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v410"" select=""position()"" />
                  <xsl:variable name=""var:v411"" select=""userCSharp:LogicalEq(string($var:v410) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v411"">
                    <xsl:variable name=""var:v412"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v413"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[1]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v414"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v415"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[2]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v416"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v417"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[3]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v418"" select=""userCSharp:StringConcat(string($var:v412) , &quot;:&quot; , string($var:v413) , &quot;,&quot; , string($var:v414) , &quot;:&quot; , string($var:v415) , &quot;,&quot; , string($var:v416) , &quot;:&quot; , string($var:v417) , &quot;,&quot;)"" />
                    <ns0:SEC_INSURED_SERVICEFACILITY_REF>
                      <xsl:value-of select=""$var:v418"" />
                    </ns0:SEC_INSURED_SERVICEFACILITY_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v419"" select=""position()"" />
                  <xsl:variable name=""var:v420"" select=""userCSharp:LogicalEq(string($var:v419) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v420"">
                    <xsl:variable name=""var:v421"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:NM1_OtherPayerSupervisingProvider_2/NM102_EntityTypeQualifier))"" />
                    <xsl:if test=""string($var:v421)='true'"">
                      <xsl:variable name=""var:v422"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:NM1_OtherPayerSupervisingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:SEC_INSURED_SUPERVISING_QUAL>
                        <xsl:value-of select=""$var:v422"" />
                      </ns0:SEC_INSURED_SUPERVISING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v423"" select=""position()"" />
                  <xsl:variable name=""var:v424"" select=""userCSharp:LogicalEq(string($var:v423) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v424"">
                    <xsl:variable name=""var:v425"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v426"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[1]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v427"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v428"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[2]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v429"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v430"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[3]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v431"" select=""userCSharp:StringConcat(string($var:v425) , &quot;:&quot; , string($var:v426) , &quot;,&quot; , string($var:v427) , &quot;:&quot; , string($var:v428) , &quot;,&quot; , string($var:v429) , &quot;:&quot; , string($var:v430) , &quot;,&quot;)"" />
                    <ns0:SEC_INSURED_SUPERVISING_REF>
                      <xsl:value-of select=""$var:v431"" />
                    </ns0:SEC_INSURED_SUPERVISING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v432"" select=""position()"" />
                  <xsl:variable name=""var:v433"" select=""userCSharp:LogicalEq(string($var:v432) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v433"">
                    <xsl:variable name=""var:v434"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:NM1_OtherPayerBillingProvider_2/NM102_EntityTypeQualifier))"" />
                    <xsl:if test=""string($var:v434)='true'"">
                      <xsl:variable name=""var:v435"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:NM1_OtherPayerBillingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:SEC_INSURED_BILLING_QUAL>
                        <xsl:value-of select=""$var:v435"" />
                      </ns0:SEC_INSURED_BILLING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v436"" select=""position()"" />
                  <xsl:variable name=""var:v437"" select=""userCSharp:LogicalEq(string($var:v436) , &quot;1&quot;)"" />
                  <xsl:if test=""$var:v437"">
                    <xsl:variable name=""var:v438"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v439"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[1]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v440"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v441"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[2]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v442"" select=""userCSharp:StringConcat(string($var:v438) , &quot;:&quot; , string($var:v439) , &quot;,&quot; , string($var:v440) , &quot;:&quot; , string($var:v441) , &quot;,&quot;)"" />
                    <ns0:SEC_INSURED_BILLING_REF>
                      <xsl:value-of select=""$var:v442"" />
                    </ns0:SEC_INSURED_BILLING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v443"" select=""position()"" />
                  <xsl:variable name=""var:v444"" select=""userCSharp:LogicalEq(string($var:v443) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v444"">
                    <xsl:variable name=""var:v445"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode)"" />
                    <xsl:variable name=""var:v446"" select=""userCSharp:LogicalExistence($var:v445)"" />
                    <xsl:if test=""string($var:v446)='true'"">
                      <xsl:variable name=""var:v447"" select=""s1:SBR_OtherSubscriberInformation_2/SBR01_PayerResponsibilitySequenceNumberCode/text()"" />
                      <ns0:TRI_SEQ_NUMBER>
                        <xsl:value-of select=""$var:v447"" />
                      </ns0:TRI_SEQ_NUMBER>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v448"" select=""position()"" />
                  <xsl:variable name=""var:v449"" select=""userCSharp:LogicalEq(string($var:v448) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v449"">
                    <xsl:variable name=""var:v450"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR02_IndividualRelationshipCode)"" />
                    <xsl:variable name=""var:v451"" select=""userCSharp:LogicalExistence($var:v450)"" />
                    <xsl:if test=""string($var:v451)='true'"">
                      <xsl:variable name=""var:v452"" select=""s1:SBR_OtherSubscriberInformation_2/SBR02_IndividualRelationshipCode/text()"" />
                      <ns0:TRI_RELATION_CODE>
                        <xsl:value-of select=""$var:v452"" />
                      </ns0:TRI_RELATION_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v453"" select=""position()"" />
                  <xsl:variable name=""var:v454"" select=""userCSharp:LogicalEq(string($var:v453) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v454"">
                    <xsl:variable name=""var:v455"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR03_InsuredGrouporPolicyNumber)"" />
                    <xsl:variable name=""var:v456"" select=""userCSharp:LogicalExistence($var:v455)"" />
                    <xsl:if test=""string($var:v456)='true'"">
                      <xsl:variable name=""var:v457"" select=""s1:SBR_OtherSubscriberInformation_2/SBR03_InsuredGrouporPolicyNumber/text()"" />
                      <ns0:TRI_GROUP_ID>
                        <xsl:value-of select=""$var:v457"" />
                      </ns0:TRI_GROUP_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v458"" select=""position()"" />
                  <xsl:variable name=""var:v459"" select=""userCSharp:LogicalEq(string($var:v458) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v459"">
                    <xsl:variable name=""var:v460"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR04_OtherInsuredGroupName)"" />
                    <xsl:variable name=""var:v461"" select=""userCSharp:LogicalExistence($var:v460)"" />
                    <xsl:if test=""string($var:v461)='true'"">
                      <xsl:variable name=""var:v462"" select=""s1:SBR_OtherSubscriberInformation_2/SBR04_OtherInsuredGroupName/text()"" />
                      <ns0:TRI_GROUP_NAME>
                        <xsl:value-of select=""$var:v462"" />
                      </ns0:TRI_GROUP_NAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v463"" select=""position()"" />
                  <xsl:variable name=""var:v464"" select=""userCSharp:LogicalEq(string($var:v463) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v464"">
                    <xsl:variable name=""var:v465"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR09_ClaimFilingIndicatorCode)"" />
                    <xsl:variable name=""var:v466"" select=""userCSharp:LogicalExistence($var:v465)"" />
                    <xsl:if test=""string($var:v466)='true'"">
                      <xsl:variable name=""var:v467"" select=""s1:SBR_OtherSubscriberInformation_2/SBR09_ClaimFilingIndicatorCode/text()"" />
                      <ns0:TRI_CLAIM_IND>
                        <xsl:value-of select=""$var:v467"" />
                      </ns0:TRI_CLAIM_IND>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v468"" select=""position()"" />
                  <xsl:variable name=""var:v469"" select=""userCSharp:LogicalEq(string($var:v468) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v469"">
                    <xsl:variable name=""var:v470"" select=""boolean(s1:SBR_OtherSubscriberInformation_2/SBR05_InsuranceTypeCode)"" />
                    <xsl:variable name=""var:v471"" select=""userCSharp:LogicalExistence($var:v470)"" />
                    <xsl:if test=""string($var:v471)='true'"">
                      <xsl:variable name=""var:v472"" select=""s1:SBR_OtherSubscriberInformation_2/SBR05_InsuranceTypeCode/text()"" />
                      <ns0:TRI_INS_TYPE_CODE>
                        <xsl:value-of select=""$var:v472"" />
                      </ns0:TRI_INS_TYPE_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v473"" select=""position()"" />
                  <xsl:variable name=""var:v474"" select=""userCSharp:LogicalEq(string($var:v473) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v474"">
                    <xsl:variable name=""var:v475"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI03_BenefitsAssignmentCertificationIndicator)"" />
                    <xsl:variable name=""var:v476"" select=""userCSharp:LogicalExistence($var:v475)"" />
                    <xsl:if test=""string($var:v476)='true'"">
                      <xsl:variable name=""var:v477"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI03_BenefitsAssignmentCertificationIndicator/text()"" />
                      <ns0:TRI_ASSIGN_BENRFIT_IND>
                        <xsl:value-of select=""$var:v477"" />
                      </ns0:TRI_ASSIGN_BENRFIT_IND>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v478"" select=""position()"" />
                  <xsl:variable name=""var:v479"" select=""userCSharp:LogicalEq(string($var:v478) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v479"">
                    <xsl:variable name=""var:v480"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI04_PatientSignatureSourceCode)"" />
                    <xsl:variable name=""var:v481"" select=""userCSharp:LogicalExistence($var:v480)"" />
                    <xsl:if test=""string($var:v481)='true'"">
                      <xsl:variable name=""var:v482"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI04_PatientSignatureSourceCode/text()"" />
                      <ns0:TRI_PAT_SIGN_SRC_CODE>
                        <xsl:value-of select=""$var:v482"" />
                      </ns0:TRI_PAT_SIGN_SRC_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v483"" select=""position()"" />
                  <xsl:variable name=""var:v484"" select=""userCSharp:LogicalEq(string($var:v483) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v484"">
                    <xsl:variable name=""var:v485"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation_2/OI06_ReleaseofInformationCode)"" />
                    <xsl:variable name=""var:v486"" select=""userCSharp:LogicalExistence($var:v485)"" />
                    <xsl:if test=""string($var:v486)='true'"">
                      <xsl:variable name=""var:v487"" select=""s1:OI_OtherInsuranceCoverageInformation_2/OI06_ReleaseofInformationCode/text()"" />
                      <ns0:TRI_RELEASE_INFO_CODE>
                        <xsl:value-of select=""$var:v487"" />
                      </ns0:TRI_RELEASE_INFO_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v488"" select=""position()"" />
                  <xsl:variable name=""var:v489"" select=""userCSharp:LogicalEq(string($var:v488) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v489"">
                    <xsl:variable name=""var:v490"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM103_OtherInsuredLastName)"" />
                    <xsl:variable name=""var:v491"" select=""userCSharp:LogicalExistence($var:v490)"" />
                    <xsl:if test=""string($var:v491)='true'"">
                      <xsl:variable name=""var:v492"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM103_OtherInsuredLastName/text()"" />
                      <ns0:TRI_INSURED_LNAME>
                        <xsl:value-of select=""$var:v492"" />
                      </ns0:TRI_INSURED_LNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v493"" select=""position()"" />
                  <xsl:variable name=""var:v494"" select=""userCSharp:LogicalEq(string($var:v493) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v494"">
                    <xsl:variable name=""var:v495"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM104_OtherInsuredFirstName)"" />
                    <xsl:variable name=""var:v496"" select=""userCSharp:LogicalExistence($var:v495)"" />
                    <xsl:if test=""string($var:v496)='true'"">
                      <xsl:variable name=""var:v497"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM104_OtherInsuredFirstName/text()"" />
                      <ns0:TRI_INSURED_FNAME>
                        <xsl:value-of select=""$var:v497"" />
                      </ns0:TRI_INSURED_FNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v498"" select=""position()"" />
                  <xsl:variable name=""var:v499"" select=""userCSharp:LogicalEq(string($var:v498) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v499"">
                    <xsl:variable name=""var:v500"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM105_OtherInsuredMiddleName)"" />
                    <xsl:variable name=""var:v501"" select=""userCSharp:LogicalExistence($var:v500)"" />
                    <xsl:if test=""string($var:v501)='true'"">
                      <xsl:variable name=""var:v502"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM105_OtherInsuredMiddleName/text()"" />
                      <ns0:TRI_INSURED_MNAME>
                        <xsl:value-of select=""$var:v502"" />
                      </ns0:TRI_INSURED_MNAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v503"" select=""position()"" />
                  <xsl:variable name=""var:v504"" select=""userCSharp:LogicalEq(string($var:v503) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v504"">
                    <xsl:variable name=""var:v505"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM107_OtherInsuredNameSuffix)"" />
                    <xsl:variable name=""var:v506"" select=""userCSharp:LogicalExistence($var:v505)"" />
                    <xsl:if test=""string($var:v506)='true'"">
                      <xsl:variable name=""var:v507"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM107_OtherInsuredNameSuffix/text()"" />
                      <ns0:TRI_INSURED_SUFFIX>
                        <xsl:value-of select=""$var:v507"" />
                      </ns0:TRI_INSURED_SUFFIX>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v508"" select=""position()"" />
                  <xsl:variable name=""var:v509"" select=""userCSharp:LogicalEq(string($var:v508) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v509"">
                    <xsl:variable name=""var:v510"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM108_IdentificationCodeQualifier)"" />
                    <xsl:variable name=""var:v511"" select=""userCSharp:LogicalExistence($var:v510)"" />
                    <xsl:if test=""string($var:v511)='true'"">
                      <xsl:variable name=""var:v512"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM108_IdentificationCodeQualifier/text()"" />
                      <ns0:TRI_INSURED_ID_QUAL>
                        <xsl:value-of select=""$var:v512"" />
                      </ns0:TRI_INSURED_ID_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v513"" select=""position()"" />
                  <xsl:variable name=""var:v514"" select=""userCSharp:LogicalEq(string($var:v513) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v514"">
                    <xsl:variable name=""var:v515"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM109_OtherInsuredIdentifier)"" />
                    <xsl:variable name=""var:v516"" select=""userCSharp:LogicalExistence($var:v515)"" />
                    <xsl:if test=""string($var:v516)='true'"">
                      <xsl:variable name=""var:v517"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:NM1_OtherSubscriberName_2/NM109_OtherInsuredIdentifier/text()"" />
                      <ns0:TRI_INSURED_ID>
                        <xsl:value-of select=""$var:v517"" />
                      </ns0:TRI_INSURED_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v518"" select=""position()"" />
                  <xsl:variable name=""var:v519"" select=""userCSharp:LogicalEq(string($var:v518) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v519"">
                    <xsl:variable name=""var:v520"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM103_OtherPayerOrganizationName)"" />
                    <xsl:variable name=""var:v521"" select=""userCSharp:LogicalExistence($var:v520)"" />
                    <xsl:if test=""string($var:v521)='true'"">
                      <xsl:variable name=""var:v522"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM103_OtherPayerOrganizationName/text()"" />
                      <ns0:TRI_PAYER_NAME>
                        <xsl:value-of select=""$var:v522"" />
                      </ns0:TRI_PAYER_NAME>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v523"" select=""position()"" />
                  <xsl:variable name=""var:v524"" select=""userCSharp:LogicalEq(string($var:v523) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v524"">
                    <xsl:variable name=""var:v525"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM109_OtherPayerPrimaryIdentifier)"" />
                    <xsl:variable name=""var:v526"" select=""userCSharp:LogicalExistence($var:v525)"" />
                    <xsl:if test=""string($var:v526)='true'"">
                      <xsl:variable name=""var:v527"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:NM1_OtherPayerName_2/NM109_OtherPayerPrimaryIdentifier/text()"" />
                      <ns0:TRI_PAYER_ID>
                        <xsl:value-of select=""$var:v527"" />
                      </ns0:TRI_PAYER_ID>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:TRI_INSURED_GENDER>
          <xsl:text />
        </ns0:TRI_INSURED_GENDER>
        <ns0:TRI_INSURED_DOB>
          <xsl:text />
        </ns0:TRI_INSURED_DOB>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v528"" select=""position()"" />
                  <xsl:variable name=""var:v529"" select=""userCSharp:LogicalEq(string($var:v528) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v529"">
                    <xsl:variable name=""var:v530"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N301_OtherInsuredAddressLine)"" />
                    <xsl:variable name=""var:v531"" select=""userCSharp:LogicalExistence($var:v530)"" />
                    <xsl:if test=""string($var:v531)='true'"">
                      <xsl:variable name=""var:v532"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N301_OtherInsuredAddressLine/text()"" />
                      <ns0:TRI_INSURED_ADD1>
                        <xsl:value-of select=""$var:v532"" />
                      </ns0:TRI_INSURED_ADD1>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v533"" select=""position()"" />
                  <xsl:variable name=""var:v534"" select=""userCSharp:LogicalEq(string($var:v533) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v534"">
                    <xsl:variable name=""var:v535"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N302_OtherInsuredAddressLine)"" />
                    <xsl:variable name=""var:v536"" select=""userCSharp:LogicalExistence($var:v535)"" />
                    <xsl:if test=""string($var:v536)='true'"">
                      <xsl:variable name=""var:v537"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N3_OtherSubscriberAddress_2/N302_OtherInsuredAddressLine/text()"" />
                      <ns0:TRI_INSURED_ADD2>
                        <xsl:value-of select=""$var:v537"" />
                      </ns0:TRI_INSURED_ADD2>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v538"" select=""position()"" />
                  <xsl:variable name=""var:v539"" select=""userCSharp:LogicalEq(string($var:v538) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v539"">
                    <xsl:variable name=""var:v540"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N401_OtherSubscriberCityName)"" />
                    <xsl:variable name=""var:v541"" select=""userCSharp:LogicalExistence($var:v540)"" />
                    <xsl:if test=""string($var:v541)='true'"">
                      <xsl:variable name=""var:v542"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N401_OtherSubscriberCityName/text()"" />
                      <ns0:TRI_INSURED_CITY>
                        <xsl:value-of select=""$var:v542"" />
                      </ns0:TRI_INSURED_CITY>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v543"" select=""position()"" />
                  <xsl:variable name=""var:v544"" select=""userCSharp:LogicalEq(string($var:v543) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v544"">
                    <xsl:variable name=""var:v545"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N402_OtherSubscriberStateorProvinceCode)"" />
                    <xsl:variable name=""var:v546"" select=""userCSharp:LogicalExistence($var:v545)"" />
                    <xsl:if test=""string($var:v546)='true'"">
                      <xsl:variable name=""var:v547"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N402_OtherSubscriberStateorProvinceCode/text()"" />
                      <ns0:TRI_INSURED_STATE>
                        <xsl:value-of select=""$var:v547"" />
                      </ns0:TRI_INSURED_STATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v548"" select=""position()"" />
                  <xsl:variable name=""var:v549"" select=""userCSharp:LogicalEq(string($var:v548) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v549"">
                    <xsl:variable name=""var:v550"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N403_OtherSubscriberPostalZoneorZIPCode)"" />
                    <xsl:variable name=""var:v551"" select=""userCSharp:LogicalExistence($var:v550)"" />
                    <xsl:if test=""string($var:v551)='true'"">
                      <xsl:variable name=""var:v552"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:N4_OtherSubscriberCity_State_ZIPCode_2/N403_OtherSubscriberPostalZoneorZIPCode/text()"" />
                      <ns0:TRI_INSURED_ZIP>
                        <xsl:value-of select=""$var:v552"" />
                      </ns0:TRI_INSURED_ZIP>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v553"" select=""position()"" />
                  <xsl:variable name=""var:v554"" select=""userCSharp:LogicalEq(string($var:v553) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v554"">
                    <xsl:variable name=""var:v555"" select=""boolean(s1:CAS_ClaimLevelAdjustments_2/CAS01_ClaimAdjustmentGroupCode)"" />
                    <xsl:variable name=""var:v556"" select=""userCSharp:LogicalExistence($var:v555)"" />
                    <xsl:if test=""string($var:v556)='true'"">
                      <xsl:variable name=""var:v557"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS01_ClaimAdjustmentGroupCode/text()"" />
                      <ns0:TRI_CAS01_CODE>
                        <xsl:value-of select=""$var:v557"" />
                      </ns0:TRI_CAS01_CODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v558"" select=""position()"" />
                  <xsl:variable name=""var:v559"" select=""userCSharp:LogicalEq(string($var:v558) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v559"">
                    <xsl:variable name=""var:v560"" select=""boolean(s1:CAS_ClaimLevelAdjustments_2/CAS02_AdjustmentReasonCode)"" />
                    <xsl:variable name=""var:v561"" select=""userCSharp:LogicalExistence($var:v560)"" />
                    <xsl:if test=""string($var:v561)='true'"">
                      <xsl:variable name=""var:v562"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS02_AdjustmentReasonCode/text()"" />
                      <ns0:TRI_CAS02_REASON>
                        <xsl:value-of select=""$var:v562"" />
                      </ns0:TRI_CAS02_REASON>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v563"" select=""position()"" />
                  <xsl:variable name=""var:v564"" select=""userCSharp:LogicalEq(string($var:v563) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v564"">
                    <xsl:variable name=""var:v565"" select=""boolean(s1:CAS_ClaimLevelAdjustments_2/CAS03_AdjustmentAmount)"" />
                    <xsl:variable name=""var:v566"" select=""userCSharp:LogicalExistence($var:v565)"" />
                    <xsl:if test=""string($var:v566)='true'"">
                      <xsl:variable name=""var:v567"" select=""s1:CAS_ClaimLevelAdjustments_2/CAS03_AdjustmentAmount/text()"" />
                      <ns0:TRI_CAS03_AMT>
                        <xsl:value-of select=""$var:v567"" />
                      </ns0:TRI_CAS03_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v568"" select=""position()"" />
                  <xsl:variable name=""var:v569"" select=""userCSharp:LogicalEq(string($var:v568) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v569"">
                    <xsl:variable name=""var:v570"" select=""boolean(s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount)"" />
                    <xsl:variable name=""var:v571"" select=""userCSharp:LogicalExistence($var:v570)"" />
                    <xsl:if test=""string($var:v571)='true'"">
                      <xsl:variable name=""var:v572"" select=""s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()"" />
                      <ns0:TRI_PAYERPAID_AMT>
                        <xsl:value-of select=""$var:v572"" />
                      </ns0:TRI_PAYERPAID_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v573"" select=""position()"" />
                  <xsl:variable name=""var:v574"" select=""userCSharp:LogicalEq(string($var:v573) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v574"">
                    <xsl:variable name=""var:v575"" select=""boolean(s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount)"" />
                    <xsl:variable name=""var:v576"" select=""userCSharp:LogicalExistence($var:v575)"" />
                    <xsl:if test=""string($var:v576)='true'"">
                      <xsl:variable name=""var:v577"" select=""s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount/text()"" />
                      <ns0:TRI_NONCOVERED_AMT>
                        <xsl:value-of select=""$var:v577"" />
                      </ns0:TRI_NONCOVERED_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v578"" select=""position()"" />
                  <xsl:variable name=""var:v579"" select=""userCSharp:LogicalEq(string($var:v578) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v579"">
                    <xsl:variable name=""var:v580"" select=""boolean(s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3/AMT02_RemainingPatientLiability)"" />
                    <xsl:variable name=""var:v581"" select=""userCSharp:LogicalExistence($var:v580)"" />
                    <xsl:if test=""string($var:v581)='true'"">
                      <xsl:variable name=""var:v582"" select=""s1:AMT_SubLoop_3/s1:AMT_RemainingPatientLiability_3/AMT02_RemainingPatientLiability/text()"" />
                      <ns0:TRI_LIABILITY_AMT>
                        <xsl:value-of select=""$var:v582"" />
                      </ns0:TRI_LIABILITY_AMT>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v583"" select=""position()"" />
                  <xsl:variable name=""var:v584"" select=""userCSharp:LogicalEq(string($var:v583) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v584"">
                    <xsl:variable name=""var:v585"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:REF_OtherSubscriberSecondaryIdentification_2/REF02_OtherInsuredAdditionalIdentifier)"" />
                    <xsl:variable name=""var:v586"" select=""userCSharp:LogicalExistence($var:v585)"" />
                    <xsl:if test=""string($var:v586)='true'"">
                      <xsl:variable name=""var:v587"" select=""s1:NM1_SubLoop_8/s1:TS837_2330A_Loop1/s1:REF_OtherSubscriberSecondaryIdentification_2/REF02_OtherInsuredAdditionalIdentifier/text()"" />
                      <ns0:TRI_INSURED_SSN_REF>
                        <xsl:value-of select=""$var:v587"" />
                      </ns0:TRI_INSURED_SSN_REF>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v588"" select=""position()"" />
                  <xsl:variable name=""var:v589"" select=""userCSharp:LogicalEq(string($var:v588) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v589"">
                    <xsl:variable name=""var:v590"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N301_OtherPayerAddressLine)"" />
                    <xsl:variable name=""var:v591"" select=""userCSharp:LogicalExistence($var:v590)"" />
                    <xsl:if test=""string($var:v591)='true'"">
                      <xsl:variable name=""var:v592"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N301_OtherPayerAddressLine/text()"" />
                      <ns0:TRI_PAYER_ADD1>
                        <xsl:value-of select=""$var:v592"" />
                      </ns0:TRI_PAYER_ADD1>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v593"" select=""position()"" />
                  <xsl:variable name=""var:v594"" select=""userCSharp:LogicalEq(string($var:v593) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v594"">
                    <xsl:variable name=""var:v595"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N302_OtherPayerAddressLine)"" />
                    <xsl:variable name=""var:v596"" select=""userCSharp:LogicalExistence($var:v595)"" />
                    <xsl:if test=""string($var:v596)='true'"">
                      <xsl:variable name=""var:v597"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N3_OtherPayerAddress_2/N302_OtherPayerAddressLine/text()"" />
                      <ns0:TRI_PAYER_ADD2>
                        <xsl:value-of select=""$var:v597"" />
                      </ns0:TRI_PAYER_ADD2>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v598"" select=""position()"" />
                  <xsl:variable name=""var:v599"" select=""userCSharp:LogicalEq(string($var:v598) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v599"">
                    <xsl:variable name=""var:v600"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N401_OtherPayerCityName)"" />
                    <xsl:variable name=""var:v601"" select=""userCSharp:LogicalExistence($var:v600)"" />
                    <xsl:if test=""string($var:v601)='true'"">
                      <xsl:variable name=""var:v602"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N401_OtherPayerCityName/text()"" />
                      <ns0:TRI_PAYER_CITY>
                        <xsl:value-of select=""$var:v602"" />
                      </ns0:TRI_PAYER_CITY>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v603"" select=""position()"" />
                  <xsl:variable name=""var:v604"" select=""userCSharp:LogicalEq(string($var:v603) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v604"">
                    <xsl:variable name=""var:v605"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N402_OtherPayerStateorProvinceCode)"" />
                    <xsl:variable name=""var:v606"" select=""userCSharp:LogicalExistence($var:v605)"" />
                    <xsl:if test=""string($var:v606)='true'"">
                      <xsl:variable name=""var:v607"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N402_OtherPayerStateorProvinceCode/text()"" />
                      <ns0:TRI_PAYER_STATE>
                        <xsl:value-of select=""$var:v607"" />
                      </ns0:TRI_PAYER_STATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v608"" select=""position()"" />
                  <xsl:variable name=""var:v609"" select=""userCSharp:LogicalEq(string($var:v608) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v609"">
                    <xsl:variable name=""var:v610"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N403_OtherPayerPostalZoneorZIPCode)"" />
                    <xsl:variable name=""var:v611"" select=""userCSharp:LogicalExistence($var:v610)"" />
                    <xsl:if test=""string($var:v611)='true'"">
                      <xsl:variable name=""var:v612"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:N4_OtherPayerCity_State_ZIPCode_2/N403_OtherPayerPostalZoneorZIPCode/text()"" />
                      <ns0:TRI_PAYER_ZIPCODE>
                        <xsl:value-of select=""$var:v612"" />
                      </ns0:TRI_PAYER_ZIPCODE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v613"" select=""position()"" />
                  <xsl:variable name=""var:v614"" select=""userCSharp:LogicalEq(string($var:v613) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v614"">
                    <xsl:variable name=""var:v615"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate)"" />
                    <xsl:variable name=""var:v616"" select=""userCSharp:LogicalExistence($var:v615)"" />
                    <xsl:if test=""string($var:v616)='true'"">
                      <xsl:variable name=""var:v617"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:DTP_ClaimCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate/text()"" />
                      <ns0:TRI_PAYER_REMITTANCE_DATE>
                        <xsl:value-of select=""$var:v617"" />
                      </ns0:TRI_PAYER_REMITTANCE_DATE>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v618"" select=""position()"" />
                  <xsl:variable name=""var:v619"" select=""userCSharp:LogicalEq(string($var:v618) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v619"">
                    <xsl:variable name=""var:v620"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v621"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[1]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v622"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v623"" select=""s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2[2]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v624"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerPriorAuthorizationNumber_2/REF01_ReferenceIdentificationQualifier/text())"" />
                    <xsl:variable name=""var:v625"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerPriorAuthorizationNumber_2/REF02_OtherPayerPriorAuthorizationNumber/text())"" />
                    <xsl:variable name=""var:v626"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerReferralNumber_2/REF01_ReferenceIdentificationQualifier/text())"" />
                    <xsl:variable name=""var:v627"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerReferralNumber_2/REF02_OtherPayerPriorAuthorizationorReferralNumber/text())"" />
                    <xsl:variable name=""var:v628"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimAdjustmentIndicator_2/REF01_ReferenceIdentificationQualifier/text())"" />
                    <xsl:variable name=""var:v629"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimAdjustmentIndicator_2/REF02_OtherPayerClaimAdjustmentIndicator/text())"" />
                    <xsl:variable name=""var:v630"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimControlNumber_2/REF01_ReferenceIdentificationQualifier/text())"" />
                    <xsl:variable name=""var:v631"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerClaimControlNumber_2/REF02_OtherPayer_sClaimControlNumber/text())"" />
                    <xsl:variable name=""var:v632"" select=""userCSharp:StringConcat(string($var:v620) , &quot;:&quot; , string($var:v621) , &quot;,&quot; , string($var:v622) , &quot;:&quot; , string($var:v623) , &quot;,&quot; , $var:v624 , &quot;:&quot; , $var:v625 , &quot;,&quot; , $var:v626 , &quot;:&quot; , $var:v627 , &quot;,&quot; , $var:v628 , &quot;:&quot; , $var:v629 , &quot;,&quot; , $var:v630 , &quot;:&quot; , $var:v631)"" />
                    <ns0:TRI_PAYER_REF>
                      <xsl:value-of select=""$var:v632"" />
                    </ns0:TRI_PAYER_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v633"" select=""position()"" />
                  <xsl:variable name=""var:v634"" select=""userCSharp:LogicalEq(string($var:v633) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v634"">
                    <xsl:variable name=""var:v635"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:NM1_OtherPayerReferringProvider_2/NM102_EntityTypeQualifier)"" />
                    <xsl:variable name=""var:v636"" select=""userCSharp:LogicalExistence($var:v635)"" />
                    <xsl:if test=""string($var:v636)='true'"">
                      <xsl:variable name=""var:v637"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:NM1_OtherPayerReferringProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:TRI_INSURED_REFERING_QUAL>
                        <xsl:value-of select=""$var:v637"" />
                      </ns0:TRI_INSURED_REFERING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v638"" select=""position()"" />
                  <xsl:variable name=""var:v639"" select=""userCSharp:LogicalEq(string($var:v638) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v639"">
                    <xsl:variable name=""var:v640"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v641"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[1]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v642"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v643"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[2]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v644"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v645"" select=""s1:NM1_SubLoop_8/s1:TS837_2330C_Loop1_Loop/s1:TS837_2330C_Loop1/s1:REF_OtherPayerReferringProviderSecondaryIdentification_2[3]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v646"" select=""userCSharp:StringConcat(string($var:v640) , &quot;:&quot; , string($var:v641) , &quot;,&quot; , string($var:v642) , &quot;:&quot; , string($var:v643) , &quot;,&quot; , string($var:v644) , &quot;:&quot; , string($var:v645) , &quot;,&quot;)"" />
                    <ns0:TRI_INSURED_REFERING_REF>
                      <xsl:value-of select=""$var:v646"" />
                    </ns0:TRI_INSURED_REFERING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v647"" select=""position()"" />
                  <xsl:variable name=""var:v648"" select=""userCSharp:LogicalEq(string($var:v647) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v648"">
                    <xsl:variable name=""var:v649"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:NM1_OtherPayerRenderingProvider_2/NM102_EntityTypeQualifier)"" />
                    <xsl:variable name=""var:v650"" select=""userCSharp:LogicalExistence($var:v649)"" />
                    <xsl:if test=""string($var:v650)='true'"">
                      <xsl:variable name=""var:v651"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:NM1_OtherPayerRenderingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:TRI_INSURED_RENDERING_QUAL>
                        <xsl:value-of select=""$var:v651"" />
                      </ns0:TRI_INSURED_RENDERING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v652"" select=""position()"" />
                  <xsl:variable name=""var:v653"" select=""userCSharp:LogicalEq(string($var:v652) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v653"">
                    <xsl:variable name=""var:v654"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v655"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[1]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v656"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v657"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[2]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v658"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v659"" select=""s1:NM1_SubLoop_8/s1:TS837_2330D_Loop1/s1:REF_OtherPayerRenderingProviderSecondaryIdentification_2[3]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                    <xsl:variable name=""var:v660"" select=""userCSharp:StringConcat(string($var:v654) , &quot;:&quot; , string($var:v655) , &quot;,&quot; , string($var:v656) , &quot;:&quot; , string($var:v657) , &quot;,&quot; , string($var:v658) , &quot;:&quot; , string($var:v659) , &quot;,&quot;)"" />
                    <ns0:TRI_INSURED_RENDERING_REF>
                      <xsl:value-of select=""$var:v660"" />
                    </ns0:TRI_INSURED_RENDERING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v661"" select=""position()"" />
                  <xsl:variable name=""var:v662"" select=""userCSharp:LogicalEq(string($var:v661) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v662"">
                    <xsl:variable name=""var:v663"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:NM1_OtherPayerServiceFacilityLocation_2/NM102_EntityTypeQualifier)"" />
                    <xsl:variable name=""var:v664"" select=""userCSharp:LogicalExistence($var:v663)"" />
                    <xsl:if test=""string($var:v664)='true'"">
                      <xsl:variable name=""var:v665"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:NM1_OtherPayerServiceFacilityLocation_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:TRI_INSURED_SERVICEFACILITY_QUAL>
                        <xsl:value-of select=""$var:v665"" />
                      </ns0:TRI_INSURED_SERVICEFACILITY_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v666"" select=""position()"" />
                  <xsl:variable name=""var:v667"" select=""userCSharp:LogicalEq(string($var:v666) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v667"">
                    <xsl:variable name=""var:v668"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v669"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[1]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v670"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v671"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[2]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v672"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v673"" select=""s1:NM1_SubLoop_8/s1:TS837_2330E_Loop1/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification_2[3]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                    <xsl:variable name=""var:v674"" select=""userCSharp:StringConcat(string($var:v668) , &quot;:&quot; , string($var:v669) , &quot;,&quot; , string($var:v670) , &quot;:&quot; , string($var:v671) , &quot;,&quot; , string($var:v672) , &quot;:&quot; , string($var:v673) , &quot;,&quot;)"" />
                    <ns0:TRI_INSURED_SERVICEFACILITY_REF>
                      <xsl:value-of select=""$var:v674"" />
                    </ns0:TRI_INSURED_SERVICEFACILITY_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v675"" select=""position()"" />
                  <xsl:variable name=""var:v676"" select=""userCSharp:LogicalEq(string($var:v675) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v676"">
                    <xsl:variable name=""var:v677"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:NM1_OtherPayerSupervisingProvider_2/NM102_EntityTypeQualifier)"" />
                    <xsl:variable name=""var:v678"" select=""userCSharp:LogicalExistence($var:v677)"" />
                    <xsl:if test=""string($var:v678)='true'"">
                      <xsl:variable name=""var:v679"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:NM1_OtherPayerSupervisingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:TRI_INSURED_SUPERVISING_QUAL>
                        <xsl:value-of select=""$var:v679"" />
                      </ns0:TRI_INSURED_SUPERVISING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v680"" select=""position()"" />
                  <xsl:variable name=""var:v681"" select=""userCSharp:LogicalEq(string($var:v680) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v681"">
                    <xsl:variable name=""var:v682"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v683"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[1]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v684"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v685"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[2]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v686"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v687"" select=""s1:NM1_SubLoop_8/s1:TS837_2330F_Loop1/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification_2[3]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v688"" select=""userCSharp:StringConcat(string($var:v682) , &quot;:&quot; , string($var:v683) , &quot;,&quot; , string($var:v684) , &quot;:&quot; , string($var:v685) , &quot;,&quot; , string($var:v686) , &quot;:&quot; , string($var:v687) , &quot;,&quot;)"" />
                    <ns0:TRI_INSURED_SUPERVISING_REF>
                      <xsl:value-of select=""$var:v688"" />
                    </ns0:TRI_INSURED_SUPERVISING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v689"" select=""position()"" />
                  <xsl:variable name=""var:v690"" select=""userCSharp:LogicalEq(string($var:v689) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v690"">
                    <xsl:variable name=""var:v691"" select=""boolean(s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:NM1_OtherPayerBillingProvider_2/NM102_EntityTypeQualifier)"" />
                    <xsl:variable name=""var:v692"" select=""userCSharp:LogicalExistence($var:v691)"" />
                    <xsl:if test=""string($var:v692)='true'"">
                      <xsl:variable name=""var:v693"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:NM1_OtherPayerBillingProvider_2/NM102_EntityTypeQualifier/text()"" />
                      <ns0:TRI_INSURED_BILLING_QUAL>
                        <xsl:value-of select=""$var:v693"" />
                      </ns0:TRI_INSURED_BILLING_QUAL>
                    </xsl:if>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v694"" select=""position()"" />
                  <xsl:variable name=""var:v695"" select=""userCSharp:LogicalEq(string($var:v694) , &quot;2&quot;)"" />
                  <xsl:if test=""$var:v695"">
                    <xsl:variable name=""var:v696"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v697"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[1]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v698"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                    <xsl:variable name=""var:v699"" select=""s1:NM1_SubLoop_8/s1:TS837_2330G_Loop1/s1:REF_OtherPayerBillingProviderSecondaryIdentification_2[2]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                    <xsl:variable name=""var:v700"" select=""userCSharp:StringConcat(string($var:v696) , &quot;:&quot; , string($var:v697) , &quot;,&quot; , string($var:v698) , &quot;:&quot; , string($var:v699) , &quot;,&quot;)"" />
                    <ns0:TRI_INSURED_BILLING_REF>
                      <xsl:value-of select=""$var:v700"" />
                    </ns0:TRI_INSURED_BILLING_REF>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:EDI_SUBMITTER_ID>
          <xsl:value-of select=""$var:v16"" />
        </ns0:EDI_SUBMITTER_ID>
        <ns0:BILLING_NOTE_QUAL>
          <xsl:text />
        </ns0:BILLING_NOTE_QUAL>
        <ns0:BILLING_NOTE>
          <xsl:text />
        </ns0:BILLING_NOTE>
        <ns0:CLAIM_NOTE_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NTE_ClaimNote_2/NTE01_NoteReferenceCode/text()"" />
        </ns0:CLAIM_NOTE_QUAL>
        <ns0:CLAIM_NOTE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NTE_ClaimNote_2/NTE02_ClaimNoteText/text()"" />
        </ns0:CLAIM_NOTE>
        <ns0:PAYER_ESTAMT_QUAL>
          <xsl:text />
        </ns0:PAYER_ESTAMT_QUAL>
        <ns0:PAYER_ESTAMT>
          <xsl:text />
        </ns0:PAYER_ESTAMT>
        <ns0:CLAIM_QTY_QUAL>
          <xsl:text />
        </ns0:CLAIM_QTY_QUAL>
        <ns0:CLAIM_QTY_DAYSCNT>
          <xsl:text />
        </ns0:CLAIM_QTY_DAYSCNT>
        <ns0:CLAIM_QTY_UOM>
          <xsl:text />
        </ns0:CLAIM_QTY_UOM>
        <xsl:if test=""string($var:v112)='true'"">
          <xsl:variable name=""var:v701"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_OnsetofCurrentIllnessorSymptom_2/DTP03_OnsetofCurrentIllnessorInjuryDate/text()"" />
          <ns0:CURRENT_ILLNESS_DATE>
            <xsl:value-of select=""$var:v701"" />
          </ns0:CURRENT_ILLNESS_DATE>
        </xsl:if>
        <xsl:if test=""string($var:v101)='true'"">
          <xsl:variable name=""var:v702"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2/DTP01_DateTimeQualifier/text()"" />
          <ns0:ACCIDENT_DATE_QUAL>
            <xsl:value-of select=""$var:v702"" />
          </ns0:ACCIDENT_DATE_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v101)='true'"">
          <xsl:variable name=""var:v703"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_Accident_2/DTP03_AccidentDate/text()"" />
          <ns0:ACCIDENT_DATE>
            <xsl:value-of select=""$var:v703"" />
          </ns0:ACCIDENT_DATE>
        </xsl:if>
        <ns0:ANESTHESIA_PROC_HI>
          <xsl:value-of select=""$var:v704"" />
        </ns0:ANESTHESIA_PROC_HI>
        <xsl:variable name=""var:v717"" select=""userCSharp:ConditionCodes($var:v705 , $var:v706 , $var:v707 , $var:v708 , $var:v709 , $var:v710 , $var:v711 , $var:v712 , $var:v713 , $var:v714 , $var:v715 , $var:v716)"" />
        <ns0:ANESTHESIA_CONDITION_HI>
          <xsl:value-of select=""$var:v717"" />
        </ns0:ANESTHESIA_CONDITION_HI>
        <ns0:ANESTHESIA_TREATMENTCODE_HI>
          <xsl:text />
        </ns0:ANESTHESIA_TREATMENTCODE_HI>
        <xsl:variable name=""var:v718"" select=""userCSharp:AutoAccident($var:v60 , $var:v61 , $var:v62 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CLM_ClaimInformation_2/s1:C024_RelatedCausesInformation_2/C02404_AutoAccidentStateorProvinceCode/text()))"" />
        <ns0:AUTO_ACCIDENT_STATE>
          <xsl:value-of select=""$var:v718"" />
        </ns0:AUTO_ACCIDENT_STATE>
        <ns0:HIPAA_VERSION_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/ST/ST03_ImplementationGuideVersionName/text()"" />
        </ns0:HIPAA_VERSION_NUMBER>
        <ns0:TRANSACTION_SET_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/ST/ST02_TransactionSetControlNumber/text()"" />
        </ns0:TRANSACTION_SET_NUMBER>
        <ns0:BATCH_CONTROL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:BHT_BeginningofHierarchicalTransaction/BHT03_OriginatorApplicationTransactionIdentifier/text()"" />
        </ns0:BATCH_CONTROL_NUMBER>
        <ns0:SUBMITTER_QUALIFIER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM102_EntityTypeQualifier/text()"" />
        </ns0:SUBMITTER_QUALIFIER>
        <ns0:SUBMITTER_LAST_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM103_SubmitterLastorOrganizationName/text()"" />
        </ns0:SUBMITTER_LAST_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM104_SubmitterFirstName"">
          <ns0:SUBMITTER_FIRST_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM104_SubmitterFirstName/text()"" />
          </ns0:SUBMITTER_FIRST_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM105_SubmitterMiddleNameorInitial"">
          <ns0:SUBMITTER_MIDDLE_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM105_SubmitterMiddleNameorInitial/text()"" />
          </ns0:SUBMITTER_MIDDLE_NAME>
        </xsl:if>
        <ns0:SUBMITTER_ID_NM109>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000A_Loop/s1:NM1_SubmitterName/NM109_SubmitterIdentifier/text()"" />
        </ns0:SUBMITTER_ID_NM109>
        <ns0:RECEIVER_QUALIFIER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM102_EntityTypeQualifier/text()"" />
        </ns0:RECEIVER_QUALIFIER>
        <ns0:RECEIVER_LAST_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM103_ReceiverName/text()"" />
        </ns0:RECEIVER_LAST_NAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM104_NameFirst"">
          <ns0:RECEIVER_FIRST_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM104_NameFirst/text()"" />
          </ns0:RECEIVER_FIRST_NAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM105_NameMiddle"">
          <ns0:RECEIVER_MIDDLE_NAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM105_NameMiddle/text()"" />
          </ns0:RECEIVER_MIDDLE_NAME>
        </xsl:if>
        <ns0:RECEIVER_ID_NM109>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM109_ReceiverPrimaryIdentifier/text()"" />
        </ns0:RECEIVER_ID_NM109>
        <ns0:SOURCE_FILE_NAME>
          <xsl:value-of select=""$var:v16"" />
        </ns0:SOURCE_FILE_NAME>
        <xsl:for-each select=""/*[local-name()='Root']/*[local-name()='InputMessagePart_0']/*[local-name()='X12_00501_837_P']/*[local-name()='TS837_2000A_Loop']/*[local-name()='TS837_2000B_Loop']/*[local-name()='TS837_2000C_Loop']/*[local-name()='TS837_2300_Loop1']/*[local-name()='TS837_2320_Loop1']"">
            <xsl:if test=""position() = '1'"">

              <xsl:element name=""CAS_ADJ_CODE_PAYER_A_LIST"">


                <xsl:for-each select=""./*[local-name()='CAS_ClaimLevelAdjustments_2']"">
                  <xsl:if test=""CAS01_ClaimAdjustmentGroupCode/text() !=''"">
                    <xsl:value-of select=""CAS01_ClaimAdjustmentGroupCode/text()"" />

                  </xsl:if>

                  <xsl:if test="" CAS02_AdjustmentReasonCode/text() !=''"">
                    <xsl:text>*</xsl:text>
                    <xsl:value-of select=""CAS02_AdjustmentReasonCode/text()"" />

                  </xsl:if>

                  <xsl:if test="" CAS03_AdjustmentAmount/text() !=''"">
                    <xsl:text>*</xsl:text>
                    <xsl:value-of select=""CAS03_AdjustmentAmount/text()"" />

                  </xsl:if>
                  <xsl:choose>
		       <xsl:when test="" CAS04_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS04_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
		<xsl:choose>
		       <xsl:when test="" CAS05_AdjustmentReasonCode/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS05_AdjustmentReasonCode/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
		<xsl:choose>
		       <xsl:when test="" CAS06_AdjustmentAmount/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS06_AdjustmentAmount/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  
		<xsl:choose>
		       <xsl:when test="" CAS07_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS07_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  
		<xsl:choose>
		       <xsl:when test="" CAS08_AdjustmentReasonCode/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS08_AdjustmentReasonCode/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                 <xsl:choose>
		       <xsl:when test="" CAS09_AdjustmentAmount/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS09_AdjustmentAmount/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS10_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS10_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
 		<xsl:choose>
		       <xsl:when test="" CAS11_AdjustmentReasonCode/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS11_AdjustmentReasonCode/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS12_AdjustmentAmount/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS12_AdjustmentAmount/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS13_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS13_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
		<xsl:choose>
		       <xsl:when test="" CAS14_AdjustmentReasonCode/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS14_AdjustmentReasonCode/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS15_AdjustmentAmount/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS15_AdjustmentAmount/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                 <xsl:choose>
		       <xsl:when test="" CAS16_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS16_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS17_AdjustmentReasonCode/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS17_AdjustmentReasonCode/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  <xsl:choose>
		       <xsl:when test="" CAS18_AdjustmentAmount/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS18_AdjustmentAmount/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
		<xsl:choose>
		       <xsl:when test="" CAS19_AdjustmentQuantity/text() !=''"">
				       <xsl:text>*</xsl:text>
				       <xsl:value-of select=""CAS19_AdjustmentQuantity/text()"" />
		      </xsl:when>
		      <xsl:otherwise>
			<xsl:text>*</xsl:text>
		      </xsl:otherwise>
                 </xsl:choose>
                  
                  <xsl:if test=""position()!=last()"">
                    <xsl:text>,</xsl:text>
                  </xsl:if>
                </xsl:for-each>

              </xsl:element>
            </xsl:if>
            <xsl:if test=""position() = '2'"">
              <xsl:element name=""CAS_ADJ_CODE_PAYER_B_LIST"">
                <xsl:for-each select=""./*[local-name()='CAS_ClaimLevelAdjustments_2']"">
                  <xsl:if test="" CAS01_ClaimAdjustmentGroupCode/text() !=''"">
		                      <xsl:value-of select=""CAS01_ClaimAdjustmentGroupCode/text()"" />
		  
		                    </xsl:if>
		  
		                    <xsl:if test="" CAS02_AdjustmentReasonCode/text() !=''"">
		                      <xsl:text>*</xsl:text>
		                      <xsl:value-of select=""CAS02_AdjustmentReasonCode/text()"" />
		  
		                    </xsl:if>
		  
		                    <xsl:if test="" CAS03_AdjustmentAmount/text() !=''"">
		                      <xsl:text>*</xsl:text>
		                      <xsl:value-of select=""CAS03_AdjustmentAmount/text()"" />
		  
		                    </xsl:if>
		                    <xsl:choose>
				    		       <xsl:when test="" CAS04_AdjustmentQuantity/text() !=''"">
				    				       <xsl:text>*</xsl:text>
				    				       <xsl:value-of select=""CAS04_AdjustmentQuantity/text()"" />
				    		      </xsl:when>
				    		      <xsl:otherwise>
				    			<xsl:text>*</xsl:text>
				    		      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS05_AdjustmentReasonCode/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS05_AdjustmentReasonCode/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS06_AdjustmentAmount/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS06_AdjustmentAmount/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS07_AdjustmentQuantity/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS07_AdjustmentQuantity/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
		  		<xsl:choose>
				       <xsl:when test="" CAS08_AdjustmentReasonCode/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS08_AdjustmentReasonCode/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS09_AdjustmentAmount/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS09_AdjustmentAmount/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS10_AdjustmentQuantity/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS10_AdjustmentQuantity/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS11_AdjustmentReasonCode/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS11_AdjustmentReasonCode/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS12_AdjustmentAmount/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS12_AdjustmentAmount/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
				       <xsl:when test="" CAS13_AdjustmentQuantity/text() !=''"">
						       <xsl:text>*</xsl:text>
						       <xsl:value-of select=""CAS13_AdjustmentQuantity/text()"" />
				      </xsl:when>
				      <xsl:otherwise>
					<xsl:text>*</xsl:text>
				      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS14_AdjustmentReasonCode/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS14_AdjustmentReasonCode/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS15_AdjustmentAmount/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS15_AdjustmentAmount/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS16_AdjustmentQuantity/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS16_AdjustmentQuantity/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS17_AdjustmentReasonCode/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS17_AdjustmentReasonCode/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS18_AdjustmentAmount/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS18_AdjustmentAmount/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                		 <xsl:choose>
					       <xsl:when test="" CAS19_AdjustmentQuantity/text() !=''"">
							       <xsl:text>*</xsl:text>
							       <xsl:value-of select=""CAS19_AdjustmentQuantity/text()"" />
					      </xsl:when>
					      <xsl:otherwise>
						<xsl:text>*</xsl:text>
					      </xsl:otherwise>
                		 </xsl:choose>
                  <xsl:if test=""position()!=last()"">
                    <xsl:text>,</xsl:text>
                  </xsl:if>
                </xsl:for-each>
              </xsl:element>
            </xsl:if>
          </xsl:for-each>
        <ns0:PAYER_ADDRESS>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N3_PayerAddress/N301_PayerAddressLine/text()"" />
        </ns0:PAYER_ADDRESS>
        <ns0:PAYER_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N4_PayerCity_State_ZIPCode/N401_PayerCityName/text()"" />
        </ns0:PAYER_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N4_PayerCity_State_ZIPCode/N402_PayerStateorProvinceCode"">
          <ns0:PAYER_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N4_PayerCity_State_ZIPCode/N402_PayerStateorProvinceCode/text()"" />
          </ns0:PAYER_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N4_PayerCity_State_ZIPCode/N403_PayerPostalZoneorZIPCode"">
          <ns0:PAYER_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:N4_PayerCity_State_ZIPCode/N403_PayerPostalZoneorZIPCode/text()"" />
          </ns0:PAYER_ZIP>
        </xsl:if>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v719"" select=""position()"" />
                  <xsl:variable name=""var:v720"" select=""userCSharp:LogicalEq(string($var:v719) , &quot;1&quot;)"" />
                  <xsl:variable name=""var:v721"" select=""userCSharp:InitCumulativeConcat(0)"" />
                  <xsl:variable name=""var:v722"" select=""userCSharp:OtherPayerSecIDList(string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2/REF01_ReferenceIdentificationQualifier/text()) , string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2/REF02_OtherPayerSecondaryIdentifier/text()))"" />
                  <xsl:variable name=""var:v723"" select=""userCSharp:AddToCumulativeConcat(0,string($var:v722),&quot;3&quot;)"" />
                  <xsl:variable name=""var:v724"" select=""userCSharp:GetCumulativeConcat(0)"" />
                  <xsl:if test=""string($var:v720)='true'"">
                    <xsl:variable name=""var:v725"" select=""string($var:v724)"" />
                    <xsl:variable name=""var:v726"" select=""userCSharp:RemoveLastChar(string($var:v725))"" />
                    <ns0:OTHER_PAYER_A_SECID>
                      <xsl:value-of select=""$var:v726"" />
                    </ns0:OTHER_PAYER_A_SECID>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:TS837_2320_Loop1"">
                  <xsl:variable name=""var:v727"" select=""position()"" />
                  <xsl:variable name=""var:v728"" select=""userCSharp:LogicalEq(string($var:v727) , &quot;2&quot;)"" />
                  <xsl:variable name=""var:v729"" select=""userCSharp:InitCumulativeConcat(0)"" />
                  <xsl:variable name=""var:v730"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2/REF01_ReferenceIdentificationQualifier/text())"" />
                  <xsl:variable name=""var:v731"" select=""string(s1:NM1_SubLoop_8/s1:TS837_2330B_Loop1/s1:REF_SubLoop_10/s1:REF_OtherPayerSecondaryIdentifier_2_Loop/s1:REF_OtherPayerSecondaryIdentifier_2/REF02_OtherPayerSecondaryIdentifier/text())"" />
                  <xsl:variable name=""var:v732"" select=""userCSharp:OtherPayerSecIDList($var:v730 , $var:v731)"" />
                  <xsl:variable name=""var:v733"" select=""userCSharp:AddToCumulativeConcat(0,string($var:v732),&quot;3&quot;)"" />
                  <xsl:variable name=""var:v734"" select=""userCSharp:GetCumulativeConcat(0)"" />
                  <xsl:if test=""string($var:v728)='true'"">
                    <xsl:variable name=""var:v735"" select=""string($var:v734)"" />
                    <xsl:variable name=""var:v736"" select=""userCSharp:RemoveLastChar(string($var:v735))"" />
                    <ns0:OTHER_PAYER_B_SECID>
                      <xsl:value-of select=""$var:v736"" />
                    </ns0:OTHER_PAYER_B_SECID>
                  </xsl:if>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:OTHER_PAYER_A_MIA_RESERVE_DAYS>
          <xsl:text />
        </ns0:OTHER_PAYER_A_MIA_RESERVE_DAYS>
        <ns0:OTHER_PAYER_B_MIA_RESERVE_DAYS>
          <xsl:text />
        </ns0:OTHER_PAYER_B_MIA_RESERVE_DAYS>
        <ns0:OTHER_PAYER_A_REMARK_CODE>
          <xsl:text />
        </ns0:OTHER_PAYER_A_REMARK_CODE>
        <ns0:OTHER_PAYER_B_REMARK_CODE>
          <xsl:text />
        </ns0:OTHER_PAYER_B_REMARK_CODE>
        <ns0:OTHER_PAYER_A_ADDRESS>
          <xsl:text />
        </ns0:OTHER_PAYER_A_ADDRESS>
        <ns0:OTHER_PAYER_B_ADDRESS>
          <xsl:text />
        </ns0:OTHER_PAYER_B_ADDRESS>
        <ns0:OTHER_PAYER_A_CITY>
          <xsl:text />
        </ns0:OTHER_PAYER_A_CITY>
        <ns0:OTHER_PAYER_B_CITY>
          <xsl:text />
        </ns0:OTHER_PAYER_B_CITY>
        <ns0:OTHER_PAYER_A_STATE>
          <xsl:text />
        </ns0:OTHER_PAYER_A_STATE>
        <ns0:OTHER_PAYER_B_STATE>
          <xsl:text />
        </ns0:OTHER_PAYER_B_STATE>
        <ns0:OTHER_PAYER_A_ZIP>
          <xsl:text />
        </ns0:OTHER_PAYER_A_ZIP>
        <ns0:OTHER_PAYER_B_ZIP>
          <xsl:text />
        </ns0:OTHER_PAYER_B_ZIP>
        <xsl:if test=""string($var:v739)='true'"">
          <xsl:variable name=""var:v740"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount/text()"" />
          <ns0:COB_NONCOVEREDAMOUNT>
            <xsl:value-of select=""$var:v740"" />
          </ns0:COB_NONCOVEREDAMOUNT>
        </xsl:if>
        <ns0:COB_ALLOWEDAMOUNT>
          <xsl:text />
        </ns0:COB_ALLOWEDAMOUNT>
        <ns0:COB_TOTALSUBMITTEDCHARGES>
          <xsl:text />
        </ns0:COB_TOTALSUBMITTEDCHARGES>
        <ns0:PAY_TO_PLAN_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM108_IdentificationCodeQualifier/text()"" />
        </ns0:PAY_TO_PLAN_QUAL>
        <ns0:OPERATING_PROVIDER_LNAME>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_LNAME>
        <ns0:OPERATING_PROVIDER_MNAME>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_MNAME>
        <ns0:OPERATING_PROVIDER_FNAME>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_FNAME>
        <ns0:OPERATING_PROVIDER_SUFFIX>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_SUFFIX>
        <ns0:OPERATING_PROVIDER_QUAL>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_QUAL>
        <ns0:OPERATING_PROVIDER_ID>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_ID>
        <ns0:OPERATING_PROVIDER_NPI>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_NPI>
        <ns0:OPERATING_PROVIDER_REF>
          <xsl:text />
        </ns0:OPERATING_PROVIDER_REF>
        <ns0:OTH_OPERATING_PROVIDER_LNAME>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_LNAME>
        <ns0:OTH_OPERATING_PROVIDER_MNAME>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_MNAME>
        <ns0:OTH_OPERATING_PROVIDER_FNAME>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_FNAME>
        <ns0:OTH_OPERATING_PROVIDER_SUFFIX>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_SUFFIX>
        <ns0:OTH_OPERATING_PROVIDER_QUAL>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_QUAL>
        <ns0:OTH_OPERATING_PROVIDER_ID>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_ID>
        <ns0:OTH_OPERATING_PROVIDER_NPI>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_NPI>
        <ns0:OTH_OPERATING_PROVIDER_REF>
          <xsl:text />
        </ns0:OTH_OPERATING_PROVIDER_REF>
        <ns0:ATTENDING_PROVIDER_LNAME>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_LNAME>
        <ns0:ATTENDING_PROVIDER_MNAME>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_MNAME>
        <ns0:ATTENDING_PROVIDER_FNAME>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_FNAME>
        <ns0:ATTENDING_PROVIDER_SUFFIX>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_SUFFIX>
        <ns0:ATTENDING_PROVIDER_QUAL>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_QUAL>
        <ns0:ATTENDING_PROVIDER_ID>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_ID>
        <ns0:ATTENDING_PROVIDER_NPI>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_NPI>
        <ns0:ATTENDING_PROVIDER_REF>
          <xsl:text />
        </ns0:ATTENDING_PROVIDER_REF>
        <ns0:SEC_INSURED_ATTENDING_QUAL>
          <xsl:text />
        </ns0:SEC_INSURED_ATTENDING_QUAL>
        <ns0:SEC_INSURED_ATTENDING_REF>
          <xsl:text />
        </ns0:SEC_INSURED_ATTENDING_REF>
        <ns0:SEC_INSURED_OPERATING_QUAL>
          <xsl:text />
        </ns0:SEC_INSURED_OPERATING_QUAL>
        <ns0:SEC_INSURED_OPERATING_REF>
          <xsl:text />
        </ns0:SEC_INSURED_OPERATING_REF>
        <ns0:TRI_INSURED_ATTENDING_QUAL>
          <xsl:text />
        </ns0:TRI_INSURED_ATTENDING_QUAL>
        <ns0:TRI_INSURED_ATTENDING_REF>
          <xsl:text />
        </ns0:TRI_INSURED_ATTENDING_REF>
        <ns0:TRI_INSURED_OPERATING_QUAL>
          <xsl:text />
        </ns0:TRI_INSURED_OPERATING_QUAL>
        <ns0:TRI_INSURED_OPERATING_REF>
          <xsl:text />
        </ns0:TRI_INSURED_OPERATING_REF>
        <ns0:RECEIVER_ID>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:NM1_SubLoop/s1:TS837_1000B_Loop/s1:NM1_ReceiverName/NM109_ReceiverPrimaryIdentifier/text()"" />
        </ns0:RECEIVER_ID>
        <ns0:COB_APPROVEDAMOUNT>
          <xsl:text />
        </ns0:COB_APPROVEDAMOUNT>
        <ns0:COB_COVERAGEAMOUNT>
          <xsl:text />
        </ns0:COB_COVERAGEAMOUNT>
        <ns0:COB_DISCOUNTAMOUNT>
          <xsl:text />
        </ns0:COB_DISCOUNTAMOUNT>
        <ns0:COB_PATIENT_RSP_ACTUAL>
          <xsl:text />
        </ns0:COB_PATIENT_RSP_ACTUAL>
        <ns0:COB_PATIENTPAIDAMOUNT>
          <xsl:text />
        </ns0:COB_PATIENTPAIDAMOUNT>
        <ns0:COB_PERDAYLIMITAMOUNT>
          <xsl:text />
        </ns0:COB_PERDAYLIMITAMOUNT>
        <ns0:PERFORMING_PROVIDER_SPECIALTY>
          <xsl:text />
        </ns0:PERFORMING_PROVIDER_SPECIALTY>
        <ns0:PERFORMING_PROVIDER_TYPE>
          <xsl:text />
        </ns0:PERFORMING_PROVIDER_TYPE>
        <ns0:OPL_CALC_METHOD>
          <xsl:text />
        </ns0:OPL_CALC_METHOD>
        <ns0:OPL_VALUE_AMOUNT_LIST>
          <xsl:text />
        </ns0:OPL_VALUE_AMOUNT_LIST>
        <ns0:OPL_VALUE_CODE_LIST>
          <xsl:text />
        </ns0:OPL_VALUE_CODE_LIST>
        <ns0:RULE_NUMBER_PRIMARY>
          <xsl:text />
        </ns0:RULE_NUMBER_PRIMARY>
        <ns0:RULE_NUMBER_SECONDARY>
          <xsl:text />
        </ns0:RULE_NUMBER_SECONDARY>
        <ns0:SF_MESSAGE_CODE>
          <xsl:text />
        </ns0:SF_MESSAGE_CODE>
        <ns0:SPCC_AMOUNT>
          <xsl:text />
        </ns0:SPCC_AMOUNT>
        <ns0:SPCC_CODE>
          <xsl:text />
        </ns0:SPCC_CODE>
        <ns0:SPCC_DAYS>
          <xsl:text />
        </ns0:SPCC_DAYS>
        <ns0:SPCC_PERCENT>
          <xsl:text />
        </ns0:SPCC_PERCENT>
        <ns0:AVG_SEMI_PRIVATE_ROOM_RATE>
          <xsl:text />
        </ns0:AVG_SEMI_PRIVATE_ROOM_RATE>
        <ns0:HOST_OPL_PROV_ARRANGEMENT>
          <xsl:text />
        </ns0:HOST_OPL_PROV_ARRANGEMENT>
        <ns0:FACILITY_TYPE>
          <xsl:text />
        </ns0:FACILITY_TYPE>
        <ns0:PER_DIEM_RATE>
          <xsl:text />
        </ns0:PER_DIEM_RATE>
        <ns0:PERCENTAGE_FACTOR>
          <xsl:text />
        </ns0:PERCENTAGE_FACTOR>
        <ns0:PPO_AVAILABILITY>
          <xsl:text />
        </ns0:PPO_AVAILABILITY>
        <ns0:PPO_PROVIDER_TYPE_AVAILABILITY>
          <xsl:text />
        </ns0:PPO_PROVIDER_TYPE_AVAILABILITY>
        <ns0:PRIVATE_ROOM_RATE>
          <xsl:text />
        </ns0:PRIVATE_ROOM_RATE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N404_CountryCode"">
          <ns0:BILLING_PROVIDER_COUNTRY_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N4_BillingProviderCity_State_ZIPCode/N404_CountryCode/text()"" />
          </ns0:BILLING_PROVIDER_COUNTRY_CODE>
        </xsl:if>
        <ns0:PRICING_METHOD>
          <xsl:text />
        </ns0:PRICING_METHOD>
        <ns0:STREAMLINE_IND>
          <xsl:text />
        </ns0:STREAMLINE_IND>
        <ns0:DF_MESSAGE_CODE>
          <xsl:text />
        </ns0:DF_MESSAGE_CODE>
        <xsl:if test=""string($var:v744)='true'"">
          <xsl:variable name=""var:v745"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()"" />
          <ns0:COB_PAYERPAIDAMOUNT>
            <xsl:value-of select=""$var:v745"" />
          </ns0:COB_PAYERPAIDAMOUNT>
        </xsl:if>
        <ns0:COB_PATIENTRESPONSIBILITYACTUAL>
          <xsl:text />
        </ns0:COB_PATIENTRESPONSIBILITYACTUAL>
        <xsl:if test=""string($var:v749)='true'"">
          <xsl:variable name=""var:v750"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount_2/AMT02_PayerPaidAmount/text()"" />
          <ns0:SEC_COB_PAYERPAIDAMOUNT>
            <xsl:value-of select=""$var:v750"" />
          </ns0:SEC_COB_PAYERPAIDAMOUNT>
        </xsl:if>
        <ns0:SEC_COB_PATIENTRESPONSIBILITYACTUAL>
          <xsl:text />
        </ns0:SEC_COB_PATIENTRESPONSIBILITYACTUAL>
        <ns0:SEC_COB_DISCOUNTAMOUNT>
          <xsl:text />
        </ns0:SEC_COB_DISCOUNTAMOUNT>
        <xsl:if test=""string($var:v753)='true'"">
          <xsl:variable name=""var:v754"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:TS837_2320_Loop1/s1:AMT_SubLoop_3/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount_2/AMT02_Non_CoveredChargeAmount/text()"" />
          <ns0:SEC_COB_NONCOVEREDAMOUNT>
            <xsl:value-of select=""$var:v754"" />
          </ns0:SEC_COB_NONCOVEREDAMOUNT>
        </xsl:if>
        <ns0:REPRICED_CLAIM_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_RepricedClaimNumber_2/REF02_RepricedClaimReferenceNumber/text()"" />
        </ns0:REPRICED_CLAIM_NUMBER>
        <ns0:CONTRACT_TYPE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN101_ContractTypeCode/text()"" />
        </ns0:CONTRACT_TYPE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN102_ContractAmount"">
          <ns0:CONTRACT_AMOUNT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN102_ContractAmount/text()"" />
          </ns0:CONTRACT_AMOUNT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN103_ContractPercentage"">
          <ns0:CONTRACT_PERCENTAGE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN103_ContractPercentage/text()"" />
          </ns0:CONTRACT_PERCENTAGE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN104_ContractCode"">
          <ns0:CONTRACT_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN104_ContractCode/text()"" />
          </ns0:CONTRACT_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN105_TermsDiscountPercentage"">
          <ns0:TERMS_DISCNT_PERCNT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN105_TermsDiscountPercentage/text()"" />
          </ns0:TERMS_DISCNT_PERCNT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN106_ContractVersionIdentifier"">
          <ns0:CONTRACT_VER_IDENT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CN1_ContractInformation_3/CN106_ContractVersionIdentifier/text()"" />
          </ns0:CONTRACT_VER_IDENT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR109_RoundTripPurposeDescription"">
          <ns0:AMBULANCE_DESCRIPTION>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR109_RoundTripPurposeDescription/text()"" />
          </ns0:AMBULANCE_DESCRIPTION>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR110_StretcherPurposeDescription"">
          <ns0:AMBULANCE_STRETCHER_DESC>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR110_StretcherPurposeDescription/text()"" />
          </ns0:AMBULANCE_STRETCHER_DESC>
        </xsl:if>
        <ns0:CRC03_AMBULANCE_CODE1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC03_ConditionCode/text()"" />
        </ns0:CRC03_AMBULANCE_CODE1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC04_ConditionCode"">
          <ns0:CRC04_AMBULANCE_CODE2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC04_ConditionCode/text()"" />
          </ns0:CRC04_AMBULANCE_CODE2>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC05_ConditionCode"">
          <ns0:CRC05_AMBULANCE_CODE3>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC05_ConditionCode/text()"" />
          </ns0:CRC05_AMBULANCE_CODE3>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC06_ConditionCode"">
          <ns0:CRC06_AMBULANCE_CODE4>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC06_ConditionCode/text()"" />
          </ns0:CRC06_AMBULANCE_CODE4>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC07_ConditionCode"">
          <ns0:CRC07_AMBULANCE_CODE5>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC07_ConditionCode/text()"" />
          </ns0:CRC07_AMBULANCE_CODE5>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR102_PatientWeight"">
          <ns0:AMBULANCE_WEIGHT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR102_PatientWeight/text()"" />
          </ns0:AMBULANCE_WEIGHT>
        </xsl:if>
        <ns0:AMBULANCE_QTY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR106_TransportDistance/text()"" />
        </ns0:AMBULANCE_QTY>
        <ns0:AMBULANCE_REASON_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR1_AmbulanceTransportInformation_3/CR104_AmbulanceTransportReasonCode/text()"" />
        </ns0:AMBULANCE_REASON_CODE>
        <xsl:if test=""string($var:v755)='true'"">
          <xsl:variable name=""var:v756"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_3/REF02_ClinicalLaboratoryImprovementAmendmentNumber/text()"" />
          <ns0:CLIA_REF>
            <xsl:value-of select=""$var:v756"" />
          </ns0:CLIA_REF>
        </xsl:if>
        <xsl:if test=""string($var:v757)='true'"">
          <xsl:variable name=""var:v758"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_EPSDTReferral_2/CRC03_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND1>
            <xsl:value-of select=""$var:v758"" />
          </ns0:CRC_EPSDT_COND1>
        </xsl:if>
        <xsl:if test=""string($var:v760)='true'"">
          <xsl:variable name=""var:v761"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_EPSDTReferral_2/CRC04_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND2>
            <xsl:value-of select=""$var:v761"" />
          </ns0:CRC_EPSDT_COND2>
        </xsl:if>
        <xsl:if test=""string($var:v760)='true'"">
          <xsl:variable name=""var:v762"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_EPSDTReferral_2/CRC05_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND3>
            <xsl:value-of select=""$var:v762"" />
          </ns0:CRC_EPSDT_COND3>
        </xsl:if>
        <xsl:if test=""string($var:v763)='true'"">
          <xsl:variable name=""var:v764"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_MammographyCertificationNumber_3/REF02_MammographyCertificationNumber/text()"" />
          <ns0:MAMMOGRAPHY_NUM_REF>
            <xsl:value-of select=""$var:v764"" />
          </ns0:MAMMOGRAPHY_NUM_REF>
        </xsl:if>
        <xsl:if test=""string($var:v765)='true'"">
          <xsl:variable name=""var:v766"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:NM1_SubLoop_7/s1:TS837_2310F_Loop1/s1:NM1_AmbulanceDrop_offLocation_3/NM103_AmbulanceDrop_offLocation/text()"" />
          <ns0:AMBULANCE_DROPOFF_NAME>
            <xsl:value-of select=""$var:v766"" />
          </ns0:AMBULANCE_DROPOFF_NAME>
        </xsl:if>
        <ns0:CRC02_AMBULANCE_RESPONSECODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CRC_SubLoop_3/s1:CRC_AmbulanceCertification_3_Loop/s1:CRC_AmbulanceCertification_3/CRC02_CertificationConditionIndicator/text()"" />
        </ns0:CRC02_AMBULANCE_RESPONSECODE>
        <ns0:CR209_SPINAL_COND_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR2_SpinalManipulationServiceInformation_2/CR208_PatientConditionCode/text()"" />
        </ns0:CR209_SPINAL_COND_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR2_SpinalManipulationServiceInformation_2/CR210_PatientConditionDescription"">
          <ns0:CR210_PATIENT_COND_DESC1>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR2_SpinalManipulationServiceInformation_2/CR210_PatientConditionDescription/text()"" />
          </ns0:CR210_PATIENT_COND_DESC1>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR2_SpinalManipulationServiceInformation_2/CR211_PatientConditionDescription"">
          <ns0:CR211_PATIENT_COND_DESC2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:CR2_SpinalManipulationServiceInformation_2/CR211_PatientConditionDescription/text()"" />
          </ns0:CR211_PATIENT_COND_DESC2>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK06_AttachmentControlNumber"">
          <ns0:REPORT_PWK06_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:PWK_ClaimSupplementalInformation_2/PWK06_AttachmentControlNumber/text()"" />
          </ns0:REPORT_PWK06_ID>
        </xsl:if>
        <xsl:if test=""string($var:v767)='true'"">
          <xsl:variable name=""var:v768"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP01_DateTimeQualifier/text()"" />
          <ns0:XRAY_QUAL>
            <xsl:value-of select=""$var:v768"" />
          </ns0:XRAY_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v769)='true'"">
          <xsl:variable name=""var:v770"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:DTP_SubLoop_3/s1:DTP_Date_LastX_rayDate_3/DTP03_LastX_RayDate/text()"" />
          <ns0:XRAY_DATE>
            <xsl:value-of select=""$var:v770"" />
          </ns0:XRAY_DATE>
        </xsl:if>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v771"" select=""position()"" />
                      <xsl:variable name=""var:v772"" select=""userCSharp:LogicalEq(string($var:v771) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v772"">
                        <xsl:variable name=""var:v773"" select=""boolean(s1:NM1_ReferringProviderName_3)"" />
                        <xsl:variable name=""var:v774"" select=""userCSharp:LogicalExistence($var:v773)"" />
                        <xsl:if test=""string($var:v774)='true'"">
                          <xsl:variable name=""var:v775"" select=""s1:NM1_ReferringProviderName_3/NM102_EntityTypeQualifier/text()"" />
                          <ns0:PCP_PROVIDER_QUAL>
                            <xsl:value-of select=""$var:v775"" />
                          </ns0:PCP_PROVIDER_QUAL>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v776"" select=""position()"" />
                      <xsl:variable name=""var:v777"" select=""userCSharp:LogicalEq(string($var:v776) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v777"">
                        <ns0:PCP_PROVIDER_LNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM103_ReferringProviderLastName/text()"" />
                        </ns0:PCP_PROVIDER_LNAME>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v778"" select=""position()"" />
                      <xsl:variable name=""var:v779"" select=""userCSharp:LogicalEq(string($var:v778) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v779"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM105_ReferringProviderMiddleNameorInitial"">
                          <ns0:PCP_PROVIDER_MNAME>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                          </ns0:PCP_PROVIDER_MNAME>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v780"" select=""position()"" />
                      <xsl:variable name=""var:v781"" select=""userCSharp:LogicalEq(string($var:v780) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v781"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM104_ReferringProviderFirstName"">
                          <ns0:PCP_PROVIDER_FNAME>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM104_ReferringProviderFirstName/text()"" />
                          </ns0:PCP_PROVIDER_FNAME>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v782"" select=""position()"" />
                      <xsl:variable name=""var:v783"" select=""userCSharp:LogicalEq(string($var:v782) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v783"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM107_ReferringProviderNameSuffix"">
                          <ns0:PCP_PROVIDER_SUFFIX>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM107_ReferringProviderNameSuffix/text()"" />
                          </ns0:PCP_PROVIDER_SUFFIX>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v784"" select=""position()"" />
                      <xsl:variable name=""var:v785"" select=""userCSharp:LogicalEq(string($var:v784) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v785"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM108_IdentificationCodeQualifier"">
                          <ns0:PCP_PROVIDER_ID_QUAL>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM108_IdentificationCodeQualifier/text()"" />
                          </ns0:PCP_PROVIDER_ID_QUAL>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v786"" select=""position()"" />
                      <xsl:variable name=""var:v787"" select=""userCSharp:LogicalEq(string($var:v786) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v787"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier"">
                          <ns0:PCP_PROVIDER_ID>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier/text()"" />
                          </ns0:PCP_PROVIDER_ID>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v788"" select=""position()"" />
                      <xsl:variable name=""var:v789"" select=""userCSharp:LogicalEq(string($var:v788) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v789"">
                        <xsl:if test=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier"">
                          <ns0:PCP_PROVIDER_NPI_ID>
                            <xsl:value-of select=""s1:NM1_ReferringProviderName_3/NM109_ReferringProviderIdentifier/text()"" />
                          </ns0:PCP_PROVIDER_NPI_ID>
                        </xsl:if>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2000C_Loop"">
              <xsl:for-each select=""s1:TS837_2300_Loop1"">
                <xsl:for-each select=""s1:NM1_SubLoop_7"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop1_Loop"">
                    <xsl:for-each select=""s1:TS837_2310A_Loop1"">
                      <xsl:variable name=""var:v790"" select=""position()"" />
                      <xsl:variable name=""var:v791"" select=""userCSharp:LogicalEq(string($var:v790) , &quot;2&quot;)"" />
                      <xsl:if test=""$var:v791"">
                        <xsl:variable name=""var:v792"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v793"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
                        <xsl:variable name=""var:v794"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v795"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
                        <xsl:variable name=""var:v796"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v797"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v798"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                        <xsl:variable name=""var:v799"" select=""./s1:REF_ReferringProviderSecondaryIdentification_3[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                        <xsl:variable name=""var:v800"" select=""userCSharp:StringConcat(string($var:v792) , string($var:v793) , string($var:v794) , string($var:v795) , string($var:v796) , string($var:v793) , string($var:v797) , string($var:v795) , string($var:v798) , string($var:v793) , string($var:v799) , string($var:v795))"" />
                        <ns0:PCP_PROVIDER_REF>
                          <xsl:value-of select=""$var:v800"" />
                        </ns0:PCP_PROVIDER_REF>
                      </xsl:if>
                    </xsl:for-each>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:AUTH_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_PriorAuthorization_3/REF02_PriorAuthorizationNumber/text()"" />
        </ns0:AUTH_NUMBER>
        <ns0:REFERRAL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2300_Loop1/s1:REF_SubLoop_9/s1:REF_ReferralNumber_3/REF02_ReferralNumber/text()"" />
        </ns0:REFERRAL_NUMBER>
      </ns0:CLAIM_ADDTNL>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2000C_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop1"">
              <xsl:for-each select=""s1:TS837_2400_Loop1"">
                <xsl:variable name=""var:v801"" select=""s1:PWK_SubLoop_2/s1:PWK_LineSupplementalInformation_2_Loop/s1:PWK_LineSupplementalInformation_2[1]/PWK01_AttachmentReportTypeCode/text()"" />
                <xsl:variable name=""var:v802"" select=""s1:PWK_SubLoop_2/s1:PWK_LineSupplementalInformation_2_Loop/s1:PWK_LineSupplementalInformation_2[1]/PWK02_AttachmentTransmissionCode/text()"" />
                <xsl:variable name=""var:v803"" select=""userCSharp:LogicalExistence(boolean(s1:DTP_SubLoop_4/s1:DTP_Date_PrescriptionDate_2))"" />
                <xsl:variable name=""var:v805"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_RepricedLineItemReferenceNumber_2))"" />
                <xsl:variable name=""var:v807"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_ReferralNumber_4_Loop/s1:REF_ReferralNumber_4))"" />
                <xsl:variable name=""var:v809"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_PriorAuthorization_4_Loop/s1:REF_PriorAuthorization_4))"" />
                <xsl:variable name=""var:v811"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_4))"" />
                <xsl:variable name=""var:v813"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_LineItemControlNumber_2))"" />
                <xsl:variable name=""var:v815"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v816"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
                <xsl:variable name=""var:v817"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[1]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v818"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
                <xsl:variable name=""var:v819"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v820"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[2]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v821"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v822"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[3]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v823"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[4]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v824"" select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:REF_RenderingProviderSecondaryIdentification_4[4]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v825"" select=""userCSharp:StringConcat(string($var:v815) , string($var:v816) , string($var:v817) , string($var:v818) , string($var:v819) , string($var:v816) , string($var:v820) , string($var:v818) , string($var:v821) , string($var:v816) , string($var:v822) , string($var:v818) , string($var:v823) , string($var:v816) , string($var:v824) , string($var:v818))"" />
                <xsl:variable name=""var:v826"" select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_4[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v827"" select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_4[1]/REF02_ServiceFacilityLocationSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v828"" select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_4[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v829"" select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:REF_ServiceFacilityLocationSecondaryIdentification_4[2]/REF02_ServiceFacilityLocationSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v830"" select=""userCSharp:StringConcat(string($var:v826) , string($var:v816) , string($var:v827) , string($var:v818) , string($var:v828) , string($var:v816) , string($var:v829) , string($var:v818))"" />
                <xsl:variable name=""var:v831"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v832"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[1]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v833"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v834"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[2]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v835"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v836"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[3]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v837"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[4]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v838"" select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:REF_SupervisingProviderSecondaryIdentification_4[4]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v839"" select=""userCSharp:StringConcat(string($var:v831) , string($var:v816) , string($var:v832) , string($var:v818) , string($var:v833) , string($var:v816) , string($var:v834) , string($var:v818) , string($var:v835) , string($var:v816) , string($var:v836) , string($var:v818) , string($var:v837) , string($var:v816) , string($var:v838) , string($var:v818))"" />
                <xsl:variable name=""var:v840"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v841"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v842"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v843"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v844"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v845"" select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:REF_ReferringProviderSecondaryIdentification_4[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v846"" select=""userCSharp:StringConcat(string($var:v840) , string($var:v816) , string($var:v841) , string($var:v818) , string($var:v842) , string($var:v816) , string($var:v843) , string($var:v818) , string($var:v844) , string($var:v816) , string($var:v845) , string($var:v818))"" />
                <xsl:variable name=""var:v848"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_AdjustedRepricedLineItemReferenceNumber_2))"" />
                <xsl:variable name=""var:v850"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_MammographyCertificationNumber_4))"" />
                <xsl:variable name=""var:v852"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_ReferringClinicalLaboratoryImprovementAmendment_CLIA_FacilityIdentification_2))"" />
                <xsl:variable name=""var:v854"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_11/s1:REF_ImmunizationBatchNumber_2))"" />
                <xsl:variable name=""var:v856"" select=""s1:TS837_2410_Loop1/s1:REF_PrescriptionorCompoundDrugAssociationNumber_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v857"" select=""s1:TS837_2410_Loop1/s1:REF_PrescriptionorCompoundDrugAssociationNumber_2[1]/REF02_PrescriptionNumber/text()"" />
                <xsl:variable name=""var:v858"" select=""userCSharp:StringConcat(string($var:v856) , string($var:v816) , string($var:v857))"" />
                <xsl:variable name=""var:v859"" select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:REF_OrderingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                <xsl:variable name=""var:v860"" select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:REF_OrderingProviderSecondaryIdentification_2[1]/REF02_OrderingProviderSecondaryIdentifier/text()"" />
                <xsl:variable name=""var:v861"" select=""userCSharp:StringConcat(string($var:v859) , string($var:v816) , string($var:v860))"" />
                <xsl:variable name=""var:v862"" select=""string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP02_DateTimePeriodFormatQualifier/text())"" />
                <xsl:variable name=""var:v863"" select=""userCSharp:LogicalEq($var:v862 , &quot;D8&quot;)"" />
                <xsl:variable name=""var:v865"" select=""userCSharp:LogicalEq($var:v862 , &quot;RD8&quot;)"" />
                <xsl:variable name=""var:v866"" select=""string(s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP03_ServiceDate/text())"" />
                <xsl:variable name=""var:v867"" select=""userCSharp:StringLeft($var:v866 , &quot;8&quot;)"" />
                <xsl:variable name=""var:v869"" select=""userCSharp:StringRight($var:v866 , &quot;8&quot;)"" />
                <xsl:variable name=""var:v871"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:NM1_AmbulanceDrop_offLocation_4))"" />
                <ns0:CLAIM_ADDTNL_DETAIL>
                  <ns0:LINE_NUMBER>
                    <xsl:value-of select=""s1:LX_ServiceLineNumber_2/LX01_AssignedNumber/text()"" />
                  </ns0:LINE_NUMBER>
                  <ns0:SERVICE_CODE>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00302_ProcedureCode/text()"" />
                  </ns0:SERVICE_CODE>
                  <ns0:REPORT_TYPECODE>
                    <xsl:value-of select=""$var:v801"" />
                  </ns0:REPORT_TYPECODE>
                  <ns0:REPORT_TRANCODE>
                    <xsl:value-of select=""$var:v802"" />
                  </ns0:REPORT_TRANCODE>
                  <xsl:if test=""string($var:v803)='true'"">
                    <xsl:variable name=""var:v804"" select=""s1:DTP_SubLoop_4/s1:DTP_Date_PrescriptionDate_2/DTP03_PrescriptionDate/text()"" />
                    <ns0:PRESCRIPTION_DATE>
                      <xsl:value-of select=""$var:v804"" />
                    </ns0:PRESCRIPTION_DATE>
                  </xsl:if>
                  <xsl:if test=""string($var:v805)='true'"">
                    <xsl:variable name=""var:v806"" select=""s1:REF_SubLoop_11/s1:REF_RepricedLineItemReferenceNumber_2/REF02_RepricedLineItemReferenceNumber/text()"" />
                    <ns0:REPRICEDLINE_ITEM_REF>
                      <xsl:value-of select=""$var:v806"" />
                    </ns0:REPRICEDLINE_ITEM_REF>
                  </xsl:if>
                  <xsl:if test=""string($var:v807)='true'"">
                    <xsl:variable name=""var:v808"" select=""s1:REF_SubLoop_11/s1:REF_ReferralNumber_4_Loop/s1:REF_ReferralNumber_4/REF02_ReferralNumber/text()"" />
                    <ns0:REFERRAL_NUMBER>
                      <xsl:value-of select=""$var:v808"" />
                    </ns0:REFERRAL_NUMBER>
                  </xsl:if>
                  <xsl:if test=""string($var:v809)='true'"">
                    <xsl:variable name=""var:v810"" select=""s1:REF_SubLoop_11/s1:REF_PriorAuthorization_4_Loop/s1:REF_PriorAuthorization_4/REF02_PriorAuthorizationorReferralNumber/text()"" />
                    <ns0:PRIOR_AUTHORIZATION>
                      <xsl:value-of select=""$var:v810"" />
                    </ns0:PRIOR_AUTHORIZATION>
                  </xsl:if>
                  <xsl:if test=""string($var:v811)='true'"">
                    <xsl:variable name=""var:v812"" select=""s1:REF_SubLoop_11/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_4/REF02_ClinicalLaboratoryImprovementAmendmentNumber/text()"" />
                    <ns0:CLIA>
                      <xsl:value-of select=""$var:v812"" />
                    </ns0:CLIA>
                  </xsl:if>
                  <xsl:if test=""string($var:v813)='true'"">
                    <xsl:variable name=""var:v814"" select=""s1:REF_SubLoop_11/s1:REF_LineItemControlNumber_2/REF02_LineItemControlNumber/text()"" />
                    <ns0:LINECONTROL_NUM>
                      <xsl:value-of select=""$var:v814"" />
                    </ns0:LINECONTROL_NUM>
                  </xsl:if>
                  <ns0:NTE_QUAL>
                    <xsl:value-of select=""s1:NTE_SubLoop_2/s1:NTE_LineNote_2/NTE01_NoteReferenceCode/text()"" />
                  </ns0:NTE_QUAL>
                  <ns0:NTE_DESCRIPTION>
                    <xsl:value-of select=""s1:NTE_SubLoop_2/s1:NTE_LineNote_2/NTE02_LineNoteText/text()"" />
                  </ns0:NTE_DESCRIPTION>
                  <ns0:REPRICE_METHOD>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP01_PricingMethodology/text()"" />
                  </ns0:REPRICE_METHOD>
                  <ns0:REPRICE_ALLOWED_AMT>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP02_RepricedAllowedAmount/text()"" />
                  </ns0:REPRICE_ALLOWED_AMT>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP03_RepricedSavingAmount"">
                    <ns0:REPRICE_SAVING_AMT>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP03_RepricedSavingAmount/text()"" />
                    </ns0:REPRICE_SAVING_AMT>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM108_IdentificationCodeQualifier"">
                    <ns0:RENDERING_PROV_QUAL>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM108_IdentificationCodeQualifier/text()"" />
                    </ns0:RENDERING_PROV_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM109_RenderingProviderIdentifier"">
                    <ns0:RENDERING_PROV_ID>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM109_RenderingProviderIdentifier/text()"" />
                    </ns0:RENDERING_PROV_ID>
                  </xsl:if>
                  <ns0:RENDERING_TAXONOMY>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:PRV_RenderingProviderSpecialtyInformation_4/PRV03_ProviderTaxonomyCode/text()"" />
                  </ns0:RENDERING_TAXONOMY>
                  <ns0:RENDERING_PROV_LNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM103_RenderingProviderLastorOrganizationName/text()"" />
                  </ns0:RENDERING_PROV_LNAME>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM105_RenderingProviderMiddleName"">
                    <ns0:RENDERING_PROV_MNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM105_RenderingProviderMiddleName/text()"" />
                    </ns0:RENDERING_PROV_MNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM104_RenderingProviderFirstName"">
                    <ns0:RENDERING_PROV_FNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM104_RenderingProviderFirstName/text()"" />
                    </ns0:RENDERING_PROV_FNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM107_RenderingProviderNameSuffix"">
                    <ns0:RENDERING_PROV_SUFFIX>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420A_Loop1/s1:NM1_RenderingProviderName_4/NM107_RenderingProviderNameSuffix/text()"" />
                    </ns0:RENDERING_PROV_SUFFIX>
                  </xsl:if>
                  <ns0:RENDERING_REF>
                    <xsl:value-of select=""$var:v825"" />
                  </ns0:RENDERING_REF>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:NM1_ServiceFacilityLocation_2/NM108_IdentificationCodeQualifier"">
                    <ns0:FACILITY_QUAL>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:NM1_ServiceFacilityLocation_2/NM108_IdentificationCodeQualifier/text()"" />
                    </ns0:FACILITY_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:NM1_ServiceFacilityLocation_2/NM109_LaboratoryorFacilityPrimaryIdentifier"">
                    <ns0:FACILITY_ID>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:NM1_ServiceFacilityLocation_2/NM109_LaboratoryorFacilityPrimaryIdentifier/text()"" />
                    </ns0:FACILITY_ID>
                  </xsl:if>
                  <ns0:FACILITY_LNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:NM1_ServiceFacilityLocation_2/NM103_LaboratoryorFacilityName/text()"" />
                  </ns0:FACILITY_LNAME>
                  <ns0:FACILITY_REF>
                    <xsl:value-of select=""$var:v830"" />
                  </ns0:FACILITY_REF>
                  <ns0:FACILITY_ADD1>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N3_ServiceFacilityLocationAddress_4/N301_LaboratoryorFacilityAddressLine/text()"" />
                  </ns0:FACILITY_ADD1>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N3_ServiceFacilityLocationAddress_4/N302_LaboratoryorFacilityAddressLine"">
                    <ns0:FACILITY_ADD2>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N3_ServiceFacilityLocationAddress_4/N302_LaboratoryorFacilityAddressLine/text()"" />
                    </ns0:FACILITY_ADD2>
                  </xsl:if>
                  <ns0:FACILITY_CITY>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_4/N401_LaboratoryorFacilityCityName/text()"" />
                  </ns0:FACILITY_CITY>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_4/N402_LaboratoryorFacilityStateorProvinceCode"">
                    <ns0:FACILITY_STATE>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_4/N402_LaboratoryorFacilityStateorProvinceCode/text()"" />
                    </ns0:FACILITY_STATE>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_4/N403_LaboratoryorFacilityPostalZoneorZIPCode"">
                    <ns0:FACILITY_ZIP>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420C_Loop1/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_4/N403_LaboratoryorFacilityPostalZoneorZIPCode/text()"" />
                    </ns0:FACILITY_ZIP>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM108_IdentificationCodeQualifier"">
                    <ns0:SUPERVISING_QUAL>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM108_IdentificationCodeQualifier/text()"" />
                    </ns0:SUPERVISING_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM109_SupervisingProviderIdentifier"">
                    <ns0:SUPERVISING_ID>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM109_SupervisingProviderIdentifier/text()"" />
                    </ns0:SUPERVISING_ID>
                  </xsl:if>
                  <ns0:SUPERVISING_LNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM103_SupervisingProviderLastName/text()"" />
                  </ns0:SUPERVISING_LNAME>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM104_SupervisingProviderFirstName"">
                    <ns0:SUPERVISING_FNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM104_SupervisingProviderFirstName/text()"" />
                    </ns0:SUPERVISING_FNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM105_SupervisingProviderMiddleNameorInitial"">
                    <ns0:SUPERVISING_MNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM105_SupervisingProviderMiddleNameorInitial/text()"" />
                    </ns0:SUPERVISING_MNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM107_SupervisingProviderNameSuffix"">
                    <ns0:SUPERVISING_SUFFIX>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420D_Loop1/s1:NM1_SupervisingProviderName_4/NM107_SupervisingProviderNameSuffix/text()"" />
                    </ns0:SUPERVISING_SUFFIX>
                  </xsl:if>
                  <ns0:SUPERVISING_REF>
                    <xsl:value-of select=""$var:v839"" />
                  </ns0:SUPERVISING_REF>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM108_IdentificationCodeQualifier"">
                    <ns0:REFERRING_PROV_QUAL>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM108_IdentificationCodeQualifier/text()"" />
                    </ns0:REFERRING_PROV_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM109_ReferringProviderIdentifier"">
                    <ns0:REFERRING_PROV_ID>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM109_ReferringProviderIdentifier/text()"" />
                    </ns0:REFERRING_PROV_ID>
                  </xsl:if>
                  <ns0:REFERRING_PROV_LNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM103_ReferringProviderLastName/text()"" />
                  </ns0:REFERRING_PROV_LNAME>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM105_ReferringProviderMiddleNameorInitial"">
                    <ns0:REFERRING_PROV_MNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                    </ns0:REFERRING_PROV_MNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM104_ReferringProviderFirstName"">
                    <ns0:REFERRING_PROV_FNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM104_ReferringProviderFirstName/text()"" />
                    </ns0:REFERRING_PROV_FNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM107_ReferringProviderNameSuffix"">
                    <ns0:REFERRING_PROV_SUFFIX>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420F_Loop1_Loop/s1:TS837_2420F_Loop1/s1:NM1_ReferringProviderName_4/NM107_ReferringProviderNameSuffix/text()"" />
                    </ns0:REFERRING_PROV_SUFFIX>
                  </xsl:if>
                  <ns0:REFERRING_REF>
                    <xsl:value-of select=""$var:v846"" />
                  </ns0:REFERRING_REF>
                  <ns0:LINE_ADJUDICATION_CODE>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD01_OtherPayerPrimaryIdentifier/text()"" />
                  </ns0:LINE_ADJUDICATION_CODE>
                  <ns0:LINE_ADJUDICATION_AMT>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD02_ServiceLinePaidAmount/text()"" />
                  </ns0:LINE_ADJUDICATION_AMT>
                  <ns0:LINE_ADJUDICATION_QUAL>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00301_ProductorServiceIDQualifier/text()"" />
                  </ns0:LINE_ADJUDICATION_QUAL>
                  <ns0:LINE_ADJUDICATION_PCODE>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00302_ProcedureCode/text()"" />
                  </ns0:LINE_ADJUDICATION_PCODE>
                  <xsl:variable name=""var:v847"" select=""userCSharp:modifierDentalSub(string(s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00303_ProcedureModifier/text()) , string(s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00304_ProcedureModifier/text()) , string(s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00305_ProcedureModifier/text()) , string(s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00306_ProcedureModifier/text()))"" />
                  <ns0:LINE_ADJUDICATION_MOD>
                    <xsl:value-of select=""$var:v847"" />
                  </ns0:LINE_ADJUDICATION_MOD>
                  <ns0:LINE_ADJUDICATION_QTY>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD05_PaidServiceUnitCount/text()"" />
                  </ns0:LINE_ADJUDICATION_QTY>
                  <ns0:LQ_FRM_TYPE>
                    <xsl:value-of select=""s1:TS837_2440_Loop1/s1:LQ_FormIdentificationCode_2/LQ01_CodeListQualifierCode/text()"" />
                  </ns0:LQ_FRM_TYPE>
                  <ns0:LQ_FRM_CODE>
                    <xsl:value-of select=""s1:TS837_2440_Loop1/s1:LQ_FormIdentificationCode_2/LQ02_FormIdentifier/text()"" />
                  </ns0:LQ_FRM_CODE>
                  <ns0:FRM_ASSIGNED>
                    <xsl:value-of select=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM01_QuestionNumber_Letter/text()"" />
                  </ns0:FRM_ASSIGNED>
                  <xsl:if test=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM02_QuestionResponse"">
                    <ns0:FRM_QUESTION>
                      <xsl:value-of select=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM02_QuestionResponse/text()"" />
                    </ns0:FRM_QUESTION>
                  </xsl:if>
                  <xsl:if test=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM03_QuestionResponse"">
                    <ns0:FRM_RESPONSE>
                      <xsl:value-of select=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM03_QuestionResponse/text()"" />
                    </ns0:FRM_RESPONSE>
                  </xsl:if>
                  <xsl:if test=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM04_QuestionResponse"">
                    <ns0:FRM_DATE>
                      <xsl:value-of select=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM04_QuestionResponse/text()"" />
                    </ns0:FRM_DATE>
                  </xsl:if>
                  <xsl:if test=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM05_QuestionResponse"">
                    <ns0:FRM_AMT>
                      <xsl:value-of select=""s1:TS837_2440_Loop1/s1:FRM_SupportingDocumentation_2/FRM05_QuestionResponse/text()"" />
                    </ns0:FRM_AMT>
                  </xsl:if>
                  <xsl:for-each select=""./*[local-name()='TS837_2430_Loop1'][1]"">
  <xsl:element name=""CAS_ADJ_CODE_PAYER_A_LIST"">
    <xsl:for-each select=""./*[local-name()='CAS_LineAdjustment_2']"">
      <xsl:if test="" CAS01_ClaimAdjustmentGroupCode/text() !=''"">
        <xsl:value-of select=""CAS01_ClaimAdjustmentGroupCode/text()"" />
      </xsl:if>
      <xsl:if test="" CAS02_AdjustmentReasonCode/text() !=''"">
        <xsl:text>*</xsl:text>
        <xsl:value-of select=""CAS02_AdjustmentReasonCode/text()"" />
      </xsl:if>
      <xsl:if test="" CAS03_AdjustmentAmount/text() !=''"">
        <xsl:text>*</xsl:text>
        <xsl:value-of select=""CAS03_AdjustmentAmount/text()"" />
      </xsl:if>
      <xsl:choose>
        <xsl:when test="" CAS04_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS04_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS05_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS05_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS06_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS06_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS07_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS07_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS08_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS08_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS09_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS09_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS10_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS10_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS11_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS11_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS12_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS12_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS13_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS13_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS14_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS14_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS15_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS15_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS16_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS16_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS17_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS17_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS18_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS18_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS19_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS19_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:if test=""position()!=last()"">
        <xsl:text>,</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:element>
</xsl:for-each>
                  <xsl:for-each select=""./*[local-name()='TS837_2430_Loop1'][2]"">
  <xsl:element name=""CAS_ADJ_CODE_PAYER_B_LIST"">
    <xsl:for-each select=""./*[local-name()='CAS_LineAdjustment_2']"">
      <xsl:if test="" CAS01_ClaimAdjustmentGroupCode/text() !=''"">
        <xsl:value-of select=""CAS01_ClaimAdjustmentGroupCode/text()"" />
      </xsl:if>
      <xsl:if test="" CAS02_AdjustmentReasonCode/text() !=''"">
        <xsl:text>*</xsl:text>
        <xsl:value-of select=""CAS02_AdjustmentReasonCode/text()"" />
      </xsl:if>
      <xsl:if test="" CAS03_AdjustmentAmount/text() !=''"">
        <xsl:text>*</xsl:text>
        <xsl:value-of select=""CAS03_AdjustmentAmount/text()"" />
      </xsl:if>
      <xsl:choose>
        <xsl:when test="" CAS04_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS04_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS05_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS05_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS06_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS06_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS07_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS07_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS08_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS08_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS09_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS09_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS10_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS10_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS11_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS11_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS12_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS12_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS12_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS12_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS13_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS13_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS14_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS14_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS15_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS15_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS16_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS16_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS17_AdjustmentReasonCode/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS17_AdjustmentReasonCode/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS18_AdjustmentAmount/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS18_AdjustmentAmount/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:choose>
        <xsl:when test="" CAS19_AdjustmentQuantity/text() !=''"">
          <xsl:text>*</xsl:text>
          <xsl:value-of select=""CAS19_AdjustmentQuantity/text()"" />
        </xsl:when>
        <xsl:otherwise>
          <xsl:text>*</xsl:text>
        </xsl:otherwise>
      </xsl:choose>
      <xsl:if test=""position()!=last()"">
        <xsl:text>,</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:element>
</xsl:for-each>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:NM1_AmbulancePick_upLocation_4/NM103_NameLastorOrganizationName"">
                    <ns0:OTHER_PAYER_A_NAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:NM1_AmbulancePick_upLocation_4/NM103_NameLastorOrganizationName/text()"" />
                    </ns0:OTHER_PAYER_A_NAME>
                  </xsl:if>
                  <ns0:OTHER_PAYER_B_NAME>
                    <xsl:text />
                  </ns0:OTHER_PAYER_B_NAME>
                  <ns0:SERVICE_CODE_QUAL>
                    <xsl:value-of select=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00301_ProductorServiceIDQualifier/text()"" />
                  </ns0:SERVICE_CODE_QUAL>
                  <ns0:REVENUE_CODE>
                    <xsl:text />
                  </ns0:REVENUE_CODE>
                  <xsl:if test=""s1:PWK_SubLoop_2/s1:PWK_LineSupplementalInformation_2_Loop/s1:PWK_LineSupplementalInformation_2/PWK06_AttachmentControlNumber"">
                    <ns0:REPORT_PWK06_ID>
                      <xsl:value-of select=""s1:PWK_SubLoop_2/s1:PWK_LineSupplementalInformation_2_Loop/s1:PWK_LineSupplementalInformation_2/PWK06_AttachmentControlNumber/text()"" />
                    </ns0:REPORT_PWK06_ID>
                  </xsl:if>
                  <ns0:DURABLE_TRANS_CODE>
                    <xsl:value-of select=""s1:PWK_SubLoop_2/s1:PWK_DurableMedicalEquipmentCertificateofMedicalNecessityIndicator_2/PWK02_AttachmentTransmissionCode/text()"" />
                  </ns0:DURABLE_TRANS_CODE>
                  <xsl:if test=""s1:CR1_AmbulanceTransportInformation_4/CR102_PatientWeight"">
                    <ns0:AMBULANCE_WEIGHT>
                      <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_4/CR102_PatientWeight/text()"" />
                    </ns0:AMBULANCE_WEIGHT>
                  </xsl:if>
                  <ns0:AMBULANCE_REASON_CODE>
                    <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_4/CR104_AmbulanceTransportReasonCode/text()"" />
                  </ns0:AMBULANCE_REASON_CODE>
                  <ns0:AMBULANCE_QTY>
                    <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_4/CR106_TransportDistance/text()"" />
                  </ns0:AMBULANCE_QTY>
                  <xsl:if test=""s1:CR1_AmbulanceTransportInformation_4/CR109_RoundTripPurposeDescription"">
                    <ns0:AMBULANCE_DESCRIPTION>
                      <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_4/CR109_RoundTripPurposeDescription/text()"" />
                    </ns0:AMBULANCE_DESCRIPTION>
                  </xsl:if>
                  <ns0:CR301_AMBULANCE_typeCODE>
                    <xsl:value-of select=""s1:CR3_DurableMedicalEquipmentCertification_2/CR301_CertificationTypeCode/text()"" />
                  </ns0:CR301_AMBULANCE_typeCODE>
                  <ns0:CR303_AMBULANCE_QTY>
                    <xsl:value-of select=""s1:CR3_DurableMedicalEquipmentCertification_2/CR303_DurableMedicalEquipmentDuration/text()"" />
                  </ns0:CR303_AMBULANCE_QTY>
                  <ns0:CRC02_AMBULANCE_RESPONSECODE>
                    <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC02_CertificationConditionIndicator/text()"" />
                  </ns0:CRC02_AMBULANCE_RESPONSECODE>
                  <ns0:CRC03_AMBULANCE_CODE1>
                    <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC03_ConditionCode/text()"" />
                  </ns0:CRC03_AMBULANCE_CODE1>
                  <xsl:if test=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC04_ConditionCode"">
                    <ns0:CRC04_AMBULANCE_CODE2>
                      <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC04_ConditionCode/text()"" />
                    </ns0:CRC04_AMBULANCE_CODE2>
                  </xsl:if>
                  <xsl:if test=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC05_ConditionCode"">
                    <ns0:CRC05_AMBULANCE_CODE3>
                      <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC05_ConditionCode/text()"" />
                    </ns0:CRC05_AMBULANCE_CODE3>
                  </xsl:if>
                  <xsl:if test=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC06_ConditionCode"">
                    <ns0:CRC06_AMBULANCE_CODE4>
                      <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC06_ConditionCode/text()"" />
                    </ns0:CRC06_AMBULANCE_CODE4>
                  </xsl:if>
                  <xsl:if test=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC07_ConditionCode"">
                    <ns0:CRC07_AMBULANCE_CODE5>
                      <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_AmbulanceCertification_4_Loop/s1:CRC_AmbulanceCertification_4/CRC07_ConditionCode/text()"" />
                    </ns0:CRC07_AMBULANCE_CODE5>
                  </xsl:if>
                  <ns0:CRC02_HOSPICE_RESPONSECODE>
                    <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_HospiceEmployeeIndicator_2/CRC02_HospiceEmployedProviderIndicator/text()"" />
                  </ns0:CRC02_HOSPICE_RESPONSECODE>
                  <ns0:CRC02_DURABLE_RESPONSECODE>
                    <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_ConditionIndicator_DurableMedicalEquipment_2/CRC02_CertificationConditionIndicator/text()"" />
                  </ns0:CRC02_DURABLE_RESPONSECODE>
                  <ns0:CRC02_DURABLE_CONDITIONCODE>
                    <xsl:value-of select=""s1:CRC_SubLoop_4/s1:CRC_ConditionIndicator_DurableMedicalEquipment_2/CRC03_ConditionIndicator/text()"" />
                  </ns0:CRC02_DURABLE_CONDITIONCODE>
                  <ns0:REVISION_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_DATE_CertificationRevision_RecertificationDate_2/DTP03_CertificationRevisionorRecertificationDate/text()"" />
                  </ns0:REVISION_DATE>
                  <ns0:THERAPY_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_BeginTherapyDate_2/DTP03_BeginTherapyDate/text()"" />
                  </ns0:THERAPY_DATE>
                  <ns0:LAST_CERTIFICATION_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_LastCertificationDate_2/DTP03_LastCertificationDate/text()"" />
                  </ns0:LAST_CERTIFICATION_DATE>
                  <ns0:LAST_SEEN_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_LastSeenDate_4/DTP03_TreatmentorTherapyDate/text()"" />
                  </ns0:LAST_SEEN_DATE>
                  <ns0:TEST_DATE_QUAL>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_TestDate_2_Loop/s1:DTP_Date_TestDate_2/DTP02_DateTimePeriodFormatQualifier/text()"" />
                  </ns0:TEST_DATE_QUAL>
                  <ns0:TEST_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_TestDate_2_Loop/s1:DTP_Date_TestDate_2/DTP03_TestPerformedDate/text()"" />
                  </ns0:TEST_DATE>
                  <ns0:XRAY_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_LastX_rayDate_4/DTP03_LastX_RayDate/text()"" />
                  </ns0:XRAY_DATE>
                  <ns0:INTIAL_TREATMENT_DATE>
                    <xsl:value-of select=""s1:DTP_SubLoop_4/s1:DTP_Date_InitialTreatmentDate_4/DTP03_InitialTreatmentDate/text()"" />
                  </ns0:INTIAL_TREATMENT_DATE>
                  <ns0:AMBULANCE_PAT_COUNT>
                    <xsl:value-of select=""s1:QTY_SubLoop_2/s1:QTY_AmbulancePatientCount_2/QTY02_AmbulancePatientCount/text()"" />
                  </ns0:AMBULANCE_PAT_COUNT>
                  <ns0:OBSTETRIC_UNITS>
                    <xsl:value-of select=""s1:QTY_SubLoop_2/s1:QTY_ObstetricAnesthesiaAdditionalUnits_2/QTY02_ObstetricAdditionalUnits/text()"" />
                  </ns0:OBSTETRIC_UNITS>
                  <ns0:MEA01_REF_ID>
                    <xsl:value-of select=""s1:MEA_TestResult_2/MEA01_MeasurementReferenceIdentificationCode/text()"" />
                  </ns0:MEA01_REF_ID>
                  <ns0:MEA02_QUAL>
                    <xsl:value-of select=""s1:MEA_TestResult_2/MEA02_MeasurementQualifier/text()"" />
                  </ns0:MEA02_QUAL>
                  <ns0:MEA03_VALUE>
                    <xsl:value-of select=""s1:MEA_TestResult_2/MEA03_TestResults/text()"" />
                  </ns0:MEA03_VALUE>
                  <xsl:if test=""string($var:v848)='true'"">
                    <xsl:variable name=""var:v849"" select=""s1:REF_SubLoop_11/s1:REF_AdjustedRepricedLineItemReferenceNumber_2/REF02_AdjustedRepricedLineItemReferenceNumber/text()"" />
                    <ns0:ADJUSTED_ITEM_REF>
                      <xsl:value-of select=""$var:v849"" />
                    </ns0:ADJUSTED_ITEM_REF>
                  </xsl:if>
                  <xsl:if test=""string($var:v850)='true'"">
                    <xsl:variable name=""var:v851"" select=""s1:REF_SubLoop_11/s1:REF_MammographyCertificationNumber_4/REF02_MammographyCertificationNumber/text()"" />
                    <ns0:MAMMOGRAPHY_NUM_REF>
                      <xsl:value-of select=""$var:v851"" />
                    </ns0:MAMMOGRAPHY_NUM_REF>
                  </xsl:if>
                  <xsl:if test=""string($var:v852)='true'"">
                    <xsl:variable name=""var:v853"" select=""s1:REF_SubLoop_11/s1:REF_ReferringClinicalLaboratoryImprovementAmendment_CLIA_FacilityIdentification_2/REF02_ReferringCLIANumber/text()"" />
                    <ns0:LAB_CLIA_REF>
                      <xsl:value-of select=""$var:v853"" />
                    </ns0:LAB_CLIA_REF>
                  </xsl:if>
                  <xsl:if test=""string($var:v854)='true'"">
                    <xsl:variable name=""var:v855"" select=""s1:REF_SubLoop_11/s1:REF_ImmunizationBatchNumber_2/REF02_ImmunizationBatchNumber/text()"" />
                    <ns0:IMM_BATCHNUM_REF>
                      <xsl:value-of select=""$var:v855"" />
                    </ns0:IMM_BATCHNUM_REF>
                  </xsl:if>
                  <ns0:TAX_AMOUNT>
                    <xsl:value-of select=""s1:AMT_SubLoop_4/s1:AMT_SalesTaxAmount_2/AMT02_SalesTaxAmount/text()"" />
                  </ns0:TAX_AMOUNT>
                  <ns0:POSTAGE_FACILITY_AMT>
                    <xsl:value-of select=""s1:AMT_SubLoop_4/s1:AMT_PostageClaimedAmount_2/AMT02_PostageClaimedAmount/text()"" />
                  </ns0:POSTAGE_FACILITY_AMT>
                  <ns0:K3_FILE_INFO>
                    <xsl:value-of select=""s1:K3_FileInformation_4/K301_FixedFormatInformation/text()"" />
                  </ns0:K3_FILE_INFO>
                  <ns0:NTE_LINENOTE>
                    <xsl:value-of select=""s1:NTE_SubLoop_2/s1:NTE_LineNote_2/NTE02_LineNoteText/text()"" />
                  </ns0:NTE_LINENOTE>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP04_RepricingOrganizationIdentifier"">
                    <ns0:HCP04_ORG_ID>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP04_RepricingOrganizationIdentifier/text()"" />
                    </ns0:HCP04_ORG_ID>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP05_RepricingPerDiemorFlatRateAmount"">
                    <ns0:HCP05_FLAT_RATE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP05_RepricingPerDiemorFlatRateAmount/text()"" />
                    </ns0:HCP05_FLAT_RATE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP06_RepricedApprovedAmbulatoryPatientGroupCode"">
                    <ns0:HCP06_DRGCODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP06_RepricedApprovedAmbulatoryPatientGroupCode/text()"" />
                    </ns0:HCP06_DRGCODE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP07_RepricedApprovedAmbulatoryPatientGroupAmount"">
                    <ns0:HCP07_DRGAMT>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP07_RepricedApprovedAmbulatoryPatientGroupAmount/text()"" />
                    </ns0:HCP07_DRGAMT>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP08_Product_ServiceID"">
                    <ns0:HCP08_REVENUECODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP08_Product_ServiceID/text()"" />
                    </ns0:HCP08_REVENUECODE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP09_ProductorServiceIDQualifier"">
                    <ns0:HCP09_SVCODE_QUAL>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP09_ProductorServiceIDQualifier/text()"" />
                    </ns0:HCP09_SVCODE_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP10_RepricedApprovedHCPCSCode"">
                    <ns0:HCP10_SVCODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP10_RepricedApprovedHCPCSCode/text()"" />
                    </ns0:HCP10_SVCODE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP11_UnitorBasisforMeasurementCode"">
                    <ns0:HCP11_UNITS>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP11_UnitorBasisforMeasurementCode/text()"" />
                    </ns0:HCP11_UNITS>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP12_RepricedApprovedServiceUnitCount"">
                    <ns0:HCP12_QUANTITY>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP12_RepricedApprovedServiceUnitCount/text()"" />
                    </ns0:HCP12_QUANTITY>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP13_RejectReasonCode"">
                    <ns0:HCP13_REJECT_CODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP13_RejectReasonCode/text()"" />
                    </ns0:HCP13_REJECT_CODE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP14_PolicyComplianceCode"">
                    <ns0:HCP14_POLICY_CODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP14_PolicyComplianceCode/text()"" />
                    </ns0:HCP14_POLICY_CODE>
                  </xsl:if>
                  <xsl:if test=""s1:HCP_LinePricing_RepricingInformation_2/HCP15_ExceptionCode"">
                    <ns0:HCP15_EXCEPTION_CODE>
                      <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation_2/HCP15_ExceptionCode/text()"" />
                    </ns0:HCP15_EXCEPTION_CODE>
                  </xsl:if>
                  <ns0:LIN03_NATIONALDRUG_CODE>
                    <xsl:value-of select=""s1:TS837_2410_Loop1/s1:LIN_DrugIdentification_2/LIN03_NationalDrugCodeorUniversalProductNumber/text()"" />
                  </ns0:LIN03_NATIONALDRUG_CODE>
                  <ns0:CTP04_NATIONALDRUG_UNIT>
                    <xsl:value-of select=""s1:TS837_2410_Loop1/s1:CTP_DrugQuantity_2/CTP04_NationalDrugUnitCount/text()"" />
                  </ns0:CTP04_NATIONALDRUG_UNIT>
                  <ns0:CTP05_NATIONALDRUG_QUAL>
                    <xsl:value-of select=""s1:TS837_2410_Loop1/s1:CTP_DrugQuantity_2/s1:C001_CompositeUnitofMeasure_12/C00101_CodeQualifier/text()"" />
                  </ns0:CTP05_NATIONALDRUG_QUAL>
                  <ns0:PRESCRIPTION_NUMBER>
                    <xsl:value-of select=""$var:v858"" />
                  </ns0:PRESCRIPTION_NUMBER>
                  <xsl:if test=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00307_ProcedureCodeDescription"">
                    <ns0:SVD03_7_DESCRIPTION>
                      <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/s1:C003_CompositeMedicalProcedureIdentifier_6/C00307_ProcedureCodeDescription/text()"" />
                    </ns0:SVD03_7_DESCRIPTION>
                  </xsl:if>
                  <xsl:if test=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD06_BundledorUnbundledLineNumber"">
                    <ns0:SVD06_ASSIGNED_NUMBER>
                      <xsl:value-of select=""s1:TS837_2430_Loop1/s1:SVD_LineAdjudicationInformation_2/SVD06_BundledorUnbundledLineNumber/text()"" />
                    </ns0:SVD06_ASSIGNED_NUMBER>
                  </xsl:if>
                  <ns0:CAS01_ADJ_CODE>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:CAS_LineAdjustment_2/CAS01_ClaimAdjustmentGroupCode/text()"" />
                  </ns0:CAS01_ADJ_CODE>
                  <ns0:CAS02_ADJ_REASON>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:CAS_LineAdjustment_2/CAS02_AdjustmentReasonCode/text()"" />
                  </ns0:CAS02_ADJ_REASON>
                  <ns0:CAS03_ADJ_AMT>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:CAS_LineAdjustment_2/CAS03_AdjustmentAmount/text()"" />
                  </ns0:CAS03_ADJ_AMT>
                  <xsl:if test=""s1:TS837_2430_Loop1/s1:CAS_LineAdjustment_2/CAS04_AdjustmentQuantity"">
                    <ns0:CAS04_ADJ_QTY>
                      <xsl:value-of select=""s1:TS837_2430_Loop1/s1:CAS_LineAdjustment_2/CAS04_AdjustmentQuantity/text()"" />
                    </ns0:CAS04_ADJ_QTY>
                  </xsl:if>
                  <ns0:LINE_ADJUDICATION_DATE>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:DTP_LineCheckorRemittanceDate_2/DTP03_AdjudicationorPaymentDate/text()"" />
                  </ns0:LINE_ADJUDICATION_DATE>
                  <ns0:PATIENT_LIABILITY>
                    <xsl:value-of select=""s1:TS837_2430_Loop1/s1:AMT_RemainingPatientLiability_4/AMT02_RemainingPatientLiability/text()"" />
                  </ns0:PATIENT_LIABILITY>
                  <ns0:OTH_OPERATING_PROV_LNAME>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_LNAME>
                  <ns0:OTH_OPERATING_PROV_MNAME>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_MNAME>
                  <ns0:OTH_OPERATING_PROV_FNAME>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_FNAME>
                  <ns0:OTH_OPERATING_PROV_SUFFIX>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_SUFFIX>
                  <ns0:OTH_OPERATING_PROV_QUAL>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_QUAL>
                  <ns0:OTH_OPERATING_PROV_ID>
                    <xsl:text />
                  </ns0:OTH_OPERATING_PROV_ID>
                  <ns0:OTH_OPERATING_REF>
                    <xsl:text />
                  </ns0:OTH_OPERATING_REF>
                  <ns0:ORDERING_PROV_LNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM103_OrderingProviderLastName/text()"" />
                  </ns0:ORDERING_PROV_LNAME>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM104_OrderingProviderFirstName"">
                    <ns0:ORDERING_PROV_FNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM104_OrderingProviderFirstName/text()"" />
                    </ns0:ORDERING_PROV_FNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM105_OrderingProviderMiddleNameorInitial"">
                    <ns0:ORDERING_PROV_MNAME>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM105_OrderingProviderMiddleNameorInitial/text()"" />
                    </ns0:ORDERING_PROV_MNAME>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM107_OrderingProviderNameSuffix"">
                    <ns0:ORDERING_PROV_SUFFIX>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM107_OrderingProviderNameSuffix/text()"" />
                    </ns0:ORDERING_PROV_SUFFIX>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM108_IdentificationCodeQualifier"">
                    <ns0:ORDERING_PROV_QUAL>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM108_IdentificationCodeQualifier/text()"" />
                    </ns0:ORDERING_PROV_QUAL>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM109_OrderingProviderIdentifier"">
                    <ns0:ORDERING_PROV_ID>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:NM1_OrderingProviderName_2/NM109_OrderingProviderIdentifier/text()"" />
                    </ns0:ORDERING_PROV_ID>
                  </xsl:if>
                  <ns0:ORDERING_PROV_ADD1>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N3_OrderingProviderAddress_2/N301_OrderingProviderAddressLine/text()"" />
                  </ns0:ORDERING_PROV_ADD1>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N3_OrderingProviderAddress_2/N302_OrderingProviderAddressLine"">
                    <ns0:ORDERING_PROV_ADD2>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N3_OrderingProviderAddress_2/N302_OrderingProviderAddressLine/text()"" />
                    </ns0:ORDERING_PROV_ADD2>
                  </xsl:if>
                  <ns0:ORDERING_PROV_CITY>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N4_OrderingProviderCity_State_ZIPCode_2/N401_OrderingProviderCityName/text()"" />
                  </ns0:ORDERING_PROV_CITY>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N4_OrderingProviderCity_State_ZIPCode_2/N402_OrderingProviderStateorProvinceCode"">
                    <ns0:ORDERING_PROV_STATE>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N4_OrderingProviderCity_State_ZIPCode_2/N402_OrderingProviderStateorProvinceCode/text()"" />
                    </ns0:ORDERING_PROV_STATE>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N4_OrderingProviderCity_State_ZIPCode_2/N403_OrderingProviderPostalZoneorZIPCode"">
                    <ns0:ORDERING_PROV_ZIP>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:N4_OrderingProviderCity_State_ZIPCode_2/N403_OrderingProviderPostalZoneorZIPCode/text()"" />
                    </ns0:ORDERING_PROV_ZIP>
                  </xsl:if>
                  <ns0:ORDERING_PROV_REF>
                    <xsl:value-of select=""$var:v861"" />
                  </ns0:ORDERING_PROV_REF>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER02_OrderingProviderContactName"">
                    <ns0:ORDERING_PER02>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER02_OrderingProviderContactName/text()"" />
                    </ns0:ORDERING_PER02>
                  </xsl:if>
                  <ns0:ORDERING_PER03>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER03_CommunicationNumberQualifier/text()"" />
                  </ns0:ORDERING_PER03>
                  <ns0:ORDERING_PER04>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER04_CommunicationNumber/text()"" />
                  </ns0:ORDERING_PER04>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER05_CommunicationNumberQualifier"">
                    <ns0:ORDERING_PER05>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER05_CommunicationNumberQualifier/text()"" />
                    </ns0:ORDERING_PER05>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER06_CommunicationNumber"">
                    <ns0:ORDERING_PER06>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER06_CommunicationNumber/text()"" />
                    </ns0:ORDERING_PER06>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER07_CommunicationNumberQualifier"">
                    <ns0:ORDERING_PER07>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER07_CommunicationNumberQualifier/text()"" />
                    </ns0:ORDERING_PER07>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER08_CommunicationNumber"">
                    <ns0:ORDERING_PER08>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420E_Loop1/s1:PER_OrderingProviderContactInformation_2/PER08_CommunicationNumber/text()"" />
                    </ns0:ORDERING_PER08>
                  </xsl:if>
                  <ns0:AMBULANCE_PICKUP_ADD1>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N3_AmbulancePick_upLocationAddress_4/N301_AmbulancePick_upAddressLine/text()"" />
                  </ns0:AMBULANCE_PICKUP_ADD1>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N3_AmbulancePick_upLocationAddress_4/N302_AmbulancePick_upAddressLine"">
                    <ns0:AMBULANCE_PICKUP_ADD2>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N3_AmbulancePick_upLocationAddress_4/N302_AmbulancePick_upAddressLine/text()"" />
                    </ns0:AMBULANCE_PICKUP_ADD2>
                  </xsl:if>
                  <ns0:AMBULANCE_PICKUP_CITY>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_4/N401_AmbulancePick_upCityName/text()"" />
                  </ns0:AMBULANCE_PICKUP_CITY>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_4/N402_AmbulancePick_upStateorProvinceCode"">
                    <ns0:AMBULANCE_PICKUP_STATE>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_4/N402_AmbulancePick_upStateorProvinceCode/text()"" />
                    </ns0:AMBULANCE_PICKUP_STATE>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_4/N403_AmbulancePick_upPostalZoneorZIPCode"">
                    <ns0:AMBULANCE_PICKUP_ZIP>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420G_Loop1/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_4/N403_AmbulancePick_upPostalZoneorZIPCode/text()"" />
                    </ns0:AMBULANCE_PICKUP_ZIP>
                  </xsl:if>
                  <ns0:AMBULANCE_DROPOFF_ADD1>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_4/N301_AmbulanceDrop_offAddressLine/text()"" />
                  </ns0:AMBULANCE_DROPOFF_ADD1>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_4/N302_AmbulanceDrop_offAddressLine"">
                    <ns0:AMBULANCE_DROPOFF_ADD2>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N3_AmbulanceDrop_offLocationAddress_4/N302_AmbulanceDrop_offAddressLine/text()"" />
                    </ns0:AMBULANCE_DROPOFF_ADD2>
                  </xsl:if>
                  <ns0:AMBULANCE_DROPOFF_CITY>
                    <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_4/N401_AmbulanceDrop_offCityName/text()"" />
                  </ns0:AMBULANCE_DROPOFF_CITY>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_4/N402_AmbulanceDrop_offStateorProvinceCode"">
                    <ns0:AMBULANCE_DROPOFF_STATE>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_4/N402_AmbulanceDrop_offStateorProvinceCode/text()"" />
                    </ns0:AMBULANCE_DROPOFF_STATE>
                  </xsl:if>
                  <xsl:if test=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_4/N403_AmbulanceDrop_offPostalZoneorZIPCode"">
                    <ns0:AMBULANCE_DROPOFF_ZIP>
                      <xsl:value-of select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_4/N403_AmbulanceDrop_offPostalZoneorZIPCode/text()"" />
                    </ns0:AMBULANCE_DROPOFF_ZIP>
                  </xsl:if>
                  <ns0:OPL_VALUE_AMOUNT_LIST>
                    <xsl:text />
                  </ns0:OPL_VALUE_AMOUNT_LIST>
                  <ns0:OPL_VALUE_CODE_LIST>
                    <xsl:text />
                  </ns0:OPL_VALUE_CODE_LIST>
                  <ns0:RULE_NUMBER>
                    <xsl:text />
                  </ns0:RULE_NUMBER>
                  <ns0:SPCC_AMOUNT>
                    <xsl:text />
                  </ns0:SPCC_AMOUNT>
                  <ns0:SPCC_CODE>
                    <xsl:text />
                  </ns0:SPCC_CODE>
                  <ns0:SPCC_PERCENT>
                    <xsl:text />
                  </ns0:SPCC_PERCENT>
                  <ns0:PPO_AVAILABILITY>
                    <xsl:text />
                  </ns0:PPO_AVAILABILITY>
                  <ns0:PERFORMING_PROV_NUMBER>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_NUMBER>
                  <ns0:PERFORMING_PROV_LNAME>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_LNAME>
                  <ns0:PERFORMING_PROV_MNAME>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_MNAME>
                  <ns0:PERFORMING_PROV_FNAME>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_FNAME>
                  <ns0:PERFORMING_PROV_ZIP>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_ZIP>
                  <ns0:PERFORMING_PROV_SPECIALTY>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_SPECIALTY>
                  <ns0:PERFORMING_PROV_PROVIDER_TYPE>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_PROVIDER_TYPE>
                  <ns0:PERFORMING_PROV_CLASSIFICATION>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_CLASSIFICATION>
                  <ns0:PERFORMING_PROV_TAXONOMY>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_TAXONOMY>
                  <ns0:PERFORMING_PROV_NPI>
                    <xsl:text />
                  </ns0:PERFORMING_PROV_NPI>
                  <ns0:SF_MESSAGE_CODE>
                    <xsl:text />
                  </ns0:SF_MESSAGE_CODE>
                  <ns0:PERCENTAGE_FACTOR>
                    <xsl:text />
                  </ns0:PERCENTAGE_FACTOR>
                  <ns0:PRICING_METHOD>
                    <xsl:text />
                  </ns0:PRICING_METHOD>
                  <ns0:DF_MESSAGE_CODE>
                    <xsl:text />
                  </ns0:DF_MESSAGE_CODE>
                  <ns0:SEC_PAYER_PROCESS_QUAL>
                    <xsl:text />
                  </ns0:SEC_PAYER_PROCESS_QUAL>
                  <xsl:for-each select=""./*[local-name()='TS837_2430_Loop1'][1]"">
          <xsl:element name=""PRI_LINE_PAID_AMT"">
            <xsl:for-each select=""./*[local-name()='SVD_LineAdjudicationInformation_2']"">
              <xsl:if test="" SVD02_ServiceLinePaidAmount/text() !=''"">
                <xsl:value-of select=""SVD02_ServiceLinePaidAmount/text()"" />
              </xsl:if>
            </xsl:for-each>
          </xsl:element>
</xsl:for-each>
                  <xsl:for-each select=""./*[local-name()='TS837_2430_Loop1'][2]"">
          <xsl:element name=""SEC_LINE_PAID_AMT"">
            <xsl:for-each select=""./*[local-name()='SVD_LineAdjudicationInformation_2']"">
              <xsl:if test="" SVD02_ServiceLinePaidAmount/text() !=''"">
                <xsl:value-of select=""SVD02_ServiceLinePaidAmount/text()"" />
              </xsl:if>
            </xsl:for-each>
          </xsl:element>
</xsl:for-each>
                  <xsl:if test=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00307_Description"">
                    <ns0:PROCEDURE_DESCRIPTION>
                      <xsl:value-of select=""s1:SV1_ProfessionalService_2/s1:C003_CompositeMedicalProcedureIdentifier_4/C00307_Description/text()"" />
                    </ns0:PROCEDURE_DESCRIPTION>
                  </xsl:if>
                  <xsl:if test=""string($var:v863)='true'"">
                    <xsl:variable name=""var:v864"" select=""s1:DTP_SubLoop_4/s1:DTP_Date_ServiceDate_2/DTP03_ServiceDate/text()"" />
                    <ns0:SERVICE_FROM_DATE>
                      <xsl:value-of select=""$var:v864"" />
                    </ns0:SERVICE_FROM_DATE>
                  </xsl:if>
                  <xsl:if test=""string($var:v865)='true'"">
                    <xsl:variable name=""var:v868"" select=""string($var:v867)"" />
                    <ns0:SERVICE_FROM_DATE>
                      <xsl:value-of select=""$var:v868"" />
                    </ns0:SERVICE_FROM_DATE>
                  </xsl:if>
                  <xsl:if test=""string($var:v865)='true'"">
                    <xsl:variable name=""var:v870"" select=""string($var:v869)"" />
                    <ns0:SERVICE_THROUGH_DATE>
                      <xsl:value-of select=""$var:v870"" />
                    </ns0:SERVICE_THROUGH_DATE>
                  </xsl:if>
                  <xsl:if test=""s1:CR1_AmbulanceTransportInformation_4/CR110_StretcherPurposeDescription"">
                    <ns0:AMBULANCE_STRETCHER_DESC>
                      <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_4/CR110_StretcherPurposeDescription/text()"" />
                    </ns0:AMBULANCE_STRETCHER_DESC>
                  </xsl:if>
                  <xsl:if test=""string($var:v871)='true'"">
                    <xsl:variable name=""var:v872"" select=""s1:NM1_SubLoop_9/s1:TS837_2420H_Loop1/s1:NM1_AmbulanceDrop_offLocation_4/NM103_AmbulanceDrop_offLocation/text()"" />
                    <ns0:AMBULANCE_DROPOFF_NAME>
                      <xsl:value-of select=""$var:v872"" />
                    </ns0:AMBULANCE_DROPOFF_NAME>
                  </xsl:if>
                </ns0:CLAIM_ADDTNL_DETAIL>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
    </ns0:Integration_Professional_Claims>
  </xsl:template>
  <msxsl:script language=""C#"" implements-prefix=""userCSharp""><![CDATA[
public string StringLeft(string str, string count)
{
	string retval = """";
	double d = 0;
	if (str != null && IsNumeric(count, ref d))
	{
		int i = (int) d;
		if (i > 0)
		{ 
			if (i <= str.Length)
			{
				retval = str.Substring(0, i);
			}
			else
			{
				retval = str;
			}
		}
	}
	return retval;
}


public string InitCumulativeMin(int index)
{
	if (index >= 0)
	{
		if (index >= myCumulativeMinArray.Count)
		{
			int i = myCumulativeMinArray.Count;
			for (; i<=index; i++)
			{
				myCumulativeMinArray.Add("""");
			}
		}
		else
		{
			myCumulativeMinArray[index] = """";
		}
	}
	return """";
}

public System.Collections.ArrayList myCumulativeMinArray = new System.Collections.ArrayList();

public string AddToCumulativeMin(int index, string val, string notused)
{
	if (index < 0 || index >= myCumulativeMinArray.Count)
	{
		return """";
	}
	double d = 0;
	if (IsNumeric(val, ref d))
	{
		if (myCumulativeMinArray[index] is string || (d < (double)(myCumulativeMinArray[index])))
		{
			myCumulativeMinArray[index] = d;
		}
	}
	return (myCumulativeMinArray[index] is double) ? ((double)myCumulativeMinArray[index]).ToString(System.Globalization.CultureInfo.InvariantCulture) : """";
}

public string GetCumulativeMin(int index)
{
	if (index < 0 || index >= myCumulativeMinArray.Count)
	{
		return """";
	}
	return (myCumulativeMinArray[index] is double) ? ((double)myCumulativeMinArray[index]).ToString(System.Globalization.CultureInfo.InvariantCulture) : """";
}

public string ExternalClmID(string RepriceClaimID,string ExternalClaimID)
{
     if (!string.IsNullOrEmpty(ExternalClaimID))
            return ExternalClaimID;
     else if (!string.IsNullOrEmpty(RepriceClaimID))
             return RepriceClaimID;
     else
             return string.Empty;
}

public bool LogicalExistence(bool val)
{
	return val;
}


public string StringUpperCase(string str)
{
	if (str == null)
	{
		return """";
	}
	return str.ToUpper(System.Globalization.CultureInfo.InvariantCulture);
}


public string cobindicator(string amount,string svdamt)
        {
            if ((!string.IsNullOrEmpty(amount)) || (!string.IsNullOrEmpty(svdamt)))
                return ""Y"";
            else
                return ""N"";
        }

public string cobstatusprof(string amount)
        {
            if (!string.IsNullOrEmpty(amount))
                return ""2"";
            else
                return ""0"";
        }

public string ADJREMITDATE(string HeaderremitdateExistence, string Hdrrmtdate, string linermtdate)
{
	if(System.Convert.ToBoolean(HeaderremitdateExistence))
	{
		return Hdrrmtdate;
	}
	else
	{
		return linermtdate;
	}
}


public string strAuthNumber(string PriorAuth, string ReferralNumb)
        {
            if (!string.IsNullOrEmpty(PriorAuth))
                return PriorAuth;
            else if (!string.IsNullOrEmpty(ReferralNumb))
                return ReferralNumb;
            else
                return string.Empty;
        }

public bool LogicalEq(string val1, string val2)
{
	bool ret = false;
	double d1 = 0;
	double d2 = 0;
	if (IsNumeric(val1, ref d1) && IsNumeric(val2, ref d2))
	{
		ret = d1 == d2;
	}
	else
	{
		ret = String.Compare(val1, val2, StringComparison.Ordinal) == 0;
	}
	return ret;
}


public string PayToProviderIDQual(string G2Check, string RefIDQual)
{
	if(System.Convert.ToBoolean(G2Check))
	{
		return RefIDQual;
	}
	else
		return String.Empty;
}

public string PrincipalDiagQual(string diagqual)
{
	if(diagqual == ""ABK"")
                return ""0"";
	else
                return ""9"";
}

public string PATADDRESS(string patadd1, string sbradd1, int PatExistence)
{
	if(PatExistence==1)
	{
		return (patadd1);
	}
	else
	{
		return (sbradd1);
	}
}


public string PATADDRESSST( string patadd2, string sbradd2, int PatExistence)
{
	if(PatExistence==1)
	{
		return patadd2;
	}
	else
	{
		return sbradd2;
	}
}


public string PATCITY(string patcity, string sbrcity, int PatExistence)
{
	if(PatExistence==1)
	{
		return patcity;
	}
	else
	{
		return sbrcity;
	}
}


public string PATSTATE(string patstate, string sbrstate, int PatExistence)
{
	if(PatExistence==1)
	{
		return patstate;
	}
	else
	{
		return sbrstate;
	}
}


public string PATZIP(string patzip, string sbrzip, int PatExistence)
{
	if(PatExistence==1)
	{
		return patzip;
	}
	else
	{
		return sbrzip;
	}
}


public int nHaveData(string bExist, string nSize)  
{
	if(System.Convert.ToBoolean(bExist) 
&& (System.Convert.ToInt32(nSize)>0))
		return 1;
	else
		return 0;
}


public int StringSize(string str)
{
	if (str == null)
	{
		return 0;
	}
	return str.Length;
}


public string conditionEmp(string CLM11NodeExistence, string C02401_RelatedCausesCode, string C02402_RelatedCausesCode, string C02403_RelatedCausesCode)
{
	if(System.Convert.ToBoolean(CLM11NodeExistence))
	{
		if(C02401_RelatedCausesCode == ""EM"" || C02402_RelatedCausesCode == ""EM"" || C02403_RelatedCausesCode == ""EM"")
		{
			return ""Y"";
		}
		else
		{
			return ""N"";
		}
	}
	else
	{
		return ""N"";
	}
}

public string conditionAuto(string CLM11NodeExistence, string C02401_RelatedCausesCode, string C02402_RelatedCausesCode, string C02403_RelatedCausesCode)
{
	if(System.Convert.ToBoolean(CLM11NodeExistence))
	{
		if(C02401_RelatedCausesCode == ""AA"" || C02402_RelatedCausesCode == ""AA"" || C02403_RelatedCausesCode == ""AA"")
		{
			return ""Y"";
		}
		else
		{
			return ""N"";
		}
	}
	else
	{
		return ""N"";
	}
}

public string conditionOth(string CLM11NodeExistence, string C02401_RelatedCausesCode, string C02402_RelatedCausesCode, string C02403_RelatedCausesCode)
{
	if(System.Convert.ToBoolean(CLM11NodeExistence))
	{
		if(C02401_RelatedCausesCode == ""OA"" || C02402_RelatedCausesCode == ""OA"" || C02403_RelatedCausesCode == ""OA"")
		{
			return ""Y"";
		}
		else
		{
			return ""N"";
		}
	}
	else
	{
		return ""N"";
	}
}

 public string DisabilityBeginDate(string DisabilityDatesExistence, string DTP01_DDate, string DTP02_DDate, string DTP03_DDate)
        {
            if (System.Convert.ToBoolean(DisabilityDatesExistence))
            {
                if ((DTP02_DDate.Equals(""RD8"")) && (DTP01_DDate.Equals(""314"")))
                {
                    return DTP03_DDate.Substring(0, 8);
                }
                else if ((DTP02_DDate.Equals(""D8"")) && (DTP01_DDate.Equals(""360"")))
                {
                    return DTP03_DDate;
                }
                else
                {
                    return string.Empty;
                }

            }
            else
            {
                return string.Empty;
            }
        }

 public string DisabilityEndDate(string DisabilityDatesExistence, string DTP01_DDate, string DTP02_DDate, string DTP03_DDate)
        {
            if (System.Convert.ToBoolean(DisabilityDatesExistence))
            {
                if ((DTP02_DDate.Equals(""RD8"")) && (DTP01_DDate.Equals(""314"")))
                {
                    return DTP03_DDate.Substring(9, 8);
                }
                else if ((DTP02_DDate.Equals(""D8"")) && (DTP01_DDate.Equals(""361"")))
                {
                    return DTP03_DDate;
                }
                else
                {
                    return string.Empty;
                }

            }
            else
            {
                return string.Empty;
            }
        }

public  string InstDiagCodesList(string HI156Q, string HI_156, string HI164Q, string HI_164, string HI172Q, string HI_172, string HI180Q, string HI_180,
             string HI188Q, string HI_188, string HI196Q, string HI_196, string HI204Q, string HI_204, string HI212Q, string HI_212, string HI220Q, string HI_220,
             string HI228Q, string HI_228, string HI236Q, string HI_236, string HI244Q, string HI_244)
         {
             string DiagCodesList = string.Empty;
             bool eCodeChk;

 if (!string.IsNullOrEmpty(HI156Q) && string.IsNullOrEmpty(HI_156))
            {
                 HI_156 = "" "";
             }

             if (!string.IsNullOrEmpty(HI164Q) && string.IsNullOrEmpty(HI_164))
             {
                 HI_164 = "" "";
              }

             if (!string.IsNullOrEmpty(HI172Q) && string.IsNullOrEmpty(HI_172))
             {
                 HI_172 = "" "";
             }

        if (!string.IsNullOrEmpty(HI180Q) && string.IsNullOrEmpty(HI_180))
        {
            HI_180 = "" "";
        }

        if (!string.IsNullOrEmpty(HI188Q) && string.IsNullOrEmpty(HI_188))
        {
            HI_188 = "" "";
        }

        if (!string.IsNullOrEmpty(HI196Q) && string.IsNullOrEmpty(HI_196))
        {
            HI_196 = "" "";
        }

        if (!string.IsNullOrEmpty(HI204Q) && string.IsNullOrEmpty(HI_204))
        {
            HI_204 = "" "";
        }

        if (!string.IsNullOrEmpty(HI212Q) && string.IsNullOrEmpty(HI_212))
        {
            HI_212 = "" "";
        }

        if (!string.IsNullOrEmpty(HI220Q) && string.IsNullOrEmpty(HI_220))
        {
            HI_220 = "" "";
        }

        if (!string.IsNullOrEmpty(HI228Q) && string.IsNullOrEmpty(HI_228))
        {
            HI_228 = "" "";
        }

        if (!string.IsNullOrEmpty(HI236Q) && string.IsNullOrEmpty(HI_236))
        {
            HI_236 = "" "";
        }

        if (!string.IsNullOrEmpty(HI244Q) && string.IsNullOrEmpty(HI_244))
        {
            HI_244 = "" "";
        }
 
             //HI_156
             if (!string.IsNullOrEmpty(HI_156))
             {
 
                 if (HI156Q == ""BK"")
                 {
                     eCodeChk = HI_156.StartsWith(""E"");
                     if (HI_156.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_156 = HI_156.Insert(HI_156.Length - 1, ""."");
                         else
                             HI_156 = HI_156.Insert(HI_156.Length - 2, ""."");
                     }
                     else if (HI_156.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_156 = HI_156.Insert(HI_156.Length - 1, ""."");
                     }
		     else
		             HI_156 = HI_156;
                 }
                 else if(HI156Q == ""ABK"")
                 {
                     if (HI_156.Length > 3)
                         HI_156 = HI_156.Insert(3, ""."");
		     else
		         HI_156 = HI_156;
                 }
                 else
                     DiagCodesList = HI_156 ;
 
                 DiagCodesList = HI_156;
             }
 
 
             //HI_164
             if (!string.IsNullOrEmpty(HI_164))
             {
                 if (HI164Q == ""BF"")
                 {
                     eCodeChk = HI_164.StartsWith(""E"");
                     if (HI_164.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_164 = HI_164.Insert(HI_164.Length - 1, ""."");
                         else
                             HI_164 = HI_164.Insert(HI_164.Length - 2, ""."");
                     }
                     else if (HI_164.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_164 = HI_164.Insert(HI_164.Length - 1, ""."");
                     }
		     else
		          HI_164 = HI_164;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_164;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_164;
                 }
                 else if (HI164Q == ""ABF"")
                 {
                     if (HI_164.Length > 3)
                         HI_164 = HI_164.Insert(3, ""."");
		     else
		         HI_164 = HI_164;
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_164;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_164;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_172
             if (!string.IsNullOrEmpty(HI_172))
             {
                 if (HI172Q == ""BF"")
                 {
                     eCodeChk = HI_172.StartsWith(""E"");
                     if (HI_172.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_172 = HI_172.Insert(HI_172.Length - 1, ""."");
                         else
                             HI_172 = HI_172.Insert(HI_172.Length - 2, ""."");
                     }
                     else if (HI_172.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_172 = HI_172.Insert(HI_172.Length - 1, ""."");
                     }
		     else
		          HI_172 = HI_172;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_172;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_172;
                 }
                 else if (HI172Q == ""ABF"")
                 {
                     if (HI_172.Length > 3)
                         HI_172 = HI_172.Insert(3, ""."");
		     else
		         HI_172 = HI_172;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_172;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_172;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_180
             if (!string.IsNullOrEmpty(HI_180))
             {
                 if (HI180Q == ""BF"")
                 {
                     eCodeChk = HI_180.StartsWith(""E"");
                     if (HI_180.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_180 = HI_180.Insert(HI_180.Length - 1, ""."");
                         else
                             HI_180 = HI_180.Insert(HI_180.Length - 2, ""."");
                     }
                     else if (HI_180.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_180 = HI_180.Insert(HI_180.Length - 1, ""."");
                     }
		     else
		         HI_180 = HI_180;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_180;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_180;
                 }
                 else if (HI180Q == ""ABF"")
                 {
                     if (HI_180.Length > 3)
                         HI_180 = HI_180.Insert(3, ""."");
		     else
		         HI_180 = HI_180;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_180;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_180;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_188
             if (!string.IsNullOrEmpty(HI_188))
             {
                 if (HI188Q == ""BF"")
                 {
                     eCodeChk = HI_188.StartsWith(""E"");
                     if (HI_188.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_188 = HI_188.Insert(HI_188.Length - 1, ""."");
                         else
                             HI_188 = HI_188.Insert(HI_188.Length - 2, ""."");
                     }
                     else if (HI_188.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_188 = HI_188.Insert(HI_188.Length - 1, ""."");
                     }
		     else
		         HI_188 = HI_188;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_188;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_188;
                 }
                 else if (HI188Q == ""ABF"")
                 {
                     if (HI_188.Length > 3)
                         HI_188 = HI_188.Insert(3, ""."");
		     else
		         HI_188 = HI_188;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_188;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_188;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_196
             if (!string.IsNullOrEmpty(HI_196))
             {
                 if (HI196Q == ""BF"")
                 {
                     eCodeChk = HI_196.StartsWith(""E"");
                     if (HI_196.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_196 = HI_196.Insert(HI_196.Length - 1, ""."");
                         else
                             HI_196 = HI_196.Insert(HI_196.Length - 2, ""."");
                     }
                     else if (HI_196.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_196 = HI_196.Insert(HI_196.Length - 1, ""."");
                     }
		     else
		         HI_196 = HI_196;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_196;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_196;
                 }
                 else if (HI196Q == ""ABF"")
                 {
                     if (HI_196.Length > 3)
                         HI_196 = HI_196.Insert(3, ""."");
		     else
		         HI_196 = HI_196;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_196;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_196;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_204
             if (!string.IsNullOrEmpty(HI_204))
             {
                 if (HI204Q == ""BF"")
                 {
                     eCodeChk = HI_204.StartsWith(""E"");
                     if (HI_204.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_204 = HI_204.Insert(HI_204.Length - 1, ""."");
                         else
                             HI_204 = HI_204.Insert(HI_204.Length - 2, ""."");
                     }
                     else if (HI_204.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_204 = HI_204.Insert(HI_204.Length - 1, ""."");
                     }
		     else
		         HI_204 = HI_204;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_204;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_204;
                 }
                 else if (HI204Q == ""ABF"")
                 {
                     if (HI_204.Length > 3)
                         HI_204 = HI_204.Insert(3, ""."");
		     else
		         HI_204 = HI_204;
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_204;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_204;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_212
             if (!string.IsNullOrEmpty(HI_212))
             {
                 if (HI212Q == ""BF"")
                 {
                     eCodeChk = HI_212.StartsWith(""E"");
                     if (HI_212.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_212 = HI_212.Insert(HI_212.Length - 1, ""."");
                         else
                             HI_212 = HI_212.Insert(HI_212.Length - 2, ""."");
                     }
                     else if (HI_212.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_212 = HI_212.Insert(HI_212.Length - 1, ""."");
                     }
		     else
		         HI_212 = HI_212;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_212;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_212;
                 }
                 else if (HI212Q == ""ABF"")
                 {
                     if (HI_212.Length > 3)
                         HI_212 = HI_212.Insert(3, ""."");
		     else
		         HI_212 = HI_212;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_212;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_212;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_220
             if (!string.IsNullOrEmpty(HI_220))
             {
                 if (HI220Q == ""BF"")
                 {
                     eCodeChk = HI_220.StartsWith(""E"");
                     if (HI_220.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_220 = HI_220.Insert(HI_220.Length - 1, ""."");
                         else
                             HI_220 = HI_220.Insert(HI_220.Length - 2, ""."");
                     }
                     else if (HI_220.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_220 = HI_220.Insert(HI_220.Length - 1, ""."");
                     }
		     else
		         HI_220 = HI_220;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_220;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_220;
                 }
                 else if (HI220Q == ""ABF"")
                 {
                     if (HI_220.Length > 3)
                         HI_220 = HI_220.Insert(3, ""."");
		     else
		         HI_220 = HI_220;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_220;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_220;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_228
             if (!string.IsNullOrEmpty(HI_228))
             {
                 if (HI228Q == ""BF"")
                 {
                     eCodeChk = HI_228.StartsWith(""E"");
                     if (HI_228.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_228 = HI_228.Insert(HI_228.Length - 1, ""."");
                         else
                             HI_228 = HI_228.Insert(HI_228.Length - 2, ""."");
                     }
                     else if (HI_228.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_228 = HI_228.Insert(HI_228.Length - 1, ""."");
                     }
		     else
		         HI_228 = HI_228;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_228;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_228;
                 }
                 else if (HI228Q == ""ABF"")
                 {
                     if (HI_228.Length > 3)
                         HI_228 = HI_228.Insert(3, ""."");
		     else
		         HI_228 = HI_228;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_228;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_228;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_236
             if (!string.IsNullOrEmpty(HI_236))
             {
                 if (HI236Q == ""BF"")
                 {
                     eCodeChk = HI_236.StartsWith(""E"");
                     if (HI_236.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_236 = HI_236.Insert(HI_236.Length - 1, ""."");
                         else
                             HI_236 = HI_236.Insert(HI_236.Length - 2, ""."");
                     }
                     else if (HI_236.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_236 = HI_236.Insert(HI_236.Length - 1, ""."");
                     }
		     else
		         HI_236 = HI_236;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_236;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_236;
                 }
                 else if (HI236Q == ""ABF"")
                 {
                     if (HI_236.Length > 3)
                         HI_236 = HI_236.Insert(3, ""."");
		     else
		         HI_236 = HI_236;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_236;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_236;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             //HI_244
             if (!string.IsNullOrEmpty(HI_244))
             {
                 if (HI244Q == ""BF"")
                 {
                     eCodeChk = HI_244.StartsWith(""E"");
                     if (HI_244.Length.Equals(5))
                     {
                         if (eCodeChk)
                             HI_244 = HI_244.Insert(HI_244.Length - 1, ""."");
                         else
                             HI_244 = HI_244.Insert(HI_244.Length - 2, ""."");
                     }
                     else if (HI_244.Length.Equals(4))
                     {
                         if (eCodeChk == false)
                             HI_244 = HI_244.Insert(HI_244.Length - 1, ""."");
                     }
		     else
		         HI_244 = HI_244;
 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_244;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_244;
                 }
                 else if (HI244Q == ""ABF"")
                 {
                     if (HI_244.Length > 3)
                         HI_244 = HI_244.Insert(3, ""."");
		     else
		         HI_244 = HI_244;
			 
                     if (string.IsNullOrEmpty(DiagCodesList))
                         DiagCodesList = HI_244;
                     else
                         DiagCodesList = DiagCodesList + "","" + HI_244;
                 }
                 else
                     DiagCodesList = DiagCodesList;
             }
 
 
             return DiagCodesList + "","";
        }


public string ConditionCodes(string C022_CD1, string C022_CD2, string C022_CD3, string C022_CD4, string C022_CD5, string C022_CD6, string C022_CD7, string C022_CD8,string C022_CD9,string C022_CD10,string C022_CD11,string C022_CD12)
        {
            string ConditionCodesList = string.Empty;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD1;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD1;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD2;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD2;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD3;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD3;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD4;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD4;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD5;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD5;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD6;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD6;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD7;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD7;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD8;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD8;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD9;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD9;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD10;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD10;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD11;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD11;

            if (string.IsNullOrEmpty(ConditionCodesList))
                ConditionCodesList = C022_CD12;
            else
                ConditionCodesList = ConditionCodesList + "","" + C022_CD12;

            return ConditionCodesList;
        }

  public string DTPseg(string dt454,string dtp454,string dt304, string dtp304,string dt453, string dtp453,
             string dt439, string dtp439, string dt455, string dtp455, string dt471, string dtp471, string dt090, string dtp090, string dt444, string dtp444)
         {
             string dtpdate = string.Empty;

             if (System.Convert.ToBoolean(dt454))
                 dtpdate = dtp454;
             else if (System.Convert.ToBoolean(dt304))
                 dtpdate = dtp304;
             else if (System.Convert.ToBoolean(dt453))
                 dtpdate = dtp453;
             else if (System.Convert.ToBoolean(dt439))
                 dtpdate = dtp439;
             else if (System.Convert.ToBoolean(dt455))
                 dtpdate = dtp455;
             else if (System.Convert.ToBoolean(dt471))
                 dtpdate = dtp471;
             else if (System.Convert.ToBoolean(dt090))
                 dtpdate = dtp090;
             else
                 dtpdate = dtp444;
             return dtpdate;

         }

  public string DTPsegQual(string dt454,string dtp454,string dt304, string dtp304,string dt453, string dtp453,
             string dt439, string dtp439, string dt455, string dtp455, string dt471, string dtp471, string dt090, string dtp090, string dt444, string dtp444)
         {
             string dtpdate = string.Empty;

             if (System.Convert.ToBoolean(dt454))
                 dtpdate = dtp454;
             else if (System.Convert.ToBoolean(dt304))
                 dtpdate = dtp304;
             else if (System.Convert.ToBoolean(dt453))
                 dtpdate = dtp453;
             else if (System.Convert.ToBoolean(dt439))
                 dtpdate = dtp439;
             else if (System.Convert.ToBoolean(dt455))
                 dtpdate = dtp455;
             else if (System.Convert.ToBoolean(dt471))
                 dtpdate = dtp471;
             else if (System.Convert.ToBoolean(dt090))
                 dtpdate = dtp090;
             else
                 dtpdate = dtp444;
             return dtpdate;

         }

  public string DTPIllnesssegQual(string dt431,string dtp431,string dt484, string dtp484)
         {
             string dtpdate = string.Empty;

             if (System.Convert.ToBoolean(dt431))
                 dtpdate = dtp431;
             else
                 dtpdate = dtp484;
             return dtpdate;

         }

  public string DTPIllnessseg(string dt431,string dtp431,string dt484, string dtp484)
         {
             string dtpdate = string.Empty;

             if (System.Convert.ToBoolean(dt431))
                 dtpdate = dtp431;
             else
                 dtpdate = dtp484;
             return dtpdate;

         }

public string SubServiceModifierList(string PM303, string PM304, string PM305, string PM306)
{
	string ModList = string.Empty;

	if(!string.IsNullOrEmpty(PM303))
	{
		ModList = PM303;
	}
	
	if(!string.IsNullOrEmpty(PM304))
	{
		if(string.IsNullOrEmpty(ModList))
			ModList = PM304;
		else
			ModList = ModList + "","" + PM304; 
	}

	if(!string.IsNullOrEmpty(PM305))
	{
		if(string.IsNullOrEmpty(ModList))
			ModList = PM305;
		else
			ModList = ModList + "","" + PM305;
	}

	if(!string.IsNullOrEmpty(PM306))
	{
		if(string.IsNullOrEmpty(ModList))
			ModList = PM306;
		else
			ModList = ModList + "","" + PM306;
	}

	return ModList;
}

public string SubServiceFromDate(string DateTimeQualifier , string ServiceDate)
{
	string ServiceFromDate = string.Empty;	
	if (DateTimeQualifier.Equals(""RD8""))
	{		
     		int intlen;
		int intsubPot;
		intsubPot = ServiceDate.IndexOf(""-"");
		intlen = ServiceDate.Length - 1;
		intlen = intlen - intsubPot;
		ServiceFromDate = ServiceDate.Substring(0, intsubPot);	
	}
                 if (DateTimeQualifier.Equals(""D8""))
                  {
                   ServiceFromDate = ServiceDate;
                   }

	return ServiceFromDate;
}

public string SubServiceToDate(string DateTimeQualifier ,string ServiceDate)
{	
	string ServiceToDate = string.Empty;		            
	if (DateTimeQualifier.Equals(""RD8""))
	{		
		int intnext;
		int intPosition;
		intPosition = ServiceDate.IndexOf(""-"");
		intnext = ServiceDate.Length - 1;
		intnext = intnext  - intPosition;
		ServiceToDate= ServiceDate.Substring(intPosition + 1, intnext);
	}
                  if (DateTimeQualifier.Equals(""D8""))
                  {
                   ServiceToDate = ServiceDate;
                   }
	return ServiceToDate;
}

public string LocationCode(string SVCPlaceofServiceCode,  string CLMPlaceofServiceCode, int bSVDExistence)
{
	if(bSVDExistence==1)
	{
		return SVCPlaceofServiceCode;
	}
	else
	{
		return CLMPlaceofServiceCode;
	}
}


 public static string DiagnosisPointers(string C00401, string C00402, string C00403, string C00404)
        {
            string DPointers = string.Empty;

            if (!string.IsNullOrEmpty(C00401))
            {
                if (C00401 == ""10"")
                    DPointers = ""A"";
                else if (C00401 == ""11"")
                    DPointers = ""B"";
                else if (C00401 == ""12"")
                    DPointers = ""C"";
                else
                DPointers = C00401;
            }

            if (!string.IsNullOrEmpty(C00402))
            {
                if (string.IsNullOrEmpty(DPointers))
                    DPointers = C00402;
                else if (C00402 == ""10"")
                    DPointers = DPointers + ""A"";
                else if (C00402 == ""11"")
                    DPointers = DPointers + ""B"";
                else if (C00402 == ""12"")
                    DPointers = DPointers + ""C"";
                else
                    DPointers = DPointers + C00402;
            }

            if (!string.IsNullOrEmpty(C00403))
            {
                if (string.IsNullOrEmpty(DPointers))
                    DPointers = C00403;
                else if (C00403 == ""10"")
                    DPointers = DPointers + ""A"";
                else if (C00403 == ""11"")
                    DPointers = DPointers + ""B"";
                else if (C00403 == ""12"")
                    DPointers = DPointers + ""C"";
                else
                    DPointers = DPointers + C00403;
            }

            if (!string.IsNullOrEmpty(C00404))
            {
                if (string.IsNullOrEmpty(DPointers))
                    DPointers = C00404;
                else if (C00404 == ""10"")
                    DPointers = DPointers + ""A"";
                else if (C00404 == ""11"")
                    DPointers = DPointers + ""B"";
                else if (C00404 == ""12"")
                    DPointers = DPointers + ""C"";
                else
                    DPointers = DPointers + C00404;
            }

            return DPointers;
        }

public string DiagPatCodesList(string D1qual,string C22021,string D2qual, string C22022,string D3qual, string C22023,string D4qual, string C22024,string D5qual, string C22025,
string D6qual, string C22026,string D7qual, string C22027,string D8qual, string C22028,string D9qual, string C22029,string D10qual, string C220210,
string D11qual, string C220211,string D12qual, string C220212, string DPointers)
        {
            string DiagnosticCodesList = string.Empty;
            bool eCodeChk;
            bool qualChk;

if (!String.IsNullOrEmpty(D1qual) && String.IsNullOrEmpty(C22021))
        {
            C22021 = "" "";
        }

        if (!String.IsNullOrEmpty(D2qual) && String.IsNullOrEmpty(C22022))
        {
            C22022 = "" "";
        }
        if (!String.IsNullOrEmpty(D3qual) && String.IsNullOrEmpty(C22023))
        {
            C22023 = "" "";
        }
        if (!String.IsNullOrEmpty(D4qual) && String.IsNullOrEmpty(C22024))
        {
            C22024 = "" "";
        }
        if (!String.IsNullOrEmpty(D5qual) && String.IsNullOrEmpty(C22025))
        {
            C22025 = "" "";
        }
        if (!String.IsNullOrEmpty(D6qual) && String.IsNullOrEmpty(C22026))
        {
            C22026 = "" "";
        }
        if (!String.IsNullOrEmpty(D7qual) && String.IsNullOrEmpty(C22027))
        {
            C22027 = "" "";
        }
        if (!String.IsNullOrEmpty(D8qual) && String.IsNullOrEmpty(C22028))
        {
            C22028 = "" "";
        }
        if (!String.IsNullOrEmpty(D9qual) && String.IsNullOrEmpty(C22029))
        {
            C22029 = "" "";
        }
        if (!String.IsNullOrEmpty(D10qual) && String.IsNullOrEmpty(C220210))
        {
            C220210 = "" "";
        }
        if (!String.IsNullOrEmpty(D11qual) && String.IsNullOrEmpty(C220211))
        {
            C220211 = "" "";
        }
        if (!String.IsNullOrEmpty(D12qual) && String.IsNullOrEmpty(C220212))
        {
            C220212 = "" "";
        }

            //C22021
            eCodeChk = C22021.StartsWith(""E"");
            qualChk = D1qual.StartsWith(""B"");

            if (C22021.Length.Equals(7))
            {
                C22021 = C22021.Insert(C22021.Length - 4, ""."");
            }
            else if (C22021.Length.Equals(6))
            {
                C22021 = C22021.Insert(C22021.Length - 3, ""."");
            }
            
            else if (C22021.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22021 = C22021.Insert(C22021.Length - 1, ""."");
                else
                    C22021 = C22021.Insert(C22021.Length - 2, ""."");
              }
              else
                C22021 = C22021.Insert(3, ""."");
            }
            else if (C22021.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D1qual.StartsWith(""A"")))
                    C22021 = C22021.Insert(C22021.Length - 1, ""."");
            }
	    else
	       C22021 = C22021;


            //C22022
            eCodeChk = C22022.StartsWith(""E"");
            qualChk = D2qual.StartsWith(""B"");

            if (C22022.Length.Equals(7))
            {
                C22022 = C22022.Insert(C22022.Length - 4, ""."");
            }
            else if (C22022.Length.Equals(6))
            {
                C22022 = C22022.Insert(C22022.Length - 3, ""."");
            }
            else if (C22022.Length.Equals(5))
            {
              if(qualChk)
              {
                if (eCodeChk)
                    C22022 = C22022.Insert(C22022.Length - 1, ""."");
                else
                    C22022 = C22022.Insert(C22022.Length - 2, ""."");
              }
              else
                C22022 = C22022.Insert(3, ""."");
            }
            else if (C22022.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D2qual.StartsWith(""A"")))
                    C22022 = C22022.Insert(C22022.Length - 1, ""."");
            }
	     else
	       C22022 = C22022;


            //C22023
            eCodeChk = C22023.StartsWith(""E"");
            qualChk = D3qual.StartsWith(""B"");

            if (C22023.Length.Equals(7))
            {
                C22023 = C22023.Insert(C22023.Length - 4, ""."");
            }
            else if (C22023.Length.Equals(6))
            {
                C22023 = C22023.Insert(C22023.Length - 3, ""."");
            }
            else if (C22023.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22023 = C22023.Insert(C22023.Length - 1, ""."");
                else
                    C22023 = C22023.Insert(C22023.Length - 2, ""."");
              }
              else
                C22023 = C22023.Insert(3, ""."");
            }
            else if (C22023.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D3qual.StartsWith(""A"")))
                    C22023 = C22023.Insert(C22023.Length - 1, ""."");
            }
	    else
	       C22023 = C22023;


            //C22024
            eCodeChk = C22024.StartsWith(""E"");
            qualChk = D4qual.StartsWith(""B"");

            if (C22024.Length.Equals(7))
            {
                C22024 = C22024.Insert(C22024.Length - 4, ""."");
            }
            else if (C22024.Length.Equals(6))
            {
                C22024 = C22024.Insert(C22024.Length - 3, ""."");
            }
            else if (C22024.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22024 = C22024.Insert(C22024.Length - 1, ""."");
                else
                    C22024 = C22024.Insert(C22024.Length - 2, ""."");
              }
              else
                C22024 = C22024.Insert(3, ""."");
            }
            else if (C22024.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D4qual.StartsWith(""A"")))
                    C22024 = C22024.Insert(C22024.Length - 1, ""."");
            }
	    else
	       C22024 = C22024;


            //C22025
            eCodeChk = C22025.StartsWith(""E"");
            qualChk = D5qual.StartsWith(""B"");

            if (C22025.Length.Equals(7))
            {
                C22025 = C22025.Insert(C22025.Length - 4, ""."");
            }
            else if (C22025.Length.Equals(6))
            {
                C22025 = C22025.Insert(C22025.Length - 3, ""."");
            }
            else if (C22025.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22025 = C22025.Insert(C22025.Length - 1, ""."");
                else
                    C22025 = C22025.Insert(C22025.Length - 2, ""."");
              }
              else
                C22025 = C22025.Insert(3, ""."");
            }
            else if (C22025.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D5qual.StartsWith(""A"")))
                    C22025 = C22025.Insert(C22025.Length - 1, ""."");
            }
	    else
	       C22025 = C22025;


            //C22026
            eCodeChk = C22026.StartsWith(""E"");
            qualChk = D6qual.StartsWith(""B"");

            if (C22026.Length.Equals(7))
            {
                C22026 = C22026.Insert(C22026.Length - 4, ""."");
            }
            else if (C22026.Length.Equals(6))
            {
                C22026 = C22026.Insert(C22026.Length - 3, ""."");
            }
            else if (C22026.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22026 = C22026.Insert(C22026.Length - 1, ""."");
                else
                    C22026 = C22026.Insert(C22026.Length - 2, ""."");
              }
              else
                C22026 = C22026.Insert(3, ""."");
            }
            else if (C22026.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D6qual.StartsWith(""A"")))
                    C22026 = C22026.Insert(C22026.Length - 1, ""."");
            }
	    else
	       C22026 = C22026;

            //C22027
            eCodeChk = C22027.StartsWith(""E"");
            qualChk = D7qual.StartsWith(""B"");

            if (C22027.Length.Equals(7))
            {
                C22027 = C22027.Insert(C22027.Length - 4, ""."");
            }
            else if (C22027.Length.Equals(6))
            {
                C22027 = C22027.Insert(C22027.Length - 3, ""."");
            }
            else if (C22027.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22027 = C22027.Insert(C22027.Length - 1, ""."");
                else
                    C22027 = C22027.Insert(C22027.Length - 2, ""."");
              }
              else
                C22027 = C22027.Insert(3, ""."");
            }
            else if (C22027.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D7qual.StartsWith(""A"")))
                    C22027 = C22027.Insert(C22027.Length - 1, ""."");
            }
	    else
	       C22027 = C22027;

            //C22028
            eCodeChk = C22028.StartsWith(""E"");
            qualChk = D8qual.StartsWith(""B"");

            if (C22028.Length.Equals(7))
            {
                C22028 = C22028.Insert(C22028.Length - 4, ""."");
            }
            else if (C22028.Length.Equals(6))
            {
                C22028 = C22028.Insert(C22028.Length - 3, ""."");
            }
            else if (C22028.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22028 = C22028.Insert(C22028.Length - 1, ""."");
                else
                    C22028 = C22028.Insert(C22028.Length - 2, ""."");
              }
              else
                C22028 = C22028.Insert(3, ""."");
            }
            else if (C22028.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D8qual.StartsWith(""A"")))
                    C22028 = C22028.Insert(C22028.Length - 1, ""."");
            }
	    else
	       C22028 = C22028;


            //C22029
            eCodeChk = C22029.StartsWith(""E"");
            qualChk = D9qual.StartsWith(""B"");

            if (C22029.Length.Equals(7))
            {
                C22029 = C22029.Insert(C22029.Length - 4, ""."");
            }
            else if (C22029.Length.Equals(6))
            {
                C22029 = C22029.Insert(C22029.Length - 3, ""."");
            }
            else if (C22029.Length.Equals(5))
            {
             if(qualChk)
              {
                if (eCodeChk)
                    C22029 = C22029.Insert(C22029.Length - 1, ""."");
                else
                    C22029 = C22029.Insert(C22029.Length - 2, ""."");
              }
              else
                C22029 = C22029.Insert(3, ""."");
            }
            else if (C22029.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D9qual.StartsWith(""A"")))
                    C22029 = C22029.Insert(C22029.Length - 1, ""."");
            }
	    else
	       C22029 = C22029;

            //C220210
            eCodeChk = C220210.StartsWith(""E"");
            qualChk = D10qual.StartsWith(""B"");

            if (C220210.Length.Equals(7))
            {
                C220210 = C220210.Insert(C220210.Length - 4, ""."");
            }
            else if (C220210.Length.Equals(6))
            {
                C220210 = C220210.Insert(C220210.Length - 3, ""."");
            }
            else if (C220210.Length.Equals(5))
            {
            if(qualChk)
              {
                if (eCodeChk)
                    C220210 = C220210.Insert(C220210.Length - 1, ""."");
                else
                    C220210 = C220210.Insert(C220210.Length - 2, ""."");
              }
              else
                C220210 = C220210.Insert(3, ""."");
            }
            else if (C220210.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D10qual.StartsWith(""A"")))
                    C220210 = C220210.Insert(C220210.Length - 1, ""."");
            }
	    else
	       C220210 = C220210;

            //C220211
            eCodeChk = C220211.StartsWith(""E"");
            qualChk = D11qual.StartsWith(""B"");

            if (C220211.Length.Equals(7))
            {
                C220211 = C220211.Insert(C220211.Length - 4, ""."");
            }
            else if (C220211.Length.Equals(6))
            {
                C220211 = C220211.Insert(C220211.Length - 3, ""."");
            }
            else if (C220211.Length.Equals(5))
            {
            if(qualChk)
              {
                if (eCodeChk)
                    C220211 = C220211.Insert(C220211.Length - 1, ""."");
                else
                    C220211 = C220211.Insert(C220211.Length - 2, ""."");
              }
              else
                C220211 = C220211.Insert(3, ""."");
            }
            else if (C220211.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D11qual.StartsWith(""A"")))
                    C220211 = C220211.Insert(C220211.Length - 1, ""."");
            }
	    else
	       C220211 = C220211;

            //C220212
            eCodeChk = C220212.StartsWith(""E"");
            qualChk = D12qual.StartsWith(""B"");

            if (C220212.Length.Equals(7))
            {
                C220212 = C220212.Insert(C220212.Length - 4, ""."");
            }
            else if (C220212.Length.Equals(6))
            {
                C220212 = C220212.Insert(C220212.Length - 3, ""."");
            }
            else if (C220212.Length.Equals(5))
            {
            if(qualChk)
              {
                if (eCodeChk)
                    C220212 = C220212.Insert(C220212.Length - 1, ""."");
                else
                    C220212 = C220212.Insert(C220212.Length - 2, ""."");
              }
              else
                C220212 = C220212.Insert(3, ""."");
            }
            else if (C220212.Length.Equals(4))
            {
                if (eCodeChk == false || (eCodeChk == true && D12qual.StartsWith(""A"")))
                    C220212 = C220212.Insert(C220212.Length - 1, ""."");
            }
	    else
	       C220212 = C220212;


            //Get the list with pointers
                   char[] AllPointers = DPointers.ToCharArray();
	             
	              int pointercount = AllPointers.Length;
	  
	              for (int i = 0; i < pointercount; i++)
	              { 
	              
	                if (AllPointers.GetValue(i).Equals('1'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22021;
	                      else if (!string.IsNullOrEmpty(C22021))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22021;
	                          
	                  }
	                  else if (AllPointers.GetValue(i).Equals('2'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22022;
	                      else if (!string.IsNullOrEmpty(C22022))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22022;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('3'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22023;
	                      else if (!string.IsNullOrEmpty(C22023))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22023;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('4'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22024;
	                      else if (!string.IsNullOrEmpty(C22024))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22024;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('5'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22025;
	                      else if (!string.IsNullOrEmpty(C22025))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22025;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('6'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22026;
	                      else if (!string.IsNullOrEmpty(C22026))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22026;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('7'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22027;
	                      else if (!string.IsNullOrEmpty(C22027))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22027;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('8'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22028;
	                      else if (!string.IsNullOrEmpty(C22028))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22028;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('9'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C22029;
	                      else if (!string.IsNullOrEmpty(C22029))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C22029;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('A'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C220210;
	                      else if (!string.IsNullOrEmpty(C220210))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C220210;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('B'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C220211;
	                      else if (!string.IsNullOrEmpty(C220211))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C220211;
	                  }
	                  else if (AllPointers.GetValue(i).Equals('C'))
	                  {
	                      if (string.IsNullOrEmpty(DiagnosticCodesList))
	                          DiagnosticCodesList = C220212;
	                      else if (!string.IsNullOrEmpty(C220212))
	                          DiagnosticCodesList = DiagnosticCodesList + "","" + C220212;
	                  }
	  
	              }
	  
            return DiagnosticCodesList;
        }

public int bHaveData(string bExist, int nSize)
{
   if(System.Convert.ToBoolean(bExist) && nSize>0)
           return 1;
   else
            return 0;
}

public string StringLowerCase(string str)
{
	if (str == null)
	{
		return """";
	}
	return str.ToLower(System.Globalization.CultureInfo.InvariantCulture);
}


public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7, string param8, string param9, string param10, string param11)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 + param10 + param11;
}


public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7;
}


public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7, string param8, string param9, string param10, string param11, string param12, string param13, string param14, string param15)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 + param10 + param11 + param12 + param13 + param14 + param15;
}


public string StringConcat(string param0, string param1)
{
   return param0 + param1;
}


public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6;
}


public string AutoAccident(string AA12401, string AA22401, string AA32401, string State_2401)
        {
            string StateAA = string.Empty;

            if (AA12401 == ""AA"")
            {
                StateAA = State_2401;
            }
            else if (AA22401 == ""AA"")
            {
                StateAA = State_2401;
            }
            else if (AA32401 == ""AA"")
            {
                StateAA = State_2401;
            }

            return StateAA; 
        }

public string RemoveLastChar(string param1)
{
    return (param1.Substring(0, param1.Length == 0 ? 0 : param1.Length - 1));
}

public string InitCumulativeConcat(int index)
{
	if (index >= 0)
	{
		if (index >= myCumulativeConcatArray.Count)
		{
			int i = myCumulativeConcatArray.Count;
			for (; i<=index; i++)
			{
				myCumulativeConcatArray.Add("""");
			}
		}
		else
		{
			myCumulativeConcatArray[index] = """";
		}
	}
	return """";
}

public System.Collections.ArrayList myCumulativeConcatArray = new System.Collections.ArrayList();

public string AddToCumulativeConcat(int index, string val, string notused)
{
	if (index < 0 || index >= myCumulativeConcatArray.Count)
	{
		return """";
	}
	myCumulativeConcatArray[index] = (string)(myCumulativeConcatArray[index]) + val;
	return myCumulativeConcatArray[index].ToString();
}

public string GetCumulativeConcat(int index)
{
	if (index < 0 || index >= myCumulativeConcatArray.Count)
	{
		return """";
	}
	return myCumulativeConcatArray[index].ToString();
}

public string OtherPayerSecIDList(string REF_01, string REF_02)
        {
            string SecIDList = string.Empty;
                       
            if (!string.IsNullOrEmpty(REF_01))
                SecIDList = REF_01;

            if (!string.IsNullOrEmpty(REF_02))
            {
                if (!string.IsNullOrEmpty(SecIDList))
                    SecIDList = SecIDList + "":"" + REF_02;
                else
                    SecIDList = REF_02;
            }

             return SecIDList + "","";        
	               
        }

public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7, string param8, string param9, string param10, string param11, string param12, string param13, string param14, string param15, string param16, string param17, string param18, string param19, string param20, string param21, string param22)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 + param10 + param11 + param12 + param13 + param14 + param15 + param16 + param17 + param18 + param19 + param20 + param21 + param22;
}


public string StringConcat(string param0, string param1, string param2)
{
   return param0 + param1 + param2;
}


public string StringRight(string str, string count)
{
	string retval = """";
	double d = 0;
	if (str != null && IsNumeric(count, ref d))
	{
		int i = (int) d;
		if (i > 0)
		{
			if (i <= str.Length)
			{
				retval = str.Substring(str.Length-i);
			}
			else
			{
				retval = str;
			}
		}
	}
	return retval;
}


public string modifierDentalSub(string pDSM1, string pDSM2,string pDSM3,string pDSM4)
{
		string pCompleteDSPoint = string.Empty;
		pCompleteDSPoint = """";
		if (pDSM1 != """")
		{
			pCompleteDSPoint = pDSM1;
		 }            
	 	 if (pDSM2 != """")
		 {
		          if (pCompleteDSPoint.Equals(""""))
		         {
			pCompleteDSPoint = pDSM2;
		         }    
		        else 
		        {
		             pCompleteDSPoint = pCompleteDSPoint + "","" + pDSM2;
         		        }
		}    

		if (pDSM3 != """") 
	               {
		    if (pCompleteDSPoint.Equals(""""))
		   {
			pCompleteDSPoint = pDSM3;
		    }    
		    else
	     	    {
			pCompleteDSPoint = pCompleteDSPoint + "","" + pDSM3;
	 	      }            
		}
		if (pDSM4 != """")
		{
		if (pCompleteDSPoint.Equals(""""))
		{            
			pCompleteDSPoint = pDSM4;
		} 
		else
		{
		pCompleteDSPoint = pCompleteDSPoint + "","" + pDSM4;
	     }
         }
         return pCompleteDSPoint;
}

public bool IsNumeric(string val)
{
	if (val == null)
	{
		return false;
	}
	double d = 0;
	return Double.TryParse(val, System.Globalization.NumberStyles.AllowThousands | System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out d);
}

public bool IsNumeric(string val, ref double d)
{
	if (val == null)
	{
		return false;
	}
	return Double.TryParse(val, System.Globalization.NumberStyles.AllowThousands | System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out d);
}


]]></msxsl:script>
</xsl:stylesheet>";
        
        private const int _useXSLTransform = 0;
        
        private const string _strArgList = @"<ExtensionObjects />";
        
        private const string _strSrcSchemasList0 = @"Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P";
        
        private const global::Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P _srcSchemaTypeReference0 = null;
        
        private const string _strTrgSchemasList0 = @"Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema";
        
        private const global::Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema _trgSchemaTypeReference0 = null;
        
        public override string XmlContent {
            get {
                return _strMap;
            }
        }
        
        public override int UseXSLTransform {
            get {
                return _useXSLTransform;
            }
        }
        
        public override string XsltArgumentListContent {
            get {
                return _strArgList;
            }
        }
        
        public override string[] SourceSchemas {
            get {
                string[] _SrcSchemas = new string [1];
                _SrcSchemas[0] = @"Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P";
                return _SrcSchemas;
            }
        }
        
        public override string[] TargetSchemas {
            get {
                string[] _TrgSchemas = new string [1];
                _TrgSchemas[0] = @"Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema";
                return _TrgSchemas;
            }
        }
    }
}
