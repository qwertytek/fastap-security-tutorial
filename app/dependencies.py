from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.models import User
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

dep_token = Annotated[str, Depends(oauth2_scheme)]

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: dep_token):
    user = fake_decode_token(token)
    return user

dep_current_user = Annotated[User, Depends(get_current_user)]