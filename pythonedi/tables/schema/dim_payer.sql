-- =============================================================
-- DIMENSION: PAYER (Gold Layer)
-- Derived from: payer table
-- =============================================================
CREATE TABLE IF NOT EXISTS dim_payer (
    payer_key SERIAL PRIMARY KEY,
    payer_id VARCHAR(100) UNIQUE,
    payer_name VARCHAR(255),
    
    address_line_1 TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    zip_code VARCHAR(20),
    
    payer_ref_id_1 VARCHAR(100),
    payer_ref_id_2 VARCHAR(100),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
