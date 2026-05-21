with source as (

    select * from {{ source('public', 'claim') }}

),

renamed as (

    select
        claim_number,
        subscriber_id,
        billing_provider_id,
        payer_id,
        rendering_provider_npi,
        total_charge_amount,
        facility_code,
        place_of_service,
        frequency_code,
        claim_type_code,
        provider_signature_indicator,
        assignment_participation_code,
        assignment_certification_indicator,
        release_of_information_code,
        patient_signature_source_code,
        related_causes_code_1,
        related_causes_code_2,
        related_causes_code_3,
        auto_accident_state,
        special_program_code,
        yes_no_condition_code_1,
        yes_no_condition_code_2,
        provider_agreement_code,
        claim_status_code,
        yes_no_condition_code_3,
        claim_submission_reason_code,
        delay_reason_code,
        transaction_control_number,
        created_at

    from source

)

select * from renamed