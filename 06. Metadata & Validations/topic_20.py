"""
    alias PARAMETER
    - Imagine that you want the parameter to be item-query.
    - But item-query is not a valid Python variable name.
    - But you still need it to be exactly item-query.
    - Then you can declare an alias, and that alias is what will be used to find the parameter value
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/alias_param/')
async def read_items(q: Annotated[str | None, Query(alias='item-query')] = None):  # q (item-query) is Optional
    item = {'items': [{'item_id': 342}, {'item_name': 'Watch'}]}
    if q:
        item['q'] = q
    return item