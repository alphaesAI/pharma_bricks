"""
EDI 837 Comprehensive Dimension Tables Mapping
================================================
Production-grade mapping for Healthcare EDI 837 (Professional / Institutional / Dental)

Loop / Segment Coverage:
  ISA / GS / ST / BHT
  2000A  – Billing Provider Hierarchy
  2000B  – Subscriber Hierarchy
  2000C  – Patient Hierarchy
  2010AA – Billing Provider Name (NM1*85)
  2010AB – Pay-to Address (NM1*87)
  2010AC – Pay-to Plan (NM1*PE)
  2010BA – Subscriber Name (NM1*IL)
  2010BB – Payer Name (NM1*PR)
  2010CA – Patient Name (NM1*QC)
  2300   – Claim (CLM + all supporting segments)
  2310A  – Referring Provider (NM1*DN / NM1*P3)
  2310B  – Rendering Provider (NM1*82)
  2310C  – Service Facility Location (NM1*77)
  2310D  – Supervising Provider (NM1*DQ)
  2310E  – Ambulance Pick-up (NM1*PW)
  2310F  – Ambulance Drop-off (NM1*45)
  2320   – Other Subscriber (SBR + MOA + OI + WC)
  2330A  – Other Subscriber Name (NM1*IL)
  2330B  – Other Payer Name (NM1*PR)
  2330C  – Other Payer Referring Provider (NM1*DN)
  2330D  – Other Payer Rendering Provider (NM1*82)
  2330E  – Other Payer Service Facility (NM1*77)
  2330F  – Other Payer Supervising Provider (NM1*DQ)
  2330G  – Other Payer Billing Provider (NM1*85)
  2400   – Service Line (LX / SV1 / SV2 / DTP / REF / NTE / HCP)
  2410   – Drug Identification (LIN / CTP / REF)
  2420A  – Rendering Provider (NM1*82) at line level
  2420B  – Purchased Service Provider (NM1*QB)
  2420C  – Service Facility Location at line level (NM1*77)
  2420D  – Supervising Provider at line level (NM1*DQ)
  2420E  – Ordering Provider (NM1*DK)
  2420F  – Referring Provider at line level (NM1*DN / NM1*P3)
  2420G  – Ambulance Pick-up at line level (NM1*PW)
  2420H  – Ambulance Drop-off at line level (NM1*45)
  2430   – Line Adjudication / COB
  2440   – Form Identification / SV3 (Dental)
  IEA / GE (trailer segments)
"""

