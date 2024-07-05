#!/bin/bash

# Define the base directory and virtual environment directory
BASE_DIR=$(pwd)
VENV_DIR="venv"

# Activate the virtual environment
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # For Linux and macOS
    source $VENV_DIR/bin/activate
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # For Windows
    source $VENV_DIR/Scripts/activate
else
    echo "Unsupported OS: $OSTYPE"
    exit 1
fi

# Launch the FastAPI application
python test_api.py