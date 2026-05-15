# WARNING: 
# This mapping definition uses hardcoded array indices (e.g. NM1[0], NM1[1]) which is the pattern established in the original file.
# In production EDI 837, loops can be optional or repeated. If an optional loop is omitted, all subsequent array indices will shift,
# leading to catastrophic data corruption (e.g. mapping a Referring Provider as a Rendering Provider).
# It is highly recommended to update the PyEDI implementation to support dynamic JSONPath filtering (e.g. NM1[?(@.entity_identifier_code == '85')])
# or use business logic in DBT to pivot out the provider types based on NM101 instead of relying on position.

MAPPING_DEFINITION = {
    "name": "EDI 837 Comprehensive Dimension Tables Mapping",
    "mapping_type": "only_mapped",

    "expressions": {

        # =========================================================
        # INTERCHANGE / ISA
        # =========================================================
        "interchange": {
            "authorization_information_qualifier": "interchange.authorization_information_qualifier",
            "authorization_information": "interchange.authorization_information",
            "security_information_qualifier": "interchange.security_information_qualifier",
            "security_information": "interchange.security_information",
            "sender_qualifier": "interchange.sender_qualifier",
            "sender_id": "interchange.sender_id",
            "receiver_qualifier": "interchange.receiver_qualifier",
            "receiver_id": "interchange.receiver_id",
            "interchange_date": "interchange.date",
            "interchange_time": "interchange.time",
            "repetition_separator": "interchange.repetition_separator",
            "version": "interchange.version",
            "control_number": "interchange.control_number",
            "acknowledgment_requested": "interchange.acknowledgment_requested",
            "test_indicator": "interchange.test_indicator",
            "component_element_separator": "interchange.component_element_separator"
        },

        # =========================================================
        # FUNCTIONAL GROUP / GS
        # =========================================================
        "functional_group": {
            "functional_id": "functional_group.functional_id",
            "sender_code": "functional_group.sender_code",
            "receiver_code": "functional_group.receiver_code",
            "group_date": "functional_group.date",
            "group_time": "functional_group.time",
            "group_control_number": "functional_group.control_number",
            "responsible_agency_code": "functional_group.responsible_agency_code",
            "implementation_version": "functional_group.version"
        },

        # =========================================================
        # TRANSACTION HEADER / ST + BHT
        # =========================================================
        "transaction_header": {
            "transaction_set_identifier": "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_identifier_code",
            "transaction_control_number": "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_control_number_02",
            "implementation_reference": "heading.transaction_set_header_loop.transaction_set_header_ST.implementation_convention_reference_03",
            "hierarchical_structure_code": "heading.transaction_set_header_loop.transaction_set_header_BHT.hierarchical_structure_code",
            "transaction_purpose_code": "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_purpose_code",
            "batch_id": "heading.transaction_set_header_loop.transaction_set_header_BHT.originator_application_transaction_identifier",
            "transaction_creation_date": "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_date",
            "transaction_creation_time": "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_time_05",
            "claim_or_encounter_identifier": "heading.transaction_set_header_loop.transaction_set_header_BHT.claim_or_encounter_identifier"
        },

        # =========================================================
        # SUBMITTER / 1000A / NM1*41 + PER
        # =========================================================
        "submitter": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].entity_type_qualifier",
            "submitter_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_name",
            "submitter_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].first_name",
            "submitter_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].middle_name",
            "submitter_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_prefix",
            "submitter_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_suffix",
            "submitter_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_id_qualifier",
            "submitter_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_id",
            "contact_function_code": "detail.submitter_NM1_loop.transaction_set_header_PER[0].contact_function_code",
            "contact_name": "detail.submitter_NM1_loop.transaction_set_header_PER[0].ordering_provider_contact_name",
            "communication_number_qualifier": "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_qualifier_03",
            "communication_number": "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_04",
            "communication_number_qualifier_2": "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_qualifier_05",
            "communication_number_2": "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_06"
        },

        # =========================================================
        # RECEIVER / 1000B / NM1*40
        # =========================================================
        "receiver": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].entity_type_qualifier",
            "receiver_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_name",
            "receiver_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].first_name",
            "receiver_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].middle_name",
            "receiver_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_prefix",
            "receiver_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_suffix",
            "receiver_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_id_qualifier",
            "receiver_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_id"
        },

        # =========================================================
        # BILLING PROVIDER / 2000A / NM1*85
        # =========================================================
        "billing_provider": {
            "hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_id_number",
            "parent_hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_parent_id_number_02",
            "hierarchical_level_code": "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_level_code",
            "hierarchical_child_code": "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_child_code",
            "provider_code": "detail.submitter_NM1_loop.transaction_set_header_PRV[0].provider_code",
            "reference_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_PRV[0].reference_identification_qualifier",
            "provider_taxonomy_code": "detail.submitter_NM1_loop.transaction_set_header_PRV[0].provider_taxonomy_code",
            
            # NM1 85
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_type_qualifier",
            "billing_provider_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_name",
            "billing_provider_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].first_name",
            "billing_provider_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].middle_name",
            "billing_provider_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_prefix",
            "billing_provider_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_suffix",
            "billing_provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id_qualifier",
            "billing_provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id",
            
            # N3/N4 2010AA
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_1",
            "address_line_2": "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_2",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_zip_code",
            
            # REF 2010AA Tax ID
            "tax_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "tax_id": "detail.submitter_NM1_loop.transaction_set_header_REF[0].employer_id",
            
            # PER 2010AA
            "contact_name": "detail.submitter_NM1_loop.transaction_set_header_PER[1].ordering_provider_contact_name",
            "communication_number_qualifier": "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_qualifier_03",
            "communication_number": "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_04"
        },

        # =========================================================
        # PAY-TO ADDRESS / 2010AB / NM1*87
        # =========================================================
        "pay_to_address": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].entity_type_qualifier",
            "pay_to_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[3].pay_to_name",
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_1",
            "address_line_2": "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_2",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_zip_code"
        },

        # =========================================================
        # SUBSCRIBER / 2000B / NM1*IL
        # =========================================================
        "subscriber": {
            "hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_id_number",
            "parent_hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_parent_id_number_02",
            "hierarchical_level_code": "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_level_code",
            "hierarchical_child_code": "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_child_code",
            
            # SBR 2000B
            "payer_responsibility_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].payer_responsibility_sequence_number_code",
            "relationship_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].individual_relationship_code",
            "insured_group_or_policy_number": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].insured_group_or_policy_number_03",
            "other_insured_group_name": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].other_insured_group_name",
            "insurance_type_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].insurance_type_code",
            "coordination_of_benefits_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].coordination_of_benefits_code",
            "yes_no_condition_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].yes_no_condition_or_response_code",
            "employment_status_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].employment_status_code",
            "claim_filing_indicator": "detail.submitter_NM1_loop.transaction_set_header_SBR[0].claim_filing_indicator_code",
            
            # PAT 2000B
            "individual_relationship_code": "detail.submitter_NM1_loop.transaction_set_header_PAT[0].individual_relationship_code",
            "patient_location_code": "detail.submitter_NM1_loop.transaction_set_header_PAT[0].patient_location_code",
            "employment_status_code_pat": "detail.submitter_NM1_loop.transaction_set_header_PAT[0].employment_status_code",
            
            # NM1 2010BA
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].entity_type_qualifier",
            "subscriber_last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_last_name",
            "subscriber_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_first_name",
            "subscriber_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_middle_name",
            "subscriber_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_prefix",
            "subscriber_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_suffix",
            "subscriber_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_id_qualifier",
            "subscriber_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[4].insured_id",
            
            # N3/N4 2010BA
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[2].rendering_provider_address_line_1",
            "address_line_2": "detail.submitter_NM1_loop.transaction_set_header_N3[2].rendering_provider_address_line_2",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[2].rendering_provider_city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[2].rendering_provider_state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[2].rendering_provider_zip_code",
            
            # DMG 2010BA
            "date_time_period_format_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].date_time_period_format_qualifier",
            "birth_date": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_birth_date",
            "gender": "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_gender_code",
            
            # REF 2010BA Secondary ID
            "secondary_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "secondary_id": "detail.submitter_NM1_loop.transaction_set_header_REF[1].reference_identification"
        },

        # =========================================================
        # PAYER / 2010BB / NM1*PR
        # =========================================================
        "payer": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].entity_type_qualifier",
            "payer_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].payer_name",
            "payer_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].first_name",
            "payer_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].middle_name",
            "payer_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].payer_prefix",
            "payer_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].payer_suffix",
            "payer_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].payer_id_qualifier",
            "payer_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[5].payer_id",
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[3].rendering_provider_address_line_1",
            "address_line_2": "detail.submitter_NM1_loop.transaction_set_header_N3[3].rendering_provider_address_line_2",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[3].rendering_provider_city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[3].rendering_provider_state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[3].rendering_provider_zip_code",
            "secondary_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_REF[2].reference_identification_qualifier",
            "secondary_id": "detail.submitter_NM1_loop.transaction_set_header_REF[2].reference_identification"
        },

        # =========================================================
        # PATIENT / 2000C / NM1*QC (If Patient is NOT Subscriber)
        # =========================================================
        "patient": {
            "hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_id_number",
            "parent_hierarchical_id": "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_parent_id_number_02",
            "hierarchical_level_code": "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_level_code",
            "hierarchical_child_code": "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_child_code",
            
            # PAT 2000C
            "individual_relationship_code": "detail.submitter_NM1_loop.transaction_set_header_PAT[1].individual_relationship_code",
            "patient_location_code": "detail.submitter_NM1_loop.transaction_set_header_PAT[1].patient_location_code",
            "employment_status_code": "detail.submitter_NM1_loop.transaction_set_header_PAT[1].employment_status_code",
            
            # NM1 2010CA
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].entity_type_qualifier",
            "patient_last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].patient_last_name",
            "patient_first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].patient_first_name",
            "patient_middle_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].patient_middle_name",
            "patient_prefix": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].patient_prefix",
            "patient_suffix": "detail.submitter_NM1_loop.transaction_set_header_NM1[6].patient_suffix",
            
            # N3/N4 2010CA
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[4].rendering_provider_address_line_1",
            "address_line_2": "detail.submitter_NM1_loop.transaction_set_header_N3[4].rendering_provider_address_line_2",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[4].rendering_provider_city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[4].rendering_provider_state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[4].rendering_provider_zip_code",
            
            # DMG 2010CA
            "date_time_period_format_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DMG[1].date_time_period_format_qualifier",
            "birth_date": "detail.submitter_NM1_loop.transaction_set_header_DMG[1].patient_birth_date",
            "gender": "detail.submitter_NM1_loop.transaction_set_header_DMG[1].patient_gender_code",
            
            # REF 2010CA
            "secondary_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_REF[3].reference_identification_qualifier",
            "secondary_id": "detail.submitter_NM1_loop.transaction_set_header_REF[3].reference_identification"
        },

        # =========================================================
        # CLAIM / 2300 / CLM
        # =========================================================
        "claim": {
            "claim_number": "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_control_number",
            "total_charge_amount": "detail.submitter_NM1_loop.transaction_set_header_CLM.total_charge_amount",
            "facility_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.facility_code",
            "place_of_service": "detail.submitter_NM1_loop.transaction_set_header_CLM.place_of_service",
            "frequency_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.frequency_code",
            "claim_type_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.claim_type_code",
            "provider_signature_indicator": "detail.submitter_NM1_loop.transaction_set_header_CLM.provider_signature_indicator",
            "assignment_participation_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_participation_code",
            "assignment_certification_indicator": "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_certification_indicator",
            "release_of_information_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.release_of_information_code",
            "patient_signature_source_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_signature_source_code",
            "related_causes_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code",
            "special_program_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.special_program_code",
            "delay_reason_code": "detail.submitter_NM1_loop.transaction_set_header_CLM.delay_reason_code"
        },

        # =========================================================
        # CLAIM AMOUNTS / AMT / 2300
        # =========================================================
        "claim_amounts": {
            "amount_qualifier_code": "detail.submitter_NM1_loop.transaction_set_header_AMT[0].amount_qualifier_code",
            "monetary_amount": "detail.submitter_NM1_loop.transaction_set_header_AMT[0].monetary_amount"
        },

        # =========================================================
        # CLAIM REFERENCES / REF / 2300 (Prior Auth, Referral, etc.)
        # =========================================================
        "claim_references": {
            "reference_identification_qualifier": "detail.submitter_NM1_loop.transaction_set_header_REF[4].reference_identification_qualifier",
            "reference_identification": "detail.submitter_NM1_loop.transaction_set_header_REF[4].reference_identification"
        },

        # =========================================================
        # PAPERWORK / PWK / 2300
        # =========================================================
        "paperwork": {
            "report_type_code": "detail.submitter_NM1_loop.transaction_set_header_PWK[0].report_type_code",
            "report_transmission_code": "detail.submitter_NM1_loop.transaction_set_header_PWK[0].report_transmission_code",
            "identification_code": "detail.submitter_NM1_loop.transaction_set_header_PWK[0].identification_code",
            "attachment_control_number": "detail.submitter_NM1_loop.transaction_set_header_PWK[0].attachment_control_number"
        },

        # =========================================================
        # NOTES / NTE / 2300
        # =========================================================
        "claim_notes": {
            "note_reference_code": "detail.submitter_NM1_loop.transaction_set_header_NTE[0].note_reference_code",
            "description": "detail.submitter_NM1_loop.transaction_set_header_NTE[0].description"
        },

        # =========================================================
        # AMBULANCE / CR1 / 2300
        # =========================================================
        "ambulance_transport": {
            "unit_of_measurement_code": "detail.submitter_NM1_loop.transaction_set_header_CR1[0].unit_or_basis_for_measurement_code",
            "weight": "detail.submitter_NM1_loop.transaction_set_header_CR1[0].weight",
            "ambulance_transport_reason_code": "detail.submitter_NM1_loop.transaction_set_header_CR1[0].ambulance_transport_reason_code",
            "transport_distance": "detail.submitter_NM1_loop.transaction_set_header_CR1[0].transport_distance"
        },

        # =========================================================
        # CLAIM DATES / DTP / 2300
        # =========================================================
        "claim_dates": {
            "date_time_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DTP[0].date_time_qualifier",
            "date_time_period_format_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DTP[0].date_time_period_format_qualifier",
            "service_date": "detail.submitter_NM1_loop.transaction_set_header_DTP[0].service_date"
        },

        # =========================================================
        # DIAGNOSIS / HI / 2300
        # =========================================================
        "diagnosis": {
            "diagnosis_type": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[0]",
            "diagnosis_code": "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[1]"
        },

        # =========================================================
        # CLAIM LEVEL PROVIDERS / 2310A - 2310F
        # =========================================================
        "referring_provider_2310A": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[7].identification_code"
        },
        "rendering_provider_2310B": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[8].identification_code"
        },
        "service_facility_2310C": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[9].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[9].entity_type_qualifier",
            "name": "detail.submitter_NM1_loop.transaction_set_header_NM1[9].name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[9].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[9].identification_code",
            "address_line_1": "detail.submitter_NM1_loop.transaction_set_header_N3[5].address_line_1",
            "city": "detail.submitter_NM1_loop.transaction_set_header_N4[5].city",
            "state": "detail.submitter_NM1_loop.transaction_set_header_N4[5].state",
            "zip_code": "detail.submitter_NM1_loop.transaction_set_header_N4[5].zip_code"
        },
        "supervising_provider_2310D": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[10].identification_code"
        },

        # =========================================================
        # COORDINATION OF BENEFITS / 2320 + 2330
        # =========================================================
        "cob_other_subscriber_2320": {
            "payer_responsibility_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].payer_responsibility_sequence_number_code",
            "relationship_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].individual_relationship_code",
            "insured_group_or_policy_number": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].insured_group_or_policy_number_03",
            "other_insured_group_name": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].other_insured_group_name",
            "insurance_type_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].insurance_type_code",
            "coordination_of_benefits_code": "detail.submitter_NM1_loop.transaction_set_header_SBR[1].coordination_of_benefits_code"
        },
        "cob_claim_adjustment_CAS": {
            "group_code": "detail.submitter_NM1_loop.transaction_set_header_CAS[0].claim_adjustment_group_code",
            "reason_code": "detail.submitter_NM1_loop.transaction_set_header_CAS[0].claim_adjustment_reason_code_1",
            "monetary_amount": "detail.submitter_NM1_loop.transaction_set_header_CAS[0].monetary_amount_1"
        },
        "cob_payer_paid_AMT": {
            "amount_qualifier_code": "detail.submitter_NM1_loop.transaction_set_header_AMT[1].amount_qualifier_code",
            "monetary_amount": "detail.submitter_NM1_loop.transaction_set_header_AMT[1].monetary_amount"
        },
        "cob_other_subscriber_name_2330A": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[11].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[11].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[11].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[11].first_name"
        },
        "cob_other_payer_name_2330B": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[12].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[12].entity_type_qualifier",
            "payer_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[12].payer_name",
            "payer_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[12].identification_code_qualifier",
            "payer_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[12].identification_code",
            "remittance_date": "detail.submitter_NM1_loop.transaction_set_header_DTP[1].service_date"
        },

        # =========================================================
        # SERVICE LINE / LX + SV1 / 2400
        # =========================================================
        "service_line": {
            "line_number": "detail.submitter_NM1_loop.transaction_set_header_LX[0].assigned_number",
            "procedure_qualifier": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[0]",
            "procedure_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[1]",
            "procedure_modifier_1": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[2]",
            "procedure_modifier_2": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[3]",
            "procedure_modifier_3": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[4]",
            "procedure_modifier_4": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[5]",
            "line_charge_amount": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].line_item_charge_amount",
            "unit_measurement_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].unit_or_basis_for_measurement_code",
            "service_unit_count": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].service_unit_count_104",
            "place_of_service_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].place_of_service_code",
            "service_type_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].service_type_code",
            "diagnosis_code_pointer_1": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_107[0]",
            "diagnosis_code_pointer_2": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_107[1]",
            "diagnosis_code_pointer_3": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_107[2]",
            "diagnosis_code_pointer_4": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_107[3]",
            "emergency_indicator": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].emergency_indicator",
            "multiple_procedure_indicator": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].multiple_procedure_indicator",
            "epsdt_indicator": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].epsdt_indicator",
            "family_planning_indicator": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].family_planning_indicator",
            "co_pay_status_code": "detail.submitter_NM1_loop.transaction_set_header_SV1[0].co_pay_status_code"
        },

        # =========================================================
        # SERVICE LINE DATES / DTP / 2400
        # =========================================================
        "service_line_dates": {
            "date_time_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DTP[2].date_time_qualifier",
            "date_time_period_format_qualifier": "detail.submitter_NM1_loop.transaction_set_header_DTP[2].date_time_period_format_qualifier",
            "service_date": "detail.submitter_NM1_loop.transaction_set_header_DTP[2].service_date"
        },

        # =========================================================
        # CLINICAL MEASUREMENTS / MEA / 2400 (e.g. HbA1c, Blood Pressure)
        # =========================================================
        "service_line_measurements": {
            "measurement_reference_id_code": "detail.submitter_NM1_loop.transaction_set_header_MEA[0].measurement_reference_id_code",
            "measurement_qualifier": "detail.submitter_NM1_loop.transaction_set_header_MEA[0].measurement_qualifier",
            "measurement_value": "detail.submitter_NM1_loop.transaction_set_header_MEA[0].measurement_value"
        },

        # =========================================================
        # DRUG IDENTIFICATION / LIN + CTP / 2410
        # =========================================================
        "drug_identification": {
            "product_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_LIN[0].product_service_id_qualifier",
            "national_drug_code": "detail.submitter_NM1_loop.transaction_set_header_LIN[0].product_service_id",
            "national_drug_unit_count": "detail.submitter_NM1_loop.transaction_set_header_CTP[0].national_drug_unit_count",
            "unit_measurement_code": "detail.submitter_NM1_loop.transaction_set_header_CTP[0].unit_or_basis_for_measurement_code"
        },

        # =========================================================
        # SERVICE LINE PROVIDERS / 2420A - 2420F
        # =========================================================
        "line_rendering_provider_2420A": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[13].identification_code"
        },
        "line_service_facility_2420C": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[14].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[14].entity_type_qualifier",
            "name": "detail.submitter_NM1_loop.transaction_set_header_NM1[14].name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[14].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[14].identification_code"
        },
        "line_supervising_provider_2420D": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[15].identification_code"
        },
        "line_ordering_provider_2420E": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[16].identification_code"
        },
        "line_referring_provider_2420F": {
            "entity_identifier_code": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].entity_identifier_code",
            "entity_type_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].entity_type_qualifier",
            "last_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].last_name",
            "first_name": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].first_name",
            "provider_id_qualifier": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].identification_code_qualifier",
            "provider_id": "detail.submitter_NM1_loop.transaction_set_header_NM1[17].identification_code"
        },

        # =========================================================
        # LINE ADJUDICATION / SVD + CAS / 2430
        # =========================================================
        "line_adjudication_2430": {
            "other_payer_primary_identifier": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].other_payer_primary_identifier",
            "service_line_paid_amount": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].service_line_paid_amount",
            "procedure_qualifier": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].svd03_03[0]",
            "procedure_code": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].svd03_03[1]",
            "product_service_id": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].product_service_id",
            "paid_service_unit_count": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].paid_service_unit_count",
            "bundled_line_number": "detail.submitter_NM1_loop.transaction_set_header_SVD[0].bundled_line_number"
        },
        "line_adjustment_CAS": {
            "group_code": "detail.submitter_NM1_loop.transaction_set_header_CAS[1].claim_adjustment_group_code",
            "reason_code": "detail.submitter_NM1_loop.transaction_set_header_CAS[1].claim_adjustment_reason_code_1",
            "monetary_amount": "detail.submitter_NM1_loop.transaction_set_header_CAS[1].monetary_amount_1"
        },

        # =========================================================
        # FORM IDENTIFICATION / LQ + FRM / 2440
        # =========================================================
        "form_identification_2440": {
            "code_list_qualifier_code": "detail.submitter_NM1_loop.transaction_set_header_LQ[0].code_list_qualifier_code",
            "industry_code": "detail.submitter_NM1_loop.transaction_set_header_LQ[0].industry_code",
            "question_number": "detail.submitter_NM1_loop.transaction_set_header_FRM[0].question_number",
            "question_response": "detail.submitter_NM1_loop.transaction_set_header_FRM[0].question_response",
            "question_response_date": "detail.submitter_NM1_loop.transaction_set_header_FRM[0].question_response_date"
        }
    }
}