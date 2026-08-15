"""
    Query Parameters
    - Other function parameters that are not part of the path parameters are called Query Parameters.
    - Query parameters are defined in the function signature and can have default values.
    - The query is the set of key-value pairs that go after the '?' in a URL, separated by '&'.  
        * Example:          http://127.0.0.1:8000/items/?skip=0&limit=10
"""


from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):    # Query Parameters with default values
    return fake_items_db[skip : skip + limit]