import os
from pathlib import Path

from dagster_dbt import DbtCliResource
from dagster import AssetExecutionContext, load_assets_from_modules
from dagster_dbt import DbtCliResource, dbt_assets

dbt_project_dir = Path(__file__).joinpath("..", "..", "..", "..", "transformation").resolve()
dbt = DbtCliResource(project_dir=os.fspath(dbt_project_dir))

# If DAGSTER_DBT_PARSE_PROJECT_ON_LOAD is set, a manifest will be created at run time.
# Otherwise, we expect a manifest to be present in the project's target directory.
if os.getenv("DAGSTER_DBT_PARSE_PROJECT_ON_LOAD"):
    dbt_parse_invocation = dbt.cli(["parse"]).wait()
    dbt_manifest_path = dbt_parse_invocation.target_path.joinpath("manifest.json")
else:
    dbt_manifest_path = dbt_project_dir.joinpath("target", "manifest.json")

@dbt_assets(manifest=dbt_manifest_path)
def transformation_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
