with source as (

    select * from {{ source('public', 'claim_dates') }}

),

renamed as (

    select
        id,
        claim_number,
        service_date_qualifier,
        service_date_format,
        service_date,
        statement_date_qualifier,
        statement_date_format,
        statement_from_date,
        admission_date_qualifier,
        admission_date_format,
        admission_date,
        discharge_date_qualifier,
        discharge_date_format,
        discharge_date,
        onset_date_qualifier,
        onset_date_format,
        onset_date,
        accident_date_qualifier,
        accident_date_format,
        accident_date,
        last_seen_date_qualifier,
        last_seen_date_format,
        last_seen_date,
        initial_treatment_date_qualifier,
        initial_treatment_date_format,
        initial_treatment_date,
        last_xray_date_qualifier,
        last_xray_date,
        prescription_date_qualifier,
        prescription_date,
        disability_from_date_qualifier,
        disability_from_date,
        last_worked_date_qualifier,
        last_worked_date,
        return_to_work_date_qualifier,
        return_to_work_date,
        created_at

    from source

)

select * from renamed