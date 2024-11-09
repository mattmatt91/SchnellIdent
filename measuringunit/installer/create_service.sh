#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Define variables for FastAPI service
USER="daq"
APP_BASE_DIR="/home/daq/Desktop/daq"
VENV_DIR="venv"
SERVICE_FILE="/etc/systemd/system/fastapi.service"
APP_ENTRY="main:app"
PORT="8500"

# Define variables for dhcpcd restart service
DHCPCD_SERVICE_FILE="/etc/systemd/system/restart-dhcpcd.service"

# Ensure the application directory and virtual environment exist
if [ ! -d "$APP_BASE_DIR" ]; then
    echo "Error: Application directory $APP_BASE_DIR does not exist."
    exit 1
fi

if [ ! -d "$APP_BASE_DIR/$VENV_DIR" ]; then
    echo "Error: Virtual environment directory $APP_BASE_DIR/$VENV_DIR does not exist."
    exit 1
fi

# Create the FastAPI service file
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

# Reload systemd to apply the new FastAPI service
sudo systemctl daemon-reload

# Enable and start the FastAPI service
sudo systemctl enable fastapi.service
sudo systemctl start fastapi.service

# Check the status of the FastAPI service
sudo systemctl status fastapi.service

# Create the dhcpcd restart service if it doesn't already exist
if [ ! -f "$DHCPCD_SERVICE_FILE" ]; then
    echo "Creating the restart-dhcpcd service file..."

    sudo bash -c "cat > $DHCPCD_SERVICE_FILE" <<EOF
[Unit]
Description=Restart dhcpcd at startup
After=network.target

[Service]
Type=oneshot
ExecStart=/bin/systemctl restart dhcpcd
RemainAfterExit=true

[Install]
WantedBy=multi-user.target
EOF

    # Reload systemd to recognize the new dhcpcd service
    sudo systemctl daemon-reload

    # Enable the dhcpcd restart service to run at startup
    sudo systemctl enable restart-dhcpcd.service
fi

# Start the dhcpcd restart service immediately (optional)
sudo systemctl start restart-dhcpcd.service

# Check the status of the dhcpcd restart service
sudo systemctl status restart-dhcpcd.service
