"""
    RESPONSE MODEL - Return Type
    - You can declare the type used for the response by annotating the path operation function return type.
    - You can use type annotations the same way you would for input data in function parameters.
    - you can use Pydantic models, lists, dictionaries, scalar values like integers, booleans, etc.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float  | None = None
    tags: list[str] = []

@app.post('/items/')
async def create_item(item: Item) -> Item:
    return item

@app.get('/items/')
async def read_items() -> list[Item]:
    return [
        Item(name='Portal Gun', price=23.4),
        Item(name='Plumbus', price=34.3),
    ]