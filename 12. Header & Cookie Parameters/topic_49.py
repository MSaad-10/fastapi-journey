"""
    DUPLICATE HEADERS
    - It is possible to receive duplicate headers. That means, the same header with multiple values.
    - You can define those cases using a list in the type declaration.
    - You will receive all the values from the duplicate header as a Python list.
"""


from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {'X-Token values': x_token}