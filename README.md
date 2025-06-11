# bird-finder-2.0

## Description
`bird-finder-2.0` is a demo of the dlt (data load tool) package to locate birding hotspots relative to a given location. It leverages the eBird API to fetch recent observations of notable birds in the specified location and supports various destinations like DuckDB.

> **Note**: This project has been migrated from Poetry to UV for faster package management and dependency resolution.

## Requirements
- Python 3.12+
- UV package manager

## Installation

Use the package manager [UV](https://docs.astral.sh/uv/) to install `bird-finder-2.0`.

```bash
# Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

## Usage

1. Use `uv run` to execute commands in the project environment
2. Ingest data from ebirdapi `~/orchestration/assets/ebirdapi$ uv run python ebirdapi.py `
3. Create staging layer files `~/$ uv run gen-staging {file-path-to-ebirdapi_source.schema.yaml}`
4. Materialize staging layer `~/transformation$ uv run dbt run`
5. Update staging layer docs `~/transformations$ uv run dbt-osmosis yaml refactor --fqn staging`

You can specify the location code using the `loc_code` parameter. Please refer to the eBird API documentation for valid location codes.

## Development

To install development dependencies and set up a development environment, use:

```bash
uv sync --dev
```

## Contributions

Feel free to contribute to the project by opening issues or submitting pull requests.

## Authors

- Connor Lough

## Roadmap

1. Containerize assets and orchestrator

## Acknowledgements

Special thanks to the eBird API for providing the data.

```

Feel free to add any additional information, guidelines, or documentation that might be relevant to your project. If you have specific instructions or caveats that are not covered here, be sure to include those as well.