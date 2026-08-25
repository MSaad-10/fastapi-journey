"""
    Cookie PARAMETER MODELS
    - If you have a group of cookies that are related, you can create a Pydantic model to declare them.
    - Declare the cookie parameters that you need in a Pydantic model, and then declare the parameter as Cookie.
    - FastAPI will extract the data for each field from the cookies received in the request and give you the Pydantic model you defined.
"""


from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

@app.get('/items/')
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies



"""
    FORBID EXTRA Cookies
    - In some cases, you might want to restrict the cookies that you want to receive.
    - You can use Pydantic's model configuration to forbid any extra fields.
    - If a client tries to send some extra cookies, they will receive an error response.
"""


from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class Cookies(BaseModel):
    model_config = {'extra': 'forbid'}
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None

@app.get('/items/')
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies