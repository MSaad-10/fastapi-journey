"""
    BODY - Field
    - The same way you can declare additional validation and metadata in path operation function parameters with Query, Path and Body.
    - you can declare validation and metadata inside of Pydantic models using Pydantic's 'Field'.
"""


from fastapi import FastAPI, Body, Path
from pydantic import BaseModel, Field
from typing import Annotated  

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The descripion of the item", max_length=100
    )
    price: float = Field(
        gt=0, description="The price must be greater than zero"
    )
    tax: float | None = Field(default=None)

@app.put('/items/{item_id}')
async def update_item(
    item_id: Annotated[int, Path(description='The ID of the item to get.')],
    item: Annotated[Item, Body(embed=True)],
):
    results = {'item_id': item_id, 'item': item}
    return results