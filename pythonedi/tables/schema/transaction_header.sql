-- =============================================================
-- TRANSACTION SET HEADER (ST / BHT / SE)
-- Maps to: mapping.py → "transaction_header"
-- =============================================================
CREATE TABLE IF NOT EXISTS transaction_header (

    id SERIAL PRIMARY KEY,

    -- ST Segment
    transaction_set_identifier VARCHAR(10),
    transaction_control_number VARCHAR(100) UNIQUE,
    implementation_reference VARCHAR(50),

    -- BHT Segment
    hierarchical_structure_code VARCHAR(10),
    transaction_purpose_code VARCHAR(10),
    batch_id VARCHAR(100),
    transaction_creation_date VARCHAR(25),
    transaction_creation_time VARCHAR(25),
    claim_or_encounter_identifier VARCHAR(10),

    -- SE Segment
    included_segment_count VARCHAR(10),
    se_control_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
