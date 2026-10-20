from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.repositories import availability_repository, reservation_repository
from app.schemas.reservation import ReservationCreate, ReservationResponse
from app.services.reservation_service import (
    ReservationConflictError,
    ReservationNotFoundError,
    ReservationPermissionError,
    cancel_reservation,
    create_reservation,
    list_my_reservations,
)

router = APIRouter(prefix="/api/reservations", tags=["reservations"])


@router.post("", response_model=ReservationResponse, status_code=status.HTTP_201_CREATED)
def create_reservation_endpoint(
    data: ReservationCreate,
    db: Session = Depends(get_db),
    current_user: dict[str, object] = Depends(get_current_user),
) -> ReservationResponse:
    availability = availability_repository.get_by_id(db, data.availability_id)
    try:
        reservation = create_reservation(db, availability, current_user)
    except ReservationConflictError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc
    except ReservationPermissionError as exc:
        raise HTTPException(status_code=401, detail=str(exc)) from exc
    return ReservationResponse.model_validate(reservation)


@router.get("/me", response_model=list[ReservationResponse])
def get_my_reservations(
    db: Session = Depends(get_db),
    current_user: dict[str, object] = Depends(get_current_user),
) -> list[ReservationResponse]:
    reservations = list_my_reservations(db, current_user)
    return [ReservationResponse.model_validate(item) for item in reservations]


@router.delete("/{reservation_id}", response_model=ReservationResponse)
def cancel_reservation_endpoint(
    reservation_id: int,
    db: Session = Depends(get_db),
    current_user: dict[str, object] = Depends(get_current_user),
) -> ReservationResponse:
    reservation = reservation_repository.get_by_id(db, reservation_id)
    availability = (
        availability_repository.get_by_id(db, reservation.availability_id)
        if reservation is not None
        else None
    )
    try:
        result = cancel_reservation(db, reservation, current_user, availability)
    except ReservationNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ReservationPermissionError as exc:
        raise HTTPException(status_code=403, detail=str(exc)) from exc
    return ReservationResponse.model_validate(result)
