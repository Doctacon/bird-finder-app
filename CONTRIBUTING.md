# Contributing to Bird Finder App

Thank you for your interest in contributing to Bird Finder App! We welcome contributions from the community.

## Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/bird-finder-app.git
   cd bird-finder-app
   ```

2. **Install UV (if not already installed):**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **Install dependencies:**
   ```bash
   uv sync --dev
   ```

4. **Install pre-commit hooks:**
   ```bash
   uv run pre-commit install
   ```

## Development Workflow

1. **Create a new branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes and ensure they pass all checks:**
   ```bash
   # Run tests
   uv run pytest
   
   # Run linting
   uv run black .
   uv run isort .
   uv run flake8
   uv run mypy
   ```

3. **Commit your changes:**
   ```bash
   git add .
   git commit -m "Add your descriptive commit message"
   ```

4. **Push your branch and create a pull request**

## Code Style

- We use [Black](https://black.readthedocs.io/) for code formatting
- We use [isort](https://pycqa.github.io/isort/) for import sorting
- We use [flake8](https://flake8.pycqa.org/) for linting
- We use [mypy](http://mypy-lang.org/) for type checking

## Testing

- Write tests for new functionality
- Ensure all tests pass before submitting a pull request
- Aim for good test coverage

## Documentation

- Update documentation for any new features
- Use clear and descriptive docstrings
- Update the README if necessary

## Questions?

Feel free to open an issue if you have any questions about contributing! 