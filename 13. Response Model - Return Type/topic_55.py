"""
    ADD AN OUTPUT MODEL
    - You can create separate models for input and the output data.
    - Like from previous example, you can create an input model with the plaintext password and an output model without it.
"""


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Any

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

@app.post('/user/', response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user