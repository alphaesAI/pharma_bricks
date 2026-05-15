CREATE TABLE IF NOT EXISTS service_line (

    id SERIAL PRIMARY KEY,

    claim_number VARCHAR(100),

    -- LX – Line Counter
    line_number VARCHAR(20),

    -- SV1 – Professional Service
    procedure_qualifier VARCHAR(20),
    procedure_code VARCHAR(50),
    modifier_1 VARCHAR(10),
    modifier_2 VARCHAR(10),
    modifier_3 VARCHAR(10),
    modifier_4 VARCHAR(10),
    procedure_description VARCHAR(255),

    line_charge_amount DECIMAL(18, 2),
    unit_measurement_code VARCHAR(20),
    service_unit_count INTEGER,
    place_of_service_code VARCHAR(10),
    service_type_code VARCHAR(10),

    -- Diagnosis Code Pointers
    diagnosis_code_pointer_1 VARCHAR(10),
    diagnosis_code_pointer_2 VARCHAR(10),
    diagnosis_code_pointer_3 VARCHAR(10),
    diagnosis_code_pointer_4 VARCHAR(10),

    -- SV1 Indicators
    emergency_indicator VARCHAR(5),
    multiple_procedure_code VARCHAR(5),
    epsdt_indicator VARCHAR(5),
    family_planning_indicator VARCHAR(5),
    review_code VARCHAR(10),
    national_or_local_assigned_review_value VARCHAR(10),
    copay_status_code VARCHAR(5),
    health_care_professional_shortage_area_code VARCHAR(10),
    reference_identification VARCHAR(100),
    postal_code VARCHAR(20),

    -- SV2 – Institutional Service Line
    revenue_code VARCHAR(10),
    sv2_procedure_qualifier VARCHAR(20),
    sv2_procedure_code VARCHAR(50),
    sv2_modifier_1 VARCHAR(10),
    sv2_line_charge_amount DECIMAL(18, 2),
    sv2_unit_measurement_code VARCHAR(20),
    sv2_service_unit_count INTEGER,
    sv2_non_covered_charge_amount DECIMAL(18, 2),
    sv2_blood_deductible_pints VARCHAR(10),
    sv2_measurement_code VARCHAR(10),

    -- SV3 – Dental Service
    sv3_procedure_qualifier VARCHAR(20),
    sv3_procedure_code VARCHAR(50),
    sv3_line_charge_amount DECIMAL(18, 2),
    sv3_facility_code_qualifier VARCHAR(10),
    sv3_facility_code VARCHAR(20),
    sv3_oral_cavity_designation_1 VARCHAR(10),
    sv3_oral_cavity_designation_2 VARCHAR(10),
    sv3_oral_cavity_designation_3 VARCHAR(10),
    sv3_oral_cavity_designation_4 VARCHAR(10),
    sv3_oral_cavity_designation_5 VARCHAR(10),
    sv3_prosthesis_crown_onlay_code VARCHAR(10),
    sv3_tooth_number VARCHAR(10),
    sv3_tooth_surface_code_1 VARCHAR(10),
    sv3_tooth_surface_code_2 VARCHAR(10),
    sv3_tooth_surface_code_3 VARCHAR(10),
    sv3_tooth_surface_code_4 VARCHAR(10),
    sv3_tooth_surface_code_5 VARCHAR(10),

    -- DTP – Service Line Dates
    service_date_qualifier VARCHAR(10),
    service_date_format VARCHAR(10),
    service_date VARCHAR(25),

    -- REF – Line-level Reference Numbers
    line_ref_qualifier_1 VARCHAR(10),
    line_ref_id_1 VARCHAR(100),
    prior_auth_qualifier VARCHAR(10),
    prior_auth_number VARCHAR(100),
    line_item_control_number_qualifier VARCHAR(10),
    line_item_control_number VARCHAR(100),
    repriced_line_ref_qualifier VARCHAR(10),
    repriced_line_ref_id VARCHAR(100),
    mammography_certification_qualifier VARCHAR(10),
    mammography_certification_number VARCHAR(100),
    clia_ref_qualifier VARCHAR(10),
    clia_ref_number VARCHAR(100),

    -- NTE – Line Notes
    line_note_reference_code VARCHAR(10),
    line_note_text TEXT,

    -- HCP – Line Pricing/Repricing
    line_pricing_methodology VARCHAR(10),
    line_repriced_allowed_amount DECIMAL(18, 2),
    line_repriced_saving_amount DECIMAL(18, 2),
    line_repriced_org_id VARCHAR(50),
    line_reject_reason_code VARCHAR(10),
    line_policy_compliance_code VARCHAR(10),
    line_exception_code VARCHAR(10),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_service_line_claim
        FOREIGN KEY (claim_number)
        REFERENCES claim(claim_number)
);