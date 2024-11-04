#!/bin/bash

# Variables
REMOTE_USER="daq"  # Replace with your Raspberry Pi username
REMOTE_HOST="daq.local"  # Replace with your Raspberry Pi IP or hostname
REMOTE_FOLDER="~/Desktop/test_heater"
PYTHON_SCRIPT="test_heater.py"
VENV_PATH="venv/bin/activate"  # Path to the virtual environment's activate script

# Copy the Python script to the Raspberry Pi
echo "Copying $PYTHON_SCRIPT to $REMOTE_HOST..."
scp $PYTHON_SCRIPT $REMOTE_USER@$REMOTE_HOST:$REMOTE_FOLDER/

# Connect to the Raspberry Pi, create the folder if it doesn't exist, activate the virtual environment, and run the script
ssh $REMOTE_USER@$REMOTE_HOST << EOF
    mkdir -p $REMOTE_FOLDER
    cd $REMOTE_FOLDER
    if [ -f "$VENV_PATH" ]; then
        source $VENV_PATH
        echo "Virtual environment activated."
        python $PYTHON_SCRIPT
    else
        echo "Virtual environment not found. Running the script without venv."
        python3 $PYTHON_SCRIPT
    fi
EOF

echo "Script executed successfully on the Raspberry Pi."
