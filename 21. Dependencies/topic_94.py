"""
    ADD dependencies TO THE PATH OPERATION DECORATOR
    - The path operation decorator receives an optional argument dependencies.
    - It should be a list of Depends().
"""


from fastapi import FastAPI, Header, Depends, HTTPException
from typing import Annotated

app = FastAPI()

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=404, detail='X-Token header invalid')

async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=404, detail="X-Key header invalid")
    return x_key        # won't be used

@app.get('/items/', dependencies=[Depends(verify_key), Depends(verify_token)])
async def read_items():
    return {'item_id': 'ID_101'}