"""
Declarative pyedi Mapping Definition matching submitted837professionaloutboundclaims JSON Schema
"""

SUBMITTED837PROFESSIONALOUTBOUNDCLAIMS_MAPPING_DEFINITION = {
    "name": "Submitted 837 Professional Outbound Claims Schema Mapping",
    "mapping_type": "only_mapped",

    "expressions": {
        # Encounter / Claim identifiers
        "EncounterICN": "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_control_number",
        
        # Billing Provider Info
        "BillingProviderLastOrOrg": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_name",
        "BillingProviderFirstName": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].first_name",
        "BillingProviderMiddleName": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].middle_name",
        "BillingProviderNameSuffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_suffix",
        "BillingProviderNPI": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id",
        "BillingProviderAddressLine1": "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_1",
        "BillingProviderAddressLine2": "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_2",
        "BillingProviderCity": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_city",
        "BillingProviderState": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_state",
        "BillingProviderZip": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_zip_code",
        "BillingProviderTIN": "detail.submitter_NM1_loop.transaction_set_header_REF[0].employer_id",
        
        # Member (Subscriber) Info
        "MemberLastName": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_last_name",
        "MemberFirstName": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_first_name",
        "MemberMiddleName": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_middle_name",
        "MemberNameSuffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].name_suffix",
        "HICNumber": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",
        "MemberAddress1": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_1",
        "MemberAddress2": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_2",
        "MemberCity": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_city",
        "MemberState": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_state",
        "MemberZip": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_zip_code",
        "MemberCountry": "detail.submitter_NM1_loop.transaction_set_header_N4[1].country_code",
        "MemberCountrySubdivision": "detail.submitter_NM1_loop.transaction_set_header_N4[1].country_subdivision_code",
        "MemberDOB": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_birth_date",
        "MemberGender": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_gender_code",
        
        # Claim details
        "BilledAmount": "detail.submitter_NM1_loop.transaction_set_header_CLM.total_charge_amount",
        "PlaceOfService": "detail.submitter_NM1_loop.transaction_set_header_CLM.place_of_service",
        "FrequencyTypeCd": "detail.submitter_NM1_loop.transaction_set_header_CLM.frequency_code",
        "PrvSignFile": "detail.submitter_NM1_loop.transaction_set_header_CLM.provider_signature_indicator",
        "PrvAcceptAssignCd": "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_participation_code",
        "BeneAssignCertInd": "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_certification_indicator",
        "ReleaseOfInfoCd": "detail.submitter_NM1_loop.transaction_set_header_CLM.release_of_information_code",
        "PatientSignSrcCd": "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_signature_source_code",
        
        # Accident details
        "AutoAccidentInd": "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_1",
        "EmploymentAccidentInd": "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_2",
        "OtherAccidentInd": "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_3",
        "DelayReasonCd": "detail.submitter_NM1_loop.transaction_set_header_CLM.delay_reason_code",
        
        # Key Dates
        "OnsetDate": "detail.submitter_NM1_loop.transaction_set_header_DTP[4].service_date",
        "InitialTreatmentDate": "detail.submitter_NM1_loop.transaction_set_header_DTP[7].service_date",
        "LastSeen": "detail.submitter_NM1_loop.transaction_set_header_DTP[6].service_date",
        "AccidentDt": "detail.submitter_NM1_loop.transaction_set_header_DTP[5].service_date",
        "LastXray": "detail.submitter_NM1_loop.transaction_set_header_DTP[8].service_date",
        
        # Primary rendering provider
        "RenderingProviderNPI": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].billing_provider_id",
        
        # Diagnoses (ICD Codes from HI segment) - Aligned to Diag1-Diag12 in the schema
        "Diag1": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[1]",
        "Diag2": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi02_01[1]",
        "Diag3": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi03_01[1]",
        "Diag4": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi04_01[1]",
        "Diag5": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi05_01[1]",
        "Diag6": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi06_01[1]",
        "Diag7": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi07_01[1]",
        "Diag8": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi08_01[1]",
        "Diag9": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi09_01[1]",
        "Diag10": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi10_01[1]",
        "Diag11": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi12_01[1]",
        "Diag12": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi12_01[1]",
        
        # Service Lines - We will map these repeating lists so that the CSVConverter
        # can dynamically flatten them into the columns DiagCdPointer1-50, ProcCd1-50, etc.
        "service_lines": {
            "line_number": "detail.submitter_NM1_loop.transaction_set_header_LX[*].assigned_number",
            "procedure_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv101_101[1]",
            "modifier_1": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv101_101[2]",
            "modifier_2": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv101_101[3]",
            "modifier_3": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv101_101[4]",
            "modifier_4": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv101_101[5]",
            "line_charge_amount": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].line_item_charge_amount",
            "unit_measurement_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].unit_or_basis_for_measurement_code",
            "service_unit_count": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].service_unit_count_104",
            "diagnosis_code_pointer_1": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv107_107",
            "diagnosis_code_pointer_2": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv107_108",
            "diagnosis_code_pointer_3": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv107_109",
            "diagnosis_code_pointer_4": "detail.submitter_NM1_loop.transaction_set_header_SV1[*].sv107_110"
        }
    }
}
