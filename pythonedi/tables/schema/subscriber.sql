CREATE TABLE IF NOT EXISTS subscriber (

    id SERIAL PRIMARY KEY,

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    subscriber_last_name VARCHAR(255),
    subscriber_first_name VARCHAR(255),
    subscriber_middle_name VARCHAR(255),
    subscriber_name_prefix VARCHAR(50),
    subscriber_name_suffix VARCHAR(50),

    subscriber_id_qualifier VARCHAR(50),
    subscriber_id VARCHAR(100) UNIQUE,

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

    -- DMG – Demographics
    date_time_period_format_qualifier VARCHAR(10),
    birth_date VARCHAR(25),
    gender_code VARCHAR(10),
    marital_status_code VARCHAR(10),
    race_or_ethnicity_code VARCHAR(10),
    citizenship_status_code VARCHAR(10),
    country_code_dmg VARCHAR(10),

    -- REF – SSN / Additional Identifiers
    ssn_qualifier VARCHAR(10),
    ssn VARCHAR(20),

    -- HL Segment (2000B – merged from subscriber_hl)
    hierarchical_id VARCHAR(50),
    parent_hierarchical_id VARCHAR(50),
    hierarchical_level_code VARCHAR(20),
    hierarchical_child_code VARCHAR(20),

    -- SBR – Subscriber Information
    payer_responsibility_code VARCHAR(10),
    individual_relationship_code VARCHAR(10),
    insured_group_or_policy_number VARCHAR(100),
    insured_group_name VARCHAR(255),
    insurance_type_code VARCHAR(10),
    coordination_of_benefits_code VARCHAR(10),
    yes_no_condition_code VARCHAR(5),
    employment_status_code VARCHAR(10),
    claim_filing_indicator VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);