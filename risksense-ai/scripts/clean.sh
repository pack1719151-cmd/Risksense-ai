#!/bin/bash
# Script to clean up build artifacts and temporary files

set -euo pipefail

echo "Cleaning Python cache and build artifacts..."

# Remove Python cache directories
find . -type d -name "__pycache__" -prune -exec rm -rf {} +

# Remove Python bytecode files
find . -type f \( -name "*.pyc" -o -name "*.pyo" -o -name "*~" \) -delete

# Remove build directories and metadata
rm -rf build/ dist/ .pytest_cache .mypy_cache .coverage
rm -rf *.egg-info

echo "Cleanup complete."