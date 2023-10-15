with final as (
select
code as 'code',
name as 'name',
last_update as 'last_update',
_dlt_load_id as '_dlt_load_id',
_dlt_id as '_dlt_id'
from {{ source('ebirdapi', 'taxa_local_codes') }}
)
select * from final