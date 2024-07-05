#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables
USER="daq"
APP_BASE_DIR="/home/daq/Desktop/daq/myfastapiapp"
VENV_DIR="venv"
SERVICE_FILE="/etc/systemd/system/fastapi.service"
APP_ENTRY="main:app"
PORT="8500"

# Ensure the application directory and virtual environment exist
if [ ! -d "$APP_BASE_DIR" ]; then
    echo "Error: Application directory $APP_BASE_DIR does not exist."
    exit 1
fi

if [ ! -d "$APP_BASE_DIR/$VENV_DIR" ]; then
    echo "Error: Virtual environment directory $APP_BASE_DIR/$VENV_DIR does not exist."
    exit 1
fi

# Create the service file with the variables
sudo bash -c "cat > $SERVICE_FILE" <<EOF
[Unit]
Description=FastAPI server
After=network.target

[Service]
User=$USER
WorkingDirectory=$APP_BASE_DIR
ExecStart=/bin/bash -c 'source $APP_BASE_DIR/$VENV_DIR/bin/activate && exec uvicorn $APP_ENTRY --host 0.0.0.0 --port $PORT --reload'
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd to apply the new service
sudo systemctl daemon-reload

# Enable the FastAPI service to start on boot
sudo systemctl enable fastapi.service

# Start the FastAPI service
sudo systemctl start fastapi.service

# Check the status of the FastAPI service
sudo systemctl status fastapi.service
