from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.availability import router as availability_router
from app.api.health import router as health_router
from app.api.reservations import router as reservations_router

app = FastAPI(title="Tingo Reservas", version="0.1.0")
app.include_router(health_router)
app.include_router(auth_router)
app.include_router(availability_router)
app.include_router(reservations_router)
