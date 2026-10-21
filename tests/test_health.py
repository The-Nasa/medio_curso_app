from app.api.health import health
from app.main import app


def test_health_check_function() -> None:
    assert health() == {"status": "ok"}


def test_health_check_contract() -> None:
    assert any(getattr(route, "path", None) == "/health" for route in app.routes)
    assert health() == {"status": "ok"}
