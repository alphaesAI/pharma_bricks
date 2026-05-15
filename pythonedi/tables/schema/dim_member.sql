-- =============================================================
-- DIMENSION: MEMBER (Gold Layer)
-- Derived from: subscriber and patient tables
-- =============================================================
CREATE TABLE IF NOT EXISTS dim_member (
    member_key SERIAL PRIMARY KEY,
    bis_internal_person_id VARCHAR(255),
    client_id VARCHAR(20),
    unique_person_key VARCHAR(20),
    plan_member_id VARCHAR(100) UNIQUE,
    subscriber_id VARCHAR(100) REFERENCES subscriber(subscriber_id),
    
    last_name VARCHAR(300),
    first_name VARCHAR(300),
    middle_initial VARCHAR(10),
    
    date_of_birth DATE,
    gender VARCHAR(20),
    
    address_line_1 VARCHAR(510),
    address_line_2 VARCHAR(510),
    city VARCHAR(200),
    state VARCHAR(20),
    zip_code VARCHAR(20),
    
    phone_number VARCHAR(20),
    email VARCHAR(255),
    
    race_code VARCHAR(20),
    ethnicity_code VARCHAR(20),
    spoken_language VARCHAR(20),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
