CREATE TABLE IF NOT EXISTS submitter (

    id SERIAL PRIMARY KEY,

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    submitter_name VARCHAR(255),

    submitter_id_qualifier VARCHAR(50),
    submitter_id VARCHAR(100) UNIQUE,

    contact_function_code VARCHAR(20),
    contact_name VARCHAR(255),

    communication_number_qualifier VARCHAR(20),
    communication_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);