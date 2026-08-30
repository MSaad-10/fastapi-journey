"""
    Summary AND Description
    - You can add a summary and description.
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
        "/items/", 
        tags=["Items"],
        summary='Create an item',
        description='Create an item with all the information, name, description, price, tax and a set of unique tags',
)
async def create_item(item: Item) -> Item:
    return item



"""
    Description FROM docstring
    - As descriptions tend to be long and cover multiple lines.
    - You can declare the path operation description in the function docstring and FastAPI will read it from there.
    - You can write Markdown in the docstring, it will be interpreted and displayed correctly.
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

@app.post('/items/', tags=["Item"], summary='Create an item')
async def create_item(item: Item) -> Item:
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item