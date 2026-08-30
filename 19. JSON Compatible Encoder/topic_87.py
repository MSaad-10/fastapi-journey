"""
    USING THE jsonable_encoder
    - There are some cases where you might need to convert a data type (Pydantic model) to something compatible with JSON (like a dict, list, etc).
        * For example, if you need to store it in a database.
    - For that, FastAPI provides a jsonable_encoder() function.
"""


from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

fake_db = {}

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: str | None = None

@app.put('/items/{id}', tags=['Put Data'])
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data 

@app.get('/items/{item_id}', tags=['Get Data'])
async def get_item(item_id: str):
    return fake_db[item_id]