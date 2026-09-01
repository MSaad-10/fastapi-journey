"""
    EARLY EXIT AND scope
    - Normally the exit code of dependencies with yield is executed after the response is sent to the client.
    - But if you know that you won't need to use the dependency after returning from the path operation function.
    - You can use Depends(scope="function") to tell FastAPI that it should close the dependency after the path operation function returns, but before the response is sent.
    - You can also test the application by using Depends(scope='request') which closes the dependency after the path operation function returns, but after the response is sent.
    - If not specified and the dependency has yield, it will have a scope of "request" by default.
"""


from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

def get_username():
    try:
        yield "Rick"
    finally:
        print("Cleanup up before response is sent")

@app.get('/users/me', tags=['Get Users'])
def get_user_me(username: Annotated[str, Depends(get_username, scope='function')]):
    return username