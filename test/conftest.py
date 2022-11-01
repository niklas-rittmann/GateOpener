from fastapi.testclient import TestClient
import main
import pytest


@pytest.fixture(scope="session")
def client() -> TestClient:
    return TestClient(main.app)
