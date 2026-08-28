"""
    INSTALL CUSTOM EXCEPTION HANDLERS
    - You can add custom exception handlers with the same exception utilities from Starlette.
    - Let's say you have a custom exception UnicornException that you might raise.
    - And you want to handle this exception globally with FastAPI.
    - You could add a custom exception handler with @app.exception_handler().
"""


from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={'message': f'Oops! {exc.name} did something. There goes a rainbow...'},
    )

@app.get('/unicorn/{name}')
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {'unicorn_name': name}