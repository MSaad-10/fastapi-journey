"""
    QUERY PARAMETER TYPE CONVERSION
    - Type conversion is automatically handled by FastAPI for query parameters.
    - You can declare the type of the query parameter in the function signature.
    - For instance, you can declare bool types, and they will be converted from strings to boolean values.
    - Test the following URLs:
        * http://127.0.0.1:8000/items/123?q=hello&short=true
        * http://127.0.0.1:8000/items/123?q=hello
        * http://127.0.0.1:8000/items/foo?short=1
        * http://127.0.0.1:8000/items/foo?short=0
        * http://127.0.0.1:8000/items/foo?short=True
        * http://127.0.0.1:8000/items/foo?short=False
        * http://127.0.0.1:8000/items/foo?short=true
        * http://127.0.0.1:8000/items/foo?short=false
        * http://127.0.0.1:8000/items/foo?short=on
        * http://127.0.0.1:8000/items/foo?short=off
        * http://127.0.0.1:8000/items/foo?short=yes
        * http://127.0.0.1:8000/items/foo?short=no
"""


from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):  # short: Query Parameter with default value and type conversion 
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': 'This is an amazing item that has a long description'})
    return item