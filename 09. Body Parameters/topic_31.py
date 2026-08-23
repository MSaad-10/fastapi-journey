"""
    MIX Path, Query AND BODY PARAMETERS
    - You can mix Path, Query and request body parameter declarations freely and FastAPI will know what to do.
    - You can also declare body parameters as optional, by setting the default to None.
"""


from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.put('/items/{item_id}')
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,       # Optional
    item: Item | None = None    # Optional
):
    results = {"item_id": item_id}
    if q:
        results.update({'q': q})
    if item:
        results['item'] = item
    return results    