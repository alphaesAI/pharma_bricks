{{ config(materialized='table') }}

SELECT

    -- Degenerate dimension
    claim_number AS fact_claim_id,

    -- Foreign keys to dimensions
    subscriber_id,
    billing_provider_id,
    payer_id,

    -- Measures
    total_charge_amount,
    line_charge_amount,
    service_unit_count,

    -- Dates
    service_date,
    claim_service_date,
    created_at

FROM {{ ref('dim_claim') }}