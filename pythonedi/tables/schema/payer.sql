CREATE TABLE IF NOT EXISTS payer (

    id SERIAL PRIMARY KEY,

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    payer_name VARCHAR(255),
    payer_first_name VARCHAR(255),
    payer_middle_name VARCHAR(255),
    payer_prefix VARCHAR(50),
    payer_suffix VARCHAR(50),

    payer_id_qualifier VARCHAR(50),
    payer_id VARCHAR(100) UNIQUE,

    -- N3 – Address
    address_line_1 TEXT,
    address_line_2 TEXT,

    -- N4 – City / State / ZIP
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),

    -- REF – Payer Additional Identifiers
    payer_ref_qualifier_1 VARCHAR(10),
    payer_ref_id_1 VARCHAR(100),
    payer_ref_qualifier_2 VARCHAR(10),
    payer_ref_id_2 VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);