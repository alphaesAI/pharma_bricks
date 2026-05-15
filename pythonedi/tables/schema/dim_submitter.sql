-- =============================================================
-- DIMENSION: SUBMITTER (Gold Layer)
-- Derived from: submitter table
-- =============================================================
CREATE TABLE IF NOT EXISTS dim_submitter (
    submitter_key SERIAL PRIMARY KEY,
    submitter_id VARCHAR(100) UNIQUE,
    submitter_name VARCHAR(255),
    
    contact_name VARCHAR(255),
    communication_number_1 VARCHAR(100),
    communication_number_2 VARCHAR(100),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
