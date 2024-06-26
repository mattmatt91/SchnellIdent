#!/bin/bash

# Define variables
BASE_DIR="~/Desktop/daq"
APP_DIR="daq"
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"

# Create and navigate to the application directory
cd $BASE_DIR
mkdir -p $APP_DIR
cd $APP_DIR

# Create a virtual environment and activate it
python3 -m venv $VENV_DIR
source $VENV_DIR/bin/activate

# Install the requirements
pip install -r $REQUIREMENTS_FILE

echo "Virtual environment setup complete in $BASE_DIR/$APP_DIR/$VENV_DIR"
