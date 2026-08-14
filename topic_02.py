"""
    Path Parameters in FastAPI
    - This FastAPI application demonstrates the use of path parameters in defining endpoints.
    - Path parameters allow you to capture values from the URL path and use them in your endpoint functions.
    - The application defines a single endpoint that responds to GET requests at the URL pattern '/items/{item_id}'.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/items/{item_id}')          
async def read_item(item_id: int):      # Data Validation: item_id is expected to be an integer
    return {"item_id": item_id}