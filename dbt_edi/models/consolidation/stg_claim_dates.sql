with source as (

    select * from {{ source('public', 'claim_dates') }}

),

renamed as (

    select
        id,
        service_date,
        created_at

    from source

)

select * from renamed