"""
    DECLARE MORE METADATA
    - You can add more information about the parameter.
    - Information will be included in the generated OpenAPI & used by the documentation UIs & external tools.
"""


# You can add a 'title'
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/more_metadata_title/')
async def read_item(
    q: Annotated[
        str | None, 
        Query(
            title='Hello World',            # Title   
            min_length=3)] = None           # Default = None
):                     
    item = {"items": [{"item_id": 535}, {"item_name": "Bag"}]}
    if q:
        item['q'] = q
    return item



# You can also add a 'description'
from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/more_metadata_title_desc/')
async def read_item(
    q: Annotated[
        str | None, 
        Query(
            title='This is title',               # Title
            description='This is description',   # Description           
            min_length=3)] = None                # Default = None
):                     
    item = {"items": [{"item_id": 535}, {"item_name": "Bag"}]}
    if q:
        item['q'] = q
    return item