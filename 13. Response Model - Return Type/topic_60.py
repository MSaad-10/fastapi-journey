"""
    'response_model_include' AND 'response_model_exclude'
    - Both of the parameters will take a 'set' of 'str' with the name of attributes to include or to exclude.
    - It can function as a quick shortcut if you have only one Pydantic model and want to remove some data from the output.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": 'There goes my baz', "price": 50.2, "tax": 10.5,},
}

@app.get('/items/{item_id}/name', response_model=Item, response_model_include={'name', 'description'})
async def read_item_name(item_id: str):
    return items[item_id]

@app.get('/items/{item_id}/public', response_model=Item, response_model_exclude={'tax'})
async def read_item_public_data(item_id: str):
    return items[item_id]



"""
    USING list INSTEAD OF set
    - You can use list instead of set with 'response_model_include' and 'response_model_exclude'.
    - If you forget to use a set and use a list or tuple instead, FastAPI will still convert it to a set and it will work correctly.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": 'There goes my baz', "price": 50.2, "tax": 10.5,},
}

@app.get('/items/{item_id}/name', response_model=Item, response_model_include=['name', 'description'])
async def read_item_name(item_id: str):
    return items[item_id]

@app.get('/items/{item_id}/public', response_model=Item, response_model_exclude=['tax'])
async def read_item_public_data(item_id: str):
    return items[item_id]