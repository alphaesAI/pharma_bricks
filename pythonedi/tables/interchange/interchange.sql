CREATE TABLE IF NOT EXISTS interchange (

    id SERIAL PRIMARY KEY,

    sender_id VARCHAR(100),
    sender_qualifier VARCHAR(20),
    receiver_id VARCHAR(100),
    receiver_qualifier VARCHAR(20),

    interchange_date VARCHAR(20),
    interchange_time VARCHAR(20),

    control_number VARCHAR(100),
    version VARCHAR(20),
    test_indicator VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
