"""
    Order Matters
    - In FastAPI, the order of path operations matters. 
    - The path operations are evaluated in the order they are defined in the code.
    - The first matching path operation will be executed, so more specific paths should be defined before more general ones.

    Test the application by changing the order of the path operations and observing the behavior when accessing the endpoints.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/users/me')           # More specific path
async def read_user_me():
    return {"user_id": "the current user"}

@app.get('/users/{user_id}')    # More general path
async def read_user(user_id: str):
    return {"user_id": user_id}