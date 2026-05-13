with source as (
    select * from {{ source('public', 'service_line') }}
),
renamed as (
    select
        id,
        line_number,
        procedure_qualifier,
        procedure_code,
        line_charge_amount,
        unit_measurement_code,
        service_unit_count,
        sv107_107,
        service_date,
        created_at
    from source
)
select * from renamed