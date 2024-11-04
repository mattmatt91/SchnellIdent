#!/bin/bash

HOST_IP="daq.local"
HOST_NAME="daq"
DEST_DIR="home/daq/Desktop/daq"

# Remove old SSH key entry for the host
ssh-keygen -R "$HOST_IP"

# Check if SSH keys already exist, generate if not
if [ ! -f ~/.ssh/id_rsa ]; then
    ssh-keygen -t rsa -b 4096 -N "" -f ~/.ssh/id_rsa
fi

# Copy the public SSH key to the remote host for passwordless SSH access
ssh-copy-id "$HOST_NAME@$HOST_IP"

# Check if SSH access is working
ssh -o BatchMode=yes -o ConnectTimeout=5 "$HOST_NAME@$HOST_IP" 'exit'
if [ $? -ne 0 ]; then
    echo "Error: Unable to establish SSH connection to $HOST_NAME@$HOST_IP"
    exit 1
fi

# Install DAQ
scp install_daq.sh "$HOST_NAME@$HOST_IP:~/"
if ssh "$HOST_NAME@$HOST_IP" 'bash ~/install_daq.sh'; then
    echo "DAQ installed successfully"
else
    echo "Error: DAQ installation failed"
    exit 1
fi

# Create virtual environment
scp create_venv.sh "$HOST_NAME@$HOST_IP:~/"
if ssh "$HOST_NAME@$HOST_IP" 'bash ~/create_venv.sh'; then
    echo "Virtual environment created successfully"
else
    echo "Error: Virtual environment creation failed"
    exit 1
fi

# Create auto-start service
scp create_service.sh "$HOST_NAME@$HOST_IP:~/"
if ssh "$HOST_NAME@$HOST_IP" 'bash ~/create_service.sh'; then
    echo "Auto-start service created successfully"
else
    echo "Error: Auto-start service creation failed"
    exit 1
fi

# 
# 
# 
# 