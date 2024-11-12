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
import os
import json


app = FastAPI()

sensors_pins_json = os.getenv("SENSORS_PINS", '{}')
sensors_pins = json.loads(sensors_pins_json)

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

    channels = {key: value for key, value in sensors_pins.items()}

    # Prepare daq_arguments including the channels dictionary
    daq_arguments = {
        "rate": rate,
        "duration": duration,
        "power": power,
        "duration_heater": duration_heater,
        "offset_heater": offset_heater,
        "channels": channels  # Passing the dynamically created channels dict
    }
    data = command_daq(daq_arguments)
  
    return data




