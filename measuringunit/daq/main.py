from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import os
import asyncio

# Conditionally import the get_data function
if os.getenv("RUNNING_LOCALLY"):
    from read_data_mock import get_data
else:
    from read_data import get_data  # Import your actual get_data function

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Pydantic model for the expected input
class SensorDataParams(BaseModel):
    rate: int = 10000
    duration: float = 2.0
    power: float = 0.5
    duration_heater: float = 0.5
    channel_ir: int = 0
    channel_mic: int = 1

@app.get("/")
def read_root():
    return "test from backend"

async def toggle_heater(duration_heater: float):
    await asyncio.sleep(0.5)  # Wait for 0.5 seconds before turning the heater on
    print("HEATER ON")
    await asyncio.sleep(duration_heater)  # Keep the heater on for the specified duration
    print("HEATER OFF")

@app.post("/sensor_data")
async def measure_data(params: SensorDataParams):
    # Start the heater toggle task
    heater_task = asyncio.create_task(toggle_heater(params.duration_heater))
    
    # Fetch the data
    samples_per_channel = int(params.duration * params.rate)
    data = get_data(params.rate, samples_per_channel, [params.channel_ir, params.channel_mic], ["MIC", "IR"])
    
    # Wait for the heater task to complete
    await heater_task
    
    return data
