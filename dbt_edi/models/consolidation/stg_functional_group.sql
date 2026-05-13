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
        implementation_version,
        created_at
    from source
)
select * from renamed