#!/bin/bash

# SSH details
SSH_USER="daq"
SSH_SERVER="daq.local"
DEST_DIR="/home/${SSH_USER}/Desktop"

# Folders to copy
FOLDER1="daq"

# Function to check and create destination directory
check_and_create_dest_dir() {
    ssh ${SSH_USER}@${SSH_SERVER} "mkdir -p ${DEST_DIR}"
    if [ $? -eq 0 ]; then
        echo "Destination directory ${DEST_DIR} verified/created."
    else
        echo "Failed to verify/create destination directory ${DEST_DIR}."
        exit 1
    fi
}

# Function to copy folder
copy_folder() {
    local folder=$1
    echo "Starting to copy folder: $folder"
    rsync -av --exclude 'node_modules' --exclude 'venv' "$folder" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
    if [ $? -eq 0 ]; then
        echo "Successfully copied $folder to ${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
    else
        echo "Failed to copy $folder"
    fi
}

# Check and create destination directory if necessary
check_and_create_dest_dir

# Call the function to copy the folder
copy_folder "$FOLDER1"

# ssh ${SSH_USER}@${SSH_SERVER}  "cd $DEST_DIR; source testdaq/venv/bin/activate; cd daq; uvicorn main:app --host 0.0.0.0 --port 8200 --reload"
# ssh ${SSH_USER}@${SSH_SERVER}  "cd $DEST_DIR; source testdaq/venv/bin/activate; cd daq; uvicorn main:app --host 0.0.0.0 --port 8500 --reload"





# Function to kill any running uvicorn server
stop_uvicorn_server() {
    ssh ${SSH_USER}@${SSH_SERVER} "pkill -f 'uvicorn main:app'"
    if [ $? -eq 0 ]; then
        echo "Uvicorn server stopped successfully."
    else
        echo "No running Uvicorn server found or failed to stop."
    fi
}

# Stop any running server before starting a new one
stop_uvicorn_server

# Start the server
 ssh ${SSH_USER}@${SSH_SERVER}  "cd $DEST_DIR; source testdaq/venv/bin/activate; cd daq; uvicorn main:app --host 0.0.0.0 --port 8500 --reload"
