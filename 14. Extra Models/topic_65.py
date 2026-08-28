"""
    RESPONSE STATUS CODE
    - The same way you can specify a response model.
    - You can also declare the HTTP status code used for the response with the parameter status_code in any of the path operations:
        * @app.get()
        * @app.post()
        * @app.put()
        * @app.delete()
"""


from fastapi import FastAPI

app = FastAPI()

@app.post('/items/', status_code=201)
async def create_item(name: str):
    return {'name': name}



"""
    SHORTCUT TO REMEMBER THE NAMES
    - From the previous example, 201 is the status code for "Created".
    - But you don't have to memorize what each of these codes mean.
    - You can use the convenience variables from fastapi.status.
"""


from fastapi import FastAPI, status

app = FastAPI()

@app.post('/items/', status_code = status.HTTP_201_CREATED)
async def create_item(item_id: str):
    return {'item_id': item_id}