CREATE TABLE IF NOT EXISTS billing_provider (

    id SERIAL PRIMARY KEY,

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    billing_provider_name VARCHAR(255),
    billing_provider_id_qualifier VARCHAR(50),
    billing_provider_id VARCHAR(100),

    address_line_1 TEXT,
    address_line_2 TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),

    tax_id VARCHAR(100),

    hierarchical_id VARCHAR(50),
    hierarchical_level_code VARCHAR(20),
    hierarchical_child_code VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
