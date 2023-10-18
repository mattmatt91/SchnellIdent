from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from heater import toggle_heater


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None





@app.get("/measurement/")
def read_item():
    return {"item_id": 123}


# @app.put("/items/")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


def measure():
    toggle_heater()