with source as (

    select * from {{ source('public', 'claim_dates') }}

),

renamed as (

    select
        id,
        claim_number,
        service_date,
        created_at

    from source

)

select * from renamed