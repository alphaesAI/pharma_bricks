{{ config(materialized='table') }}

SELECT
    id AS receiver_id,
    MAX(receiver_name) AS receiver_name,
    MAX(entity_identifier_code) AS entity_identifier_code
FROM {{ ref('stg_receiver') }}
GROUP BY id, receiver_id