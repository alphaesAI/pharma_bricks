{{ config(materialized='table') }}

SELECT
    billing_provider_id AS provider_id,
    MAX(billing_provider_name) AS provider_name,
    MAX(tax_id) AS tax_id,
    MAX(address_line_1) AS address_line_1,
    MAX(city) AS city,
    MAX(state) AS state,
    MAX(zip_code) AS zip_code
FROM {{ ref('stg_billing_provider') }}
GROUP BY billing_provider_id