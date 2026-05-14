CREATE TABLE IF NOT EXISTS claim (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),
    total_charge_amount DECIMAL(18, 2),

    facility_code VARCHAR(20),
    place_of_service VARCHAR(100),
    frequency_code VARCHAR(20),
    claim_type_code VARCHAR(20),

    provider_signature_indicator VARCHAR(10),
    assignment_participation_code VARCHAR(20),
    assignment_certification_indicator VARCHAR(10),
    release_of_information_code VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
