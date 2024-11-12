from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import os
import asyncio
from read_data import get_data  # Import your actual get_data function

# Import GPIO library for controlling the pins
try:
    import RPi.GPIO as GPIO
except ImportError:
    GPIO = None  # Handle the case when running locally without GPIO

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
    duration_heater: float = 1
    offset_heater: float = 0.5
    channels: Dict[str, int]  # Dictionary of channel names to numbers

# Set up the GPIO pin for the heater control (e.g., GPIO17)
HEATER_PIN = 17

if GPIO:
    GPIO.setmode(GPIO.BCM)  # Use BCM numbering
    GPIO.setup(HEATER_PIN, GPIO.OUT)  # Set up the pin as an output

@app.get("/")
def read_root():
    return "test from backend"

async def toggle_heater(duration_heater: float, offset_heater: float):
    await asyncio.sleep(offset_heater)  # Wait before turning the heater on
    if GPIO:
        GPIO.output(HEATER_PIN, GPIO.HIGH)  # Set the pin high (turn the heater on)
        print("HEATER ON")
    
    await asyncio.sleep(duration_heater)  # Keep the heater on for the specified duration
    
    if GPIO:
        GPIO.output(HEATER_PIN, GPIO.LOW)  # Set the pin low (turn the heater off)
        print("HEATER OFF")

@app.post("/sensor_data")
async def measure_data(params: SensorDataParams):
    # Start the heater toggle task asynchronously
    print(params)
    heater_task = asyncio.create_task(toggle_heater(params.duration_heater, params.offset_heater))
    
    # Run get_data in a separate thread to allow the event loop to handle other tasks
    samples_per_channel = int(params.duration * params.rate)
    channel_names = list(params.channels.keys())
    channel_numbers = list(params.channels.values())
    
    data = await asyncio.to_thread(get_data, params.rate, samples_per_channel, channel_numbers, channel_names)
    
    # Wait for the heater task to complete
    await heater_task
    
    return data

# Ensure GPIO is cleaned up on exit if applicable
if GPIO:
    import atexit
    atexit.register(GPIO.cleanup)
