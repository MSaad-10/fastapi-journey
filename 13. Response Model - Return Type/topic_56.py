"""
    Return Type AND DATA FILTERING
    - Like in previous example, we used two models UserIn and UserOut for input and output data, we can do the same with Data Filtering.
    -  A function can return more data than what is defined in the response model.
    - Classes and Inheritance can be used to:
        * Get better editor/type-checking support through function type annotations.
        * Still get FastAPI's automatic response data filtering.
"""


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None

class UserIn(BaseUser):     # Inheritance
    password: str

@app.post('/user/')
async def create_user(user: UserIn) -> BaseUser:
    return user