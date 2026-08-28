"""
    FORBID REXTRA Form FIELDS
    - You can also restrict the form fields to only those declared in the Pydantic model and restrict any extra fields.
    - You can use Pydantic's model configuration to forbid any extra fields.
"""


from fastapi import FastAPI, Form
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

class FormData(BaseModel):
    username: str
    password: str
    model_config = {"extra": "forbid"}

@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data