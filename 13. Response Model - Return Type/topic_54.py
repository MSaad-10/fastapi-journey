"""
    RETURN THE SAME INPUT DATA
    - You can return the same data that you used in input field.
    - We can use a model to declare our input and the same model to declare our output.
"""


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None

# Don't do this in production
@app.post('/user/')
async def create_user(user: UserIn) -> UserIn:  # same model for input & output
    return user