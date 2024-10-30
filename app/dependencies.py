from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from app.models import User
from typing import Annotated

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

dep_token = Annotated[str, Depends(oauth2_scheme)]

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

dep_form_data = Annotated[OAuth2PasswordRequestForm, Depends()]

async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)]
):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

dep_current_active_user = Annotated[User, Depends(get_current_active_user)]