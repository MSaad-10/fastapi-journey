""" QUERY PARAMETERS & STRING VALIDATIONS """


from fastapi import FastAPI, Query
from typing import Annotated 

app = FastAPI()

@app.get('/items/')
async def read_items(q: Annotated [str | None, Query(max_length=50)] = None):   # 'q' can be optional or it can contain a string of length 50.
    results = {'items': [{'item_id': '123'}, {'item_id': 'Bar'}]}
    if q:
        results['q'] = q
    return results