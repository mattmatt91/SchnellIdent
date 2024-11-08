#!/bin/bash

# Define the new configuration for eth0
config="
interface eth0
static ip_address=192.168.2.100/24
"

# Remove any existing eth0 configuration in /etc/dhcpcd.conf
sudo sed -i '/^interface eth0$/,/^$/d' /etc/dhcpcd.conf

# Append the new configuration to /etc/dhcpcd.conf
echo "$config" | sudo tee -a /etc/dhcpcd.conf > /dev/null

# Restart dhcpcd service to apply changes
sudo systemctl restart dhcpcd

echo "Replaced configuration for eth0 in /etc/dhcpcd.conf and restarted dhcpcd."
