"""
    Tags WITH Enums
    - If you have a big application, you might end up accumulating several tags.
    - And you would want to make sure you always use the same tag for related path operations.
    - In these cases, it could make sense to store the tags in an Enum.
"""

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class Tags(Enum):
    items = 'Items'
    users = 'Users'

@app.get('/items/', tags=[Tags.items])
async def get_items():
    return ["Portal gun", "Plumbus"]

@app.get('/users/', tags=[Tags.users])
async def read_users():
    return ['Saad', 'Asad']