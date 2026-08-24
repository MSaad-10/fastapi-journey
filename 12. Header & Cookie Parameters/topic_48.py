"""
    Header PARAMETERS
    - You can define Header parameters the same way you define Query, Path and Cookie parameters.
    - You can define the default value as well as all the extra validation or annotation parameters.
    - To declare headers, you need to use Header, because otherwise the parameters would be interpreted as query parameters.
"""


from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(
    user_agent: Annotated[str | None, Header()] = None
):
    return {'User-Agent': user_agent}



"""
    AUTOMATIC CONVERSION
    - The standard headers are separated by a "hyphen" character, also known as the "minus symbol" (-).
    - But a variable like user-agent is invalid in Python.
    - So,  by default, Header will convert the parameter names characters from underscore (_) to hyphen (-) to extract and document the headers.
    - If you need to disable automatic conversion of underscores to hyphens, set the parameter convert_underscores of Header to False.
"""


from fastapi import FastAPI, Header
from typing import Annotated

app = FastAPI()

@app.get('/items/')
async def read_items(
    user_agent: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {'strange_header': user_agent}