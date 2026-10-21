from datetime import date, timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.repositories.availability_repository import list_available
from app.schemas.availability import AvailabilityCreate
from app.services.availability_service import (
    AvailabilityOverlapError,
    AvailabilityPermissionError,
    create_availability,
    deactivate_availability,
    list_available_slots,
)

engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
Base.metadata.create_all(engine)


def user(role: str, identifier: int) -> dict[str, object]:
    return {"sub": str(identifier), "role": role}


def slot_data(day_offset: int, start: str = "09:00", end: str = "10:00") -> AvailabilityCreate:
    return AvailabilityCreate(
        date=date.today() + timedelta(days=day_offset),
        start_time=start,
        end_time=end,
    )


def test_admin_can_create_and_list_availability() -> None:
    with Session(engine) as db:
        slot = create_availability(db, slot_data(5), user("admin", 1))
        available = list_available_slots(db, target_date=slot.date)
        assert slot.id in [item.id for item in available]
        assert slot.is_reserved is False


def test_client_cannot_create_availability() -> None:
    with Session(engine) as db:
        with pytest.raises(AvailabilityPermissionError):
            create_availability(db, slot_data(6), user("client", 2))


def test_overlapping_availability_is_rejected() -> None:
    with Session(engine) as db:
        create_availability(db, slot_data(7, "14:00", "16:00"), user("admin", 3))
        with pytest.raises(AvailabilityOverlapError):
            create_availability(db, slot_data(7, "15:00", "17:00"), user("admin", 3))


def test_admin_can_deactivate_availability() -> None:
    with Session(engine) as db:
        slot = create_availability(db, slot_data(8, "11:00", "12:00"), user("admin", 4))
        deactivated = deactivate_availability(db, slot.id, user("admin", 4))
        assert deactivated.status == "inactive"
        assert list_available(db, target_date=slot.date) == []


def test_past_availability_is_rejected_by_schema() -> None:
    with pytest.raises(ValueError):
        slot_data(-1)
