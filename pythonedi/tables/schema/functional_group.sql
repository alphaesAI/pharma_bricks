CREATE TABLE IF NOT EXISTS functional_group (

    id SERIAL PRIMARY KEY,

    -- GS Segment
    functional_id VARCHAR(20),

    sender_code VARCHAR(100),
    receiver_code VARCHAR(100),

    group_date VARCHAR(20),
    group_time VARCHAR(20), 

    group_control_number VARCHAR(100) UNIQUE,
    responsible_agency_code VARCHAR(10),
    implementation_version VARCHAR(50),

    -- GE Segment
    transaction_set_count VARCHAR(10),
    ge_control_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);