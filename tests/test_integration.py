from datetime import date, timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.models.user import User
from app.repositories import reservation_repository
from app.repositories.availability_repository import get_by_id, list_available
from app.schemas.availability import AvailabilityCreate
from app.services.availability_service import create_availability
from app.services.reservation_service import (
    ReservationConflictError,
    cancel_reservation,
    create_reservation,
)

engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
Base.metadata.create_all(engine)


def make_user(db: Session, user_id: int, role: str) -> dict[str, object]:
    user = User(
        id=user_id,
        name=f"user-{user_id}",
        email=f"user-{user_id}@example.com",
        password_hash="test-hash",
        role=role,
    )
    db.add(user)
    db.flush()
    return {"sub": str(user_id), "role": role}


def test_complete_customer_reservation_flow() -> None:
    with Session(engine) as db:
        admin = make_user(db, 101, "admin")
        customer = make_user(db, 102, "client")
        slot = create_availability(
            db,
            AvailabilityCreate(
                date=date.today() + timedelta(days=20),
                start_time="09:00",
                end_time="10:00",
            ),
            admin,
        )
        assert slot in list_available(db, target_date=slot.date)

        reservation = create_reservation(db, slot, customer)
        assert slot.is_reserved is True
        assert reservation.user_id == 102
        assert get_by_id(db, slot.id).is_reserved is True

        with pytest.raises(ReservationConflictError):
            create_reservation(db, slot, customer)

        mine = reservation_repository.list_by_user(db, 102)
        assert [item.id for item in mine] == [reservation.id]

        cancelled = cancel_reservation(db, reservation, customer, slot)
        assert cancelled.status == "cancelled"
        assert slot.is_reserved is False
        assert slot in list_available(db, target_date=slot.date)


def test_customer_cannot_create_availability() -> None:
    with Session(engine) as db:
        customer = make_user(db, 103, "client")
        with pytest.raises(Exception, match="administrador"):
            create_availability(
                db,
                AvailabilityCreate(
                    date=date.today() + timedelta(days=21),
                    start_time="11:00",
                    end_time="12:00",
                ),
                customer,
            )
