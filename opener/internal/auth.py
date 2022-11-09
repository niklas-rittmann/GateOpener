from datetime import datetime, timedelta

from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic.main import BaseModel
from sqlalchemy.orm.session import Session

from opener.internal.database import User, get_db

SECRET_KEY = "050ac200bf94cbe14cd61e7353f5a21782912d3a978c7266a3173b0a793e6ace"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


INCORRECT_USERNAME_OR_PASSWORD = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Incorrect username or password",
    headers={"WWW-Authenticate": "Bearer"},
)


class UserInDB(BaseModel):
    username: str
    hashed_password: str

    class Config:
        orm_mode = True


def authenticate_user(db: Session, username: str, password: str) -> UserInDB:
    """Check if user exists in db and is a valid user"""
    user = get_user(db, username)
    if not verify_password(password, user.hashed_password):
        raise INCORRECT_USERNAME_OR_PASSWORD
    return user


def get_user(db: Session, username: str | None) -> UserInDB:
    """Fetch user from db"""
    user = db.query(User).filter(User.username == username).first()
    if user:
        return UserInDB.from_orm(user)
    raise INCORRECT_USERNAME_OR_PASSWORD


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check if the given password is the actual password"""
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(username: str) -> str:
    """Create a access token for the user"""
    data = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(days=7),
    }
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def check_current_user(
    db: Session = Depends(get_db), token: str | None = Depends(oauth2_scheme)
) -> UserInDB:
    """Check if the token matches a saved user"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise CREDENTIALS_EXCEPTION
    username = payload.get("sub")
    return get_user(db, username)
