from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
from time import sleep
from get_data import command_daq 
# from get_data import command_daq
from fastapi.middleware.cors import CORSMiddleware
import platform
import math
import pandas as pd


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
    offset_heater: float
    duration_heater: float
    id: str


@app.post("/start")
async def start(data: MeasurementData):
    rate = int(data.rate)
    duration = int(data.duration)
    power= float(data.power)
    offset_heater = float(data.offset_heater)
    duration_heater = float(data.duration_heater)
    channel_mic = 1
    channel_ir = 2
    daq_arguments = {"rate":int(rate), 
                     "duration":float(duration),
                       "power":float(power),
                         "duration_heater":float(duration_heater),
                         "offset_heater":float(offset_heater),
                           "channel_ir":int(channel_ir),
                             "channel_mic":int(channel_mic)}
    data = command_daq(daq_arguments)
  
    return data


