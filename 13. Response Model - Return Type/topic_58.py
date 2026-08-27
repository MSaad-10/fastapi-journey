"""
    INVALID Return Type ANNOTATIONS
    - An error will occur if you try to return a union between different types where one or more of them are not valid Pydantic types.
    - If you try to return some other types of objects which are not valid Pydantic type and you annotate in function, FastAPI try to create a Pydantic response model and fails.
"""


from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/portal')
async def get_portal(teleport: bool = False) -> Response | dict:    # Error
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}



"""
    DISABLE RESPONSE MODEL
    - From the above example, in case, you might what to keep the return type annotation in the function and get the support from tools like editors and type checkers (e.g. mypy).
    - In this case, you can disable the response model generation by setting 'response_model=None'.
    - This will make FastAPI skip the response model generation and that way you can have any return type annotations you need.
"""


from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return {"message": "Here's your interdimensional portal."}