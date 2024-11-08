#!/bin/bash

# Define the configuration lines you want to add
config="
interface eth0
static ip_address=192.168.2.100/24
"

# Append the configuration lines to /etc/dhcpcd.conf
echo "$config" | sudo tee -a /etc/dhcpcd.conf > /dev/null

# Restart dhcpcd service to apply changes
sudo systemctl restart dhcpcd

echo "Configuration added to /etc/dhcpcd.conf and dhcpcd restarted."