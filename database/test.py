import requests

# Base URL of your FastAPI app
base_url = "http://localhost:80"  # Update this URL as needed

# Test adding a new dataset
dataset_id = "unique_id_2"
data = {"key1": "value1", "key2": "value2"}
info = {"location": "Sensor A", "measurement_type": "Type 1"}
response = requests.post(f"{base_url}/add_dataset/{dataset_id}", json={"data": data, "info": info})
print("Add Dataset Response:", response.status_code)

# Test getting a dataset by ID
response = requests.get(f"{base_url}/get_dataset/{dataset_id}")
print("Get Dataset Response:", response.status_code)
if response.status_code == 200:
    print("Dataset:", response.json())

# Test listing all dataset IDs
response = requests.get(f"{base_url}/list_datasets")
print("List Datasets Response:", response.status_code)
if response.status_code == 200:
    print("Dataset IDs:", response.json()["dataset_ids"])