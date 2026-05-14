{{ config(materialized='table') }}

SELECT
    payer_id,
    MAX(payer_name) AS payer_name,
    MAX(entity_identifier_code) AS entity_identifier_code,
    MAX(entity_type_qualifier) AS entity_type_qualifier,
    MAX(payer_id_qualifier) AS payer_id_qualifier
FROM {{ ref('stg_payer') }}
GROUP BY payer_id