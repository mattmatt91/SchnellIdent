from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import pandas as pd
import io

app = FastAPI()

# Create a database and a measurements table
def create_database(database_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS measurements (
        id INTEGER PRIMARY KEY,
        data TEXT,
        info TEXT
    )''')
    conn.commit()
    conn.close()

# Add a dataset to the database
@app.post("/add_dataset/{measurement_id}")
def add_dataset(measurement_id: int, data: pd.DataFrame, info: dict):
    database_name = 'db/measurement_data.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    data_json = data.to_json()
    
    cursor.execute('INSERT INTO measurements (id, data, info) VALUES (?, ?, ?)',
                   (measurement_id, data_json, str(info))
    )
    
    conn.commit()
    conn.close()
    return {"message": "Dataset added successfully"}

# Retrieve data for a specific measurement ID
@app.get("/get_measurement_data/{measurement_id}")
def get_measurement_data(measurement_id: int):
    database_name = 'db/measurement_data.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('SELECT data, info FROM measurements WHERE id = ?', (measurement_id,))
    data, info = cursor.fetchone()

    conn.close()

    if data:
        data = pd.read_json(io.StringIO(data))
        return {"data": data.to_dict(), "info": info}
    else:
        return {"message": "Measurement not found"}

# List all stored measurement IDs
@app.get("/list_measurement_ids")
def list_measurement_ids():
    database_name = 'db/measurement_data.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute('SELECT DISTINCT id FROM measurements')
    measurement_ids = cursor.fetchall()

    conn.close()

    return {"measurement_ids": [id[0] for id in measurement_ids]}

if __name__ == "__main__":
    create_database('db/measurement_data.db')
