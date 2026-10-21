from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health", status_code=200)
@router.get("/healt", status_code=200, include_in_schema=False)
def health() -> dict[str, str]:
    return {"status": "ok"}
