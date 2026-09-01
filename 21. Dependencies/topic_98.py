"""
    DEPENDENCIES WITH yield AND except
    - If you catch an exception using except in a dependency with yield and you don't raise it again.
    - FastAPI won't be able to notice there was an exception, the same way that would happen with regular Python.
"""


from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield 'Rick'
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")

@app.get('/items/{id}', tags=['Get Item'])
def get_item(id: str, username: Annotated[str, Depends(get_username)]):
    if id == 'portal-gun':
        raise InternalError(f"The portal gun is too dangerous to be owned by {username}")
    if id != 'plumbus':
        raise HTTPException(status_code=404, detail="Item not found, there's only a plumbus here")
    return id



"""
    ALWAYS raise IN DEPENDENCIES WITH yield AND except
    - If you catch an exception in a dependency with yield.
    - Unless you are raising another HTTPException or similar, you should re-raise the original exception.
    - You can re-raise the same exception using raise.
"""


from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

class InternalError(Exception):
    pass

def get_username():
    try:
        yield 'Rick'
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")
        raise

@app.get('/items/{id}', tags=['Get Item'])
def get_item(id: str, username: Annotated[str, Depends(get_username)]):
    if id == 'portal-gun':
        raise InternalError(f"The portal gun is too dangerous to be owned by {username}")
    if id != 'plumbus':
        raise HTTPException(status_code=404, detail="Item not found, there's only a plumbus here")
    return id