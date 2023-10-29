#!/bin/bash

# Check if an argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <server_address>"
    exit 1
fi

# Store the server address from the command line argument
server_address="$1"
echo "Sending to: $server_address"

# Define the server user
server_user="si"

# Define the destination directory on the remote server
remote_directory="~/Desktop/schnellident"

# Copy files to the remote server using the provided server address
scp -r ./frontend/package-lock.json "$server_user@$server_address:$remote_directory/frontend"
scp -r ./frontend/package.json "$server_user@$server_address:$remote_directory/frontend"
scp -r ./frontend/Dockerfile "$server_user@$server_address:$remote_directory/frontend"
scp -r ./frontend/public "$server_user@$server_address:$remote_directory/frontend"
scp -r ./frontend/src "$server_user@$server_address:$remote_directory/frontend"

scp -r ./backend "$server_user@$server_address:$remote_directory/backend"
scp -r ./hardware "$server_user@$server_address:$remote_directory/hardware"
scp -r ./database "$server_user@$server_address:$remote_directory/database"
scp ./start.sh "$server_user@$server_address:$remote_directory/start.sh"

# Execute a remote command to set permissions
remote_command="cd $remote_directory && chmod +x ./start.sh"
ssh "$server_user@$server_address" "$remote_command"
