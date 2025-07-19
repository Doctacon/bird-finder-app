"""
Pytest configuration and shared fixtures for Bird Finder App tests.
"""

import pytest
from pathlib import Path


@pytest.fixture
def project_root():
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def sample_data_dir(project_root):
    """Return the sample data directory."""
    return project_root / "tests" / "data"


@pytest.fixture
def temp_dir(tmp_path):
    """Return a temporary directory for test files."""
    return tmp_path
