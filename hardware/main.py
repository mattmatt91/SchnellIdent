from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from time import sleep
# from read_data import get_data
from fastapi.middleware.cors import CORSMiddleware
import platform
import math
from get_mock_data import get_data_mock

local_ip_address ="localhost"

app = FastAPI()

# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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

    if platform.system == "Linux" and False:
        pass
        data = get_data(rate, samples_per_channel, [channel_mic, channel_ir], ["mic", "ir"])
    else:
        data, explosive = get_data_mock()
    sleep(duration)  # Simulating a delay to mimic real-time data generation
    return data, explosive

def toggle_heater(power:int, duration:int):
    pass


# moc data    



