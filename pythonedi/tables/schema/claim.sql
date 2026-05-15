CREATE TABLE IF NOT EXISTS claim (

    claim_number VARCHAR(100) PRIMARY KEY,

    -- Foreign Keys
    subscriber_id VARCHAR(100),
    billing_provider_npi VARCHAR(100),
    payer_id VARCHAR(100),
    rendering_provider_npi VARCHAR(100),

    -- CLM Segment
    total_charge_amount DECIMAL(18,2),

    facility_code VARCHAR(20),
    place_of_service VARCHAR(100),
    frequency_code VARCHAR(20),
    claim_type_code VARCHAR(20),

    provider_signature_indicator VARCHAR(10),
    assignment_participation_code VARCHAR(20),
    assignment_certification_indicator VARCHAR(10),
    release_of_information_code VARCHAR(10),
    patient_signature_source_code VARCHAR(10),

    -- Related Causes
    related_causes_code_1 VARCHAR(10),
    related_causes_code_2 VARCHAR(10),
    related_causes_code_3 VARCHAR(10),
    auto_accident_state VARCHAR(5),

    -- Additional CLM fields
    special_program_code VARCHAR(10),
    yes_no_condition_code_1 VARCHAR(5),
    yes_no_condition_code_2 VARCHAR(5),
    provider_agreement_code VARCHAR(10),
    claim_status_code VARCHAR(10),
    yes_no_condition_code_3 VARCHAR(5),
    claim_submission_reason_code VARCHAR(10),
    delay_reason_code VARCHAR(10),

    -- Metadata
    transaction_control_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Foreign Key Constraints
    CONSTRAINT fk_claim_subscriber
        FOREIGN KEY (subscriber_id)
        REFERENCES subscriber(subscriber_id),

    CONSTRAINT fk_claim_payer
        FOREIGN KEY (payer_id)
        REFERENCES payer(payer_id)
);