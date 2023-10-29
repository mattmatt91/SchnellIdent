#!/bin/bash

local_ip_address=$(hostname -I | cut -d' ' -f1)
export LOCAL_IP_ADDRESS="$local_ip_address"  # Set the LOCAL_IP_ADDRESS environment variable
echo "Starting on address: $local_ip_address"

source venv/bin/activate
nvm use 18

cd "hardware"
uvicorn main:app --host "$LOCAL_IP_ADDRESS" --port 3010 --reload &
cd ..

cd "database"
uvicorn main:app --host "$LOCAL_IP_ADDRESS" --port 3040 --reload &
cd ..

cd "backend"
uvicorn main:app --host "$LOCAL_IP_ADDRESS" --port 4000 --reload &
cd ..

cd "frontend"
npm start &
cd ..

echo "All scripts have started."
wait
