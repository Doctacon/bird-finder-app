with dlt_loads as (
    select * from {{ ref('_dlt_loads') }}
),
load_info as (
    select * from {{ ref('_load_info') }}
),
final as (
    select
        dlt_loads.*
    from dlt_loads
    join load_info
        on dlt_loads.load_id = load_info._dlt_load_id
)
select * from final