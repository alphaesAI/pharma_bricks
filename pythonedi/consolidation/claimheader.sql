-- claim_header.sql

CREATE TABLE IF NOT EXISTS ClaimHeader (

    claim_id SERIAL PRIMARY KEY,

    -- Claim fields
    claim_number VARCHAR(100),
    total_charge_amount DECIMAL(18,2),
    facility_code VARCHAR(20),
    place_of_service VARCHAR(100),
    frequency_code VARCHAR(20),
    claim_type_code VARCHAR(20),
    provider_signature_indicator VARCHAR(10),
    assignment_participation_code VARCHAR(20),
    assignment_certification_indicator VARCHAR(10),
    release_of_information_code VARCHAR(10),

    -- Service Line fields
    line_number VARCHAR(20),
    procedure_qualifier VARCHAR(20),
    procedure_code VARCHAR(50),
    line_charge_amount DECIMAL(18,2),
    unit_measurement_code VARCHAR(20),
    service_unit_count INTEGER,
    sv107_107 VARCHAR(50),
    service_date VARCHAR(20),

    -- Claim Dates fields
    claim_service_date VARCHAR(20),

    -- Diagnosis fields
    diagnosis_type VARCHAR(20),
    diagnosis_code VARCHAR(50),

    -- Billing Provider fields
    billing_provider_name VARCHAR(255),
    billing_provider_id_qualifier VARCHAR(50),
    billing_provider_id VARCHAR(100),
    billing_provider_address_line_1 TEXT,
    billing_provider_address_line_2 TEXT,
    billing_provider_city VARCHAR(100),
    billing_provider_state VARCHAR(50),
    billing_provider_zip_code VARCHAR(20),
    billing_provider_tax_id VARCHAR(100),
    billing_provider_hierarchical_id VARCHAR(50),
    billing_provider_hierarchical_level_code VARCHAR(20),
    billing_provider_hierarchical_child_code VARCHAR(20),

    -- Rendering Provider fields
    rendering_provider_last_name VARCHAR(255),
    rendering_provider_first_name VARCHAR(255),
    rendering_provider_middle_name VARCHAR(255),
    rendering_provider_id_qualifier VARCHAR(50),
    rendering_provider_id VARCHAR(100),

    -- Subscriber fields
    subscriber_last_name VARCHAR(255),
    subscriber_first_name VARCHAR(255),
    subscriber_middle_name VARCHAR(255),
    subscriber_id_qualifier VARCHAR(50),
    subscriber_id VARCHAR(100),
    subscriber_birth_date DATE,
    subscriber_gender VARCHAR(10),
    subscriber_address_line_1 TEXT,
    subscriber_city VARCHAR(100),
    subscriber_state VARCHAR(50),
    subscriber_zip_code VARCHAR(20),
    subscriber_payer_responsibility_code VARCHAR(20),
    subscriber_relationship_code VARCHAR(20),
    subscriber_claim_filing_indicator VARCHAR(20),
    subscriber_hierarchical_id VARCHAR(50),
    subscriber_parent_hierarchical_id VARCHAR(50),
    subscriber_hierarchical_level_code VARCHAR(20),
    subscriber_hierarchical_child_code VARCHAR(20),

    -- Payer fields
    payer_name VARCHAR(255),
    payer_id_qualifier VARCHAR(50),
    payer_id VARCHAR(100),

    -- Interchange fields
    sender_id VARCHAR(100),
    sender_qualifier VARCHAR(20),
    receiver_id VARCHAR(100),
    receiver_qualifier VARCHAR(20),
    interchange_date VARCHAR(20),
    interchange_time VARCHAR(20),
    interchange_control_number VARCHAR(100),
    interchange_version VARCHAR(20),
    interchange_test_indicator VARCHAR(10),

    -- Functional Group fields
    functional_id VARCHAR(20),
    functional_sender_code VARCHAR(100),
    functional_receiver_code VARCHAR(100),
    functional_group_date VARCHAR(20),
    functional_group_time VARCHAR(20),
    functional_group_control_number VARCHAR(100),
    functional_implementation_version VARCHAR(50),

    -- Transaction Header fields
    transaction_set_identifier VARCHAR(20),
    transaction_control_number VARCHAR(100),
    transaction_implementation_reference VARCHAR(50),
    transaction_hierarchical_structure_code VARCHAR(20),
    transaction_purpose_code VARCHAR(20),
    transaction_batch_id VARCHAR(100),
    transaction_creation_date VARCHAR(20),
    transaction_creation_time VARCHAR(20),

    -- Submitter fields
    submitter_name VARCHAR(255),
    submitter_id_qualifier VARCHAR(50),
    submitter_id VARCHAR(100),
    submitter_contact_function_code VARCHAR(20),
    submitter_contact_name VARCHAR(255),
    submitter_communication_number_qualifier VARCHAR(20),
    submitter_communication_number VARCHAR(100),

    -- Receiver fields
    receiver_name VARCHAR(255),
    receiver_id_qualifier VARCHAR(50),
    receiver_id VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);