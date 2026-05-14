CREATE TABLE IF NOT EXISTS subscriber (

    subscriber_id VARCHAR(100) PRIMARY KEY,

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    subscriber_last_name VARCHAR(255),
    subscriber_first_name VARCHAR(255),
    subscriber_middle_name VARCHAR(255),

    subscriber_id_qualifier VARCHAR(50),

    birth_date DATE,
    gender VARCHAR(10),

    address_line_1 TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),

    payer_responsibility_code VARCHAR(20),
    relationship_code VARCHAR(20),
    claim_filing_indicator VARCHAR(20),

    hierarchical_id VARCHAR(50),
    parent_hierarchical_id VARCHAR(50),
    hierarchical_level_code VARCHAR(20),
    hierarchical_child_code VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);