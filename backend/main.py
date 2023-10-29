from fastapi import FastAPI
import requests
import uuid
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import socket

import socket

def get_local_network_ip():
    hostname = socket.gethostname()
    # Get a list of IP addresses associated with the hostname
    ip_addresses = socket.gethostbyname_ex(hostname)
    
    # Filter for IP addresses that match the desired style (e.g., 192.168.1.xxx)
    local_network_ips = [ip for ip in ip_addresses[2] if ip.startswith('192.168.1.')]
    
    if local_network_ips:
        return local_network_ips[0]  # Use the first matching IP address
    else:
        return None  # No matching IP address found

local_ip_address = "192.168.1.30" # 
# local_ip_address = get_local_network_ip()
    

app = FastAPI()
    


# local_network_ips = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if ip.startswith('192.168.1.')][0]
allowed_origins = [
    "*"  # Update with your second IP or URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[allowed_origins], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return "test from backend"


@app.get("/measurement")
async def measure_data():
    id = get_current_datetime_string()
    params = {"duration": 1, "rate": 1000,
              "power": 1, "duration_heater": 1, "id": id}
    url = f'http://{local_ip_address}:3010/start'
    data = requests.post(url=url, json=params).json()
    params = eval_measurement(data, params)

    url = f"http://{local_ip_address}:3040/add_dataset/{id}"
    response = requests.post(url, json={"data": data, "info": params})
    data = convert_to_list(data)
    return {"data":data, "params":params}


@app.get("/get_measurement/{id}")
async def get_data(id: str):
    url = f"http://{local_ip_address}:3040/get_dataset/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        data =  convert_to_list(response.json()["data"])   
        params = response.json()["info"]
        return {"data":data, "params":params}


@app.get("/get_all_ids")
async def get_get_all_measurements():
    url = f"http://{local_ip_address}:3040"
    response = requests.get(f"{url}/list_datasets")
    if response.status_code == 200:
        return response.json()["dataset_ids"]
    


def convert_to_list(data: dict):
    new_data = []
    for i, n in zip(data["time"], range(len(data["time"]))):
        new_data.append(
            {"timestamp": i, "MIC": data["mic"][n], "IR": data["ir"][n]})
    return new_data

def get_current_datetime_string():
    now = datetime.now()
    formatted_datetime = now.strftime("%H_%M_%S-%d_%m_%Y")
    return formatted_datetime


def eval_measurement(data:dict, params:dict):
    params["explosive"] = random.choice([True, False])
    return params