#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
BASE_DIR="$HOME/Desktop/daq"
APP_DIR="daq"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Create and navigate to the application directory
mkdir -p "$BASE_DIR/$APP_DIR"
cd "$BASE_DIR/$APP_DIR"

# Create a virtual environment and activate it
python3 -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# Check if requirements.txt exists before installing
if [ -f "$REQUIREMENTS_FILE" ]; then
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Error: $REQUIREMENTS_FILE not found."
    exit 1
fi

echo "Virtual environment setup complete in $BASE_DIR/$APP_DIR/$VENV_DIR"
