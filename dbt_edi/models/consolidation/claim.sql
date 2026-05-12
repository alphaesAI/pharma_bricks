with source as (
    select * from {{ source('public', 'claim') }}
),
renamed as (
    select
        id as claim_id,
        claim_number,
        total_charge_amount,
        facility_code,
        place_of_service,
        frequency_code,
        claim_type_code,
        provider_signature_indicator,
        assignment_participation_code,
        assignment_certification_indicator,
        release_of_information_code,
        created_at
    from source
)

select * from renamed