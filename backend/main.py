
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import requests
from fastapi.responses import StreamingResponse
import pandas as pd
import json
from io import BytesIO
import zipfile
import os
from datetime import datetime


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
              "power": 5,"offset_heater":0.5, "duration_heater": 1, "id": id}
    
    url = f'http://hardware:3010/start'
    print(params)
    data = requests.post(url=url, json=params).json()
    print("BACKEND", type(data))
    params = eval_measurement(data, params)
    url = f"http://database:3040/add_dataset/{id}"
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


@app.get("/download_measurement/{measurement_id}")
async def download_measurement(measurement_id: str):
    data = await get_data(measurement_id)
    measurement_data = data["data"]
    measurement_info = data["params"]
    # if not measurement_data or not measurement_info:
    #     raise HTTPException(status_code=404, detail="Measurement not found")

    # Create CSV content in memory
    df = pd.DataFrame(measurement_data)
    csv_buffer = BytesIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    # Create JSON content in memory
    json_buffer = BytesIO()
    json_buffer.write(json.dumps(measurement_info).encode('utf-8'))
    json_buffer.seek(0)

    # Create a ZIP file in memory
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        zip_file.writestr('data.csv', csv_buffer.getvalue())
        zip_file.writestr('info.json', json_buffer.getvalue())
    zip_buffer.seek(0)

    return StreamingResponse(
        zip_buffer,
        media_type='application/zip',
        headers={
            'Content-Disposition': f'attachment; filename=measurement_{measurement_id}.zip'}
    )


@app.get("/download_all_measurements")
async def download_all_measurements():
    all_ids = await get_get_all_measurements()

    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for measurement_id in all_ids:
            data = await get_data(measurement_id)
            measurement_data = data["data"]
            measurement_info = data["params"]

            # Create CSV content in memory
            df = pd.DataFrame(measurement_data)
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)

            # Create JSON content in memory
            json_buffer = BytesIO()
            json_buffer.write(json.dumps(measurement_info).encode('utf-8'))
            json_buffer.seek(0)

            # Create a folder for each measurement and add files
            folder_name = f"measurement_{measurement_id}"
            zip_file.writestr(f"{folder_name}/data.csv", csv_buffer.getvalue())
            zip_file.writestr(f"{folder_name}/info.json",
                              json_buffer.getvalue())

    zip_buffer.seek(0)

    return StreamingResponse(
        zip_buffer,
        media_type='application/zip',
        headers={'Content-Disposition': 'attachment; filename=all_measurements.zip'}
    )



@app.post("/save_measurement/{measurement_id}")
async def save_measurement(measurement_id: str):
    data = await get_data(measurement_id)
    measurement_data = data["data"]
    measurement_info = data["params"]

    # Get the current date and time
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = f"/data/measurement_{measurement_id}_{now}"
    os.makedirs(save_path, exist_ok=True)

    # Save CSV file
    df = pd.DataFrame(measurement_data)
    csv_path = os.path.join(save_path, "data.csv")
    df.to_csv(csv_path, index=False)

    # Save JSON file
    json_path = os.path.join(save_path, "info.json")
    with open(json_path, "w") as json_file:
        json.dump(measurement_info, json_file)

    return {"message": f"Measurement {measurement_id} saved successfully at {save_path}"}

@app.post("/save_all_measurements")
async def save_all_measurements():
    all_ids = await get_get_all_measurements()
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base_save_path = f"/data/all_measurements_{now}"
    os.makedirs(base_save_path, exist_ok=True)

    for measurement_id in all_ids:
        data = await get_data(measurement_id)
        measurement_data = data["data"]
        measurement_info = data["params"]

        # Create a folder for each measurement
        save_path = os.path.join(base_save_path, f"measurement_{measurement_id}")
        os.makedirs(save_path, exist_ok=True)

        # Save CSV file
        df = pd.DataFrame(measurement_data)
        csv_path = os.path.join(save_path, "data.csv")
        df.to_csv(csv_path, index=False)

        # Save JSON file
        json_path = os.path.join(save_path, "info.json")
        with open(json_path, "w") as json_file:
            json.dump(measurement_info, json_file)

    return {"message": f"All measurements saved successfully in {base_save_path}"}



@app.get("/delete_measurement/{id}")
async def del_data(id: str):
    url = f"http://database:3040/delete_dataset/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        return {"info": "Measurement deleted"}


@app.get("/delete_all_measurement/{id}")
async def del_all_data(id: str):
    url = f"http://database:3040d/delete_all_datasets"
    response = requests.get(url)
    if response.status_code == 200:
        return {"info": "Measurement deleted"}


def convert_to_list(data: dict):
    print(data.keys())

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
    params["explosive"] = False # random.choice([True, False])
    return params
