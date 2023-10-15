with final as (
select
load_id as 'load_id',
schema_name as 'schema_name',
status as 'status',
inserted_at as 'inserted_at',
schema_version_hash as 'schema_version_hash'
from {{ source('ebirdapi', '_dlt_loads') }}
)
select * from final