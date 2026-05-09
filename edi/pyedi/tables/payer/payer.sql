CREATE TABLE IF NOT EXISTS payer (

    id SERIAL PRIMARY KEY,

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    payer_name VARCHAR(255),
    payer_id_qualifier VARCHAR(50),
    payer_id VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
