"""
    Header PARAMETER MODELS
    - If you have a group of header parameters that are related, you can create a Pydantic model to declare them.
    - Declare the header parameters that you need in a Pydantic model, and then declare the parameter as Header.
    - FastAPI will extract the data for each field from the headers in the request and give you the Pydantic model you defined.
"""


from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@app.get('/items/')
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers



"""
    FORBID EXTRA Headers
    - In some cases, you might want to restrict the headers that you want to receive.
    - You can use Pydantic's model configuration to forbid any extra fields.
    - If a client tries to send some extra headers, they will receive an error response.
"""


from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
    model_config = {'extra': 'forbid'}
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@app.get('/items/')
async def read_items(headers: Annotated[CommonHeaders, Header()]):
    return headers



"""
    DISABLE CONVERT UNDERSCORES
    - This conversion works the same way as with regular header parameters.
    - When you have underscore characters in the parameter names, they are automatically converted to hyphens.
    - If you have a header parameter save_data in the code, the expected HTTP header will be save-data, and it will show up like that in the docs.
    - This automatic conversion can be stopped by using 'convert_underscores=False' in Header().
"""


from fastapi import FastAPI, Header
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []

@app.get('/items/')
async def read_items(headers: Annotated[CommonHeaders, Header(convert_underscores=False)]):
    return headers