#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Update package list and install Git
sudo apt update
# sudo apt full-upgrade
# sudo reboot
sudo apt install -y git python3-pip

# Download and run DAQ stuff
cd ~
if [ -d "daqhats" ]; then
    echo "Directory daqhats already exists. Pulling latest changes."
    cd daqhats
    git pull
else
    git clone https://github.com/mccdaq/daqhats.git
    cd daqhats
fi

sudo ./install.sh

# Install the Python package
sudo pip3 install daqhats
