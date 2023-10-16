with final as (
    select
        sci_name as 'sci_name',
        com_name as 'com_name',
        species_code as 'species_code',
        category as 'category',
        taxon_order as 'taxon_order',
        order as 'order',
        family_code as 'family_code',
        family_com_name as 'family_com_name',
        family_sci_name as 'family_sci_name',
        _dlt_load_id as '_dlt_load_id',
        _dlt_id as '_dlt_id',
        report_as as 'report_as',
        extinct as 'extinct',
        extinct_year as 'extinct_year'
    from {{ source('ebirdapi', 'taxonomy') }}
)
select * from final