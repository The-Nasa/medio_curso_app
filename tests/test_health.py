from fastapi.testclient import TestClient

from app.api.health import health
from app.main import app

client = TestClient(app)


def test_health_check_function() -> None:
    assert health() == {"status": "ok"}


def test_health_check_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
