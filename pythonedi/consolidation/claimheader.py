# claim_header.py

from psycopg2.extras import RealDictCursor


class ClaimHeaderProcessor:

    def __init__(self, conn):
        self.conn = conn


    def process(self):

        cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("""

            SELECT

                -- Claim fields
                c.claim_number,
                c.total_charge_amount,
                c.facility_code,
                c.place_of_service,
                c.frequency_code,
                c.claim_type_code,
                c.provider_signature_indicator,
                c.assignment_participation_code,
                c.assignment_certification_indicator,
                c.release_of_information_code,

                -- Service Line fields
                sl.line_number,
                sl.procedure_qualifier,
                sl.procedure_code,
                sl.line_charge_amount,
                sl.unit_measurement_code,
                sl.service_unit_count,
                sl.sv107_107,
                sl.service_date,

                -- Claim Dates fields
                cd.service_date as claim_service_date,

                -- Diagnosis fields
                d.diagnosis_type,
                d.diagnosis_code,

                -- Billing Provider fields
                bp.entity_identifier_code as billing_entity_identifier_code,
                bp.entity_type_qualifier as billing_entity_type_qualifier,
                bp.billing_provider_name,
                bp.billing_provider_id_qualifier,
                bp.billing_provider_id,
                bp.address_line_1 as billing_provider_address_line_1,
                bp.address_line_2 as billing_provider_address_line_2,
                bp.city as billing_provider_city,
                bp.state as billing_provider_state,
                bp.zip_code as billing_provider_zip_code,
                bp.tax_id as billing_provider_tax_id,
                bp.hierarchical_id as billing_provider_hierarchical_id,
                bp.hierarchical_level_code as billing_provider_hierarchical_level_code,
                bp.hierarchical_child_code as billing_provider_hierarchical_child_code,

                -- Rendering Provider fields
                rp.entity_identifier_code as rendering_entity_identifier_code,
                rp.entity_type_qualifier as rendering_entity_type_qualifier,
                rp.rendering_provider_last_name,
                rp.rendering_provider_first_name,
                rp.rendering_provider_middle_name,
                rp.rendering_provider_id_qualifier,
                rp.rendering_provider_id,

                -- Subscriber fields
                sub.entity_identifier_code as subscriber_entity_identifier_code,
                sub.entity_type_qualifier as subscriber_entity_type_qualifier,
                sub.subscriber_last_name,
                sub.subscriber_first_name,
                sub.subscriber_middle_name,
                sub.subscriber_id_qualifier,
                sub.subscriber_id,
                sub.birth_date as subscriber_birth_date,
                sub.gender as subscriber_gender,
                sub.address_line_1 as subscriber_address_line_1,
                sub.city as subscriber_city,
                sub.state as subscriber_state,
                sub.zip_code as subscriber_zip_code,
                sub.payer_responsibility_code as subscriber_payer_responsibility_code,
                sub.relationship_code as subscriber_relationship_code,
                sub.claim_filing_indicator as subscriber_claim_filing_indicator,
                sub.hierarchical_id as subscriber_hierarchical_id,
                sub.parent_hierarchical_id as subscriber_parent_hierarchical_id,
                sub.hierarchical_level_code as subscriber_hierarchical_level_code,
                sub.hierarchical_child_code as subscriber_hierarchical_child_code,

                -- Payer fields
                p.entity_identifier_code as payer_entity_identifier_code,
                p.entity_type_qualifier as payer_entity_type_qualifier,
                p.payer_name,
                p.payer_id_qualifier,
                p.payer_id,

                -- Interchange fields
                i.sender_id,
                i.sender_qualifier,
                i.receiver_id,
                i.receiver_qualifier,
                i.interchange_date,
                i.interchange_time,
                i.control_number as interchange_control_number,
                i.version as interchange_version,
                i.test_indicator as interchange_test_indicator,

                -- Functional Group fields
                fg.functional_id,
                fg.sender_code as functional_sender_code,
                fg.receiver_code as functional_receiver_code,
                fg.group_date as functional_group_date,
                fg.group_time as functional_group_time,
                fg.group_control_number as functional_group_control_number,
                fg.implementation_version as functional_implementation_version,

                -- Transaction Header fields
                th.transaction_set_identifier,
                th.control_number as transaction_control_number,
                th.implementation_reference as transaction_implementation_reference,
                th.hierarchical_structure_code as transaction_hierarchical_structure_code,
                th.transaction_purpose_code,
                th.batch_id as transaction_batch_id,
                th.transaction_creation_date,
                th.transaction_creation_time,

                -- Submitter fields
                subm.entity_identifier_code as submitter_entity_identifier_code,
                subm.entity_type_qualifier as submitter_entity_type_qualifier,
                subm.submitter_name,
                subm.submitter_id_qualifier,
                subm.submitter_id,
                subm.contact_function_code as submitter_contact_function_code,
                subm.contact_name as submitter_contact_name,
                subm.communication_number_qualifier as submitter_communication_number_qualifier,
                subm.communication_number as submitter_communication_number,

                -- Receiver fields
                r.entity_identifier_code as receiver_entity_identifier_code,
                r.entity_type_qualifier as receiver_entity_type_qualifier,
                r.receiver_name,
                r.receiver_id_qualifier,
                r.receiver_id

            FROM claim c

            LEFT JOIN service_line sl
                ON TRUE

            LEFT JOIN claim_dates cd
                ON TRUE

            LEFT JOIN diagnosis d
                ON TRUE

            LEFT JOIN billing_provider bp
                ON TRUE

            LEFT JOIN rendering_provider rp
                ON TRUE

            LEFT JOIN subscriber sub
                ON TRUE

            LEFT JOIN payer p
                ON TRUE

            LEFT JOIN interchange i
                ON TRUE

            LEFT JOIN functional_group fg
                ON TRUE

            LEFT JOIN transaction_header th
                ON TRUE

            LEFT JOIN submitter subm
                ON TRUE

            LEFT JOIN receiver r
                ON TRUE

        """)

        rows = cursor.fetchall()

        for row in rows:

            self.insert(row)

        cursor.close()


    def insert(self, row):

        cursor = self.conn.cursor()

        query = """

            INSERT INTO ClaimHeader (

                -- Claim fields
                claim_number,
                total_charge_amount,
                facility_code,
                place_of_service,
                frequency_code,
                claim_type_code,
                provider_signature_indicator,
                assignment_participation_code,
                assignment_certification_indicator,
                release_of_information_code,

                -- Service Line fields
                line_number,
                procedure_qualifier,
                procedure_code,
                line_charge_amount,
                unit_measurement_code,
                service_unit_count,
                sv107_107,
                service_date,

                -- Claim Dates fields
                claim_service_date,

                -- Diagnosis fields
                diagnosis_type,
                diagnosis_code,

                -- Billing Provider fields
                billing_provider_name,
                billing_provider_id_qualifier,
                billing_provider_id,
                billing_provider_address_line_1,
                billing_provider_address_line_2,
                billing_provider_city,
                billing_provider_state,
                billing_provider_zip_code,
                billing_provider_tax_id,
                billing_provider_hierarchical_id,
                billing_provider_hierarchical_level_code,
                billing_provider_hierarchical_child_code,

                -- Rendering Provider fields
                rendering_provider_last_name,
                rendering_provider_first_name,
                rendering_provider_middle_name,
                rendering_provider_id_qualifier,
                rendering_provider_id,

                -- Subscriber fields
                subscriber_last_name,
                subscriber_first_name,
                subscriber_middle_name,
                subscriber_id_qualifier,
                subscriber_id,
                subscriber_birth_date,
                subscriber_gender,
                subscriber_address_line_1,
                subscriber_city,
                subscriber_state,
                subscriber_zip_code,
                subscriber_payer_responsibility_code,
                subscriber_relationship_code,
                subscriber_claim_filing_indicator,
                subscriber_hierarchical_id,
                subscriber_parent_hierarchical_id,
                subscriber_hierarchical_level_code,
                subscriber_hierarchical_child_code,

                -- Payer fields
                payer_name,
                payer_id_qualifier,
                payer_id,

                -- Interchange fields
                sender_id,
                sender_qualifier,
                receiver_id,
                receiver_qualifier,
                interchange_date,
                interchange_time,
                interchange_control_number,
                interchange_version,
                interchange_test_indicator,

                -- Functional Group fields
                functional_id,
                functional_sender_code,
                functional_receiver_code,
                functional_group_date,
                functional_group_time,
                functional_group_control_number,
                functional_implementation_version,

                -- Transaction Header fields
                transaction_set_identifier,
                transaction_control_number,
                transaction_implementation_reference,
                transaction_hierarchical_structure_code,
                transaction_purpose_code,
                transaction_batch_id,
                transaction_creation_date,
                transaction_creation_time,

                -- Submitter fields
                submitter_name,
                submitter_id_qualifier,
                submitter_id,
                submitter_contact_function_code,
                submitter_contact_name,
                submitter_communication_number_qualifier,
                submitter_communication_number,

                -- Receiver fields
                receiver_name,
                receiver_id_qualifier,
                receiver_id

            )

            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s
            )

        """

        values = (

            # Claim fields
            row["claim_number"],
            row["total_charge_amount"],
            row["facility_code"],
            row["place_of_service"],
            row["frequency_code"],
            row["claim_type_code"],
            row["provider_signature_indicator"],
            row["assignment_participation_code"],
            row["assignment_certification_indicator"],
            row["release_of_information_code"],

            # Service Line fields
            row["line_number"],
            row["procedure_qualifier"],
            row["procedure_code"],
            row["line_charge_amount"],
            row["unit_measurement_code"],
            row["service_unit_count"],
            row["sv107_107"],
            row["service_date"],

            # Claim Dates fields
            row["claim_service_date"],

            # Diagnosis fields
            row["diagnosis_type"],
            row["diagnosis_code"],

            # Billing Provider fields
            row["billing_provider_name"],
            row["billing_provider_id_qualifier"],
            row["billing_provider_id"],
            row["billing_provider_address_line_1"],
            row["billing_provider_address_line_2"],
            row["billing_provider_city"],
            row["billing_provider_state"],
            row["billing_provider_zip_code"],
            row["billing_provider_tax_id"],
            row["billing_provider_hierarchical_id"],
            row["billing_provider_hierarchical_level_code"],
            row["billing_provider_hierarchical_child_code"],

            # Rendering Provider fields
            row["rendering_provider_last_name"],
            row["rendering_provider_first_name"],
            row["rendering_provider_middle_name"],
            row["rendering_provider_id_qualifier"],
            row["rendering_provider_id"],

            # Subscriber fields
            row["subscriber_last_name"],
            row["subscriber_first_name"],
            row["subscriber_middle_name"],
            row["subscriber_id_qualifier"],
            row["subscriber_id"],
            row["subscriber_birth_date"],
            row["subscriber_gender"],
            row["subscriber_address_line_1"],
            row["subscriber_city"],
            row["subscriber_state"],
            row["subscriber_zip_code"],
            row["subscriber_payer_responsibility_code"],
            row["subscriber_relationship_code"],
            row["subscriber_claim_filing_indicator"],
            row["subscriber_hierarchical_id"],
            row["subscriber_parent_hierarchical_id"],
            row["subscriber_hierarchical_level_code"],
            row["subscriber_hierarchical_child_code"],

            # Payer fields
            row["payer_name"],
            row["payer_id_qualifier"],
            row["payer_id"],

            # Interchange fields
            row["sender_id"],
            row["sender_qualifier"],
            row["receiver_id"],
            row["receiver_qualifier"],
            row["interchange_date"],
            row["interchange_time"],
            row["interchange_control_number"],
            row["interchange_version"],
            row["interchange_test_indicator"],

            # Functional Group fields
            row["functional_id"],
            row["functional_sender_code"],
            row["functional_receiver_code"],
            row["functional_group_date"],
            row["functional_group_time"],
            row["functional_group_control_number"],
            row["functional_implementation_version"],

            # Transaction Header fields
            row["transaction_set_identifier"],
            row["transaction_control_number"],
            row["transaction_implementation_reference"],
            row["transaction_hierarchical_structure_code"],
            row["transaction_purpose_code"],
            row["transaction_batch_id"],
            row["transaction_creation_date"],
            row["transaction_creation_time"],

            # Submitter fields
            row["submitter_name"],
            row["submitter_id_qualifier"],
            row["submitter_id"],
            row["submitter_contact_function_code"],
            row["submitter_contact_name"],
            row["submitter_communication_number_qualifier"],
            row["submitter_communication_number"],

            # Receiver fields
            row["receiver_name"],
            row["receiver_id_qualifier"],
            row["receiver_id"]

        )

        cursor.execute(query, values)

        self.conn.commit()

        cursor.close()