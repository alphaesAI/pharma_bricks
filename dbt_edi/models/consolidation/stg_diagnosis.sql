with source as (
    select * from {{ source('public', 'diagnosis') }}
),
renamed as (
    select
        id as diagnosis_id,
        diagnosis_type,
        diagnosis_code,
        created_at
    from source
)
select * from renamed