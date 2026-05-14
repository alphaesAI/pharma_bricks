CREATE TABLE IF NOT EXISTS diagnosis (

    id SERIAL PRIMARY KEY,

    diagnosis_type VARCHAR(20),
    diagnosis_code VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
