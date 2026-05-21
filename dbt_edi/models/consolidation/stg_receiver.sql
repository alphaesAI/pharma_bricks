with source as (

    select * from {{ source('public', 'receiver') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        receiver_last_name,
        receiver_first_name,
        receiver_middle_name,
        receiver_prefix,
        receiver_suffix,
        receiver_id_qualifier,
        receiver_id,
        created_at

    from source

)

select * from renamed