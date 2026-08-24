"""
    Cookie PARAMETERS
    - You can define Cookie parameters the same way you define Query and Path parameters.
    - You can define the default value as well as all the extra validation or annotation parameters.
    - To declare cookies, you need to use Cookie, because otherwise the parameters would be interpreted as query parameters.
"""


from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(
    ads_id: Annotated[str | None, Cookie()] = None
):
    return {'ads_id': ads_id}