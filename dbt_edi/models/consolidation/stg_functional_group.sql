with source as (

    select * from {{ source('public', 'functional_group') }}

),

renamed as (

    select
        id,
        functional_id,
        sender_code,
        receiver_code,
        group_date,
        group_time,
        group_control_number,
        responsible_agency_code,
        implementation_version,
        transaction_set_count,
        ge_control_number,
        created_at

    from source

)

select * from renamed