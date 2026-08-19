""" Query AS THE DEFAULT VALUE OR IN Annotated """


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str, Query()] = 'Saad'):          # 'q' is required with default value 'Saad'
    return {'items': [{'item_id': 123}, {'item_name': 'Ball'}], 'q': q}


""" ADD MORE VALIDATIONS """


from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
    item = {'items': [{"item_id": 523}, {"item_name": "Clock"}]}
    if q:
        item['q'] = q
    return item