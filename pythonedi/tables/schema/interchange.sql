CREATE TABLE IF NOT EXISTS interchange (

    id SERIAL PRIMARY KEY,

    -- ISA Segment
    sender_qualifier VARCHAR(20),
    sender_id VARCHAR(100),

    receiver_qualifier VARCHAR(20),
    receiver_id VARCHAR(100),

    interchange_date VARCHAR(20),
    interchange_time VARCHAR(20),

    repetition_separator VARCHAR(5),
    control_version_number VARCHAR(20),
    control_number VARCHAR(100) UNIQUE,
    acknowledgment_requested VARCHAR(5),
    test_indicator VARCHAR(10),
    component_element_separator VARCHAR(5),

    -- IEA Segment
    functional_group_count VARCHAR(10),
    iea_control_number VARCHAR(100),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);