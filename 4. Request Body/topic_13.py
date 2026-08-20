"""
    REQUEST BODY + PATH PARAMETERS
    - You can declare path parameters and request body at the same time.
    - FastAPI will recognize that the function parameters that match path parameters should be taken from the path.
    - And the function parameters that are declared to be Pydantic models should be taken from the request body.
"""


from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")                        # works same as @app.post()
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}


"""
    REQUEST BODY + PATH PARAMETERS + QUERY PARAMETERS
    - You can also declare body, path and query parameters, all at the same time.
    - FastAPI will recognize each of them and take the data from the correct place.
"""


from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q": q})
    return result
