"""
    OTHER Return Type ANNOTATIONS
    - There might be cases where you return something that is not a valid Pydantic field.
    - And you annotate it in the function, only to get the support provided by tooling (the editor, mypy, etc).

    RETURN A Response DIRECTLY
    - The most common case would be returning a Response directly.
    - FastAPI will handle it automatically because the return type annotation is the class or subclass of Response.
"""


from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

@app.get('/portal/')
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={'message': 'Here is your interdimensional portal.'})



"""
    ANNOTATE A RESPONSE SUBCLASS
    - You can also use a subclass of 'Response' in the type annotation.
    - This will also work because RedirectResponse is a subclass of Response, and FastAPI will automatically handle this simple case.
"""


from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/teleport')
async def get_teleport() -> RedirectResponse:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")