"""
    MULTIPLE Body PARAMETERS AND Query
    - You can also declare additional query parameters, additional to any body parameters.
    - By default, singular values are interpreted as query parameters, you don't have to explicitly add a 'Query'.
"""


from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None  
    price: float
    tax : float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id: int,                               # Path Parameter
    item: Item,                                 # Body Parameter
    user: User,                                 # Body Parameter    
    importance: Annotated[int, Body(gt=0)],     # Body Parameter
    q: str | None = None,                       # Query Parameter
):
    results = {'item_id': item_id, 'item': item, 'user': user, 'importance': importance}
    if q:
        results['q'] = q
    return results