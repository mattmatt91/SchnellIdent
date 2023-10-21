from fastapi import FastAPI
import requests
import uuid
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your React app's URL here
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

    url = f"http://database:3040/add_dataset/{id}"
    print(url)
    response = requests.post(url, json={"data": data, "info": params})
    print(response)
    print("Add Dataset Response:", response.status_code)
    return id


@app.get("/get_measurement/{id}")
async def get_data(id: str):
    url = f"http://database:3040/get_dataset/{id}"
    response = requests.get(url)
    print("Get Dataset Response:", response.status_code)
    if response.status_code == 200:
        # print("Dataset:", response.json())
        return response.json()


@app.get("/get_all_ids")
async def get_get_all_measurements():
    url = "http://database:3040"
    response = requests.get(f"{url}/list_datasets")
    print("List Datasets Response:", response.status_code)
    if response.status_code == 200:
        print("Dataset IDs:", response.json()["dataset_ids"])
        return response.json()
