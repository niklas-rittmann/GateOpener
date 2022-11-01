import pytest
from fastapi.testclient import TestClient

from opener import main


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(main.app)
