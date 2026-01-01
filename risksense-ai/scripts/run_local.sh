#!/bin/bash
# Script to run RiskSense AI locally

set -e  # Exit on error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="$SCRIPT_DIR/../venv"
MAIN_PY="$SCRIPT_DIR/../src/main.py"

# Activate virtual environment if it exists
if [ -d "$VENV_DIR" ]; then
    source "$VENV_DIR/bin/activate"
    echo "Activated virtual environment."
else
    echo "Warning: Virtual environment not found at $VENV_DIR"
fi

# Set environment variables
export FLASK_ENV=development

# Run the main application
if [ -f "$MAIN_PY" ]; then
    python "$MAIN_PY"
else
    echo "Error: main.py not found at $MAIN_PY"
    exit 1
fi