"""
    SHARED "Annotated" DEPENDENCIES
    - In the previous example, you see that there's a tiny bit of code duplication.
    - When you need to use the common_parameters() dependency, you have to write the whole parameter with the type annotation and Depends().
    - But because we are using Annotated, we can store that Annotated value in a variable and use it in multiple places.
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

CommonDep = Annotated[dict, Depends(common_parameters)]

@app.get('/items/')
async def read_items(commons: CommonDep):
    return commons

@app.get('/users/')
async def read_users(commons: CommonDep):
    return commons