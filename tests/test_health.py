from app.api.health import health


def test_health_check() -> None:
    assert health() == {"status": "ok"}
