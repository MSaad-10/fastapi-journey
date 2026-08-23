"""
    REDEFINING A PATH OPERATION FUNCTION
    - You can redefine a path operation function in FastAPI by using the same path and HTTP method.
    - The return value of first path operation will be used in Swagger UI and OpenAPI documentation.
    - While the function name of second function will be used in Swagger UI.

    Test the application by changing the order of the two path operations.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/users')  
async def read_users_again():
    return ['Tom', 'Jerry']

@app.get('/users')
async def read_users():
    return ["Rick", "Morty"]