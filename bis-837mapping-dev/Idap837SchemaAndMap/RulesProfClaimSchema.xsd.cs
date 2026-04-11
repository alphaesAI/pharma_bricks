namespace Idap837SchemaAndMap {
    using Microsoft.XLANGs.BaseTypes;
    
    
    [global::System.CodeDom.Compiler.GeneratedCodeAttribute("Microsoft.BizTalk.Schema.Compiler", "3.0.1.0")]
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute()]
    [global::System.Runtime.CompilerServices.CompilerGeneratedAttribute()]
    [SchemaType(SchemaTypeEnum.Document)]
    [Schema(@"https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent",@"Prof_Claim")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "RulesToCheck", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='RulesToCheck' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "ExternalClaimID", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ExternalClaimID' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "PatientControlNumber", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='PatientControlNumber' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "ConfigReceiveDateBool", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ConfigReceiveDateBool' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "Claim_ID", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Claim_ID' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "PayToProvider.PayToProvStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='PayToProvider' and namespace-uri()='']/*[local-name()='PayToProvStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "BillingProvider.BillProvStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='BillingProvider' and namespace-uri()='']/*[local-name()='BillProvStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "RenderingProvider.RenProvStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='RenderingProvider' and namespace-uri()='']/*[local-name()='RenProvStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "ReferringProvider.RefProvStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ReferringProvider' and namespace-uri()='']/*[local-name()='RefProvStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "ServiceProvider.SvcProvStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ServiceProvider' and namespace-uri()='']/*[local-name()='SvcProvStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "Insured.InsStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Insured' and namespace-uri()='']/*[local-name()='InsStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "Insured.InsErrCode", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Insured' and namespace-uri()='']/*[local-name()='InsErrCode' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "Payer.PayerStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Payer' and namespace-uri()='']/*[local-name()='PayerStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "GroupNumber.GroupStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='GroupNumber' and namespace-uri()='']/*[local-name()='GroupStatus' and namespace-uri()='']", XsdType = @"string")]
    [Microsoft.XLANGs.BaseTypes.DistinguishedFieldAttribute(typeof(System.String), "AuthNumber.AuthNumberStatus", XPath = @"/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='AuthNumber' and namespace-uri()='']/*[local-name()='AuthNumberStatus' and namespace-uri()='']", XsdType = @"string")]
    [System.SerializableAttribute()]
    [SchemaRoots(new string[] {@"Prof_Claim"})]
    public sealed class RulesProfClaimSchema : Microsoft.XLANGs.BaseTypes.SchemaBase {
        
        [System.NonSerializedAttribute()]
        private static object _rawSchema;
        
        [System.NonSerializedAttribute()]
        private const string _strSchema = @"<?xml version=""1.0"" encoding=""utf-16""?>
<xs:schema xmlns=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent"" xmlns:b=""http://schemas.microsoft.com/BizTalk/2003"" targetNamespace=""https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent"" xmlns:xs=""http://www.w3.org/2001/XMLSchema"">
  <xs:element name=""Prof_Claim"">
    <xs:annotation>
      <xs:appinfo>
        <b:properties>
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='RulesToCheck' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ExternalClaimID' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='PatientControlNumber' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ConfigReceiveDateBool' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Claim_ID' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='PayToProvider' and namespace-uri()='']/*[local-name()='PayToProvStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='BillingProvider' and namespace-uri()='']/*[local-name()='BillProvStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='RenderingProvider' and namespace-uri()='']/*[local-name()='RenProvStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ReferringProvider' and namespace-uri()='']/*[local-name()='RefProvStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='ServiceProvider' and namespace-uri()='']/*[local-name()='SvcProvStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Insured' and namespace-uri()='']/*[local-name()='InsStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Insured' and namespace-uri()='']/*[local-name()='InsErrCode' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='Payer' and namespace-uri()='']/*[local-name()='PayerStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='GroupNumber' and namespace-uri()='']/*[local-name()='GroupStatus' and namespace-uri()='']"" />
          <b:property distinguished=""true"" xpath=""/*[local-name()='Prof_Claim' and namespace-uri()='https://Integration.BIZ.CLMIB.Schemas.Prof.ProfClaimsRulesComponent']/*[local-name()='AuthNumber' and namespace-uri()='']/*[local-name()='AuthNumberStatus' and namespace-uri()='']"" />
        </b:properties>
      </xs:appinfo>
    </xs:annotation>
    <xs:complexType>
      <xs:sequence minOccurs=""0"">
        <xs:element name=""Claim_ID"" type=""xs:string"" />
        <xs:element name=""RulesToCheck"" type=""xs:string"" />
        <xs:element name=""ExternalClaimID"" type=""xs:string"" />
        <xs:element name=""PatientControlNumber"" type=""xs:string"" />
        <xs:element name=""ConfigReceiveDateBool"" type=""xs:string"" />
        <xs:element name=""PayToProvider"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""PayToProvID"" type=""xs:string"" />
              <xs:element name=""PayToProvNPID"" type=""xs:string"" />
              <xs:element name=""PayToProvTaxId"" type=""xs:string"" />
              <xs:element default=""0"" name=""PayToProvLName"" type=""xs:string"" />
              <xs:element name=""PayToProvFName"" type=""xs:string"" />
              <xs:element name=""PayToProvMName"" type=""xs:string"" />
              <xs:element name=""PayToProvSuff"" type=""xs:string"" />
              <xs:element name=""PayToProvCity"" type=""xs:string"" />
              <xs:element name=""PayToProvState"" type=""xs:string"" />
              <xs:element name=""PayToProvZip"" type=""xs:string"" />
              <xs:element name=""PayToProvAdd1"" type=""xs:string"" />
              <xs:element name=""PayToProvAdd2"" type=""xs:string"" />
              <xs:element default=""02"" name=""PayToProvStatus"" type=""xs:string"" />
              <xs:element name=""PayToProvErrCode"" type=""xs:string"" />
              <xs:element default=""2"" name=""PayToProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""BillingProvider"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""BillProvID"" type=""xs:string"" />
              <xs:element name=""BillProvNPID"" type=""xs:string"" />
              <xs:element name=""BillProvTaxId"" type=""xs:string"" />
              <xs:element name=""BillProvLName"" type=""xs:string"" />
              <xs:element name=""BillProvFName"" type=""xs:string"" />
              <xs:element name=""BillProvMName"" type=""xs:string"" />
              <xs:element name=""BillProvSuff"" type=""xs:string"" />
              <xs:element name=""BillProvCity"" type=""xs:string"" />
              <xs:element name=""BillProvState"" type=""xs:string"" />
              <xs:element name=""BillProvZip"" type=""xs:string"" />
              <xs:element name=""BillProvAdd1"" type=""xs:string"" />
              <xs:element name=""BillProvAdd2"" type=""xs:string"" />
              <xs:element default=""02"" name=""BillProvStatus"" type=""xs:string"" />
              <xs:element name=""BillProvErrCode"" type=""xs:string"" />
              <xs:element default=""2"" name=""BillProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""RenderingProvider"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""RenProvId"" type=""xs:string"" />
              <xs:element name=""RenProvNPID"" type=""xs:string"" />
              <xs:element name=""RenProvTaxId"" type=""xs:string"" />
              <xs:element name=""RenProvLName"" type=""xs:string"" />
              <xs:element name=""RenProvFName"" type=""xs:string"" />
              <xs:element name=""RenProvMName"" type=""xs:string"" />
              <xs:element name=""RenProvSuff"" type=""xs:string"" />
              <xs:element name=""RenProvCity"" type=""xs:string"" />
              <xs:element name=""RenProvState"" type=""xs:string"" />
              <xs:element name=""RenProvZip"" type=""xs:string"" />
              <xs:element name=""RenProvAdd1"" type=""xs:string"" />
              <xs:element name=""RenProvAdd2"" type=""xs:string"" />
              <xs:element default=""02"" name=""RenProvStatus"" type=""xs:string"" />
              <xs:element name=""RenProvErrCode"" type=""xs:string"" />
              <xs:element default=""1"" name=""RenProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""RenderingProviderLine1"">
          <xs:complexType>
            <xs:sequence minOccurs=""0"">
              <xs:element name=""RenProvId"" type=""xs:string"" />
              <xs:element name=""RenProvNPID"" type=""xs:string"" />
              <xs:element name=""RenProvTaxId"" type=""xs:string"" />
              <xs:element name=""RenProvLName"" type=""xs:string"" />
              <xs:element name=""RenProvFName"" type=""xs:string"" />
              <xs:element name=""RenProvMName"" type=""xs:string"" />
              <xs:element name=""RenProvSuff"" type=""xs:string"" />
              <xs:element name=""RenProvCity"" type=""xs:string"" />
              <xs:element name=""RenProvState"" type=""xs:string"" />
              <xs:element name=""RenProvZip"" type=""xs:string"" />
              <xs:element name=""RenProvAdd1"" type=""xs:string"" />
              <xs:element name=""RenProvAdd2"" type=""xs:string"" />
              <xs:element default=""02"" name=""RenProvStatus"" type=""xs:string"" />
              <xs:element name=""RenProvErrCode"" type=""xs:string"" />
              <xs:element default=""1"" name=""RenProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""ReferringProvider"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""RefProvId"" type=""xs:string"" />
              <xs:element name=""RefProvNPId"" type=""xs:string"" />
              <xs:element name=""RefProvTaxID"" type=""xs:string"" />
              <xs:element name=""RefProvLName"" type=""xs:string"" />
              <xs:element name=""RefProvFName"" type=""xs:string"" />
              <xs:element name=""RefProvMName"" type=""xs:string"" />
              <xs:element name=""RefProvSuff"" type=""xs:string"" />
              <xs:element name=""RefProvCity"" type=""xs:string"" />
              <xs:element name=""RefProvState"" type=""xs:string"" />
              <xs:element name=""RefProvZip"" type=""xs:string"" />
              <xs:element name=""RefProvAdd1"" type=""xs:string"" />
              <xs:element name=""RefProvAdd2"" type=""xs:string"" />
              <xs:element name=""ReferringPhysicianID"" type=""xs:string"" />
              <xs:element default=""02"" name=""RefProvStatus"" type=""xs:string"" />
              <xs:element name=""RefProvErrCode"" type=""xs:string"" />
              <xs:element default=""3"" name=""RefProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""ServiceProvider"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""SvcProvId"" type=""xs:string"" />
              <xs:element name=""SvcProvNPId"" type=""xs:string"" />
              <xs:element name=""SvcProvTaxId"" type=""xs:string"" />
              <xs:element name=""SvcProvLName"" type=""xs:string"" />
              <xs:element name=""SvcProvFName"" type=""xs:string"" />
              <xs:element name=""SvcProvMName"" type=""xs:string"" />
              <xs:element name=""SvcProvSuff"" type=""xs:string"" />
              <xs:element name=""SvcProvCity"" type=""xs:string"" />
              <xs:element name=""SvcProvState"" type=""xs:string"" />
              <xs:element name=""SvcProvZip"" type=""xs:string"" />
              <xs:element name=""SvcProvAdd1"" type=""xs:string"" />
              <xs:element name=""SvcProvAdd2"" type=""xs:string"" />
              <xs:element default=""02"" name=""SvcProvStatus"" type=""xs:string"" />
              <xs:element name=""SvcProvErrCode"" type=""xs:string"" />
              <xs:element default=""4"" name=""SvcProvType"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""Insured"">
          <xs:complexType>
            <xs:sequence minOccurs=""0"">
              <xs:element name=""InsID"" type=""xs:string"" />
              <xs:element name=""InsSuffix"" type=""xs:string"" />
              <xs:element name=""InsLastName"" type=""xs:string"" />
              <xs:element name=""InsFirstName"" type=""xs:string"" />
              <xs:element name=""InsMidName"" type=""xs:string"" />
              <xs:element name=""InsGrpNo"" type=""xs:string"" />
              <xs:element name=""InsGN"" type=""xs:string"" />
              <xs:element name=""InsDOB"" type=""xs:string"" />
              <xs:element name=""PatID"" type=""xs:string"" />
              <xs:element name=""PatLastName"" type=""xs:string"" />
              <xs:element name=""PatFirstName"" type=""xs:string"" />
              <xs:element name=""PatMidName"" type=""xs:string"" />
              <xs:element name=""PatGN"" type=""xs:string"" />
              <xs:element name=""PatDOB"" type=""xs:string"" />
              <xs:element name=""PatGrpNo"" type=""xs:string"" />
              <xs:element name=""InsErrDtls"" type=""xs:string"" />
              <xs:element default=""02"" name=""InsStatus"" type=""xs:string"" />
              <xs:element name=""InsErrCode"" type=""xs:string"" />
              <xs:element name=""SBR02"" type=""xs:string"" />
              <xs:element name=""SBR03"" type=""xs:string"" />
              <xs:element name=""FirstServiceDate"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""InsAddLine1"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""InsAddLine2"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""InsCity"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""InsState"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""InsZip"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""PatRelCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""Payer"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""PayerID"" type=""xs:string"" />
              <xs:element name=""PayerName"" type=""xs:string"" />
              <xs:element default=""02"" name=""PayerStatus"" type=""xs:string"" />
              <xs:element name=""PayerErrCode"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""Sub_Payer_ID"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""GroupNumber"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""GroupID"" type=""xs:string"" />
              <xs:element default=""02"" name=""GroupStatus"" type=""xs:string"" />
              <xs:element name=""GroupErrCode"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""GroupName"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""AuthNumber"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""AuthorizationNum"" type=""xs:string"" />
              <xs:element default=""02"" name=""AuthNumberStatus"" type=""xs:string"" />
              <xs:element name=""AuthNumberErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""RepExternalCodeValid"">
          <xs:complexType>
            <xs:sequence>
              <xs:element default=""02"" name=""RepExtCdValStatus"" type=""xs:string"" />
              <xs:element name=""RepExtCdValErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""ProfRepRejectGroup"">
          <xs:complexType>
            <xs:sequence>
              <xs:element default=""02"" name=""ProfRepRejGrpStatus"" type=""xs:string"" />
              <xs:element name=""ProfRepRejGrpErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element name=""AttendingPhysician"">
          <xs:complexType>
            <xs:sequence>
              <xs:element name=""AttendingPhysicianID"" type=""xs:string"" />
              <xs:element name=""AttPhyErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""ModifierCodes"">
          <xs:complexType>
            <xs:sequence minOccurs=""0"">
              <xs:element minOccurs=""0"" name=""ModifierList"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ModifierListResult"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ModifierListStatus"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ModifierListErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""ICDCodes"">
          <xs:complexType>
            <xs:sequence minOccurs=""0"">
              <xs:element minOccurs=""0"" name=""ICDList"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICDListResult"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICDListStatus"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ICDListErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
        <xs:element minOccurs=""0"" name=""ServiceCodes"">
          <xs:complexType>
            <xs:sequence minOccurs=""0"">
              <xs:element minOccurs=""0"" name=""ServiceList"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ServiceListResult"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ServiceListStatus"" type=""xs:string"" />
              <xs:element minOccurs=""0"" name=""ServiceListErrCode"" type=""xs:string"" />
            </xs:sequence>
          </xs:complexType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>";
        
        public RulesProfClaimSchema() {
        }
        
        public override string XmlContent {
            get {
                return _strSchema;
            }
        }
        
        public override string[] RootNodes {
            get {
                string[] _RootElements = new string [1];
                _RootElements[0] = "Prof_Claim";
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
