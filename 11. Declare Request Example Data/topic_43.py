"""
    Field ADDITIONAL ARGUMENTS
    - When using Field() with Pydantic models, you can also declare additional examples.
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(examples=["Van"])
    description: str | None = Field(default='None', examples=['A very nice item'])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}