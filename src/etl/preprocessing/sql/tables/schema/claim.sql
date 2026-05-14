CREATE TABLE IF NOT EXISTS claim (

    -- =====================================
    -- Primary Key
    -- =====================================

    claim_number VARCHAR(100) PRIMARY KEY,

    -- =====================================
    -- Foreign Keys
    -- =====================================

    subscriber_id VARCHAR(100),
    billing_provider_id VARCHAR(100),
    payer_id VARCHAR(100),
    rendering_provider_id VARCHAR(100),

    -- =====================================
    -- Claim Details (CLM Segment)
    -- =====================================

    total_charge_amount DECIMAL(18,2),

    facility_code VARCHAR(20),
    place_of_service VARCHAR(100),
    frequency_code VARCHAR(20),
    claim_type_code VARCHAR(20),

    provider_signature_indicator VARCHAR(10),
    assignment_participation_code VARCHAR(20),
    assignment_certification_indicator VARCHAR(10),
    release_of_information_code VARCHAR(10),

    -- =====================================
    -- Claim Metadata
    -- =====================================

    transaction_control_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- =====================================
    -- Foreign Key Constraints
    -- =====================================

    CONSTRAINT fk_claim_subscriber
        FOREIGN KEY (subscriber_id)
        REFERENCES subscriber(subscriber_id),

    CONSTRAINT fk_claim_billing_provider
        FOREIGN KEY (billing_provider_id)
        REFERENCES billing_provider(billing_provider_id),

    CONSTRAINT fk_claim_payer
        FOREIGN KEY (payer_id)
        REFERENCES payer(payer_id),

    CONSTRAINT fk_claim_rendering_provider
        FOREIGN KEY (rendering_provider_id)
        REFERENCES rendering_provider(rendering_provider_id)

);