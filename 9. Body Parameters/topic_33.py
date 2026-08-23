"""
    SINGULAR VALUES IN BODY
    - The same way there is a 'Query' and 'Path' to define extra data for query and path parameters.
    - FastAPI provides an equivalent 'Body'.
    - You can decide to have another key 'importance' in the body, besides the 'item' and 'user'.
    - If you declare it as is, because it is a singular value, FastAPI will assume that it is a query parameter.
    - But you can instruct FastAPI to treat it as another body key using 'Body'.
"""


from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str  | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body()]
):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    return results