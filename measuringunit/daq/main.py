from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
# from read_data_mock import get_data  # Import your actual get_data function
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

@app.post("/sensor_data")
async def measure_data(params: SensorDataParams):
    samples_per_channel = int(params.duration * params.rate)
    data = get_data(params.rate, samples_per_channel, [params.channel_ir, params.channel_mic], ["MIC", "IR"])
    return data
