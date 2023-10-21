with final as (
    select
        write_disposition as 'write_disposition',
        "name" as 'name',
        resource as 'resource',
        schema_name as 'schema_name',
        load_id as 'load_id',
        _dlt_load_id as '_dlt_load_id',
        _dlt_id as '_dlt_id',
        parent as 'parent',
        description as 'description'
    from {{ source('ebirdapi', '_new_tables') }}
)
select * from final