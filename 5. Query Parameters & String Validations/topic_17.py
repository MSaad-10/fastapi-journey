"""
    REQUIRED PARAMETERS
    - When we don't need to declare more validations or metadata, we can make a parameter required. 
    - A parameter can be made required just by not declaring a default value for it.
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str, Query(min_length=3)]):       # no default values
    item = {"items": [{"item_id": 123}, {"item_name": "Chocolate"}], 'q': q}
    return item



"""
    REQUIRED, CAN BE None
    - You can declare that a parameter can accept None, but that it's still required.
    - This would force clients to send a value, even if the value is None. 
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/required_none/')
async def read_item(q: Annotated[str | None, Query(min_length=3)]):
    item = {'items': [{'item_id': 456}, {'item_name': 'Light'}]}
    if q:
        item.update({'q': q})
    return item