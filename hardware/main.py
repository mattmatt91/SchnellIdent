from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from time import sleep
# from read_data import get_data
from fastapi.middleware.cors import CORSMiddleware
import platform
import math

local_ip_address ="localhost"

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[f"http://{local_ip_address}:4000"],  # Replace with the origin of your frontend
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

class MeasurementData(BaseModel):
    duration: int
    rate: int
    power: int
    duration_heater: int
    id: str


@app.post("/start")
async def start(data: MeasurementData):
    rate = int(data.rate)
    duration = int(data.duration)
    power= data.power
    duration_heater = data.duration_heater
    id = data.id
    data = read_data(rate, duration)
    return data

def read_data(rate:int, duration:int):
    samples_per_channel = rate * duration
    channel_mic = 1,
    channel_ir = 2

    if platform.system == "Linux":
        data = get_data(rate, samples_per_channel, [channel_mic, channel_ir], ["mic", "ir"])
    else:
        data = generate_random_data(rate, duration)
    return data

def toggle_heater(power:int, duration:int):
    pass


# moc data    

def generate_random_data(rate: int, duration: int):
    num_data_points = int(rate * duration)
    time_intervals = [(i / rate) for i in range(num_data_points)]  # List of seconds
    t = [2 * math.pi * duration * i / num_data_points for i in range(num_data_points)]
    ir_data = [math.sin(val) + random.gauss(0, 0.1) for val in t]
    mic_data = [math.sin(val + math.pi) + random.gauss(0, 0.1) for val in t]
    ir_data = [round(val, 2) for val in ir_data]
    mic_data = [round(val, 2) for val in mic_data]
    data = {
        "time": time_intervals,  # List of time in seconds
        "IR": ir_data,
        "MIC": mic_data
    }
    sleep(duration)  # Simulating a delay to mimic real-time data generation
    return data


