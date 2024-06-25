#!/bin/bash

HOST_IP="daq.local"
HOST_NAME="daq"
# rm hostname

# Transfer the Docker installation script to the remote host
scp install_daq.sh $HOST_NAME@$HOST_IP:~/

# Execute the Docker installation script on the remote host
ssh $HOST_NAME@$HOST_IP 'bash ~/install_daq.sh'



# install node and react stuff, npm then nom install and npm start for debugging frontend