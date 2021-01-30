from typing import List

from fastapi import APIRouter, Depends

from app.database import SessionLocal
from .adapters import SQLStorage
from .services import AnimeListUseCase, Anime

router = APIRouter(
    prefix="/anime",
    tags=["anime"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_use_case(db = Depends(get_db)) -> AnimeListUseCase:
    return AnimeListUseCase(SQLStorage(db))


@router.get("/", response_model=List[Anime])
def anime(use_case=Depends(get_use_case)):
    return use_case.show_anime()
