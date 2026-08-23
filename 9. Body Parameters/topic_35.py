"""
    EMBED A SINGLE Body PARAMETER
    - Let's say you only have a single item body parameter from a Pydantic model 'Item'.
    - By default, FastAPI will then expect its body directly.
    - But if you want it to expect a JSON with a key item and inside of it the model contents, you can use the special Body parameter embed.
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

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {'item_id': item_id, 'item': item}
    return results