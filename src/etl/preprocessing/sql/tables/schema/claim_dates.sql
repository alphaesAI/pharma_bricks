CREATE TABLE IF NOT EXISTS claim_dates (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    service_date DATE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_claim_dates_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);