#!/bin/bash

sudo apt update
# sudo apt full-upgrade
# sudo reboot
sudo apt install git

# Download and run daq stuff
cd ~
git clone https://github.com/mccdaq/daqhats.git

cd ~/daqhats
sudo ./install.sh

sudo pip install daqhats
