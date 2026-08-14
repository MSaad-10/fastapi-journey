"""
    Basic FastAPI Application
    - A simple FastAPI application that returns a greeting message.
    - This application defines a single endpoint that responds to GET requests at the root URL ('/').
    - It uses async functions to handle requests, allowing for efficient handling of multiple requests concurrently.
"""


from fastapi import FastAPI
app = FastAPI()

@app.get('/async')          # Path Operator Decorator
async def hello_async():    # Path Operation Function (can be 'async' or 'sync')
    return {"message": "Hello, World! from async function"}     # Return Content (can be 'dict', 'list', 'str', 'int' or 'Pydantic model')


@app.get('/sync')
def hello_sync():                            
    return {"message": "Hello, World! from sync function"}