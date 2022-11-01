from starlette.testclient import TestClient


def test_index_endpoint(client: TestClient) -> None:
    """Test the index enpoint returns template file and status code"""
    resp = client.get("/")
    assert resp.status_code == 200
    assert "<!DOCTYPE html>" in resp.text


def test_trigger_endpoint_valid_input(client: TestClient) -> None:
    """Test the trigger endpoint"""
    resp = client.post("/", json={"action": "trigger"})
    assert resp.status_code == 200
    assert "trigger" in resp.text


def test_trigger_endpoint_invalid_input(client: TestClient) -> None:
    """Test the trigger endpoint with invalid input"""
    resp = client.post("/")
    assert resp.status_code != 200
