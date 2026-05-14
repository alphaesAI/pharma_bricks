CREATE TABLE IF NOT EXISTS functional_group (

    id SERIAL PRIMARY KEY,

    functional_id VARCHAR(20),

    sender_code VARCHAR(100),
    receiver_code VARCHAR(100),

    group_date VARCHAR(20),
    group_time VARCHAR(20),

    group_control_number VARCHAR(100) UNIQUE,

    implementation_version VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);