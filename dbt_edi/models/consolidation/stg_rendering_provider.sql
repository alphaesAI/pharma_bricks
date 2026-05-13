with source as (
    select * from {{ source('public', 'rendering_provider') }}
),
renamed as (
    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        rendering_provider_last_name,
        rendering_provider_first_name,
        rendering_provider_middle_name,
        rendering_provider_id_qualifier,
        rendering_provider_id,
        created_at
    from source
)
select * from renamed