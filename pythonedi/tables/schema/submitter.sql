-- =============================================================
-- SUBMITTER (NM1*41 / PER)
-- Maps to: mapping.py → "submitter"
-- =============================================================
CREATE TABLE IF NOT EXISTS submitter (

    id SERIAL PRIMARY KEY,

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    submitter_last_name VARCHAR(255),
    submitter_first_name VARCHAR(255),
    submitter_middle_name VARCHAR(255),
    submitter_prefix VARCHAR(50),
    submitter_suffix VARCHAR(50),

    submitter_id_qualifier VARCHAR(50),
    submitter_id VARCHAR(100) UNIQUE,

    -- PER Segment – Contact Information
    contact_function_code VARCHAR(20),
    contact_name VARCHAR(255),

    communication_number_qualifier_1 VARCHAR(20),
    communication_number_1 VARCHAR(100),
    communication_number_qualifier_2 VARCHAR(20),
    communication_number_2 VARCHAR(100),
    communication_number_qualifier_3 VARCHAR(20),
    communication_number_3 VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);