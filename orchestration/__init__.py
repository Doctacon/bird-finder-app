import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets.dbt import transformation_dbt_assets, dbt_project_dir
from .assets.ebirdapi.ebirdapi import dagster_ebirdapi_assets, dlt_resource

defs = Definitions(
    assets=[transformation_dbt_assets, dagster_ebirdapi_assets],
    resources={
        "dlt": dlt_resource,
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)