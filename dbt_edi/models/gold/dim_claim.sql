WITH claim_base AS (

    SELECT

        claim_number,

        subscriber_id,
        billing_provider_id,
        payer_id,

        total_charge_amount,

        facility_code,
        place_of_service,
        frequency_code,
        claim_type_code,

        provider_signature_indicator,
        assignment_participation_code,
        assignment_certification_indicator,
        release_of_information_code,

        created_at

    FROM {{ source('edi_source', 'claim') }}

),

diagnosis_data AS (

    SELECT

        claim_number,

        diagnosis_type,
        diagnosis_code

    FROM {{ source('edi_source', 'diagnosis') }}

),

service_data AS (

    SELECT

        claim_number,

        line_number,

        procedure_qualifier,
        procedure_code,

        line_charge_amount,

        unit_measurement_code,
        service_unit_count,

        service_date,

        sv107_107

    FROM {{ source('edi_source', 'service_line') }}

),

claim_dates_data AS (

    SELECT

        claim_number,

        service_date AS claim_service_date

    FROM {{ source('edi_source', 'claim_dates') }}

),

rendering_provider_data AS (

    SELECT

        claim_number,

        rendering_provider_id,

        rendering_provider_last_name,
        rendering_provider_first_name,
        rendering_provider_middle_name

    FROM {{ source('edi_source', 'rendering_provider') }}

)

SELECT

    cb.claim_number,

    cb.subscriber_id,
    cb.billing_provider_id,
    cb.payer_id,

    cb.total_charge_amount,

    cb.facility_code,
    cb.place_of_service,
    cb.frequency_code,
    cb.claim_type_code,

    cb.provider_signature_indicator,
    cb.assignment_participation_code,
    cb.assignment_certification_indicator,
    cb.release_of_information_code,

    dd.diagnosis_type,
    dd.diagnosis_code,

    sd.line_number,
    sd.procedure_qualifier,
    sd.procedure_code,
    sd.line_charge_amount,
    sd.unit_measurement_code,
    sd.service_unit_count,
    sd.service_date,
    sd.sv107_107,

    cdd.claim_service_date,

    rpd.rendering_provider_id,
    rpd.rendering_provider_last_name,
    rpd.rendering_provider_first_name,
    rpd.rendering_provider_middle_name,

    cb.created_at

FROM claim_base cb

LEFT JOIN diagnosis_data dd
    ON cb.claim_number = dd.claim_number

LEFT JOIN service_data sd
    ON cb.claim_number = sd.claim_number

LEFT JOIN claim_dates_data cdd
    ON cb.claim_number = cdd.claim_number

LEFT JOIN rendering_provider_data rpd
    ON cb.claim_number = rpd.claim_number