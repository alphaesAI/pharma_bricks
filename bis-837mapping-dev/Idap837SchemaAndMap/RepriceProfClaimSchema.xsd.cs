namespace Idap837SchemaAndMap {
    using Microsoft.XLANGs.BaseTypes;
    
    
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.BizTalk.Schema.Compiler", "3.0.1.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    [SchemaType(SchemaTypeEnum.Document)]
    [Schema(@"https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim",@"Integration_Professional_Claims")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.EDI_SUBMITTER_ID", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_SUBMITTER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.EDI_RECEIVER_ID", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_RECEIVER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICE_CLAIM_ADDTNL.EDI_SUBMITTER_ID", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICE_CLAIM_ADDTNL' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_SUBMITTER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.CLAIM_ID", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='CLAIM_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.PRIMARY_PAYER_NAME", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PRIMARY_PAYER_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.PAY_TO_PROVIDER_NAME", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PAY_TO_PROVIDER_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.PROVIDER_LAST_NAME", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PROVIDER_LAST_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICED_CLAIM.INSURED_LAST_NAME", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='INSURED_LAST_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "REPRICE_CLAIM_ADDTNL.SOURCE_FILE_NAME", XPath = @"/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICE_CLAIM_ADDTNL' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='SOURCE_FILE_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']", XsdType = @"string")]
    [System.SerializableAttribute()]
    [SchemaRoots(new string[] {@"Integration_Professional_Claims"})]
    public sealed class RepriceProfClaimSchema : Microsoft.XLANGs.BaseTypes.SchemaBase {
        
        [System.NonSerializedAttribute()]
        private static object _rawSchema;
        
        [System.NonSerializedAttribute()]
        private const string _strSchema = @"<?xml version=""1.0"" encoding=""utf-16""?>
<xs:schema xmlns:b=""http://schemas.microsoft.com/BizTalk/2003"" xmlns:tns=""https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim"" attributeFormDefault=""unqualified"" elementFormDefault=""qualified"" targetNamespace=""https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim"" xmlns:xs=""http://www.w3.org/2001/XMLSchema"">
  <xs:element name=""Integration_Professional_Claims"">
    <xs:annotation>
      <xs:appinfo>
        <b:properties>
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_SUBMITTER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_RECEIVER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICE_CLAIM_ADDTNL' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='EDI_SUBMITTER_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='CLAIM_ID' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PRIMARY_PAYER_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PAY_TO_PROVIDER_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='PROVIDER_LAST_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICED_CLAIM' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='INSURED_LAST_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Integration_Professional_Claims' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='REPRICE_CLAIM_ADDTNL' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']/*[local-name()='SOURCE_FILE_NAME' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.RepriceProfessionalClaim']"" />
        </b:properties>
      </xs:appinfo>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs=""0"" name=""REPRICED_CLAIM"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element name=""RECEIVE_TIME"" type=""xs:string"" />
              <xs:element name=""DETAIL_COUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TOTAL_CHARGES"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AUTHORIZATION_NUMBER"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COB_STATUS"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAID_BY_PRIMARY_PAYER"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PAYER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUB_PAYER_ID"" type=""xs:string"" />
              <xs:element name=""SUBSCRIBER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEMBER_SUFFIX"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""FIRST_SERVICE_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EXTERNAL_CLAIM_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_CONTROL_NUMBER"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEDICAL_RECORD_NUMBER"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PRIMARY_PAYER_NAME"" type=""xs:string"" />
              <xs:element name=""PRIMARY_PAYER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ID_QUAL"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_NPI_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PAY_TO_PROVIDER_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_TAX_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PAY_TO_PROVIDER_ADDRESS1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ADDRESS2"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PAY_TO_PROVIDER_CITY"" type=""xs:string"" />
              <xs:element name=""PAY_TO_PROVIDER_STATE"" type=""xs:string"" />
              <xs:element name=""PAY_TO_PROVIDER_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_NPI_ID"" type=""xs:string"" />
              <xs:element name=""PROVIDER_LAST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_MIDDLE_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_NAME_SUFFIX"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_ID_TAX_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_ADDRESS1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_ADDRESS2"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PROVIDER_CITY"" type=""xs:string"" />
              <xs:element name=""PROVIDER_STATE"" type=""xs:string"" />
              <xs:element name=""PROVIDER_ZIP"" type=""xs:string"" />
              <xs:element name=""INSURED_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_SUFFIX"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_GROUP_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""INSURED_LAST_NAME"" type=""xs:string"" />
              <xs:element name=""INSURED_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_MIDDLE_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""INSURED_GENDER"" type=""xs:string"" />
              <xs:element name=""INSURED_BIRTH_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_MEMBER_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PATIENT_LAST_NAME"" type=""xs:string"" />
              <xs:element name=""PATIENT_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_MIDDLE_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""PATIENT_GENDER"" type=""xs:string"" />
              <xs:element name=""PATIENT_BIRTH_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAID_BY_MEMBER"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EOB_NOTE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROVIDER_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROVIDER_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EDI_SUBMITTER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EDI_RECEIVER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EDI_CORRECTION_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EDI_PAY_TO_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROVIDER_SIGNATURE_FILE_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEDICARE_ASSIGNMENT_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ASSIGNMENT_BENEFIT_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RELEASE_INFO_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_SIGNATURE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CONDITION_EMPLOYMENT"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CONDITION_OTHER_ACCIDENT"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CONDITION_AUTO_ACCIDENT"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AUTO_ACCIDENT_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SPECIAL_PROGRAM_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PARTICIPATION_AGREEMENT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DELAY_REASON_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_EXTID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_EXTID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REJECTIONCODESLIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_NPI"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_TAXID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ADD1"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ADD2"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_CITY"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_STATE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ZIP"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICER_RECVD_DATE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_LIABILTY_AMT"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_ADD1"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_ADD2"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_CITY"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_STATE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_ZIP"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_SUFFIX_NAME"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""COB_INDICATOR"" type=""xs:string"" />
              <xs:element name=""ICD_VERSION_IND"" type=""xs:string"" />
              <xs:element name=""PRIMARY_PAID_DATE"" type=""xs:string"" />
              <xs:element name=""PATIENT_ADD1"" type=""xs:string"" />
              <xs:element name=""PATIENT_ADD2"" type=""xs:string"" />
              <xs:element name=""PATIENT_CITY"" type=""xs:string"" />
              <xs:element name=""PATIENT_STATE"" type=""xs:string"" />
              <xs:element name=""PATIENT_ZIP"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" maxOccurs=""unbounded"" name=""REPRICE_CLAIM_DETAIL"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element name=""LINE_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CORRECTION_LEVEL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TOTAL_CHARGES"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""UNIT_MEASUREMENT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""QUANTITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""UNIT_RATE"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""REPRICE_PROF_CLAIM"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CORRECTION_LEVEL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_INSURANCE_FLAG"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FIRST_SYMPTOM_DATE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FIRST_SIMILAR_SYMPTOM_DATE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LOSS_OF_WORK_BEGIN"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LOSS_OF_WORK_END"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HOSPITALIZATION_BEGIN"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HOSPITALIZATION_END"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULATORY_PATIENT_GROUP"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_EMP_STATUS"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_MARRIED_STATUS"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LOCATION_CODE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_FREQUENCY_CODE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLIA_NUMBER"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_1"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_2"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_3"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_4"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_5"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_6"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_7"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_8"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_9"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_10"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_11"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICD9_12"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICE_CHARGES"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CONDITION_CODES_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PHYSICIAN_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PHYSICIAN_NPI_ID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PHYSICIAN_LNAME"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PHYSICIAN_FNAME"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PHYSICIAN_MNAME"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""OTHER_DATE_QUAL"" type=""xs:string"" />
              <xs:element name=""OTHER_DATE"" type=""xs:string"" />
              <xs:element name=""FIRST_SYMPTOM_DATE_QUAL"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element maxOccurs=""unbounded"" name=""REPRICE_PROF_DETAIL"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element name=""LINE_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CORRECTION_LEVEL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_CODE_QUALIFIER"" type=""xs:string"" />
              <xs:element name=""SERVICE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_MODIFIER_LIST"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""SERVICE_FROM_DATE"" type=""xs:string"" />
              <xs:element name=""SERVICE_TO_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LOCATION_CODE"" nillable=""true"" type=""xs:string"" />
              <xs:element name=""DIAGNOSIS_CODE_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""NDC_CODE_LIST"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TYPE_OF_SERVICE"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EMERGENCY_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EPSDT_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FAMILY_PLAN_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COPAY_WAVIER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PROV_LINEITEM_NUM"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COB_PAID"" nillable=""true"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICE_CHARGES"" type=""xs:string"" />
              <xs:element name=""DIAGNOSIS_IDX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TP_ORG_NOTES"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINEITEM_CONTROL_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OBS_ANESTHSIA_ADDTNL_UNITS"" type=""xs:string"" />
              <xs:element name=""PATIENT_LIABILTY_AMT"" type=""xs:string"" />
              <xs:element name=""NATIONAL_DRUG_COUNT"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""REPRICE_CLAIM_ADDTNL"">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs=""0"" name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PAYTO_TAX_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PAYTO_TAXONOMY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER01"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER02"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER03"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER04"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER05"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER06"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER07"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_PER08"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_TAXONOMY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_REN_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_TAXONOMY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_TAXONOMY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER01"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER02"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER03"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER04"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER05"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_PER06"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ENTITY_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_SEQ_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_RELATION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_GROUP_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_INS_TYPE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_CLAIM_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIMARY_PAYER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_GROUP_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_PAYER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_PAYER_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_LAST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_MIDDLE_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_GENDER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_BIRTH_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_DEATH"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_UOM"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_WEIGHT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INSURED_PRG_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_RELATION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_LAST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_MIDDLE_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_GENDER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_BIRTH_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_DEATH"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_UOM"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_WEIGHT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_PRG_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPORT_TYPE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRANSMISSION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ID_CODER_QUALIFIER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CONTROL_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FIXED_FORMAT_INFO"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DRUG_PROD_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""NATIONAL_DRUG_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DRUG_UNIT_PRICE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DRUG_UNIT_COUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DRUG_CODE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRE_CODE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRE_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ENTITYQUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_LASTNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_ZIPCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAY_TO_PLAN_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_SEQ_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_RELATION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_GROUP_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_GROUP_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_CLAIM_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INS_TYPE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_ASSIGN_BENRFIT_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAT_SIGN_SRC_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_RELEASE_INFO_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_GENDER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_DOB"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_CAS01_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_CAS02_REASON"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_CAS03_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYERPAID_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_NONCOVERED_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_LIABILITY_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SSN_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_ZIPCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_REMITTANCE_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_PAYER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_REFERING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_REFERING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_RENDERING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_RENDERING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SERVICEFACILITY_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SERVICEFACILITY_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SUPERVISING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_SUPERVISING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_BILLING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_BILLING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_SEQ_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_RELATION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_GROUP_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_GROUP_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_CLAIM_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INS_TYPE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_ASSIGN_BENRFIT_IND"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAT_SIGN_SRC_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_RELEASE_INFO_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ID_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_GENDER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_DOB"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_CAS01_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_CAS02_REASON"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_CAS03_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYERPAID_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_NONCOVERED_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_LIABILITY_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SSN_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_ZIPCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_REMITTANCE_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_PAYER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_REFERING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_REFERING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_RENDERING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_RENDERING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SERVICEFACILITY_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SERVICEFACILITY_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SUPERVISING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_SUPERVISING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_BILLING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_BILLING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""EDI_SUBMITTER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILLING_NOTE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILLING_NOTE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_NOTE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_NOTE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_ESTAMT_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_ESTAMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_QTY_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_QTY_DAYSCNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLAIM_QTY_UOM"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CURRENT_ILLNESS_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ACCIDENT_DATE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ACCIDENT_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ANESTHESIA_PROC_HI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ANESTHESIA_CONDITION_HI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ANESTHESIA_TREATMENTCODE_HI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AUTO_ACCIDENT_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HIPAA_VERSION_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRANSACTION_SET_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BATCH_CONTROL_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUBMITTER_QUALIFIER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUBMITTER_LAST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUBMITTER_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUBMITTER_MIDDLE_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUBMITTER_ID_NM109"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RECEIVER_QUALIFIER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RECEIVER_LAST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RECEIVER_FIRST_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RECEIVER_MIDDLE_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RECEIVER_ID_NM109"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SOURCE_FILE_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS_ADJ_CODE_PAYER_A_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS_ADJ_CODE_PAYER_B_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_ADDRESS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PAYER_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_SECID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_SECID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_MIA_RESERVE_DAYS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_MIA_RESERVE_DAYS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_REMARK_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_REMARK_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_ADDRESS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_ADDRESS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COB_NONCOVEREDAMOUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COB_ALLOWEDAMOUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""COB_TOTALSUBMITTEDCHARGES"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""BILL_PROVIDER_NPI_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REN_PROVIDER_NPI_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AREF_PROVIDER_NPI_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPER_PROVIDER_NPI_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_PROV_NPI_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_NPI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OPERATING_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_NPI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_NPI"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ATTENDING_PROVIDER_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ATTENDING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_ATTENDING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_OPERATING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SEC_INSURED_OPERATING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ATTENDING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_ATTENDING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_OPERATING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TRI_INSURED_OPERATING_REF"" type=""xs:string"" />
              <xs:element name=""RECEIVER_ID"" type=""xs:string"" />
              <xs:element name=""COB_PAYERPAIDAMOUNT"" type=""xs:string"" />
              <xs:element name=""COB_PATIENTRESPONSIBILITYACTUAL"" type=""xs:string"" />
              <xs:element name=""COB_DISCOUNTAMOUNT"" type=""xs:string"" />
              <xs:element name=""SEC_COB_PAYERPAIDAMOUNT"" type=""xs:string"" />
              <xs:element name=""SEC_COB_PATIENTRESPONSIBILITYACTUAL"" type=""xs:string"" />
              <xs:element name=""SEC_COB_DISCOUNTAMOUNT"" type=""xs:string"" />
              <xs:element name=""SEC_COB_NONCOVEREDAMOUNT"" type=""xs:string"" />
              <xs:element name=""REPRICED_CLAIM_NUMBER"" type=""xs:string"" />
              <xs:element name=""CONTRACT_TYPE"" type=""xs:string"" />
              <xs:element name=""CONTRACT_AMOUNT"" type=""xs:string"" />
              <xs:element name=""CONTRACT_PERCENTAGE"" type=""xs:string"" />
              <xs:element name=""CONTRACT_CODE"" type=""xs:string"" />
              <xs:element name=""TERMS_DISCNT_PERCNT"" type=""xs:string"" />
              <xs:element name=""CONTRACT_VER_IDENT"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_DESCRIPTION"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_STRETCHER_DESC"" type=""xs:string"" />
              <xs:element name=""CRC03_AMBULANCE_CODE1"" type=""xs:string"" />
              <xs:element name=""CRC04_AMBULANCE_CODE2"" type=""xs:string"" />
              <xs:element name=""CRC05_AMBULANCE_CODE3"" type=""xs:string"" />
              <xs:element name=""CRC06_AMBULANCE_CODE4"" type=""xs:string"" />
              <xs:element name=""CRC07_AMBULANCE_CODE5"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_WEIGHT"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_QTY"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_REASON_CODE"" type=""xs:string"" />
              <xs:element name=""CLIA_REF"" type=""xs:string"" />
              <xs:element name=""CRC_EPSDT_COND1"" type=""xs:string"" />
              <xs:element name=""CRC_EPSDT_COND2"" type=""xs:string"" />
              <xs:element name=""CRC_EPSDT_COND3"" type=""xs:string"" />
              <xs:element name=""MAMMOGRAPHY_NUM_REF"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_DROPOFF_NAME"" type=""xs:string"" />
              <xs:element name=""CRC02_AMBULANCE_RESPONSECODE"" type=""xs:string"" />
              <xs:element name=""CR209_SPINAL_COND_CODE"" type=""xs:string"" />
              <xs:element name=""CR210_PATIENT_COND_DESC1"" type=""xs:string"" />
              <xs:element name=""CR211_PATIENT_COND_DESC2"" type=""xs:string"" />
              <xs:element name=""REPORT_PWK06_ID"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element maxOccurs=""unbounded"" name=""REPRICE_CLAIM_ADDTNL_DETAIL"">
          <xs:complexType>
            <xs:sequence>
              <xs:element minOccurs=""0"" name=""CLAIM_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPORT_TYPECODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPORT_TRANCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRESCRIPTION_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICEDLINE_ITEM_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRAL_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRIOR_AUTHORIZATION"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CLIA"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINECONTROL_NUM"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""NTE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""NTE_DESCRIPTION"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICE_METHOD"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICE_ALLOWED_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPRICE_SAVING_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_TAXONOMY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_PROV_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""RENDERING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FACILITY_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SUPERVISING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_PROV_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REFERRING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_PCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_MOD"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_QTY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LQ_FRM_TYPE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LQ_FRM_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FRM_ASSIGNED"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FRM_QUESTION"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FRM_RESPONSE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FRM_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""FRM_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS_ADJ_CODE_PAYER_A_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS_ADJ_CODE_PAYER_B_LIST"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_A_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTHER_PAYER_B_NAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SERVICE_CODE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REVENUE_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REPORT_PWK06_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""DURABLE_TRANS_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_WEIGHT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_REASON_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_QTY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DESCRIPTION"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CR301_AMBULANCE_typeCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CR303_AMBULANCE_QTY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC02_AMBULANCE_RESPONSECODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC03_AMBULANCE_CODE1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC04_AMBULANCE_CODE2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC05_AMBULANCE_CODE3"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC06_AMBULANCE_CODE4"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC07_AMBULANCE_CODE5"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC02_HOSPICE_RESPONSECODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC02_DURABLE_RESPONSECODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CRC02_DURABLE_CONDITIONCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""REVISION_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""THERAPY_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LAST_CERTIFICATION_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LAST_SEEN_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TEST_DATE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TEST_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""XRAY_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""INTIAL_TREATMENT_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PAT_COUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OBSTETRIC_UNITS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEA01_REF_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEA02_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MEA03_VALUE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ADJUSTED_ITEM_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""MAMMOGRAPHY_NUM_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LAB_CLIA_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""IMM_BATCHNUM_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""TAX_AMOUNT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""POSTAGE_FACILITY_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""K3_FILE_INFO"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""NTE_LINENOTE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP04_ORG_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP05_FLAT_RATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP06_DRGCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP07_DRGAMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP08_REVENUECODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP09_SVCODE_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP10_SVCODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP11_UNITS"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP12_QUANTITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP13_REJECT_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP14_POLICY_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""HCP15_EXCEPTION_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LIN03_NATIONALDRUG_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CTP04_NATIONALDRUG_UNIT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CTP05_NATIONALDRUG_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PRESCRIPTION_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SVD03_7_DESCRIPTION"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""SVD06_ASSIGNED_NUMBER"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS01_ADJ_CODE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS02_ADJ_REASON"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS03_ADJ_AMT"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""CAS04_ADJ_QTY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""LINE_ADJUDICATION_DATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PATIENT_LIABILITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_PROV_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""OTH_OPERATING_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_LNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_FNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_MNAME"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_SUFFIX"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_QUAL"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_ID"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PROV_REF"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER02"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER03"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER04"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER05"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER06"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER07"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ORDERING_PER08"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_PICKUP_ZIP"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ADD1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ADD2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_CITY"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_STATE"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""AMBULANCE_DROPOFF_ZIP"" type=""xs:string"" />
              <xs:element name=""PRI_LINE_PAID_AMT"" type=""xs:string"" />
              <xs:element name=""SEC_LINE_PAID_AMT"" type=""xs:string"" />
              <xs:element name=""PROCEDURE_DESCRIPTION"" type=""xs:string"" />
              <xs:element name=""SERVICE_FROM_DATE"" type=""xs:string"" />
              <xs:element name=""SERVICE_THROUGH_DATE"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_STRETCHER_DESC"" type=""xs:string"" />
              <xs:element name=""AMBULANCE_DROPOFF_NAME"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>";
        
        public RepriceProfClaimSchema() {
        }
        
        public override string XmlContent {
            get {
                return _strSchema;
            }
        }
        
        public override string[] RootNodes {
            get {
                string[] _RootElements = new string [1];
                _RootElements[0] = "Integration_Professional_Claims";
                return _RootElements;
            }
        }
        
        protected override object RawSchema {
            get {
                return _rawSchema;
            }
            set {
                _rawSchema = value;
            }
        }
    }
}
