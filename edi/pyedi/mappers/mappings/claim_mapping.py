MAPPING_DEFINITION = {
    "name": "EDI 837 Comprehensive Dimension Tables Mapping",
    "mapping_type": "only_mapped",

    "expressions": {

        # =========================================================
        # INTERCHANGE / ISA
        # =========================================================
        "interchange": {
            "sender_id": "interchange.sender_id",
            "sender_qualifier": "interchange.sender_qualifier",
            "receiver_id": "interchange.receiver_id",
            "receiver_qualifier": "interchange.receiver_qualifier",
            "interchange_date": "interchange.date",
            "interchange_time": "interchange.time",
            "control_number": "interchange.control_number",
            "version": "interchange.version",
            "test_indicator": "interchange.test_indicator"
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
            "implementation_version": "functional_group.version"
        },

        # =========================================================
        # TRANSACTION HEADER / ST + BHT
        # =========================================================
        "transaction_header": {
            "transaction_set_identifier":
                "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_identifier_code",

            "transaction_control_number":
                "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_control_number_02",

            "implementation_reference":
                "heading.transaction_set_header_loop.transaction_set_header_ST.implementation_convention_reference_03",

            "hierarchical_structure_code":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.hierarchical_structure_code",

            "transaction_purpose_code":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_purpose_code",

            "batch_id":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.originator_application_transaction_identifier",

            "transaction_creation_date":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_date",

            "transaction_creation_time":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_time_05"
        },

        # =========================================================
        # BILLING PROVIDER / 2000A / NM1*85
        # =========================================================
        "billing_provider": {

            # NM1
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_identifier_code",

            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_type_qualifier",

            "billing_provider_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_name",

            "billing_provider_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id_qualifier",

            "billing_provider_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_1",

            "address_line_2":
                "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_city",

            "state":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_state",

            "zip_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_zip_code",

            # REF
            "tax_id":
                "detail.submitter_NM1_loop.transaction_set_header_REF[0].employer_id",

            # HL
            "hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_id_number",

            "hierarchical_level_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_level_code"
        },

        # =========================================================
        # SUBSCRIBER / 2000B / NM1*IL
        # =========================================================
        "subscriber": {

            # NM1
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].entity_identifier_code",

            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].entity_type_qualifier",

            "subscriber_last_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_last_name",

            "subscriber_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_first_name",

            "subscriber_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_middle_name",

            "subscriber_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id_qualifier",

            "subscriber_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",

            # DMG
            "birth_date":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_birth_date",

            "gender":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_gender_code",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_1",

            # N4
            "city":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_city",

            "state":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_state",

            "zip_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_zip_code",

            # SBR
            "payer_responsibility_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.payer_responsibility_sequence_number_code",

            "relationship_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.individual_relationship_code",

            "claim_filing_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.claim_filing_indicator_code",

            # HL
            "hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_id_number",

            "parent_hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_parent_id_number_02",

            "hierarchical_level_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_level_code"
        },

        # =========================================================
        # PAYER / NM1*PR
        # =========================================================
        "payer": {

            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].entity_identifier_code",

            "payer_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_name",

            "payer_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_id_qualifier",

            "payer_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_id"
        },

        # =========================================================
        # CLAIM / 2300 / CLM
        # =========================================================
        "claim": {

            "claim_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_control_number",

            "total_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.total_charge_amount",

            "facility_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.facility_code",

            "place_of_service":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.place_of_service",

            "frequency_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.frequency_code",

            "claim_type_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.claim_type_code",

            "provider_signature_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.provider_signature_indicator",

            "assignment_participation_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_participation_code",

            "assignment_certification_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.assignment_certification_indicator",

            "release_of_information_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.release_of_information_code"
        },

        # =========================================================
        # DIAGNOSIS / HI
        # =========================================================
        "diagnosis": {

            "diagnosis_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[0]",

            "diagnosis_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[1]"
        },

        # =========================================================
        # SERVICE LINE / LX + SV1 + DTP
        # =========================================================
        "service_line": {

            "line_number":
                "detail.submitter_NM1_loop.transaction_set_header_LX[0].assigned_number",

            "procedure_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[0]",

            "procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[1]",

            "line_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].line_item_charge_amount",

            "unit_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].unit_or_basis_for_measurement_code",

            "service_unit_count":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].service_unit_count_104",

            "service_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[0].service_date"
        }
    }
}