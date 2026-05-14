with source as (

    select * from {{ source('public', 'subscriber') }}

),

renamed as (

    select
        subscriber_id,
        entity_identifier_code,
        entity_type_qualifier,
        subscriber_last_name,
        subscriber_first_name,
        subscriber_middle_name,
        subscriber_id_qualifier,
        birth_date,
        gender,
        address_line_1,
        city,
        state,
        zip_code,
        payer_responsibility_code,
        relationship_code,
        claim_filing_indicator,
        hierarchical_id,
        parent_hierarchical_id,
        hierarchical_level_code,
        hierarchical_child_code,
        created_at,
        date_time_period_format_qualifier

    from source

)

select * from renamed