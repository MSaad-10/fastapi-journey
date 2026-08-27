"""
    RESPONSE MODEL ENCODING PARAMETERS
    - Your response model could have default values.
    - But you might want to omit them from the result if they were not actually stored.
    - This is possible by using response model encoding parameters.

    USE THE 'response_model_exclude_unset' PARAMETER
    - You can set the path operation decorator parameter 'response_model_exclude_unset=True'.
    - And the default values won't be included in the response, only the values actually set. 
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None   # Optional + Default value
    price: float        
    tax: float = 10.5               # Default value
    tags: list[str] = []            # Default value

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

@app.get('/items/{item_id}', response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]