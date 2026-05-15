CREATE TABLE IF NOT EXISTS rendering_provider (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    rendering_provider_last_name VARCHAR(255),
    rendering_provider_first_name VARCHAR(255),
    rendering_provider_middle_name VARCHAR(255),
    rendering_provider_prefix VARCHAR(50),
    rendering_provider_suffix VARCHAR(50),

    rendering_provider_id_qualifier VARCHAR(50),
    rendering_provider_npi VARCHAR(100) UNIQUE,

    -- PRV – Rendering Provider Specialty
    provider_code VARCHAR(10),
    reference_id_qualifier VARCHAR(10),
    provider_taxonomy_code VARCHAR(50),

    -- REF – Additional Identifiers
    ref_qualifier_1 VARCHAR(10),
    ref_id_1 VARCHAR(100),
    ref_qualifier_2 VARCHAR(10),
    ref_id_2 VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rendering_provider_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);