import pytest
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from opener.internal.auth import (
    authenticate_user,
    check_current_user,
    create_access_token,
    get_password_hash,
    get_user,
    verify_password,
)


def test_authenticate_user(db: Session) -> None:
    """Test user authentification works"""
    username = "tests"
    user = authenticate_user(db, username, "test")
    assert user.username == username


def test_authenticate_user_unknown(db: Session) -> None:
    """Test user authentification works"""
    username = "unknown"
    with pytest.raises(HTTPException):
        authenticate_user(db, username, "test")


def test_authenticate_user_wrong_pw(db: Session) -> None:
    """Test user authentification works"""
    username = "tests"
    password = "wrong"
    with pytest.raises(HTTPException):
        authenticate_user(db, username, password)


def test_get_user(db: Session) -> None:
    """Test valid user in db"""
    username = "tests"
    user = get_user(db, username)
    assert user.username == username


def test_user_unknown(db: Session) -> None:
    """Test valid user in db"""
    with pytest.raises(HTTPException):
        get_user(db, "unknown")


def test_get_password_hash() -> None:
    """Test password hash creation"""
    pass_one = get_password_hash("password")
    pass_two = get_password_hash("assword")
    assert pass_one != pass_two


def test_verify_password_true() -> None:
    """Test password verification true"""
    hashed = get_password_hash("password")
    assert verify_password("password", hashed)


def test_verify_password_false() -> None:
    """Test password verification false"""
    hashed = get_password_hash("password")
    assert not verify_password("assword", hashed)


def test_create_token() -> None:
    """Test token generation"""
    token = create_access_token("tests")
    assert len(token) == 124


async def test_check_current_user_invalid_token(db) -> None:
    """Test invalid token raises error"""
    with pytest.raises(HTTPException):
        await check_current_user(db=db, token="Nicht valide")


async def test_check_user_name_invalid(db) -> None:
    """Test invalid token raises error"""
    token = create_access_token("nicht in db")
    with pytest.raises(HTTPException):
        await check_current_user(db=db, token=token)
