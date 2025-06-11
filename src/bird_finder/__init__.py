"""
Bird Finder App - A comprehensive bird finding application using eBird API data.

This package provides tools for:
- Ingesting bird observation data from the eBird API using DLT
- Orchestrating data pipelines with Dagster
- Transforming data with DBT
- Analyzing bird observation patterns and hotspots
"""

__version__ = "0.1.0"
__email__ = "flocka_birdz@pm.me"

# Import main modules for easy access
from bird_finder import orchestration, scripts, utils

__all__ = ["orchestration", "scripts", "utils", "__version__"] 