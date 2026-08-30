"""
    UPDATE REPLACING WITH PUT
    - To update an item you can use the HTTP PUT operation.
    - You can use the jsonable_encoder to convert the input data to data that can be stored as JSON (e.g. with a NoSQL database).
        * For example, converting datetime to str.
"""


from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get('/items/{item_id}', response_model=Item, tags=['Get Data'], description="Get the updated/stored data by putting item_id.")
async def read_item(item_id: str):
    return items[item_id]

@app.put('/items/{item_id}', response_model=Item, tags=['Put Data'], description="Update the already saved data.")
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded