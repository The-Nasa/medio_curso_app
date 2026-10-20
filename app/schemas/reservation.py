from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReservationCreate(BaseModel):
    availability_id: int


class ReservationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    availability_id: int
    status: str
    created_at: datetime | None = None
    cancelled_at: datetime | None = None
