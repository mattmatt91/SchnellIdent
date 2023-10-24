#!/bin/bash

# Define the paths to your backend and frontend directories
backend_dir=".test/front_end_test/main"
frontend_dir=".frontend"

# Start the FastAPI backend using Uvicorn
cd $backend_dir
uvicorn main:app --host 0.0.0.0 --port 4000 &

# Start the React frontend
cd ../$frontend_dir
npm start
