"""
    REQUIRED QUERY PARAMETERS
    - You can declare query parameters as required by simply not providing a default value.
    - In this case, FastAPI will consider the query parameter as required and will raise an error if it is not provided in the request.
"""


# from fastapi import FastAPI
# app = FastAPI()

# @app.get('/items/{item_id}')
# async def read_user_item(item_id: str, needy: str):     # 'needy' is a required query parameter.
#     item = {'item_id': item_id, 'needy': needy}
#     return item


"""
    - You can also declare other parameters alongside the required query parameters.
    - You can define some parameters as required, some as having a default value, and some entirely optional.
"""

from fastapi import FastAPI
app = FastAPI()

@app.get('/items/{item_id}')
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {'item_id': item_id}
    item['needy'] = needy
    item['skip'] = skip
    item['limit'] = limit
    return item