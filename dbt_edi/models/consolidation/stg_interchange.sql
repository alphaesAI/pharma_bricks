with source as (

    select * from {{ source('public', 'interchange') }}

),

renamed as (

    select
        id,
        sender_qualifier,
        sender_id,
        receiver_qualifier,
        receiver_id,
        interchange_date,
        interchange_time,
        repetition_separator,
        control_version_number,
        control_number,
        acknowledgment_requested,
        test_indicator,
        component_element_separator,
        functional_group_count,
        iea_control_number,
        created_at

    from source

)

select * from renamed