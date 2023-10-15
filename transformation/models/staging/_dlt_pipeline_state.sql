with final as (
select
version as 'version',
engine_version as 'engine_version',
pipeline_name as 'pipeline_name',
state as 'state',
created_at as 'created_at',
_dlt_load_id as '_dlt_load_id',
_dlt_id as '_dlt_id'
from {{ source('ebirdapi', '_dlt_pipeline_state') }}
)
select * from final