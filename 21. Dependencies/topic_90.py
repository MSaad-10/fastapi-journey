"""
    CREATE A DEPENDENCY, OR 'DEPENDABLE'
    - Let's first focus on the dependency.
    - It is just a function that can take all the same parameters that a path operation function can take.
"""


from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

async def common_parameters(
        q: str | None = None,
        skip: int = 0,
        limit: int = 100
):
    return {'q': q, 'skip': skip, 'limit': limit}

@app.get('/items/')
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons

@app.get('/users/')
async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
    return commons