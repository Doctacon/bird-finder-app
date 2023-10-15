with final as (
select
name as 'name',
write_disposition as 'write_disposition',
resource as 'resource',
schema_name as 'schema_name',
load_id as 'load_id',
_dlt_load_id as '_dlt_load_id',
_dlt_id as '_dlt_id',
description as 'description',
parent as 'parent'
from {{ source('ebirdapi', '_new_tables') }}
)
select * from final