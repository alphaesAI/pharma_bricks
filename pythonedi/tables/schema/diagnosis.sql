CREATE TABLE IF NOT EXISTS diagnosis (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100) REFERENCES claim(claim_number),

    -- HI[0] – Principal Diagnosis (ICD-10-CM / ICD-9-CM)
    principal_diagnosis_type VARCHAR(10),
    principal_diagnosis_code VARCHAR(20),
    principal_diagnosis_date VARCHAR(25),

    -- HI[0] – Additional Diagnoses (hi02 through hi12)
    additional_diagnosis_type_2 VARCHAR(10),
    additional_diagnosis_code_2 VARCHAR(20),
    additional_diagnosis_type_3 VARCHAR(10),
    additional_diagnosis_code_3 VARCHAR(20),
    additional_diagnosis_type_4 VARCHAR(10),
    additional_diagnosis_code_4 VARCHAR(20),
    additional_diagnosis_type_5 VARCHAR(10),
    additional_diagnosis_code_5 VARCHAR(20),
    additional_diagnosis_type_6 VARCHAR(10),
    additional_diagnosis_code_6 VARCHAR(20),
    additional_diagnosis_type_7 VARCHAR(10),
    additional_diagnosis_code_7 VARCHAR(20),
    additional_diagnosis_type_8 VARCHAR(10),
    additional_diagnosis_code_8 VARCHAR(20),
    additional_diagnosis_type_9 VARCHAR(10),
    additional_diagnosis_code_9 VARCHAR(20),
    additional_diagnosis_type_10 VARCHAR(10),
    additional_diagnosis_code_10 VARCHAR(20),
    additional_diagnosis_type_11 VARCHAR(10),
    additional_diagnosis_code_11 VARCHAR(20),
    additional_diagnosis_type_12 VARCHAR(10),
    additional_diagnosis_code_12 VARCHAR(20),

    -- HI[1] – Reason for Visit / E-Code / POA
    reason_for_visit_type VARCHAR(10),
    reason_for_visit_code VARCHAR(20),

    -- HI[2] – External Cause of Injury
    external_cause_type VARCHAR(10),
    external_cause_code VARCHAR(20),

    -- HI[3] – Principal Procedure (Institutional ICD-10-PCS)
    principal_procedure_type VARCHAR(10),
    principal_procedure_code VARCHAR(20),
    principal_procedure_date VARCHAR(25),

    -- HI[4] – Other Procedures (Institutional)
    other_procedure_type_2 VARCHAR(10),
    other_procedure_code_2 VARCHAR(20),
    other_procedure_date_2 VARCHAR(25),

    -- HI[5] – Occurrence Codes (UB-04)
    occurrence_code_type VARCHAR(10),
    occurrence_code VARCHAR(20),
    occurrence_date VARCHAR(25),

    -- HI[6] – Value Codes (Institutional / UB)
    value_code_type VARCHAR(10),
    value_code VARCHAR(20),
    value_amount VARCHAR(20),

    -- HI[7] – Condition Codes (Institutional / UB)
    condition_code_type VARCHAR(10),
    condition_code VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);