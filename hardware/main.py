from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import pandas as pd
from time import sleep
import threading

class MeasurementData(BaseModel):
    duration: int
    rate: int
    power: int
    duration_heater: int
    id: str

app = FastAPI()


@app.post("/start")
async def start(data: MeasurementData):
    print(data)

    rate = data.rate
    duration = data.duration
    power= data.power
    duration_heater = data.duration_heater
    id = data.id
    print(id)
    thread1 = threading.Thread(target=read_data, args = (rate, duration))
    thread2 = threading.Thread(target=toggle_heater, args = (power, duration_heater))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


def read_data(rate:int, duration:int):
    data = generate_random_data(rate, duration)
    return data

def toggle_heater(power:int, duration:int):
    pass



# moc data    
def generate_random_data(rate:int, duration:int):
    num_data_points = int(rate *duration)
    time_intervals = [timedelta(seconds=i)/rate for i in range(num_data_points)]
    ir_data = [random.uniform(0, 1) for _ in range(num_data_points)]
    mic_data = [random.uniform(0, 1) for _ in range(num_data_points)]
    data = {
        "Time": time_intervals,
        "IR": ir_data,
        "MIC": mic_data
    }
    df = pd.DataFrame(data)
    start_time = datetime.now()
    df["Time"] = df["Time"] # + start_time
    df.set_index('Time', inplace=True)
    sleep(duration)
    print(data)
    # return df

