"""
    CUSTOM VALIDATION
    - There could be cases where you need to do some custom validation that can't be done with the other parameters.
    - In those cases, you can use a custom validator function that is applied after the normal validation (e.g. str)
    - You can achieve that using Pydantic's 'AfterValidator' inside of 'Annotated'.
"""


import random
from typing import Annotated
from fastapi import FastAPI
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(id: str):
    if not id.startswith(('isbn-', 'imdb-')):       # .startswith() can take tuple and check each value in tuple.
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id

@app.get('/items/')
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,   # Optional
):
    if id:
        item = data.get(id)
    else:
        id, item = random.choice(list(data.items()))
    return {'id': id, 'name': item}