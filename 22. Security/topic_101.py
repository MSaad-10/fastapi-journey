"""
    SECURITY - FIRST STEPS
    - Let's imagine that you have your backend API in some domain.
    - And you have a frontend in another domain or in a different path of the same domain.
    - And you want to have a way for the frontend to authenticate with the backend, using a username and password.
    - We can use OAuth2 to build that with FastAPI.
"""


from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/items/')
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'token': token}