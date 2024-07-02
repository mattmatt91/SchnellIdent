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

# Files to copy
ADDITIONAL_FILES=("docker-compose.yml" ".env.rpi")

# Function to copy folders
copy_folder() {
    local folder=$1
    rsync -av --exclude 'node_modules' --exclude 'venv'  "$folder" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
}

# Copy folders
copy_folder "$FOLDER1"
copy_folder "$FOLDER2"
copy_folder "$FOLDER3"
copy_folder "$FOLDER4"

# Copy additional files
for file in "${ADDITIONAL_FILES[@]}"; do
    scp "$file" "${SSH_USER}@${SSH_SERVER}:${DEST_DIR}"
done

# Rename .env.rpi to .env on the Raspberry Pi
ssh "${SSH_USER}@${SSH_SERVER}" "mv ${DEST_DIR}/.env.rpi ${DEST_DIR}/.env"

# Run Docker Compose
ssh "${SSH_USER}@${SSH_SERVER}" "cd ${DEST_DIR} && docker-compose up --build hardware"
