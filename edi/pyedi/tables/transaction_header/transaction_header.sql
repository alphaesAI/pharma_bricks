CREATE TABLE IF NOT EXISTS transaction_header (

    id SERIAL PRIMARY KEY,

    transaction_set_identifier VARCHAR(20),
    transaction_control_number VARCHAR(100),
    implementation_reference VARCHAR(50),

    hierarchical_structure_code VARCHAR(20),
    transaction_purpose_code VARCHAR(20),
    batch_id VARCHAR(100),

    transaction_creation_date VARCHAR(20),
    transaction_creation_time VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
