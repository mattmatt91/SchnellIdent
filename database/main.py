from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import database

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://backend"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.on_event("startup")
def create_if_not_exists():
    database.create_database()


@app.post("/add_dataset/{dataset_id}")
def add_dataset_route(dataset_id: str, data: dict, info: dict):
    database.add_dataset(dataset_id, data, info)
    return {"message": "Dataset added successfully"}


@app.get("/get_dataset/{dataset_id}")
def get_dataset_route(dataset_id: str):  # dataset_id: str):
    dataset = database.read_dataset(dataset_id)
    if dataset:
        return dataset
    else:
        raise HTTPException(status_code=404, detail="Dataset not found")


@app.get("/list_datasets")
def list_datasets_route():
    dataset_ids = database.list_dataset_ids()
    return {"dataset_ids": dataset_ids}


@app.get("/")
def test_route():
    return {"data": "test"}


@app.get("/download_datasets_zip")
async def download_datasets_zip():
    output_folder_data = 'data'
    zip_file_path_data = 'datasets_data.zip'
    database.save_datasets_as_csv(output_folder_data)
    database.save_info_as_csv(output_folder_data)
    database.create_zip_from_folder(output_folder_data, zip_file_path_data)
    return FileResponse(zip_file_path_data, media_type='application/zip', filename='datasets.zip')

@app.get("/delete_all_datasets")
def delete_all_datasets():
    try:
        database.delete_all_data()
    except:
        raise HTTPException(status_code=404, detail="Dataset not found")

@app.get("/delete_dataset/{dataset_id}")
def delete_dataset(dataset_id: str):
    try:
        database.delete_dataset_id(dataset_id)
    except:
        raise HTTPException(status_code=404, detail="Dataset not found")
