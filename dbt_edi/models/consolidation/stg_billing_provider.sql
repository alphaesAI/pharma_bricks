with source as (

    select * from {{ source('public', 'billing_provider') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        billing_provider_last_name,
        billing_provider_first_name,
        billing_provider_middle_name,
        billing_provider_prefix,
        billing_provider_suffix,
        billing_provider_id_qualifier,
        billing_provider_npi,
        address_line_1,
        address_line_2,
        city,
        state,
        zip_code,
        country_code,
        location_qualifier,
        location_identifier,
        country_subdivision_code,
        tax_id_qualifier,
        tax_id,
        upin_qualifier,
        upin,
        clia_qualifier,
        clia_number,
        contact_function_code,
        contact_name,
        contact_comm_qualifier_1,
        contact_comm_number_1,
        contact_comm_qualifier_2,
        contact_comm_number_2,
        hierarchical_id,
        parent_hierarchical_id,
        hierarchical_level_code,
        hierarchical_child_code,
        prv_provider_code,
        prv_reference_id_qualifier,
        prv_provider_taxonomy_code,
        cur_entity_identifier_code,
        cur_currency_code,
        created_at

    from source

)

select * from renamed