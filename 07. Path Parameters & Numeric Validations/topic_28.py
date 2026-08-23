"""
    NUMBER VALIDATIONS: floats, greater than and less than
    - Number validations also work for float values.
    - The float values require when we have to use decimal values.
    - For Example, a value must be greater than 0, even if it is less than 1.
        * So, in case of floats 0.5 would be a valid value. But 0.0 or 0 would not.
"""


from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)]
):
    results = {'item_id': item_id, 'size': size}
    if q:
        results.update({'q': q})
    return results