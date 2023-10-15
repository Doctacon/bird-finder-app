with final as (
select
load_id as 'load_id',
package_path as 'package_path',
state as 'state',
schema_name as 'schema_name',
completed_at as 'completed_at',
_dlt_parent_id as '_dlt_parent_id',
_dlt_list_idx as '_dlt_list_idx',
_dlt_id as '_dlt_id'
from {{ source('ebirdapi', '_load_info__load_packages') }}
)
select * from final