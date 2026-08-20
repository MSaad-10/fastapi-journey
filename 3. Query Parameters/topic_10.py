"""
    MULTIPLE PATH & QUERY PARAMETERS
    - You can declare multiple path parameters and query parameters at the same time.
    - FastAPI will automatically detect which is which and will validate them accordingly.
    - Also, you don't need to declare them in any specific order.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update({'description': 'This is an amazing item that has a long description'})
    return item