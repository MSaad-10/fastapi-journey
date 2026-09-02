"""
    GET CURRENT USER
    - In the previous example, the security system was giving the path operation function a token as a str.
    - But that is not useful. Let's make it give us the current user.
    - For that, create a Pydantic user model.
    - The same way we use Pydantic to declare bodies, we can use it anywhere else.
"""


from fastapi import FastAPI, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

app = FastAPI()

oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

class User(BaseModel):
    username: str
    email: EmailStr | None = None
    full_name: str | None = None
    disabled: bool | None = None

def fake_decode_token(token):
    return User(
        username = token + 'fakecoded',
        email = "john@gmail.com",
        full_name = "John Doe"  
    )

async def get_current_user(token: Annotated[str, Depends(oauth_scheme)]):
    user = fake_decode_token(token)
    return user

@app.get('/user/')
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user