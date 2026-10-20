from collections.abc import Generator
from datetime import date, timedelta

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.security import create_access_token
from app.db.base import Base
from app.db.session import get_db
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
Base.metadata.create_all(engine)


def override_get_db() -> Generator[Session, None, None]:
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def get_auth_header(user_id: int, role: str) -> dict[str, str]:
    token = create_access_token(user_id=user_id, role=role)
    return {"Authorization": f"Bearer {token}"}


def test_api_create_availability_admin_success() -> None:
    headers = get_auth_header(1, "admin")
    target_date = str(date.today() + timedelta(days=5))
    response = client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "09:00:00", "end_time": "10:00:00"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] is not None
    assert data["date"] == target_date
    assert data["start_time"] == "09:00:00"
    assert data["end_time"] == "10:00:00"
    assert data["status"] == "active"
    assert data["is_reserved"] is False


def test_api_create_availability_client_forbidden() -> None:
    headers = get_auth_header(2, "client")
    target_date = str(date.today() + timedelta(days=5))
    response = client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "10:00:00", "end_time": "11:00:00"},
    )
    assert response.status_code == 403


def test_api_create_availability_unauthenticated() -> None:
    target_date = str(date.today() + timedelta(days=5))
    response = client.post(
        "/api/availability",
        json={"date": target_date, "start_time": "10:00:00", "end_time": "11:00:00"},
    )
    assert response.status_code == 401


def test_api_create_availability_past_date_rejected() -> None:
    headers = get_auth_header(1, "admin")
    past_date = str(date.today() - timedelta(days=1))
    response = client.post(
        "/api/availability",
        headers=headers,
        json={"date": past_date, "start_time": "10:00:00", "end_time": "11:00:00"},
    )
    assert response.status_code in (400, 422)


def test_api_create_availability_overlap_conflict() -> None:
    headers = get_auth_header(1, "admin")
    target_date = str(date.today() + timedelta(days=6))
    res1 = client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "14:00:00", "end_time": "16:00:00"},
    )
    assert res1.status_code == 201

    res2 = client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "15:00:00", "end_time": "17:00:00"},
    )
    assert res2.status_code == 409


def test_api_get_availability_public_and_filter() -> None:
    target_date = str(date.today() + timedelta(days=7))
    headers = get_auth_header(1, "admin")
    client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "08:00:00", "end_time": "09:00:00"},
    )

    response = client.get(f"/api/availability?date={target_date}")
    assert response.status_code == 200
    slots = response.json()
    assert len(slots) >= 1
    assert any(s["date"] == target_date and s["start_time"] == "08:00:00" for s in slots)


def test_api_deactivate_availability_admin() -> None:
    headers = get_auth_header(1, "admin")
    target_date = str(date.today() + timedelta(days=8))
    res = client.post(
        "/api/availability",
        headers=headers,
        json={"date": target_date, "start_time": "11:00:00", "end_time": "12:00:00"},
    )
    slot_id = res.json()["id"]

    # Desactivar
    deact_res = client.patch(f"/api/availability/{slot_id}/deactivate", headers=headers)
    assert deact_res.status_code == 200
    assert deact_res.json()["status"] == "inactive"

    # Verificar que ya no se muestra en lista de disponibles
    list_res = client.get(f"/api/availability?date={target_date}")
    assert not any(s["id"] == slot_id for s in list_res.json())


def test_api_deactivate_client_forbidden() -> None:
    admin_headers = get_auth_header(1, "admin")
    client_headers = get_auth_header(2, "client")
    target_date = str(date.today() + timedelta(days=9))
    res = client.post(
        "/api/availability",
        headers=admin_headers,
        json={"date": target_date, "start_time": "11:00:00", "end_time": "12:00:00"},
    )
    slot_id = res.json()["id"]

    deact_res = client.patch(f"/api/availability/{slot_id}/deactivate", headers=client_headers)
    assert deact_res.status_code == 403
