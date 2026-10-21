from app.api.health import health


def test_health_check_function() -> None:
    assert health() == {"status": "ok"}


def test_health_check_contract() -> None:
    assert health() == {"status": "ok"}
