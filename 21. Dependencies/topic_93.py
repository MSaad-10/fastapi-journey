"""
    SUB-DEPENDENCIES
    - You can create dependencies that have sub-dependencies.
    - They can be as deep as you need them to be.

    FIRST DEPENDENCY "DEPENDABLE"
    - You could create a first dependency ("dependable") like:
"""


from fastapi import FastAPI, Depends, Cookie
from typing import Annotated

app = FastAPI()

def query_extractor(q: str | None = None):
    return q

def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[str | None, Cookie()] = None,
):
    if not q:
        return last_query
    return q

@app.get('/items/')
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
    return {'q_or_cookie': query_or_default}