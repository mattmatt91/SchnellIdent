#!/bin/bash

# Define the base directory and virtual environment directory
BASE_DIR=$(pwd)
VENV_DIR="venv"

# Create the virtual environment
python3 -m venv $VENV_DIR

# Activate the virtual environment and install requirements
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

# Install the requirements
pip install -r requirements.txt

echo "Virtual environment setup complete in $BASE_DIR/$VENV_DIR"
