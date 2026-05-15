-- =============================================================
-- RECEIVER (NM1*40)
-- Maps to: mapping.py → "receiver"
-- =============================================================
CREATE TABLE IF NOT EXISTS receiver (

    id SERIAL PRIMARY KEY,

    -- NM1 Segment
    entity_identifier_code VARCHAR(20),
    entity_type_qualifier VARCHAR(20),

    receiver_last_name VARCHAR(255),
    receiver_first_name VARCHAR(255),
    receiver_middle_name VARCHAR(255),
    receiver_prefix VARCHAR(50),
    receiver_suffix VARCHAR(50),

    receiver_id_qualifier VARCHAR(50),
    receiver_id VARCHAR(100) UNIQUE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);