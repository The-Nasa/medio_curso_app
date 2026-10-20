from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_current_user
from app.db.session import get_db
from app.schemas.availability import AvailabilityCreate, AvailabilityResponse
from app.services.availability_service import (
    AvailabilityNotFoundError,
    AvailabilityOverlapError,
    AvailabilityPermissionError,
    AvailabilityValidationError,
    create_availability,
    deactivate_availability,
    list_available_slots,
)

router = APIRouter(prefix="/api/availability", tags=["availability"])


@router.get("", response_model=list[AvailabilityResponse])
def get_availability(
    target_date: date | None = Query(default=None, alias="date"),
    db: Session = Depends(get_db),
) -> list[AvailabilityResponse]:
    slots = list_available_slots(db, target_date=target_date)
    return [AvailabilityResponse.model_validate(slot) for slot in slots]


@router.post("", response_model=AvailabilityResponse, status_code=status.HTTP_201_CREATED)
def create_availability_endpoint(
    data: AvailabilityCreate,
    db: Session = Depends(get_db),
    current_user: dict[str, object] = Depends(get_current_user),
) -> AvailabilityResponse:
    try:
        slot = create_availability(db, data, current_user)
    except AvailabilityPermissionError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except AvailabilityOverlapError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    except AvailabilityValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    return AvailabilityResponse.model_validate(slot)


@router.patch("/{availability_id}/deactivate", response_model=AvailabilityResponse)
@router.post("/{availability_id}/deactivate", response_model=AvailabilityResponse)
def deactivate_availability_endpoint(
    availability_id: int,
    db: Session = Depends(get_db),
    current_user: dict[str, object] = Depends(get_current_user),
) -> AvailabilityResponse:
    try:
        slot = deactivate_availability(db, availability_id, current_user)
    except AvailabilityPermissionError as exc:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(exc)) from exc
    except AvailabilityNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return AvailabilityResponse.model_validate(slot)
