from datetime import date, time, timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.availability import Availability
from app.schemas.availability import AvailabilityCreate
from app.services.availability_service import (
    AvailabilityNotFoundError,
    AvailabilityOverlapError,
    AvailabilityPermissionError,
    create_availability,
    deactivate_availability,
    list_available_slots,
)


def make_session() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_create_availability_success() -> None:
    db = make_session()
    admin_user = {"sub": "1", "role": "admin"}
    future_date = date.today() + timedelta(days=2)

    data = AvailabilityCreate(
        date=future_date,
        start_time=time(10, 0),
        end_time=time(11, 0),
    )
    slot = create_availability(db, data, admin_user)

    assert slot.id is not None
    assert slot.date == future_date
    assert slot.start_time == time(10, 0)
    assert slot.end_time == time(11, 0)
    assert slot.status == "active"
    assert not slot.is_reserved


def test_reject_non_admin_creation() -> None:
    db = make_session()
    client_user = {"sub": "2", "role": "client"}
    future_date = date.today() + timedelta(days=2)

    data = AvailabilityCreate(
        date=future_date,
        start_time=time(10, 0),
        end_time=time(11, 0),
    )
    with pytest.raises(AvailabilityPermissionError, match="Solo los administradores"):
        create_availability(db, data, client_user)


def test_reject_past_date() -> None:
    past_date = date.today() - timedelta(days=1)

    with pytest.raises(ValueError, match="pasado"):
        AvailabilityCreate(
            date=past_date,
            start_time=time(10, 0),
            end_time=time(11, 0),
        )


def test_reject_invalid_time_range() -> None:
    future_date = date.today() + timedelta(days=2)
    with pytest.raises(ValueError, match="anterior"):
        AvailabilityCreate(
            date=future_date,
            start_time=time(12, 0),
            end_time=time(10, 0),
        )


def test_reject_overlapping_schedules() -> None:
    db = make_session()
    admin_user = {"sub": "1", "role": "admin"}
    target_date = date.today() + timedelta(days=3)

    slot1 = AvailabilityCreate(
        date=target_date,
        start_time=time(9, 0),
        end_time=time(11, 0),
    )
    create_availability(db, slot1, admin_user)

    # Superposición parcial
    slot2 = AvailabilityCreate(
        date=target_date,
        start_time=time(10, 0),
        end_time=time(12, 0),
    )
    with pytest.raises(AvailabilityOverlapError, match="superpone"):
        create_availability(db, slot2, admin_user)

    # Superposición interna
    slot3 = AvailabilityCreate(
        date=target_date,
        start_time=time(9, 30),
        end_time=time(10, 30),
    )
    with pytest.raises(AvailabilityOverlapError, match="superpone"):
        create_availability(db, slot3, admin_user)


def test_allow_consecutive_schedules() -> None:
    db = make_session()
    admin_user = {"sub": "1", "role": "admin"}
    target_date = date.today() + timedelta(days=3)

    slot1 = AvailabilityCreate(
        date=target_date,
        start_time=time(9, 0),
        end_time=time(10, 0),
    )
    create_availability(db, slot1, admin_user)

    slot2 = AvailabilityCreate(
        date=target_date,
        start_time=time(10, 0),
        end_time=time(11, 0),
    )
    res2 = create_availability(db, slot2, admin_user)
    assert res2.id is not None


def test_list_only_active_and_unreserved_slots() -> None:
    db = make_session()
    target_date = date.today() + timedelta(days=4)

    # Uno activo libre
    s1 = Availability(
        date=target_date,
        start_time=time(9, 0),
        end_time=time(10, 0),
        status="active",
        is_reserved=False,
    )
    # Uno activo reservado
    s2 = Availability(
        date=target_date,
        start_time=time(10, 0),
        end_time=time(11, 0),
        status="active",
        is_reserved=True,
    )
    # Uno inactivo
    s3 = Availability(
        date=target_date,
        start_time=time(11, 0),
        end_time=time(12, 0),
        status="inactive",
        is_reserved=False,
    )
    db.add_all([s1, s2, s3])
    db.commit()

    slots = list_available_slots(db, target_date=target_date)
    assert len(slots) == 1
    assert slots[0].start_time == time(9, 0)


def test_deactivate_availability_success() -> None:
    db = make_session()
    admin_user = {"sub": "1", "role": "admin"}
    target_date = date.today() + timedelta(days=5)

    created = create_availability(
        db,
        AvailabilityCreate(date=target_date, start_time=time(14, 0), end_time=time(15, 0)),
        admin_user,
    )

    deactivated = deactivate_availability(db, created.id, admin_user)
    assert deactivated.status == "inactive"
    assert deactivated.id == created.id

    # Comprobar que persiste en BD para historial
    persisted = db.get(Availability, created.id)
    assert persisted is not None
    assert persisted.status == "inactive"

    # Y no aparece en consulta de disponibles
    available = list_available_slots(db, target_date=target_date)
    assert len(available) == 0


def test_deactivate_not_found_or_non_admin() -> None:
    db = make_session()
    admin_user = {"sub": "1", "role": "admin"}
    client_user = {"sub": "2", "role": "client"}

    with pytest.raises(AvailabilityPermissionError):
        deactivate_availability(db, 999, client_user)

    with pytest.raises(AvailabilityNotFoundError):
        deactivate_availability(db, 999, admin_user)
