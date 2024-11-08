#!/bin/bash

HOST_IP="si.local"
HOST_NAME="si"
# # rm hostname
# ssh-keygen -R $HOST_IP
# 
# # Generate a new SSH key pair (follow the prompts, or check if you already have keys you want to use)
# ssh-keygen
# 
# # Copy the public SSH key to the remote host for passwordless SSH access
# ssh-copy-id $HOST_NAME@$HOST_IP
# 
# # SSH into the remote host
# ssh $HOST_NAME@$HOST_IP 'exit'
# 
# # Transfer the Docker installation script to the remote host
# scp install_docker_compose.sh $HOST_NAME@$HOST_IP:~/
# 
# # Execute the Docker installation script on the remote host
# ssh $HOST_NAME@$HOST_IP 'bash ~/install_docker_compose.sh'


scp set_static_ip.sh $HOST_NAME@$HOST_IP:~/


# set static ip and install requirements
ssh $HOST_NAME@$HOST_IP 'sudo apt update'
ssh $HOST_NAME@$HOST_IP 'sudo apt install -y dhcpcd5' 
ssh $HOST_NAME@$HOST_IP 'sudo apt update --fix-missing'
ssh $HOST_NAME@$HOST_IP 'sudo apt install -y dhcpcd5'
ssh $HOST_NAME@$HOST_IP 'sudo systemctl enable dhcpcd '

ssh $HOST_NAME@$HOST_IP 'sudo systemctl start dhcpcd'

ssh $HOST_NAME@$HOST_IP 'chmod +x ~/set_static_ip.sh'

ssh $HOST_NAME@$HOST_IP 'bash ~/set_static_ip.sh'
 
ssh $HOST_NAME@$HOST_IP 'sudo systemctl restart dhcpcd'


# bash ../deploy_to_rp

