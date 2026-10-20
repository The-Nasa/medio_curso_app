from collections.abc import Sequence
from datetime import date

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.availability import Availability


def create(db: Session, availability: Availability) -> Availability:
    db.add(availability)
    db.commit()
    db.refresh(availability)
    return availability


def get_by_id(db: Session, availability_id: int) -> Availability | None:
    return db.scalar(select(Availability).where(Availability.id == availability_id))


def get_active_by_date(db: Session, target_date: date) -> Sequence[Availability]:
    stmt = (
        select(Availability)
        .where(Availability.date == target_date, Availability.status == "active")
        .order_by(Availability.start_time)
    )
    return db.scalars(stmt).all()


def list_available(db: Session, target_date: date | None = None) -> Sequence[Availability]:
    stmt = select(Availability).where(
        Availability.status == "active",
        Availability.is_reserved.is_(False),
    )
    if target_date is not None:
        stmt = stmt.where(Availability.date == target_date)
    stmt = stmt.order_by(Availability.date, Availability.start_time)
    return db.scalars(stmt).all()


def deactivate(db: Session, availability: Availability) -> Availability:
    availability.status = "inactive"
    db.commit()
    db.refresh(availability)
    return availability


def list_all(db: Session) -> Sequence[Availability]:
    return db.scalars(
        select(Availability).order_by(Availability.date, Availability.start_time)
    ).all()
