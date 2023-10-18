
from fastapi import FastAPI
import requests
import uuid



app = FastAPI()


@app.get("/")
def read_root():
    return "test from backend"


@app.get("/measurement")
async def read_item():
    duration = 3
    rate = 1000
    power = 10
    duration_heater = 1
    id = str(uuid.uuid4())
    params = {"duration": duration, "rate": rate, "power":power, "duration_heater":duration_heater, "id":id}
    print(params)
    url = 'http://hardware:3010/start'
    requests.post(url=url, json=params)
    return id






