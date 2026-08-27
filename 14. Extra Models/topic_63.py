"""
    'Union' OR 'anyof'
    - You can declare a response to be the Union of two or more types.
    - It means the response would be any of them.
    - It will be defined in OpenAPI with 'anyOf'.
    - To do that, use the standard Python type hint 'typing.Union'.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BaseItem(BaseModel):
    type: str
    description: str

class CarItem(BaseItem):
    type: str = 'Car'

class PlaneItem(BaseItem):
    type: str = 'Plane'
    size: int

items = {
    'item1': {'description': 'All my friends drive a low rider', 'type': 'Car'},
    'item2': {'description': "Music is my aeroplane, it's my aeroplane", 'type': 'Plane', 'size': 5,},
}

@app.get('/items/{item_id}', response_model = PlaneItem | CarItem) 
async def read_item(item_id: str):
    return items[item_id]