from starlette.testclient import TestClient


def test_authenticate_user(client: TestClient) -> None:
    """Test that token is returned when authorized"""
    resp = client.post("/token", data={"username": "tests", "password": "test"})
    assert resp.status_code == 200
    assert "access_token" in resp.text


def test_refresh_token(client: TestClient, token: dict[str, str]) -> None:
    """Test that token refresh works"""
    resp = client.post("/refresh", headers=token)
    assert resp.status_code == 200
    assert "access_token" in resp.text
