""" 
    ADD REGULAR EXPRESSIONS
    - You can define a regular expression pattern that the parameter should match. 
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = None):  # 'q' must be 'fixedquery'  
    item = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        item['q'] = q
    return item


"""
    DEFAULT VALUES
    - Having a default value of any type, including 'None', makes the parameter optional (not required).
"""


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str, Query(min_length=3)] = 'defaultquery'):      # default = 'defaultquery' but can be changed
    item = {"items": [{"item_id": 123}, {"item_name": "Car"}], 'q': q}
    return item