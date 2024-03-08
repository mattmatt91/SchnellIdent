#!/bin/bash

# SSH details
SSH_USER="si"
SSH_SERVER="si.local"
DEST_DIR="/home/${SSH_USER}/Desktop/si"

# Folders to copy
FOLDER1="frontend"
FOLDER2="database"
FOLDER3="hardware"
FOLDER4="backend"

ADDITIONAL_FILES=("docker-compose.yml")


copy_folder() {
    local folder=$1
    rsync -av --exclude 'node_modules' --exclude 'venv'  "$folder" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
}


ssh "${SSH_USER}@${SSH_SERVER}" "cd ${DEST_DIR} && rm -rf frontend && mkdir frontend"
# Copy folders
copy_folder "$FOLDER1"
copy_folder "$FOLDER2"
copy_folder "$FOLDER3"
copy_folder "$FOLDER4"


# Copy additional files
for file in "${ADDITIONAL_FILES[@]}"; do
    scp "$file" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
done

# Run Docker Compose

ssh "${SSH_USER}@${SSH_SERVER}" "cd ${DEST_DIR} && docker-compose up --build database"