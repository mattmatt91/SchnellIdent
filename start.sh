#!/bin/bash

# local_ip_address=$(hostname -I | cut -d' ' -f1)
export LOCAL_IP_ADDRESS="192.168.1.30" 
export LOCAL_IP_ADDRESS=${LOCAL_IP_ADDRESS:-192.168.1.30}
echo "Starting on address: $LOCAL_IP_ADDRESS"

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
