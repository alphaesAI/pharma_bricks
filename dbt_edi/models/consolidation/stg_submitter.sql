with source as (

    select * from {{ source('public', 'submitter') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        submitter_name,
        submitter_id_qualifier,
        submitter_id,
        contact_function_code,
        contact_name,
        communication_number_qualifier,
        communication_number,
        created_at

    from source

)

select * from renamed