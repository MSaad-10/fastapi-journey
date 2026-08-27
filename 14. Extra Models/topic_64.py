"""
    LIST OF MODELS
    - The same way, you can declare responses of lists of objects.
    - For that, use the standard Python list.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get('/items/', response_model=list[Item])
async def read_items():
    return items



"""
    RESPONSE WITH ARBITRARY dict
    - You can also declare a response using a plain arbitrary dict, declaring just the type of the keys and values, without using Pydantic model.
    - This is useful if you don't know the valid field/attribute names beforehand.
"""


from fastapi import FastAPI

app = FastAPI()

@app.get('/keyword-weights/', response_model=dict[str, float])
async def read_keyboard_weights():
    return {'foo': 2.3, 'bar': 3.4}