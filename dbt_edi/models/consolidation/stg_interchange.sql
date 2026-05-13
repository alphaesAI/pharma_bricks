with source as (
    select * from {{ source('public', 'interchange') }}
),
renamed as (
    select
        id,
        sender_id,
        sender_qualifier,
        receiver_id,
        receiver_qualifier,
        interchange_date,
        interchange_time,
        control_number,
        version,
        test_indicator,
        created_at
    from source
)
select * from renamed