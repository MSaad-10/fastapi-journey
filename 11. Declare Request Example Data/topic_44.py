"""
    Body WITH examples
    - We can pass examples containing one example of the data expected in Body().
"""


from fastapi import FastAPI, Body
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
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    'name': 'Remote',
                    'description': 'A very nice item',
                    'price': 35.4,
                    'tax': 3.4,
                }
            ]
        )
    ]
):
    return {'item_id': item_id, 'item': item}



"""
    Body WITH MULTIPLE examples
    - You can of course also pass multiple examples.
    - The Swagger UI will only display the very first item of examples list instead of dsiplaying all examples.
"""


from fastapi import FastAPI, Body
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
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    'name': 'Remote',
                    'description': 'A very nice item',
                    'price': 35.4,
                    'tax': 3.4,
                },
                {
                    'name': 'Watch',
                    'price': 23.4
                },
                {
                    'name': 'Mobile',
                    'price': 'thirty five point three'
                }
            ]
        )
    ]
):
    return {'item_id': item_id, 'item': item}