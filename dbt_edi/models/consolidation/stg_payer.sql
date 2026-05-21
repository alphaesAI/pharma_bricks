with source as (

    select * from {{ source('public', 'payer') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        payer_name,
        payer_first_name,
        payer_middle_name,
        payer_prefix,
        payer_suffix,
        payer_id_qualifier,
        payer_id,
        address_line_1,
        address_line_2,
        city,
        state,
        zip_code,
        payer_ref_qualifier_1,
        payer_ref_id_1,
        payer_ref_qualifier_2,
        payer_ref_id_2,
        created_at

    from source

)

select * from renamed