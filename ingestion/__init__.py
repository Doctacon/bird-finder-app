from dagster import Definitions, load_assets_from_modules

from . import ebirdapi

all_assets = load_assets_from_modules([ebirdapi])

defs = Definitions(
    assets=all_assets,
)