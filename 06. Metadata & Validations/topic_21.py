"""
    DEPRECATING PARAMETERS
    - Let's say you created a parameter and you don't want it anymore.
    - You have to leave it there a while because there are clients using it.
    - But you want the docs to clearly show it as deprecated (obsolete, recommended not to use).
    - Then pass the parameter deprecated=True to Query.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/deprecated_param')
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias='query-item',
            title='Query-string',
            description='Query string for items to be searched in the database',
            min_length=3,
            max_length=50,
            pattern = "^fixedquery$",
            deprecated=True,
        )
    ] = None                # Optional
):
    item = {'items': [{'item_id': 423}, {'item_name': 'Car'}]}
    if q:
        item['q'] = q
    return item