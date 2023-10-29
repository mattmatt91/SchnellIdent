#!/bin/bash

source venv/bin/activate
nvm use 18

cd "hardware"
uvicorn main:app --host 192.168.1.30 --port 3010 --reload &
cd ..

cd "database"
uvicorn main:app --host 192.168.1.30 --port 3040 --reload &
cd ..

cd "backend"
# uvicorn main:app --host 192.168.1.30 --port 4000 --reload &
cd ..

cd "frontend"
npm start &
cd ..

echo "All scripts have started."
wait 


