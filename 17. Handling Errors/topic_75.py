"""
    HANDLING ERRORS
    - There are many situations in which you need to report an error to a client that is using your API.
    - In these cases, you would normally return an HTTP status code in the range of 400 (from 400 to 499).
    - To return HTTP responses with errors to the client you use HTTPException.
"""


from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return {'item': items[item_id]}