#!/bin/bash

# Get WLAN IP address (replace 'en0' with your Wi-Fi interface name if different)
WLAN_IP=$(ifconfig en0 | grep 'inet ' | awk '{print $2}')

# Get Ethernet IP address (replace 'en7' with your Ethernet interface name if different)
ETH_IP=$(ifconfig en7 | grep 'inet ' | awk '{print $2}')

# Display the results
echo "WLAN IP Address: ${WLAN_IP:-Not connected}"
echo "Ethernet IP Address: ${ETH_IP:-Not connected}"

# Check if Ethernet IP is available
if [[ -n "$ETH_IP" ]]; then
  # Prompt for SSH destination
  read -p "Enter the SSH username and remote host (e.g., user@remote_host_ip): " SSH_DEST
  
  # Initiate SSH using Ethernet IP
  echo "Attempting SSH connection via Ethernet interface ($ETH_IP)..."
  ssh -b "$ETH_IP" "$SSH_DEST"
else
  echo "Ethernet interface is not connected. Cannot initiate SSH."
fi

