"""
    RESPONSE DESCRIPTION
    - You can specify the response description with the parameter response_description.
    - Notice that response_description refers specifically to the response.
    - The description refers to the path operation in general.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.post(
        '/items/', 
        tags=["Item"], 
        summary='Create an item',
        response_description="response_description: The created item",
)
async def create_item(item: Item) -> Item:
    """
    ### Description
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item