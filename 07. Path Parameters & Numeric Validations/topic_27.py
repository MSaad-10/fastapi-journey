"""
    NUMBER VALIDATIONS: greater than or equal to
    - With Query and Path (and others you'll see later) you can declare number constraints.
"""


from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get.", ge=1)],    # Required
    q: str                                                                      # Required
):
    results = {'item_id': item_id}
    if q:                           # Does 'q' contain a truthy value (or, it contains " ")
        results['q'] = q 
    return results



"""
    NUMBER VALIDATIONS: greater than and less than or equal
    - The same applies for:
        * gt: greater than
        * le: less than or equal
"""


from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get.", gt=0, le=100)],     # Required
    q: str                                                                               # Required
):
    results = {'item_id': item_id}
    if q:                           
        results['q'] = q 
    return results