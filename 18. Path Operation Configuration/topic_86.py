"""
    DEPCREATE A PATH OPERATION
    - If you need to mark a path operation as deprecated, but without removing it.
    - You can pass the 'deprecated' parameter in path operation decorator.
"""


from fastapi import FastAPI

app = FastAPI()

@app.get(
        "/items/", 
        tags=["Items"]
)
async def read_items():
    return [{"name": "Mobile", "price": 42}]

@app.get(
        "/users/",
        tags=["Users"]
)
async def read_users():
    return [{"username": "msaad"}]

@app.get(
        "/elements/",
        tags=["Elements"],
        deprecated=True
)
async def read_elements():
    return [{"element_name": "Hydrogen"}]