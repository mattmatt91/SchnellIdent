#!/bin/bash
HOST_NAME="si"

sudo apt update
sudo apt upgrade -y
sudo apt-get update
sudo apt-get install i2c-tools

# Download and run Docker installation script
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add 'pi' user to the 'docker' group
sudo usermod -aG docker $HOST_NAME

docker --version

sudo apt install -y libffi-dev libssl-dev python3 python3-pip
sudo apt-get install -y docker-compose
sudo systemctl enable docker

docker-compose --version