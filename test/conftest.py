from fastapi.testclient import TestClient
from opener import main
import pytest


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(main.app)
