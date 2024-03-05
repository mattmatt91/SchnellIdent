#!/bin/bash

# Define the SSH user and host
SSH_USER="si"
RPI_HOST="si.local"

# Define the local and remote directories
REMOTE_DIR="/home/${SSH_USER}/Desktop/${SSH_USER}/frontend"

# Copy App.js, src, and public directories to Raspberry Pi
rsync -avz --progress frontend/src $SSH_USER@$RPI_HOST:$REMOTE_DIR
rsync -avz --progress frontend/public $SSH_USER@$RPI_HOST:$REMOTE_DIR

echo "Copy completed."
