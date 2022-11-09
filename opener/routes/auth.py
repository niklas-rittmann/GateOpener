from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from pydantic.main import BaseModel
from sqlalchemy.orm.session import Session

from opener.internal.auth import (
    authenticate_user,
    check_current_user,
    create_access_token,
)
from opener.internal.database import get_db

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/token", response_model=Token)
async def authenticate(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """Authenticate to create user token"""
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(user.username)
    return Token(access_token=access_token)


@router.post("/refresh", response_model=Token)
async def refresh(User=Depends(check_current_user)):
    """Refresh user token"""
    access_token = create_access_token(User.username)
    return Token(access_token=access_token)
