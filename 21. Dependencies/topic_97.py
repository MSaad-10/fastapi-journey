"""
    DEPENDENCIES WITH yield AND HTTPException
    - You can use dependencies with yield and have try blocks that try to execute some code and then run some exit code after finally.
    - You can also use except to catch the exception that was raised and do something with it.
        * For example, you can raise a different exception, like HTTPException.
"""


from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()

data = {
    "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
    "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
}

class OwnerError(Exception):
    pass

def get_username():
    try:
        yield 'Rick'
    except OwnerError as e:
        raise HTTPException(status_code=404, detail=f"Owner error: {e}")

@app.get('/items/{item_id}')
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
    item = data[item_id]
    if item["owner"] != username:
        raise OwnerError(username)
    return item 