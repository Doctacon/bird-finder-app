# Bird Finder App

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive bird finding application that leverages the eBird API to locate birding hotspots and analyze bird observation patterns. Built with modern data engineering tools including DLT, DBT, and Dagster.

## 🚀 Features

- **Data Ingestion**: Automated data collection from eBird API using DLT (Data Load Tool)
- **Data Orchestration**: Pipeline management and scheduling with Dagster
- **Data Transformation**: Analytics-ready data models using DBT
- **Database Support**: Fast analytics with DuckDB
- **Modern Tooling**: Built with UV for fast dependency management

## 📁 Project Structure

```
bird-finder-app/
├── src/bird_finder/          # Main Python package
│   ├── orchestration/        # Dagster pipeline definitions
│   ├── transformation/       # DBT transformations
│   ├── scripts/              # Utility scripts
│   └── utils/                # Common utilities
├── tests/                    # Test suite
├── docs/                     # Documentation
├── examples/                 # Usage examples
├── schemas/                  # Data schemas
├── pyproject.toml           # Project configuration
├── LICENSE                  # MIT License
└── README.md               # This file
```

## 🛠 Installation

### Prerequisites

- Python 3.12+
- [UV package manager](https://docs.astral.sh/uv/)

### Quick Start

1. **Install UV** (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone and install**:
   ```bash
   git clone https://github.com/doctacon/bird-finder-app.git
   cd bird-finder-app
   uv sync
   ```

3. **Install development dependencies**:
   ```bash
   uv sync --dev
   ```

## 📖 Usage

### Data Pipeline

1. **Ingest eBird data**:
   ```bash
   uv run python -m bird_finder.orchestration.assets.ebirdapi
   ```

2. **Generate staging layer**:
   ```bash
   uv run gen-staging schemas/export/ebirdapi_source.schema.yaml
   ```

3. **Run DBT transformations**:
   ```bash
   cd src/bird_finder/transformation
   uv run dbt run
   ```

4. **Update documentation**:
   ```bash
   cd src/bird_finder/transformation
   uv run dbt-osmosis yaml refactor --fqn staging
   ```

### Configuration

The application supports configuration through environment variables and the eBird API. 
Refer to the eBird API documentation for valid location codes.

## 🧪 Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=bird_finder --cov-report=html
```

### Code Quality

```bash
# Format code
uv run black .
uv run isort .

# Lint code
uv run flake8
uv run mypy
```

### Pre-commit Hooks

```bash
# Install pre-commit hooks
uv run pre-commit install

# Run hooks manually
uv run pre-commit run --all-files
```

## 🗂 Data Sources

- **eBird API**: Real-time bird observation data
- **Location Codes**: Configurable geographic regions for data collection

## 🚧 Roadmap

- [ ] Containerize application components
- [ ] Implement incremental data streaming
- [ ] Add more data sources beyond eBird
- [ ] Machine learning models for bird prediction

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [eBird](https://ebird.org/) for providing comprehensive bird observation data
- [DLT](https://dlthub.com/) for modern data loading capabilities
- [Dagster](https://dagster.io/) for data orchestration
- [DBT](https://www.getdbt.com/) for data transformation framework

## 📧 Contact

flocka_birdz@pm.me

Project Link: [https://github.com/doctacon/bird-finder-app](https://github.com/doctacon/bird-finder-app)
