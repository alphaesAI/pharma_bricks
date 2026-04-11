namespace Idap837SchemaAndMap {
    
    
    [Microsoft.XLANGs.BaseTypes.SchemaReference(@"Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P", typeof(global::Integration.BIZ.Core.X12Schemas.Multiple837P.X12_00501_837_P))]
    [Microsoft.XLANGs.BaseTypes.SchemaReference(@"Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema", typeof(global::Integration.BIZ.CLMIB.PROF.Schemas.RegularProfClaimSchema))]
    public sealed class RegularProfClaimSubscriberMap : global::Microsoft.XLANGs.BaseTypes.TransformBase {
        
        private const string _strMap = @"<?xml version=""1.0"" encoding=""UTF-16""?>
<xsl:stylesheet xmlns:xsl=""http://www.w3.org/1999/XSL/Transform"" xmlns:msxsl=""urn:schemas-microsoft-com:xslt"" xmlns:var=""http://schemas.microsoft.com/BizTalk/2003/var"" exclude-result-prefixes=""msxsl var s0 s1 s2 userCSharp"" version=""1.0"" xmlns:s0=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent"" xmlns:s2=""http://schemas.microsoft.com/BizTalk/2003/aggschema"" xmlns:s1=""http://schemas.microsoft.com/BizTalk/EDI/X12/2006"" xmlns:ns0=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfessionalClaim"" xmlns:userCSharp=""http://schemas.microsoft.com/BizTalk/2003/userCSharp"">
  <xsl:output omit-xml-declaration=""yes"" method=""xml"" version=""1.0"" />
  <xsl:template match=""/"">
    <xsl:apply-templates select=""/s2:Root"" />
  </xsl:template>
  <xsl:template match=""/s2:Root"">
    <xsl:variable name=""var:v2"" select=""count(/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2400_Loop/s1:LX_ServiceLineNumber/LX01_AssignedNumber)"" />
    <xsl:variable name=""var:v9"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text())"" />
    <xsl:variable name=""var:v11"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_MedicalRecordNumber))"" />
    <xsl:variable name=""var:v13"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text()) , &quot;EI&quot;)"" />
    <xsl:variable name=""var:v14"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text())"" />
    <xsl:variable name=""var:v16"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification/REF01_ReferenceIdentificationQualifier/text()) , &quot;G2&quot;)"" />
    <xsl:variable name=""var:v18"" select=""userCSharp:StringUpperCase(&quot;   &quot;)"" />
    <xsl:variable name=""var:v19"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM108_IdentificationCodeQualifier/text()) , &quot;XV&quot;)"" />
    <xsl:variable name=""var:v21"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber))"" />
    <xsl:variable name=""var:v23"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text())"" />
    <xsl:variable name=""var:v26"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate))"" />
    <xsl:variable name=""var:v32"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress))"" />
    <xsl:variable name=""var:v33"" select=""userCSharp:StringSize(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N301_PatientAddressLine/text()))"" />
    <xsl:variable name=""var:v35"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N301_PatientAddressLine/text())"" />
    <xsl:variable name=""var:v37"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress)"" />
    <xsl:variable name=""var:v38"" select=""userCSharp:LogicalExistence($var:v37)"" />
    <xsl:variable name=""var:v39"" select=""userCSharp:StringSize($var:v35)"" />
    <xsl:variable name=""var:v42"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode))"" />
    <xsl:variable name=""var:v43"" select=""userCSharp:StringSize(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N401_PatientCityName/text()))"" />
    <xsl:variable name=""var:v45"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N401_PatientCityName/text())"" />
    <xsl:variable name=""var:v47"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode)"" />
    <xsl:variable name=""var:v48"" select=""userCSharp:LogicalExistence($var:v47)"" />
    <xsl:variable name=""var:v49"" select=""userCSharp:StringSize($var:v45)"" />
    <xsl:variable name=""var:v55"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text())"" />
    <xsl:variable name=""var:v57"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation))"" />
    <xsl:variable name=""var:v59"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation)"" />
    <xsl:variable name=""var:v60"" select=""userCSharp:LogicalExistence($var:v59)"" />
    <xsl:variable name=""var:v61"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02401_RelatedCausesCode/text())"" />
    <xsl:variable name=""var:v62"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02402_RelatedCausesCode/text())"" />
    <xsl:variable name=""var:v63"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02403_Related_CausesCode/text())"" />
    <xsl:variable name=""var:v66"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom))"" />
    <xsl:variable name=""var:v67"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod))"" />
    <xsl:variable name=""var:v69"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates))"" />
    <xsl:variable name=""var:v71"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates)"" />
    <xsl:variable name=""var:v72"" select=""userCSharp:LogicalExistence($var:v71)"" />
    <xsl:variable name=""var:v73"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP01_DateTimeQualifier/text())"" />
    <xsl:variable name=""var:v74"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP02_DateTimePeriodFormatQualifier/text())"" />
    <xsl:variable name=""var:v75"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP03_DisabilityFromDate/text())"" />
    <xsl:variable name=""var:v77"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Admission))"" />
    <xsl:variable name=""var:v79"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Discharge))"" />
    <xsl:variable name=""var:v81"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM10_PatientSignatureSourceCode))"" />
    <xsl:variable name=""var:v83"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation/C02201_DiagnosisTypeCode/text())"" />
    <xsl:variable name=""var:v86"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_InitialTreatmentDate))"" />
    <xsl:variable name=""var:v87"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate))"" />
    <xsl:variable name=""var:v88"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation))"" />
    <xsl:variable name=""var:v89"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident))"" />
    <xsl:variable name=""var:v90"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate))"" />
    <xsl:variable name=""var:v91"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate))"" />
    <xsl:variable name=""var:v92"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AssumedandRelinquishedCareDates_Loop))"" />
    <xsl:variable name=""var:v93"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_PropertyandCasualtyDateofFirstContact))"" />
    <xsl:variable name=""var:v95"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_InitialTreatmentDate)"" />
    <xsl:variable name=""var:v96"" select=""userCSharp:LogicalExistence($var:v95)"" />
    <xsl:variable name=""var:v97"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate)"" />
    <xsl:variable name=""var:v98"" select=""userCSharp:LogicalExistence($var:v97)"" />
    <xsl:variable name=""var:v99"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation)"" />
    <xsl:variable name=""var:v100"" select=""userCSharp:LogicalExistence($var:v99)"" />
    <xsl:variable name=""var:v101"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident)"" />
    <xsl:variable name=""var:v102"" select=""userCSharp:LogicalExistence($var:v101)"" />
    <xsl:variable name=""var:v103"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate)"" />
    <xsl:variable name=""var:v104"" select=""userCSharp:LogicalExistence($var:v103)"" />
    <xsl:variable name=""var:v105"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate)"" />
    <xsl:variable name=""var:v106"" select=""userCSharp:LogicalExistence($var:v105)"" />
    <xsl:variable name=""var:v107"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AssumedandRelinquishedCareDates_Loop)"" />
    <xsl:variable name=""var:v108"" select=""userCSharp:LogicalExistence($var:v107)"" />
    <xsl:variable name=""var:v109"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_PropertyandCasualtyDateofFirstContact)"" />
    <xsl:variable name=""var:v110"" select=""userCSharp:LogicalExistence($var:v109)"" />
    <xsl:variable name=""var:v112"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom)"" />
    <xsl:variable name=""var:v113"" select=""userCSharp:LogicalExistence($var:v112)"" />
    <xsl:variable name=""var:v114"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod)"" />
    <xsl:variable name=""var:v115"" select=""userCSharp:LogicalExistence($var:v114)"" />
    <xsl:variable name=""var:v117"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_DemonstrationProjectIdentifier))"" />
    <xsl:variable name=""var:v119"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_DemonstrationProjectIdentifier)"" />
    <xsl:variable name=""var:v120"" select=""userCSharp:LogicalExistence($var:v119)"" />
    <xsl:variable name=""var:v150"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV02_ReferenceIdentificationQualifier))"" />
    <xsl:variable name=""var:v152"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV03_ProviderTaxonomyCode))"" />
    <xsl:variable name=""var:v154"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N3_BillingProviderAddress/N302_BillingProviderAddressLine))"" />
    <xsl:variable name=""var:v156"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification))"" />
    <xsl:variable name=""var:v168"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM102_EntityTypeQualifier))"" />
    <xsl:variable name=""var:v170"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM103_Pay_toLastorOrganizationalName))"" />
    <xsl:variable name=""var:v172"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM104_NameFirst))"" />
    <xsl:variable name=""var:v174"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM108_IdentificationCodeQualifier))"" />
    <xsl:variable name=""var:v176"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode))"" />
    <xsl:variable name=""var:v178"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode)"" />
    <xsl:variable name=""var:v179"" select=""userCSharp:LogicalExistence($var:v178)"" />
    <xsl:variable name=""var:v180"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode/text())"" />
    <xsl:variable name=""var:v182"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:PRV_RenderingProviderSpecialtyInformation))"" />
    <xsl:variable name=""var:v184"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName))"" />
    <xsl:variable name=""var:v186"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName)"" />
    <xsl:variable name=""var:v187"" select=""userCSharp:LogicalExistence($var:v186)"" />
    <xsl:variable name=""var:v189"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM104_RenderingProviderFirstName))"" />
    <xsl:variable name=""var:v191"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM108_IdentificationCodeQualifier))"" />
    <xsl:variable name=""var:v193"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM109_RenderingProviderIdentifier))"" />
    <xsl:variable name=""var:v195"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM109_RenderingProviderIdentifier)"" />
    <xsl:variable name=""var:v196"" select=""userCSharp:LogicalExistence($var:v195)"" />
    <xsl:variable name=""var:v197"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM109_RenderingProviderIdentifier/text())"" />
    <xsl:variable name=""var:v199"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v200"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
    <xsl:variable name=""var:v201"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[1]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v202"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
    <xsl:variable name=""var:v203"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v204"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[2]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v205"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v206"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[3]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v207"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[4]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v208"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification[4]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v209"" select=""userCSharp:StringConcat(string($var:v199) , string($var:v200) , string($var:v201) , string($var:v202) , string($var:v203) , string($var:v200) , string($var:v204) , string($var:v202) , string($var:v205) , string($var:v200) , string($var:v206) , string($var:v202) , string($var:v207) , string($var:v200) , string($var:v208) , string($var:v202))"" />
    <xsl:variable name=""var:v239"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v240"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[1]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v241"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v242"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[2]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v243"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v244"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[3]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v245"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[4]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v246"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:REF_SupervisingProviderSecondaryIdentification[4]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v247"" select=""userCSharp:StringConcat(string($var:v239) , string($var:v200) , string($var:v240) , string($var:v202) , string($var:v241) , string($var:v200) , string($var:v242) , string($var:v202) , string($var:v243) , string($var:v200) , string($var:v244) , string($var:v202) , string($var:v245) , string($var:v200) , string($var:v246) , string($var:v202))"" />
    <xsl:variable name=""var:v248"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM108_IdentificationCodeQualifier))"" />
    <xsl:variable name=""var:v250"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM109_LaboratoryorFacilityPrimaryIdentifier))"" />
    <xsl:variable name=""var:v252"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM109_LaboratoryorFacilityPrimaryIdentifier)"" />
    <xsl:variable name=""var:v253"" select=""userCSharp:LogicalExistence($var:v252)"" />
    <xsl:variable name=""var:v254"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM109_LaboratoryorFacilityPrimaryIdentifier/text())"" />
    <xsl:variable name=""var:v256"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N3_ServiceFacilityLocationAddress/N302_LaboratoryorFacilityAddressLine))"" />
    <xsl:variable name=""var:v258"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N401_LaboratoryorFacilityCityName))"" />
    <xsl:variable name=""var:v260"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N402_LaboratoryorFacilityStateorProvinceCode))"" />
    <xsl:variable name=""var:v262"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N403_LaboratoryorFacilityPostalZoneorZIPCode))"" />
    <xsl:variable name=""var:v264"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v265"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[1]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v266"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v267"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[2]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v268"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v269"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification[3]/REF02_LaboratoryorFacilitySecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v270"" select=""userCSharp:StringConcat(string($var:v264) , string($var:v200) , string($var:v265) , string($var:v202) , string($var:v266) , string($var:v200) , string($var:v267) , string($var:v202) , string($var:v268) , string($var:v200) , string($var:v269) , string($var:v202))"" />
    <xsl:variable name=""var:v271"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v272"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[1]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v273"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v274"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[2]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v275"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v276"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_PayerSecondaryIdentification_Loop/s1:REF_PayerSecondaryIdentification[3]/REF02_PayerSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v277"" select=""userCSharp:StringConcat(string($var:v271) , &quot;:&quot; , string($var:v272) , &quot;,&quot; , string($var:v273) , &quot;:&quot; , string($var:v274) , &quot;,&quot; , string($var:v275) , &quot;:&quot; , string($var:v276) , &quot;,&quot;)"" />
    <xsl:variable name=""var:v278"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v279"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[1]/REF02_BillingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v280"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
    <xsl:variable name=""var:v281"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BB_Loop/s1:REF_SubLoop_4/s1:REF_BillingProviderSecondaryIdentification_Loop/s1:REF_BillingProviderSecondaryIdentification[2]/REF02_BillingProviderSecondaryIdentifier/text()"" />
    <xsl:variable name=""var:v282"" select=""userCSharp:StringConcat(string($var:v278) , &quot;:&quot; , string($var:v279) , &quot;,&quot; , string($var:v280) , &quot;:&quot; , string($var:v281) , &quot;,&quot;)"" />
    <xsl:variable name=""var:v283"" select=""userCSharp:StringConcat(string($var:v277) , string($var:v282))"" />
    <xsl:variable name=""var:v284"" select=""userCSharp:StringConcat(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanSecondaryIdentification/REF01_ReferenceIdentificationQualifier/text()) , string($var:v200) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanSecondaryIdentification/REF02_Pay_toPlanSecondaryIdentifier/text()) , string($var:v202) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF01_ReferenceIdentificationQualifier/text()) , string($var:v200) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF02_Pay_ToPlanTaxIdentificationNumber/text()) , string($var:v202))"" />
    <xsl:variable name=""var:v756"" select=""userCSharp:StringConcat(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_AnesthesiaRelatedProcedure/s1:C022_HealthCareCodeInformation_13/C02201_CodeListQualifierCode/text()) , &quot;:&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_AnesthesiaRelatedProcedure/s1:C022_HealthCareCodeInformation_13/C02202_AnesthesiaRelatedSurgicalProcedure/text()) , &quot;,&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_AnesthesiaRelatedProcedure/s1:C022_HealthCareCodeInformation_14/C02201_CodeListQualifierCode/text()) , &quot;:&quot; , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_AnesthesiaRelatedProcedure/s1:C022_HealthCareCodeInformation_14/C02202_IndustryCode/text()) , &quot;,&quot;)"" />
    <xsl:variable name=""var:v757"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_25/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v758"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_26/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v759"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_27/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v760"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_28/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v761"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_29/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v762"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_30/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v763"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_31/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v764"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_32/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v765"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_33/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v766"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_34/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v767"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_35/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v768"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_36/C02202_ConditionCode/text())"" />
    <xsl:variable name=""var:v789"" select=""userCSharp:LogicalEq(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode/text()) , &quot;P&quot;)"" />
    <xsl:variable name=""var:v790"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount))"" />
    <xsl:variable name=""var:v791"" select=""userCSharp:LogicalEq(string($var:v789) , string($var:v790))"" />
    <xsl:variable name=""var:v793"" select=""string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode/text())"" />
    <xsl:variable name=""var:v794"" select=""userCSharp:LogicalEq($var:v793 , &quot;P&quot;)"" />
    <xsl:variable name=""var:v795"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount))"" />
    <xsl:variable name=""var:v796"" select=""userCSharp:LogicalEq(string($var:v794) , string($var:v795))"" />
    <xsl:variable name=""var:v798"" select=""userCSharp:LogicalEq($var:v793 , &quot;S&quot;)"" />
    <xsl:variable name=""var:v799"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount)"" />
    <xsl:variable name=""var:v800"" select=""userCSharp:LogicalExistence($var:v799)"" />
    <xsl:variable name=""var:v801"" select=""userCSharp:LogicalEq(string($var:v798) , string($var:v800))"" />
    <xsl:variable name=""var:v803"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount)"" />
    <xsl:variable name=""var:v804"" select=""userCSharp:LogicalExistence($var:v803)"" />
    <xsl:variable name=""var:v805"" select=""userCSharp:LogicalEq(string($var:v798) , string($var:v804))"" />
    <xsl:variable name=""var:v807"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number))"" />
    <xsl:variable name=""var:v809"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_EPSDTReferral))"" />
    <xsl:variable name=""var:v811"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_EPSDTReferral)"" />
    <xsl:variable name=""var:v812"" select=""userCSharp:LogicalExistence($var:v811)"" />
    <xsl:variable name=""var:v815"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_MammographyCertificationNumber))"" />
    <xsl:variable name=""var:v817"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:NM1_AmbulanceDrop_offLocation))"" />
    <xsl:variable name=""var:v819"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP01_DateTimeQualifier))"" />
    <xsl:variable name=""var:v821"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP03_LastX_RayDate))"" />
    <xsl:variable name=""var:v823"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation/DTP03_AcuteManifestationDate))"" />
    <xsl:variable name=""var:v825"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom/DTP03_OnsetofCurrentIllnessorInjuryDate))"" />
    <xsl:variable name=""var:v827"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate/DTP03_LastSeenDate))"" />
    <xsl:variable name=""var:v829"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod/DTP03_LastMenstrualPeriodDate))"" />
    <xsl:variable name=""var:v831"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate/DTP03_PrescriptionDate))"" />
    <xsl:variable name=""var:v833"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastWorked/DTP03_LastWorkedDate))"" />
    <xsl:variable name=""var:v835"" select=""userCSharp:LogicalExistence(boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AuthorizedReturntoWork/DTP03_WorkReturnDate))"" />
    <ns0:Integration_Professional_Claims>
      <ns0:CLAIM>
        <xsl:variable name=""var:v1"" select=""userCSharp:ExternalClmID(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text()))"" />
        <ns0:CLAIM_ID>
          <xsl:value-of select=""$var:v1"" />
        </ns0:CLAIM_ID>
        <ns0:RECEIVE_TIME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:BHT_BeginningofHierarchicalTransaction/BHT04_TransactionSetCreationDate/text()"" />
        </ns0:RECEIVE_TIME>
        <ns0:DETAIL_COUNT>
          <xsl:value-of select=""$var:v2"" />
        </ns0:DETAIL_COUNT>
        <xsl:variable name=""var:v3"" select=""userCSharp:strAuthNumber(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_PriorAuthorization/REF02_PriorAuthorizationNumber/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ReferralNumber/REF02_ReferralNumber/text()))"" />
        <ns0:AUTHORIZATION_NUMBER>
          <xsl:value-of select=""$var:v3"" />
        </ns0:AUTHORIZATION_NUMBER>
        <xsl:variable name=""var:v4"" select=""userCSharp:cobstatusprof(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()))"" />
        <ns0:COB_STATUS>
          <xsl:value-of select=""$var:v4"" />
        </ns0:COB_STATUS>
        <ns0:PAID_BY_PRIMARY_PAYER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()"" />
        </ns0:PAID_BY_PRIMARY_PAYER>
        <xsl:variable name=""var:v5"" select=""userCSharp:InitCumulativeMin(0)"" />
        <xsl:for-each select=""/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2400_Loop/s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate"">
          <xsl:variable name=""var:v6"" select=""userCSharp:StringLeft(string(DTP03_ServiceDate/text()) , &quot;8&quot;)"" />
          <xsl:variable name=""var:v7"" select=""userCSharp:AddToCumulativeMin(0,string($var:v6),&quot;1000&quot;)"" />
        </xsl:for-each>
        <xsl:variable name=""var:v8"" select=""userCSharp:GetCumulativeMin(0)"" />
        <ns0:FIRST_SERVICE_DATE>
          <xsl:value-of select=""$var:v8"" />
        </ns0:FIRST_SERVICE_DATE>
        <xsl:variable name=""var:v10"" select=""userCSharp:ExternalClmID($var:v9 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ClaimIdentifierForTransmissionIntermediaries/REF02_ValueAddedNetworkTraceNumber/text()))"" />
        <ns0:EXTERNAL_CLAIM_ID>
          <xsl:value-of select=""$var:v10"" />
        </ns0:EXTERNAL_CLAIM_ID>
        <ns0:PATIENT_CONTROL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text()"" />
        </ns0:PATIENT_CONTROL_NUMBER>
        <xsl:if test=""string($var:v11)='true'"">
          <xsl:variable name=""var:v12"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_MedicalRecordNumber/REF02_MedicalRecordNumber/text()"" />
          <ns0:MEDICAL_RECORD_NUMBER>
            <xsl:value-of select=""$var:v12"" />
          </ns0:MEDICAL_RECORD_NUMBER>
        </xsl:if>
        <xsl:variable name=""var:v15"" select=""userCSharp:PayToProviderIDQual(string($var:v13) , $var:v14)"" />
        <ns0:PAY_TO_PROVIDER_ID_QUAL>
          <xsl:value-of select=""$var:v15"" />
        </ns0:PAY_TO_PROVIDER_ID_QUAL>
        <xsl:if test=""string($var:v16)='true'"">
          <xsl:variable name=""var:v17"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:REF_RenderingProviderSecondaryIdentification/REF01_ReferenceIdentificationQualifier/text()"" />
          <ns0:PROVIDER_ID_QUAL>
            <xsl:value-of select=""$var:v17"" />
          </ns0:PROVIDER_ID_QUAL>
        </xsl:if>
        <ns0:PAID_BY_MEMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:AMT_PatientAmountPaid/AMT02_PatientAmountPaid/text()"" />
        </ns0:PAID_BY_MEMBER>
        <ns0:EOB_NOTE>
          <xsl:text />
        </ns0:EOB_NOTE>
        <ns0:EDI_SUBMITTER_ID>
          <xsl:value-of select=""$var:v18"" />
        </ns0:EDI_SUBMITTER_ID>
        <ns0:EDI_RECEIVER_ID>
          <xsl:value-of select=""$var:v18"" />
        </ns0:EDI_RECEIVER_ID>
        <ns0:EDI_CORRECTION_LIST>
          <xsl:value-of select=""$var:v18"" />
        </ns0:EDI_CORRECTION_LIST>
        <ns0:PAY_TO_PLAN_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM103_Pay_toPlanOrganizationalName/text()"" />
        </ns0:PAY_TO_PLAN_NAME>
        <xsl:if test=""string($var:v19)='true'"">
          <xsl:variable name=""var:v20"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM109_Pay_toPlanPrimaryIdentifier/text()"" />
          <ns0:PAY_TO_PLAN_NPI>
            <xsl:value-of select=""$var:v20"" />
          </ns0:PAY_TO_PLAN_NPI>
        </xsl:if>
        <xsl:if test=""string($var:v21)='true'"">
          <xsl:variable name=""var:v22"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:REF_SubLoop_2/s1:REF_Pay_ToPlanTaxIdentificationNumber/REF02_Pay_ToPlanTaxIdentificationNumber/text()"" />
          <ns0:PAY_TO_PLAN_TAXID>
            <xsl:value-of select=""$var:v22"" />
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
        <ns0:REPRICER_RECVD_DATE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_RepricerReceivedDate/DTP03_RepricerReceivedDate/text()"" />
        </ns0:REPRICER_RECVD_DATE>
        <ns0:PATIENT_LIABILTY_AMT>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_RemainingPatientLiability/AMT02_RemainingPatientLiability/text()"" />
        </ns0:PATIENT_LIABILTY_AMT>
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
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM06_ProviderorSupplierSignatureIndicator/text()"" />
        </ns0:PROVIDER_SIGNATURE_FILE_IND>
        <ns0:MEDICARE_ASSIGNMENT_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM07_AssignmentorPlanParticipationCode/text()"" />
        </ns0:MEDICARE_ASSIGNMENT_CODE>
        <ns0:ASSIGNMENT_BENEFIT_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM08_BenefitsAssignmentCertificationIndicator/text()"" />
        </ns0:ASSIGNMENT_BENEFIT_IND>
        <ns0:RELEASE_INFO_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM09_ReleaseofInformationCode/text()"" />
        </ns0:RELEASE_INFO_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM10_PatientSignatureSourceCode"">
          <ns0:PATIENT_SIGNATURE_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM10_PatientSignatureSourceCode/text()"" />
          </ns0:PATIENT_SIGNATURE_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02404_AutoAccidentStateorProvinceCode"">
          <ns0:AUTO_ACCIDENT_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02404_AutoAccidentStateorProvinceCode/text()"" />
          </ns0:AUTO_ACCIDENT_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM12_SpecialProgramIndicator"">
          <ns0:SPECIAL_PROGRAM_IND>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM12_SpecialProgramIndicator/text()"" />
          </ns0:SPECIAL_PROGRAM_IND>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM16_ProviderAgreementCode"">
          <ns0:PARTICIPATION_AGREEMENT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM16_ProviderAgreementCode/text()"" />
          </ns0:PARTICIPATION_AGREEMENT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM20_DelayReasonCode"">
          <ns0:DELAY_REASON_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM20_DelayReasonCode/text()"" />
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
        <xsl:variable name=""var:v24"" select=""userCSharp:cobindicator($var:v23 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2400_Loop/s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD02_ServiceLinePaidAmount/text()))"" />
        <ns0:COB_INDICATOR>
          <xsl:value-of select=""$var:v24"" />
        </ns0:COB_INDICATOR>
        <ns0:ITS_PPSPA_REQUEST_ID>
          <xsl:text />
        </ns0:ITS_PPSPA_REQUEST_ID>
        <ns0:ITS_CLAIM_TYPE>
          <xsl:text />
        </ns0:ITS_CLAIM_TYPE>
        <ns0:TOTAL_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM02_TotalClaimChargeAmount/text()"" />
        </ns0:TOTAL_CHARGES>
        <xsl:variable name=""var:v25"" select=""userCSharp:PrincipalDiagQual(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation/C02201_DiagnosisTypeCode/text()))"" />
        <ns0:ICD_VERSION_IND>
          <xsl:value-of select=""$var:v25"" />
        </ns0:ICD_VERSION_IND>
        <xsl:variable name=""var:v27"" select=""userCSharp:InitCumulativeMin(1)"" />
        <xsl:for-each select=""/s2:Root/InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2400_Loop/s1:TS837_2430_Loop/s1:DTP_LineCheckorRemittanceDate"">
          <xsl:variable name=""var:v28"" select=""userCSharp:StringLeft(string(DTP03_AdjudicationorPaymentDate/text()) , &quot;8&quot;)"" />
          <xsl:variable name=""var:v29"" select=""userCSharp:AddToCumulativeMin(1,string($var:v28),&quot;1000&quot;)"" />
        </xsl:for-each>
        <xsl:variable name=""var:v30"" select=""userCSharp:GetCumulativeMin(1)"" />
        <xsl:variable name=""var:v31"" select=""userCSharp:ADJREMITDATE(string($var:v26) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate/text()) , string($var:v30))"" />
        <ns0:PRIMARY_PAID_DATE>
          <xsl:value-of select=""$var:v31"" />
        </ns0:PRIMARY_PAID_DATE>
        <xsl:variable name=""var:v34"" select=""userCSharp:nHaveData(string($var:v32) , string($var:v33))"" />
        <xsl:variable name=""var:v36"" select=""userCSharp:PATADDRESS($var:v35 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N301_SubscriberAddressLine/text()) , string($var:v34))"" />
        <ns0:PATIENT_ADD1>
          <xsl:value-of select=""$var:v36"" />
        </ns0:PATIENT_ADD1>
        <xsl:variable name=""var:v40"" select=""userCSharp:nHaveData(string($var:v38) , string($var:v39))"" />
        <xsl:variable name=""var:v41"" select=""userCSharp:PATADDRESSST(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N3_PatientAddress/N302_PatientAddressLine/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N3_SubscriberAddress/N302_SubscriberAddressLine/text()) , string($var:v40))"" />
        <ns0:PATIENT_ADD2>
          <xsl:value-of select=""$var:v41"" />
        </ns0:PATIENT_ADD2>
        <xsl:variable name=""var:v44"" select=""userCSharp:nHaveData(string($var:v42) , string($var:v43))"" />
        <xsl:variable name=""var:v46"" select=""userCSharp:PATCITY($var:v45 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N401_SubscriberCityName/text()) , string($var:v44))"" />
        <ns0:PATIENT_CITY>
          <xsl:value-of select=""$var:v46"" />
        </ns0:PATIENT_CITY>
        <xsl:variable name=""var:v50"" select=""userCSharp:nHaveData(string($var:v48) , string($var:v49))"" />
        <xsl:variable name=""var:v51"" select=""userCSharp:PATSTATE(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N402_PatientStateCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N402_SubscriberStateCode/text()) , string($var:v50))"" />
        <ns0:PATIENT_STATE>
          <xsl:value-of select=""$var:v51"" />
        </ns0:PATIENT_STATE>
        <xsl:variable name=""var:v52"" select=""userCSharp:nHaveData(string($var:v48) , string($var:v49))"" />
        <xsl:variable name=""var:v53"" select=""userCSharp:PATZIP(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2000C_Loop/s1:TS837_2010CA_Loop/s1:N4_PatientCity_State_ZIPCode/N403_PatientPostalZoneorZIPCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:NM1_SubLoop_3/s1:TS837_2010BA_Loop/s1:N4_SubscriberCity_State_ZIPCode/N403_SubscriberPostalZoneorZIPCode/text()) , string($var:v52))"" />
        <ns0:PATIENT_ZIP>
          <xsl:value-of select=""$var:v53"" />
        </ns0:PATIENT_ZIP>
      </ns0:CLAIM>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2300_Loop"">
            <xsl:for-each select=""s1:TS837_2400_Loop"">
              <ns0:CLAIM_DETAIL>
                <xsl:variable name=""var:v54"" select=""userCSharp:ExternalClmID(string(../s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text()) , string(../s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text()))"" />
                <ns0:CLAIM_ID>
                  <xsl:value-of select=""$var:v54"" />
                </ns0:CLAIM_ID>
                <ns0:LINE_NUMBER>
                  <xsl:value-of select=""s1:LX_ServiceLineNumber/LX01_AssignedNumber/text()"" />
                </ns0:LINE_NUMBER>
              </ns0:CLAIM_DETAIL>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
      <ns0:PROF_CLAIM>
        <xsl:variable name=""var:v56"" select=""userCSharp:ExternalClmID($var:v55 , $var:v9)"" />
        <ns0:CLAIM_ID>
          <xsl:value-of select=""$var:v56"" />
        </ns0:CLAIM_ID>
        <xsl:variable name=""var:v58"" select=""userCSharp:conditionEmp(string($var:v57) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02401_RelatedCausesCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02402_RelatedCausesCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02403_Related_CausesCode/text()))"" />
        <ns0:CONDITION_EMPLOYMENT>
          <xsl:value-of select=""$var:v58"" />
        </ns0:CONDITION_EMPLOYMENT>
        <xsl:variable name=""var:v64"" select=""userCSharp:conditionAuto(string($var:v60) , $var:v61 , $var:v62 , $var:v63)"" />
        <ns0:CONDITION_AUTO_ACCIDENT>
          <xsl:value-of select=""$var:v64"" />
        </ns0:CONDITION_AUTO_ACCIDENT>
        <xsl:variable name=""var:v65"" select=""userCSharp:conditionOth(string($var:v60) , $var:v61 , $var:v62 , $var:v63)"" />
        <ns0:CONDITION_OTHER_ACCIDENT>
          <xsl:value-of select=""$var:v65"" />
        </ns0:CONDITION_OTHER_ACCIDENT>
        <ns0:OTHER_INSURANCE_FLAG>
          <xsl:text>N</xsl:text>
        </ns0:OTHER_INSURANCE_FLAG>
        <xsl:variable name=""var:v68"" select=""userCSharp:DTPIllnessseg(string($var:v66) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom/DTP03_OnsetofCurrentIllnessorInjuryDate/text()) , string($var:v67) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod/DTP03_LastMenstrualPeriodDate/text()))"" />
        <ns0:FIRST_SYMPTOM_DATE>
          <xsl:value-of select=""$var:v68"" />
        </ns0:FIRST_SYMPTOM_DATE>
        <ns0:FIRST_SIMILAR_SYMPTOM_DATE>
          <xsl:text />
        </ns0:FIRST_SIMILAR_SYMPTOM_DATE>
        <xsl:variable name=""var:v70"" select=""userCSharp:DisabilityBeginDate(string($var:v69) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP01_DateTimeQualifier/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP02_DateTimePeriodFormatQualifier/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_DisabilityDates/DTP03_DisabilityFromDate/text()))"" />
        <ns0:LOSS_OF_WORK_BEGIN>
          <xsl:value-of select=""$var:v70"" />
        </ns0:LOSS_OF_WORK_BEGIN>
        <xsl:variable name=""var:v76"" select=""userCSharp:DisabilityEndDate(string($var:v72) , $var:v73 , $var:v74 , $var:v75)"" />
        <ns0:LOSS_OF_WORK_END>
          <xsl:value-of select=""$var:v76"" />
        </ns0:LOSS_OF_WORK_END>
        <xsl:if test=""string($var:v77)='true'"">
          <xsl:variable name=""var:v78"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Admission/DTP03_RelatedHospitalizationAdmissionDate/text()"" />
          <ns0:HOSPITALIZATION_BEGIN>
            <xsl:value-of select=""$var:v78"" />
          </ns0:HOSPITALIZATION_BEGIN>
        </xsl:if>
        <xsl:if test=""string($var:v79)='true'"">
          <xsl:variable name=""var:v80"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Discharge/DTP03_RelatedHospitalizationDischargeDate/text()"" />
          <ns0:HOSPITALIZATION_END>
            <xsl:value-of select=""$var:v80"" />
          </ns0:HOSPITALIZATION_END>
        </xsl:if>
        <ns0:RELEASE_INFO_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM09_ReleaseofInformationCode/text()"" />
        </ns0:RELEASE_INFO_CODE>
        <xsl:if test=""string($var:v81)='true'"">
          <xsl:variable name=""var:v82"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM10_PatientSignatureSourceCode/text()"" />
          <ns0:PATIENT_SIGNATURE_CODE>
            <xsl:value-of select=""$var:v82"" />
          </ns0:PATIENT_SIGNATURE_CODE>
        </xsl:if>
        <ns0:PROVIDER_SIGNATURE_FILE_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM06_ProviderorSupplierSignatureIndicator/text()"" />
        </ns0:PROVIDER_SIGNATURE_FILE_IND>
        <ns0:AMBULATORY_PATIENT_GROUP>
          <xsl:text />
        </ns0:AMBULATORY_PATIENT_GROUP>
        <ns0:TOTAL_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/CLM02_TotalClaimChargeAmount/text()"" />
        </ns0:TOTAL_CHARGES>
        <xsl:variable name=""var:v84"" select=""userCSharp:InstDiagCodesList($var:v83 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_2/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_2/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_3/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_3/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_4/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_4/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_5/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_5/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_6/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_6/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_7/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_7/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_8/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_8/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_9/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_9/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_10/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_10/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_11/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_11/C02202_DiagnosisCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_12/C02201_DiagnosisTypeCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_12/C02202_DiagnosisCode/text()))"" />
        <ns0:DIAGNOSIS_CODES_LIST>
          <xsl:value-of select=""$var:v84"" />
        </ns0:DIAGNOSIS_CODES_LIST>
        <ns0:REPRICE_CHARGES>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HCP_ClaimPricing_RepricingInformation/HCP02_RepricedAllowedAmount/text()"" />
        </ns0:REPRICE_CHARGES>
        <xsl:variable name=""var:v85"" select=""userCSharp:SubConditionCodes(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_25/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_26/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_27/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_28/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_29/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_30/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_31/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_32/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_33/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_34/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_35/C02202_ConditionCode/text()) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:HI_SubLoop/s1:HI_ConditionInformation_Loop/s1:HI_ConditionInformation/s1:C022_HealthCareCodeInformation_36/C02202_ConditionCode/text()))"" />
        <ns0:CONDITION_CODES_LIST>
          <xsl:value-of select=""$var:v85"" />
        </ns0:CONDITION_CODES_LIST>
        <ns0:CLAIM_FREQUENCY_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C023_HealthCareServiceLocationInformation/C02303_ClaimFrequencyCode/text()"" />
        </ns0:CLAIM_FREQUENCY_CODE>
        <xsl:variable name=""var:v94"" select=""userCSharp:DTPsegQual(string($var:v86) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_InitialTreatmentDate/DTP01_DateTimeQualifier/text()) , string($var:v87) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate/DTP01_DateTimeQualifier/text()) , string($var:v88) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation/DTP01_DateTimeQualifier/text()) , string($var:v89) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident/DTP01_DateTimeQualifier/text()) , string($var:v90) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP01_DateTimeQualifier/text()) , string($var:v91) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate/DTP01_DateTimeQualifier/text()) , string($var:v92) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AssumedandRelinquishedCareDates_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates/DTP01_DateTimeQualifier/text()) , string($var:v93) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_PropertyandCasualtyDateofFirstContact/DTP01_DateTimeQualifier/text()))"" />
        <ns0:OTHER_DATE_QUAL>
          <xsl:value-of select=""$var:v94"" />
        </ns0:OTHER_DATE_QUAL>
        <xsl:variable name=""var:v111"" select=""userCSharp:DTPseg(string($var:v96) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_InitialTreatmentDate/DTP03_InitialTreatmentDate/text()) , string($var:v98) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate/DTP03_LastSeenDate/text()) , string($var:v100) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation/DTP03_AcuteManifestationDate/text()) , string($var:v102) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident/DTP03_AccidentDate/text()) , string($var:v104) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP03_LastX_RayDate/text()) , string($var:v106) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate/DTP03_PrescriptionDate/text()) , string($var:v108) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AssumedandRelinquishedCareDates_Loop/s1:DTP_Date_AssumedandRelinquishedCareDates/DTP03_AssumedorRelinquishedCareDate/text()) , string($var:v110) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_PropertyandCasualtyDateofFirstContact/DTP03_DateTimePeriod/text()))"" />
        <ns0:OTHER_DATE>
          <xsl:value-of select=""$var:v111"" />
        </ns0:OTHER_DATE>
        <xsl:variable name=""var:v116"" select=""userCSharp:DTPIllnesssegQual(string($var:v113) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom/DTP01_DateTimeQualifier/text()) , string($var:v115) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod/DTP01_DateTimeQualifier/text()))"" />
        <ns0:FIRST_SYMPTOM_DATE_QUAL>
          <xsl:value-of select=""$var:v116"" />
        </ns0:FIRST_SYMPTOM_DATE_QUAL>
        <ns0:LOCATION_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C023_HealthCareServiceLocationInformation/C02301_PlaceofServiceCode/text()"" />
        </ns0:LOCATION_CODE>
        <xsl:if test=""string($var:v117)='true'"">
          <xsl:variable name=""var:v118"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_DemonstrationProjectIdentifier/REF01_ReferenceIdentificationQualifier/text()"" />
          <ns0:ADDTNL_CLAIM_INFO_QUAL>
            <xsl:value-of select=""$var:v118"" />
          </ns0:ADDTNL_CLAIM_INFO_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v120)='true'"">
          <xsl:variable name=""var:v121"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_DemonstrationProjectIdentifier/REF02_DemonstrationProjectIdentifier/text()"" />
          <ns0:ADDTNL_CLAIM_INFO>
            <xsl:value-of select=""$var:v121"" />
          </ns0:ADDTNL_CLAIM_INFO>
        </xsl:if>
      </ns0:PROF_CLAIM>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2300_Loop"">
            <xsl:for-each select=""s1:TS837_2400_Loop"">
              <xsl:variable name=""var:v122"" select=""string(../s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text())"" />
              <xsl:variable name=""var:v123"" select=""string(../s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text())"" />
              <xsl:variable name=""var:v127"" select=""string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP02_DateTimePeriodFormatQualifier/text())"" />
              <xsl:variable name=""var:v128"" select=""string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP03_ServiceDate/text())"" />
              <xsl:variable name=""var:v130"" select=""userCSharp:LogicalExistence(boolean(s1:SV1_ProfessionalService/SV105_PlaceofServiceCode))"" />
              <xsl:variable name=""var:v131"" select=""userCSharp:StringSize(string(s1:SV1_ProfessionalService/SV105_PlaceofServiceCode/text()))"" />
              <xsl:variable name=""var:v133"" select=""string(s1:SV1_ProfessionalService/SV105_PlaceofServiceCode/text())"" />
              <xsl:variable name=""var:v137"" select=""s1:TS837_2410_Loop/s1:LIN_DrugIdentification[1]/LIN03_NationalDrugCodeorUniversalProductNumber/text()"" />
              <xsl:variable name=""var:v138"" select=""string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00401_DiagnosisCodePointer/text())"" />
              <xsl:variable name=""var:v139"" select=""string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00402_DiagnosisCodePointer/text())"" />
              <xsl:variable name=""var:v140"" select=""string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00403_DiagnosisCodePointer/text())"" />
              <xsl:variable name=""var:v141"" select=""string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00404_DiagnosisCodePointer/text())"" />
              <xsl:variable name=""var:v143"" select=""userCSharp:LogicalExistence(boolean(s1:NTE_SubLoop/s1:NTE_ThirdPartyOrganizationNotes/NTE02_LineNoteText))"" />
              <xsl:variable name=""var:v145"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_LineItemControlNumber/REF02_LineItemControlNumber))"" />
              <xsl:variable name=""var:v147"" select=""userCSharp:LogicalExistence(boolean(s1:QTY_SubLoop/s1:QTY_ObstetricAnesthesiaAdditionalUnits/QTY02_ObstetricAdditionalUnits))"" />
              <ns0:PROF_CLAIM_DETAIL>
                <xsl:variable name=""var:v124"" select=""userCSharp:ExternalClmID($var:v122 , $var:v123)"" />
                <ns0:CLAIM_ID>
                  <xsl:value-of select=""$var:v124"" />
                </ns0:CLAIM_ID>
                <ns0:LINE_NUMBER>
                  <xsl:value-of select=""s1:LX_ServiceLineNumber/LX01_AssignedNumber/text()"" />
                </ns0:LINE_NUMBER>
                <ns0:SERVICE_CODE_QUALIFIER>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00301_ProductorServiceIDQualifier/text()"" />
                </ns0:SERVICE_CODE_QUALIFIER>
                <ns0:SERVICE_CODE>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00302_ProcedureCode/text()"" />
                </ns0:SERVICE_CODE>
                <xsl:variable name=""var:v125"" select=""userCSharp:SubServiceModifierList(string(s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00303_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00304_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00305_ProcedureModifier/text()) , string(s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00306_ProcedureModifier/text()))"" />
                <ns0:SERVICE_MODIFIER_LIST>
                  <xsl:value-of select=""$var:v125"" />
                </ns0:SERVICE_MODIFIER_LIST>
                <xsl:variable name=""var:v126"" select=""userCSharp:SubServiceFromDate(string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP02_DateTimePeriodFormatQualifier/text()) , string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP03_ServiceDate/text()))"" />
                <ns0:SERVICE_FROM_DATE>
                  <xsl:value-of select=""$var:v126"" />
                </ns0:SERVICE_FROM_DATE>
                <xsl:variable name=""var:v129"" select=""userCSharp:SubServiceToDate($var:v127 , $var:v128)"" />
                <ns0:SERVICE_TO_DATE>
                  <xsl:value-of select=""$var:v129"" />
                </ns0:SERVICE_TO_DATE>
                <xsl:variable name=""var:v132"" select=""userCSharp:bHaveData(string($var:v130) , string($var:v131))"" />
                <xsl:variable name=""var:v134"" select=""userCSharp:LocationCode($var:v133 , string(../s1:CLM_ClaimInformation/s1:C023_HealthCareServiceLocationInformation/C02301_PlaceofServiceCode/text()) , string($var:v132))"" />
                <ns0:LOCATION_CODE>
                  <xsl:value-of select=""$var:v134"" />
                </ns0:LOCATION_CODE>
                <xsl:variable name=""var:v135"" select=""userCSharp:DiagnosisPointers(string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00401_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00402_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00403_DiagnosisCodePointer/text()) , string(s1:SV1_ProfessionalService/s1:C004_CompositeDiagnosisCodePointer/C00404_DiagnosisCodePointer/text()))"" />
                <xsl:variable name=""var:v136"" select=""userCSharp:DiagPatCodesList(string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_2/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_2/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_3/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_3/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_4/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_4/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_5/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_5/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_6/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_6/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_7/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_7/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_8/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_8/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_9/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_9/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_10/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_10/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_11/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_11/C02202_DiagnosisCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_12/C02201_DiagnosisTypeCode/text()) , string(../s1:HI_SubLoop/s1:HI_HealthCareDiagnosisCode/s1:C022_HealthCareCodeInformation_12/C02202_DiagnosisCode/text()) , string($var:v135))"" />
                <ns0:DIAGNOSIS_CODE_LIST>
                  <xsl:value-of select=""$var:v136"" />
                </ns0:DIAGNOSIS_CODE_LIST>
                <ns0:NDC_CODE_LIST>
                  <xsl:value-of select=""$var:v137"" />
                </ns0:NDC_CODE_LIST>
                <ns0:TYPE_OF_SERVICE>
                  <xsl:text />
                </ns0:TYPE_OF_SERVICE>
                <ns0:TOTAL_CHARGES>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/SV102_LineItemChargeAmount/text()"" />
                </ns0:TOTAL_CHARGES>
                <ns0:UNIT_MEASUREMENT>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/SV103_UnitorBasisforMeasurementCode/text()"" />
                </ns0:UNIT_MEASUREMENT>
                <ns0:QUANTITY>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/SV104_ServiceUnitCount/text()"" />
                </ns0:QUANTITY>
                <ns0:COB_PAID>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD02_ServiceLinePaidAmount/text()"" />
                </ns0:COB_PAID>
                <ns0:REPRICE_CHARGES>
                  <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP02_RepricedAllowedAmount/text()"" />
                </ns0:REPRICE_CHARGES>
                <xsl:variable name=""var:v142"" select=""userCSharp:DiagnosisPointers($var:v138 , $var:v139 , $var:v140 , $var:v141)"" />
                <ns0:DIAGNOSIS_IDX>
                  <xsl:value-of select=""$var:v142"" />
                </ns0:DIAGNOSIS_IDX>
                <xsl:variable name=""var:v144"" select=""userCSharp:fCommon(string(s1:NTE_SubLoop/s1:NTE_ThirdPartyOrganizationNotes/NTE02_LineNoteText/text()) , string($var:v143))"" />
                <ns0:TP_ORG_NOTES>
                  <xsl:value-of select=""$var:v144"" />
                </ns0:TP_ORG_NOTES>
                <xsl:variable name=""var:v146"" select=""userCSharp:fCommon(string(s1:REF_SubLoop_7/s1:REF_LineItemControlNumber/REF02_LineItemControlNumber/text()) , string($var:v145))"" />
                <ns0:LINEITEM_CONTROL_NUMBER>
                  <xsl:value-of select=""$var:v146"" />
                </ns0:LINEITEM_CONTROL_NUMBER>
                <xsl:variable name=""var:v148"" select=""userCSharp:fCommon(string(s1:QTY_SubLoop/s1:QTY_ObstetricAnesthesiaAdditionalUnits/QTY02_ObstetricAdditionalUnits/text()) , string($var:v147))"" />
                <ns0:OBS_ANESTHSIA_ADDTNL_UNITS>
                  <xsl:value-of select=""$var:v148"" />
                </ns0:OBS_ANESTHSIA_ADDTNL_UNITS>
                <ns0:PATIENT_LIABILTY_AMT>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:AMT_RemainingPatientLiability_2/AMT02_RemainingPatientLiability/text()"" />
                </ns0:PATIENT_LIABILTY_AMT>
                <xsl:if test=""s1:SV1_ProfessionalService/SV109_EmergencyIndicator"">
                  <ns0:EMERGENCY_IND>
                    <xsl:value-of select=""s1:SV1_ProfessionalService/SV109_EmergencyIndicator/text()"" />
                  </ns0:EMERGENCY_IND>
                </xsl:if>
                <xsl:if test=""s1:SV1_ProfessionalService/SV111_EPSDTIndicator"">
                  <ns0:EPSDT_IND>
                    <xsl:value-of select=""s1:SV1_ProfessionalService/SV111_EPSDTIndicator/text()"" />
                  </ns0:EPSDT_IND>
                </xsl:if>
                <xsl:if test=""s1:SV1_ProfessionalService/SV112_FamilyPlanningIndicator"">
                  <ns0:FAMILY_PLAN_IND>
                    <xsl:value-of select=""s1:SV1_ProfessionalService/SV112_FamilyPlanningIndicator/text()"" />
                  </ns0:FAMILY_PLAN_IND>
                </xsl:if>
                <xsl:if test=""s1:SV1_ProfessionalService/SV115_Co_PayStatusCode"">
                  <ns0:COPAY_WAVIER>
                    <xsl:value-of select=""s1:SV1_ProfessionalService/SV115_Co_PayStatusCode/text()"" />
                  </ns0:COPAY_WAVIER>
                </xsl:if>
                <ns0:PROV_LINEITEM_NUM>
                  <xsl:text />
                </ns0:PROV_LINEITEM_NUM>
                <ns0:NATIONAL_DRUG_COUNT>
                  <xsl:value-of select=""s1:TS837_2410_Loop/s1:CTP_DrugQuantity/CTP04_NationalDrugUnitCount/text()"" />
                </ns0:NATIONAL_DRUG_COUNT>
              </ns0:PROF_CLAIM_DETAIL>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
      </xsl:for-each>
      <ns0:CLAIM_ADDTNL>
        <xsl:variable name=""var:v149"" select=""userCSharp:ExternalClmID($var:v55 , $var:v9)"" />
        <ns0:CLAIM_ID>
          <xsl:value-of select=""$var:v149"" />
        </ns0:CLAIM_ID>
        <xsl:variable name=""var:v151"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV02_ReferenceIdentificationQualifier/text()) , string($var:v150))"" />
        <ns0:BILL_PAYTO_TAX_QUAL>
          <xsl:value-of select=""$var:v151"" />
        </ns0:BILL_PAYTO_TAX_QUAL>
        <xsl:variable name=""var:v153"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:PRV_BillingProviderSpecialtyInformation/PRV03_ProviderTaxonomyCode/text()) , string($var:v152))"" />
        <ns0:BILL_PAYTO_TAXONOMY>
          <xsl:value-of select=""$var:v153"" />
        </ns0:BILL_PAYTO_TAXONOMY>
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
        <xsl:variable name=""var:v155"" select=""userCSharp:MyConcat(string($var:v154) , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:N3_BillingProviderAddress/N302_BillingProviderAddressLine/text()))"" />
        <ns0:BILL_PROVIDER_ADD2>
          <xsl:value-of select=""$var:v155"" />
        </ns0:BILL_PROVIDER_ADD2>
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
        <xsl:if test=""string($var:v156)='true'"">
          <xsl:variable name=""var:v157"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF01_ReferenceIdentificationQualifier/text()"" />
          <xsl:variable name=""var:v158"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
          <xsl:variable name=""var:v159"" select=""boolean(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification)"" />
          <xsl:variable name=""var:v160"" select=""userCSharp:LogicalExistence($var:v159)"" />
          <xsl:if test=""string($var:v160)='true'"">
            <xsl:variable name=""var:v161"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderTaxIdentification/REF02_BillingProviderTaxIdentificationNumber/text()"" />
            <xsl:variable name=""var:v162"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
            <xsl:variable name=""var:v163"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[1]/REF01_ReferenceIdentificationQualifier/text()"" />
            <xsl:variable name=""var:v164"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[1]/REF02_BillingProviderLicenseand_orUPINInformation/text()"" />
            <xsl:variable name=""var:v165"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[2]/REF01_ReferenceIdentificationQualifier/text()"" />
            <xsl:variable name=""var:v166"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AA_Loop/s1:REF_SubLoop/s1:REF_BillingProviderUPIN_LicenseInformation_Loop/s1:REF_BillingProviderUPIN_LicenseInformation[2]/REF02_BillingProviderLicenseand_orUPINInformation/text()"" />
            <xsl:variable name=""var:v167"" select=""userCSharp:StringConcat(string($var:v157) , string($var:v158) , string($var:v161) , string($var:v162) , string($var:v163) , string($var:v158) , string($var:v164) , string($var:v162) , string($var:v165) , string($var:v158) , string($var:v166) , string($var:v162))"" />
            <ns0:BILL_PROVIDER_REF>
              <xsl:value-of select=""$var:v167"" />
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
        <xsl:variable name=""var:v169"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM102_EntityTypeQualifier/text()) , string($var:v168))"" />
        <ns0:PAY_TO_PROVIDER_QUAL>
          <xsl:value-of select=""$var:v169"" />
        </ns0:PAY_TO_PROVIDER_QUAL>
        <xsl:variable name=""var:v171"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM103_Pay_toLastorOrganizationalName/text()) , string($var:v170))"" />
        <ns0:PAY_TO_PROVIDER_LNAME>
          <xsl:value-of select=""$var:v171"" />
        </ns0:PAY_TO_PROVIDER_LNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM105_NameMiddle"">
          <ns0:PAY_TO_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM105_NameMiddle/text()"" />
          </ns0:PAY_TO_PROVIDER_MNAME>
        </xsl:if>
        <xsl:variable name=""var:v173"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM104_NameFirst/text()) , string($var:v172))"" />
        <ns0:PAY_TO_PROVIDER_FNAME>
          <xsl:value-of select=""$var:v173"" />
        </ns0:PAY_TO_PROVIDER_FNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM107_NameSuffix"">
          <ns0:PAY_TO_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM107_NameSuffix/text()"" />
          </ns0:PAY_TO_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:variable name=""var:v175"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM108_IdentificationCodeQualifier/text()) , string($var:v174))"" />
        <ns0:PAY_TO_PROVIDER_ID_QUAL>
          <xsl:value-of select=""$var:v175"" />
        </ns0:PAY_TO_PROVIDER_ID_QUAL>
        <xsl:variable name=""var:v177"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AB_Loop/s1:NM1_Pay_toAddressName/NM109_IdentificationCode/text()) , string($var:v176))"" />
        <ns0:PAY_TO_PROVIDER_ID>
          <xsl:value-of select=""$var:v177"" />
        </ns0:PAY_TO_PROVIDER_ID>
        <xsl:variable name=""var:v181"" select=""userCSharp:fCommon($var:v180 , string($var:v179))"" />
        <ns0:PAY_TO_PROVIDER_NPI_ID>
          <xsl:value-of select=""$var:v181"" />
        </ns0:PAY_TO_PROVIDER_NPI_ID>
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
        <xsl:variable name=""var:v183"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:PRV_RenderingProviderSpecialtyInformation/PRV03_ProviderTaxonomyCode/text()) , string($var:v182))"" />
        <ns0:REN_PROVIDER_TAXONOMY>
          <xsl:value-of select=""$var:v183"" />
        </ns0:REN_PROVIDER_TAXONOMY>
        <xsl:variable name=""var:v185"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM102_EntityTypeQualifier/text()) , string($var:v184))"" />
        <ns0:REN_PROVIDER_QUAL>
          <xsl:value-of select=""$var:v185"" />
        </ns0:REN_PROVIDER_QUAL>
        <xsl:variable name=""var:v188"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM103_RenderingProviderLastorOrganizationName/text()) , string($var:v187))"" />
        <ns0:REN_PROVIDER_LNAME>
          <xsl:value-of select=""$var:v188"" />
        </ns0:REN_PROVIDER_LNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM105_RenderingProviderMiddleNameorInitial"">
          <ns0:REN_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM105_RenderingProviderMiddleNameorInitial/text()"" />
          </ns0:REN_PROVIDER_MNAME>
        </xsl:if>
        <xsl:variable name=""var:v190"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM104_RenderingProviderFirstName/text()) , string($var:v189))"" />
        <ns0:REN_REN_PROVIDER_FNAME>
          <xsl:value-of select=""$var:v190"" />
        </ns0:REN_REN_PROVIDER_FNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM107_RenderingProviderNameSuffix"">
          <ns0:REN_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM107_RenderingProviderNameSuffix/text()"" />
          </ns0:REN_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:variable name=""var:v192"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM108_IdentificationCodeQualifier/text()) , string($var:v191))"" />
        <ns0:REN_PROVIDER_ID_QUAL>
          <xsl:value-of select=""$var:v192"" />
        </ns0:REN_PROVIDER_ID_QUAL>
        <xsl:variable name=""var:v194"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310B_Loop/s1:NM1_RenderingProviderName/NM109_RenderingProviderIdentifier/text()) , string($var:v193))"" />
        <ns0:REN_PROVIDER_ID>
          <xsl:value-of select=""$var:v194"" />
        </ns0:REN_PROVIDER_ID>
        <xsl:variable name=""var:v198"" select=""userCSharp:fCommon($var:v197 , string($var:v196))"" />
        <ns0:REN_PROVIDER_NPI_ID>
          <xsl:value-of select=""$var:v198"" />
        </ns0:REN_PROVIDER_NPI_ID>
        <ns0:REN_PROVIDER_REF>
          <xsl:value-of select=""$var:v209"" />
        </ns0:REN_PROVIDER_REF>
        <ns0:AREF_PROVIDER_TAXONOMY>
          <xsl:text />
        </ns0:AREF_PROVIDER_TAXONOMY>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v210"" select=""position()"" />
                    <xsl:variable name=""var:v211"" select=""userCSharp:LogicalEq(string($var:v210) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v211"">
                      <xsl:variable name=""var:v212"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_ReferringProviderName))"" />
                      <xsl:if test=""string($var:v212)='true'"">
                        <xsl:variable name=""var:v213"" select=""s1:NM1_ReferringProviderName/NM102_EntityTypeQualifier/text()"" />
                        <ns0:AREF_PROVIDER_QUAL>
                          <xsl:value-of select=""$var:v213"" />
                        </ns0:AREF_PROVIDER_QUAL>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v214"" select=""position()"" />
                    <xsl:variable name=""var:v215"" select=""userCSharp:LogicalEq(string($var:v214) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v215"">
                      <ns0:AREF_PROVIDER_LNAME>
                        <xsl:value-of select=""s1:NM1_ReferringProviderName/NM103_ReferringProviderLastName/text()"" />
                      </ns0:AREF_PROVIDER_LNAME>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v216"" select=""position()"" />
                    <xsl:variable name=""var:v217"" select=""userCSharp:LogicalEq(string($var:v216) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v217"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM105_ReferringProviderMiddleNameorInitial"">
                        <ns0:AREF_PROVIDER_MNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                        </ns0:AREF_PROVIDER_MNAME>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v218"" select=""position()"" />
                    <xsl:variable name=""var:v219"" select=""userCSharp:LogicalEq(string($var:v218) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v219"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM104_ReferringProviderFirstName"">
                        <ns0:AREF_PROVIDER_FNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM104_ReferringProviderFirstName/text()"" />
                        </ns0:AREF_PROVIDER_FNAME>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v220"" select=""position()"" />
                    <xsl:variable name=""var:v221"" select=""userCSharp:LogicalEq(string($var:v220) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v221"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM107_ReferringProviderNameSuffix"">
                        <ns0:AREF_PROVIDER_SUFFIX>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM107_ReferringProviderNameSuffix/text()"" />
                        </ns0:AREF_PROVIDER_SUFFIX>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v222"" select=""position()"" />
                    <xsl:variable name=""var:v223"" select=""userCSharp:LogicalEq(string($var:v222) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v223"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM108_IdentificationCodeQualifier"">
                        <ns0:AREF_PROVIDER_ID_QUAL>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM108_IdentificationCodeQualifier/text()"" />
                        </ns0:AREF_PROVIDER_ID_QUAL>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v224"" select=""position()"" />
                    <xsl:variable name=""var:v225"" select=""userCSharp:LogicalEq(string($var:v224) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v225"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier"">
                        <ns0:AREF_PROVIDER_ID>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier/text()"" />
                        </ns0:AREF_PROVIDER_ID>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v226"" select=""position()"" />
                    <xsl:variable name=""var:v227"" select=""userCSharp:LogicalEq(string($var:v226) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v227"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier"">
                        <ns0:AREF_PROVIDER_NPI_ID>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier/text()"" />
                        </ns0:AREF_PROVIDER_NPI_ID>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v228"" select=""position()"" />
                    <xsl:variable name=""var:v229"" select=""userCSharp:LogicalEq(string($var:v228) , &quot;1&quot;)"" />
                    <xsl:if test=""$var:v229"">
                      <xsl:variable name=""var:v230"" select=""./s1:REF_ReferringProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v231"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
                      <xsl:variable name=""var:v232"" select=""./s1:REF_ReferringProviderSecondaryIdentification[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v233"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
                      <xsl:variable name=""var:v234"" select=""./s1:REF_ReferringProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v235"" select=""./s1:REF_ReferringProviderSecondaryIdentification[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v236"" select=""./s1:REF_ReferringProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v237"" select=""./s1:REF_ReferringProviderSecondaryIdentification[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v238"" select=""userCSharp:StringConcat(string($var:v230) , string($var:v231) , string($var:v232) , string($var:v233) , string($var:v234) , string($var:v231) , string($var:v235) , string($var:v233) , string($var:v236) , string($var:v231) , string($var:v237) , string($var:v233))"" />
                      <ns0:AREF_PROVIDER_REF>
                        <xsl:value-of select=""$var:v238"" />
                      </ns0:AREF_PROVIDER_REF>
                    </xsl:if>
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
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM102_EntityTypeQualifier/text()"" />
        </ns0:SUPER_PROVIDER_QUAL>
        <ns0:SUPER_PROVIDER_LNAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM103_SupervisingProviderLastName/text()"" />
        </ns0:SUPER_PROVIDER_LNAME>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM105_SupervisingProviderMiddleNameorInitial"">
          <ns0:SUPER_PROVIDER_MNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM105_SupervisingProviderMiddleNameorInitial/text()"" />
          </ns0:SUPER_PROVIDER_MNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM104_SupervisingProviderFirstName"">
          <ns0:SUPER_PROVIDER_FNAME>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM104_SupervisingProviderFirstName/text()"" />
          </ns0:SUPER_PROVIDER_FNAME>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM107_SupervisingProviderNameSuffix"">
          <ns0:SUPER_PROVIDER_SUFFIX>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM107_SupervisingProviderNameSuffix/text()"" />
          </ns0:SUPER_PROVIDER_SUFFIX>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM108_IdentificationCodeQualifier"">
          <ns0:SUPER_PROVIDER_ID_QUAL>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM108_IdentificationCodeQualifier/text()"" />
          </ns0:SUPER_PROVIDER_ID_QUAL>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM109_SupervisingProviderIdentifier"">
          <ns0:SUPER_PROVIDER_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM109_SupervisingProviderIdentifier/text()"" />
          </ns0:SUPER_PROVIDER_ID>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM109_SupervisingProviderIdentifier"">
          <ns0:SUPER_PROVIDER_NPI_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310D_Loop/s1:NM1_SupervisingProviderName/NM109_SupervisingProviderIdentifier/text()"" />
          </ns0:SUPER_PROVIDER_NPI_ID>
        </xsl:if>
        <ns0:SUPER_PROVIDER_REF>
          <xsl:value-of select=""$var:v247"" />
        </ns0:SUPER_PROVIDER_REF>
        <ns0:SERVICE_PROV_ENTITY_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM101_EntityIdentifierCode/text()"" />
        </ns0:SERVICE_PROV_ENTITY_QUAL>
        <ns0:SERVICE_PROV_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM102_EntityTypeQualifier/text()"" />
        </ns0:SERVICE_PROV_QUAL>
        <ns0:SERVICE_PROV_NAME>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM103_LaboratoryorFacilityName/text()"" />
        </ns0:SERVICE_PROV_NAME>
        <xsl:variable name=""var:v249"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM108_IdentificationCodeQualifier/text()) , string($var:v248))"" />
        <ns0:SERVICE_PROV_ID_QUAL>
          <xsl:value-of select=""$var:v249"" />
        </ns0:SERVICE_PROV_ID_QUAL>
        <xsl:variable name=""var:v251"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:NM1_ServiceFacilityLocationName/NM109_LaboratoryorFacilityPrimaryIdentifier/text()) , string($var:v250))"" />
        <ns0:SERVICE_PROV_ID>
          <xsl:value-of select=""$var:v251"" />
        </ns0:SERVICE_PROV_ID>
        <xsl:variable name=""var:v255"" select=""userCSharp:fCommon($var:v254 , string($var:v253))"" />
        <ns0:SERVICE_PROV_NPI_ID>
          <xsl:value-of select=""$var:v255"" />
        </ns0:SERVICE_PROV_NPI_ID>
        <ns0:SERVICE_PROV_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N3_ServiceFacilityLocationAddress/N301_LaboratoryorFacilityAddressLine/text()"" />
        </ns0:SERVICE_PROV_ADD1>
        <xsl:variable name=""var:v257"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N3_ServiceFacilityLocationAddress/N302_LaboratoryorFacilityAddressLine/text()) , string($var:v256))"" />
        <ns0:SERVICE_PROV_ADD2>
          <xsl:value-of select=""$var:v257"" />
        </ns0:SERVICE_PROV_ADD2>
        <xsl:variable name=""var:v259"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N401_LaboratoryorFacilityCityName/text()) , string($var:v258))"" />
        <ns0:SERVICE_PROV_CITY>
          <xsl:value-of select=""$var:v259"" />
        </ns0:SERVICE_PROV_CITY>
        <xsl:variable name=""var:v261"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N402_LaboratoryorFacilityStateorProvinceCode/text()) , string($var:v260))"" />
        <ns0:SERVICE_PROV_STATE>
          <xsl:value-of select=""$var:v261"" />
        </ns0:SERVICE_PROV_STATE>
        <xsl:variable name=""var:v263"" select=""userCSharp:fCommon(string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode/N403_LaboratoryorFacilityPostalZoneorZIPCode/text()) , string($var:v262))"" />
        <ns0:SERVICE_PROV_ZIP>
          <xsl:value-of select=""$var:v263"" />
        </ns0:SERVICE_PROV_ZIP>
        <ns0:SERVICE_PROV_REF>
          <xsl:value-of select=""$var:v270"" />
        </ns0:SERVICE_PROV_REF>
        <ns0:SERVICE_PROV_PER01>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER01_ContactFunctionCode/text()"" />
        </ns0:SERVICE_PROV_PER01>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER02_Name"">
          <ns0:SERVICE_PROV_PER02>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER02_Name/text()"" />
          </ns0:SERVICE_PROV_PER02>
        </xsl:if>
        <ns0:SERVICE_PROV_PER03>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER03_CommunicationNumberQualifier/text()"" />
        </ns0:SERVICE_PROV_PER03>
        <ns0:SERVICE_PROV_PER04>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER04_CommunicationNumber/text()"" />
        </ns0:SERVICE_PROV_PER04>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER05_CommunicationNumberQualifier"">
          <ns0:SERVICE_PROV_PER05>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER05_CommunicationNumberQualifier/text()"" />
          </ns0:SERVICE_PROV_PER05>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER06_CommunicationNumber"">
          <ns0:SERVICE_PROV_PER06>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310C_Loop/s1:PER_ServiceFacilityContactInformation/PER06_CommunicationNumber/text()"" />
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
          <xsl:value-of select=""$var:v283"" />
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
          <xsl:text />
        </ns0:PATIENT_RELATION_CODE>
        <ns0:PATIENT_ID_QUAL>
          <xsl:text />
        </ns0:PATIENT_ID_QUAL>
        <ns0:PATIENT_ID>
          <xsl:text />
        </ns0:PATIENT_ID>
        <ns0:PATIENT_LAST_NAME>
          <xsl:text />
        </ns0:PATIENT_LAST_NAME>
        <ns0:PATIENT_FIRST_NAME>
          <xsl:text />
        </ns0:PATIENT_FIRST_NAME>
        <ns0:PATIENT_MIDDLE_NAME>
          <xsl:text />
        </ns0:PATIENT_MIDDLE_NAME>
        <ns0:PATIENT_GENDER>
          <xsl:text />
        </ns0:PATIENT_GENDER>
        <ns0:PATIENT_BIRTH_DATE>
          <xsl:text />
        </ns0:PATIENT_BIRTH_DATE>
        <ns0:PATIENT_ADD1>
          <xsl:text />
        </ns0:PATIENT_ADD1>
        <ns0:PATIENT_ADD2>
          <xsl:text />
        </ns0:PATIENT_ADD2>
        <ns0:PATIENT_CITY>
          <xsl:text />
        </ns0:PATIENT_CITY>
        <ns0:PATIENT_STATE>
          <xsl:text />
        </ns0:PATIENT_STATE>
        <ns0:PATIENT_ZIP>
          <xsl:text />
        </ns0:PATIENT_ZIP>
        <ns0:PATIENT_DEATH>
          <xsl:text />
        </ns0:PATIENT_DEATH>
        <ns0:PATIENT_UOM>
          <xsl:text />
        </ns0:PATIENT_UOM>
        <ns0:PATIENT_WEIGHT>
          <xsl:text />
        </ns0:PATIENT_WEIGHT>
        <ns0:PATIENT_PRG_IND>
          <xsl:text />
        </ns0:PATIENT_PRG_IND>
        <ns0:REPORT_TYPE_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK01_AttachmentReportTypeCode/text()"" />
        </ns0:REPORT_TYPE_CODE>
        <ns0:TRANSMISSION_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK02_AttachmentTransmissionCode/text()"" />
        </ns0:TRANSMISSION_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK05_IdentificationCodeQualifier"">
          <ns0:ID_CODER_QUALIFIER>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK05_IdentificationCodeQualifier/text()"" />
          </ns0:ID_CODER_QUALIFIER>
        </xsl:if>
        <ns0:CONTROL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_PayerClaimControlNumber/REF02_PayerClaimControlNumber/text()"" />
        </ns0:CONTROL_NUMBER>
        <ns0:FIXED_FORMAT_INFO>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:K3_FileInformation/K301_FixedFormatInformation/text()"" />
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
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:NM1_SubLoop_2/s1:TS837_2010AC_Loop/s1:NM1_Pay_ToPlanName/NM102_EntityTypeQualifier/text()"" />
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
          <xsl:value-of select=""$var:v284"" />
        </ns0:PAY_TO_PLAN_REF>
        <ns0:AMBULANCE_PICKUP_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N3_AmbulancePick_upLocationAddress/N301_AmbulancePick_upAddressLine/text()"" />
        </ns0:AMBULANCE_PICKUP_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N3_AmbulancePick_upLocationAddress/N302_AmbulancePick_upAddressLine"">
          <ns0:AMBULANCE_PICKUP_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N3_AmbulancePick_upLocationAddress/N302_AmbulancePick_upAddressLine/text()"" />
          </ns0:AMBULANCE_PICKUP_ADD2>
        </xsl:if>
        <ns0:AMBULANCE_PICKUP_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode/N401_AmbulancePick_upCityName/text()"" />
        </ns0:AMBULANCE_PICKUP_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode/N402_AmbulancePick_upStateorProvinceCode"">
          <ns0:AMBULANCE_PICKUP_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode/N402_AmbulancePick_upStateorProvinceCode/text()"" />
          </ns0:AMBULANCE_PICKUP_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode/N403_AmbulancePick_upPostalZoneorZIPCode"">
          <ns0:AMBULANCE_PICKUP_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310E_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode/N403_AmbulancePick_upPostalZoneorZIPCode/text()"" />
          </ns0:AMBULANCE_PICKUP_ZIP>
        </xsl:if>
        <ns0:AMBULANCE_DROPOFF_ADD1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N3_AmbulanceDrop_offLocationAddress/N301_AmbulanceDrop_offAddressLine/text()"" />
        </ns0:AMBULANCE_DROPOFF_ADD1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N3_AmbulanceDrop_offLocationAddress/N302_AmbulanceDrop_offAddressLine"">
          <ns0:AMBULANCE_DROPOFF_ADD2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N3_AmbulanceDrop_offLocationAddress/N302_AmbulanceDrop_offAddressLine/text()"" />
          </ns0:AMBULANCE_DROPOFF_ADD2>
        </xsl:if>
        <ns0:AMBULANCE_DROPOFF_CITY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode/N401_AmbulanceDrop_offCityName/text()"" />
        </ns0:AMBULANCE_DROPOFF_CITY>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode/N402_AmbulanceDrop_offStateorProvinceCode"">
          <ns0:AMBULANCE_DROPOFF_STATE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode/N402_AmbulanceDrop_offStateorProvinceCode/text()"" />
          </ns0:AMBULANCE_DROPOFF_STATE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode/N403_AmbulanceDrop_offPostalZoneorZIPCode"">
          <ns0:AMBULANCE_DROPOFF_ZIP>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode/N403_AmbulanceDrop_offPostalZoneorZIPCode/text()"" />
          </ns0:AMBULANCE_DROPOFF_ZIP>
        </xsl:if>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v285"" select=""position()"" />
                <xsl:variable name=""var:v286"" select=""userCSharp:LogicalEq(string($var:v285) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v286"">
                  <xsl:variable name=""var:v287"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode))"" />
                  <xsl:if test=""string($var:v287)='true'"">
                    <xsl:variable name=""var:v288"" select=""s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode/text()"" />
                    <ns0:SEC_SEQ_NUMBER>
                      <xsl:value-of select=""$var:v288"" />
                    </ns0:SEC_SEQ_NUMBER>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v289"" select=""position()"" />
                <xsl:variable name=""var:v290"" select=""userCSharp:LogicalEq(string($var:v289) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v290"">
                  <xsl:variable name=""var:v291"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR02_IndividualRelationshipCode))"" />
                  <xsl:if test=""string($var:v291)='true'"">
                    <xsl:variable name=""var:v292"" select=""s1:SBR_OtherSubscriberInformation/SBR02_IndividualRelationshipCode/text()"" />
                    <ns0:SEC_RELATION_CODE>
                      <xsl:value-of select=""$var:v292"" />
                    </ns0:SEC_RELATION_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v293"" select=""position()"" />
                <xsl:variable name=""var:v294"" select=""userCSharp:LogicalEq(string($var:v293) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v294"">
                  <xsl:variable name=""var:v295"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR03_InsuredGrouporPolicyNumber))"" />
                  <xsl:if test=""string($var:v295)='true'"">
                    <xsl:variable name=""var:v296"" select=""s1:SBR_OtherSubscriberInformation/SBR03_InsuredGrouporPolicyNumber/text()"" />
                    <ns0:SEC_GROUP_ID>
                      <xsl:value-of select=""$var:v296"" />
                    </ns0:SEC_GROUP_ID>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v297"" select=""position()"" />
                <xsl:variable name=""var:v298"" select=""userCSharp:LogicalEq(string($var:v297) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v298"">
                  <xsl:variable name=""var:v299"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR04_OtherInsuredGroupName))"" />
                  <xsl:if test=""string($var:v299)='true'"">
                    <xsl:variable name=""var:v300"" select=""s1:SBR_OtherSubscriberInformation/SBR04_OtherInsuredGroupName/text()"" />
                    <ns0:SEC_GROUP_NAME>
                      <xsl:value-of select=""$var:v300"" />
                    </ns0:SEC_GROUP_NAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v301"" select=""position()"" />
                <xsl:variable name=""var:v302"" select=""userCSharp:LogicalEq(string($var:v301) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v302"">
                  <xsl:variable name=""var:v303"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR09_ClaimFilingIndicatorCode))"" />
                  <xsl:if test=""string($var:v303)='true'"">
                    <xsl:variable name=""var:v304"" select=""s1:SBR_OtherSubscriberInformation/SBR09_ClaimFilingIndicatorCode/text()"" />
                    <ns0:SEC_CLAIM_IND>
                      <xsl:value-of select=""$var:v304"" />
                    </ns0:SEC_CLAIM_IND>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v305"" select=""position()"" />
                <xsl:variable name=""var:v306"" select=""userCSharp:LogicalEq(string($var:v305) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v306"">
                  <xsl:variable name=""var:v307"" select=""userCSharp:LogicalExistence(boolean(s1:SBR_OtherSubscriberInformation/SBR05_InsuranceTypeCode))"" />
                  <xsl:if test=""string($var:v307)='true'"">
                    <xsl:variable name=""var:v308"" select=""s1:SBR_OtherSubscriberInformation/SBR05_InsuranceTypeCode/text()"" />
                    <ns0:SEC_INS_TYPE_CODE>
                      <xsl:value-of select=""$var:v308"" />
                    </ns0:SEC_INS_TYPE_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v309"" select=""position()"" />
                <xsl:variable name=""var:v310"" select=""userCSharp:LogicalEq(string($var:v309) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v310"">
                  <xsl:variable name=""var:v311"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation/OI03_BenefitsAssignmentCertificationIndicator))"" />
                  <xsl:if test=""string($var:v311)='true'"">
                    <xsl:variable name=""var:v312"" select=""s1:OI_OtherInsuranceCoverageInformation/OI03_BenefitsAssignmentCertificationIndicator/text()"" />
                    <ns0:SEC_ASSIGN_BENRFIT_IND>
                      <xsl:value-of select=""$var:v312"" />
                    </ns0:SEC_ASSIGN_BENRFIT_IND>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v313"" select=""position()"" />
                <xsl:variable name=""var:v314"" select=""userCSharp:LogicalEq(string($var:v313) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v314"">
                  <xsl:variable name=""var:v315"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation/OI04_PatientSignatureSourceCode))"" />
                  <xsl:if test=""string($var:v315)='true'"">
                    <xsl:variable name=""var:v316"" select=""s1:OI_OtherInsuranceCoverageInformation/OI04_PatientSignatureSourceCode/text()"" />
                    <ns0:SEC_PAT_SIGN_SRC_CODE>
                      <xsl:value-of select=""$var:v316"" />
                    </ns0:SEC_PAT_SIGN_SRC_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v317"" select=""position()"" />
                <xsl:variable name=""var:v318"" select=""userCSharp:LogicalEq(string($var:v317) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v318"">
                  <xsl:variable name=""var:v319"" select=""userCSharp:LogicalExistence(boolean(s1:OI_OtherInsuranceCoverageInformation/OI06_ReleaseofInformationCode))"" />
                  <xsl:if test=""string($var:v319)='true'"">
                    <xsl:variable name=""var:v320"" select=""s1:OI_OtherInsuranceCoverageInformation/OI06_ReleaseofInformationCode/text()"" />
                    <ns0:SEC_RELEASE_INFO_CODE>
                      <xsl:value-of select=""$var:v320"" />
                    </ns0:SEC_RELEASE_INFO_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v321"" select=""position()"" />
                <xsl:variable name=""var:v322"" select=""userCSharp:LogicalEq(string($var:v321) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v322"">
                  <xsl:variable name=""var:v323"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM103_OtherInsuredLastName))"" />
                  <xsl:if test=""string($var:v323)='true'"">
                    <xsl:variable name=""var:v324"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM103_OtherInsuredLastName/text()"" />
                    <ns0:SEC_INSURED_LNAME>
                      <xsl:value-of select=""$var:v324"" />
                    </ns0:SEC_INSURED_LNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v325"" select=""position()"" />
                <xsl:variable name=""var:v326"" select=""userCSharp:LogicalEq(string($var:v325) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v326"">
                  <xsl:variable name=""var:v327"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM104_OtherInsuredFirstName))"" />
                  <xsl:if test=""string($var:v327)='true'"">
                    <xsl:variable name=""var:v328"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM104_OtherInsuredFirstName/text()"" />
                    <ns0:SEC_INSURED_FNAME>
                      <xsl:value-of select=""$var:v328"" />
                    </ns0:SEC_INSURED_FNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v329"" select=""position()"" />
                <xsl:variable name=""var:v330"" select=""userCSharp:LogicalEq(string($var:v329) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v330"">
                  <xsl:variable name=""var:v331"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM105_OtherInsuredMiddleName))"" />
                  <xsl:if test=""string($var:v331)='true'"">
                    <xsl:variable name=""var:v332"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM105_OtherInsuredMiddleName/text()"" />
                    <ns0:SEC_INSURED_MNAME>
                      <xsl:value-of select=""$var:v332"" />
                    </ns0:SEC_INSURED_MNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v333"" select=""position()"" />
                <xsl:variable name=""var:v334"" select=""userCSharp:LogicalEq(string($var:v333) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v334"">
                  <xsl:variable name=""var:v335"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM107_OtherInsuredNameSuffix))"" />
                  <xsl:if test=""string($var:v335)='true'"">
                    <xsl:variable name=""var:v336"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM107_OtherInsuredNameSuffix/text()"" />
                    <ns0:SEC_INSURED_SUFFIX>
                      <xsl:value-of select=""$var:v336"" />
                    </ns0:SEC_INSURED_SUFFIX>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v337"" select=""position()"" />
                <xsl:variable name=""var:v338"" select=""userCSharp:LogicalEq(string($var:v337) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v338"">
                  <xsl:variable name=""var:v339"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM108_IdentificationCodeQualifier))"" />
                  <xsl:if test=""string($var:v339)='true'"">
                    <xsl:variable name=""var:v340"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM108_IdentificationCodeQualifier/text()"" />
                    <ns0:SEC_INSURED_ID_QUAL>
                      <xsl:value-of select=""$var:v340"" />
                    </ns0:SEC_INSURED_ID_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v341"" select=""position()"" />
                <xsl:variable name=""var:v342"" select=""userCSharp:LogicalEq(string($var:v341) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v342"">
                  <xsl:variable name=""var:v343"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM109_OtherInsuredIdentifier))"" />
                  <xsl:if test=""string($var:v343)='true'"">
                    <xsl:variable name=""var:v344"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM109_OtherInsuredIdentifier/text()"" />
                    <ns0:SEC_INSURED_ID>
                      <xsl:value-of select=""$var:v344"" />
                    </ns0:SEC_INSURED_ID>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v345"" select=""position()"" />
                <xsl:variable name=""var:v346"" select=""userCSharp:LogicalEq(string($var:v345) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v346"">
                  <xsl:variable name=""var:v347"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM103_OtherPayerOrganizationName))"" />
                  <xsl:if test=""string($var:v347)='true'"">
                    <xsl:variable name=""var:v348"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM103_OtherPayerOrganizationName/text()"" />
                    <ns0:SEC_PAYER_NAME>
                      <xsl:value-of select=""$var:v348"" />
                    </ns0:SEC_PAYER_NAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v349"" select=""position()"" />
                <xsl:variable name=""var:v350"" select=""userCSharp:LogicalEq(string($var:v349) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v350"">
                  <xsl:variable name=""var:v351"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM109_OtherPayerPrimaryIdentifier))"" />
                  <xsl:if test=""string($var:v351)='true'"">
                    <xsl:variable name=""var:v352"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM109_OtherPayerPrimaryIdentifier/text()"" />
                    <ns0:SEC_PAYER_ID>
                      <xsl:value-of select=""$var:v352"" />
                    </ns0:SEC_PAYER_ID>
                  </xsl:if>
                </xsl:if>
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
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v353"" select=""position()"" />
                <xsl:variable name=""var:v354"" select=""userCSharp:LogicalEq(string($var:v353) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v354"">
                  <xsl:variable name=""var:v355"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N301_OtherInsuredAddressLine))"" />
                  <xsl:if test=""string($var:v355)='true'"">
                    <xsl:variable name=""var:v356"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N301_OtherInsuredAddressLine/text()"" />
                    <ns0:SEC_INSURED_ADD1>
                      <xsl:value-of select=""$var:v356"" />
                    </ns0:SEC_INSURED_ADD1>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v357"" select=""position()"" />
                <xsl:variable name=""var:v358"" select=""userCSharp:LogicalEq(string($var:v357) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v358"">
                  <xsl:variable name=""var:v359"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N302_OtherInsuredAddressLine))"" />
                  <xsl:if test=""string($var:v359)='true'"">
                    <xsl:variable name=""var:v360"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N302_OtherInsuredAddressLine/text()"" />
                    <ns0:SEC_INSURED_ADD2>
                      <xsl:value-of select=""$var:v360"" />
                    </ns0:SEC_INSURED_ADD2>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v361"" select=""position()"" />
                <xsl:variable name=""var:v362"" select=""userCSharp:LogicalEq(string($var:v361) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v362"">
                  <xsl:variable name=""var:v363"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N401_OtherSubscriberCityName))"" />
                  <xsl:if test=""string($var:v363)='true'"">
                    <xsl:variable name=""var:v364"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N401_OtherSubscriberCityName/text()"" />
                    <ns0:SEC_INSURED_CITY>
                      <xsl:value-of select=""$var:v364"" />
                    </ns0:SEC_INSURED_CITY>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v365"" select=""position()"" />
                <xsl:variable name=""var:v366"" select=""userCSharp:LogicalEq(string($var:v365) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v366"">
                  <xsl:variable name=""var:v367"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N402_OtherSubscriberStateorProvinceCode))"" />
                  <xsl:if test=""string($var:v367)='true'"">
                    <xsl:variable name=""var:v368"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N402_OtherSubscriberStateorProvinceCode/text()"" />
                    <ns0:SEC_INSURED_STATE>
                      <xsl:value-of select=""$var:v368"" />
                    </ns0:SEC_INSURED_STATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v369"" select=""position()"" />
                <xsl:variable name=""var:v370"" select=""userCSharp:LogicalEq(string($var:v369) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v370"">
                  <xsl:variable name=""var:v371"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N403_OtherSubscriberPostalZoneorZIPCode))"" />
                  <xsl:if test=""string($var:v371)='true'"">
                    <xsl:variable name=""var:v372"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N403_OtherSubscriberPostalZoneorZIPCode/text()"" />
                    <ns0:SEC_INSURED_ZIP>
                      <xsl:value-of select=""$var:v372"" />
                    </ns0:SEC_INSURED_ZIP>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v373"" select=""position()"" />
                <xsl:variable name=""var:v374"" select=""userCSharp:LogicalEq(string($var:v373) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v374"">
                  <xsl:variable name=""var:v375"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments/CAS01_ClaimAdjustmentGroupCode))"" />
                  <xsl:if test=""string($var:v375)='true'"">
                    <xsl:variable name=""var:v376"" select=""s1:CAS_ClaimLevelAdjustments/CAS01_ClaimAdjustmentGroupCode/text()"" />
                    <ns0:SEC_CAS01_CODE>
                      <xsl:value-of select=""$var:v376"" />
                    </ns0:SEC_CAS01_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v377"" select=""position()"" />
                <xsl:variable name=""var:v378"" select=""userCSharp:LogicalEq(string($var:v377) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v378"">
                  <xsl:variable name=""var:v379"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments/CAS02_AdjustmentReasonCode))"" />
                  <xsl:if test=""string($var:v379)='true'"">
                    <xsl:variable name=""var:v380"" select=""s1:CAS_ClaimLevelAdjustments/CAS02_AdjustmentReasonCode/text()"" />
                    <ns0:SEC_CAS02_REASON>
                      <xsl:value-of select=""$var:v380"" />
                    </ns0:SEC_CAS02_REASON>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v381"" select=""position()"" />
                <xsl:variable name=""var:v382"" select=""userCSharp:LogicalEq(string($var:v381) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v382"">
                  <xsl:variable name=""var:v383"" select=""userCSharp:LogicalExistence(boolean(s1:CAS_ClaimLevelAdjustments/CAS03_AdjustmentAmount))"" />
                  <xsl:if test=""string($var:v383)='true'"">
                    <xsl:variable name=""var:v384"" select=""s1:CAS_ClaimLevelAdjustments/CAS03_AdjustmentAmount/text()"" />
                    <ns0:SEC_CAS03_AMT>
                      <xsl:value-of select=""$var:v384"" />
                    </ns0:SEC_CAS03_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v385"" select=""position()"" />
                <xsl:variable name=""var:v386"" select=""userCSharp:LogicalEq(string($var:v385) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v386"">
                  <xsl:variable name=""var:v387"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount))"" />
                  <xsl:if test=""string($var:v387)='true'"">
                    <xsl:variable name=""var:v388"" select=""s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()"" />
                    <ns0:SEC_PAYERPAID_AMT>
                      <xsl:value-of select=""$var:v388"" />
                    </ns0:SEC_PAYERPAID_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v389"" select=""position()"" />
                <xsl:variable name=""var:v390"" select=""userCSharp:LogicalEq(string($var:v389) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v390"">
                  <xsl:variable name=""var:v391"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount))"" />
                  <xsl:if test=""string($var:v391)='true'"">
                    <xsl:variable name=""var:v392"" select=""s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount/text()"" />
                    <ns0:SEC_NONCOVERED_AMT>
                      <xsl:value-of select=""$var:v392"" />
                    </ns0:SEC_NONCOVERED_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v393"" select=""position()"" />
                <xsl:variable name=""var:v394"" select=""userCSharp:LogicalEq(string($var:v393) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v394"">
                  <xsl:variable name=""var:v395"" select=""userCSharp:LogicalExistence(boolean(s1:AMT_SubLoop/s1:AMT_RemainingPatientLiability/AMT02_RemainingPatientLiability))"" />
                  <xsl:if test=""string($var:v395)='true'"">
                    <xsl:variable name=""var:v396"" select=""s1:AMT_SubLoop/s1:AMT_RemainingPatientLiability/AMT02_RemainingPatientLiability/text()"" />
                    <ns0:SEC_LIABILITY_AMT>
                      <xsl:value-of select=""$var:v396"" />
                    </ns0:SEC_LIABILITY_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v397"" select=""position()"" />
                <xsl:variable name=""var:v398"" select=""userCSharp:LogicalEq(string($var:v397) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v398"">
                  <xsl:variable name=""var:v399"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:REF_OtherSubscriberSecondaryIdentification/REF02_OtherInsuredAdditionalIdentifier))"" />
                  <xsl:if test=""string($var:v399)='true'"">
                    <xsl:variable name=""var:v400"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:REF_OtherSubscriberSecondaryIdentification/REF02_OtherInsuredAdditionalIdentifier/text()"" />
                    <ns0:SEC_INSURED_SSN_REF>
                      <xsl:value-of select=""$var:v400"" />
                    </ns0:SEC_INSURED_SSN_REF>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v401"" select=""position()"" />
                <xsl:variable name=""var:v402"" select=""userCSharp:LogicalEq(string($var:v401) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v402"">
                  <xsl:variable name=""var:v403"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N301_OtherPayerAddressLine))"" />
                  <xsl:if test=""string($var:v403)='true'"">
                    <xsl:variable name=""var:v404"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N301_OtherPayerAddressLine/text()"" />
                    <ns0:SEC_PAYER_ADD1>
                      <xsl:value-of select=""$var:v404"" />
                    </ns0:SEC_PAYER_ADD1>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v405"" select=""position()"" />
                <xsl:variable name=""var:v406"" select=""userCSharp:LogicalEq(string($var:v405) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v406"">
                  <xsl:variable name=""var:v407"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N302_OtherPayerAddressLine))"" />
                  <xsl:if test=""string($var:v407)='true'"">
                    <xsl:variable name=""var:v408"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N302_OtherPayerAddressLine/text()"" />
                    <ns0:SEC_PAYER_ADD2>
                      <xsl:value-of select=""$var:v408"" />
                    </ns0:SEC_PAYER_ADD2>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v409"" select=""position()"" />
                <xsl:variable name=""var:v410"" select=""userCSharp:LogicalEq(string($var:v409) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v410"">
                  <xsl:variable name=""var:v411"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N401_OtherPayerCityName))"" />
                  <xsl:if test=""string($var:v411)='true'"">
                    <xsl:variable name=""var:v412"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N401_OtherPayerCityName/text()"" />
                    <ns0:SEC_PAYER_CITY>
                      <xsl:value-of select=""$var:v412"" />
                    </ns0:SEC_PAYER_CITY>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v413"" select=""position()"" />
                <xsl:variable name=""var:v414"" select=""userCSharp:LogicalEq(string($var:v413) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v414"">
                  <xsl:variable name=""var:v415"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N402_OtherPayerStateorProvinceCode))"" />
                  <xsl:if test=""string($var:v415)='true'"">
                    <xsl:variable name=""var:v416"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N402_OtherPayerStateorProvinceCode/text()"" />
                    <ns0:SEC_PAYER_STATE>
                      <xsl:value-of select=""$var:v416"" />
                    </ns0:SEC_PAYER_STATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v417"" select=""position()"" />
                <xsl:variable name=""var:v418"" select=""userCSharp:LogicalEq(string($var:v417) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v418"">
                  <xsl:variable name=""var:v419"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N403_OtherPayerPostalZoneorZIPCode))"" />
                  <xsl:if test=""string($var:v419)='true'"">
                    <xsl:variable name=""var:v420"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N403_OtherPayerPostalZoneorZIPCode/text()"" />
                    <ns0:SEC_PAYER_ZIPCODE>
                      <xsl:value-of select=""$var:v420"" />
                    </ns0:SEC_PAYER_ZIPCODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v421"" select=""position()"" />
                <xsl:variable name=""var:v422"" select=""userCSharp:LogicalEq(string($var:v421) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v422"">
                  <xsl:variable name=""var:v423"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate))"" />
                  <xsl:if test=""string($var:v423)='true'"">
                    <xsl:variable name=""var:v424"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate/text()"" />
                    <ns0:SEC_PAYER_REMITTANCE_DATE>
                      <xsl:value-of select=""$var:v424"" />
                    </ns0:SEC_PAYER_REMITTANCE_DATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v425"" select=""position()"" />
                <xsl:variable name=""var:v426"" select=""userCSharp:LogicalEq(string($var:v425) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v426"">
                  <xsl:variable name=""var:v427"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v428"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[1]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v429"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v430"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[2]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v431"" select=""userCSharp:StringConcat(string($var:v427) , &quot;:&quot; , string($var:v428) , &quot;,&quot; , string($var:v429) , &quot;:&quot; , string($var:v430) , &quot;,&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerPriorAuthorizationNumber/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerPriorAuthorizationNumber/REF02_OtherPayerPriorAuthorizationNumber/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerReferralNumber/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerReferralNumber/REF02_OtherPayerPriorAuthorizationorReferralNumber/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimAdjustmentIndicator/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimAdjustmentIndicator/REF02_OtherPayerClaimAdjustmentIndicator/text()) , &quot;,&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimControlNumber/REF01_ReferenceIdentificationQualifier/text()) , &quot;:&quot; , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimControlNumber/REF02_OtherPayer_sClaimControlNumber/text()) , &quot;,&quot;)"" />
                  <ns0:SEC_PAYER_REF>
                    <xsl:value-of select=""$var:v431"" />
                  </ns0:SEC_PAYER_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v432"" select=""position()"" />
                <xsl:variable name=""var:v433"" select=""userCSharp:LogicalEq(string($var:v432) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v433"">
                  <xsl:variable name=""var:v434"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:NM1_OtherPayerReferringProvider/NM102_EntityTypeQualifier))"" />
                  <xsl:if test=""string($var:v434)='true'"">
                    <xsl:variable name=""var:v435"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:NM1_OtherPayerReferringProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:SEC_INSURED_REFERING_QUAL>
                      <xsl:value-of select=""$var:v435"" />
                    </ns0:SEC_INSURED_REFERING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v436"" select=""position()"" />
                <xsl:variable name=""var:v437"" select=""userCSharp:LogicalEq(string($var:v436) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v437"">
                  <xsl:variable name=""var:v438"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v439"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[1]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v440"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v441"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[2]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v442"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v443"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[3]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v444"" select=""userCSharp:StringConcat(string($var:v438) , &quot;:&quot; , string($var:v439) , &quot;,&quot; , string($var:v440) , &quot;:&quot; , string($var:v441) , &quot;,&quot; , string($var:v442) , &quot;:&quot; , string($var:v443) , &quot;,&quot;)"" />
                  <ns0:SEC_INSURED_REFERING_REF>
                    <xsl:value-of select=""$var:v444"" />
                  </ns0:SEC_INSURED_REFERING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v445"" select=""position()"" />
                <xsl:variable name=""var:v446"" select=""userCSharp:LogicalEq(string($var:v445) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v446"">
                  <xsl:variable name=""var:v447"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:NM1_OtherPayerRenderingProvider/NM102_EntityTypeQualifier))"" />
                  <xsl:if test=""string($var:v447)='true'"">
                    <xsl:variable name=""var:v448"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:NM1_OtherPayerRenderingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:SEC_INSURED_RENDERING_QUAL>
                      <xsl:value-of select=""$var:v448"" />
                    </ns0:SEC_INSURED_RENDERING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v449"" select=""position()"" />
                <xsl:variable name=""var:v450"" select=""userCSharp:LogicalEq(string($var:v449) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v450"">
                  <xsl:variable name=""var:v451"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v452"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[1]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v453"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v454"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[2]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v455"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v456"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[3]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v457"" select=""userCSharp:StringConcat(string($var:v451) , &quot;:&quot; , string($var:v452) , &quot;,&quot; , string($var:v453) , &quot;:&quot; , string($var:v454) , &quot;,&quot; , string($var:v455) , &quot;:&quot; , string($var:v456) , &quot;,&quot;)"" />
                  <ns0:SEC_INSURED_RENDERING_REF>
                    <xsl:value-of select=""$var:v457"" />
                  </ns0:SEC_INSURED_RENDERING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v458"" select=""position()"" />
                <xsl:variable name=""var:v459"" select=""userCSharp:LogicalEq(string($var:v458) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v459"">
                  <xsl:variable name=""var:v460"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:NM1_OtherPayerServiceFacilityLocation/NM102_EntityTypeQualifier))"" />
                  <xsl:if test=""string($var:v460)='true'"">
                    <xsl:variable name=""var:v461"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:NM1_OtherPayerServiceFacilityLocation/NM102_EntityTypeQualifier/text()"" />
                    <ns0:SEC_INSURED_SERVICEFACILITY_QUAL>
                      <xsl:value-of select=""$var:v461"" />
                    </ns0:SEC_INSURED_SERVICEFACILITY_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v462"" select=""position()"" />
                <xsl:variable name=""var:v463"" select=""userCSharp:LogicalEq(string($var:v462) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v463"">
                  <xsl:variable name=""var:v464"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v465"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[1]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v466"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v467"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[2]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v468"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v469"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[3]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v470"" select=""userCSharp:StringConcat(string($var:v464) , &quot;:&quot; , string($var:v465) , &quot;,&quot; , string($var:v466) , &quot;:&quot; , string($var:v467) , &quot;,&quot; , string($var:v468) , &quot;:&quot; , string($var:v469) , &quot;,&quot;)"" />
                  <ns0:SEC_INSURED_SERVICEFACILITY_REF>
                    <xsl:value-of select=""$var:v470"" />
                  </ns0:SEC_INSURED_SERVICEFACILITY_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v471"" select=""position()"" />
                <xsl:variable name=""var:v472"" select=""userCSharp:LogicalEq(string($var:v471) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v472"">
                  <xsl:variable name=""var:v473"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:NM1_OtherPayerSupervisingProvider/NM102_EntityTypeQualifier))"" />
                  <xsl:if test=""string($var:v473)='true'"">
                    <xsl:variable name=""var:v474"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:NM1_OtherPayerSupervisingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:SEC_INSURED_SUPERVISING_QUAL>
                      <xsl:value-of select=""$var:v474"" />
                    </ns0:SEC_INSURED_SUPERVISING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v475"" select=""position()"" />
                <xsl:variable name=""var:v476"" select=""userCSharp:LogicalEq(string($var:v475) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v476"">
                  <xsl:variable name=""var:v477"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v478"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[1]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v479"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v480"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[2]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v481"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v482"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[3]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v483"" select=""userCSharp:StringConcat(string($var:v477) , &quot;:&quot; , string($var:v478) , &quot;,&quot; , string($var:v479) , &quot;:&quot; , string($var:v480) , &quot;,&quot; , string($var:v481) , &quot;:&quot; , string($var:v482) , &quot;,&quot;)"" />
                  <ns0:SEC_INSURED_SUPERVISING_REF>
                    <xsl:value-of select=""$var:v483"" />
                  </ns0:SEC_INSURED_SUPERVISING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v484"" select=""position()"" />
                <xsl:variable name=""var:v485"" select=""userCSharp:LogicalEq(string($var:v484) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v485"">
                  <xsl:variable name=""var:v486"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:NM1_OtherPayerBillingProvider/NM102_EntityTypeQualifier))"" />
                  <xsl:if test=""string($var:v486)='true'"">
                    <xsl:variable name=""var:v487"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:NM1_OtherPayerBillingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:SEC_INSURED_BILLING_QUAL>
                      <xsl:value-of select=""$var:v487"" />
                    </ns0:SEC_INSURED_BILLING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v488"" select=""position()"" />
                <xsl:variable name=""var:v489"" select=""userCSharp:LogicalEq(string($var:v488) , &quot;1&quot;)"" />
                <xsl:if test=""$var:v489"">
                  <xsl:variable name=""var:v490"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v491"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[1]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v492"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v493"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[2]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v494"" select=""userCSharp:StringConcat(string($var:v490) , &quot;:&quot; , string($var:v491) , &quot;,&quot; , string($var:v492) , &quot;:&quot; , string($var:v493) , &quot;,&quot;)"" />
                  <ns0:SEC_INSURED_BILLING_REF>
                    <xsl:value-of select=""$var:v494"" />
                  </ns0:SEC_INSURED_BILLING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v495"" select=""position()"" />
                <xsl:variable name=""var:v496"" select=""userCSharp:LogicalEq(string($var:v495) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v496"">
                  <xsl:variable name=""var:v497"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode)"" />
                  <xsl:variable name=""var:v498"" select=""userCSharp:LogicalExistence($var:v497)"" />
                  <xsl:if test=""string($var:v498)='true'"">
                    <xsl:variable name=""var:v499"" select=""s1:SBR_OtherSubscriberInformation/SBR01_PayerResponsibilitySequenceNumberCode/text()"" />
                    <ns0:TRI_SEQ_NUMBER>
                      <xsl:value-of select=""$var:v499"" />
                    </ns0:TRI_SEQ_NUMBER>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v500"" select=""position()"" />
                <xsl:variable name=""var:v501"" select=""userCSharp:LogicalEq(string($var:v500) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v501"">
                  <xsl:variable name=""var:v502"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR02_IndividualRelationshipCode)"" />
                  <xsl:variable name=""var:v503"" select=""userCSharp:LogicalExistence($var:v502)"" />
                  <xsl:if test=""string($var:v503)='true'"">
                    <xsl:variable name=""var:v504"" select=""s1:SBR_OtherSubscriberInformation/SBR02_IndividualRelationshipCode/text()"" />
                    <ns0:TRI_RELATION_CODE>
                      <xsl:value-of select=""$var:v504"" />
                    </ns0:TRI_RELATION_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v505"" select=""position()"" />
                <xsl:variable name=""var:v506"" select=""userCSharp:LogicalEq(string($var:v505) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v506"">
                  <xsl:variable name=""var:v507"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR03_InsuredGrouporPolicyNumber)"" />
                  <xsl:variable name=""var:v508"" select=""userCSharp:LogicalExistence($var:v507)"" />
                  <xsl:if test=""string($var:v508)='true'"">
                    <xsl:variable name=""var:v509"" select=""s1:SBR_OtherSubscriberInformation/SBR03_InsuredGrouporPolicyNumber/text()"" />
                    <ns0:TRI_GROUP_ID>
                      <xsl:value-of select=""$var:v509"" />
                    </ns0:TRI_GROUP_ID>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v510"" select=""position()"" />
                <xsl:variable name=""var:v511"" select=""userCSharp:LogicalEq(string($var:v510) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v511"">
                  <xsl:variable name=""var:v512"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR04_OtherInsuredGroupName)"" />
                  <xsl:variable name=""var:v513"" select=""userCSharp:LogicalExistence($var:v512)"" />
                  <xsl:if test=""string($var:v513)='true'"">
                    <xsl:variable name=""var:v514"" select=""s1:SBR_OtherSubscriberInformation/SBR04_OtherInsuredGroupName/text()"" />
                    <ns0:TRI_GROUP_NAME>
                      <xsl:value-of select=""$var:v514"" />
                    </ns0:TRI_GROUP_NAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v515"" select=""position()"" />
                <xsl:variable name=""var:v516"" select=""userCSharp:LogicalEq(string($var:v515) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v516"">
                  <xsl:variable name=""var:v517"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR09_ClaimFilingIndicatorCode)"" />
                  <xsl:variable name=""var:v518"" select=""userCSharp:LogicalExistence($var:v517)"" />
                  <xsl:if test=""string($var:v518)='true'"">
                    <xsl:variable name=""var:v519"" select=""s1:SBR_OtherSubscriberInformation/SBR09_ClaimFilingIndicatorCode/text()"" />
                    <ns0:TRI_CLAIM_IND>
                      <xsl:value-of select=""$var:v519"" />
                    </ns0:TRI_CLAIM_IND>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v520"" select=""position()"" />
                <xsl:variable name=""var:v521"" select=""userCSharp:LogicalEq(string($var:v520) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v521"">
                  <xsl:variable name=""var:v522"" select=""boolean(s1:SBR_OtherSubscriberInformation/SBR05_InsuranceTypeCode)"" />
                  <xsl:variable name=""var:v523"" select=""userCSharp:LogicalExistence($var:v522)"" />
                  <xsl:if test=""string($var:v523)='true'"">
                    <xsl:variable name=""var:v524"" select=""s1:SBR_OtherSubscriberInformation/SBR05_InsuranceTypeCode/text()"" />
                    <ns0:TRI_INS_TYPE_CODE>
                      <xsl:value-of select=""$var:v524"" />
                    </ns0:TRI_INS_TYPE_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v525"" select=""position()"" />
                <xsl:variable name=""var:v526"" select=""userCSharp:LogicalEq(string($var:v525) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v526"">
                  <xsl:variable name=""var:v527"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation/OI03_BenefitsAssignmentCertificationIndicator)"" />
                  <xsl:variable name=""var:v528"" select=""userCSharp:LogicalExistence($var:v527)"" />
                  <xsl:if test=""string($var:v528)='true'"">
                    <xsl:variable name=""var:v529"" select=""s1:OI_OtherInsuranceCoverageInformation/OI03_BenefitsAssignmentCertificationIndicator/text()"" />
                    <ns0:TRI_ASSIGN_BENRFIT_IND>
                      <xsl:value-of select=""$var:v529"" />
                    </ns0:TRI_ASSIGN_BENRFIT_IND>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v530"" select=""position()"" />
                <xsl:variable name=""var:v531"" select=""userCSharp:LogicalEq(string($var:v530) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v531"">
                  <xsl:variable name=""var:v532"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation/OI04_PatientSignatureSourceCode)"" />
                  <xsl:variable name=""var:v533"" select=""userCSharp:LogicalExistence($var:v532)"" />
                  <xsl:if test=""string($var:v533)='true'"">
                    <xsl:variable name=""var:v534"" select=""s1:OI_OtherInsuranceCoverageInformation/OI04_PatientSignatureSourceCode/text()"" />
                    <ns0:TRI_PAT_SIGN_SRC_CODE>
                      <xsl:value-of select=""$var:v534"" />
                    </ns0:TRI_PAT_SIGN_SRC_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v535"" select=""position()"" />
                <xsl:variable name=""var:v536"" select=""userCSharp:LogicalEq(string($var:v535) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v536"">
                  <xsl:variable name=""var:v537"" select=""boolean(s1:OI_OtherInsuranceCoverageInformation/OI06_ReleaseofInformationCode)"" />
                  <xsl:variable name=""var:v538"" select=""userCSharp:LogicalExistence($var:v537)"" />
                  <xsl:if test=""string($var:v538)='true'"">
                    <xsl:variable name=""var:v539"" select=""s1:OI_OtherInsuranceCoverageInformation/OI06_ReleaseofInformationCode/text()"" />
                    <ns0:TRI_RELEASE_INFO_CODE>
                      <xsl:value-of select=""$var:v539"" />
                    </ns0:TRI_RELEASE_INFO_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v540"" select=""position()"" />
                <xsl:variable name=""var:v541"" select=""userCSharp:LogicalEq(string($var:v540) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v541"">
                  <xsl:variable name=""var:v542"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM103_OtherInsuredLastName)"" />
                  <xsl:variable name=""var:v543"" select=""userCSharp:LogicalExistence($var:v542)"" />
                  <xsl:if test=""string($var:v543)='true'"">
                    <xsl:variable name=""var:v544"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM103_OtherInsuredLastName/text()"" />
                    <ns0:TRI_INSURED_LNAME>
                      <xsl:value-of select=""$var:v544"" />
                    </ns0:TRI_INSURED_LNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v545"" select=""position()"" />
                <xsl:variable name=""var:v546"" select=""userCSharp:LogicalEq(string($var:v545) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v546"">
                  <xsl:variable name=""var:v547"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM104_OtherInsuredFirstName)"" />
                  <xsl:variable name=""var:v548"" select=""userCSharp:LogicalExistence($var:v547)"" />
                  <xsl:if test=""string($var:v548)='true'"">
                    <xsl:variable name=""var:v549"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM104_OtherInsuredFirstName/text()"" />
                    <ns0:TRI_INSURED_FNAME>
                      <xsl:value-of select=""$var:v549"" />
                    </ns0:TRI_INSURED_FNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v550"" select=""position()"" />
                <xsl:variable name=""var:v551"" select=""userCSharp:LogicalEq(string($var:v550) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v551"">
                  <xsl:variable name=""var:v552"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM105_OtherInsuredMiddleName)"" />
                  <xsl:variable name=""var:v553"" select=""userCSharp:LogicalExistence($var:v552)"" />
                  <xsl:if test=""string($var:v553)='true'"">
                    <xsl:variable name=""var:v554"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM105_OtherInsuredMiddleName/text()"" />
                    <ns0:TRI_INSURED_MNAME>
                      <xsl:value-of select=""$var:v554"" />
                    </ns0:TRI_INSURED_MNAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v555"" select=""position()"" />
                <xsl:variable name=""var:v556"" select=""userCSharp:LogicalEq(string($var:v555) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v556"">
                  <xsl:variable name=""var:v557"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM107_OtherInsuredNameSuffix)"" />
                  <xsl:variable name=""var:v558"" select=""userCSharp:LogicalExistence($var:v557)"" />
                  <xsl:if test=""string($var:v558)='true'"">
                    <xsl:variable name=""var:v559"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM107_OtherInsuredNameSuffix/text()"" />
                    <ns0:TRI_INSURED_SUFFIX>
                      <xsl:value-of select=""$var:v559"" />
                    </ns0:TRI_INSURED_SUFFIX>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v560"" select=""position()"" />
                <xsl:variable name=""var:v561"" select=""userCSharp:LogicalEq(string($var:v560) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v561"">
                  <xsl:variable name=""var:v562"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM108_IdentificationCodeQualifier)"" />
                  <xsl:variable name=""var:v563"" select=""userCSharp:LogicalExistence($var:v562)"" />
                  <xsl:if test=""string($var:v563)='true'"">
                    <xsl:variable name=""var:v564"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM108_IdentificationCodeQualifier/text()"" />
                    <ns0:TRI_INSURED_ID_QUAL>
                      <xsl:value-of select=""$var:v564"" />
                    </ns0:TRI_INSURED_ID_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v565"" select=""position()"" />
                <xsl:variable name=""var:v566"" select=""userCSharp:LogicalEq(string($var:v565) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v566"">
                  <xsl:variable name=""var:v567"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM109_OtherInsuredIdentifier)"" />
                  <xsl:variable name=""var:v568"" select=""userCSharp:LogicalExistence($var:v567)"" />
                  <xsl:if test=""string($var:v568)='true'"">
                    <xsl:variable name=""var:v569"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:NM1_OtherSubscriberName/NM109_OtherInsuredIdentifier/text()"" />
                    <ns0:TRI_INSURED_ID>
                      <xsl:value-of select=""$var:v569"" />
                    </ns0:TRI_INSURED_ID>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v570"" select=""position()"" />
                <xsl:variable name=""var:v571"" select=""userCSharp:LogicalEq(string($var:v570) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v571"">
                  <xsl:variable name=""var:v572"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM103_OtherPayerOrganizationName)"" />
                  <xsl:variable name=""var:v573"" select=""userCSharp:LogicalExistence($var:v572)"" />
                  <xsl:if test=""string($var:v573)='true'"">
                    <xsl:variable name=""var:v574"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM103_OtherPayerOrganizationName/text()"" />
                    <ns0:TRI_PAYER_NAME>
                      <xsl:value-of select=""$var:v574"" />
                    </ns0:TRI_PAYER_NAME>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v575"" select=""position()"" />
                <xsl:variable name=""var:v576"" select=""userCSharp:LogicalEq(string($var:v575) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v576"">
                  <xsl:variable name=""var:v577"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM109_OtherPayerPrimaryIdentifier)"" />
                  <xsl:variable name=""var:v578"" select=""userCSharp:LogicalExistence($var:v577)"" />
                  <xsl:if test=""string($var:v578)='true'"">
                    <xsl:variable name=""var:v579"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:NM1_OtherPayerName/NM109_OtherPayerPrimaryIdentifier/text()"" />
                    <ns0:TRI_PAYER_ID>
                      <xsl:value-of select=""$var:v579"" />
                    </ns0:TRI_PAYER_ID>
                  </xsl:if>
                </xsl:if>
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
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v580"" select=""position()"" />
                <xsl:variable name=""var:v581"" select=""userCSharp:LogicalEq(string($var:v580) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v581"">
                  <xsl:variable name=""var:v582"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N301_OtherInsuredAddressLine)"" />
                  <xsl:variable name=""var:v583"" select=""userCSharp:LogicalExistence($var:v582)"" />
                  <xsl:if test=""string($var:v583)='true'"">
                    <xsl:variable name=""var:v584"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N301_OtherInsuredAddressLine/text()"" />
                    <ns0:TRI_INSURED_ADD1>
                      <xsl:value-of select=""$var:v584"" />
                    </ns0:TRI_INSURED_ADD1>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v585"" select=""position()"" />
                <xsl:variable name=""var:v586"" select=""userCSharp:LogicalEq(string($var:v585) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v586"">
                  <xsl:variable name=""var:v587"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N302_OtherInsuredAddressLine)"" />
                  <xsl:variable name=""var:v588"" select=""userCSharp:LogicalExistence($var:v587)"" />
                  <xsl:if test=""string($var:v588)='true'"">
                    <xsl:variable name=""var:v589"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N3_OtherSubscriberAddress/N302_OtherInsuredAddressLine/text()"" />
                    <ns0:TRI_INSURED_ADD2>
                      <xsl:value-of select=""$var:v589"" />
                    </ns0:TRI_INSURED_ADD2>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v590"" select=""position()"" />
                <xsl:variable name=""var:v591"" select=""userCSharp:LogicalEq(string($var:v590) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v591"">
                  <xsl:variable name=""var:v592"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N401_OtherSubscriberCityName)"" />
                  <xsl:variable name=""var:v593"" select=""userCSharp:LogicalExistence($var:v592)"" />
                  <xsl:if test=""string($var:v593)='true'"">
                    <xsl:variable name=""var:v594"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N401_OtherSubscriberCityName/text()"" />
                    <ns0:TRI_INSURED_CITY>
                      <xsl:value-of select=""$var:v594"" />
                    </ns0:TRI_INSURED_CITY>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v595"" select=""position()"" />
                <xsl:variable name=""var:v596"" select=""userCSharp:LogicalEq(string($var:v595) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v596"">
                  <xsl:variable name=""var:v597"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N402_OtherSubscriberStateorProvinceCode)"" />
                  <xsl:variable name=""var:v598"" select=""userCSharp:LogicalExistence($var:v597)"" />
                  <xsl:if test=""string($var:v598)='true'"">
                    <xsl:variable name=""var:v599"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N402_OtherSubscriberStateorProvinceCode/text()"" />
                    <ns0:TRI_INSURED_STATE>
                      <xsl:value-of select=""$var:v599"" />
                    </ns0:TRI_INSURED_STATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v600"" select=""position()"" />
                <xsl:variable name=""var:v601"" select=""userCSharp:LogicalEq(string($var:v600) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v601"">
                  <xsl:variable name=""var:v602"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N403_OtherSubscriberPostalZoneorZIPCode)"" />
                  <xsl:variable name=""var:v603"" select=""userCSharp:LogicalExistence($var:v602)"" />
                  <xsl:if test=""string($var:v603)='true'"">
                    <xsl:variable name=""var:v604"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:N4_OtherSubscriberCity_State_ZIPCode/N403_OtherSubscriberPostalZoneorZIPCode/text()"" />
                    <ns0:TRI_INSURED_ZIP>
                      <xsl:value-of select=""$var:v604"" />
                    </ns0:TRI_INSURED_ZIP>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v605"" select=""position()"" />
                <xsl:variable name=""var:v606"" select=""userCSharp:LogicalEq(string($var:v605) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v606"">
                  <xsl:variable name=""var:v607"" select=""boolean(s1:CAS_ClaimLevelAdjustments/CAS01_ClaimAdjustmentGroupCode)"" />
                  <xsl:variable name=""var:v608"" select=""userCSharp:LogicalExistence($var:v607)"" />
                  <xsl:if test=""string($var:v608)='true'"">
                    <xsl:variable name=""var:v609"" select=""s1:CAS_ClaimLevelAdjustments/CAS01_ClaimAdjustmentGroupCode/text()"" />
                    <ns0:TRI_CAS01_CODE>
                      <xsl:value-of select=""$var:v609"" />
                    </ns0:TRI_CAS01_CODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v610"" select=""position()"" />
                <xsl:variable name=""var:v611"" select=""userCSharp:LogicalEq(string($var:v610) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v611"">
                  <xsl:variable name=""var:v612"" select=""boolean(s1:CAS_ClaimLevelAdjustments/CAS02_AdjustmentReasonCode)"" />
                  <xsl:variable name=""var:v613"" select=""userCSharp:LogicalExistence($var:v612)"" />
                  <xsl:if test=""string($var:v613)='true'"">
                    <xsl:variable name=""var:v614"" select=""s1:CAS_ClaimLevelAdjustments/CAS02_AdjustmentReasonCode/text()"" />
                    <ns0:TRI_CAS02_REASON>
                      <xsl:value-of select=""$var:v614"" />
                    </ns0:TRI_CAS02_REASON>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v615"" select=""position()"" />
                <xsl:variable name=""var:v616"" select=""userCSharp:LogicalEq(string($var:v615) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v616"">
                  <xsl:variable name=""var:v617"" select=""boolean(s1:CAS_ClaimLevelAdjustments/CAS03_AdjustmentAmount)"" />
                  <xsl:variable name=""var:v618"" select=""userCSharp:LogicalExistence($var:v617)"" />
                  <xsl:if test=""string($var:v618)='true'"">
                    <xsl:variable name=""var:v619"" select=""s1:CAS_ClaimLevelAdjustments/CAS03_AdjustmentAmount/text()"" />
                    <ns0:TRI_CAS03_AMT>
                      <xsl:value-of select=""$var:v619"" />
                    </ns0:TRI_CAS03_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v620"" select=""position()"" />
                <xsl:variable name=""var:v621"" select=""userCSharp:LogicalEq(string($var:v620) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v621"">
                  <xsl:variable name=""var:v622"" select=""boolean(s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount)"" />
                  <xsl:variable name=""var:v623"" select=""userCSharp:LogicalExistence($var:v622)"" />
                  <xsl:if test=""string($var:v623)='true'"">
                    <xsl:variable name=""var:v624"" select=""s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()"" />
                    <ns0:TRI_PAYERPAID_AMT>
                      <xsl:value-of select=""$var:v624"" />
                    </ns0:TRI_PAYERPAID_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v625"" select=""position()"" />
                <xsl:variable name=""var:v626"" select=""userCSharp:LogicalEq(string($var:v625) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v626"">
                  <xsl:variable name=""var:v627"" select=""boolean(s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount)"" />
                  <xsl:variable name=""var:v628"" select=""userCSharp:LogicalExistence($var:v627)"" />
                  <xsl:if test=""string($var:v628)='true'"">
                    <xsl:variable name=""var:v629"" select=""s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount/text()"" />
                    <ns0:TRI_NONCOVERED_AMT>
                      <xsl:value-of select=""$var:v629"" />
                    </ns0:TRI_NONCOVERED_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v630"" select=""position()"" />
                <xsl:variable name=""var:v631"" select=""userCSharp:LogicalEq(string($var:v630) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v631"">
                  <xsl:variable name=""var:v632"" select=""boolean(s1:AMT_SubLoop/s1:AMT_RemainingPatientLiability/AMT02_RemainingPatientLiability)"" />
                  <xsl:variable name=""var:v633"" select=""userCSharp:LogicalExistence($var:v632)"" />
                  <xsl:if test=""string($var:v633)='true'"">
                    <xsl:variable name=""var:v634"" select=""s1:AMT_SubLoop/s1:AMT_RemainingPatientLiability/AMT02_RemainingPatientLiability/text()"" />
                    <ns0:TRI_LIABILITY_AMT>
                      <xsl:value-of select=""$var:v634"" />
                    </ns0:TRI_LIABILITY_AMT>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v635"" select=""position()"" />
                <xsl:variable name=""var:v636"" select=""userCSharp:LogicalEq(string($var:v635) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v636"">
                  <xsl:variable name=""var:v637"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:REF_OtherSubscriberSecondaryIdentification/REF02_OtherInsuredAdditionalIdentifier)"" />
                  <xsl:variable name=""var:v638"" select=""userCSharp:LogicalExistence($var:v637)"" />
                  <xsl:if test=""string($var:v638)='true'"">
                    <xsl:variable name=""var:v639"" select=""s1:NM1_SubLoop_5/s1:TS837_2330A_Loop/s1:REF_OtherSubscriberSecondaryIdentification/REF02_OtherInsuredAdditionalIdentifier/text()"" />
                    <ns0:TRI_INSURED_SSN_REF>
                      <xsl:value-of select=""$var:v639"" />
                    </ns0:TRI_INSURED_SSN_REF>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v640"" select=""position()"" />
                <xsl:variable name=""var:v641"" select=""userCSharp:LogicalEq(string($var:v640) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v641"">
                  <xsl:variable name=""var:v642"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N301_OtherPayerAddressLine)"" />
                  <xsl:variable name=""var:v643"" select=""userCSharp:LogicalExistence($var:v642)"" />
                  <xsl:if test=""string($var:v643)='true'"">
                    <xsl:variable name=""var:v644"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N301_OtherPayerAddressLine/text()"" />
                    <ns0:TRI_PAYER_ADD1>
                      <xsl:value-of select=""$var:v644"" />
                    </ns0:TRI_PAYER_ADD1>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v645"" select=""position()"" />
                <xsl:variable name=""var:v646"" select=""userCSharp:LogicalEq(string($var:v645) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v646"">
                  <xsl:variable name=""var:v647"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N302_OtherPayerAddressLine)"" />
                  <xsl:variable name=""var:v648"" select=""userCSharp:LogicalExistence($var:v647)"" />
                  <xsl:if test=""string($var:v648)='true'"">
                    <xsl:variable name=""var:v649"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N3_OtherPayerAddress/N302_OtherPayerAddressLine/text()"" />
                    <ns0:TRI_PAYER_ADD2>
                      <xsl:value-of select=""$var:v649"" />
                    </ns0:TRI_PAYER_ADD2>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v650"" select=""position()"" />
                <xsl:variable name=""var:v651"" select=""userCSharp:LogicalEq(string($var:v650) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v651"">
                  <xsl:variable name=""var:v652"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N401_OtherPayerCityName)"" />
                  <xsl:variable name=""var:v653"" select=""userCSharp:LogicalExistence($var:v652)"" />
                  <xsl:if test=""string($var:v653)='true'"">
                    <xsl:variable name=""var:v654"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N401_OtherPayerCityName/text()"" />
                    <ns0:TRI_PAYER_CITY>
                      <xsl:value-of select=""$var:v654"" />
                    </ns0:TRI_PAYER_CITY>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v655"" select=""position()"" />
                <xsl:variable name=""var:v656"" select=""userCSharp:LogicalEq(string($var:v655) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v656"">
                  <xsl:variable name=""var:v657"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N402_OtherPayerStateorProvinceCode)"" />
                  <xsl:variable name=""var:v658"" select=""userCSharp:LogicalExistence($var:v657)"" />
                  <xsl:if test=""string($var:v658)='true'"">
                    <xsl:variable name=""var:v659"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N402_OtherPayerStateorProvinceCode/text()"" />
                    <ns0:TRI_PAYER_STATE>
                      <xsl:value-of select=""$var:v659"" />
                    </ns0:TRI_PAYER_STATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v660"" select=""position()"" />
                <xsl:variable name=""var:v661"" select=""userCSharp:LogicalEq(string($var:v660) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v661"">
                  <xsl:variable name=""var:v662"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N403_OtherPayerPostalZoneorZIPCode)"" />
                  <xsl:variable name=""var:v663"" select=""userCSharp:LogicalExistence($var:v662)"" />
                  <xsl:if test=""string($var:v663)='true'"">
                    <xsl:variable name=""var:v664"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:N4_OtherPayerCity_State_ZIPCode/N403_OtherPayerPostalZoneorZIPCode/text()"" />
                    <ns0:TRI_PAYER_ZIPCODE>
                      <xsl:value-of select=""$var:v664"" />
                    </ns0:TRI_PAYER_ZIPCODE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v665"" select=""position()"" />
                <xsl:variable name=""var:v666"" select=""userCSharp:LogicalEq(string($var:v665) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v666"">
                  <xsl:variable name=""var:v667"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate)"" />
                  <xsl:variable name=""var:v668"" select=""userCSharp:LogicalExistence($var:v667)"" />
                  <xsl:if test=""string($var:v668)='true'"">
                    <xsl:variable name=""var:v669"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:DTP_ClaimCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate/text()"" />
                    <ns0:TRI_PAYER_REMITTANCE_DATE>
                      <xsl:value-of select=""$var:v669"" />
                    </ns0:TRI_PAYER_REMITTANCE_DATE>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v670"" select=""position()"" />
                <xsl:variable name=""var:v671"" select=""userCSharp:LogicalEq(string($var:v670) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v671"">
                  <xsl:variable name=""var:v672"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v673"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[1]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v674"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v675"" select=""s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier[2]/REF02_OtherPayerSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v676"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerPriorAuthorizationNumber/REF01_ReferenceIdentificationQualifier/text())"" />
                  <xsl:variable name=""var:v677"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerPriorAuthorizationNumber/REF02_OtherPayerPriorAuthorizationNumber/text())"" />
                  <xsl:variable name=""var:v678"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerReferralNumber/REF01_ReferenceIdentificationQualifier/text())"" />
                  <xsl:variable name=""var:v679"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerReferralNumber/REF02_OtherPayerPriorAuthorizationorReferralNumber/text())"" />
                  <xsl:variable name=""var:v680"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimAdjustmentIndicator/REF01_ReferenceIdentificationQualifier/text())"" />
                  <xsl:variable name=""var:v681"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimAdjustmentIndicator/REF02_OtherPayerClaimAdjustmentIndicator/text())"" />
                  <xsl:variable name=""var:v682"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimControlNumber/REF01_ReferenceIdentificationQualifier/text())"" />
                  <xsl:variable name=""var:v683"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerClaimControlNumber/REF02_OtherPayer_sClaimControlNumber/text())"" />
                  <xsl:variable name=""var:v684"" select=""userCSharp:StringConcat(string($var:v672) , &quot;:&quot; , string($var:v673) , &quot;,&quot; , string($var:v674) , &quot;:&quot; , string($var:v675) , &quot;,&quot; , $var:v676 , &quot;:&quot; , $var:v677 , &quot;,&quot; , $var:v678 , &quot;:&quot; , $var:v679 , &quot;,&quot; , $var:v680 , &quot;:&quot; , $var:v681 , &quot;,&quot; , $var:v682 , &quot;:&quot; , $var:v683 , &quot;,&quot;)"" />
                  <ns0:TRI_PAYER_REF>
                    <xsl:value-of select=""$var:v684"" />
                  </ns0:TRI_PAYER_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v685"" select=""position()"" />
                <xsl:variable name=""var:v686"" select=""userCSharp:LogicalEq(string($var:v685) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v686"">
                  <xsl:variable name=""var:v687"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:NM1_OtherPayerReferringProvider/NM102_EntityTypeQualifier)"" />
                  <xsl:variable name=""var:v688"" select=""userCSharp:LogicalExistence($var:v687)"" />
                  <xsl:if test=""string($var:v688)='true'"">
                    <xsl:variable name=""var:v689"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:NM1_OtherPayerReferringProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:TRI_INSURED_REFERING_QUAL>
                      <xsl:value-of select=""$var:v689"" />
                    </ns0:TRI_INSURED_REFERING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v690"" select=""position()"" />
                <xsl:variable name=""var:v691"" select=""userCSharp:LogicalEq(string($var:v690) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v691"">
                  <xsl:variable name=""var:v692"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v693"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[1]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v694"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v695"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[2]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v696"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v697"" select=""s1:NM1_SubLoop_5/s1:TS837_2330C_Loop_Loop/s1:TS837_2330C_Loop/s1:REF_OtherPayerReferringProviderSecondaryIdentification[3]/REF02_OtherPayerReferringProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v698"" select=""userCSharp:StringConcat(string($var:v692) , &quot;:&quot; , string($var:v693) , &quot;,&quot; , string($var:v694) , &quot;:&quot; , string($var:v695) , &quot;,&quot; , string($var:v696) , &quot;:&quot; , string($var:v697) , &quot;,&quot;)"" />
                  <ns0:TRI_INSURED_REFERING_REF>
                    <xsl:value-of select=""$var:v698"" />
                  </ns0:TRI_INSURED_REFERING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v699"" select=""position()"" />
                <xsl:variable name=""var:v700"" select=""userCSharp:LogicalEq(string($var:v699) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v700"">
                  <xsl:variable name=""var:v701"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:NM1_OtherPayerRenderingProvider/NM102_EntityTypeQualifier)"" />
                  <xsl:variable name=""var:v702"" select=""userCSharp:LogicalExistence($var:v701)"" />
                  <xsl:if test=""string($var:v702)='true'"">
                    <xsl:variable name=""var:v703"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:NM1_OtherPayerRenderingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:TRI_INSURED_RENDERING_QUAL>
                      <xsl:value-of select=""$var:v703"" />
                    </ns0:TRI_INSURED_RENDERING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v704"" select=""position()"" />
                <xsl:variable name=""var:v705"" select=""userCSharp:LogicalEq(string($var:v704) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v705"">
                  <xsl:variable name=""var:v706"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v707"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[1]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v708"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v709"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[2]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v710"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v711"" select=""s1:NM1_SubLoop_5/s1:TS837_2330D_Loop/s1:REF_OtherPayerRenderingProviderSecondaryIdentification[3]/REF02_OtherPayerRenderingProviderSecondaryIdentifier/text()"" />
                  <xsl:variable name=""var:v712"" select=""userCSharp:StringConcat(string($var:v706) , &quot;:&quot; , string($var:v707) , &quot;,&quot; , string($var:v708) , &quot;:&quot; , string($var:v709) , &quot;,&quot; , string($var:v710) , &quot;:&quot; , string($var:v711) , &quot;,&quot;)"" />
                  <ns0:TRI_INSURED_RENDERING_REF>
                    <xsl:value-of select=""$var:v712"" />
                  </ns0:TRI_INSURED_RENDERING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v713"" select=""position()"" />
                <xsl:variable name=""var:v714"" select=""userCSharp:LogicalEq(string($var:v713) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v714"">
                  <xsl:variable name=""var:v715"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:NM1_OtherPayerServiceFacilityLocation/NM102_EntityTypeQualifier)"" />
                  <xsl:variable name=""var:v716"" select=""userCSharp:LogicalExistence($var:v715)"" />
                  <xsl:if test=""string($var:v716)='true'"">
                    <xsl:variable name=""var:v717"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:NM1_OtherPayerServiceFacilityLocation/NM102_EntityTypeQualifier/text()"" />
                    <ns0:TRI_INSURED_SERVICEFACILITY_QUAL>
                      <xsl:value-of select=""$var:v717"" />
                    </ns0:TRI_INSURED_SERVICEFACILITY_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v718"" select=""position()"" />
                <xsl:variable name=""var:v719"" select=""userCSharp:LogicalEq(string($var:v718) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v719"">
                  <xsl:variable name=""var:v720"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v721"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[1]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v722"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v723"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[2]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v724"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v725"" select=""s1:NM1_SubLoop_5/s1:TS837_2330E_Loop/s1:REF_OtherPayerServiceFacilityLocationSecondaryIdentification[3]/REF02_OtherPayerServiceFacilityLocationSecondary__Identifier/text()"" />
                  <xsl:variable name=""var:v726"" select=""userCSharp:StringConcat(string($var:v720) , &quot;:&quot; , string($var:v721) , &quot;,&quot; , string($var:v722) , &quot;:&quot; , string($var:v723) , &quot;,&quot; , string($var:v724) , &quot;:&quot; , string($var:v725) , &quot;,&quot;)"" />
                  <ns0:TRI_INSURED_SERVICEFACILITY_REF>
                    <xsl:value-of select=""$var:v726"" />
                  </ns0:TRI_INSURED_SERVICEFACILITY_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v727"" select=""position()"" />
                <xsl:variable name=""var:v728"" select=""userCSharp:LogicalEq(string($var:v727) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v728"">
                  <xsl:variable name=""var:v729"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:NM1_OtherPayerSupervisingProvider/NM102_EntityTypeQualifier)"" />
                  <xsl:variable name=""var:v730"" select=""userCSharp:LogicalExistence($var:v729)"" />
                  <xsl:if test=""string($var:v730)='true'"">
                    <xsl:variable name=""var:v731"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:NM1_OtherPayerSupervisingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:TRI_INSURED_SUPERVISING_QUAL>
                      <xsl:value-of select=""$var:v731"" />
                    </ns0:TRI_INSURED_SUPERVISING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v732"" select=""position()"" />
                <xsl:variable name=""var:v733"" select=""userCSharp:LogicalEq(string($var:v732) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v733"">
                  <xsl:variable name=""var:v734"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v735"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[1]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v736"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v737"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[2]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v738"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v739"" select=""s1:NM1_SubLoop_5/s1:TS837_2330F_Loop/s1:REF_OtherPayerSupervisingProviderSecondaryIdentification[3]/REF02_OtherPayerSupervisingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v740"" select=""userCSharp:StringConcat(string($var:v734) , &quot;:&quot; , string($var:v735) , &quot;,&quot; , string($var:v736) , &quot;:&quot; , string($var:v737) , &quot;,&quot; , string($var:v738) , &quot;:&quot; , string($var:v739) , &quot;,&quot;)"" />
                  <ns0:TRI_INSURED_SUPERVISING_REF>
                    <xsl:value-of select=""$var:v740"" />
                  </ns0:TRI_INSURED_SUPERVISING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v741"" select=""position()"" />
                <xsl:variable name=""var:v742"" select=""userCSharp:LogicalEq(string($var:v741) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v742"">
                  <xsl:variable name=""var:v743"" select=""boolean(s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:NM1_OtherPayerBillingProvider/NM102_EntityTypeQualifier)"" />
                  <xsl:variable name=""var:v744"" select=""userCSharp:LogicalExistence($var:v743)"" />
                  <xsl:if test=""string($var:v744)='true'"">
                    <xsl:variable name=""var:v745"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:NM1_OtherPayerBillingProvider/NM102_EntityTypeQualifier/text()"" />
                    <ns0:TRI_INSURED_BILLING_QUAL>
                      <xsl:value-of select=""$var:v745"" />
                    </ns0:TRI_INSURED_BILLING_QUAL>
                  </xsl:if>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v746"" select=""position()"" />
                <xsl:variable name=""var:v747"" select=""userCSharp:LogicalEq(string($var:v746) , &quot;2&quot;)"" />
                <xsl:if test=""$var:v747"">
                  <xsl:variable name=""var:v748"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v749"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[1]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v750"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                  <xsl:variable name=""var:v751"" select=""s1:NM1_SubLoop_5/s1:TS837_2330G_Loop/s1:REF_OtherPayerBillingProviderSecondaryIdentification[2]/REF02_OtherPayerBillingProviderIdentifier/text()"" />
                  <xsl:variable name=""var:v752"" select=""userCSharp:StringConcat(string($var:v748) , &quot;:&quot; , string($var:v749) , &quot;,&quot; , string($var:v750) , &quot;:&quot; , string($var:v751) , &quot;,&quot;)"" />
                  <ns0:TRI_INSURED_BILLING_REF>
                    <xsl:value-of select=""$var:v752"" />
                  </ns0:TRI_INSURED_BILLING_REF>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:EDI_SUBMITTER_ID>
          <xsl:value-of select=""$var:v18"" />
        </ns0:EDI_SUBMITTER_ID>
        <ns0:BILLING_NOTE_QUAL>
          <xsl:text />
        </ns0:BILLING_NOTE_QUAL>
        <ns0:BILLING_NOTE>
          <xsl:text />
        </ns0:BILLING_NOTE>
        <ns0:CLAIM_NOTE_QUAL>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NTE_ClaimNote/NTE01_NoteReferenceCode/text()"" />
        </ns0:CLAIM_NOTE_QUAL>
        <ns0:CLAIM_NOTE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NTE_ClaimNote/NTE02_ClaimNoteText/text()"" />
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
        <xsl:if test=""string($var:v113)='true'"">
          <xsl:variable name=""var:v753"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom/DTP03_OnsetofCurrentIllnessorInjuryDate/text()"" />
          <ns0:CURRENT_ILLNESS_DATE>
            <xsl:value-of select=""$var:v753"" />
          </ns0:CURRENT_ILLNESS_DATE>
        </xsl:if>
        <xsl:if test=""string($var:v102)='true'"">
          <xsl:variable name=""var:v754"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident/DTP01_DateTimeQualifier/text()"" />
          <ns0:ACCIDENT_DATE_QUAL>
            <xsl:value-of select=""$var:v754"" />
          </ns0:ACCIDENT_DATE_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v102)='true'"">
          <xsl:variable name=""var:v755"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_Accident/DTP03_AccidentDate/text()"" />
          <ns0:ACCIDENT_DATE>
            <xsl:value-of select=""$var:v755"" />
          </ns0:ACCIDENT_DATE>
        </xsl:if>
        <ns0:ANESTHESIA_PROC_HI>
          <xsl:value-of select=""$var:v756"" />
        </ns0:ANESTHESIA_PROC_HI>
        <xsl:variable name=""var:v769"" select=""userCSharp:SubConditionCodes($var:v757 , $var:v758 , $var:v759 , $var:v760 , $var:v761 , $var:v762 , $var:v763 , $var:v764 , $var:v765 , $var:v766 , $var:v767 , $var:v768)"" />
        <ns0:ANESTHESIA_CONDITION_HI>
          <xsl:value-of select=""$var:v769"" />
        </ns0:ANESTHESIA_CONDITION_HI>
        <ns0:ANESTHESIA_TREATMENTCODE_HI>
          <xsl:text />
        </ns0:ANESTHESIA_TREATMENTCODE_HI>
        <xsl:variable name=""var:v770"" select=""userCSharp:AutoAccident($var:v61 , $var:v62 , $var:v63 , string(InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CLM_ClaimInformation/s1:C024_RelatedCausesInformation/C02404_AutoAccidentStateorProvinceCode/text()))"" />
        <ns0:AUTO_ACCIDENT_STATE>
          <xsl:value-of select=""$var:v770"" />
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
          <xsl:value-of select=""$var:v18"" />
        </ns0:SOURCE_FILE_NAME>
        <xsl:for-each select=""/*[local-name()='Root']/*[local-name()='InputMessagePart_0']/*[local-name()='X12_00501_837_P']/*[local-name()='TS837_2000A_Loop']/*[local-name()='TS837_2000B_Loop']/*[local-name()='TS837_2300_Loop']/*[local-name()='TS837_2320_Loop']"">
            <xsl:if test=""position() = '1'"">

              <xsl:element name=""CAS_ADJ_CODE_PAYER_A_LIST"">


                <xsl:for-each select=""./*[local-name()='CAS_ClaimLevelAdjustments']"">
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
            <xsl:if test=""position() = '2'"">
              <xsl:element name=""CAS_ADJ_CODE_PAYER_B_LIST"">
                <xsl:for-each select=""./*[local-name()='CAS_ClaimLevelAdjustments']"">
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
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v771"" select=""position()"" />
                <xsl:variable name=""var:v772"" select=""userCSharp:LogicalEq(string($var:v771) , &quot;1&quot;)"" />
                <xsl:variable name=""var:v773"" select=""userCSharp:InitCumulativeConcat(0)"" />
                <xsl:variable name=""var:v774"" select=""userCSharp:OtherPayerSecIDList(string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier/REF01_ReferenceIdentificationQualifier/text()) , string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier/REF02_OtherPayerSecondaryIdentifier/text()))"" />
                <xsl:variable name=""var:v775"" select=""userCSharp:AddToCumulativeConcat(0,string($var:v774),&quot;2&quot;)"" />
                <xsl:variable name=""var:v776"" select=""userCSharp:GetCumulativeConcat(0)"" />
                <xsl:if test=""string($var:v772)='true'"">
                  <xsl:variable name=""var:v777"" select=""string($var:v776)"" />
                  <xsl:variable name=""var:v778"" select=""userCSharp:RemoveLastChar(string($var:v777))"" />
                  <ns0:OTHER_PAYER_A_SECID>
                    <xsl:value-of select=""$var:v778"" />
                  </ns0:OTHER_PAYER_A_SECID>
                </xsl:if>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:TS837_2320_Loop"">
                <xsl:variable name=""var:v779"" select=""position()"" />
                <xsl:variable name=""var:v780"" select=""userCSharp:LogicalEq(string($var:v779) , &quot;2&quot;)"" />
                <xsl:variable name=""var:v781"" select=""userCSharp:InitCumulativeConcat(0)"" />
                <xsl:variable name=""var:v782"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier/REF01_ReferenceIdentificationQualifier/text())"" />
                <xsl:variable name=""var:v783"" select=""string(s1:NM1_SubLoop_5/s1:TS837_2330B_Loop/s1:REF_SubLoop_6/s1:REF_OtherPayerSecondaryIdentifier_Loop/s1:REF_OtherPayerSecondaryIdentifier/REF02_OtherPayerSecondaryIdentifier/text())"" />
                <xsl:variable name=""var:v784"" select=""userCSharp:OtherPayerSecIDList($var:v782 , $var:v783)"" />
                <xsl:variable name=""var:v785"" select=""userCSharp:AddToCumulativeConcat(0,string($var:v784),&quot;2&quot;)"" />
                <xsl:variable name=""var:v786"" select=""userCSharp:GetCumulativeConcat(0)"" />
                <xsl:if test=""string($var:v780)='true'"">
                  <xsl:variable name=""var:v787"" select=""string($var:v786)"" />
                  <xsl:variable name=""var:v788"" select=""userCSharp:RemoveLastChar(string($var:v787))"" />
                  <ns0:OTHER_PAYER_B_SECID>
                    <xsl:value-of select=""$var:v788"" />
                  </ns0:OTHER_PAYER_B_SECID>
                </xsl:if>
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
        <xsl:if test=""string($var:v791)='true'"">
          <xsl:variable name=""var:v792"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount/text()"" />
          <ns0:COB_NONCOVEREDAMOUNT>
            <xsl:value-of select=""$var:v792"" />
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
        <xsl:if test=""string($var:v796)='true'"">
          <xsl:variable name=""var:v797"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()"" />
          <ns0:COB_PAYERPAIDAMOUNT>
            <xsl:value-of select=""$var:v797"" />
          </ns0:COB_PAYERPAIDAMOUNT>
        </xsl:if>
        <ns0:COB_PATIENTRESPONSIBILITYACTUAL>
          <xsl:text />
        </ns0:COB_PATIENTRESPONSIBILITYACTUAL>
        <xsl:if test=""string($var:v801)='true'"">
          <xsl:variable name=""var:v802"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_PayerPaidAmount/AMT02_PayerPaidAmount/text()"" />
          <ns0:SEC_COB_PAYERPAIDAMOUNT>
            <xsl:value-of select=""$var:v802"" />
          </ns0:SEC_COB_PAYERPAIDAMOUNT>
        </xsl:if>
        <ns0:SEC_COB_PATIENTRESPONSIBILITYACTUAL>
          <xsl:text />
        </ns0:SEC_COB_PATIENTRESPONSIBILITYACTUAL>
        <ns0:SEC_COB_DISCOUNTAMOUNT>
          <xsl:text />
        </ns0:SEC_COB_DISCOUNTAMOUNT>
        <xsl:if test=""string($var:v805)='true'"">
          <xsl:variable name=""var:v806"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:TS837_2320_Loop/s1:AMT_SubLoop/s1:AMT_CoordinationofBenefits_COB_TotalNon_coveredAmount/AMT02_Non_CoveredChargeAmount/text()"" />
          <ns0:SEC_COB_NONCOVEREDAMOUNT>
            <xsl:value-of select=""$var:v806"" />
          </ns0:SEC_COB_NONCOVEREDAMOUNT>
        </xsl:if>
        <ns0:REPRICED_CLAIM_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text()"" />
        </ns0:REPRICED_CLAIM_NUMBER>
        <ns0:CONTRACT_TYPE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN101_ContractTypeCode/text()"" />
        </ns0:CONTRACT_TYPE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN102_ContractAmount"">
          <ns0:CONTRACT_AMOUNT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN102_ContractAmount/text()"" />
          </ns0:CONTRACT_AMOUNT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN103_ContractPercentage"">
          <ns0:CONTRACT_PERCENTAGE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN103_ContractPercentage/text()"" />
          </ns0:CONTRACT_PERCENTAGE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN104_ContractCode"">
          <ns0:CONTRACT_CODE>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN104_ContractCode/text()"" />
          </ns0:CONTRACT_CODE>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN105_TermsDiscountPercentage"">
          <ns0:TERMS_DISCNT_PERCNT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN105_TermsDiscountPercentage/text()"" />
          </ns0:TERMS_DISCNT_PERCNT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN106_ContractVersionIdentifier"">
          <ns0:CONTRACT_VER_IDENT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CN1_ContractInformation/CN106_ContractVersionIdentifier/text()"" />
          </ns0:CONTRACT_VER_IDENT>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR109_RoundTripPurposeDescription"">
          <ns0:AMBULANCE_DESCRIPTION>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR109_RoundTripPurposeDescription/text()"" />
          </ns0:AMBULANCE_DESCRIPTION>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR110_StretcherPurposeDescription"">
          <ns0:AMBULANCE_STRETCHER_DESC>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR110_StretcherPurposeDescription/text()"" />
          </ns0:AMBULANCE_STRETCHER_DESC>
        </xsl:if>
        <ns0:CRC03_AMBULANCE_CODE1>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC03_ConditionCode/text()"" />
        </ns0:CRC03_AMBULANCE_CODE1>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC04_ConditionCode"">
          <ns0:CRC04_AMBULANCE_CODE2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC04_ConditionCode/text()"" />
          </ns0:CRC04_AMBULANCE_CODE2>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC05_ConditionCode"">
          <ns0:CRC05_AMBULANCE_CODE3>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC05_ConditionCode/text()"" />
          </ns0:CRC05_AMBULANCE_CODE3>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC06_ConditionCode"">
          <ns0:CRC06_AMBULANCE_CODE4>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC06_ConditionCode/text()"" />
          </ns0:CRC06_AMBULANCE_CODE4>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC07_ConditionCode"">
          <ns0:CRC07_AMBULANCE_CODE5>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC07_ConditionCode/text()"" />
          </ns0:CRC07_AMBULANCE_CODE5>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR102_PatientWeight"">
          <ns0:AMBULANCE_WEIGHT>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR102_PatientWeight/text()"" />
          </ns0:AMBULANCE_WEIGHT>
        </xsl:if>
        <ns0:AMBULANCE_QTY>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR106_TransportDistance/text()"" />
        </ns0:AMBULANCE_QTY>
        <ns0:AMBULANCE_REASON_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR1_AmbulanceTransportInformation/CR104_AmbulanceTransportReasonCode/text()"" />
        </ns0:AMBULANCE_REASON_CODE>
        <xsl:if test=""string($var:v807)='true'"">
          <xsl:variable name=""var:v808"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number/REF02_ClinicalLaboratoryImprovementAmendmentNumber/text()"" />
          <ns0:CLIA_REF>
            <xsl:value-of select=""$var:v808"" />
          </ns0:CLIA_REF>
        </xsl:if>
        <xsl:if test=""string($var:v809)='true'"">
          <xsl:variable name=""var:v810"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_EPSDTReferral/CRC03_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND1>
            <xsl:value-of select=""$var:v810"" />
          </ns0:CRC_EPSDT_COND1>
        </xsl:if>
        <xsl:if test=""string($var:v812)='true'"">
          <xsl:variable name=""var:v813"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_EPSDTReferral/CRC04_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND2>
            <xsl:value-of select=""$var:v813"" />
          </ns0:CRC_EPSDT_COND2>
        </xsl:if>
        <xsl:if test=""string($var:v812)='true'"">
          <xsl:variable name=""var:v814"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_EPSDTReferral/CRC05_ConditionIndicator/text()"" />
          <ns0:CRC_EPSDT_COND3>
            <xsl:value-of select=""$var:v814"" />
          </ns0:CRC_EPSDT_COND3>
        </xsl:if>
        <xsl:if test=""string($var:v815)='true'"">
          <xsl:variable name=""var:v816"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_MammographyCertificationNumber/REF02_MammographyCertificationNumber/text()"" />
          <ns0:MAMMOGRAPHY_NUM_REF>
            <xsl:value-of select=""$var:v816"" />
          </ns0:MAMMOGRAPHY_NUM_REF>
        </xsl:if>
        <xsl:if test=""string($var:v817)='true'"">
          <xsl:variable name=""var:v818"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:NM1_SubLoop_4/s1:TS837_2310F_Loop/s1:NM1_AmbulanceDrop_offLocation/NM103_AmbulanceDrop_offLocation/text()"" />
          <ns0:AMBULANCE_DROPOFF_NAME>
            <xsl:value-of select=""$var:v818"" />
          </ns0:AMBULANCE_DROPOFF_NAME>
        </xsl:if>
        <ns0:CRC02_AMBULANCE_RESPONSECODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CRC_SubLoop/s1:CRC_AmbulanceCertification_Loop/s1:CRC_AmbulanceCertification/CRC02_CertificationConditionIndicator/text()"" />
        </ns0:CRC02_AMBULANCE_RESPONSECODE>
        <ns0:CR209_SPINAL_COND_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR2_SpinalManipulationServiceInformation/CR208_PatientConditionCode/text()"" />
        </ns0:CR209_SPINAL_COND_CODE>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR2_SpinalManipulationServiceInformation/CR210_PatientConditionDescription"">
          <ns0:CR210_PATIENT_COND_DESC1>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR2_SpinalManipulationServiceInformation/CR210_PatientConditionDescription/text()"" />
          </ns0:CR210_PATIENT_COND_DESC1>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR2_SpinalManipulationServiceInformation/CR211_PatientConditionDescription"">
          <ns0:CR211_PATIENT_COND_DESC2>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:CR2_SpinalManipulationServiceInformation/CR211_PatientConditionDescription/text()"" />
          </ns0:CR211_PATIENT_COND_DESC2>
        </xsl:if>
        <xsl:if test=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK06_AttachmentControlNumber"">
          <ns0:REPORT_PWK06_ID>
            <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:PWK_ClaimSupplementalInformation/PWK06_AttachmentControlNumber/text()"" />
          </ns0:REPORT_PWK06_ID>
        </xsl:if>
        <xsl:if test=""string($var:v819)='true'"">
          <xsl:variable name=""var:v820"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP01_DateTimeQualifier/text()"" />
          <ns0:XRAY_QUAL>
            <xsl:value-of select=""$var:v820"" />
          </ns0:XRAY_QUAL>
        </xsl:if>
        <xsl:if test=""string($var:v821)='true'"">
          <xsl:variable name=""var:v822"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastX_rayDate/DTP03_LastX_RayDate/text()"" />
          <ns0:XRAY_DATE>
            <xsl:value-of select=""$var:v822"" />
          </ns0:XRAY_DATE>
        </xsl:if>
        <ns0:SRV_AUTH_EXPT_CODE>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ServiceAuthorizationExceptionCode/REF02_ServiceAuthorizationExceptionCode/text()"" />
        </ns0:SRV_AUTH_EXPT_CODE>
        <ns0:MEDICARE_SEC_4081_IND>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_MandatoryMedicare_Section4081_CrossoverIndicator/REF02_MedicareSection4081Indicator/text()"" />
        </ns0:MEDICARE_SEC_4081_IND>
        <ns0:ADJ_REPRICED_CLAIM_REF_NUM>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_AdjustedRepricedClaimNumber/REF02_AdjustedRepricedClaimReferenceNumber/text()"" />
        </ns0:ADJ_REPRICED_CLAIM_REF_NUM>
        <ns0:INVST_DEVICE_EXPT_ID>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_InvestigationalDeviceExemptionNumber/REF02_InvestigationalDeviceExemptionIdentifier/text()"" />
        </ns0:INVST_DEVICE_EXPT_ID>
        <ns0:CARE_PLAN_OVERSIGHT_NUM>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_CarePlanOversight/REF02_CarePlanOversightNumber/text()"" />
        </ns0:CARE_PLAN_OVERSIGHT_NUM>
        <xsl:if test=""string($var:v823)='true'"">
          <xsl:variable name=""var:v824"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AcuteManifestation/DTP03_AcuteManifestationDate/text()"" />
          <ns0:ACUTE_MANIFESTATION_DT>
            <xsl:value-of select=""$var:v824"" />
          </ns0:ACUTE_MANIFESTATION_DT>
        </xsl:if>
        <xsl:if test=""string($var:v825)='true'"">
          <xsl:variable name=""var:v826"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_OnsetofCurrentIllnessorSymptom/DTP03_OnsetofCurrentIllnessorInjuryDate/text()"" />
          <ns0:ONSET_OF_CURRENT_ILLNESS_DT>
            <xsl:value-of select=""$var:v826"" />
          </ns0:ONSET_OF_CURRENT_ILLNESS_DT>
        </xsl:if>
        <xsl:if test=""string($var:v827)='true'"">
          <xsl:variable name=""var:v828"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastSeenDate/DTP03_LastSeenDate/text()"" />
          <ns0:LAST_SEEN_DT>
            <xsl:value-of select=""$var:v828"" />
          </ns0:LAST_SEEN_DT>
        </xsl:if>
        <xsl:if test=""string($var:v829)='true'"">
          <xsl:variable name=""var:v830"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastMenstrualPeriod/DTP03_LastMenstrualPeriodDate/text()"" />
          <ns0:LAST_MENSTRUAL_REC_DT>
            <xsl:value-of select=""$var:v830"" />
          </ns0:LAST_MENSTRUAL_REC_DT>
        </xsl:if>
        <xsl:if test=""string($var:v831)='true'"">
          <xsl:variable name=""var:v832"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_HearingandVisionPrescriptionDate/DTP03_PrescriptionDate/text()"" />
          <ns0:HEARING_VISION_PRES_DT>
            <xsl:value-of select=""$var:v832"" />
          </ns0:HEARING_VISION_PRES_DT>
        </xsl:if>
        <xsl:if test=""string($var:v833)='true'"">
          <xsl:variable name=""var:v834"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_LastWorked/DTP03_LastWorkedDate/text()"" />
          <ns0:LAST_WORKED_DT>
            <xsl:value-of select=""$var:v834"" />
          </ns0:LAST_WORKED_DT>
        </xsl:if>
        <xsl:if test=""string($var:v835)='true'"">
          <xsl:variable name=""var:v836"" select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:DTP_SubLoop/s1:DTP_Date_AuthorizedReturntoWork/DTP03_WorkReturnDate/text()"" />
          <ns0:AUTHORIZED_TO_RETURN_TO_WORK_DT>
            <xsl:value-of select=""$var:v836"" />
          </ns0:AUTHORIZED_TO_RETURN_TO_WORK_DT>
        </xsl:if>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v837"" select=""position()"" />
                    <xsl:variable name=""var:v838"" select=""userCSharp:LogicalEq(string($var:v837) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v838"">
                      <xsl:variable name=""var:v839"" select=""boolean(s1:NM1_ReferringProviderName)"" />
                      <xsl:variable name=""var:v840"" select=""userCSharp:LogicalExistence($var:v839)"" />
                      <xsl:if test=""string($var:v840)='true'"">
                        <xsl:variable name=""var:v841"" select=""s1:NM1_ReferringProviderName/NM102_EntityTypeQualifier/text()"" />
                        <ns0:PCP_PROVIDER_QUAL>
                          <xsl:value-of select=""$var:v841"" />
                        </ns0:PCP_PROVIDER_QUAL>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v842"" select=""position()"" />
                    <xsl:variable name=""var:v843"" select=""userCSharp:LogicalEq(string($var:v842) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v843"">
                      <ns0:PCP_PROVIDER_LNAME>
                        <xsl:value-of select=""s1:NM1_ReferringProviderName/NM103_ReferringProviderLastName/text()"" />
                      </ns0:PCP_PROVIDER_LNAME>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v844"" select=""position()"" />
                    <xsl:variable name=""var:v845"" select=""userCSharp:LogicalEq(string($var:v844) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v845"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM105_ReferringProviderMiddleNameorInitial"">
                        <ns0:PCP_PROVIDER_MNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                        </ns0:PCP_PROVIDER_MNAME>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v846"" select=""position()"" />
                    <xsl:variable name=""var:v847"" select=""userCSharp:LogicalEq(string($var:v846) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v847"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM104_ReferringProviderFirstName"">
                        <ns0:PCP_PROVIDER_FNAME>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM104_ReferringProviderFirstName/text()"" />
                        </ns0:PCP_PROVIDER_FNAME>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v848"" select=""position()"" />
                    <xsl:variable name=""var:v849"" select=""userCSharp:LogicalEq(string($var:v848) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v849"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM107_ReferringProviderNameSuffix"">
                        <ns0:PCP_PROVIDER_SUFFIX>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM107_ReferringProviderNameSuffix/text()"" />
                        </ns0:PCP_PROVIDER_SUFFIX>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v850"" select=""position()"" />
                    <xsl:variable name=""var:v851"" select=""userCSharp:LogicalEq(string($var:v850) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v851"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM108_IdentificationCodeQualifier"">
                        <ns0:PCP_PROVIDER_ID_QUAL>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM108_IdentificationCodeQualifier/text()"" />
                        </ns0:PCP_PROVIDER_ID_QUAL>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v852"" select=""position()"" />
                    <xsl:variable name=""var:v853"" select=""userCSharp:LogicalEq(string($var:v852) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v853"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier"">
                        <ns0:PCP_PROVIDER_ID>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier/text()"" />
                        </ns0:PCP_PROVIDER_ID>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v854"" select=""position()"" />
                    <xsl:variable name=""var:v855"" select=""userCSharp:LogicalEq(string($var:v854) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v855"">
                      <xsl:if test=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier"">
                        <ns0:PCP_PROVIDER_NPI_ID>
                          <xsl:value-of select=""s1:NM1_ReferringProviderName/NM109_ReferringProviderIdentifier/text()"" />
                        </ns0:PCP_PROVIDER_NPI_ID>
                      </xsl:if>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
          <xsl:for-each select=""s1:TS837_2000B_Loop"">
            <xsl:for-each select=""s1:TS837_2300_Loop"">
              <xsl:for-each select=""s1:NM1_SubLoop_4"">
                <xsl:for-each select=""s1:TS837_2310A_Loop_Loop"">
                  <xsl:for-each select=""s1:TS837_2310A_Loop"">
                    <xsl:variable name=""var:v856"" select=""position()"" />
                    <xsl:variable name=""var:v857"" select=""userCSharp:LogicalEq(string($var:v856) , &quot;2&quot;)"" />
                    <xsl:if test=""$var:v857"">
                      <xsl:variable name=""var:v858"" select=""./s1:REF_ReferringProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v859"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
                      <xsl:variable name=""var:v860"" select=""./s1:REF_ReferringProviderSecondaryIdentification[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v861"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
                      <xsl:variable name=""var:v862"" select=""./s1:REF_ReferringProviderSecondaryIdentification[2]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v863"" select=""./s1:REF_ReferringProviderSecondaryIdentification[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v864"" select=""./s1:REF_ReferringProviderSecondaryIdentification[3]/REF01_ReferenceIdentificationQualifier/text()"" />
                      <xsl:variable name=""var:v865"" select=""./s1:REF_ReferringProviderSecondaryIdentification[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
                      <xsl:variable name=""var:v866"" select=""userCSharp:StringConcat(string($var:v858) , string($var:v859) , string($var:v860) , string($var:v861) , string($var:v862) , string($var:v859) , string($var:v863) , string($var:v861) , string($var:v864) , string($var:v859) , string($var:v865) , string($var:v861))"" />
                      <ns0:PCP_PROVIDER_REF>
                        <xsl:value-of select=""$var:v866"" />
                      </ns0:PCP_PROVIDER_REF>
                    </xsl:if>
                  </xsl:for-each>
                </xsl:for-each>
              </xsl:for-each>
            </xsl:for-each>
          </xsl:for-each>
        </xsl:for-each>
        <ns0:AUTH_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_PriorAuthorization/REF02_PriorAuthorizationNumber/text()"" />
        </ns0:AUTH_NUMBER>
        <ns0:REFERRAL_NUMBER>
          <xsl:value-of select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop/s1:TS837_2000B_Loop/s1:TS837_2300_Loop/s1:REF_SubLoop_5/s1:REF_ReferralNumber/REF02_ReferralNumber/text()"" />
        </ns0:REFERRAL_NUMBER>
      </ns0:CLAIM_ADDTNL>
      <xsl:for-each select=""InputMessagePart_0/s1:X12_00501_837_P/s1:TS837_2000A_Loop"">
        <xsl:for-each select=""s1:TS837_2000B_Loop"">
          <xsl:for-each select=""s1:TS837_2300_Loop"">
            <xsl:for-each select=""s1:TS837_2400_Loop"">
              <xsl:variable name=""var:v867"" select=""string(../s1:CLM_ClaimInformation/CLM01_PatientControlNumber/text())"" />
              <xsl:variable name=""var:v868"" select=""string(../s1:REF_SubLoop_5/s1:REF_RepricedClaimNumber/REF02_RepricedClaimReferenceNumber/text())"" />
              <xsl:variable name=""var:v870"" select=""s1:PWK_SubLoop/s1:PWK_LineSupplementalInformation_Loop/s1:PWK_LineSupplementalInformation[1]/PWK01_AttachmentReportTypeCode/text()"" />
              <xsl:variable name=""var:v871"" select=""s1:PWK_SubLoop/s1:PWK_LineSupplementalInformation_Loop/s1:PWK_LineSupplementalInformation[1]/PWK02_AttachmentTransmissionCode/text()"" />
              <xsl:variable name=""var:v872"" select=""userCSharp:LogicalExistence(boolean(s1:DTP_SubLoop_2/s1:DTP_Date_PrescriptionDate))"" />
              <xsl:variable name=""var:v874"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_RepricedLineItemReferenceNumber))"" />
              <xsl:variable name=""var:v876"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_AdjustedRepricedLineItemReferenceNumber))"" />
              <xsl:variable name=""var:v878"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_PriorAuthorization_2_Loop/s1:REF_PriorAuthorization_2))"" />
              <xsl:variable name=""var:v880"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_2))"" />
              <xsl:variable name=""var:v882"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_LineItemControlNumber))"" />
              <xsl:variable name=""var:v884"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v885"" select=""userCSharp:StringUpperCase(&quot;:&quot;)"" />
              <xsl:variable name=""var:v886"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[1]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v887"" select=""userCSharp:StringLowerCase(&quot;,&quot;)"" />
              <xsl:variable name=""var:v888"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v889"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[2]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v890"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v891"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[3]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v892"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[4]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v893"" select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:REF_RenderingProviderSecondaryIdentification_2[4]/REF02_RenderingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v894"" select=""userCSharp:StringConcat(string($var:v884) , string($var:v885) , string($var:v886) , string($var:v887) , string($var:v888) , string($var:v885) , string($var:v889) , string($var:v887) , string($var:v890) , string($var:v885) , string($var:v891) , string($var:v887) , string($var:v892) , string($var:v885) , string($var:v893) , string($var:v887))"" />
              <xsl:variable name=""var:v895"" select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v896"" select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification_2[1]/REF02_ServiceFacilityLocationSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v897"" select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v898"" select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:REF_ServiceFacilityLocationSecondaryIdentification_2[2]/REF02_ServiceFacilityLocationSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v899"" select=""userCSharp:StringConcat(string($var:v895) , string($var:v885) , string($var:v896) , string($var:v887) , string($var:v897) , string($var:v885) , string($var:v898) , string($var:v887))"" />
              <xsl:variable name=""var:v900"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v901"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[1]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v902"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v903"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[2]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v904"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v905"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[3]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v906"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[4]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v907"" select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:REF_SupervisingProviderSecondaryIdentification_2[4]/REF02_SupervisingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v908"" select=""userCSharp:StringConcat(string($var:v900) , string($var:v885) , string($var:v901) , string($var:v887) , string($var:v902) , string($var:v885) , string($var:v903) , string($var:v887) , string($var:v904) , string($var:v885) , string($var:v905) , string($var:v887) , string($var:v906) , string($var:v885) , string($var:v907) , string($var:v887))"" />
              <xsl:variable name=""var:v909"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v910"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[1]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v911"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[2]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v912"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[2]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v913"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[3]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v914"" select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:REF_ReferringProviderSecondaryIdentification_2[3]/REF02_ReferringProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v915"" select=""userCSharp:StringConcat(string($var:v909) , string($var:v885) , string($var:v910) , string($var:v887) , string($var:v911) , string($var:v885) , string($var:v912) , string($var:v887) , string($var:v913) , string($var:v885) , string($var:v914) , string($var:v887))"" />
              <xsl:variable name=""var:v917"" select=""boolean(s1:REF_SubLoop_7/s1:REF_AdjustedRepricedLineItemReferenceNumber)"" />
              <xsl:variable name=""var:v918"" select=""userCSharp:LogicalExistence($var:v917)"" />
              <xsl:variable name=""var:v920"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_MammographyCertificationNumber_2))"" />
              <xsl:variable name=""var:v922"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_ReferringClinicalLaboratoryImprovementAmendment_CLIA_FacilityIdentification))"" />
              <xsl:variable name=""var:v924"" select=""userCSharp:LogicalExistence(boolean(s1:REF_SubLoop_7/s1:REF_ImmunizationBatchNumber))"" />
              <xsl:variable name=""var:v926"" select=""s1:TS837_2410_Loop/s1:REF_PrescriptionorCompoundDrugAssociationNumber[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v927"" select=""s1:TS837_2410_Loop/s1:REF_PrescriptionorCompoundDrugAssociationNumber[1]/REF02_PrescriptionNumber/text()"" />
              <xsl:variable name=""var:v928"" select=""userCSharp:StringConcat(string($var:v926) , string($var:v885) , string($var:v927))"" />
              <xsl:variable name=""var:v929"" select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:REF_OrderingProviderSecondaryIdentification[1]/REF01_ReferenceIdentificationQualifier/text()"" />
              <xsl:variable name=""var:v930"" select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:REF_OrderingProviderSecondaryIdentification[1]/REF02_OrderingProviderSecondaryIdentifier/text()"" />
              <xsl:variable name=""var:v931"" select=""userCSharp:StringConcat(string($var:v929) , string($var:v885) , string($var:v930))"" />
              <xsl:variable name=""var:v932"" select=""string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP02_DateTimePeriodFormatQualifier/text())"" />
              <xsl:variable name=""var:v933"" select=""userCSharp:LogicalEq($var:v932 , &quot;D8&quot;)"" />
              <xsl:variable name=""var:v935"" select=""userCSharp:LogicalEq($var:v932 , &quot;RD8&quot;)"" />
              <xsl:variable name=""var:v936"" select=""string(s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP03_ServiceDate/text())"" />
              <xsl:variable name=""var:v937"" select=""userCSharp:StringLeft($var:v936 , &quot;8&quot;)"" />
              <xsl:variable name=""var:v939"" select=""userCSharp:StringRight($var:v936 , &quot;8&quot;)"" />
              <xsl:variable name=""var:v941"" select=""userCSharp:LogicalExistence(boolean(s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:NM1_AmbulanceDrop_offLocation_2))"" />
              <ns0:CLAIM_ADDTNL_DETAIL>
                <xsl:variable name=""var:v869"" select=""userCSharp:ExternalClmID($var:v867 , $var:v868)"" />
                <ns0:CLAIM_ID>
                  <xsl:value-of select=""$var:v869"" />
                </ns0:CLAIM_ID>
                <ns0:LINE_NUMBER>
                  <xsl:value-of select=""s1:LX_ServiceLineNumber/LX01_AssignedNumber/text()"" />
                </ns0:LINE_NUMBER>
                <ns0:SERVICE_CODE>
                  <xsl:value-of select=""s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00302_ProcedureCode/text()"" />
                </ns0:SERVICE_CODE>
                <ns0:REPORT_TYPECODE>
                  <xsl:value-of select=""$var:v870"" />
                </ns0:REPORT_TYPECODE>
                <ns0:REPORT_TRANCODE>
                  <xsl:value-of select=""$var:v871"" />
                </ns0:REPORT_TRANCODE>
                <xsl:if test=""string($var:v872)='true'"">
                  <xsl:variable name=""var:v873"" select=""s1:DTP_SubLoop_2/s1:DTP_Date_PrescriptionDate/DTP03_PrescriptionDate/text()"" />
                  <ns0:PRESCRIPTION_DATE>
                    <xsl:value-of select=""$var:v873"" />
                  </ns0:PRESCRIPTION_DATE>
                </xsl:if>
                <xsl:if test=""string($var:v874)='true'"">
                  <xsl:variable name=""var:v875"" select=""s1:REF_SubLoop_7/s1:REF_RepricedLineItemReferenceNumber/REF02_RepricedLineItemReferenceNumber/text()"" />
                  <ns0:REPRICEDLINE_ITEM_REF>
                    <xsl:value-of select=""$var:v875"" />
                  </ns0:REPRICEDLINE_ITEM_REF>
                </xsl:if>
                <xsl:if test=""string($var:v876)='true'"">
                  <xsl:variable name=""var:v877"" select=""s1:REF_SubLoop_7/s1:REF_AdjustedRepricedLineItemReferenceNumber/REF02_AdjustedRepricedLineItemReferenceNumber/text()"" />
                  <ns0:REFERRAL_NUMBER>
                    <xsl:value-of select=""$var:v877"" />
                  </ns0:REFERRAL_NUMBER>
                </xsl:if>
                <xsl:if test=""string($var:v878)='true'"">
                  <xsl:variable name=""var:v879"" select=""s1:REF_SubLoop_7/s1:REF_PriorAuthorization_2_Loop/s1:REF_PriorAuthorization_2/REF02_PriorAuthorizationorReferralNumber/text()"" />
                  <ns0:PRIOR_AUTHORIZATION>
                    <xsl:value-of select=""$var:v879"" />
                  </ns0:PRIOR_AUTHORIZATION>
                </xsl:if>
                <xsl:if test=""string($var:v880)='true'"">
                  <xsl:variable name=""var:v881"" select=""s1:REF_SubLoop_7/s1:REF_ClinicalLaboratoryImprovementAmendment_CLIA_Number_2/REF02_ClinicalLaboratoryImprovementAmendmentNumber/text()"" />
                  <ns0:CLIA>
                    <xsl:value-of select=""$var:v881"" />
                  </ns0:CLIA>
                </xsl:if>
                <xsl:if test=""string($var:v882)='true'"">
                  <xsl:variable name=""var:v883"" select=""s1:REF_SubLoop_7/s1:REF_LineItemControlNumber/REF02_LineItemControlNumber/text()"" />
                  <ns0:LINECONTROL_NUM>
                    <xsl:value-of select=""$var:v883"" />
                  </ns0:LINECONTROL_NUM>
                </xsl:if>
                <ns0:NTE_QUAL>
                  <xsl:value-of select=""s1:NTE_SubLoop/s1:NTE_LineNote/NTE01_NoteReferenceCode/text()"" />
                </ns0:NTE_QUAL>
                <ns0:NTE_DESCRIPTION>
                  <xsl:value-of select=""s1:NTE_SubLoop/s1:NTE_LineNote/NTE02_LineNoteText/text()"" />
                </ns0:NTE_DESCRIPTION>
                <ns0:REPRICE_METHOD>
                  <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP01_PricingMethodology/text()"" />
                </ns0:REPRICE_METHOD>
                <ns0:REPRICE_ALLOWED_AMT>
                  <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP02_RepricedAllowedAmount/text()"" />
                </ns0:REPRICE_ALLOWED_AMT>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP03_RepricedSavingAmount"">
                  <ns0:REPRICE_SAVING_AMT>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP03_RepricedSavingAmount/text()"" />
                  </ns0:REPRICE_SAVING_AMT>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM108_IdentificationCodeQualifier"">
                  <ns0:RENDERING_PROV_QUAL>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM108_IdentificationCodeQualifier/text()"" />
                  </ns0:RENDERING_PROV_QUAL>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM109_RenderingProviderIdentifier"">
                  <ns0:RENDERING_PROV_ID>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM109_RenderingProviderIdentifier/text()"" />
                  </ns0:RENDERING_PROV_ID>
                </xsl:if>
                <ns0:RENDERING_TAXONOMY>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:PRV_RenderingProviderSpecialtyInformation_2/PRV03_ProviderTaxonomyCode/text()"" />
                </ns0:RENDERING_TAXONOMY>
                <ns0:RENDERING_PROV_LNAME>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM103_RenderingProviderLastorOrganizationName/text()"" />
                </ns0:RENDERING_PROV_LNAME>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM105_RenderingProviderMiddleName"">
                  <ns0:RENDERING_PROV_MNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM105_RenderingProviderMiddleName/text()"" />
                  </ns0:RENDERING_PROV_MNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM104_RenderingProviderFirstName"">
                  <ns0:RENDERING_PROV_FNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM104_RenderingProviderFirstName/text()"" />
                  </ns0:RENDERING_PROV_FNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM107_RenderingProviderNameSuffix"">
                  <ns0:RENDERING_PROV_SUFFIX>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420A_Loop/s1:NM1_RenderingProviderName_2/NM107_RenderingProviderNameSuffix/text()"" />
                  </ns0:RENDERING_PROV_SUFFIX>
                </xsl:if>
                <ns0:RENDERING_REF>
                  <xsl:value-of select=""$var:v894"" />
                </ns0:RENDERING_REF>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:NM1_ServiceFacilityLocation/NM108_IdentificationCodeQualifier"">
                  <ns0:FACILITY_QUAL>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:NM1_ServiceFacilityLocation/NM108_IdentificationCodeQualifier/text()"" />
                  </ns0:FACILITY_QUAL>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:NM1_ServiceFacilityLocation/NM109_LaboratoryorFacilityPrimaryIdentifier"">
                  <ns0:FACILITY_ID>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:NM1_ServiceFacilityLocation/NM109_LaboratoryorFacilityPrimaryIdentifier/text()"" />
                  </ns0:FACILITY_ID>
                </xsl:if>
                <ns0:FACILITY_LNAME>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:NM1_ServiceFacilityLocation/NM103_LaboratoryorFacilityName/text()"" />
                </ns0:FACILITY_LNAME>
                <ns0:FACILITY_REF>
                  <xsl:value-of select=""$var:v899"" />
                </ns0:FACILITY_REF>
                <ns0:FACILITY_ADD1>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N3_ServiceFacilityLocationAddress_2/N301_LaboratoryorFacilityAddressLine/text()"" />
                </ns0:FACILITY_ADD1>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N3_ServiceFacilityLocationAddress_2/N302_LaboratoryorFacilityAddressLine"">
                  <ns0:FACILITY_ADD2>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N3_ServiceFacilityLocationAddress_2/N302_LaboratoryorFacilityAddressLine/text()"" />
                  </ns0:FACILITY_ADD2>
                </xsl:if>
                <ns0:FACILITY_CITY>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_2/N401_LaboratoryorFacilityCityName/text()"" />
                </ns0:FACILITY_CITY>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_2/N402_LaboratoryorFacilityStateorProvinceCode"">
                  <ns0:FACILITY_STATE>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_2/N402_LaboratoryorFacilityStateorProvinceCode/text()"" />
                  </ns0:FACILITY_STATE>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_2/N403_LaboratoryorFacilityPostalZoneorZIPCode"">
                  <ns0:FACILITY_ZIP>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420C_Loop/s1:N4_ServiceFacilityLocationCity_State_ZIPCode_2/N403_LaboratoryorFacilityPostalZoneorZIPCode/text()"" />
                  </ns0:FACILITY_ZIP>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM108_IdentificationCodeQualifier"">
                  <ns0:SUPERVISING_QUAL>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM108_IdentificationCodeQualifier/text()"" />
                  </ns0:SUPERVISING_QUAL>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM109_SupervisingProviderIdentifier"">
                  <ns0:SUPERVISING_ID>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM109_SupervisingProviderIdentifier/text()"" />
                  </ns0:SUPERVISING_ID>
                </xsl:if>
                <ns0:SUPERVISING_LNAME>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM103_SupervisingProviderLastName/text()"" />
                </ns0:SUPERVISING_LNAME>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM104_SupervisingProviderFirstName"">
                  <ns0:SUPERVISING_FNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM104_SupervisingProviderFirstName/text()"" />
                  </ns0:SUPERVISING_FNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM105_SupervisingProviderMiddleNameorInitial"">
                  <ns0:SUPERVISING_MNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM105_SupervisingProviderMiddleNameorInitial/text()"" />
                  </ns0:SUPERVISING_MNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM107_SupervisingProviderNameSuffix"">
                  <ns0:SUPERVISING_SUFFIX>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420D_Loop/s1:NM1_SupervisingProviderName_2/NM107_SupervisingProviderNameSuffix/text()"" />
                  </ns0:SUPERVISING_SUFFIX>
                </xsl:if>
                <ns0:SUPERVISING_REF>
                  <xsl:value-of select=""$var:v908"" />
                </ns0:SUPERVISING_REF>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM108_IdentificationCodeQualifier"">
                  <ns0:REFERRING_PROV_QUAL>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM108_IdentificationCodeQualifier/text()"" />
                  </ns0:REFERRING_PROV_QUAL>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM109_ReferringProviderIdentifier"">
                  <ns0:REFERRING_PROV_ID>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM109_ReferringProviderIdentifier/text()"" />
                  </ns0:REFERRING_PROV_ID>
                </xsl:if>
                <ns0:REFERRING_PROV_LNAME>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM103_ReferringProviderLastName/text()"" />
                </ns0:REFERRING_PROV_LNAME>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM105_ReferringProviderMiddleNameorInitial"">
                  <ns0:REFERRING_PROV_MNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM105_ReferringProviderMiddleNameorInitial/text()"" />
                  </ns0:REFERRING_PROV_MNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM104_ReferringProviderFirstName"">
                  <ns0:REFERRING_PROV_FNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM104_ReferringProviderFirstName/text()"" />
                  </ns0:REFERRING_PROV_FNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM107_ReferringProviderNameSuffix"">
                  <ns0:REFERRING_PROV_SUFFIX>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420F_Loop_Loop/s1:TS837_2420F_Loop/s1:NM1_ReferringProviderName_2/NM107_ReferringProviderNameSuffix/text()"" />
                  </ns0:REFERRING_PROV_SUFFIX>
                </xsl:if>
                <ns0:REFERRING_REF>
                  <xsl:value-of select=""$var:v915"" />
                </ns0:REFERRING_REF>
                <ns0:LINE_ADJUDICATION_CODE>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD01_OtherPayerPrimaryIdentifier/text()"" />
                </ns0:LINE_ADJUDICATION_CODE>
                <ns0:LINE_ADJUDICATION_AMT>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD02_ServiceLinePaidAmount/text()"" />
                </ns0:LINE_ADJUDICATION_AMT>
                <ns0:LINE_ADJUDICATION_QUAL>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00301_ProductorServiceIDQualifier/text()"" />
                </ns0:LINE_ADJUDICATION_QUAL>
                <ns0:LINE_ADJUDICATION_PCODE>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00302_ProcedureCode/text()"" />
                </ns0:LINE_ADJUDICATION_PCODE>
                <xsl:variable name=""var:v916"" select=""userCSharp:modifierDentalSub(string(s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00303_ProcedureModifier/text()) , string(s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00304_ProcedureModifier/text()) , string(s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00305_ProcedureModifier/text()) , string(s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00306_ProcedureModifier/text()))"" />
                <ns0:LINE_ADJUDICATION_MOD>
                  <xsl:value-of select=""$var:v916"" />
                </ns0:LINE_ADJUDICATION_MOD>
                <ns0:LINE_ADJUDICATION_QTY>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD05_PaidServiceUnitCount/text()"" />
                </ns0:LINE_ADJUDICATION_QTY>
                <ns0:LQ_FRM_TYPE>
                  <xsl:value-of select=""s1:TS837_2440_Loop/s1:LQ_FormIdentificationCode/LQ01_CodeListQualifierCode/text()"" />
                </ns0:LQ_FRM_TYPE>
                <ns0:LQ_FRM_CODE>
                  <xsl:value-of select=""s1:TS837_2440_Loop/s1:LQ_FormIdentificationCode/LQ02_FormIdentifier/text()"" />
                </ns0:LQ_FRM_CODE>
                <ns0:FRM_ASSIGNED>
                  <xsl:value-of select=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM01_QuestionNumber_Letter/text()"" />
                </ns0:FRM_ASSIGNED>
                <xsl:if test=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM02_QuestionResponse"">
                  <ns0:FRM_QUESTION>
                    <xsl:value-of select=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM02_QuestionResponse/text()"" />
                  </ns0:FRM_QUESTION>
                </xsl:if>
                <xsl:if test=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM03_QuestionResponse"">
                  <ns0:FRM_RESPONSE>
                    <xsl:value-of select=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM03_QuestionResponse/text()"" />
                  </ns0:FRM_RESPONSE>
                </xsl:if>
                <xsl:if test=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM04_QuestionResponse"">
                  <ns0:FRM_DATE>
                    <xsl:value-of select=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM04_QuestionResponse/text()"" />
                  </ns0:FRM_DATE>
                </xsl:if>
                <xsl:if test=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM05_QuestionResponse"">
                  <ns0:FRM_AMT>
                    <xsl:value-of select=""s1:TS837_2440_Loop/s1:FRM_SupportingDocumentation/FRM05_QuestionResponse/text()"" />
                  </ns0:FRM_AMT>
                </xsl:if>
                <xsl:for-each select=""./*[local-name()='TS837_2430_Loop'][1]"">
                
          <xsl:element name=""CAS_ADJ_CODE_PAYER_A_LIST"">


            <xsl:for-each select=""./*[local-name()='CAS_LineAdjustment']"">
         
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
                <xsl:for-each select=""./*[local-name()='TS837_2430_Loop'][2]"">
        
          <xsl:element name=""CAS_ADJ_CODE_PAYER_B_LIST"">
            <xsl:for-each select=""./*[local-name()='CAS_LineAdjustment']"">
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
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:NM1_AmbulancePick_upLocation_2/NM103_NameLastorOrganizationName"">
                  <ns0:OTHER_PAYER_A_NAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:NM1_AmbulancePick_upLocation_2/NM103_NameLastorOrganizationName/text()"" />
                  </ns0:OTHER_PAYER_A_NAME>
                </xsl:if>
                <ns0:SERVICE_CODE_QUAL>
                  <xsl:value-of select=""s1:SV5_DurableMedicalEquipmentService/s1:C003_CompositeMedicalProcedureIdentifier_2/C00301_ProcedureIdentifier/text()"" />
                </ns0:SERVICE_CODE_QUAL>
                <ns0:REVENUE_CODE>
                  <xsl:text />
                </ns0:REVENUE_CODE>
                <xsl:if test=""s1:PWK_SubLoop/s1:PWK_LineSupplementalInformation_Loop/s1:PWK_LineSupplementalInformation/PWK06_AttachmentControlNumber"">
                  <ns0:REPORT_PWK06_ID>
                    <xsl:value-of select=""s1:PWK_SubLoop/s1:PWK_LineSupplementalInformation_Loop/s1:PWK_LineSupplementalInformation/PWK06_AttachmentControlNumber/text()"" />
                  </ns0:REPORT_PWK06_ID>
                </xsl:if>
                <ns0:DURABLE_TRANS_CODE>
                  <xsl:value-of select=""s1:PWK_SubLoop/s1:PWK_DurableMedicalEquipmentCertificateofMedicalNecessityIndicator/PWK02_AttachmentTransmissionCode/text()"" />
                </ns0:DURABLE_TRANS_CODE>
                <xsl:if test=""s1:CR1_AmbulanceTransportInformation_2/CR102_PatientWeight"">
                  <ns0:AMBULANCE_WEIGHT>
                    <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_2/CR102_PatientWeight/text()"" />
                  </ns0:AMBULANCE_WEIGHT>
                </xsl:if>
                <ns0:AMBULANCE_REASON_CODE>
                  <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_2/CR104_AmbulanceTransportReasonCode/text()"" />
                </ns0:AMBULANCE_REASON_CODE>
                <ns0:AMBULANCE_QTY>
                  <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_2/CR106_TransportDistance/text()"" />
                </ns0:AMBULANCE_QTY>
                <xsl:if test=""s1:CR1_AmbulanceTransportInformation_2/CR109_RoundTripPurposeDescription"">
                  <ns0:AMBULANCE_DESCRIPTION>
                    <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_2/CR109_RoundTripPurposeDescription/text()"" />
                  </ns0:AMBULANCE_DESCRIPTION>
                </xsl:if>
                <ns0:CR301_AMBULANCE_typeCODE>
                  <xsl:value-of select=""s1:CR3_DurableMedicalEquipmentCertification/CR301_CertificationTypeCode/text()"" />
                </ns0:CR301_AMBULANCE_typeCODE>
                <ns0:CR303_AMBULANCE_QTY>
                  <xsl:value-of select=""s1:CR3_DurableMedicalEquipmentCertification/CR303_DurableMedicalEquipmentDuration/text()"" />
                </ns0:CR303_AMBULANCE_QTY>
                <ns0:CRC02_AMBULANCE_RESPONSECODE>
                  <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC02_CertificationConditionIndicator/text()"" />
                </ns0:CRC02_AMBULANCE_RESPONSECODE>
                <ns0:CRC03_AMBULANCE_CODE1>
                  <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC03_ConditionCode/text()"" />
                </ns0:CRC03_AMBULANCE_CODE1>
                <xsl:if test=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC04_ConditionCode"">
                  <ns0:CRC04_AMBULANCE_CODE2>
                    <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC04_ConditionCode/text()"" />
                  </ns0:CRC04_AMBULANCE_CODE2>
                </xsl:if>
                <xsl:if test=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC05_ConditionCode"">
                  <ns0:CRC05_AMBULANCE_CODE3>
                    <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC05_ConditionCode/text()"" />
                  </ns0:CRC05_AMBULANCE_CODE3>
                </xsl:if>
                <xsl:if test=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC06_ConditionCode"">
                  <ns0:CRC06_AMBULANCE_CODE4>
                    <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC06_ConditionCode/text()"" />
                  </ns0:CRC06_AMBULANCE_CODE4>
                </xsl:if>
                <xsl:if test=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC07_ConditionCode"">
                  <ns0:CRC07_AMBULANCE_CODE5>
                    <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_AmbulanceCertification_2_Loop/s1:CRC_AmbulanceCertification_2/CRC07_ConditionCode/text()"" />
                  </ns0:CRC07_AMBULANCE_CODE5>
                </xsl:if>
                <ns0:CRC02_HOSPICE_RESPONSECODE>
                  <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_HospiceEmployeeIndicator/CRC02_HospiceEmployedProviderIndicator/text()"" />
                </ns0:CRC02_HOSPICE_RESPONSECODE>
                <ns0:CRC02_DURABLE_RESPONSECODE>
                  <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_ConditionIndicator_DurableMedicalEquipment/CRC02_CertificationConditionIndicator/text()"" />
                </ns0:CRC02_DURABLE_RESPONSECODE>
                <ns0:CRC02_DURABLE_CONDITIONCODE>
                  <xsl:value-of select=""s1:CRC_SubLoop_2/s1:CRC_ConditionIndicator_DurableMedicalEquipment/CRC03_ConditionIndicator/text()"" />
                </ns0:CRC02_DURABLE_CONDITIONCODE>
                <ns0:REVISION_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_DATE_CertificationRevision_RecertificationDate/DTP03_CertificationRevisionorRecertificationDate/text()"" />
                </ns0:REVISION_DATE>
                <ns0:THERAPY_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_BeginTherapyDate/DTP03_BeginTherapyDate/text()"" />
                </ns0:THERAPY_DATE>
                <ns0:LAST_CERTIFICATION_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_LastCertificationDate/DTP03_LastCertificationDate/text()"" />
                </ns0:LAST_CERTIFICATION_DATE>
                <ns0:LAST_SEEN_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_LastSeenDate_2/DTP03_TreatmentorTherapyDate/text()"" />
                </ns0:LAST_SEEN_DATE>
                <ns0:TEST_DATE_QUAL>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_TestDate_Loop/s1:DTP_Date_TestDate/DTP02_DateTimePeriodFormatQualifier/text()"" />
                </ns0:TEST_DATE_QUAL>
                <ns0:TEST_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_TestDate_Loop/s1:DTP_Date_TestDate/DTP03_TestPerformedDate/text()"" />
                </ns0:TEST_DATE>
                <ns0:XRAY_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_LastX_rayDate_2/DTP03_LastX_RayDate/text()"" />
                </ns0:XRAY_DATE>
                <ns0:INTIAL_TREATMENT_DATE>
                  <xsl:value-of select=""s1:DTP_SubLoop_2/s1:DTP_Date_InitialTreatmentDate_2/DTP03_InitialTreatmentDate/text()"" />
                </ns0:INTIAL_TREATMENT_DATE>
                <ns0:AMBULANCE_PAT_COUNT>
                  <xsl:value-of select=""s1:QTY_SubLoop/s1:QTY_AmbulancePatientCount/QTY02_AmbulancePatientCount/text()"" />
                </ns0:AMBULANCE_PAT_COUNT>
                <ns0:OBSTETRIC_UNITS>
                  <xsl:value-of select=""s1:QTY_SubLoop/s1:QTY_ObstetricAnesthesiaAdditionalUnits/QTY02_ObstetricAdditionalUnits/text()"" />
                </ns0:OBSTETRIC_UNITS>
                <ns0:MEA01_REF_ID>
                  <xsl:value-of select=""s1:MEA_TestResult/MEA01_MeasurementReferenceIdentificationCode/text()"" />
                </ns0:MEA01_REF_ID>
                <ns0:MEA02_QUAL>
                  <xsl:value-of select=""s1:MEA_TestResult/MEA02_MeasurementQualifier/text()"" />
                </ns0:MEA02_QUAL>
                <ns0:MEA03_VALUE>
                  <xsl:value-of select=""s1:MEA_TestResult/MEA03_TestResults/text()"" />
                </ns0:MEA03_VALUE>
                <xsl:if test=""string($var:v918)='true'"">
                  <xsl:variable name=""var:v919"" select=""s1:REF_SubLoop_7/s1:REF_AdjustedRepricedLineItemReferenceNumber/REF02_AdjustedRepricedLineItemReferenceNumber/text()"" />
                  <ns0:ADJUSTED_ITEM_REF>
                    <xsl:value-of select=""$var:v919"" />
                  </ns0:ADJUSTED_ITEM_REF>
                </xsl:if>
                <xsl:if test=""string($var:v920)='true'"">
                  <xsl:variable name=""var:v921"" select=""s1:REF_SubLoop_7/s1:REF_MammographyCertificationNumber_2/REF02_MammographyCertificationNumber/text()"" />
                  <ns0:MAMMOGRAPHY_NUM_REF>
                    <xsl:value-of select=""$var:v921"" />
                  </ns0:MAMMOGRAPHY_NUM_REF>
                </xsl:if>
                <xsl:if test=""string($var:v922)='true'"">
                  <xsl:variable name=""var:v923"" select=""s1:REF_SubLoop_7/s1:REF_ReferringClinicalLaboratoryImprovementAmendment_CLIA_FacilityIdentification/REF02_ReferringCLIANumber/text()"" />
                  <ns0:LAB_CLIA_REF>
                    <xsl:value-of select=""$var:v923"" />
                  </ns0:LAB_CLIA_REF>
                </xsl:if>
                <xsl:if test=""string($var:v924)='true'"">
                  <xsl:variable name=""var:v925"" select=""s1:REF_SubLoop_7/s1:REF_ImmunizationBatchNumber/REF02_ImmunizationBatchNumber/text()"" />
                  <ns0:IMM_BATCHNUM_REF>
                    <xsl:value-of select=""$var:v925"" />
                  </ns0:IMM_BATCHNUM_REF>
                </xsl:if>
                <ns0:TAX_AMOUNT>
                  <xsl:value-of select=""s1:AMT_SubLoop_2/s1:AMT_SalesTaxAmount/AMT02_SalesTaxAmount/text()"" />
                </ns0:TAX_AMOUNT>
                <ns0:POSTAGE_FACILITY_AMT>
                  <xsl:value-of select=""s1:AMT_SubLoop_2/s1:AMT_PostageClaimedAmount/AMT02_PostageClaimedAmount/text()"" />
                </ns0:POSTAGE_FACILITY_AMT>
                <ns0:K3_FILE_INFO>
                  <xsl:value-of select=""s1:K3_FileInformation_2/K301_FixedFormatInformation/text()"" />
                </ns0:K3_FILE_INFO>
                <ns0:NTE_LINENOTE>
                  <xsl:value-of select=""s1:NTE_SubLoop/s1:NTE_LineNote/NTE02_LineNoteText/text()"" />
                </ns0:NTE_LINENOTE>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP04_RepricingOrganizationIdentifier"">
                  <ns0:HCP04_ORG_ID>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP04_RepricingOrganizationIdentifier/text()"" />
                  </ns0:HCP04_ORG_ID>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP05_RepricingPerDiemorFlatRateAmount"">
                  <ns0:HCP05_FLAT_RATE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP05_RepricingPerDiemorFlatRateAmount/text()"" />
                  </ns0:HCP05_FLAT_RATE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP06_RepricedApprovedAmbulatoryPatientGroupCode"">
                  <ns0:HCP06_DRGCODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP06_RepricedApprovedAmbulatoryPatientGroupCode/text()"" />
                  </ns0:HCP06_DRGCODE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP07_RepricedApprovedAmbulatoryPatientGroupAmount"">
                  <ns0:HCP07_DRGAMT>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP07_RepricedApprovedAmbulatoryPatientGroupAmount/text()"" />
                  </ns0:HCP07_DRGAMT>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP08_Product_ServiceID"">
                  <ns0:HCP08_REVENUECODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP08_Product_ServiceID/text()"" />
                  </ns0:HCP08_REVENUECODE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP09_ProductorServiceIDQualifier"">
                  <ns0:HCP09_SVCODE_QUAL>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP09_ProductorServiceIDQualifier/text()"" />
                  </ns0:HCP09_SVCODE_QUAL>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP10_RepricedApprovedHCPCSCode"">
                  <ns0:HCP10_SVCODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP10_RepricedApprovedHCPCSCode/text()"" />
                  </ns0:HCP10_SVCODE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP11_UnitorBasisforMeasurementCode"">
                  <ns0:HCP11_UNITS>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP11_UnitorBasisforMeasurementCode/text()"" />
                  </ns0:HCP11_UNITS>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP12_RepricedApprovedServiceUnitCount"">
                  <ns0:HCP12_QUANTITY>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP12_RepricedApprovedServiceUnitCount/text()"" />
                  </ns0:HCP12_QUANTITY>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP13_RejectReasonCode"">
                  <ns0:HCP13_REJECT_CODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP13_RejectReasonCode/text()"" />
                  </ns0:HCP13_REJECT_CODE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP14_PolicyComplianceCode"">
                  <ns0:HCP14_POLICY_CODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP14_PolicyComplianceCode/text()"" />
                  </ns0:HCP14_POLICY_CODE>
                </xsl:if>
                <xsl:if test=""s1:HCP_LinePricing_RepricingInformation/HCP15_ExceptionCode"">
                  <ns0:HCP15_EXCEPTION_CODE>
                    <xsl:value-of select=""s1:HCP_LinePricing_RepricingInformation/HCP15_ExceptionCode/text()"" />
                  </ns0:HCP15_EXCEPTION_CODE>
                </xsl:if>
                <ns0:LIN03_NATIONALDRUG_CODE>
                  <xsl:value-of select=""s1:TS837_2410_Loop/s1:LIN_DrugIdentification/LIN03_NationalDrugCodeorUniversalProductNumber/text()"" />
                </ns0:LIN03_NATIONALDRUG_CODE>
                <ns0:CTP04_NATIONALDRUG_UNIT>
                  <xsl:value-of select=""s1:TS837_2410_Loop/s1:CTP_DrugQuantity/CTP04_NationalDrugUnitCount/text()"" />
                </ns0:CTP04_NATIONALDRUG_UNIT>
                <ns0:CTP05_NATIONALDRUG_QUAL>
                  <xsl:value-of select=""s1:TS837_2410_Loop/s1:CTP_DrugQuantity/s1:C001_CompositeUnitofMeasure_6/C00101_CodeQualifier/text()"" />
                </ns0:CTP05_NATIONALDRUG_QUAL>
                <ns0:PRESCRIPTION_NUMBER>
                  <xsl:value-of select=""$var:v928"" />
                </ns0:PRESCRIPTION_NUMBER>
                <xsl:if test=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00307_ProcedureCodeDescription"">
                  <ns0:SVD03_7_DESCRIPTION>
                    <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/s1:C003_CompositeMedicalProcedureIdentifier_3/C00307_ProcedureCodeDescription/text()"" />
                  </ns0:SVD03_7_DESCRIPTION>
                </xsl:if>
                <xsl:if test=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD06_BundledorUnbundledLineNumber"">
                  <ns0:SVD06_ASSIGNED_NUMBER>
                    <xsl:value-of select=""s1:TS837_2430_Loop/s1:SVD_LineAdjudicationInformation/SVD06_BundledorUnbundledLineNumber/text()"" />
                  </ns0:SVD06_ASSIGNED_NUMBER>
                </xsl:if>
                <ns0:CAS01_ADJ_CODE>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:CAS_LineAdjustment/CAS01_ClaimAdjustmentGroupCode/text()"" />
                </ns0:CAS01_ADJ_CODE>
                <ns0:CAS02_ADJ_REASON>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:CAS_LineAdjustment/CAS02_AdjustmentReasonCode/text()"" />
                </ns0:CAS02_ADJ_REASON>
                <ns0:CAS03_ADJ_AMT>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:CAS_LineAdjustment/CAS03_AdjustmentAmount/text()"" />
                </ns0:CAS03_ADJ_AMT>
                <xsl:if test=""s1:TS837_2430_Loop/s1:CAS_LineAdjustment/CAS04_AdjustmentQuantity"">
                  <ns0:CAS04_ADJ_QTY>
                    <xsl:value-of select=""s1:TS837_2430_Loop/s1:CAS_LineAdjustment/CAS04_AdjustmentQuantity/text()"" />
                  </ns0:CAS04_ADJ_QTY>
                </xsl:if>
                <ns0:LINE_ADJUDICATION_DATE>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:DTP_LineCheckorRemittanceDate/DTP03_AdjudicationorPaymentDate/text()"" />
                </ns0:LINE_ADJUDICATION_DATE>
                <ns0:PATIENT_LIABILITY>
                  <xsl:value-of select=""s1:TS837_2430_Loop/s1:AMT_RemainingPatientLiability_2/AMT02_RemainingPatientLiability/text()"" />
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
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM103_OrderingProviderLastName/text()"" />
                </ns0:ORDERING_PROV_LNAME>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM104_OrderingProviderFirstName"">
                  <ns0:ORDERING_PROV_FNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM104_OrderingProviderFirstName/text()"" />
                  </ns0:ORDERING_PROV_FNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM105_OrderingProviderMiddleNameorInitial"">
                  <ns0:ORDERING_PROV_MNAME>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM105_OrderingProviderMiddleNameorInitial/text()"" />
                  </ns0:ORDERING_PROV_MNAME>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM107_OrderingProviderNameSuffix"">
                  <ns0:ORDERING_PROV_SUFFIX>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM107_OrderingProviderNameSuffix/text()"" />
                  </ns0:ORDERING_PROV_SUFFIX>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM108_IdentificationCodeQualifier"">
                  <ns0:ORDERING_PROV_QUAL>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM108_IdentificationCodeQualifier/text()"" />
                  </ns0:ORDERING_PROV_QUAL>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM109_OrderingProviderIdentifier"">
                  <ns0:ORDERING_PROV_ID>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:NM1_OrderingProviderName/NM109_OrderingProviderIdentifier/text()"" />
                  </ns0:ORDERING_PROV_ID>
                </xsl:if>
                <ns0:ORDERING_PROV_ADD1>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N3_OrderingProviderAddress/N301_OrderingProviderAddressLine/text()"" />
                </ns0:ORDERING_PROV_ADD1>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N3_OrderingProviderAddress/N302_OrderingProviderAddressLine"">
                  <ns0:ORDERING_PROV_ADD2>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N3_OrderingProviderAddress/N302_OrderingProviderAddressLine/text()"" />
                  </ns0:ORDERING_PROV_ADD2>
                </xsl:if>
                <ns0:ORDERING_PROV_CITY>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N4_OrderingProviderCity_State_ZIPCode/N401_OrderingProviderCityName/text()"" />
                </ns0:ORDERING_PROV_CITY>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N4_OrderingProviderCity_State_ZIPCode/N402_OrderingProviderStateorProvinceCode"">
                  <ns0:ORDERING_PROV_STATE>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N4_OrderingProviderCity_State_ZIPCode/N402_OrderingProviderStateorProvinceCode/text()"" />
                  </ns0:ORDERING_PROV_STATE>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N4_OrderingProviderCity_State_ZIPCode/N403_OrderingProviderPostalZoneorZIPCode"">
                  <ns0:ORDERING_PROV_ZIP>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:N4_OrderingProviderCity_State_ZIPCode/N403_OrderingProviderPostalZoneorZIPCode/text()"" />
                  </ns0:ORDERING_PROV_ZIP>
                </xsl:if>
                <ns0:ORDERING_PROV_REF>
                  <xsl:value-of select=""$var:v931"" />
                </ns0:ORDERING_PROV_REF>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER02_OrderingProviderContactName"">
                  <ns0:ORDERING_PER02>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER02_OrderingProviderContactName/text()"" />
                  </ns0:ORDERING_PER02>
                </xsl:if>
                <ns0:ORDERING_PER03>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER03_CommunicationNumberQualifier/text()"" />
                </ns0:ORDERING_PER03>
                <ns0:ORDERING_PER04>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER04_CommunicationNumber/text()"" />
                </ns0:ORDERING_PER04>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER05_CommunicationNumberQualifier"">
                  <ns0:ORDERING_PER05>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER05_CommunicationNumberQualifier/text()"" />
                  </ns0:ORDERING_PER05>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER06_CommunicationNumber"">
                  <ns0:ORDERING_PER06>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER06_CommunicationNumber/text()"" />
                  </ns0:ORDERING_PER06>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER07_CommunicationNumberQualifier"">
                  <ns0:ORDERING_PER07>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER07_CommunicationNumberQualifier/text()"" />
                  </ns0:ORDERING_PER07>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER08_CommunicationNumber"">
                  <ns0:ORDERING_PER08>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420E_Loop/s1:PER_OrderingProviderContactInformation/PER08_CommunicationNumber/text()"" />
                  </ns0:ORDERING_PER08>
                </xsl:if>
                <ns0:AMBULANCE_PICKUP_ADD1>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N3_AmbulancePick_upLocationAddress_2/N301_AmbulancePick_upAddressLine/text()"" />
                </ns0:AMBULANCE_PICKUP_ADD1>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N3_AmbulancePick_upLocationAddress_2/N302_AmbulancePick_upAddressLine"">
                  <ns0:AMBULANCE_PICKUP_ADD2>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N3_AmbulancePick_upLocationAddress_2/N302_AmbulancePick_upAddressLine/text()"" />
                  </ns0:AMBULANCE_PICKUP_ADD2>
                </xsl:if>
                <ns0:AMBULANCE_PICKUP_CITY>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_2/N401_AmbulancePick_upCityName/text()"" />
                </ns0:AMBULANCE_PICKUP_CITY>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_2/N402_AmbulancePick_upStateorProvinceCode"">
                  <ns0:AMBULANCE_PICKUP_STATE>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_2/N402_AmbulancePick_upStateorProvinceCode/text()"" />
                  </ns0:AMBULANCE_PICKUP_STATE>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_2/N403_AmbulancePick_upPostalZoneorZIPCode"">
                  <ns0:AMBULANCE_PICKUP_ZIP>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420G_Loop/s1:N4_AmbulancePick_upLocationCity_State_ZipCode_2/N403_AmbulancePick_upPostalZoneorZIPCode/text()"" />
                  </ns0:AMBULANCE_PICKUP_ZIP>
                </xsl:if>
                <ns0:AMBULANCE_DROPOFF_ADD1>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N3_AmbulanceDrop_offLocationAddress_2/N301_AmbulanceDrop_offAddressLine/text()"" />
                </ns0:AMBULANCE_DROPOFF_ADD1>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N3_AmbulanceDrop_offLocationAddress_2/N302_AmbulanceDrop_offAddressLine"">
                  <ns0:AMBULANCE_DROPOFF_ADD2>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N3_AmbulanceDrop_offLocationAddress_2/N302_AmbulanceDrop_offAddressLine/text()"" />
                  </ns0:AMBULANCE_DROPOFF_ADD2>
                </xsl:if>
                <ns0:AMBULANCE_DROPOFF_CITY>
                  <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_2/N401_AmbulanceDrop_offCityName/text()"" />
                </ns0:AMBULANCE_DROPOFF_CITY>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_2/N402_AmbulanceDrop_offStateorProvinceCode"">
                  <ns0:AMBULANCE_DROPOFF_STATE>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_2/N402_AmbulanceDrop_offStateorProvinceCode/text()"" />
                  </ns0:AMBULANCE_DROPOFF_STATE>
                </xsl:if>
                <xsl:if test=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_2/N403_AmbulanceDrop_offPostalZoneorZIPCode"">
                  <ns0:AMBULANCE_DROPOFF_ZIP>
                    <xsl:value-of select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:N4_AmbulanceDrop_offLocationCity_State_ZipCode_2/N403_AmbulanceDrop_offPostalZoneorZIPCode/text()"" />
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
                <xsl:for-each select=""./*[local-name()='TS837_2430_Loop'][1]"">
          <xsl:element name=""PRI_LINE_PAID_AMT"">
            <xsl:for-each select=""./*[local-name()='SVD_LineAdjudicationInformation']"">
              <xsl:if test="" SVD02_ServiceLinePaidAmount/text() !=''"">
                <xsl:value-of select=""SVD02_ServiceLinePaidAmount/text()"" />
              </xsl:if>
            </xsl:for-each>
          </xsl:element>
</xsl:for-each>
                <xsl:for-each select=""./*[local-name()='TS837_2430_Loop'][2]"">
          <xsl:element name=""SEC_LINE_PAID_AMT"">
            <xsl:for-each select=""./*[local-name()='SVD_LineAdjudicationInformation']"">
              <xsl:if test="" SVD02_ServiceLinePaidAmount/text() !=''"">
                <xsl:value-of select=""SVD02_ServiceLinePaidAmount/text()"" />
              </xsl:if>
            </xsl:for-each>
          </xsl:element>
</xsl:for-each>
                <xsl:if test=""s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00307_Description"">
                  <ns0:PROCEDURE_DESCRIPTION>
                    <xsl:value-of select=""s1:SV1_ProfessionalService/s1:C003_CompositeMedicalProcedureIdentifier/C00307_Description/text()"" />
                  </ns0:PROCEDURE_DESCRIPTION>
                </xsl:if>
                <xsl:if test=""string($var:v933)='true'"">
                  <xsl:variable name=""var:v934"" select=""s1:DTP_SubLoop_2/s1:DTP_Date_ServiceDate/DTP03_ServiceDate/text()"" />
                  <ns0:SERVICE_FROM_DATE>
                    <xsl:value-of select=""$var:v934"" />
                  </ns0:SERVICE_FROM_DATE>
                </xsl:if>
                <xsl:if test=""string($var:v935)='true'"">
                  <xsl:variable name=""var:v938"" select=""string($var:v937)"" />
                  <ns0:SERVICE_FROM_DATE>
                    <xsl:value-of select=""$var:v938"" />
                  </ns0:SERVICE_FROM_DATE>
                </xsl:if>
                <xsl:if test=""string($var:v935)='true'"">
                  <xsl:variable name=""var:v940"" select=""string($var:v939)"" />
                  <ns0:SERVICE_THROUGH_DATE>
                    <xsl:value-of select=""$var:v940"" />
                  </ns0:SERVICE_THROUGH_DATE>
                </xsl:if>
                <xsl:if test=""s1:CR1_AmbulanceTransportInformation_2/CR110_StretcherPurposeDescription"">
                  <ns0:AMBULANCE_STRETCHER_DESC>
                    <xsl:value-of select=""s1:CR1_AmbulanceTransportInformation_2/CR110_StretcherPurposeDescription/text()"" />
                  </ns0:AMBULANCE_STRETCHER_DESC>
                </xsl:if>
                <xsl:if test=""string($var:v941)='true'"">
                  <xsl:variable name=""var:v942"" select=""s1:NM1_SubLoop_6/s1:TS837_2420H_Loop/s1:NM1_AmbulanceDrop_offLocation_2/NM103_AmbulanceDrop_offLocation/text()"" />
                  <ns0:AMBULANCE_DROPOFF_NAME>
                    <xsl:value-of select=""$var:v942"" />
                  </ns0:AMBULANCE_DROPOFF_NAME>
                </xsl:if>
              </ns0:CLAIM_ADDTNL_DETAIL>
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
     bool HeaderRemitDateBool = System.Convert.ToBoolean(HeaderremitdateExistence);
	if(HeaderRemitDateBool)
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


public string PayToProviderIDQual(string G2CheckString, string RefIDQual)
{
  bool G2Check = System.Convert.ToBoolean(G2CheckString);

	if(G2Check)
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
		return patadd1;
	}
	else
	{
		return sbradd1;
	}
}


public string PATADDRESSST( string patadd2, string sbradd2,int PatExistence)
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


public int nHaveData(string bExist, int nSize)  
{
	if(System.Convert.ToBoolean(bExist) && nSize>0)
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
                return  string.Empty;
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


public string SubConditionCodes(string C022_CD1, string C022_CD2, string C022_CD3, string C022_CD4, string C022_CD5, string C022_CD6, string C022_CD7, string C022_CD8,string C022_CD9,string C022_CD10,string C022_CD11,string C022_CD12)
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

public string SubServiceModifierList(string P303, string PM304, string PM305, string PM306)
{
	string ModList = string.Empty;

	if(!string.IsNullOrEmpty(P303))
	{
		ModList = P303;
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

public int bHaveData(string bExist, int nSize)
{
   if(System.Convert.ToBoolean(bExist) && nSize>0)
           return 1;
   else
            return 0;
}

public string fCommon(string param1, bool bparam2)
{
          if(bparam2)
	return param1;
         else
               return """";
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



public string MyConcat(bool bExising, string sAdd2)
{
              if(!bExising)
 	return """";
             else 
               return sAdd2;

}


public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7, string param8, string param9, string param10, string param11, string param12, string param13, string param14, string param15)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 + param10 + param11 + param12 + param13 + param14 + param15;
}


public string StringConcat(string param0, string param1)
{
   return param0 + param1;
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

public string StringConcat(string param0, string param1, string param2, string param3, string param4, string param5, string param6, string param7, string param8, string param9, string param10, string param11, string param12, string param13, string param14, string param15, string param16, string param17, string param18, string param19, string param20, string param21, string param22, string param23)
{
   return param0 + param1 + param2 + param3 + param4 + param5 + param6 + param7 + param8 + param9 + param10 + param11 + param12 + param13 + param14 + param15 + param16 + param17 + param18 + param19 + param20 + param21 + param22 + param23;
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
