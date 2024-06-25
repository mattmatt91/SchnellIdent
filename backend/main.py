
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import requests



app = FastAPI()
# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "test from backend"


@app.get("/data")
def get_random_data():
    # Generate some random data for demonstration
    random_numbers = [random.randint(1, 100) for _ in range(5)]
    return {"random_data": random_numbers}


@app.get("/measurement")
async def measure_data():
    id = get_current_datetime_string()
    params = {"duration": 3, "rate": 1000,
              "power": 5, "duration_heater": 0.1, "id": id}
    url = f'http://hardware:3010/start'
    data = requests.post(url=url, json=params).json()
    params = eval_measurement(data, params)
    url = f"http://database:3040/add_dataset/{id}" ###################################### change against database
    requests.post(url, json={"data": data, "info": params})
    data = convert_to_list(data)
    return {"data": data, "params": params}


@app.get("/get_measurement/{id}")
async def get_data(id: str):
    url = f"http://database:3040/get_dataset/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = convert_to_list(response.json()["data"])
        params = response.json()["info"]
        return {"data": data, "params": params}


@app.get("/get_all_ids")
async def get_get_all_measurements():
    response = requests.get(f"http://database:3040/list_datasets")
    if response.status_code == 200:
        return response.json()["dataset_ids"]


def convert_to_list(data: dict):
    new_data = []
    for i, n in zip(data["time"], range(len(data["time"]))):
        new_data.append(
            {"timestamp": i, "MIC": data["MIC"][n], "IR": data["IR"][n]})
    return new_data


def get_current_datetime_string():
    now = datetime.now()
    formatted_datetime = now.strftime("%H_%M_%S-%d_%m_%Y")
    return formatted_datetime


def eval_measurement(data: dict, params: dict):
    params["explosive"] = random.choice([True, False])
    return params
