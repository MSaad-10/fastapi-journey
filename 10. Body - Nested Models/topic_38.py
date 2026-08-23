"""
    NESTED MODELS
    - Each attribute of a Pydantic model has a type.
    - But that type can itself be another Pydantic model.
    - So, you can declare deeply nested JSON "objects" with specific attribute names, types and validations
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}



"""
    SPECIAL TYPES AND VALIDATION
    - Apart from normal singular types like str, int, float, etc. you can use more complex singular types that inherit from str.
    - For example, as in the Image model we have a url field.
"""


from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl            # Special type for URLs
    name: str

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    return {'item_id': item_id, 'item': item}