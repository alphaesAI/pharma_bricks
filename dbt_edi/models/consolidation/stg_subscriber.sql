with source as (

    select * from {{ source('public', 'subscriber') }}

),

renamed as (

    select
        id,
        entity_identifier_code,
        entity_type_qualifier,
        subscriber_last_name,
        subscriber_first_name,
        subscriber_middle_name,
        subscriber_name_prefix,
        subscriber_name_suffix,
        subscriber_id_qualifier,
        subscriber_id,
        address_line_1,
        address_line_2,
        city,
        state,
        zip_code,
        country_code,
        location_qualifier,
        location_identifier,
        country_subdivision_code,
        date_time_period_format_qualifier,
        birth_date,
        gender_code,
        marital_status_code,
        race_or_ethnicity_code,
        citizenship_status_code,
        country_code_dmg,
        ssn_qualifier,
        ssn,
        hierarchical_id,
        parent_hierarchical_id,
        hierarchical_level_code,
        hierarchical_child_code,
        payer_responsibility_code,
        individual_relationship_code,
        insured_group_or_policy_number,
        insured_group_name,
        insurance_type_code,
        coordination_of_benefits_code,
        yes_no_condition_code,
        employment_status_code,
        claim_filing_indicator,
        created_at

    from source

)

select * from renamed