MAPPING_DEFINITION = {
    "name": "EDI 837 Comprehensive Dimension Tables Mapping",
    "mapping_type": "only_mapped",

    "expressions": {

        # =============================================================
        # INTERCHANGE CONTROL HEADER / ISA – IEA
        # =============================================================
        "interchange": {
            "sender_qualifier":         "interchange.sender_qualifier",
            "sender_id":                "interchange.sender_id",
            "receiver_qualifier":       "interchange.receiver_qualifier",
            "receiver_id":              "interchange.receiver_id",
            "interchange_date":         "interchange.date",
            "interchange_time":         "interchange.time",
            "repetition_separator":     "interchange.repetition_separator",
            "control_version_number":   "interchange.version",
            "control_number":           "interchange.control_number",
            "acknowledgment_requested": "interchange.acknowledgment_requested",
            "test_indicator":           "interchange.test_indicator",
            "component_element_separator": "interchange.component_element_separator",
            # IEA
            "functional_group_count":   "interchange.functional_group_count",
            "iea_control_number":       "interchange.iea_control_number",
        },

        # =============================================================
        # FUNCTIONAL GROUP HEADER / GS – GE
        # =============================================================
        "functional_group": {
            "functional_id":            "functional_group.functional_id",
            "sender_code":              "functional_group.sender_code",
            "receiver_code":            "functional_group.receiver_code",
            "group_date":               "functional_group.date",
            "group_time":               "functional_group.time",
            "group_control_number":     "functional_group.control_number",
            "responsible_agency_code":  "functional_group.responsible_agency_code",
            "implementation_version":   "functional_group.version",
            # GE
            "transaction_set_count":    "functional_group.transaction_set_count",
            "ge_control_number":        "functional_group.ge_control_number",
        },

        # =============================================================
        # TRANSACTION SET HEADER / ST + BHT
        # =============================================================
        "transaction_header": {
            # ST
            "transaction_set_identifier":
                "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_identifier_code",
            "transaction_control_number":
                "heading.transaction_set_header_loop.transaction_set_header_ST.transaction_set_control_number_02",
            "implementation_reference":
                "heading.transaction_set_header_loop.transaction_set_header_ST.implementation_convention_reference_03",

            # BHT
            "hierarchical_structure_code":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.hierarchical_structure_code",
            "transaction_purpose_code":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_purpose_code",
            "batch_id":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.originator_application_transaction_identifier",
            "transaction_creation_date":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_date",
            "transaction_creation_time":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.transaction_set_creation_time_05",
            "claim_or_encounter_identifier":
                "heading.transaction_set_header_loop.transaction_set_header_BHT.claim_or_encounter_identifier",

            # SE (transaction set trailer)
            "included_segment_count":
                "heading.transaction_set_header_loop.transaction_set_trailer_SE.number_of_included_segments",
            "se_control_number":
                "heading.transaction_set_header_loop.transaction_set_trailer_SE.transaction_set_control_number_02",
        },

        # =============================================================
        # SUBMITTER / NM1*41 + PER
        # =============================================================
        "submitter": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].entity_type_qualifier",
            "submitter_last_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_name",
            "submitter_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].first_name",
            "submitter_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].middle_name",
            "submitter_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_prefix",
            "submitter_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_suffix",
            "submitter_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_id_qualifier",
            "submitter_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[0].submitter_id",

            # PER – Contact Information
            "contact_function_code":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].contact_function_code",
            "contact_name":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].ordering_provider_contact_name",
            "communication_number_qualifier_1":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_qualifier_03",
            "communication_number_1":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_04",
            "communication_number_qualifier_2":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_qualifier_05",
            "communication_number_2":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_06",
            "communication_number_qualifier_3":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_qualifier_07",
            "communication_number_3":
                "detail.submitter_NM1_loop.transaction_set_header_PER[0].communication_number_08",
        },

        # =============================================================
        # RECEIVER / NM1*40
        # =============================================================
        "receiver": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].entity_type_qualifier",
            "receiver_last_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_name",
            "receiver_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].first_name",
            "receiver_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].middle_name",
            "receiver_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_prefix",
            "receiver_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_suffix",
            "receiver_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_id_qualifier",
            "receiver_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[1].receiver_id",
        },

        # =============================================================
        # 2000A – BILLING PROVIDER HIERARCHICAL LEVEL
        # HL*1**20*1  +  PRV  +  CUR
        # =============================================================
        "billing_provider_hl": {
            "hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_id_number",
            "parent_hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_parent_id_number_02",
            "hierarchical_level_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_level_code",
            "hierarchical_child_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[0].hierarchical_child_code",

            # PRV – Billing Provider Specialty Information
            "prv_provider_code":
                "detail.submitter_NM1_loop.transaction_set_header_PRV[0].provider_code",
            "prv_reference_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_PRV[0].reference_identification_qualifier",
            "prv_provider_taxonomy_code":
                "detail.submitter_NM1_loop.transaction_set_header_PRV[0].provider_taxonomy_code",

            # CUR – Foreign Currency Information
            "cur_entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_CUR[0].entity_identifier_code",
            "cur_currency_code":
                "detail.submitter_NM1_loop.transaction_set_header_CUR[0].currency_code",
        },

        # =============================================================
        # 2010AA – BILLING PROVIDER NAME / NM1*85
        # NM1 + N3 + N4 + REF + PER
        # =============================================================
        "billing_provider": {
            # NM1
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].entity_type_qualifier",
            "billing_provider_last_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_name",
            "billing_provider_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].first_name",
            "billing_provider_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].middle_name",
            "billing_provider_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_prefix",
            "billing_provider_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_suffix",
            "billing_provider_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id_qualifier",
            "billing_provider_npi":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[2].billing_provider_id",

            # N3 – Address
            "address_line_1":
                "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.transaction_set_header_N3[0].rendering_provider_address_line_2",

            # N4 – City / State / ZIP
            "city":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_city",
            "state":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_state",
            "zip_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_zip_code",
            "country_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].rendering_provider_country_code",
            "location_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].location_qualifier",
            "location_identifier":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].location_identifier",
            "country_subdivision_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[0].country_subdivision_code",

            # REF – Tax ID / Additional Identifiers
            "tax_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "tax_id":
                "detail.submitter_NM1_loop.transaction_set_header_REF[0].employer_id",
            "upin":
                "detail.submitter_NM1_loop.transaction_set_header_REF[1].employer_id",
            "upin_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "clia_number":
                "detail.submitter_NM1_loop.transaction_set_header_REF[2].employer_id",
            "clia_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_REF[2].reference_identification_qualifier",

            # PER – Contact Information
            "contact_function_code":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].contact_function_code",
            "contact_name":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].ordering_provider_contact_name",
            "contact_comm_qualifier_1":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_qualifier_03",
            "contact_comm_number_1":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_04",
            "contact_comm_qualifier_2":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_qualifier_05",
            "contact_comm_number_2":
                "detail.submitter_NM1_loop.transaction_set_header_PER[1].communication_number_06",
        },

        # =============================================================
        # 2010AB – PAY-TO ADDRESS / NM1*87
        # =============================================================
        "pay_to_address": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "pay_to_last_name":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.pay_to_name",
            "pay_to_first_name":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.first_name",
            "pay_to_id_qualifier":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "pay_to_id":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_NM1.identification_code",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N3.address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N4.zip_code",
            "country_code":
                "detail.submitter_NM1_loop.pay_to_address_NM1_loop.transaction_set_header_N4.country_code",
        },

        # =============================================================
        # 2010AC – PAY-TO PLAN NAME / NM1*PE
        # =============================================================
        "pay_to_plan": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "pay_to_plan_name":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_NM1.pay_to_plan_name",
            "pay_to_plan_id_qualifier":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "pay_to_plan_id":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_NM1.identification_code",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_N3.address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_N4.zip_code",

            # REF
            "payer_id_qualifier":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "payer_id":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "group_number_qualifier":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "group_number":
                "detail.submitter_NM1_loop.pay_to_plan_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2000B – SUBSCRIBER HIERARCHICAL LEVEL
        # HL*2*1*22*0 or HL*2*1*22*1  +  SBR
        # =============================================================
        "subscriber_hl": {
            "hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_id_number",
            "parent_hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_parent_id_number_02",
            "hierarchical_level_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_level_code",
            "hierarchical_child_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[1].hierarchical_child_code",

            # SBR – Subscriber Information
            "payer_responsibility_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.payer_responsibility_sequence_number_code",
            "individual_relationship_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.individual_relationship_code",
            "insured_group_or_policy_number":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.insured_group_or_policy_number_03",
            "insured_group_name":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.other_insured_group_name",
            "insurance_type_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.insurance_type_code",
            "coordination_of_benefits_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.coordination_of_benefits_code",
            "yes_no_condition_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.yes_no_condition_or_response_code",
            "employment_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.employment_status_code",
            "claim_filing_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_SBR.claim_filing_indicator_code",
        },

        # =============================================================
        # 2010BA – SUBSCRIBER NAME / NM1*IL
        # NM1 + N3 + N4 + DMG + REF
        # =============================================================
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
            "subscriber_name_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].name_prefix",
            "subscriber_name_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].name_suffix",
            "subscriber_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id_qualifier",
            "subscriber_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[3].insured_id",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.transaction_set_header_N3[1].rendering_provider_address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_city",
            "state":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_state",
            "zip_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].rendering_provider_zip_code",
            "country_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].country_code",
            "location_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].location_qualifier",
            "location_identifier":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].location_identifier",
            "country_subdivision_code":
                "detail.submitter_NM1_loop.transaction_set_header_N4[1].country_subdivision_code",

            # DMG – Demographic Information
            "date_time_period_format_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].date_time_period_format_qualifier",
            "birth_date":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_birth_date",
            "gender_code":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].patient_gender_code",
            "marital_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].marital_status_code",
            "race_or_ethnicity_code":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].race_or_ethnicity_code",
            "citizenship_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].citizenship_status_code",
            "country_code_dmg":
                "detail.submitter_NM1_loop.transaction_set_header_DMG[0].country_code",

            # REF – Additional Subscriber Identifiers
            "ssn_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_REF[3].reference_identification_qualifier",
            "ssn":
                "detail.submitter_NM1_loop.transaction_set_header_REF[3].reference_identification",
        },

        # =============================================================
        # 2010BB – PAYER NAME / NM1*PR
        # NM1 + N3 + N4 + DTP + REF
        # =============================================================
        "payer": {
            # NM1
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].entity_type_qualifier",
            "payer_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_name",
            "payer_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].first_name",
            "payer_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].middle_name",
            "payer_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_prefix",
            "payer_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_suffix",
            "payer_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_id_qualifier",
            "payer_id":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[4].payer_id",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_N3.address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_N4.zip_code",

            # REF – Payer Additional Identifiers
            "payer_ref_qualifier_1":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "payer_ref_id_1":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "payer_ref_qualifier_2":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "payer_ref_id_2":
                "detail.submitter_NM1_loop.payer_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2000C – PATIENT HIERARCHICAL LEVEL
        # HL*3*2*23*0  +  PAT
        # =============================================================
        "patient_hl": {
            "hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_id_number",
            "parent_hierarchical_id":
                "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_parent_id_number_02",
            "hierarchical_level_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_level_code",
            "hierarchical_child_code":
                "detail.submitter_NM1_loop.transaction_set_header_HL[2].hierarchical_child_code",

            # PAT – Patient Information
            "individual_relationship_code":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.individual_relationship_code",
            "patient_location_code":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.patient_location_code",
            "employment_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.employment_status_code",
            "student_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.student_status_code",
            "date_time_period_format_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.date_time_period_format_qualifier",
            "patient_death_date":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.date_time_period",
            "unit_or_basis_for_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.unit_or_basis_for_measurement_code",
            "patient_weight":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.weight",
            "pregnancy_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_PAT.pregnancy_indicator",
        },

        # =============================================================
        # 2010CA – PATIENT NAME / NM1*QC
        # NM1 + N3 + N4 + DMG + REF
        # =============================================================
        "patient": {
            # NM1
            "entity_identifier_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "patient_last_name":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.patient_last_name",
            "patient_first_name":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.patient_first_name",
            "patient_middle_name":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.patient_middle_name",
            "patient_name_prefix":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.name_prefix",
            "patient_name_suffix":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.name_suffix",
            "patient_id_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "patient_id":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_NM1.identification_code",

            # N3 – Patient Address
            "address_line_1":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N3.address_line_2",

            # N4 – Patient City/State/ZIP
            "city":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.zip_code",
            "country_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.country_code",
            "location_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.location_qualifier",
            "location_identifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.location_identifier",
            "country_subdivision_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_N4.country_subdivision_code",

            # DMG – Patient Demographics
            "date_time_period_format_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.date_time_period_format_qualifier",
            "birth_date":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.patient_birth_date",
            "gender_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.patient_gender_code",
            "marital_status_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.marital_status_code",
            "race_or_ethnicity_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.race_or_ethnicity_code",
            "citizenship_status_code":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_DMG.citizenship_status_code",

            # REF – Patient Additional Identifiers
            "patient_account_number_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "patient_account_number":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "ssn_qualifier":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "ssn":
                "detail.submitter_NM1_loop.patient_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2300 – CLAIM INFORMATION
        # CLM + DTP + REF + HI + NTE + CR1/CR2/CR3/CR4/CR5/CR6/CR7/CR8
        # =============================================================
        "claim": {
            # CLM
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
                "detail.submitter_NM1_loop.transaction_set_header_CLM.release_of_information_code",
            "patient_signature_source_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.patient_signature_source_code",
            "related_causes_code_1":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_1",
            "related_causes_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_2",
            "related_causes_code_3":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.related_causes_code_3",
            "auto_accident_state":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.auto_accident_state",
            "special_program_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.special_program_code",
            "yes_no_condition_code_1":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.yes_no_condition_or_response_code_1",
            "yes_no_condition_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.yes_no_condition_or_response_code_2",
            "provider_agreement_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.provider_agreement_code",
            "claim_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.claim_status_code",
            "yes_no_condition_code_3":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.yes_no_condition_or_response_code_3",
            "claim_submission_reason_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.claim_submission_reason_code",
            "delay_reason_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM.delay_reason_code",
        },

        # =============================================================
        # 2300 – CLAIM DATES / DTP
        # Multiple DTP qualifiers: 431=Onset, 439=Accident, 435=Admit,
        # 096=Discharge, 304=Last X-Ray, 453=Acute Manifestation,
        # 454=Initial Treatment, 090=Last Seen, 444=First Visit,
        # 050=Repricer Received, 438=Occurrence Span, 471=Hearing/Vision
        # =============================================================
        "claim_dates": {
            # DTP[0] – Service Date (431 / D8 or RD8)
            "service_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[0].date_time_qualifier",
            "service_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[0].date_time_period_format_qualifier",
            "service_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[0].service_date",

            # DTP[1] – Statement Dates (434)
            "statement_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[1].date_time_qualifier",
            "statement_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[1].date_time_period_format_qualifier",
            "statement_from_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[1].service_date",

            # DTP[2] – Admission Date (435)
            "admission_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[2].date_time_qualifier",
            "admission_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[2].date_time_period_format_qualifier",
            "admission_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[2].service_date",

            # DTP[3] – Discharge Date (096)
            "discharge_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[3].date_time_qualifier",
            "discharge_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[3].date_time_period_format_qualifier",
            "discharge_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[3].service_date",

            # DTP[4] – Onset of Current Illness (431)
            "onset_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[4].date_time_qualifier",
            "onset_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[4].date_time_period_format_qualifier",
            "onset_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[4].service_date",

            # DTP[5] – Accident Date (439)
            "accident_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[5].date_time_qualifier",
            "accident_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[5].date_time_period_format_qualifier",
            "accident_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[5].service_date",

            # DTP[6] – Last Seen Date (304)
            "last_seen_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[6].date_time_qualifier",
            "last_seen_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[6].date_time_period_format_qualifier",
            "last_seen_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[6].service_date",

            # DTP[7] – Initial Treatment Date (454)
            "initial_treatment_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[7].date_time_qualifier",
            "initial_treatment_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[7].date_time_period_format_qualifier",
            "initial_treatment_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[7].service_date",

            # DTP[8] – Last X-Ray Date (455)
            "last_xray_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[8].date_time_qualifier",
            "last_xray_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[8].service_date",

            # DTP[9] – Hearing / Vision Prescription Date (471)
            "prescription_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[9].date_time_qualifier",
            "prescription_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[9].service_date",

            # DTP[10] – Disability dates (360/361)
            "disability_from_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[10].date_time_qualifier",
            "disability_from_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[10].service_date",

            # DTP[11] – Last Worked Date (297)
            "last_worked_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[11].date_time_qualifier",
            "last_worked_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[11].service_date",

            # DTP[12] – Return to Work Date (296)
            "return_to_work_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[12].date_time_qualifier",
            "return_to_work_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[12].service_date",
        },

        # =============================================================
        # 2300 – CLAIM REFERENCE NUMBERS / REF
        # =============================================================
        "claim_references": {
            # REF – Prior Authorization Number (G1)
            "prior_auth_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[0].reference_identification_qualifier",
            "prior_auth_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[0].reference_identification",

            # REF – Referral Number (9F)
            "referral_number_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[1].reference_identification_qualifier",
            "referral_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[1].reference_identification",

            # REF – Claim Identifier for Transmission Intermediaries (D9)
            "claim_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[2].reference_identification_qualifier",
            "claim_id":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[2].reference_identification",

            # REF – Medical Record Number (EA)
            "medical_record_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[3].reference_identification_qualifier",
            "medical_record_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[3].reference_identification",

            # REF – Original Reference Number (F8) – used for replacement/void
            "original_ref_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[4].reference_identification_qualifier",
            "original_ref_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[4].reference_identification",

            # REF – Service Authorization Exception Code (4N)
            "service_auth_exception_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[5].reference_identification_qualifier",
            "service_auth_exception_code":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[5].reference_identification",

            # REF – Demonstration Project ID (P4)
            "demo_project_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[6].reference_identification_qualifier",
            "demo_project_id":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[6].reference_identification",

            # REF – Adjusted Repriced Claim Reference Number (9A)
            "repriced_claim_ref_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[7].reference_identification_qualifier",
            "repriced_claim_ref_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[7].reference_identification",

            # REF – Investigational Device Exemption Number (LX)
            "investigational_device_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[8].reference_identification_qualifier",
            "investigational_device_number":
                "detail.submitter_NM1_loop.transaction_set_header_CLM_REF[8].reference_identification",
        },

        # =============================================================
        # 2300 – DIAGNOSIS / HI
        # HI*ABK / HI*BK – ICD-10-CM / ICD-9-CM
        # HI*BF – Occurrence / Value / Span Codes (UB-04 Institutional)
        # =============================================================
        "diagnosis": {
            # Principal Diagnosis
            "principal_diagnosis_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[0]",
            "principal_diagnosis_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[1]",
            "principal_diagnosis_date":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi01_01[2]",

            # Additional Diagnoses (HI[0] hi02 through hi12)
            "additional_diagnosis_type_2":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi02_01[0]",
            "additional_diagnosis_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi02_01[1]",
            "additional_diagnosis_type_3":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi03_01[0]",
            "additional_diagnosis_code_3":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi03_01[1]",
            "additional_diagnosis_type_4":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi04_01[0]",
            "additional_diagnosis_code_4":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi04_01[1]",
            "additional_diagnosis_type_5":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi05_01[0]",
            "additional_diagnosis_code_5":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi05_01[1]",
            "additional_diagnosis_type_6":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi06_01[0]",
            "additional_diagnosis_code_6":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi06_01[1]",
            "additional_diagnosis_type_7":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi07_01[0]",
            "additional_diagnosis_code_7":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi07_01[1]",
            "additional_diagnosis_type_8":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi08_01[0]",
            "additional_diagnosis_code_8":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi08_01[1]",
            "additional_diagnosis_type_9":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi09_01[0]",
            "additional_diagnosis_code_9":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi09_01[1]",
            "additional_diagnosis_type_10":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi10_01[0]",
            "additional_diagnosis_code_10":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi10_01[1]",
            "additional_diagnosis_type_11":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi11_01[0]",
            "additional_diagnosis_code_11":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi11_01[1]",
            "additional_diagnosis_type_12":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi12_01[0]",
            "additional_diagnosis_code_12":
                "detail.submitter_NM1_loop.transaction_set_header_HI[0].hi12_01[1]",

            # HI[1] – Reason for Visit / E-Code / POA
            "reason_for_visit_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[1].hi01_01[0]",
            "reason_for_visit_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[1].hi01_01[1]",

            # HI[2] – External Cause of Injury (ICD-10 V/W/X/Y codes)
            "external_cause_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[2].hi01_01[0]",
            "external_cause_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[2].hi01_01[1]",

            # HI[3] – Principal Procedure (Institutional – ICD-10-PCS)
            "principal_procedure_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[3].hi01_01[0]",
            "principal_procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[3].hi01_01[1]",
            "principal_procedure_date":
                "detail.submitter_NM1_loop.transaction_set_header_HI[3].hi01_01[2]",

            # HI[4] – Other Procedures (Institutional)
            "other_procedure_type_2":
                "detail.submitter_NM1_loop.transaction_set_header_HI[4].hi01_01[0]",
            "other_procedure_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_HI[4].hi01_01[1]",
            "other_procedure_date_2":
                "detail.submitter_NM1_loop.transaction_set_header_HI[4].hi01_01[2]",

            # HI[5] – Occurrence / Occurrence Span / Value / Condition Codes (UB-04)
            "occurrence_code_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[5].hi01_01[0]",
            "occurrence_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[5].hi01_01[1]",
            "occurrence_date":
                "detail.submitter_NM1_loop.transaction_set_header_HI[5].hi01_01[2]",

            # HI[6] – Value Codes (Institutional / UB)
            "value_code_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[6].hi01_01[0]",
            "value_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[6].hi01_01[1]",
            "value_amount":
                "detail.submitter_NM1_loop.transaction_set_header_HI[6].hi01_01[2]",

            # HI[7] – Condition Codes (Institutional / UB)
            "condition_code_type":
                "detail.submitter_NM1_loop.transaction_set_header_HI[7].hi01_01[0]",
            "condition_code":
                "detail.submitter_NM1_loop.transaction_set_header_HI[7].hi01_01[1]",
        },

        # =============================================================
        # 2300 – CLAIM NOTES / NTE
        # =============================================================
        "claim_notes": {
            "note_reference_code":
                "detail.submitter_NM1_loop.transaction_set_header_NTE[0].note_reference_code",
            "note_text":
                "detail.submitter_NM1_loop.transaction_set_header_NTE[0].claim_note_text",
            "note_reference_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_NTE[1].note_reference_code",
            "note_text_2":
                "detail.submitter_NM1_loop.transaction_set_header_NTE[1].claim_note_text",
        },

        # =============================================================
        # 2300 – AMBULANCE TRANSPORT INFORMATION / CR1
        # =============================================================
        "ambulance_transport": {
            "weight_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.unit_or_basis_for_measurement_code_01",
            "patient_weight_pounds":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.patient_weight",
            "ambulance_transport_reason_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_transport_reason_code",
            "transport_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.unit_or_basis_for_measurement_code_04",
            "transport_distance":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.transport_distance",
            "round_trip_purpose_desc":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.round_trip_purpose_description",
            "stretcher_purpose_desc":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.stretcher_purpose_description",
            "ambulance_condition_indicator_1":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_conditions_indicator_1",
            "ambulance_condition_indicator_2":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_conditions_indicator_2",
            "ambulance_condition_indicator_3":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_conditions_indicator_3",
            "ambulance_condition_indicator_4":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_conditions_indicator_4",
            "ambulance_condition_indicator_5":
                "detail.submitter_NM1_loop.transaction_set_header_CR1.ambulance_conditions_indicator_5",
        },

        # =============================================================
        # 2300 – SPINAL MANIPULATION SERVICE INFORMATION / CR2
        # =============================================================
        "spinal_manipulation": {
            "category_of_illness_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.category_of_illness_indicator",
            "patient_condition_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.patient_condition_code",
            "nature_of_condition_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.nature_of_the_condition_code",
            "patient_condition_description_1":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.patient_condition_description_1",
            "patient_condition_description_2":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.patient_condition_description_2",
            "xray_available_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_CR2.xray_availability_indicator",
        },

        # =============================================================
        # 2300 – DURABLE MEDICAL EQUIPMENT CERTIFICATION / CR3
        # =============================================================
        "dme_certification": {
            "dme_certification_type_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR3.dme_certification_type_code",
            "dme_duration_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_CR3.unit_or_basis_for_measurement_code",
            "dme_duration":
                "detail.submitter_NM1_loop.transaction_set_header_CR3.durable_medical_equipment_duration",
            "dme_description":
                "detail.submitter_NM1_loop.transaction_set_header_CR3.dme_description",
        },

        # =============================================================
        # 2300 – VISION SUBMISSION CODE / CR7
        # =============================================================
        "vision_submission": {
            "national_or_local_code_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_CR7.national_or_local_assigned_review_value_01",
            "total_visits_rendered":
                "detail.submitter_NM1_loop.transaction_set_header_CR7.total_visits_rendered_02",
            "total_visits_projected":
                "detail.submitter_NM1_loop.transaction_set_header_CR7.total_visits_projected_03",
        },

        # =============================================================
        # 2300 – HOMEBOUND INDICATOR / CRC (Condition Codes – Homebound)
        # =============================================================
        "condition_indicators": {
            "code_category":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].code_category",
            "yes_no_condition_code":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].yes_no_condition_or_response_code",
            "condition_indicator_1":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].condition_indicator_1",
            "condition_indicator_2":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].condition_indicator_2",
            "condition_indicator_3":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].condition_indicator_3",
            "condition_indicator_4":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].condition_indicator_4",
            "condition_indicator_5":
                "detail.submitter_NM1_loop.transaction_set_header_CRC[0].condition_indicator_5",
        },

        # =============================================================
        # 2300 – CLAIM PRICING/REPRICING INFORMATION / HCP
        # =============================================================
        "claim_repricing": {
            "pricing_methodology":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.pricing_methodology",
            "repriced_allowed_amount":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_allowed_amount",
            "repriced_saving_amount":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_saving_amount",
            "repriced_org_id":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repricing_organization_identifier",
            "repriced_per_diem_amount":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_per_diem_amount",
            "repriced_approved_amount":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_amount",
            "repriced_approved_drg_code":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_drg_code",
            "repriced_approved_revenue_code":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_revenue_code",
            "repriced_approved_unit_measurement":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.unit_or_basis_for_measurement_code",
            "repriced_approved_service_unit_count":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_service_unit_count",
            "repriced_approved_place_of_service":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_place_of_service",
            "repriced_approved_drg_weight":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.repriced_approved_drg_weight",
            "reject_reason_code":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.reject_reason_code",
            "policy_compliance_code":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.policy_compliance_code",
            "exception_code":
                "detail.submitter_NM1_loop.transaction_set_header_HCP.exception_code",
        },

        # =============================================================
        # 2310A – REFERRING PROVIDER / NM1*DN or NM1*P3
        # =============================================================
        "referring_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "referring_provider_last_name":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.last_name",
            "referring_provider_first_name":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.first_name",
            "referring_provider_middle_name":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.middle_name",
            "referring_provider_prefix":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.name_prefix",
            "referring_provider_suffix":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.name_suffix",
            "referring_provider_id_qualifier":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "referring_provider_npi":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_NM1.identification_code",

            # REF
            "ref_qualifier_1":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ref_id_1":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "ref_qualifier_2":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "ref_id_2":
                "detail.submitter_NM1_loop.referring_provider_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2310B – RENDERING PROVIDER / NM1*82
        # =============================================================
        "rendering_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].entity_type_qualifier",
            "rendering_provider_last_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_last_name",
            "rendering_provider_first_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_first_name",
            "rendering_provider_middle_name":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_middle_name",
            "rendering_provider_prefix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_prefix",
            "rendering_provider_suffix":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_suffix",
            "rendering_provider_id_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_id_qualifier",
            "rendering_provider_npi":
                "detail.submitter_NM1_loop.transaction_set_header_NM1[5].rendering_provider_id",

            # PRV – Rendering Provider Specialty
            "provider_code":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_PRV.provider_code",
            "reference_id_qualifier":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_PRV.reference_identification_qualifier",
            "provider_taxonomy_code":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_PRV.provider_taxonomy_code",

            # REF
            "ref_qualifier_1":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ref_id_1":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "ref_qualifier_2":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "ref_id_2":
                "detail.submitter_NM1_loop.rendering_provider_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2310C – SERVICE FACILITY LOCATION / NM1*77
        # =============================================================
        "service_facility": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "facility_name":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_NM1.facility_name",
            "facility_id_qualifier":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "facility_npi":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_NM1.identification_code",

            # N3
            "address_line_1":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N3.address_line_2",

            # N4
            "city":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N4.zip_code",
            "country_code":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_N4.country_code",

            # REF
            "ref_qualifier_1":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ref_id_1":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "ref_qualifier_2":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "ref_id_2":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_REF[1].reference_identification",

            # PER
            "contact_function_code":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_PER.contact_function_code",
            "contact_name":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_PER.contact_name",
            "contact_comm_qualifier_1":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_PER.communication_number_qualifier_03",
            "contact_comm_number_1":
                "detail.submitter_NM1_loop.service_facility_NM1_loop.transaction_set_header_PER.communication_number_04",
        },

        # =============================================================
        # 2310D – SUPERVISING PROVIDER / NM1*DQ
        # =============================================================
        "supervising_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "supervising_provider_last_name":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.last_name",
            "supervising_provider_first_name":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.first_name",
            "supervising_provider_middle_name":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.middle_name",
            "supervising_provider_prefix":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.name_prefix",
            "supervising_provider_suffix":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.name_suffix",
            "supervising_provider_id_qualifier":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "supervising_provider_npi":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_NM1.identification_code",

            # REF
            "ref_qualifier_1":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ref_id_1":
                "detail.submitter_NM1_loop.supervising_provider_NM1_loop.transaction_set_header_REF[0].reference_identification",
        },

        # =============================================================
        # 2310E – AMBULANCE PICK-UP LOCATION / NM1*PW
        # =============================================================
        "ambulance_pickup": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "location_name":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_NM1.location_name",
            "address_line_1":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_N3.address_line_2",
            "city":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.ambulance_pickup_NM1_loop.transaction_set_header_N4.zip_code",
        },

        # =============================================================
        # 2310F – AMBULANCE DROP-OFF LOCATION / NM1*45
        # =============================================================
        "ambulance_dropoff": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "facility_name":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_NM1.facility_name",
            "address_line_1":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_N3.address_line_1",
            "address_line_2":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_N3.address_line_2",
            "city":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.ambulance_dropoff_NM1_loop.transaction_set_header_N4.zip_code",
        },

        # =============================================================
        # 2320 – OTHER SUBSCRIBER INFORMATION / SBR + MOA + OI + WC
        # =============================================================
        "other_subscriber_info": {
            # SBR
            "payer_responsibility_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.payer_responsibility_sequence_number_code",
            "individual_relationship_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.individual_relationship_code",
            "group_policy_number":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.reference_identification",
            "group_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.name",
            "insurance_type_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.insurance_type_code",
            "coordination_of_benefits_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.coordination_of_benefits_code",
            "yes_no_condition_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.yes_no_condition_or_response_code",
            "employment_status_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.employment_status_code",
            "claim_filing_indicator":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_SBR.claim_filing_indicator_code",

            # CAS – Claim Adjustment
            "claim_adjustment_group_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_CAS[0].claim_adjustment_group_code",
            "adjustment_reason_code_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_CAS[0].claim_adjustment_reason_code_1",
            "adjustment_amount_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_CAS[0].adjustment_amount_1",
            "adjustment_quantity_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_CAS[0].adjustment_quantity_1",

            # MOA – Medicare Outpatient Adjudication
            "reimbursement_rate":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.reimbursement_rate",
            "hcpcs_payable_amount":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.hcpcs_payable_amount",
            "claim_payment_remark_code_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.claim_payment_remark_code_1",
            "claim_payment_remark_code_2":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.claim_payment_remark_code_2",
            "claim_payment_remark_code_3":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.claim_payment_remark_code_3",
            "claim_payment_remark_code_4":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.claim_payment_remark_code_4",
            "claim_payment_remark_code_5":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.claim_payment_remark_code_5",
            "end_stage_renal_disease_amount":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.end_stage_renal_disease_payment_amount",
            "non_payable_professional_component_amount":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_MOA.non_payable_professional_component_billed_amount",

            # AMT – COB Payer Paid Amount
            "cob_payer_paid_amount_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_AMT[0].amount_qualifier_code",
            "cob_payer_paid_amount":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_AMT[0].monetary_amount",
            "remaining_patient_liability_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_AMT[1].amount_qualifier_code",
            "remaining_patient_liability":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_AMT[1].monetary_amount",

            # OI – Other Insurance Coverage Information
            "benefits_assignment_certification_indicator":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_OI.benefits_assignment_certification_indicator",
            "patient_signature_source_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_OI.patient_signature_source_code",
            "medicare_secondary_reason_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_OI.medicare_secondary_reason_code",
            "release_of_information_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_OI.release_of_information_code",

            # WC – Workers Compensation Related Causes
            "wc_related_causes_code_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_WC.related_causes_code_1",
            "wc_related_causes_code_2":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_WC.related_causes_code_2",
            "wc_auto_accident_state":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_WC.auto_accident_state",
            "wc_country_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_WC.country_code",
            "wc_work_related_indicator":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.transaction_set_header_WC.yes_no_condition_or_response_code",
        },

        # =============================================================
        # 2330A – OTHER SUBSCRIBER NAME / NM1*IL  (COB loop)
        # =============================================================
        "other_subscriber": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "other_subscriber_last_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.last_name",
            "other_subscriber_first_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.first_name",
            "other_subscriber_middle_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.middle_name",
            "other_subscriber_id_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "other_subscriber_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_NM1.identification_code",
            # N3 / N4
            "address_line_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_subscriber_NM1_loop.transaction_set_header_N4.zip_code",
        },

        # =============================================================
        # 2330B – OTHER PAYER NAME / NM1*PR  (COB loop)
        # =============================================================
        "other_payer": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "other_payer_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_NM1.payer_name",
            "other_payer_id_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "other_payer_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_NM1.identification_code",
            # N3 / N4
            "address_line_1":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_N4.zip_code",
            # DTP
            "adjudication_date_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_DTP.date_time_qualifier",
            "adjudication_date":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_DTP.date_time_period",
            # REF
            "prior_auth_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "prior_auth_number":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_REF[0].reference_identification",
            "claim_id_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "claim_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_NM1_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2330C – OTHER PAYER REFERRING PROVIDER / NM1*DN (COB)
        # =============================================================
        "other_payer_referring_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "last_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_NM1.first_name",
            "npi":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_referring_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2330D – OTHER PAYER RENDERING PROVIDER / NM1*82 (COB)
        # =============================================================
        "other_payer_rendering_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "last_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_NM1.first_name",
            "npi":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_rendering_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2330E – OTHER PAYER SERVICE FACILITY / NM1*77 (COB)
        # =============================================================
        "other_payer_service_facility": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_facility_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "facility_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_facility_NM1_loop.transaction_set_header_NM1.facility_name",
            "npi":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_facility_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_facility_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_facility_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2330F – OTHER PAYER SUPERVISING PROVIDER / NM1*DQ (COB)
        # =============================================================
        "other_payer_supervising_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_supervising_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "last_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_supervising_NM1_loop.transaction_set_header_NM1.last_name",
            "npi":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_supervising_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_supervising_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_supervising_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2330G – OTHER PAYER BILLING PROVIDER / NM1*85 (COB)
        # =============================================================
        "other_payer_billing_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "billing_provider_name":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_NM1.billing_provider_name",
            "npi":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.other_subscriber_SBR_loop.other_payer_billing_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2400 – SERVICE LINE (Professional)
        # LX + SV1 + SV2(Institutional) + DTP + REF + NTE + HCP
        # =============================================================
        "service_line": {
            # LX – Line Counter
            "line_number":
                "detail.submitter_NM1_loop.transaction_set_header_LX[0].assigned_number",

            # SV1 – Professional Service
            "procedure_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[0]",
            "procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[1]",
            "modifier_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[2]",
            "modifier_2":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[3]",
            "modifier_3":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[4]",
            "modifier_4":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[5]",
            "procedure_description":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv101_101[6]",
            "line_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].line_item_charge_amount",
            "unit_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].unit_or_basis_for_measurement_code",
            "service_unit_count":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].service_unit_count_104",
            "place_of_service_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].place_of_service_code",
            "service_type_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].service_type_code",
            "diagnosis_code_pointer_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_107",
            "diagnosis_code_pointer_2":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_108",
            "diagnosis_code_pointer_3":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_109",
            "diagnosis_code_pointer_4":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].sv107_110",
            "emergency_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].emergency_indicator",
            "multiple_procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].multiple_procedure_code",
            "epsdt_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].epsdt_indicator",
            "family_planning_indicator":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].family_planning_indicator",
            "review_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].review_code",
            "national_or_local_assigned_review_value":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].national_or_local_assigned_review_value",
            "copay_status_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].copay_status_code",
            "health_care_professional_shortage_area_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].health_care_professional_shortage_area_code",
            "reference_identification":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].reference_identification",
            "postal_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1[0].postal_code",

            # SV2 – Institutional Service Line (Revenue Code)
            "revenue_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].revenue_code",
            "sv2_procedure_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].sv201_201[0]",
            "sv2_procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].sv201_201[1]",
            "sv2_modifier_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].sv201_201[2]",
            "sv2_line_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].line_item_charge_amount",
            "sv2_unit_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].unit_or_basis_for_measurement_code",
            "sv2_service_unit_count":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].service_unit_count",
            "sv2_non_covered_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].non_covered_charge_amount",
            "sv2_blood_deductible_pints":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].blood_deductible_pints",
            "sv2_measurement_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV2[0].measurement_code",

            # SV3 – Dental Service
            "sv3_procedure_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].sv301_301[0]",
            "sv3_procedure_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].sv301_301[1]",
            "sv3_line_charge_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].line_item_charge_amount",
            "sv3_facility_code_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].facility_code_qualifier",
            "sv3_facility_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].facility_code",
            "sv3_oral_cavity_designation_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].oral_cavity_designation_1",
            "sv3_oral_cavity_designation_2":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].oral_cavity_designation_2",
            "sv3_oral_cavity_designation_3":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].oral_cavity_designation_3",
            "sv3_oral_cavity_designation_4":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].oral_cavity_designation_4",
            "sv3_oral_cavity_designation_5":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].oral_cavity_designation_5",
            "sv3_prosthesis_crown_onlay_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].prosthesis_crown_or_onlay_code",
            "sv3_tooth_number":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_number",
            "sv3_tooth_surface_code_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_surface_code_1",
            "sv3_tooth_surface_code_2":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_surface_code_2",
            "sv3_tooth_surface_code_3":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_surface_code_3",
            "sv3_tooth_surface_code_4":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_surface_code_4",
            "sv3_tooth_surface_code_5":
                "detail.submitter_NM1_loop.transaction_set_header_SV3[0].tooth_surface_code_5",

            # DTP – Service Line Dates
            "service_date_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_DTP[0].date_time_qualifier",
            "service_date_format":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_DTP[0].date_time_period_format_qualifier",
            "service_date":
                "detail.submitter_NM1_loop.transaction_set_header_DTP[0].service_date",

            # REF – Line-level Reference Numbers
            "line_ref_qualifier_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[0].reference_identification_qualifier",
            "line_ref_id_1":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[0].reference_identification",
            "prior_auth_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[1].reference_identification_qualifier",
            "prior_auth_number":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[1].reference_identification",
            "line_item_control_number_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[2].reference_identification_qualifier",
            "line_item_control_number":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[2].reference_identification",
            "repriced_line_ref_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[3].reference_identification_qualifier",
            "repriced_line_ref_id":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[3].reference_identification",
            "mammography_certification_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[4].reference_identification_qualifier",
            "mammography_certification_number":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[4].reference_identification",
            "clia_ref_qualifier":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[5].reference_identification_qualifier",
            "clia_ref_number":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_REF[5].reference_identification",

            # NTE – Line Notes
            "line_note_reference_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_NTE[0].note_reference_code",
            "line_note_text":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_NTE[0].claim_note_text",

            # HCP – Line Pricing/Repricing
            "line_pricing_methodology":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.pricing_methodology",
            "line_repriced_allowed_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.repriced_allowed_amount",
            "line_repriced_saving_amount":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.repriced_saving_amount",
            "line_repriced_org_id":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.repricing_organization_identifier",
            "line_reject_reason_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.reject_reason_code",
            "line_policy_compliance_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.policy_compliance_code",
            "line_exception_code":
                "detail.submitter_NM1_loop.transaction_set_header_SV1_HCP.exception_code",
        },

        # =============================================================
        # 2410 – DRUG IDENTIFICATION / LIN + CTP + REF
        # =============================================================
        "drug_identification": {
            # LIN
            "lin_assigned_number":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_LIN.assigned_number",
            "product_id_qualifier":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_LIN.product_id_qualifier",
            "national_drug_code":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_LIN.product_service_id",

            # CTP
            "ctp_price_multiplier_qualifier":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_CTP.price_multiplier_qualifier",
            "drug_unit_price":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_CTP.unit_price",
            "drug_quantity":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_CTP.quantity",
            "drug_measurement_code":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_CTP.unit_or_basis_for_measurement_code",
            "drug_unit_rate":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_CTP.unit_rate",

            # REF
            "ndc_ref_qualifier":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ndc_ref_id":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_REF[0].reference_identification",
            "prescription_number_qualifier":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_REF[1].reference_identification_qualifier",
            "prescription_number":
                "detail.submitter_NM1_loop.drug_LIN_loop.transaction_set_header_REF[1].reference_identification",
        },

        # =============================================================
        # 2420A – RENDERING PROVIDER (LINE LEVEL) / NM1*82
        # =============================================================
        "line_rendering_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "last_name":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.first_name",
            "middle_name":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.middle_name",
            "id_qualifier":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_NM1.identification_code",
            # PRV
            "provider_code":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_PRV.provider_code",
            "taxonomy_qualifier":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_PRV.reference_identification_qualifier",
            "taxonomy_code":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_PRV.provider_taxonomy_code",
            # REF
            "ref_qualifier":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.line_rendering_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2420B – PURCHASED SERVICE PROVIDER / NM1*QB
        # =============================================================
        "purchased_service_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "last_name":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.first_name",
            "id_qualifier":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.purchased_service_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2420C – SERVICE FACILITY (LINE LEVEL) / NM1*77
        # =============================================================
        "line_service_facility": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "facility_name":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_NM1.facility_name",
            "id_qualifier":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_NM1.identification_code",
            "address_line_1":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_N4.zip_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.line_facility_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2420D – SUPERVISING PROVIDER (LINE LEVEL) / NM1*DQ
        # =============================================================
        "line_supervising_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "last_name":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_NM1.first_name",
            "id_qualifier":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.line_supervising_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2420E – ORDERING PROVIDER / NM1*DK
        # =============================================================
        "ordering_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "last_name":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.first_name",
            "middle_name":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.middle_name",
            "prefix":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.name_prefix",
            "suffix":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.name_suffix",
            "id_qualifier":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_NM1.identification_code",
            # N3 / N4
            "address_line_1":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_N4.zip_code",
            # REF
            "ref_qualifier_1":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_REF[0].reference_identification_qualifier",
            "ref_id_1":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_REF[0].reference_identification",
            # PER
            "contact_function_code":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_PER.contact_function_code",
            "contact_comm_qualifier":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_PER.communication_number_qualifier_03",
            "contact_comm_number":
                "detail.submitter_NM1_loop.ordering_provider_NM1_loop.transaction_set_header_PER.communication_number_04",
        },

        # =============================================================
        # 2420F – REFERRING PROVIDER (LINE LEVEL) / NM1*DN or NM1*P3
        # =============================================================
        "line_referring_provider": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "entity_type_qualifier":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.entity_type_qualifier",
            "last_name":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.last_name",
            "first_name":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.first_name",
            "id_qualifier":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.id_qualifier",
            "npi":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_NM1.identification_code",
            "ref_qualifier":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_REF.reference_identification_qualifier",
            "ref_id":
                "detail.submitter_NM1_loop.line_referring_NM1_loop.transaction_set_header_REF.reference_identification",
        },

        # =============================================================
        # 2420G – AMBULANCE PICK-UP LOCATION (LINE LEVEL) / NM1*PW
        # =============================================================
        "line_ambulance_pickup": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "location_name":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_NM1.location_name",
            "address_line_1":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.line_ambulance_pickup_NM1_loop.transaction_set_header_N4.zip_code",
        },

        # =============================================================
        # 2420H – AMBULANCE DROP-OFF LOCATION (LINE LEVEL) / NM1*45
        # =============================================================
        "line_ambulance_dropoff": {
            "entity_identifier_code":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_NM1.entity_identifier_code",
            "facility_name":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_NM1.facility_name",
            "address_line_1":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_N3.address_line_1",
            "city":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_N4.city",
            "state":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_N4.state",
            "zip_code":
                "detail.submitter_NM1_loop.line_ambulance_dropoff_NM1_loop.transaction_set_header_N4.zip_code",
        },

        # =============================================================
        # 2430 – LINE ADJUDICATION / SVD + CAS + DTP + AMT
        # COB coordination-of-benefits line-level adjudication
        # =============================================================
        "line_adjudication": {
            # SVD – Service Line Adjudication
            "other_payer_id_qualifier":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.other_payer_primary_identifier_qualifier",
            "other_payer_id":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.other_payer_primary_identifier",
            "svd_service_qualifier":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.svd02_201[0]",
            "svd_procedure_code":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.svd02_201[1]",
            "svd_procedure_modifier_1":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.svd02_201[2]",
            "svd_allowed_amount":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.service_line_paid_amount",
            "svd_revenue_code":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.revenue_code",
            "svd_paid_service_unit_count":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_SVD.paid_service_unit_count",

            # CAS – Line Adjustment
            "cas_adjustment_group_code":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].claim_adjustment_group_code",
            "cas_reason_code_1":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].claim_adjustment_reason_code_1",
            "cas_adjustment_amount_1":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].adjustment_amount_1",
            "cas_adjustment_quantity_1":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].adjustment_quantity_1",
            "cas_reason_code_2":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].claim_adjustment_reason_code_2",
            "cas_adjustment_amount_2":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_CAS[0].adjustment_amount_2",

            # DTP – Adjudication Date
            "adjudication_date_qualifier":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_DTP.date_time_qualifier",
            "adjudication_date_format":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_DTP.date_time_period_format_qualifier",
            "adjudication_date":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_DTP.date_time_period",

            # AMT – Line Monetary Amounts
            "line_amount_qualifier":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_AMT.amount_qualifier_code",
            "line_monetary_amount":
                "detail.submitter_NM1_loop.line_adjudication_SVD_loop.transaction_set_header_AMT.monetary_amount",
        },

        # =============================================================
        # 2440 – FORM IDENTIFICATION / LQ + FRM (Dental Attachment)
        # =============================================================
        "form_identification": {
            # LQ
            "form_id_qualifier":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_LQ.form_id_qualifier",
            "form_identifier":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_LQ.form_identifier",

            # FRM
            "question_number_1":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[0].question_number_letter",
            "question_response_1":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[0].question_response_1",
            "question_response_date_1":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[0].question_response_date",
            "question_response_percent_1":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[0].question_response_percent",
            "question_response_amount_1":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[0].question_response_amount",
            "question_number_2":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[1].question_number_letter",
            "question_response_2":
                "detail.submitter_NM1_loop.form_LQ_loop.transaction_set_header_FRM[1].question_response_1",
        },
    }
}