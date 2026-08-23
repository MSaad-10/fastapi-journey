"""
    List FIELDS
    - You can define an attribute to be a subtype. For Example, a Python 'list'.
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None)
    price: float
    tax: float | None = None
    tags: list = []

@app.put('/items/item_id')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}



"""
    DECLARE A list WITH A TYPE PARAMETER
    - You can declare types that have type parameters (internal types), like list, dict, tuple.
    - For these we can pass the internal type(s) as "type parameters" using square brackets: [ and ].
                                        my_list:  list[str]
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None)
    price: float
    tax: float | None = None
    tags: list[str] = []

@app.put('/items/item_id')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}



"""
    set TYPES
    - But then we think about it, and realize that tags shouldn't repeat, they would probably be unique strings.
    - And Python has a special data type for sets of unique items, the set.
    - Then we can declare tags as a set of strings.
"""


from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None)
    price: float
    tax: float | None = None
    tags: set[str] = set()

@app.put('/items/item_id')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}