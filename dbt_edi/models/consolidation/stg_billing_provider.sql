with source as (

    select * from {{ source('public', 'billing_provider') }}

),

renamed as (

    select
        billing_provider_id,
        entity_identifier_code,
        entity_type_qualifier,
        billing_provider_name,
        billing_provider_id_qualifier,
        address_line_1,
        address_line_2,
        city,
        state,
        zip_code,
        tax_id,
        hierarchical_id,
        hierarchical_level_code,
        hierarchical_child_code,
        created_at

    from source

)

select * from renamed