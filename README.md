# bird-finder-2.0

## Description
`bird-finder-2.0` is a demo of the dlt (data load tool) package to locate birding hotspots relative to a given location. It leverages the eBird API to fetch recent observations of notable birds in the specified location and supports various destinations like DuckDB.

## Requirements
- Python 3.10
- dlt 0.3.12
- duckdb 0.8.0
- python-dotenv 0.20.0
- click 8.1.1
- colorama 0.4.4

## Installation

Use the package manager [poetry](https://python-poetry.org/) to install `bird-finder-2.0`.

```bash
poetry install
```

## Usage

You can run the main script to fetch and load bird observation data as follows:

```bash
python main.py
```

You can specify the location code using the `loc_code` parameter. Please refer to the eBird API documentation for valid location codes.

## Development

To install development dependencies and set up a development environment, use:

```bash
poetry install --dev
```

## Contributions

Feel free to contribute to the project by opening issues or submitting pull requests.

## Authors

- Connor Lough

## Acknowledgements

Special thanks to the eBird API for providing the data.

```

Feel free to add any additional information, guidelines, or documentation that might be relevant to your project. If you have specific instructions or caveats that are not covered here, be sure to include those as well.