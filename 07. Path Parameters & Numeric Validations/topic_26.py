"""
    ORDER THE PARAMETERS AS YOU NEED, TRICKS
    - If you want to:
        * declare the 'q' query parameter without a 'Query' nor any default value
        * declare the path parameter 'item_id' using 'Path'
        * have them in a different order
        * not use 'Annotated'
    - Pass '*' as the first parameter of the function.
        * It will know that all the following parameters should be called as kwargs (key-value pairs).
"""


from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    *,
    item_id: int = Path(title="The ID of the item to get"),    # Default = Path(...) & Required
    q: str                                                     # Required                                                                   
):
    item = {'item_id': item_id, 'q': q}
    return item



"""
    BETTER WITH 'Annotated'
    - Keep in mind that if you use 'Annotated', as you are not using function parameter default values.
    - You won't have this problem, and you probably won't need to use '*'.
"""


from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],   # Required
    q: str                                                              # Required
):
    item = {'item_id': item_id, 'q': q}
    return item