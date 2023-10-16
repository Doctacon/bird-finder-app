with final as (
    select
        authority_ver as 'authority_ver',
        latest as 'latest',
        _dlt_load_id as '_dlt_load_id',
        _dlt_id as '_dlt_id'
    from {{ source('ebirdapi', 'taxonomy_versions') }}
)
select * from final