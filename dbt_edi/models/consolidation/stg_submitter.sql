with source as (

    select * from {{ source('public', 'submitter') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        submitter_last_name,
        submitter_first_name,
        submitter_middle_name,
        submitter_prefix,
        submitter_suffix,
        submitter_id_qualifier,
        submitter_id,
        contact_function_code,
        contact_name,
        communication_number_qualifier_1,
        communication_number_1,
        communication_number_qualifier_2,
        communication_number_2,
        communication_number_qualifier_3,
        communication_number_3,
        created_at

    from source

)

select * from renamed