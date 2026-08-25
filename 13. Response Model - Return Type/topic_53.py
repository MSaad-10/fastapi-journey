"""
    response_model PARAMETER
    - There are some cases where you need or want to return some data that is not exactly what the type declares.
    - response_model is a path operation decorator parameter which is used in place of return type.
    - response_model is used to return some other types of objects like (a dict or database object).
    - You can use response_model parameter in any of the path operations:
        * @app.post()
        * @app.get()
        * @app.put()
        * @app.delete()
"""


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item

@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]