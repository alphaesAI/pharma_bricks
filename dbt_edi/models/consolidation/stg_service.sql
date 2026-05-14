with source as (

    select * from {{ source('public', 'service_line') }}

),

renamed as (

    select
        id,
        claim_number,
        line_number,
        procedure_qualifier,
        procedure_code,
        line_charge_amount,
        unit_measurement_code,
        service_unit_count,
        service_date,
        sv107_107,
        created_at

    from source

)

select * from renamed