with source as (

    select * from {{ source('public', 'diagnosis') }}

),

renamed as (

    select
        id,
        claim_number,
        principal_diagnosis_type,
        principal_diagnosis_code,
        principal_diagnosis_date,
        additional_diagnosis_type_2,
        additional_diagnosis_code_2,
        additional_diagnosis_type_3,
        additional_diagnosis_code_3,
        additional_diagnosis_type_4,
        additional_diagnosis_code_4,
        additional_diagnosis_type_5,
        additional_diagnosis_code_5,
        additional_diagnosis_type_6,
        additional_diagnosis_code_6,
        additional_diagnosis_type_7,
        additional_diagnosis_code_7,
        additional_diagnosis_type_8,
        additional_diagnosis_code_8,
        additional_diagnosis_type_9,
        additional_diagnosis_code_9,
        additional_diagnosis_type_10,
        additional_diagnosis_code_10,
        additional_diagnosis_type_11,
        additional_diagnosis_code_11,
        additional_diagnosis_type_12,
        additional_diagnosis_code_12,
        reason_for_visit_type,
        reason_for_visit_code,
        external_cause_type,
        external_cause_code,
        principal_procedure_type,
        principal_procedure_code,
        principal_procedure_date,
        other_procedure_type_2,
        other_procedure_code_2,
        other_procedure_date_2,
        occurrence_code_type,
        occurrence_code,
        occurrence_date,
        value_code_type,
        value_code,
        value_amount,
        condition_code_type,
        condition_code,
        created_at

    from source

)

select * from renamed