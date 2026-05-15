CREATE TABLE IF NOT EXISTS claim_dates (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    -- DTP[0] – Service Date (431)
    service_date_qualifier VARCHAR(10),
    service_date_format VARCHAR(10),
    service_date VARCHAR(25),

    -- DTP[1] – Statement Dates (434)
    statement_date_qualifier VARCHAR(10),
    statement_date_format VARCHAR(10),
    statement_from_date VARCHAR(25),

    -- DTP[2] – Admission Date (435)
    admission_date_qualifier VARCHAR(10),
    admission_date_format VARCHAR(10),
    admission_date VARCHAR(25),

    -- DTP[3] – Discharge Date (096)
    discharge_date_qualifier VARCHAR(10),
    discharge_date_format VARCHAR(10),
    discharge_date VARCHAR(25),

    -- DTP[4] – Onset of Current Illness (431)
    onset_date_qualifier VARCHAR(10),
    onset_date_format VARCHAR(10),
    onset_date VARCHAR(25),

    -- DTP[5] – Accident Date (439)
    accident_date_qualifier VARCHAR(10),
    accident_date_format VARCHAR(10),
    accident_date VARCHAR(25),

    -- DTP[6] – Last Seen Date (304)
    last_seen_date_qualifier VARCHAR(10),
    last_seen_date_format VARCHAR(10),
    last_seen_date VARCHAR(25),

    -- DTP[7] – Initial Treatment Date (454)
    initial_treatment_date_qualifier VARCHAR(10),
    initial_treatment_date_format VARCHAR(10),
    initial_treatment_date VARCHAR(25),

    -- DTP[8] – Last X-Ray Date (455)
    last_xray_date_qualifier VARCHAR(10),
    last_xray_date VARCHAR(25),

    -- DTP[9] – Hearing / Vision Prescription Date (471)
    prescription_date_qualifier VARCHAR(10),
    prescription_date VARCHAR(25),

    -- DTP[10] – Disability Dates (360/361)
    disability_from_date_qualifier VARCHAR(10),
    disability_from_date VARCHAR(25),

    -- DTP[11] – Last Worked Date (297)
    last_worked_date_qualifier VARCHAR(10),
    last_worked_date VARCHAR(25),

    -- DTP[12] – Return to Work Date (296)
    return_to_work_date_qualifier VARCHAR(10),
    return_to_work_date VARCHAR(25),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_claim_dates_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);