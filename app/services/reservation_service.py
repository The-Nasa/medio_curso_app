from collections.abc import Mapping, Sequence
from datetime import UTC, datetime

from sqlalchemy.orm import Session

from app.models.availability import Availability
from app.models.reservation import Reservation
from app.repositories import reservation_repository


class ReservationError(Exception):
    pass


class ReservationPermissionError(ReservationError):
    pass


class ReservationConflictError(ReservationError):
    pass


class ReservationNotFoundError(ReservationError):
    pass


def _user_id(current_user: Mapping[str, object]) -> int:
    try:
        return int(str(current_user["sub"]))
    except (KeyError, TypeError, ValueError) as exc:
        raise ReservationPermissionError("Usuario no autenticado") from exc


def create_reservation(
    db: Session,
    availability: Availability | None,
    current_user: Mapping[str, object],
) -> Reservation:
    if availability is None or availability.status != "active" or availability.is_reserved:
        raise ReservationConflictError("El horario no está disponible")
    reservation = Reservation(user_id=_user_id(current_user), availability_id=availability.id)
    availability.is_reserved = True
    db.add(reservation)
    db.commit()
    db.refresh(reservation)
    return reservation


def list_my_reservations(db: Session, current_user: Mapping[str, object]) -> Sequence[Reservation]:
    return reservation_repository.list_by_user(db, _user_id(current_user))


def cancel_reservation(
    db: Session,
    reservation: Reservation | None,
    current_user: Mapping[str, object],
    availability: Availability | None,
) -> Reservation:
    if reservation is None:
        raise ReservationNotFoundError("Reserva no encontrada")
    if reservation.user_id != _user_id(current_user):
        raise ReservationPermissionError("No puedes cancelar esta reserva")
    if reservation.status == "cancelled":
        return reservation
    reservation.status = "cancelled"
    reservation.cancelled_at = datetime.now(UTC)
    if availability is not None:
        availability.is_reserved = False
    db.commit()
    db.refresh(reservation)
    return reservation
