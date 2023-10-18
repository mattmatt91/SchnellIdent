from fastapi import FastAPI, HTTPException
import sqlite3
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Create a SQLite database connection and cursor
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a table to store dataframes
cursor.execute(
    """CREATE TABLE IF NOT EXISTS dataframes (id TEXT PRIMARY KEY, dataframe BLOB)"""
)
conn.commit()

class DataframeCreate(BaseModel):
    id: str
    dataframe: pd.DataFrame

class DataframeResponse(BaseModel):
    id: str

@app.post("/store_dataframe", response_model=DataframeResponse)
async def store_dataframe(dataframe_create: DataframeCreate):
    try:
        # Serialize the dataframe to bytes for storage in SQLite
        dataframe_bytes = dataframe_create.dataframe.to_pickle()
        
        # Store the dataframe in the database
        cursor.execute("INSERT INTO dataframes (id, dataframe) VALUES (?, ?)", (dataframe_create.id, dataframe_bytes))
        conn.commit()
        
        return {"id": dataframe_create.id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error storing dataframe: {e}")

@app.get("/retrieve_dataframe/{dataframe_id}", response_model=pd.DataFrame)
async def retrieve_dataframe(dataframe_id: str):
    try:
        # Retrieve the serialized dataframe from the database
        cursor.execute("SELECT dataframe FROM dataframes WHERE id = ?", (dataframe_id,))
        result = cursor.fetchone()
        if result is not None:
            dataframe_bytes = result[0]
            df = pd.read_pickle(dataframe_bytes)
            return df
        else:
            raise HTTPException(status_code=404, detail="Dataframe not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving dataframe: {e}")
