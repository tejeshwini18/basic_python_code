from fastapi.testclient import TestClient

from fastapi_app import app


client = TestClient(app)


def test_health_check():
    response = client.get("/health_check")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "good"
    assert data["message"] == "web server is fine"


def test_config_endpoint():
    response = client.get("/config")
    assert response.status_code == 200
    data = response.json()
    assert data["app_name"] == "My FastAPI App"
    assert data["admin_email"] == "admin@example.com"
    assert data["debug"] is True


def test_items_pagination_limit():
    response = client.get("/items?skip=0&limit=3")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 3


