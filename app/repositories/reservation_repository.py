from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.reservation import Reservation


def create(db: Session, reservation: Reservation) -> Reservation:
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


def get_by_id(db: Session, reservation_id: int) -> Reservation | None:
    return db.get(Reservation, reservation_id)


def list_by_user(db: Session, user_id: int) -> Sequence[Reservation]:
    return db.scalars(
        select(Reservation)
        .where(Reservation.user_id == user_id)
        .order_by(Reservation.created_at.desc())
    ).all()


def get_active_by_availability(db: Session, availability_id: int) -> Reservation | None:
    return db.scalar(
        select(Reservation).where(
            Reservation.availability_id == availability_id,
            Reservation.status == "confirmed",
        )
    )
