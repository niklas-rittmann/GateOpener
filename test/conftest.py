import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm.session import Session

from opener import main
from opener.internal.auth import create_access_token
from opener.internal.database import engine


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(main.app)


@pytest.fixture(scope="session")
def token() -> dict[str, str]:
    token = create_access_token("tests")
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture(scope="session")
def db() -> Session:
    with Session(engine) as sess:
        yield sess
