CREATE TABLE IF NOT EXISTS receiver (

    id SERIAL PRIMARY KEY,

    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    receiver_name VARCHAR(255),
    receiver_id_qualifier VARCHAR(50),
    receiver_id VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
