#!/bin/bash

HOST_IP="si.local"
HOST_NAME="si"
# rm hostname
ssh-keygen -R $HOST_IP

# Generate a new SSH key pair (follow the prompts, or check if you already have keys you want to use)
ssh-keygen

# Copy the public SSH key to the remote host for passwordless SSH access
ssh-copy-id $HOST_NAME@$HOST_IP

# SSH into the remote host
ssh $HOST_NAME@$HOST_IP 'exit'

# Transfer the Docker installation script to the remote host
scp install_docker_compose.sh $HOST_NAME@$HOST_IP:~/

# Execute the Docker installation script on the remote host
ssh $HOST_NAME@$HOST_IP 'bash ~/install_docker_compose.sh'

bash ../deploy_to_rp


# install node and react stuff, npm then nom install and npm start for debugging frontend