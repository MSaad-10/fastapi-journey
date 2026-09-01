"""
    CLASSES AS DEPENDENCIES
    - The dependency should be a "callable".
    - A "callable" in Python is anything that Python can "call" like a function.
    - A Python class is also a callable.
    - Then, in FastAPI, you could use a Python class as a dependency.
    - What FastAPI actually checks is that it is a "callable" (function, class or anything else) and the parameters defined.
"""


from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get('/items/')
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({'items': items})
    return response



"""
    Type Annotation VS Depends
    - Notice how we write CommonQueryParams twice in the above code:
    - There is no use of first CommonQueryParams in Annotated[...], FastAPI extracts the declared parameters and actually calls the class using the second CommonQueryParams in Depend(CommonQueryParams).
    - So, we can change with the following:
"""


from fastapi import FastAPI, Depends
from typing import Annotated, Any

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"}, 
    {"item_name": "Bar"}, 
    {"item_name": "Baz"}
]

class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get('/items/')
async def read_items(commons: Annotated[Any, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({'items': items})
    return response