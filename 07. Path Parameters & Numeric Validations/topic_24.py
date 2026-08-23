"""
    PATH PARAMETERS & NUMERIC VALIDATIONS
    - Like we declare validation and metadata for Query Parameters with 'Query'.
    - We can declare same type of validations & metadata for Path Parameters with 'Path'. 
"""


from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],   # Required
    q: Annotated[str | None, Query(alias='item-query')] = None,         # Optional
):
    results = {'item_id': item_id}
    if q:
        results['q'] = q
    return results