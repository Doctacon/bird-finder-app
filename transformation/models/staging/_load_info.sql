with final as (
    select
        pipeline__pipeline_name as 'pipeline__pipeline_name',
        destination_name as 'destination_name',
        destination_displayable_credentials as 'destination_displayable_credentials',
        destination_fingerprint as 'destination_fingerprint',
        dataset_name as 'dataset_name',
        started_at as 'started_at',
        first_run as 'first_run',
        _dlt_load_id as '_dlt_load_id',
        _dlt_id as '_dlt_id'
    from {{ source('ebirdapi', '_load_info') }}
)
select * from final