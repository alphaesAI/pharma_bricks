with source as (

    select * from {{ source('public', 'payer') }}

),

renamed as (

    select
        payer_id,
        entity_identifier_code,
        entity_type_qualifier,
        payer_name,
        payer_id_qualifier,
        created_at

    from source

)

select * from renamed
