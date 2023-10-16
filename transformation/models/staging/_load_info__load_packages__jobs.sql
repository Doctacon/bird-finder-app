with final as (
    select
        state as 'state',
        file_path as 'file_path',
        file_size as 'file_size',
        created_at as 'created_at',
        elapsed as 'elapsed',
        table_name as 'table_name',
        file_id as 'file_id',
        retry_count as 'retry_count',
        file_format as 'file_format',
        _dlt_parent_id as '_dlt_parent_id',
        _dlt_list_idx as '_dlt_list_idx',
        _dlt_id as '_dlt_id'
    from {{ source('ebirdapi', '_load_info__load_packages__jobs') }}
)
select * from final