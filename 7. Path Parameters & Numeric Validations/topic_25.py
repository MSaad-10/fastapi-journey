"""
    ORDER THE PARAMETERS AS YOU NEED
    - In python, a parameter with a default value cannot come before a parameter without a default value.  
    - But FastAPI doesn't care about the order.
        * FastAPI detects the parameters by their names, types and default declarations (Query, Path, etc). 
"""


# Without 'Annotated'
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    q: str,                                                     # Required
    item_id: int = Path(title="The ID of the item to get")      # Default value = Path(...) and Required
):
    results = {'item_id': item_id, 'q': q}
    return results



# With 'Annotated'
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],   # Required
    q: str                                                              # Required
):
    item = {'item_id': item_id, 'q': q}
    return item