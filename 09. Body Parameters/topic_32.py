"""
    MULTIPLE BODY PARAMETERS
    - In the previous example, the path operations would expect a JSON body with the attributes of an 'Item'.
    - You can also declare multiple body parameters e.g. 'item' and 'user'.
    - In this case, FastAPI will notice that there are more than one body parameters in the function.
    - So, it will then use the parameter names as keys (field names) in the body.
"""


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None      # Optional
    price: float
    tax: float | None = None            # Optional

class User(BaseModel):
    username: str
    full_name: str | None = None        # Optional

@app.put('/items/{item_id}')
async def update_item(
    item_id: int,
    item: Item,
    user: User
):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results