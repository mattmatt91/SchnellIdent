from fastapi import FastAPI
from typing import List
import random
import asyncio
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import string
import requests


local_ip_address ="localhost"



def get_current_datetime_string():
    now = datetime.now()
    formatted_datetime = now.strftime("%H_%M_%S-%d_%m_%Y")
    return formatted_datetime

ids = []
for i in range(10):
    ids.append(get_current_datetime_string()+str(i))

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{local_ip_address}:3000"],  # Replace with the origin of your frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
# Function to generate random data
def generate_mock_data():
    duration = 1  # 3 seconds duration
    sampling_rate = 1000  # 1000 Hz
    data = []
    for t in range(0, duration * sampling_rate):
        timestamp = t / sampling_rate
        ir = round(random.uniform(0, 10), 2)
        mic = round(random.uniform(0, 10), 2)
        data.append({"timestamp": timestamp, "IR": ir, "MIC": mic})
    return data

# Route to serve the mock data with a 5-second delay
@app.get("/measurement")
async def get_measurement_data():
    await asyncio.sleep(5)  # Simulate a 5-second delay
    data = generate_mock_data()
    id = get_current_datetime_string()
    ids.append(id)
    params = {"duration": 1, "rate": 1000,
              "power": 1, "duration_heater": 1, "id": id}
    params["explosive"] = random.choice([True, False])
    return {"data":data, "params":params}

@app.get("/get_all_ids", response_model=List[str])
def get_all_ids():
    return ids

@app.get("/get_measurement/{id}")
def get_measurement(id: str):
    if id in ids:
        params = {"duration": 1, "rate": 1000,
              "power": 1, "duration_heater": 1, "id": id,"explosive":True}
        params["explosive"] = random.choice([True, False])
        data = generate_mock_data()
        return {"data":data, "params":params}
    return {"error": "ID not found"}

@app.get("/")
def read_root():
    return "test from backend"

