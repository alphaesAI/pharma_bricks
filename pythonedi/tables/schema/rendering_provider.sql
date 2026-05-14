CREATE TABLE IF NOT EXISTS rendering_provider (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    rendering_provider_last_name VARCHAR(255),
    rendering_provider_first_name VARCHAR(255),
    rendering_provider_middle_name VARCHAR(255),

    rendering_provider_id_qualifier VARCHAR(50),
    rendering_provider_id VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_rendering_provider_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);