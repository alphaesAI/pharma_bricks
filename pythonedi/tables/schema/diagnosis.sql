CREATE TABLE IF NOT EXISTS diagnosis (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    diagnosis_type VARCHAR(20),
    diagnosis_code VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_diagnosis_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);