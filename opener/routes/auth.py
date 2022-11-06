from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

from opener.internal.auth import authenticate_user, create_access_token, fake_users_db

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    """Authenticate to create user token"""
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "exp": datetime.utcnow() + timedelta(days=7),
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}
