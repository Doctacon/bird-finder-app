from dagster import AssetExecutionContext, load_assets_from_modules
from dagster_dbt import DbtCliResource, dbt_assets

from .constants import dbt_manifest_path

from . import ebirdapi

ebirdapi_assets = load_assets_from_modules([ebirdapi])

@dbt_assets(manifest=dbt_manifest_path)
def transformation_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()