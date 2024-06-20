from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from time import sleep
# from get_data import command_daq 
from get_mock_data import command_daq
from fastapi.middleware.cors import CORSMiddleware
import platform
import math
import pandas as pd

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
    channel_mic = 1,
    channel_ir = 2
    daq_arguments = {"rate":rate, "duration":duration, "power":power, "duration_heater":duration_heater, "channel_ir":channel_ir, "channel_mic":channel_mic}
    data = command_daq(daq_arguments)
    explosive = eval_data(data)
    daq_arguments["explosive"] = explosive 
    return data, explosive



def eval_data(data:pd.DataFrame):
    result = True if random.choice([True, False]) else False
    return result
