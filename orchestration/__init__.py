import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from orchestration.assets.dbt import transformation_dbt_assets, dbt_project_dir
from orchestration.assets.ebirdapi.ebirdapi import ebirdapi_pipelines

defs = Definitions(
    assets=[transformation_dbt_assets, ebirdapi_pipelines],
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)