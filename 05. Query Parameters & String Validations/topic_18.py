"""
    QUERY PARAMETER list/MULTIPLE VALUES
    - When you define a query parameter explicitly with Query you can also declare it to receive multiple values.
    - To declare a query parameter with a type of 'list', you need to explicitly use 'Query', otherwise it would be interpreted as a request body.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/multiple_values/')
async def read_items(q: Annotated[list[str] | None, Query()] = None):       # 'q' is Optional
    item = {'items': [{'item_id': 452}, {'item_name': 'Cookie'}]}
    if q:
        item['q'] = q
    return item



"""
    QUERY PARAMETER list/MULTIPLE VALUES WITH DEFAULTS
    - You can also define a default list of values if none are provided.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/multiple_values_default')
async def read_items(q: Annotated[list[str], Query()] = ['foo', 'bar']):     # 'q' has a default value = ['foo', 'bar']
    query_item = {'q': q}
    return query_item



"""
    USING JUST list
    - You can also use 'list' directly instead of 'list[str]'.
    - Keep in mind that in this case, FastAPI won't check the contents of the list.
        * Example: list[int] would check (and document) that the contents of the list are integers. But list alone wouldn't.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/just_list/')
async def read_items(q: Annotated[list, Query()] = []):     # 'q' has a Default value = []
    query_items = {'q': q}
    return query_items
