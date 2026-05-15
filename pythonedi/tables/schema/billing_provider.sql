CREATE TABLE IF NOT EXISTS billing_provider (

    id SERIAL PRIMARY KEY,

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    billing_provider_last_name VARCHAR(255),
    billing_provider_first_name VARCHAR(255),
    billing_provider_middle_name VARCHAR(255),
    billing_provider_prefix VARCHAR(50),
    billing_provider_suffix VARCHAR(50),

    billing_provider_id_qualifier VARCHAR(50),
    billing_provider_npi VARCHAR(100) UNIQUE,

    -- N3 – Address
    address_line_1 TEXT,
    address_line_2 TEXT,

    -- N4 – City / State / ZIP
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    country_code VARCHAR(10),
    location_qualifier VARCHAR(20),
    location_identifier VARCHAR(50),
    country_subdivision_code VARCHAR(10),

    -- REF – Tax ID / Additional Identifiers
    tax_id_qualifier VARCHAR(10),
    tax_id VARCHAR(100),
    upin_qualifier VARCHAR(10),
    upin VARCHAR(50),
    clia_qualifier VARCHAR(10),
    clia_number VARCHAR(50),

    -- PER – Contact Information
    contact_function_code VARCHAR(20),
    contact_name VARCHAR(255),
    contact_comm_qualifier_1 VARCHAR(20),
    contact_comm_number_1 VARCHAR(100),
    contact_comm_qualifier_2 VARCHAR(20),
    contact_comm_number_2 VARCHAR(100),

    -- HL Segment (2000A – merged from billing_provider_hl)
    hierarchical_id VARCHAR(50),
    parent_hierarchical_id VARCHAR(50),
    hierarchical_level_code VARCHAR(20),
    hierarchical_child_code VARCHAR(20),

    -- PRV – Billing Provider Specialty
    prv_provider_code VARCHAR(10),
    prv_reference_id_qualifier VARCHAR(10),
    prv_provider_taxonomy_code VARCHAR(50),

    -- CUR – Foreign Currency
    cur_entity_identifier_code VARCHAR(10),
    cur_currency_code VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);