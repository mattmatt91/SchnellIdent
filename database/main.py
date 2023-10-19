from fastapi import FastAPI, HTTPException
import sqlite3
import json

app = FastAPI()

# Create a SQLite database and a "datasets" table
def create_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS datasets (
        id TEXT PRIMARY KEY,
        data TEXT,
        info TEXT
    )''')
    conn.commit()
    conn.close()

# Add a new dataset to the database
def add_dataset(database_name, dataset_id, data, info):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    # Convert data and info dictionaries to JSON strings
    data_json = json.dumps(data)
    info_json = json.dumps(info)

    cursor.execute('INSERT INTO datasets (id, data, info) VALUES (?, ?, ?)',
                   (dataset_id, data_json, info_json))
    
    conn.commit()
    conn.close()
    print("created database")
# Read a dataset by ID
def read_dataset(database_name, dataset_id):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('SELECT data, info FROM datasets WHERE id = ?', (dataset_id,))
    result = cursor.fetchone()

    conn.close()

    if result:
        data, info = result
        return {"data": json.loads(data), "info": json.loads(info)}
    else:
        return None

# List all dataset IDs
def list_dataset_ids(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM datasets')
    dataset_ids = [row[0] for row in cursor.fetchall()]

    conn.close()

    return dataset_ids

database_name = 'test_dataset_db.db'
# database_name = '/app/data/dataset_db.db'

@app.on_event("startup")
def create_if_not_exists():
    create_database(database_name)




@app.post("/add_dataset/{dataset_id}")
def add_dataset_route(dataset_id: str, data: dict, info: dict):
    add_dataset(database_name, dataset_id, data, info)
    return {"message": "Dataset added successfully"}

@app.get("/get_dataset/{dataset_id}")
def get_dataset_route(dataset_id: str):
    dataset = read_dataset(database_name, dataset_id)
    if dataset:
        return dataset
    else:
        raise HTTPException(status_code=404, detail="Dataset not found")

@app.get("/list_datasets")
def list_datasets_route():
    dataset_ids = list_dataset_ids(database_name)
    return {"dataset_ids": dataset_ids}
