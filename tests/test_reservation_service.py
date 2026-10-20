from datetime import date, time

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.availability import Availability
from app.services.reservation_service import (
    ReservationConflictError,
    ReservationPermissionError,
    cancel_reservation,
    create_reservation,
)


def make_session() -> Session:
    engine = create_engine("sqlite://")
    Base.metadata.create_all(engine)
    return Session(engine)


def test_create_and_cancel_reservation_releases_slot() -> None:
    db = make_session()
    slot = Availability(date=date(2030, 1, 1), start_time=time(9), end_time=time(10))
    db.add(slot)
    db.commit()
    db.refresh(slot)

    reservation = create_reservation(db, slot, {"sub": "5", "role": "client"})
    cancelled = cancel_reservation(db, reservation, {"sub": "5"}, slot)

    assert reservation.user_id == 5
    assert cancelled.status == "cancelled"
    assert slot.is_reserved is False


def test_reserved_slot_is_rejected() -> None:
    db = make_session()
    slot = Availability(
        date=date(2030, 1, 1), start_time=time(9), end_time=time(10), is_reserved=True
    )

    try:
        create_reservation(db, slot, {"sub": "5"})
    except ReservationConflictError:
        pass
    else:
        raise AssertionError("Se esperaba ReservationConflictError")


def test_other_user_cannot_cancel_reservation() -> None:
    db = make_session()
    slot = Availability(date=date(2030, 1, 1), start_time=time(9), end_time=time(10))
    db.add(slot)
    db.commit()
    db.refresh(slot)
    reservation = create_reservation(db, slot, {"sub": "5"})

    try:
        cancel_reservation(db, reservation, {"sub": "9"}, slot)
    except ReservationPermissionError:
        pass
    else:
        raise AssertionError("Se esperaba ReservationPermissionError")
