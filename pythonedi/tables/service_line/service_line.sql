CREATE TABLE IF NOT EXISTS service_line (

    id SERIAL PRIMARY KEY,

    line_number VARCHAR(20),
    procedure_qualifier VARCHAR(20),
    procedure_code VARCHAR(50),

    line_charge_amount DECIMAL(18, 2),
    unit_measurement_code VARCHAR(20),
    service_unit_count INTEGER,

    sv107_107 VARCHAR(50),
    service_date VARCHAR(20),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
