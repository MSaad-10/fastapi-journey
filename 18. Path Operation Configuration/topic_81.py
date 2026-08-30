"""
    RESPONSE STATUS CODE
    - You can define the (HTTP) status_code to be used in the response of your path operation.
    - You can pass directly the int code, like 404.
    - But if you don't remember what each number code is for, you can use the shortcut constants in status.
"""


from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post('/items/', status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> Item:
    return item