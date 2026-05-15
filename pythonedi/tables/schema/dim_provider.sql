-- =============================================================
-- DIMENSION: PROVIDER (Gold Layer)
-- Derived from: billing_provider and rendering_provider tables
-- =============================================================
CREATE TABLE IF NOT EXISTS dim_provider (
    provider_key SERIAL PRIMARY KEY,
    provider_id VARCHAR(100) UNIQUE,
    npi VARCHAR(20) UNIQUE,
    
    last_name VARCHAR(300),
    first_name VARCHAR(300),
    middle_initial VARCHAR(10),
    
    taxonomy_code_1 VARCHAR(20),
    specialty_code_1 VARCHAR(20),
    taxonomy_code_2 VARCHAR(20),
    specialty_code_2 VARCHAR(20),
    
    provider_type VARCHAR(100),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
