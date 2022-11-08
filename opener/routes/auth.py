from datetime import datetime, timedelta

from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from opener.internal.auth import authenticate_user, create_access_token
from opener.internal.database import get_db

router = APIRouter(
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token")
async def authenticate(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    """Authenticate to create user token"""
    user = authenticate_user(db, form_data.username, form_data.password)
    access_token = create_access_token(
        data={
            "sub": user.username,
            "exp": datetime.utcnow() + timedelta(days=7),
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}
