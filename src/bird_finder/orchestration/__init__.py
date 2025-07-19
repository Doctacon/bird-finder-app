import os

from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    DefaultScheduleStatus,
)
from dagster_dbt import DbtCliResource

from .assets.dbt import transformation_dbt_assets, dbt_project_dir
from .assets.ebirdapi.ebirdapi import dagster_ebirdapi_assets, dlt_resource

# Addition: define a job that will materialize the assets
ebird_job = define_asset_job("ebird_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
ebird_schedule = ScheduleDefinition(
    job=ebird_job,
    cron_schedule="0 0 * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

defs = Definitions(
    assets=[transformation_dbt_assets, dagster_ebirdapi_assets],
    resources={
        "dlt": dlt_resource,
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
    jobs=[ebird_job],
    schedules=[ebird_schedule],
)
