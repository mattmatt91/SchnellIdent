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

# Delete existing content of the directories on the remote server
ssh "$server_user@$server_address" "cd $remote_directory && ls"
echo "##########"

# Copy files to the remote server using the provided server address
scp  ./frontend/package-lock.json "$server_user@$server_address:$remote_directory/frontend/"
scp  ./frontend/package.json "$server_user@$server_address:$remote_directory/frontend/"
scp  ./frontend/Dockerfile "$server_user@$server_address:$remote_directory/frontend/"
scp -r ./frontend/public "$server_user@$server_address:$remote_directory/frontend/"
scp -r ./frontend/src "$server_user@$server_address:$remote_directory/frontend/"

scp -r ./backend "$server_user@$server_address:$remote_directory/"
scp -r ./hardware "$server_user@$server_address:$remote_directory/"
scp -r ./database "$server_user@$server_address:$remote_directory/"
scp ./start.sh "$server_user@$server_address:$remote_directory/"


echo "##########"
# Execute a remote command to set permissions
remote_command="cd $remote_directory && chmod +x ./start.sh"
ssh "$server_user@$server_address" "$remote_command" 