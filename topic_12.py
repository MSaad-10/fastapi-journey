"""
    REQUEST BODY
    - When you need to send data from a client (let's say, a browser) to your API, you send it as a request body.
    - A request body is data sent by the client to your API. A response body is the data your API sends to the client.
    - Your API almost always has to send a response body.
        * But clients don't necessarily need to send request bodies all the time.
        * Sometimes they only request a path, maybe with some query parameters, but don't send a body.
    - To declare a request body, you use Pydantic models with all their power and benefits.
    - To send data, you should use one of: POST (the most common), PUT, DELETE or PATCH.
        * Sending a body with a GET request has an undefined behavior in the specifications.
        * Nevertheless, it is supported by FastAPI, only for very complex/extreme use cases.
"""


# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str                       # Required
#     description: str | None = None  # Optional
#     price: float                    # Required
#     tax: float | None = None        # Optional

# app = FastAPI()

# @app.post('/items/')
# async def create_item(item: Item):
#     return item


"""
    USE THE MODEL
    - Inside of the function, you can access all the attributes of the model object directly.
"""


from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict