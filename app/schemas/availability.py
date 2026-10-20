from datetime import date, time

from pydantic import BaseModel, ConfigDict, model_validator


class AvailabilityCreate(BaseModel):
    date: date
    start_time: time
    end_time: time

    @model_validator(mode="after")
    def validate_times(self) -> "AvailabilityCreate":
        if self.start_time >= self.end_time:
            raise ValueError("La hora de inicio debe ser anterior a la hora de fin")
        if self.date < date.today():
            raise ValueError("No se pueden crear horarios con fecha en el pasado")
        return self


class AvailabilityResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date: date
    start_time: time
    end_time: time
    status: str
    is_reserved: bool
