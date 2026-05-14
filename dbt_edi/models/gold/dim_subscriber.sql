{{ config(materialized='table') }}

SELECT
    subscriber_id,
    MAX(subscriber_first_name) AS first_name,
    MAX(subscriber_last_name) AS last_name,
    MAX(subscriber_middle_name) AS middle_name,
    MAX(birth_date) AS birth_date,
    MAX(gender) AS gender,
    MAX(address_line_1) AS address,
    MAX(city) AS city,
    MAX(state) AS state,
    MAX(zip_code) AS zip_code
FROM {{ ref('stg_subscriber') }}
GROUP BY subscriber_id