"""
    USING PYDANTIC's exclude_unset PARAMETER
    - If you want to receive partial updates, it's very useful to use the parameter exclude_unset in Pydantic's model's .model_dump().
    - Like item.model_dump(exclude_unset=True).
    - That would generate a dict with only the data that was set when creating the item model, excluding default values.
    - Then you can use this to generate a dict with only the data that was set, omitting default values.
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

@app.get("/items/{item_id}", response_model=Item, tags=['Get Data'])
async def read_item(item_id: str):
    return items[item_id]

@app.patch('/items/{id}', tags=['Update Data'])
async def update_item(id: str, item: Item) -> Item:
    stored_item_data = items[id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.model_dump(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    items[id] = jsonable_encoder(updated_item)
    return updated_item