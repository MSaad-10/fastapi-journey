"""
    Optional Query Parameters
    - Query Paramaters can also be optional as they can have default values.
    - You can declare optional parameters, by setting their default value to None.
    - If the parameter is not provided in the request, it will be set to None.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None):    # q: Optional Query Parameter
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    return result