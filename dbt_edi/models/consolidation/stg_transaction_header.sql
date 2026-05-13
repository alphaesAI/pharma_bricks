with source as (
    select * from {{ source('public', 'transaction_header') }}
),
renamed as (
    select
        id,
        transaction_set_identifier,
        transaction_control_number,
        implementation_reference,
        hierarchical_structure_code,
        transaction_purpose_code,
        batch_id,
        transaction_creation_date,
        transaction_creation_time,
        created_at
    from source
)
select * from renamed