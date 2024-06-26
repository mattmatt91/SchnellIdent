#!/bin/bash

HOST_IP="daq.local"
HOST_NAME="daq"
DEST_DIR="home/daq/Desktop/daq"
# rm hostname
ssh-keygen -R $HOST_IP

# Generatea new SSH key pair (follow the prompts, or check if you already have keys you want to use)
ssh-keygen

# Copy the public SSH key to the remote host for passwordless SSH access
ssh-copy-id $HOST_NAME@$HOST_IP

# SSH into the remote host
ssh $HOST_NAME@$HOST_IP 'exit'

# Install DAQ
scp install_daq.sh $HOST_NAME@$HOST_IP:~/
ssh $HOST_NAME@$HOST_IP 'bash ~/install_daq.sh'

# Create venv
scp create_venv.sh $HOST_NAME@$HOST_IP:~/
ssh $HOST_NAME@$HOST_IP 'bash ~/create_venv.sh'

# create auto start service
scp create_service.sh $HOST_NAME@$HOST_IP:~/
ssh $HOST_NAME@$HOST_IP 'bash ~/create_service.sh'
