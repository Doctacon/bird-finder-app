with final as (
select
version as 'version',
engine_version as 'engine_version',
inserted_at as 'inserted_at',
schema_name as 'schema_name',
version_hash as 'version_hash',
schema as 'schema'
from {{ source('ebirdapi', '_dlt_version') }}
)
select * from final