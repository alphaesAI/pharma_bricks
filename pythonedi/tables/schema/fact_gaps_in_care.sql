-- =============================================================
-- FACT: GAPS IN CARE (Platinum Layer)
-- Derived from: claim, service, and diagnosis tables
-- =============================================================
CREATE TABLE IF NOT EXISTS fact_gaps_in_care (
    gaps_in_care_id SERIAL PRIMARY KEY,
    
    quality_year_month_key INT,
    member_key INT REFERENCES dim_member(member_key),
    provider_key INT REFERENCES dim_provider(provider_key),
    payer_key INT REFERENCES dim_payer(payer_key),
    
    measure_code VARCHAR(40),
    measure_name VARCHAR(200),
    
    numer_cnt INT DEFAULT 0,
    denom_cnt INT DEFAULT 0,
    
    pdc DECIMAL(18,4),
    
    last_hb_val DECIMAL(18,4),
    last_hb_date DATE,
    
    last_bp_dia INT,
    last_bp_sys INT,
    last_bp_date DATE,
    
    claim_number VARCHAR(100) REFERENCES claim(claim_number),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
