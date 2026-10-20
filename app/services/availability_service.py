from collections.abc import Mapping, Sequence
from datetime import date, datetime, time

from sqlalchemy.orm import Session

from app.models.availability import Availability
from app.repositories import availability_repository
from app.schemas.availability import AvailabilityCreate


class AvailabilityError(Exception):
    pass


class AvailabilityPermissionError(AvailabilityError):
    pass


class AvailabilityValidationError(AvailabilityError):
    pass


class AvailabilityOverlapError(AvailabilityError):
    pass


class AvailabilityNotFoundError(AvailabilityError):
    pass


def _check_overlap(
    existing_slots: Sequence[Availability],
    start_time: time,
    end_time: time,
) -> bool:
    for slot in existing_slots:
        if slot.status == "active":
            if start_time < slot.end_time and end_time > slot.start_time:
                return True
    return False


def create_availability(
    db: Session,
    data: AvailabilityCreate,
    current_user: Mapping[str, object],
) -> Availability:
    if current_user.get("role") != "admin":
        raise AvailabilityPermissionError("Solo los administradores pueden crear horarios")

    today = date.today()
    if data.date < today:
        raise AvailabilityValidationError("No se pueden crear horarios con fecha en el pasado")

    if data.start_time >= data.end_time:
        raise AvailabilityValidationError("La hora de inicio debe ser anterior a la hora de fin")

    now = datetime.now()
    if data.date == today and data.start_time <= now.time():
        raise AvailabilityValidationError("La hora de inicio del horario ya ha pasado")

    existing_slots = availability_repository.get_active_by_date(db, data.date)
    if _check_overlap(existing_slots, data.start_time, data.end_time):
        raise AvailabilityOverlapError("El horario se superpone con otro horario activo existente")

    availability = Availability(
        date=data.date,
        start_time=data.start_time,
        end_time=data.end_time,
        status="active",
        is_reserved=False,
    )
    return availability_repository.create(db, availability)


def list_available_slots(
    db: Session,
    target_date: date | None = None,
) -> Sequence[Availability]:
    return availability_repository.list_available(db, target_date=target_date)


def deactivate_availability(
    db: Session,
    availability_id: int,
    current_user: Mapping[str, object],
) -> Availability:
    if current_user.get("role") != "admin":
        raise AvailabilityPermissionError("Solo los administradores pueden desactivar horarios")

    slot = availability_repository.get_by_id(db, availability_id)
    if slot is None:
        raise AvailabilityNotFoundError("Horario no encontrado")

    return availability_repository.deactivate(db, slot)
