#!/usr/bin/env python3
"""
Basic usage example for Bird Finder App.

This example demonstrates how to:
1. Import the main modules
2. Run basic data operations
3. Work with the data pipeline
"""

import sys
from pathlib import Path

# Add the source directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

try:
    from bird_finder import __version__, orchestration, scripts, utils
    
    def main():
        """Main example function."""
        print(f"Bird Finder App v{__version__}")
        print("=" * 40)
        
        print("\n📦 Available modules:")
        print(f"  - Orchestration: {orchestration}")
        print(f"  - Scripts: {scripts}")
        print(f"  - Utils: {utils}")
        
        print("\n🚀 To run the data pipeline:")
        print("  1. Run: uv run python -m bird_finder.orchestration.assets.ebirdapi")
        print("  2. Generate staging: uv run gen-staging <schema-file>")
        print("  3. Transform data: cd src/bird_finder/transformation && uv run dbt run")
        
        print("\n📖 For more information, see the README.md")

    if __name__ == "__main__":
        main()

except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure to install the package first: uv sync")
    sys.exit(1) 