"""
    Tags
    - You can add tags to your path operation.
    - Pass the parameter tags with a list of str (commonly just one str).
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    sequence: set[str] = set()

@app.post('/items/', tags=['items'])
async def create_item(item: Item) -> Item:
    return item

@app.get('/items/', tags=['toys'])
async def read_items():
    return [{'name': 'clock', 'price': 42}]

@app.get('/users', tags=['users'])
async def read_users():
    return [{'username': 'saad01'}]