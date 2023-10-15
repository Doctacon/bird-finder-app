with final as (
select
value as 'value',
_dlt_id as '_dlt_id',
_dlt_parent_id as '_dlt_parent_id',
_dlt_list_idx as '_dlt_list_idx'
from {{ source('ebirdapi', 'taxonomy__com_name_codes') }}
)
select * from final