"""
    FORM MODELS
    - You can use Pydantic models to declare form fields in FastAPI.
    - You just need to declare a Pydantic model with the fields you want to receive as form fields.
    - And then declare the parameter as Form.
"""


from fastapi import FastAPI, Form
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str

@app.post('/login/')
async def login(data: Annotated[FormData, Form()]):
    return data