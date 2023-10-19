from fastapi import FastAPI
import requests
import uuid


app = FastAPI()


@app.get("/")
def read_root():
    return "test from backend"


@app.get("/measurement")
async def measure_data():
    id = str(uuid.uuid4())
    params = {"duration": 10, "rate": 1000,
              "power": 1, "duration_heater": 1, "id": id}
    url = 'http://hardware:3010/start'
    data = requests.post(url=url, json=params).json()

    url = "http://database:3040"
    response = requests.post(
        f"{url}/add_dataset/{id}", json={"data": data, "info": params})
    # print("Add Dataset Response:", response.status_code)
    return id


@app.get("/get_data")
async def get_data(id: str):
    url = "http://database:3040"
    response = requests.get(f"{url}/get_dataset/{id}")
    print("Get Dataset Response:", response.status_code)
    if response.status_code == 200:
        print("Dataset:", response.json())
        return response.json()


@app.get("/get_all_measurements")
async def get_get_all_measurements():
    url = "http://database:3040"
    response = requests.get(f"{url}/list_datasets")
    print("List Datasets Response:", response.status_code)
    if response.status_code == 200:
        print("Dataset IDs:", response.json()["dataset_ids"])
