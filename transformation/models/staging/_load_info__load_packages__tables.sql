with final as (
    select
        write_disposition as 'write_disposition',
        "name" as 'name',
        resource as 'resource',
        schema_name as 'schema_name',
        load_id as 'load_id',
        _dlt_parent_id as '_dlt_parent_id',
        _dlt_list_idx as '_dlt_list_idx',
        _dlt_id as '_dlt_id',
        parent as 'parent',
        description as 'description'
    from {{ source('ebirdapi', '_load_info__load_packages__tables') }}
)
select * from final