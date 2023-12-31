from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from time import sleep
from read_data import get_data
from fastapi.middleware.cors import CORSMiddleware
import platform

app = FastAPI()

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

    if platform.system == "Linux":
        data = get_data(rate, samples_per_channel, [channel_mic, channel_ir], ["mic", "ir"])
    else:
        data = generate_random_data(rate, duration)
    return data

def toggle_heater(power:int, duration:int):
    pass


# moc data    
def generate_random_data(rate:int, duration:int):
    num_data_points = int(rate *duration)
    time_intervals = [timedelta(seconds=i)/rate for i in range(num_data_points)]
    ir_data = [round(random.uniform(0, 1),2) for _ in range(num_data_points)]
    mic_data = [round(random.uniform(0, 1),2) for _ in range(num_data_points)]
    data = {
        "time": time_intervals,
        "IR": ir_data,
        "MIC": mic_data
    }
    sleep(duration)
    return data

