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


# https://www.opendisplaycase.de/tutorials/raspberry-pi-display-waveshare-lcd-1024x600-hdmi-touch.html
# sudo apt-get update && sudo apt-get -y upgrade
# sudo apt-get install -y xserver-xorg-input-evdev
# sudo nano /boot/firmware/config.txt
#      dtparam=i2c_arm=on
#      dtparam=spi=on
#      enable_uart=1
#      hdmi_group=2
#      hdmi_mode=1
#      hdmi_mode=87
#      hdmi_cvt 1024 600 60 6 0 0 0
#      dtoverlay=ads7846,cs=1,penirq=25,penirq_pull=2,speed=50000,keep_vref_on=0,swapxy=0,pmax=255,xohms=150,xmin=200,xmax=3900,ymin=200,ymax=3900

# sudo nano /usr/share/X11/xorg.conf.d/99-calibration.conf
#      zSection "InputClass"
#        Identifier "calibration"
#        MatchProduct "ADS7846 Touchscreen"
#        Option "Calibration" "59 3985 3882 172"
#        Option "SwapAxes" "1"
#        Driver "evdev"
#      EndSection
#      sudo reboot

# sudo apt-get install -y xinput-calibrator